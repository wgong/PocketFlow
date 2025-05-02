#!/usr/bin/env python3
"""
PocketFlow Fibonacci Demonstrations

This script demonstrates how to use PocketFlow to implement
Fibonacci sequence generation using different approaches:
- Basic flow
- Batch processing
- Parallel processing
- Composite nodes with incremental computation
"""

import asyncio
import copy
import time
import random
from typing import Dict, List, Any, Optional
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path
import click

class BaseNode:
    """Base class for all nodes in the flow framework."""
    
    def __init__(self):
        """Initialize a node with empty params and successors dictionaries."""
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
        """Internal method to run the full node execution cycle."""
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
    
    def __init__(self, max_retries=1, wait=0):
        """Initialize a node with retry capabilities."""
        super().__init__()
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
    """Node that processes a batch of items."""
    
    def _exec(self, items):
        """Execute the node logic on each item in the batch."""
        print(f"BatchNode._exec received {len(items) if items else 0} items")
        results = []
        
        for item in (items or []):
            try:
                result = self.exec(item)
                print(f"Processed batch item: {item.get('id', 'unknown')}, result: {type(result)}")
                results.append(result)
            except Exception as e:
                print(f"Error processing batch item: {e}")
        
        print(f"BatchNode._exec completed with {len(results)} results")
        return results



class Flow(BaseNode):
    """Orchestrates execution of multiple connected nodes."""
    
    def __init__(self, start=None):
        """Initialize a flow with an optional starting node."""
        super().__init__()
        self.start_node = start
    
    def start(self, start):
        """Set the starting node for this flow."""
        self.start_node = start
        return start
    
    def get_next_node(self, curr, action):
        """Find the next node to execute based on the current action."""
        return curr.successors.get(action or "default")
    
    def _orch(self, shared, params=None):
        """Orchestrate the execution of nodes in the flow."""
        curr = copy.copy(self.start_node)
        p = params or {**self.params}
        last_action = None
        
        while curr:
            curr.set_params(p)
            last_action = curr._run(shared)
            curr = copy.copy(self.get_next_node(curr, last_action))
        
        return last_action
    
    def _run(self, shared):
        """Run the entire flow."""
        p = self.prep(shared)
        o = self._orch(shared)
        return self.post(shared, p, o)
    
    def post(self, shared, prep_res, exec_res):
        """Return the final result of the flow execution."""
        return exec_res


class BatchFlow(Flow):
    """A flow that processes batches of parameters."""
    
    def _run(self, shared):
        """Run the flow for each set of parameters in the batch."""
        # Prepare the batch items
        batch_items = self.prep(shared) or []
        print(f"BatchFlow._run prepared {len(batch_items)} batch items")
        
        if not batch_items:
            print("Warning: No batch items to process")
            return self.post(shared, batch_items, [])
        
        # Process the batch with the start node
        if self.start_node:
            # Set parameters and run the start node directly with the batch
            self.start_node.set_params(self.params)
            batch_results = self.start_node._exec(batch_items)
            
            # Store the batch results in the shared context
            shared["batch_results"] = batch_results
            
            # Let the start node handle post-processing if needed
            action = self.start_node.post(shared, batch_items, batch_results)
            
            # Return the final results via post method
            return self.post(shared, batch_items, batch_results)
        else:
            print("Error: No start node defined for batch flow")
            return self.post(shared, batch_items, [])


# ----- FIBONACCI DEMONSTRATIONS -----

