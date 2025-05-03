#!/usr/bin/env python3
"""
PocketFlow Framework Demo

This script demonstrates the key features of the PocketFlow framework
with practical examples including:
- Basic node connections and flow execution
- Conditional branching
- Retry mechanisms
- Batch processing
- Async operations
- Shared context
- Custom node types
- Error handling
"""

import asyncio
import warnings
import copy
import time
import random
from typing import Dict, List, Any, Optional, Union, Tuple

from pathlib import Path
import click

from util_log import get_logger, set_log_level, configure_logging

logger = get_logger("demo-zinets")

LOG_LEVEL = "DEBUG"   # For detailed logging during development
# # "WARNING"           # Or for minimal output in production
# set_log_level(LOG_LEVEL)      

LOG_FILE = Path(__file__).name + ".log"

# Or completely customize the logging setup
configure_logging(
    level=LOG_LEVEL,
    format_str='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
    log_file=LOG_FILE  # Also log to a file
)

LINE_BREAK = 100*"="

class BaseNode:
    """
    Base class for all nodes in the flow framework.
    
    Provides core functionality for node connections, parameter management,
    and execution flow.
    """
    
    def __init__(self):
        """Initialize a node with empty params and successors dictionaries."""
        self.params = {}
        self.successors = {}
    
    def set_params(self, params):
        """Set the parameters for this node."""
        self.params = params
        return self  # For method chaining
    
    def next(self, node, action="default"):
        """
        Connect this node to another node with a specific action.
        
        Args:
            node: The successor node to connect to
            action: The action name that triggers this connection
            
        Returns:
            The successor node for easy chaining
        """
        self.successors[action] = node
        return node
    
    def prep(self, shared):
        """
        Prepare node for execution.
        
        Args:
            shared: Shared context data
            
        Returns:
            Preparation results to be passed to exec
        """
        pass
    
    def exec(self, prep_res):
        """
        Execute node logic.
        
        Args:
            prep_res: Results from the prep stage
            
        Returns:
            Execution results
        """
        pass
    
    def _exec(self, prep_res):
        """Internal method to execute the node logic."""
        return self.exec(prep_res)
    
    def post(self, shared, prep_res, exec_res):
        """
        Post-processing after execution.
        
        Args:
            shared: Shared context data
            prep_res: Results from the prep stage
            exec_res: Results from the exec stage
            
        Returns:
            Final results after post-processing
        """
        pass
    

    
    def _run(self, shared):
        """
        Internal method to run the full node execution cycle.
        
        Args:
            shared: Shared context data
            
        Returns:
            Results after the full execution cycle
        """
        p = self.prep(shared)
        e = self._exec(p)
        return self.post(shared, p, e)
    
    def run(self, shared):
        """
        Public method to run this node.
        
        Args:
            shared: Shared context data
            
        Returns:
            Results after execution
        """
        if self.successors:
            warnings.warn("Node won't run successors. Use Flow.")
        return self._run(shared)
    
    def __rshift__(self, other):
        """Override >> operator for creating node connections."""
        return self.next(other)
    
    def __sub__(self, action):
        """
        Override - operator for conditional transitions.
        
        Args:
            action: The action name as a string
            
        Returns:
            ConditionalTransition object
            
        Raises:
            TypeError: If action is not a string
        """
        if isinstance(action, str):
            return _ConditionalTransition(self, action)
        raise TypeError("Action must be a string")


class _ConditionalTransition:
    """
    Helper class for conditional transitions between nodes.
    
    Used to create connections with specific action names.
    """
    
    def __init__(self, src, action):
        """
        Initialize a conditional transition.
        
        Args:
            src: Source node
            action: Action name
        """
        self.src = src
        self.action = action
    
    def __rshift__(self, tgt):
        """
        Override >> operator to complete the conditional connection.
        
        Args:
            tgt: Target node
            
        Returns:
            Target node
        """
        return self.src.next(tgt, self.action)


