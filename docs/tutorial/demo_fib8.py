#!/usr/bin/env python3
"""
# PocketFlow Fibonacci Demonstrations

This script demonstrates how to use PocketFlow to implement
Fibonacci sequence generation using different approaches:
- Basic flow
- Batch processing
- Parallel processing
- Composite nodes with incremental computation

## Reference
- https://claude.ai/chat/16770888-3c99-4886-b452-81a585981753

## Summary:
The Fibonacci sequence is indeed a perfect metaphor for this learning journey. Like how each Fibonacci number builds on previous ones to create increasingly complex patterns, you're building a foundation of programming patterns that can scale to more complex applications in your ZiNets research.
What I find particularly elegant about your implementation is how it demonstrates different computational paradigms:

Basic sequential processing (mirroring the natural order of computation)
Batch processing (handling multiple related tasks efficiently)
Parallel processing (leveraging concurrent execution)
Composite processing (building on previous results)

Each approach offers different tradeoffs in terms of simplicity, performance, and scalability - much like how natural systems evolve different strategies for growth and adaptation.
The flow-based programming model you're exploring with PocketFlow provides a powerful abstraction that can represent complex processes as networks of simpler components, which seems perfectly aligned with your ZiNets framework for analyzing complex systems.

"""

# import asyncio
# import copy
import time
# import random
from typing import Dict, List, Any, Optional
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path
import click


# setup logger
from util_log import get_logger, set_log_level, configure_logging
LOG_FILE = Path(__file__).name + ".log"
LOG_LEVEL = "DEBUG"   # For detailed logging during development
# # "WARNING"           # Or for minimal output in production
# set_log_level(LOG_LEVEL)      
# Or completely customize the logging setup
configure_logging(
    level=LOG_LEVEL,
    format_str='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
    log_file=LOG_FILE  # Also log to a file
)
logger = get_logger("demo-fib")

LINE_BREAK = 100*"="

class BaseNode:
    """Base class for all nodes in the flow framework."""
    
    def __init__(self, name=None):
        """Initialize a node with empty params and successors dictionaries."""
        self.name = name
        self.params = {}
        self.successors = {}
    
    def set_params(self, params):
        """Set the parameters for this node."""
        self.params = params
        return self  # For method chaining
    
    def next(self, node, action="default"):
        """Connect this node to another node with a specific action."""
        self.successors[action] = node
        return node
    
    def prep(self, shared):
        """Prepare node for execution."""
        pass
    
    def exec(self, prep_res):
        """Execute node logic."""
        pass
    
    def _exec(self, prep_res):
        """Internal method to execute the node logic."""
        return self.exec(prep_res)
    
    def post(self, shared, prep_res, exec_res):
        """Post-processing after execution."""
        pass
    
    def _run(self, shared):
        """Internal method to run the full node execution cycle.
        
        Return last action
        """
        p = self.prep(shared)
        e = self._exec(p)
        return self.post(shared, p, e)
    
    def run(self, shared):
        """Public method to run this node."""
        return self._run(shared)
    
    def __rshift__(self, other):
        """Override >> operator for creating node connections."""
        return self.next(other)