def create_basic_fibonacci_flow(limit=10):
    """Create a flow that generates a Fibonacci sequence up to the specified limit."""
    
    # Define nodes
    init_node = Node()
    generate_node = Node()
    check_limit_node = Node()
    
    # Configure initialization node
    def init_exec(prep_res):
        print("Initializing Fibonacci sequence...")
        # Return dummy result, actual work in post
        return None
    
    def init_post(shared, prep_res, exec_res):
        # Initialize the sequence with first two numbers
        shared["sequence"] = [0, 1]
        shared["current_index"] = 1
        print(f"Initialized sequence: {shared['sequence']}")
        # Go to check node
        return "default"
    
    init_node.exec = init_exec
    init_node.post = init_post
    
    # Configure generation node
    def generate_exec(prep_res):
        print("Generating next Fibonacci number...")
        # Return dummy result, actual work in post
        return None
    
    def generate_post(shared, prep_res, exec_res):
        # Calculate and add the next Fibonacci number
        sequence = shared["sequence"]
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
        shared["current_index"] += 1
        print(f"Generated: {next_num}, new sequence length: {len(shared['sequence'])}")
        # Always go back to check node
        return "default"
    
    generate_node.exec = generate_exec
    generate_node.post = generate_post
    
    # Configure limit check node
    def check_limit_exec(prep_res):
        print("Checking if we've reached the limit...")
        # Return dummy result, actual work in post
        return None
    
    def check_limit_post(shared, prep_res, exec_res):
        # Check if we've reached the limit
        current_index = shared["current_index"]
        print(f"Current index: {current_index}, limit: {limit}")
        
        if current_index < limit - 1:  # -1 because we start with 2 numbers
            print(f"Continuing generation ({current_index + 1} of {limit})...")
            # Go to generate node
            return "continue"
        else:
            print(f"Reached limit. Sequence complete with {len(shared['sequence'])} terms")
            # End the flow
            return "done"
    
    check_limit_node.exec = check_limit_exec
    check_limit_node.post = check_limit_post
    
    # Connect nodes - FIXED CONNECTION METHOD
    # init -> check -> generate -> check -> ... -> done
    init_node.next(check_limit_node)
    check_limit_node.next(generate_node, "continue")
    check_limit_node.next(None, "done")  # End flow on "done"
    generate_node.next(check_limit_node)
    
    # Create the flow
    fib_flow = Flow(start=init_node)
    return fib_flow


def create_fibonacci_node():
    """Create a node that generates a Fibonacci sequence."""
    
    fib_node = BatchNode()
    
    def generate_fibonacci(params):
        """Generate Fibonacci sequence up to the specified limit."""
        limit = params.get("limit", 10)
        
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
    
    fib_node.exec = generate_fibonacci
    return fib_node

def create_fibonacci_batch_flow():
    """Create a batch flow for generating multiple Fibonacci sequences."""
    
    # Create a batch processor node
    fib_node = BatchNode()
    
    # Define the execution function that processes a single batch item
    def generate_fibonacci(params):
        """Generate Fibonacci sequence for a single batch item."""
        limit = params.get("limit", 10)
        print(f"Generating Fibonacci sequence with limit={limit}")
        
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
        print(f"Generated Fibonacci sequence with limit={limit}, length={len(sequence)}")
        return result
    
    # Configure the batch node
    fib_node.exec = generate_fibonacci
    
    # Define post-processing for batch node
    def fib_node_post(shared, prep_res, exec_res):
        print(f"Fibonacci node post-processing: {len(exec_res) if exec_res else 0} results")
        # Results will be handled by the flow's post method
        return "default"
    
    fib_node.post = fib_node_post
    
    # Create the batch flow
    batch_flow = BatchFlow(start=fib_node)
    
    # Prepare batch parameters
    def prep_batch(shared):
        print("Preparing batch of Fibonacci sequence parameters...")
        batch_params = [
            {"limit": 10, "id": "small"},
            {"limit": 30, "id": "medium"},
            {"limit": 100, "id": "large"}
        ]
        print(f"Created {len(batch_params)} batch items")
        return batch_params
    
    # Post-process the batch results
    def post_batch(shared, prep_res, exec_res):
        print(f"Batch flow post-processing: {len(exec_res) if exec_res else 0} results")
        
        # Display the results
        print("\nFibonacci Sequences Generated:")
        
        if not exec_res:
            print("Warning: No results found.")
            return "completed"
        
        # Process and display the results
        for result in exec_res:
            limit = result.get("limit", "unknown")
            sequence = result.get("sequence", [])
            last_number = result.get("last_number", None)
            
            print(f"\nSequence with limit {limit}:")
            print(f"  • First few numbers: {sequence[:min(5, len(sequence))]}...")
            print(f"  • Last number: {last_number}")
            print(f"  • Total numbers: {len(sequence)}")
        
        return "completed"
    
    # Configure the flow
    batch_flow.prep = prep_batch
    batch_flow.post = post_batch
    
    return batch_flow