class Node(BaseNode):
    """
    Standard node with retry functionality.
    
    Extends BaseNode with the ability to retry execution on failure.
    """
    
    def __init__(self, max_retries=1, wait=0):
        """
        Initialize a node with retry capabilities.
        
        Args:
            max_retries: Maximum number of execution attempts
            wait: Time to wait between retries in seconds
        """
        super().__init__()
        self.max_retries = max_retries
        self.wait = wait
    
    def exec_fallback(self, prep_res, exc):
        """
        Fallback method called when all retries are exhausted.
        
        Args:
            prep_res: Results from preparation
            exc: The exception that caused the failure
            
        Raises:
            The exception by default
        """
        raise exc
    
    def _exec(self, prep_res):
        """
        Internal execution with retry logic.
        
        Args:
            prep_res: Results from preparation
            
        Returns:
            Execution results or fallback results
        """
        for self.cur_retry in range(self.max_retries):
            try:
                return self.exec(prep_res)
            except Exception as e:
                if self.cur_retry == self.max_retries - 1:
                    return self.exec_fallback(prep_res, e)
                if self.wait > 0:
                    time.sleep(self.wait)


class BatchNode(Node):
    """
    Node that processes a batch of items.
    
    Applies the node's execution logic to each item in a batch.
    """
    
    def _exec(self, items):
        """Execute the node logic on each item in the batch."""
        logger.debug(f"BatchNode._exec received {len(items) if items else 0} items")
        results = []
        
        for item in (items or []):
            try:
                result = self.exec(item)
                logger.debug(f"Processed batch item: {item.get('id', 'unknown')}, result: {result}")
                results.append(result)
            except Exception as e:
                logger.debug(f"Error processing batch item: {e}")
        
        logger.debug(f"BatchNode._exec completed with {results} results")
        return results


class Flow(BaseNode):
    """
    Orchestrates execution of multiple connected nodes.
    
    Manages the flow of execution from a starting node through its successors.
    """
    
    def __init__(self, start=None):
        """
        Initialize a flow with an optional starting node.
        
        Args:
            start: The starting node of the flow
        """
        super().__init__()
        self.start_node = start
    
    def start(self, start):
        """
        Set the starting node for this flow.
        
        Args:
            start: The node to set as the starting point
            
        Returns:
            The starting node for chaining
        """
        self.start_node = start
        return start
    
    def get_next_node(self, curr, action):
        """
        Find the next node to execute based on the current action.
        
        Args:
            curr: Current node
            action: The action that determines the next node
            
        Returns:
            The next node or None if no successor exists
        """
        return curr.successors.get(action or "default")
    
    def _orch(self, shared, params=None):
        """
        Orchestrate the execution of nodes in the flow.
        
        Args:
            shared: Shared context data
            params: Optional parameters to start with
            
        Returns:
            The last action returned by the final node
        """
        curr = self.start_node  # Don't copy the node
        p = params or self.params  # Just reference the params
        last_action = None
        
        logger.debug(f"Starting flow orchestration with node: {curr.__class__.__name__}")
        
        while curr:
            # Set parameters if needed
            if params:
                curr.set_params(p)
                
            # Run the current node
            logger.debug(f"Running node: {curr.__class__.__name__}")
            last_action = curr.run(shared)  # Use run instead of _run
            logger.debug(f"Node returned action: {last_action}")
            
            # Get the next node
            curr = self.get_next_node(curr, last_action)
            if curr:
                logger.debug(f"Next node: {curr.__class__.__name__}")
        
        logger.debug(f"Flow orchestration completed with action: {last_action}")
        return last_action
    
    def run(self, shared):
        """Run the flow with the given shared context."""
        # Check if this flow is configured for direct execution
        if callable(getattr(self, 'exec', None)):
            logger.debug("Using direct execution for flow")
            p = self.prep(shared)
            exec_result = self.exec(p)
            return self.post(shared, p, exec_result)
        
        # Otherwise, use orchestration
        logger.debug("Using orchestration for flow")
        return self._orch(shared)


class BatchFlow(Flow):
    """A flow that processes batches of parameters."""
    
    def run(self, shared):
        """Run the flow for each set of parameters in the batch."""
        # Prepare the batch items
        batch_items = self.prep(shared) or []
        logger.debug(f"BatchFlow.run prepared {len(batch_items)} batch items")
        
        if not batch_items:
            logger.debug("Warning: No batch items to process")
            return self.post(shared, batch_items, [])
        
        # Process the batch with the start node
        if self.start_node:
            logger.debug(f"Processing batch with start node: {self.start_node.__class__.__name__}")
            
            # Set parameters and run the start node directly with the batch
            self.start_node.set_params(self.params)
            batch_results = self.start_node._exec(batch_items)
            
            logger.debug(f"Batch processing complete: {len(batch_results) if batch_results else 0} results")
            
            # Store the batch results in the shared context
            shared["batch_results"] = batch_results
            
            # Let the start node handle post-processing if needed
            action = self.start_node.post(shared, batch_items, batch_results)
            logger.debug(f"Start node post-processing returned action: {action}")
            
            # Return the final results via post method
            return self.post(shared, batch_items, batch_results)
        else:
            logger.debug("Error: No start node defined for batch flow")
            return self.post(shared, batch_items, [])