class Node(BaseNode):
    """Standard node with retry functionality."""
    
    def __init__(self, name="node", max_retries=1, wait=0):
        """Initialize a node with retry capabilities."""
        super().__init__(name=name)
        self.max_retries = max_retries
        self.wait = wait
    
    def exec_fallback(self, prep_res, exc):
        """Fallback method called when all retries are exhausted."""
        raise exc
    
    def _exec(self, prep_res):
        """Internal execution with retry logic."""
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
    def __init__(self, name="batch-node"):
        super().__init__(name=name)

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
    """Orchestrates execution of multiple connected nodes.
  
    Flow is a special node with _orch() method - similar to _run() ,
    that traverses all connected nodes.

    Manages the flow of execution from a starting node through its successors.    
    """
    
    def __init__(self, name="flow", start=None):
        """Initialize a flow with an optional starting node."""
        super().__init__(name=name)
        self.start_node = start
        self._is_direct_execution = False  # Flag to indicate if this flow uses direct execution
    
    def set_direct_execution(self):
        """Configure this flow for direct execution (exec/post pattern)."""
        self._is_direct_execution = True
        return self
    
    def start(self, start):
        """Set the starting node for this flow."""
        self.start_node = start
        return start
    
    def get_next_node(self, curr, action):
        """Find the next connected node to execute based on the current action."""
        return curr.successors.get(action or "default")
    
    def _orch(self, shared, params=None):
        """Orchestrate the execution of nodes in the flow."""
        curr = self.start_node  # Don't copy the node
        p = params or self.params  # Just reference the params
        last_action = None
        
        logger.debug(f"Starting flow orchestration with node: {curr.name}")
        
        while curr:  # traverse all connected nodes
            # Set parameters if needed
            if params:
                curr.set_params(p)
                
            # Run the current node
            logger.debug(f"Running node: {curr.name}")
            last_action = curr.run(shared)  # Use run instead of _run
            logger.debug(f"Node returned action: {last_action}")
            
            # Get the next node
            curr = self.get_next_node(curr, last_action)
            if curr:
                logger.debug(f"Next node: {curr.name}")
        
        logger.debug(f"Flow orchestration completed with action: {last_action}")
        return last_action
    
    def run(self, shared):
        """Run the flow with the given shared context."""
        # Check if this flow is configured for direct execution
        if self._is_direct_execution and callable(getattr(self, 'exec', None)):
            logger.debug("Using direct execution for flow")
            p = self.prep(shared)
            exec_result = self.exec(p)
            return self.post(shared, p, exec_result)
        
        # Otherwise, use orchestration
        logger.debug("Using orchestration for flow")
        return self._orch(shared)
    
class BatchFlow(Flow):
    """A flow that processes batches of parameters."""

    def __init__(self, name="batch-flow", start=None):
        super().__init__(name=name, start=start)

    def run(self, shared):
        """Run the flow for each set of parameters in the batch."""
        # Prepare the batch items
        batch_items = self.prep(shared) or []
        logger.debug(f"BatchFlow.run prepared {len(batch_items)} batch items")
        
        if not batch_items:
            logger.debug("Warning: No batch items to process")
            # nothing to execute
            return self.post(shared, batch_items, [])
        
        # Process the batch with the start node
        if self.start_node:
            logger.debug(f"Processing batch with start node: {self.start_node.name}")
            
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

# ----- FIBONACCI DEMONSTRATIONS -----

def create_basic_fibonacci_flow(limit=10):
    """Create a flow for generating Fibonacci sequence."""
    
    # Create a node that will generate the Fibonacci sequence
    fib_node = Node("fib")
    
    def generate_exec(prep_res):
        """Generate the Fibonacci sequence."""
        logger.debug(f"Generating Fibonacci sequence (limit={limit}) ...")
        sequence = [0, 1]
        
        for i in range(2, limit):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
            
        return sequence
    
    def generate_post(shared, prep_res, exec_res):
        """Store the generated sequence in shared context."""
        sequence = exec_res
        
        if sequence is None:
            logger.debug("ERROR: No sequence generated!")
            return "error"
            
        logger.debug(f"Storing sequence in shared context ({len(sequence)} terms)")
        shared["sequence"] = sequence.copy()  # Make a copy to ensure it's stored
        shared["count"] = len(sequence)
        shared["last"] = sequence[-1] if sequence else None
        
        logger.debug(f"Shared context after update: {shared}")
        return "done"
    
    # Configure the node
    fib_node.exec = generate_exec
    fib_node.post = generate_post
    
    # Create and return the flow
    flow = Flow(name="basic fib", start=fib_node)
    # Explicitly set the exec attribute to None to prevent direct execution
    flow.exec = None
    return flow