def create_parallel_fibonacci_flow():
    """Create a flow for parallel processing of Fibonacci sequences."""
    
    # Create a custom flow for parallel processing
    parallel_flow = Flow()
    
    def generate_fibonacci(limit):
        """Generate Fibonacci sequence up to the specified limit."""
        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    def prep_parallel(shared):
        print("Preparing parallel Fibonacci sequence generation...")
        return [10, 30, 100]  # The limits we want to process
    
    def exec_parallel(limits):
        print(f"Executing parallel Fibonacci sequence generation for limits: {limits}")
        
        # Define a list to store results
        results = []
        
        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=3) as executor:
            # Submit tasks to the executor
            future_to_limit = {executor.submit(generate_fibonacci, limit): limit for limit in limits}
            
            # Collect results as they complete
            for future in future_to_limit:
                try:
                    result = future.result()
                    results.append(result)
                    print(f"Completed sequence with limit {result['limit']}")
                except Exception as exc:
                    print(f"Generated an exception: {exc}")
        
        return results
    
    def post_parallel(shared, prep_res, exec_res):
        print(f"\nParallel processing complete. Results: {len(exec_res)} sequences")
        shared["parallel_results"] = exec_res  # Store in shared context
        
        # Sort results by limit for consistent display
        sorted_results = sorted(exec_res, key=lambda x: x["limit"])
        
        for result in sorted_results:
            limit = result["limit"]
            sequence = result["sequence"]
            last_number = result["last_number"]
            
            print(f"\nSequence with limit {limit}:")
            print(f"  • First few numbers: {sequence[:5]}...")
            print(f"  • Last number: {last_number}")
            print(f"  • Total numbers: {len(sequence)}")
        
        return "completed"
    
    # Configure the parallel flow
    parallel_flow.prep = prep_parallel
    parallel_flow.exec = exec_parallel
    parallel_flow.post = post_parallel
    
    return parallel_flow

def create_composite_fibonacci_flow():
    """
    Create a composite flow that builds Fibonacci sequences incrementally:
    1. First calculates sequence with limit=10
    2. Uses that to calculate sequence with limit=30
    3. Finally uses that to calculate sequence with limit=100
    """
    
    # Create individual nodes for each sequence length
    fib_node_10 = Node()
    fib_node_30 = Node()
    fib_node_100 = Node()
    
    # Node for limit=10 calculation
    def calculate_fib_10(prep_res):
        print("Calculating Fibonacci sequence with limit=10...")
        sequence = [0, 1]
        while len(sequence) < 10:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
    def post_fib_10(shared, prep_res, exec_res):
        # Store result in shared context
        sequence = exec_res
        shared["fib_10"] = sequence
        print(f"Generated sequence with limit=10: {sequence[:5]}... (length: {len(sequence)})")
        return "continue"
    
    fib_node_10.exec = calculate_fib_10
    fib_node_10.post = post_fib_10
    
    # Node for limit=30 calculation (builds on limit=10)
    def calculate_fib_30(prep_res):
        print("Calculating Fibonacci sequence with limit=30 (building from limit=10)...")
        # Get the base sequence from parameters
        base_sequence = prep_res  # Passed from prep function
        
        if not base_sequence:
            raise ValueError("Base sequence not found")
        
        # Continue from where we left off
        sequence = base_sequence.copy()
        while len(sequence) < 30:
            sequence.append(sequence[-1] + sequence[-2])
        
        return sequence
    
    def prep_fib_30(shared):
        # Get the result from the previous calculation
        base_sequence = shared.get("fib_10", [])
        print(f"Using base sequence of length {len(base_sequence)}")
        return base_sequence
    
    def post_fib_30(shared, prep_res, exec_res):
        # Store result in shared context
        sequence = exec_res
        shared["fib_30"] = sequence
        print(f"Generated sequence with limit=30: {sequence[:5]}... (length: {len(sequence)})")
        return "continue"
    
    fib_node_30.prep = prep_fib_30
    fib_node_30.exec = calculate_fib_30
    fib_node_30.post = post_fib_30
    
    # Node for limit=100 calculation (builds on limit=30)
    def calculate_fib_100(prep_res):
        print("Calculating Fibonacci sequence with limit=100 (building from limit=30)...")
        # Get the base sequence from parameters
        base_sequence = prep_res  # Passed from prep function
        
        if not base_sequence:
            raise ValueError("Base sequence not found")
        
        # Continue from where we left off
        sequence = base_sequence.copy()
        while len(sequence) < 100:
            sequence.append(sequence[-1] + sequence[-2])
        
        return sequence
    
    def prep_fib_100(shared):
        # Get the result from the previous calculation
        base_sequence = shared.get("fib_30", [])
        print(f"Using base sequence of length {len(base_sequence)}")
        return base_sequence
    
    def post_fib_100(shared, prep_res, exec_res):
        # Store result in shared context
        sequence = exec_res
        shared["fib_100"] = sequence
        print(f"Generated sequence with limit=100: {sequence[:5]}... (length: {len(sequence)})")
        
        # Print final results
        print("\nFinal Fibonacci Sequences:")
        print(f"Sequence (10): Last number = {shared['fib_10'][-1]}")
        print(f"Sequence (30): Last number = {shared['fib_30'][-1]}")
        print(f"Sequence (100): Last number = {shared['fib_100'][-1]}")
        
        return "done"
    
    fib_node_100.prep = prep_fib_100
    fib_node_100.exec = calculate_fib_100
    fib_node_100.post = post_fib_100
    
    # Connect nodes in sequence - FIXED CONNECTION METHOD
    fib_node_10.next(fib_node_30, "continue")
    fib_node_30.next(fib_node_100, "continue")
    fib_node_100.next(None, "done")  # Explicitly end flow
    
    # Create the flow
    composite_flow = Flow(start=fib_node_10)
    return composite_flow