class AsyncNode(Node):
    """
    Node with asynchronous execution capabilities.
    
    Provides async versions of node methods for use in async workflows.
    """
    
    async def prep_async(self, shared):
        """Async preparation."""
        pass
    
    async def exec_async(self, prep_res):
        """Async execution."""
        pass
    
    async def exec_fallback_async(self, prep_res, exc):
        """Async fallback on failure."""
        raise exc
    
    async def post_async(self, shared, prep_res, exec_res):
        """Async post-processing."""
        pass
    
    async def _exec(self, prep_res):
        """
        Async execution with retry logic.
        
        Args:
            prep_res: Results from preparation
            
        Returns:
            Execution results or fallback results
        """
        for i in range(self.max_retries):
            try:
                return await self.exec_async(prep_res)
            except Exception as e:
                if i == self.max_retries - 1:
                    return await self.exec_fallback_async(prep_res, e)
                if self.wait > 0:
                    await asyncio.sleep(self.wait)
    
    async def run_async(self, shared):
        """Public method to run this async node."""
        if self.successors:
            warnings.warn("Node won't run successors. Use AsyncFlow.")
        return await self._run_async(shared)
    
    async def _run_async(self, shared):
        """Internal method to run the full async execution cycle."""
        p = await self.prep_async(shared)
        e = await self._exec(p)
        return await self.post_async(shared, p, e)
    
    def _run(self, shared):
        """
        Override synchronous run to prevent misuse.
        
        Raises:
            RuntimeError: Always raised to prevent misuse
        """
        raise RuntimeError("Use run_async.")


class AsyncFlow(Flow, AsyncNode):
    """
    Asynchronous flow for orchestrating async nodes.
    
    Manages asynchronous execution of a flow of nodes.
    """
    
    async def _orch_async(self, shared, params=None):
        """
        Orchestrate async execution of nodes in the flow.
        
        Args:
            shared: Shared context data
            params: Optional parameters to start with
            
        Returns:
            The last action returned by the final node
        """
        curr = copy.copy(self.start_node)
        p = params or {**self.params}
        last_action = None
        
        while curr:
            curr.set_params(p)
            if isinstance(curr, AsyncNode):
                last_action = await curr._run_async(shared)
            else:
                last_action = curr._run(shared)
            curr = copy.copy(self.get_next_node(curr, last_action))
        
        return last_action
    
    async def _run_async(self, shared):
        """Run the entire async flow."""
        p = await self.prep_async(shared)
        o = await self._orch_async(shared)
        return await self.post_async(shared, p, o)
    
    async def post_async(self, shared, prep_res, exec_res):
        """Return the final result of the async flow execution."""
        return exec_res


# Extension: Weighted Connection Support
class WeightedNode(Node):
    """
    Node with support for weighted connections.
    
    Allows assigning weights to connections for prioritization.
    """
    
    def weighted_next(self, node, weight=1.0, action="default"):
        """
        Connect this node to another with a specified weight.
        
        Args:
            node: The successor node to connect to
            weight: The connection weight (higher = stronger connection)
            action: The action name that triggers this connection
            
        Returns:
            The successor node for easy chaining
        """
        if action not in self.successors:
            self.successors[action] = []
        self.successors[action].append((node, weight))
        return node