def create_fibonacci_node():
    """Create a node that generates a Fibonacci sequence."""
    LIMIT=10    
    def generate_fibonacci(params):
        """Generate Fibonacci sequence up to the specified limit."""
        limit = params.get("limit", LIMIT)
        
        # Initialize the sequence
        sequence = [0, 1]
        
        # Generate Fibonacci numbers
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    fib_node = BatchNode(f"fib-{LIMIT}")   
    fib_node.exec = generate_fibonacci
    return fib_node

def create_fibonacci_batch_flow():
    """Create a batch flow for generating multiple Fibonacci sequences."""
    LIMIT=10 
    
    # Define the execution function that processes a single batch item
    def fib_node_exec(params):
        """Generate Fibonacci sequence for a single batch item."""
        limit = params.get("limit", LIMIT)
        logger.debug(f"Generating Fibonacci sequence with limit={limit}")
        
        # Initialize the sequence
        sequence = [0, 1]
        
        # Generate Fibonacci numbers
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        
        result = {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1],
            "id": params.get("id", "unknown")
        }
        logger.debug(f"Generated Fibonacci sequence with limit={limit}, length={len(sequence)}")
        return result
    
    # Define post-processing for batch node
    def fib_node_post(shared, prep_res, exec_res):
        logger.debug(f"Fibonacci node post-processing: {len(exec_res) if exec_res else 0} results")
        # Results will be handled by the flow's post method
        return "default"
    
    # Configure the batch node
    # Create a batch processor node
    fib_node = BatchNode("batch-fib")
    fib_node.exec = fib_node_exec   
    fib_node.post = fib_node_post
    
    # Prepare batch parameters
    def prep_batch(shared):
        logger.debug("Preparing batch of Fibonacci sequence parameters...")
        batch_params = [
            {"limit": 10, "id": "small"},
            {"limit": 30, "id": "medium"},
            {"limit": 100, "id": "large"}
        ]
        logger.debug(f"Created {len(batch_params)} batch items")
        return batch_params
    
    # Post-process the batch results
    def post_batch(shared, prep_res, exec_res):
        logger.debug(f"Batch flow post-processing: {len(exec_res) if exec_res else 0} results")
        
        # Display the results
        logger.debug("\nFibonacci Sequences Generated:")
        
        if not exec_res:
            logger.debug("Warning: No results found.")
            return "completed"
        
        # Process and display the results
        for result in exec_res:
            limit = result.get("limit", "unknown")
            sequence = result.get("sequence", [])
            last_number = result.get("last_number", None)
            
            logger.debug(f"\nSequence with limit {limit}:")
            logger.debug(f"  • First few numbers: {sequence[:min(5, len(sequence))]}...")
            logger.debug(f"  • Last number: {last_number}")
            logger.debug(f"  • Total numbers: {len(sequence)}")
        
        return "completed"
    
    # Create / config the batch flow
    flow = BatchFlow(name="batch fib flow", start=fib_node)   
    flow.prep = prep_batch
    flow.post = post_batch
    
    return flow

def create_parallel_fibonacci_flow():
    """Create a flow for parallel processing of Fibonacci sequences."""
    
    def generate_fibonacci(limit):
        """Generate Fibonacci sequence up to the specified limit."""
        logger.debug(f"Generating sequence with limit={limit}")
        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    def prep_parallel(shared):
        logger.debug("Preparing parallel Fibonacci sequence generation...")
        return [10, 30, 100]
    
    def exec_parallel(limits):
        logger.debug(f"Executing with limits: {limits}")
        # Process sequentially 
        results = []
        for limit in limits:
            result = generate_fibonacci(limit)
            results.append(result)
            logger.debug(f"Added result for limit={limit}")
        logger.debug(f"Generated {len(results)} results")
        return results
    
    def post_parallel(shared, prep_res, exec_res):
        logger.debug(f"Post-processing results: {type(exec_res)}")
        results = [] if exec_res is None else exec_res
        shared["results"] = results
        
        logger.debug(f"\nParallel processing complete. Results: {len(results)} sequences")
        
        if not results:
            logger.debug("No sequences were generated.")
            return "completed"
        
        for result in results:
            limit = result["limit"]
            sequence = result["sequence"]
            logger.debug(f"\nSequence with limit {limit}:")
            logger.debug(f"  • First few numbers: {sequence[:5]}...")
            logger.debug(f"  • Last number: {result['last_number']}")
            logger.debug(f"  • Total numbers: {len(sequence)}")
        
        return "completed"
    
    # Create a custom flow for parallel processing
    flow = Flow("parallel fib flow")
    
    # Configure the flow
    flow.prep = prep_parallel
    flow.exec = exec_parallel
    flow.post = post_parallel
    
    # Configure for direct execution
    flow.set_direct_execution()
    
    return flow