# ----- CLICK CLI COMMANDS -----

@click.group()
def cli():
    """Fibonacci sequence generation with PocketFlow - Demo CLI"""
    pass


@cli.command()
@click.option('--limit', '-l', default=10, help='Number of Fibonacci numbers to generate')
def basic(limit):
    """Run the basic Fibonacci flow with iteration"""
    print("\n=== BASIC FIBONACCI FLOW DEMONSTRATION ===")
    flow = create_basic_fibonacci_flow(limit=limit)
    
    start_time = time.time()
    shared_context = {}
    
    print("Starting flow execution...")
    flow.run(shared_context)
    end_time = time.time()
    
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")

    # Print the final shared context
    print("\nFinal shared context:")
    print(shared_context)
    
    # Access specific values for the basic flow
    if "sequence" in shared_context:
        sequence = shared_context["sequence"]
        print(f"\nFibonacci sequence details:")
        print(f"  First few numbers: {sequence[:min(5, len(sequence))]}...")
        print(f"  Last number: {sequence[-1]}")
        print(f"  Total length: {len(sequence)}")
        print(f"  Current index: {shared_context.get('current_index', 'N/A')}")
    else:
        print("Warning: 'sequence' not found in shared context. Flow may not have executed correctly.")


@cli.command()
def batch():
    """Run the Fibonacci batch processing demonstration"""
    print("\n=== FIBONACCI BATCH PROCESSING DEMONSTRATION ===")
    batch_flow = create_fibonacci_batch_flow()
    
    start_time = time.time()
    shared_context = {}
    batch_flow.run(shared_context)
    end_time = time.time()
    
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")


@cli.command()
def parallel():
    """Run the Fibonacci parallel processing demonstration"""
    print("\n=== FIBONACCI PARALLEL PROCESSING DEMONSTRATION ===")
    parallel_flow = create_parallel_fibonacci_flow()
    
    start_time = time.time()
    shared_context = {}
    parallel_flow.run(shared_context)
    end_time = time.time()
    
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")


@cli.command()
def composite():
    """Run the composite Fibonacci flow demonstration"""
    print("\n=== COMPOSITE FIBONACCI FLOW DEMONSTRATION ===")
    composite_flow = create_composite_fibonacci_flow()
    
    start_time = time.time()
    shared_context = {}
    composite_flow.run(shared_context)
    end_time = time.time()
    
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")


@cli.command()
def compare():
    """Compare different Fibonacci implementations"""
    print("\n=== FIBONACCI IMPLEMENTATION COMPARISON ===")
    
    implementations = {
        "Basic Flow": create_basic_fibonacci_flow(limit=30),
        "Batch Processing": create_fibonacci_batch_flow(),
        "Parallel Processing": create_parallel_fibonacci_flow(),
        "Composite Flow": create_composite_fibonacci_flow()
    }
    
    results = {}
    
    for name, flow in implementations.items():
        print(f"\nRunning {name}...")
        shared_context = {}
        
        start_time = time.time()
        flow.run(shared_context)
        end_time = time.time()
        
        execution_time = end_time - start_time
        results[name] = execution_time
        print(f"{name} execution time: {execution_time:.4f} seconds")
    
    # Find the fastest implementation
    fastest = min(results.items(), key=lambda x: x[1])
    
    print("\n=== PERFORMANCE COMPARISON SUMMARY ===")
    for name, time_taken in results.items():
        speedup = time_taken / fastest[1]
        print(f"{name}: {time_taken:.4f}s ({speedup:.2f}x slower than fastest)")
    
    print(f"\nFastest implementation: {fastest[0]} ({fastest[1]:.4f}s)")

    
@cli.command()
def helpme():
    file_name = Path(__file__).name
    help_str = f"""
python {file_name} basic --limit 15  # Run basic flow with custom limit
python {file_name} batch             # Run batch processing
python {file_name} parallel          # Run parallel processing
python {file_name} composite         # Run composite node flow
python {file_name} compare           # Compare all implementations

    """
    print(help_str)

if __name__ == "__main__":
    cli()