class WeightedFlow(Flow):
    """
    Flow that considers connection weights when selecting the next node.
    Supports both binary selection_mode and continuous temperature parameter.
    """
    
    def __init__(self, start=None, selection_mode="deterministic", temperature=None):
        """
        Initialize a weighted flow.
        
        Args:
            start: The starting node
            selection_mode: 'deterministic' or 'probabilistic' (legacy)
            temperature: Controls randomness in selection (0.0-1.0)
                - 0.0: Purely deterministic (always highest weight)
                - 1.0: Fully temperature-scaled probabilistic selection
                - Values between: Blend of deterministic and probabilistic
                - None: Use selection_mode parameter instead
        """
        super().__init__(start)
        self.selection_mode = selection_mode
        
        # If temperature is provided, it overrides selection_mode
        self.use_temperature = temperature is not None
        self.temperature = max(0.0, min(1.0, temperature or 0.0))  # Clamp between 0.0 and 1.0
    
    def get_next_node(self, curr, action):
        """
        Get the next node based on weights using either temperature or selection_mode.
        
        Args:
            curr: Current node
            action: Action name
            
        Returns:
            Selected next node or None
        """
        successors = curr.successors.get(action or "default")
        
        if not successors:
            return None
            
        if not isinstance(successors, list):
            # Handle legacy non-weighted connection
            return successors
            
        if not successors:
            return None
        
        # Extract nodes and weights
        nodes, weights = zip(*successors)
        
        # TEMPERATURE-BASED SELECTION
        if self.use_temperature:
            # At temperature 0, always return highest weighted node
            if self.temperature == 0.0:
                return max(successors, key=lambda x: x[1])[0]
            
            # Apply temperature scaling to weights
            if self.temperature < 1.0:
                # As temperature approaches 0, highest weight becomes more dominant
                scaled_weights = []
                max_weight = max(weights)
                for w in weights:
                    # Calculate distance from max_weight (0 for the highest)
                    distance = max_weight - w
                    # Scale the distance by temperature (smaller temp = bigger effect)
                    scaled_distance = distance / self.temperature if self.temperature > 0 else float('inf')
                    # Convert back to a weight
                    scaled_weights.append(max_weight - scaled_distance)
                    
                # Handle extreme cases where all weights become effectively 0
                if sum(scaled_weights) == 0:
                    return max(successors, key=lambda x: x[1])[0]
                    
                probabilities = [w/sum(scaled_weights) for w in scaled_weights]
            else:
                # At temperature 1, use original weights directly
                total_weight = sum(weights)
                if total_weight == 0:
                    return None
                probabilities = [w/total_weight for w in weights]
            
            # Select node based on probability
            return random.choices(nodes, probabilities)[0]
        
        # LEGACY BINARY SELECTION MODE
        else:
            if self.selection_mode == "deterministic":
                # Return highest weighted node
                return max(successors, key=lambda x: x[1])[0]
            else:
                # Probabilistic selection
                total_weight = sum(weights)
                
                if total_weight == 0:
                    return None
                    
                # Normalize weights to probabilities
                probabilities = [w/total_weight for w in weights]
                
                # Select node based on probability
                return random.choices(nodes, probabilities)[0]

# Example usage of the WeightedFlow class            
if False:
    # Legacy binary approach
    legacy_flow = WeightedFlow(start=start_node, selection_mode="deterministic")
    # or
    legacy_flow = WeightedFlow(start=start_node, selection_mode="probabilistic")

    # New temperature-based approach
    temp_flow = WeightedFlow(start=start_node, temperature=0.0)  # Fully deterministic
    # or
    temp_flow = WeightedFlow(start=start_node, temperature=0.5)  # Balanced
    # or
    temp_flow = WeightedFlow(start=start_node, temperature=1.0)  # Fully probabilistic