def parallel_fibonacci_threaded(limits = [10, 30, 100]):
    """Direct implementation of parallel Fibonacci generation using ThreadPoolExecutor."""
    logger.debug(f"\n\n=== FIBONACCI PARALLEL PROCESSING DEMONSTRATION (WITH THREADING) ===\n{LINE_BREAK}")
    
    # Generate a Fibonacci sequence
    def generate_fibonacci(limit):
        logger.debug(f"Thread started: Generating sequence with limit={limit}")
        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        logger.debug(f"Thread completed: Generated sequence with limit={limit}")
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    # Define the limits to process
    
    logger.debug(f"Processing {len(limits)} limits in parallel: {limits}")
    
    # Process using ThreadPoolExecutor
    results = []
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks
        logger.debug("Submitting tasks to thread pool...")
        future_to_limit = {executor.submit(generate_fibonacci, limit): limit for limit in limits}
        
        # Collect results as they complete
        for future in future_to_limit:
            try:
                limit = future_to_limit[future]
                logger.debug(f"Waiting for result with limit={limit}...")
                result = future.result()
                logger.debug(f"Received result for limit={limit}")
                results.append(result)
            except Exception as e:
                logger.debug(f"Error processing limit {future_to_limit[future]}: {e}")
    
    end_time = time.time()
    execution_time = end_time - start_time
    logger.debug(f"All threads completed in {execution_time:.4f} seconds")
    
    # Sort results by limit for consistent display
    results.sort(key=lambda x: x["limit"])
    
    # Display results
    logger.debug("\nFibonacci Sequences Generated:")
    
    for result in results:
        limit = result["limit"]
        sequence = result["sequence"]
        last_number = result["last_number"]
        
        logger.debug(f"\nSequence with limit {limit}:")
        logger.debug(f"  • First few numbers: {sequence[:5]}...")
        logger.debug(f"  • Last number: {last_number}")
        logger.debug(f"  • Total numbers: {len(sequence)}")
    
    return results


def parallel_fibonacci(limits = [10, 30, 100]):
    """Direct implementation of parallel Fibonacci generation without Flow class."""
    logger.debug(f"\n\n=== FIBONACCI PARALLEL PROCESSING DEMONSTRATION ===\n{LINE_BREAK}")
    
    # Generate a Fibonacci sequence
    def generate_fibonacci(limit):
        logger.debug(f"Generating sequence with limit={limit}")
        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    # Process limits
    logger.debug(f"Processing limits: {limits}")

    start_time = time.time()    
    # Process each limit
    results = []
    for limit in limits:
        result = generate_fibonacci(limit)
        results.append(result)

    end_time = time.time()

    # Display results
    logger.debug("\nFibonacci Sequences Generated:")
    
    for result in results:
        limit = result["limit"]
        sequence = result["sequence"]
        last_number = result["last_number"]
        
        logger.debug(f"\nSequence with limit {limit}:")
        logger.debug(f"  • First few numbers: {sequence[:5]}...")
        logger.debug(f"  • Last number: {last_number}")
        logger.debug(f"  • Total numbers: {len(sequence)}")

    logger.debug(f"\nTotal completed in  {end_time - start_time:.4f} seconds")

    return results