# Extension: Proficiency-Based Learning Flow for ZiNets
class ZiNetsLearningFlow(WeightedFlow):
    """
    Specialized flow for ZiNets character learning.
    
    Filters nodes based on proficiency level and supports temperature-based selection.
    """
    
    def __init__(self, proficiency_level="intro", selection_mode="probabilistic", temperature=None):
        """
        Initialize ZiNets learning flow.
        
        Args:
            proficiency_level: 'intro', 'beginner', 'intermediate', or 'advanced'
            selection_mode: 'deterministic' or 'probabilistic' (legacy)
            temperature: Controls randomness in selection (0.0-1.0)
        """
        super().__init__(None, selection_mode, temperature)
        self.proficiency_level = proficiency_level
        self.threshold_map = {
            "intro": 0.95,       # Only elemental building block characters
            "beginner": 0.7,     # Common characters
            "intermediate": 0.4, # Less common characters
            "advanced": 0.1      # Rare characters
        }
        
        # Special flag for elemental character focus
        self.elemental_only = (proficiency_level == "intro")
    
    def get_next_node(self, curr, action):
        """
        Filter nodes based on proficiency level before selection.
        
        Args:
            curr: Current node
            action: Action name
            
        Returns:
            Selected next node or None
        """
        successors = curr.successors.get(action or "default")
        
        if not successors or not isinstance(successors, list):
            return super().get_next_node(curr, action)
        
        # For intro level, only follow connections to elemental characters
        if self.elemental_only:
            filtered_successors = [(node, weight) for node, weight in successors 
                                if node.params.get("is_elemental", False)]
        else:
            # Apply normal threshold filtering for other levels
            threshold = self.threshold_map.get(self.proficiency_level, 0)
            filtered_successors = [(node, weight) for node, weight in successors 
                                if weight >= threshold]
        
        if not filtered_successors:
            return None
        
        # Store original successors
        orig_successors = curr.successors.get(action or "default")
        
        # Replace with filtered successors for selection
        curr.successors[action or "default"] = filtered_successors
        
        # Use parent class method to select among filtered successors
        # This will use either temperature or selection_mode based on configuration
        selected = super().get_next_node(curr, action)
        
        # Restore original successors
        curr.successors[action or "default"] = orig_successors
        
        return selected
    

# ----- DEMONSTRATION EXAMPLES -----

def demo_basic_flow():
    """Demonstrates a basic flow with conditional branching."""
    print("\n=== BASIC FLOW DEMONSTRATION ===")
    
    # Define processing nodes
    fetch_data = Node()
    validate_data = Node()
    process_normal = Node()
    process_special = Node()
    store_results = Node()
    
    # Configure node behaviors
    def fetch_data_exec(prep_res):
        print("Fetching data...")
        return {"data": [1, 2, 3, 4, 5]}
    fetch_data.exec = fetch_data_exec
    
    def validate_data_exec(prep_res):
        data = prep_res["data"]
        total = sum(data)
        print(f"Validating data... Sum is {total}")
        if total > 10:
            return "special"  # Return an action name
        return "normal"       # Default action
    validate_data.exec = validate_data_exec
    
    def process_normal_exec(prep_res):
        print("Processing with normal algorithm...")
        return {"processed": "normal", "data": prep_res["data"]}
    process_normal.exec = process_normal_exec
    
    def process_special_exec(prep_res):
        print("Processing with special algorithm...")
        return {"processed": "special", "data": prep_res["data"]}
    process_special.exec = process_special_exec
    
    def store_results_exec(prep_res):
        print(f"Storing results: {prep_res}")
        return "completed"
    store_results.exec = store_results_exec
    
    # Connect nodes with actions
    fetch_data >> validate_data
    validate_data - "normal" >> process_normal
    validate_data - "special" >> process_special
    process_normal >> store_results
    process_special >> store_results
    
    # Create and run a flow
    workflow = Flow(start=fetch_data)
    result = workflow.run({})  # Empty shared context
    
    print(f"Final result: {result}")
    return result


def demo_retry_mechanism():
    """Demonstrates the retry mechanism for handling failures."""
    print("\n=== RETRY MECHANISM DEMONSTRATION ===")
    
    # Create a node with retry capabilities
    unreliable_node = Node(max_retries=3, wait=1)
    
    # Simulation counter for demonstration
    attempt_counter = [0]
    
    def unreliable_exec(prep_res):
        attempt_counter[0] += 1
        print(f"Attempt {attempt_counter[0]}")
        
        # Succeed only on the third attempt
        if attempt_counter[0] < 3:
            print("Operation failed, will retry...")
            raise Exception("Simulated failure")
        
        print("Operation succeeded!")
        return "Success after retries"
    
    def fallback_exec(prep_res, exc):
        print(f"All retries exhausted. Fallback activated. Error: {exc}")
        return "Fallback result"
    
    unreliable_node.exec = unreliable_exec
    unreliable_node.exec_fallback = fallback_exec
    
    # Run the node
    result = unreliable_node.run({})
    print(f"Final result: {result}")
    return result