def create_composite_fibonacci_flow():
    """
    Create a composite flow that builds Fibonacci sequences incrementally:
    1. First calculates sequence with limit=10
    2. Uses that to calculate sequence with limit=30
    3. Finally uses that to calculate sequence with limit=100
    """
    
    # Create individual nodes for each sequence length
    LIMITS = [10,30,100]

    fib_node_10 = Node(f"fib-{LIMITS[0]}")
    fib_node_30 = Node(f"fib-{LIMITS[1]}")
    fib_node_100 = Node(f"fib-{LIMITS[2]}")
    
    # Node for limit=10 calculation
    def calculate_fib_10(prep_res):
        logger.debug("Calculating Fibonacci sequence with limit=10...")
        sequence = [0, 1]
        while len(sequence) < LIMITS[0]:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
    def post_fib_10(shared, prep_res, exec_res):
        # Store result in shared context
        sequence = exec_res
        shared["fib_10"] = sequence
        logger.debug(f"Generated sequence with limit=10: {sequence[:5]}... (length: {len(sequence)})")
        return "continue"
    
    fib_node_10.exec = calculate_fib_10
    fib_node_10.post = post_fib_10
    
    # Node for limit=30 calculation (builds on limit=10)
    def calculate_fib_30(prep_res):
        logger.debug("Calculating Fibonacci sequence with limit=30 (building from limit=10)...")
        # Get the base sequence from parameters
        base_sequence = prep_res  # Passed from prep function
        
        if not base_sequence:
            raise ValueError("Base sequence not found")
        
        # Continue from where we left off
        sequence = base_sequence.copy()
        while len(sequence) < LIMITS[1]:
            sequence.append(sequence[-1] + sequence[-2])
        
        return sequence
    
    def prep_fib_30(shared):
        # Get the result from the previous calculation
        base_sequence = shared.get("fib_10", [])
        logger.debug(f"Using base sequence of length {len(base_sequence)}")
        return base_sequence
    
    def post_fib_30(shared, prep_res, exec_res):
        # Store result in shared context
        sequence = exec_res
        shared["fib_30"] = sequence
        logger.debug(f"Generated sequence with limit=30: {sequence[:5]}... (length: {len(sequence)})")
        return "continue"
    
    fib_node_30.prep = prep_fib_30
    fib_node_30.exec = calculate_fib_30
    fib_node_30.post = post_fib_30
    
    # Node for limit=100 calculation (builds on limit=30)
    def calculate_fib_100(prep_res):
        logger.debug("Calculating Fibonacci sequence with limit=100 (building from limit=30)...")
        # Get the base sequence from parameters
        base_sequence = prep_res  # Passed from prep function
        
        if not base_sequence:
            raise ValueError("Base sequence not found")
        
        # Continue from where we left off
        sequence = base_sequence.copy()
        while len(sequence) < LIMITS[2]:
            sequence.append(sequence[-1] + sequence[-2])
        
        return sequence
    
    def prep_fib_100(shared):
        # Get the result from the previous calculation
        base_sequence = shared.get("fib_30", [])
        logger.debug(f"Using base sequence of length {len(base_sequence)}")
        return base_sequence
    
    def post_fib_100(shared, prep_res, exec_res):
        # Store result in shared context
        sequence = exec_res
        shared["fib_100"] = sequence
        logger.debug(f"Generated sequence with limit=100: {sequence[:5]}... (length: {len(sequence)})")
        
        # Print final results
        logger.debug("\nFinal Fibonacci Sequences:")
        logger.debug(f"Sequence (10): Last number = {shared['fib_10'][-1]}")
        logger.debug(f"Sequence (30): Last number = {shared['fib_30'][-1]}")
        logger.debug(f"Sequence (100): Last number = {shared['fib_100'][-1]}")
        
        return "done"
    
    fib_node_100.prep = prep_fib_100
    fib_node_100.exec = calculate_fib_100
    fib_node_100.post = post_fib_100
    
    # Connect nodes in sequence - FIXED CONNECTION METHOD
    fib_node_10.next(fib_node_30, "continue")
    fib_node_30.next(fib_node_100, "continue")
    fib_node_100.next(None, "done")  # Explicitly end flow
    
    # Create the flow
    flow = Flow(name="composite fib", start=fib_node_10)
    return flow