def demo_batch_processing():
    """Demonstrates batch processing capabilities."""
    print("\n=== BATCH PROCESSING DEMONSTRATION ===")
    
    # Create a batch processor node
    batch_processor = BatchNode()
    
    def process_item(item):
        print(f"Processing item: {item}")
        return item * 2
    
    batch_processor.exec = process_item
    
    # Create a flow with batch preparation
    batch_flow = Flow(start=batch_processor)
    
    def prep_batch(shared):
        print("Preparing batch of items...")
        return [1, 2, 3, 4, 5]
    
    batch_flow.prep = prep_batch
    
    # Run the batch flow
    results = batch_flow.run({})
    print(f"Batch results: {results}")
    return results


def demo_shared_context():
    """Demonstrates using shared context across nodes."""
    print("\n=== SHARED CONTEXT DEMONSTRATION ===")
    
    # Create nodes that read and modify shared context
    node_a = Node()
    node_b = Node()
    node_c = Node()
    
    def node_a_exec(prep_res):
        print("Node A executing...")
        return {"a_result": 42}
    
    def node_a_post(shared, prep_res, exec_res):
        # Store result in shared context
        shared["a_value"] = exec_res["a_result"]
        print(f"Node A stored value {shared['a_value']} in shared context")
        return "default"
    
    def node_b_exec(prep_res):
        print("Node B executing...")
        return "B processed"
    
    def node_b_post(shared, prep_res, exec_res):
        # Read and modify shared context
        a_value = shared.get("a_value", 0)
        shared["b_value"] = a_value * 2
        print(f"Node B read {a_value} and stored {shared['b_value']}")
        return "default"
    
    def node_c_exec(prep_res):
        print("Node C executing...")
        return "C processed"
    
    def node_c_post(shared, prep_res, exec_res):
        # Read multiple shared values
        a_value = shared.get("a_value", 0)
        b_value = shared.get("b_value", 0)
        result = a_value + b_value
        shared["final_result"] = result
        print(f"Node C calculated final result: {result}")
        return "default"
    
    # Configure nodes
    node_a.exec = node_a_exec
    node_a.post = node_a_post
    
    node_b.exec = node_b_exec
    node_b.post = node_b_post
    
    node_c.exec = node_c_exec
    node_c.post = node_c_post
    
    # Connect nodes
    node_a >> node_b >> node_c
    
    # Run the flow with shared context
    shared_context = {}
    flow = Flow(start=node_a)
    flow.run(shared_context)
    
    print(f"Final shared context: {shared_context}")
    return shared_context


async def demo_async_flow():
    """Demonstrates asynchronous flow execution."""
    print("\n=== ASYNC FLOW DEMONSTRATION ===")
    
    # Create async nodes
    async_node_a = AsyncNode()
    async_node_b = AsyncNode()
    
    async def node_a_exec_async(prep_res):
        print("Async Node A starting...")
        await asyncio.sleep(1)  # Simulate async operation
        print("Async Node A completed")
        return "A result"
    
    async def node_b_exec_async(prep_res):
        print("Async Node B starting...")
        await asyncio.sleep(0.5)  # Simulate async operation
        print("Async Node B completed")
        return "B result"
    
    # Configure nodes
    async_node_a.exec_async = node_a_exec_async
    async_node_b.exec_async = node_b_exec_async
    
    # Connect nodes
    async_node_a >> async_node_b
    
    # Create and run async flow
    async_flow = AsyncFlow(start=async_node_a)
    result = await async_flow.run_async({})
    
    print(f"Async flow result: {result}")
    return result


def demo_weighted_connections():
    """Demonstrates weighted connections using both binary and temperature-based selection."""
    print("\n=== WEIGHTED CONNECTIONS DEMONSTRATION ===")
    
    # Create character nodes
    radical_water = WeightedNode().set_params({"character": "水", "type": "radical"})
    
    # Dictionary of characters with their properties
    characters = {
        "河": {"frequency": 0.9, "is_elemental": True},    # river (elemental)
        "海": {"frequency": 0.95, "is_elemental": True},   # sea (elemental)
        "湖": {"frequency": 0.8, "is_elemental": False},   # lake
        "洋": {"frequency": 0.85, "is_elemental": False},  # ocean
        "泉": {"frequency": 0.7, "is_elemental": False},   # spring
        "湾": {"frequency": 0.6, "is_elemental": False},   # bay
        "溅": {"frequency": 0.3, "is_elemental": False},   # splash
        "漩": {"frequency": 0.2, "is_elemental": False},   # whirlpool
    }
    
    # Create nodes and weighted connections
    char_nodes = {}
    for char, attrs in characters.items():
        char_nodes[char] = WeightedNode().set_params({
            "character": char, 
            "type": "character",
            "is_elemental": attrs["is_elemental"]
        })
        
        # Connect with weight based on frequency
        radical_water.weighted_next(
            char_nodes[char], 
            weight=attrs["frequency"], 
            action="visual"
        )
    
    # 1. First run with original binary selection modes
    print("\nOriginal Binary Selection Modes:")
    for mode in ["deterministic", "probabilistic"]:
        print(f"\nTesting '{mode}' selection mode (binary):")
        
        # Create a basic WeightedFlow with the binary selection mode
        flow = WeightedFlow(start=radical_water, selection_mode=mode)
        
        # Sample exploration
        current = radical_water
        path = [current.params["character"]]
        
        # Follow 5 steps in the flow
        for _ in range(5):
            next_node = flow.get_next_node(current, "visual")
            if not next_node:
                break
                
            path.append(next_node.params["character"])
            current = next_node
            
        print(f"Exploration path: {' → '.join(path)}")
    
    # 2. Now run with temperature-based selection at different temperatures
    print("\nNew Temperature-Based Selection:")
    for temp in [0.0, 0.3, 0.7, 1.0]:
        print(f"\nTesting temperature = {temp}:")
        
        # Create a WeightedFlow with the temperature parameter
        flow = WeightedFlow(start=radical_water, temperature=temp)
        
        # Sample exploration
        current = radical_water
        path = [current.params["character"]]
        
        # Follow 5 steps in the flow
        for _ in range(5):
            next_node = flow.get_next_node(current, "visual")
            if not next_node:
                break
                
            path.append(next_node.params["character"])
            current = next_node
            
        print(f"Exploration path: {' → '.join(path)}")
    
    # 3. Run ZiNetsLearningFlow with different proficiency levels and temperatures
    print("\nZiNetsLearningFlow with Temperature:")
    # Update ZiNetsLearningFlow to use temperature
    proficiency_levels = ["intro", "beginner", "intermediate", "advanced"]
    temperatures = [0.0, 0.5, 1.0]
    
    for level in proficiency_levels:
        for temp in temperatures:
            print(f"\nProficiency: '{level}', Temperature: {temp}")
            
            # Modify ZiNetsLearningFlow to accept temperature parameter
            flow = ZiNetsLearningFlow(proficiency_level=level)
            flow.use_temperature = True
            flow.temperature = temp
            flow.start_node = radical_water
            
            # Sample exploration
            current = radical_water
            path = [current.params["character"]]
            
            # Follow 5 steps in the flow
            for _ in range(5):
                next_node = flow.get_next_node(current, "visual")
                if not next_node:
                    break
                    
                path.append(next_node.params["character"])
                current = next_node
                
            print(f"Exploration path: {' → '.join(path)}")
    
    return "Weighted connections demonstration completed"


@click.group()
def cli():
    """PocketFlow Framework Demo CLI"""
    pass

@cli.command()
def basic():
    """Run the basic flow demonstration"""
    demo_basic_flow()

@cli.command()
def retry():
    """Run the retry mechanism demonstration"""
    demo_retry_mechanism()

@cli.command()
def batch():
    """Run the batch processing demonstration"""
    demo_batch_processing()

@cli.command()
def context():
    """Run the shared context demonstration"""
    demo_shared_context()

@cli.command()
def weighted():
    """Run the weighted connections demonstration"""
    demo_weighted_connections()

@cli.command()
def async_demo():
    """Run the asynchronous flow demonstration"""
    asyncio.run(demo_async_flow())

@cli.command()
def all():
    """Run all demonstrations"""
    print("POCKET FLOW FRAMEWORK DEMONSTRATION")
    print("===================================")
    
    # Run synchronous demos
    demo_basic_flow()
    demo_retry_mechanism()
    demo_batch_processing()
    demo_shared_context()
    demo_weighted_connections()
    
    # Run async demo
    asyncio.run(demo_async_flow())
    
    print("\nAll demonstrations completed successfully!")


@cli.command()
@click.option('--mode', type=click.Choice(['binary', 'temperature', 'both']), default='both',
              help='Selection mode to test')