# ----- CLICK CLI COMMANDS -----

@click.group()
def cli():
    """Fibonacci sequence generation with PocketFlow - Demo CLI"""
    pass

@cli.command()
def parallel_threaded():
    """Run parallel Fibonacci generation using ThreadPoolExecutor"""
    logger.debug("Starting parallel Fibonacci generation with ThreadPoolExecutor...")
    start_time = time.time()
    results = parallel_fibonacci_threaded()
    end_time = time.time()
    
    logger.debug(f"\n parallel_threaded completed in  {end_time - start_time:.4f} seconds")
    return results

# cli.add_command(parallel_threaded)

# Add this as a CLI command
@cli.command()
def parallel_direct():
    """Run direct parallel Fibonacci generation without using Flow class"""
    start_time = time.time()
    results = parallel_fibonacci()
    end_time = time.time()
    
    logger.debug(f"\n parallel_direct completed in  {end_time - start_time:.4f} seconds")
    return results

@cli.command()
@click.option('--limit', '-l', default=10, help='Number of Fibonacci numbers to generate')
def basic(limit):
    """Run the basic Fibonacci flow with iteration"""
    flow = create_basic_fibonacci_flow(limit=limit)
    flow_name = flow.name
    logger.debug(f"\n\n=== '{flow_name}' FLOW DEMONSTRATION ===\n{LINE_BREAK}")
    
    start_time = time.time()
    shared_context = {}
    
    logger.debug("Starting flow execution...")
    flow.run(shared_context)
    end_time = time.time()
    
    logger.debug(f"\n '{flow_name}' completed in  {end_time - start_time:.4f} seconds")

    # Print the final shared context
    logger.debug(f"\nFinal shared context:\n {shared_context}")   
    if "sequence" in shared_context:
        sequence = shared_context["sequence"]
        logger.debug(f"\nFibonacci sequence details:")
        logger.debug(f"  First few numbers: {sequence[:min(5, len(sequence))]}...")
        logger.debug(f"  Last number: {sequence[-1]}")
        logger.debug(f"  Total length: {len(sequence)}")
        logger.debug(f"  Current index: {shared_context.get('current_index', 'N/A')}")
    else:
        logger.debug("Warning: 'sequence' not found in shared context. Flow may not have executed correctly.")


@cli.command()
def batch():
    """Run the Fibonacci batch processing demonstration"""
    flow = create_fibonacci_batch_flow()
    flow_name = flow.name
    logger.debug(f"\n\n=== {flow_name} DEMONSTRATION ===\n{LINE_BREAK}")

    start_time = time.time()
    shared_context = {}
    flow.run(shared_context)
    end_time = time.time()
    
    logger.debug(f"\n {flow_name} completed in  {end_time - start_time:.4f} seconds")


@cli.command()
def parallel():
    """Run the Fibonacci parallel processing demonstration"""
    flow = create_parallel_fibonacci_flow()
    flow_name = flow.name
    logger.debug(f"\n\n=== {flow_name} DEMONSTRATION ===\n{LINE_BREAK}")
    
    start_time = time.time()
    shared_context = {}
    flow.run(shared_context)
    end_time = time.time()
    
    logger.debug(f"\n {flow_name} completed in  {end_time - start_time:.4f} seconds")


@cli.command()
def composite():
    """Run the composite Fibonacci flow demonstration"""
    flow = create_composite_fibonacci_flow()
    flow_name = flow.name 
    logger.debug(f"\n\n=== {flow_name} DEMONSTRATION ===\n{LINE_BREAK}")

    start_time = time.time()
    shared_context = {}
    flow.run(shared_context)
    end_time = time.time()
    
    logger.debug(f"\n {flow_name} completed in  {end_time - start_time:.4f} seconds")