@click.option('--temps', '-t', multiple=True, type=float, default=[0.0, 0.3, 0.7, 1.0],
              help='Temperature values to test (can be used multiple times)')
@click.option('--levels', '-l', multiple=True, 
              type=click.Choice(['intro', 'beginner', 'intermediate', 'advanced']),
              default=['intro', 'beginner', 'intermediate', 'advanced'],
              help='Proficiency levels to test (can be used multiple times)')
def weighted_custom(mode, temps, levels):
    """Run weighted connections demo with custom settings"""
    print("\n=== WEIGHTED CONNECTIONS DEMONSTRATION (CUSTOM) ===")
    
    # Create character nodes
    radical_water = WeightedNode().set_params({"character": "水", "type": "radical"})
    
    # Dictionary of characters with their properties
    characters = {
        "河": {"frequency": 0.9, "is_elemental": True},    # river (elemental)
        "海": {"frequency": 0.95, "is_elemental": True},   # sea (elemental)
        "湖": {"frequency": 0.8, "is_elemental": False},   # lake
        "洋": {"frequency": 0.85, "is_elemental": False},  # ocean
        "泉": {"frequency": 0.7, "is_elemental": False},   # spring
        "湾": {"frequency": 0.6, "is_elemental": False},   # bay
        "溅": {"frequency": 0.3, "is_elemental": False},   # splash
        "漩": {"frequency": 0.2, "is_elemental": False},   # whirlpool
    }
    
    # Create nodes and weighted connections
    char_nodes = {}
    for char, attrs in characters.items():
        char_nodes[char] = WeightedNode().set_params({
            "character": char, 
            "type": "character",
            "is_elemental": attrs["is_elemental"]
        })
        
        # Connect with weight based on frequency
        radical_water.weighted_next(
            char_nodes[char], 
            weight=attrs["frequency"], 
            action="visual"
        )
    
    # 1. Binary selection modes
    if mode in ['binary', 'both']:
        print("\nOriginal Binary Selection Modes:")
        for select_mode in ["deterministic", "probabilistic"]:
            print(f"\nTesting '{select_mode}' selection mode (binary):")
            
            # Create a basic WeightedFlow with the binary selection mode
            flow = WeightedFlow(start=radical_water, selection_mode=select_mode)
            
            # Sample exploration
            current = radical_water
            path = [current.params["character"]]
            
            # Follow 5 steps in the flow
            for _ in range(5):
                next_node = flow.get_next_node(current, "visual")
                if not next_node:
                    break
                    
                path.append(next_node.params["character"])
                current = next_node
                
            print(f"Exploration path: {' → '.join(path)}")
    
    # 2. Temperature-based selection
    if mode in ['temperature', 'both']:
        print("\nNew Temperature-Based Selection:")
        for temp in temps:
            print(f"\nTesting temperature = {temp}:")
            
            # Create a WeightedFlow with the temperature parameter
            flow = WeightedFlow(start=radical_water, temperature=temp)
            
            # Sample exploration
            current = radical_water
            path = [current.params["character"]]
            
            # Follow 5 steps in the flow
            for _ in range(5):
                next_node = flow.get_next_node(current, "visual")
                if not next_node:
                    break
                    
                path.append(next_node.params["character"])
                current = next_node
                
            print(f"Exploration path: {' → '.join(path)}")
    
    # 3. ZiNetsLearningFlow combinations
    if mode in ['both']:
        print("\nZiNetsLearningFlow with Temperature:")
        
        for level in levels:
            for temp in temps:
                print(f"\nProficiency: '{level}', Temperature: {temp}")
                
                # Modify ZiNetsLearningFlow to accept temperature parameter
                flow = ZiNetsLearningFlow(proficiency_level=level)
                flow.use_temperature = True
                flow.temperature = temp
                flow.start_node = radical_water
                
                # Sample exploration
                current = radical_water
                path = [current.params["character"]]
                
                # Follow 5 steps in the flow
                for _ in range(5):
                    next_node = flow.get_next_node(current, "visual")
                    if not next_node:
                        break
                        
                    path.append(next_node.params["character"])
                    current = next_node
                    
                print(f"Exploration path: {' → '.join(path)}")
    
    return "Weighted connections demonstration completed"



if __name__ == "__main__":
    cli()