@cli.command()
def compare():
    """Compare different Fibonacci implementations"""
    logger.debug(f"\n\n=== FIBONACCI IMPLEMENTATION COMPARISON ===\n{LINE_BREAK}")
    
    limit = 30  # Use the same sequence length for fair comparison
    
    # Test Flow-based implementations
    flow_implementations = {
        "Basic Flow": create_basic_fibonacci_flow(limit=limit),
        "Batch Processing": create_fibonacci_batch_flow(),
        "Composite Flow": create_composite_fibonacci_flow()
    }
    
    flow_results = {}
    for name, flow in flow_implementations.items():
        logger.debug(f"\nRunning {name}...")
        shared_context = {}
        
        start_time = time.time()
        flow.run(shared_context)
        end_time = time.time()
        
        execution_time = end_time - start_time
        flow_results[name] = execution_time
        logger.debug(f" {name} completed in  {execution_time:.6f} seconds")
    
    # Test direct implementations
    limits = [10, 30, 100]
    direct_implementations = {
        "Direct Sequential": lambda: parallel_fibonacci(limits=limits),
        "Direct Parallel": lambda: parallel_fibonacci_threaded(limits=limits)
    }
    
    direct_results = {}
    for name, func_ in direct_implementations.items():
        logger.debug(f"\nRunning {name}...")
        
        start_time = time.time()
        func_()
        end_time = time.time()
        
        execution_time = end_time - start_time
        direct_results[name] = execution_time
        logger.debug(f" {name} completed in  {execution_time:.6f} seconds")
    
    # Combine results
    all_results = {**flow_results, **direct_results}
    
    # Find the fastest implementation
    fastest = min(all_results.items(), key=lambda x: x[1])
    
    logger.debug(f"\n\n=== PERFORMANCE COMPARISON SUMMARY ===\n{LINE_BREAK}")
    for name, time_taken in all_results.items():
        speedup = time_taken / fastest[1]
        logger.debug(f"{name}: {time_taken:.6f}s ({speedup:.2f}x slower than fastest)")
    
    logger.debug(f"\nFastest implementation: {fastest[0]} ({fastest[1]:.6f}s)")
    
    # Additional insights
    logger.debug(f"\n\n=== IMPLEMENTATION INSIGHTS ===\n{LINE_BREAK}")
    logger.debug("• Flow-based vs Direct: Flow adds framework overhead but provides structure")
    logger.debug("• Sequential vs Parallel: Parallel shows advantage for larger workloads")
    logger.debug("• Composite approach: Reusing previous calculations optimizes performance")
    logger.debug("• Batch processing: Good for handling multiple similar tasks")
    
    # Calculate average times by category
    flow_avg = sum(flow_results.values()) / len(flow_results)
    direct_avg = sum(direct_results.values()) / len(direct_results)
    
    logger.debug(f"\nAverage times:")
    logger.debug(f"• Flow-based implementations: {flow_avg:.6f}s")
    logger.debug(f"• Direct implementations: {direct_avg:.6f}s")
    
    # Return results for potential further analysis
    return all_results
    
# @cli.command()
# def helpme():
#     file_name = Path(__file__).name
#     help_str = f"""
# python {file_name}  basic  --limit 15  # Run the basic Fibonacci flow with iteration
# python {file_name}  batch              # Run the Fibonacci batch processing demonstration
# python {file_name}  composite          # Run the composite Fibonacci flow demonstration

# python {file_name}  parallel           # Run the Fibonacci parallel processing demonstration 
# python {file_name}  parallel-direct    # Run direct parallel Fibonacci generation without...
# python {file_name}  parallel-threaded  # Run parallel Fibonacci generation using...

# python {file_name}  compare            Compare different Fibonacci implementations
#     """
#     logger.debug(help_str)

if __name__ == "__main__":
    cli()