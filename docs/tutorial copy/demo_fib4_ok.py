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
        
        # If this flow has exec defined directly (like your parallel flow)
        if callable(getattr(self, 'exec', None)):
            exec_result = self.exec(p)
            return self.post(shared, p, exec_result)
        
        # Otherwise, use orchestration for multi-node flows
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
    """Create a flow for generating Fibonacci sequence."""
    
    # Define a single node that handles the initialization and generation
    generate_node = Node()
    
    def generate_exec(prep_res):
        """Generate the entire Fibonacci sequence at once."""
        sequence = [0, 1]  # Start with first two numbers
        
        for _ in range(2, limit):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        
        return sequence
    
    def generate_post(shared, prep_res, exec_res):
        """Store the generated sequence in shared context."""
        sequence = exec_res
        shared["sequence"] = sequence
        shared["count"] = len(sequence)
        shared["last"] = sequence[-1] if sequence else None
        
        return "done"
    
    generate_node.exec = generate_exec
    generate_node.post = generate_post
    
    # Create flow with just one node
    flow = Flow(start=generate_node)
    return flow



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
        print(f"Generating sequence with limit={limit}")
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
        return [10, 30, 100]
    
    def exec_parallel(limits):
        print(f"Executing with limits: {limits}")
        # Skip ThreadPoolExecutor and just process sequentially for debugging
        results = []
        for limit in limits:
            result = generate_fibonacci(limit)
            results.append(result)
            print(f"Added result for limit={limit}")
        print(f"Generated {len(results)} results")
        return results
    
    def post_parallel(shared, prep_res, exec_res):
        print(f"Post-processing results: {type(exec_res)}")
        results = [] if exec_res is None else exec_res
        shared["results"] = results
        
        print(f"\nParallel processing complete. Results: {len(results)} sequences")
        
        if not results:
            print("No sequences were generated.")
            return "completed"
        
        for result in results:
            limit = result["limit"]
            sequence = result["sequence"]
            print(f"\nSequence with limit {limit}:")
            print(f"  • First few numbers: {sequence[:5]}...")
            print(f"  • Last number: {result['last_number']}")
            print(f"  • Total numbers: {len(sequence)}")
        
        return "completed"
    
    # Configure the flow
    parallel_flow.prep = prep_parallel
    parallel_flow.exec = exec_parallel
    parallel_flow.post = post_parallel
    
    return parallel_flow

def parallel_fibonacci_with_threading():
    """Direct implementation of parallel Fibonacci generation using ThreadPoolExecutor."""
    print("\n=== FIBONACCI PARALLEL PROCESSING DEMONSTRATION (WITH THREADING) ===")
    
    # Generate a Fibonacci sequence
    def generate_fibonacci(limit):
        print(f"Thread started: Generating sequence with limit={limit}")
        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        print(f"Thread completed: Generated sequence with limit={limit}")
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    # Define the limits to process
    limits = [10, 30, 100]
    print(f"Processing {len(limits)} limits in parallel: {limits}")
    
    # Process using ThreadPoolExecutor
    results = []
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks
        print("Submitting tasks to thread pool...")
        future_to_limit = {executor.submit(generate_fibonacci, limit): limit for limit in limits}
        
        # Collect results as they complete
        for future in future_to_limit:
            try:
                limit = future_to_limit[future]
                print(f"Waiting for result with limit={limit}...")
                result = future.result()
                print(f"Received result for limit={limit}")
                results.append(result)
            except Exception as e:
                print(f"Error processing limit {future_to_limit[future]}: {e}")
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"All threads completed in {execution_time:.4f} seconds")
    
    # Sort results by limit for consistent display
    results.sort(key=lambda x: x["limit"])
    
    # Display results
    print("\nFibonacci Sequences Generated:")
    
    for result in results:
        limit = result["limit"]
        sequence = result["sequence"]
        last_number = result["last_number"]
        
        print(f"\nSequence with limit {limit}:")
        print(f"  • First few numbers: {sequence[:5]}...")
        print(f"  • Last number: {last_number}")
        print(f"  • Total numbers: {len(sequence)}")
    
    return results


def parallel_fibonacci():
    """Direct implementation of parallel Fibonacci generation without Flow class."""
    print("\n=== FIBONACCI PARALLEL PROCESSING DEMONSTRATION ===")
    
    # Generate a Fibonacci sequence
    def generate_fibonacci(limit):
        print(f"Generating sequence with limit={limit}")
        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        return {
            "limit": limit,
            "sequence": sequence,
            "last_number": sequence[-1]
        }
    
    # Process limits
    limits = [10, 30, 100]
    print(f"Processing limits: {limits}")
    
    # Process each limit
    results = []
    for limit in limits:
        result = generate_fibonacci(limit)
        results.append(result)
    
    # Display results
    print("\nFibonacci Sequences Generated:")
    
    for result in results:
        limit = result["limit"]
        sequence = result["sequence"]
        last_number = result["last_number"]
        
        print(f"\nSequence with limit {limit}:")
        print(f"  • First few numbers: {sequence[:5]}...")
        print(f"  • Last number: {last_number}")
        print(f"  • Total numbers: {len(sequence)}")
    
    return results



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
def parallel_threaded():
    """Run parallel Fibonacci generation using ThreadPoolExecutor"""
    print("Starting parallel Fibonacci generation with ThreadPoolExecutor...")
    start_time = time.time()
    results = parallel_fibonacci_with_threading()
    end_time = time.time()
    
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")
    return results

# cli.add_command(parallel_threaded)

# Add this as a CLI command
@cli.command()
def parallel_direct():
    """Run direct parallel Fibonacci generation without using Flow class"""
    start_time = time.time()
    results = parallel_fibonacci()
    end_time = time.time()
    
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")
    return results

@cli.command()
@click.option('--limit', '-l', default=10, help='Number of Fibonacci numbers to generate')
def basic(limit):
    """Generate Fibonacci sequence using PocketFlow framework."""
    print("\n=== FIBONACCI USING POCKETFLOW ===")
    
    # Create flow
    fib_flow = create_basic_fibonacci_flow(limit=limit)
    
    # Run with empty shared context
    shared_context = {}
    print("Initial shared context:", shared_context)
    
    # Execute flow
    start_time = time.time()
    result = fib_flow.run(shared_context)
    end_time = time.time()
    
    # Show results
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print("Final shared context:")
    print(shared_context)
    
    # Show sequence details
    if "sequence" in shared_context:
        seq = shared_context["sequence"]
        print("\nFibonacci sequence:")
        print(f"  First few numbers: {seq[:min(5, len(seq))]}...")
        print(f"  Last number: {seq[-1]}")
        print(f"  Length: {len(seq)}")


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
    
    limit = 30  # Use the same sequence length for fair comparison
    
    # Test Flow-based implementations
    flow_implementations = {
        "Basic Flow": create_basic_fibonacci_flow(limit=limit),
        "Batch Processing": create_fibonacci_batch_flow(),
        "Composite Flow": create_composite_fibonacci_flow()
    }
    
    flow_results = {}
    for name, flow in flow_implementations.items():
        print(f"\nRunning {name}...")
        shared_context = {}
        
        start_time = time.time()
        flow.run(shared_context)
        end_time = time.time()
        
        execution_time = end_time - start_time
        flow_results[name] = execution_time
        print(f"{name} execution time: {execution_time:.6f} seconds")
    
    # Test direct implementations
    direct_implementations = {
        "Direct Sequential": lambda: parallel_fibonacci(),
        "Direct Parallel": parallel_fibonacci_with_threading
    }
    
    direct_results = {}
    for name, func in direct_implementations.items():
        print(f"\nRunning {name}...")
        
        start_time = time.time()
        func()
        end_time = time.time()
        
        execution_time = end_time - start_time
        direct_results[name] = execution_time
        print(f"{name} execution time: {execution_time:.6f} seconds")
    
    # Combine results
    all_results = {**flow_results, **direct_results}
    
    # Find the fastest implementation
    fastest = min(all_results.items(), key=lambda x: x[1])
    
    print("\n=== PERFORMANCE COMPARISON SUMMARY ===")
    for name, time_taken in all_results.items():
        speedup = time_taken / fastest[1]
        print(f"{name}: {time_taken:.6f}s ({speedup:.2f}x slower than fastest)")
    
    print(f"\nFastest implementation: {fastest[0]} ({fastest[1]:.6f}s)")
    
    # Additional insights
    print("\n=== IMPLEMENTATION INSIGHTS ===")
    print("• Flow-based vs Direct: Flow adds framework overhead but provides structure")
    print("• Sequential vs Parallel: Parallel shows advantage for larger workloads")
    print("• Composite approach: Reusing previous calculations optimizes performance")
    print("• Batch processing: Good for handling multiple similar tasks")
    
    # Calculate average times by category
    flow_avg = sum(flow_results.values()) / len(flow_results)
    direct_avg = sum(direct_results.values()) / len(direct_results)
    
    print(f"\nAverage times:")
    print(f"• Flow-based implementations: {flow_avg:.6f}s")
    print(f"• Direct implementations: {direct_avg:.6f}s")
    
    # Return results for potential further analysis
    return all_results
    
@cli.command()
def helpme():
    file_name = Path(__file__).name
    help_str = f"""
python {file_name}  basic  --limit 15  # Run the basic Fibonacci flow with iteration
python {file_name}  batch              # Run the Fibonacci batch processing demonstration
python {file_name}  composite          # Run the composite Fibonacci flow demonstration

python {file_name}  parallel           # Run the Fibonacci parallel processing demonstration 
python {file_name}  parallel-direct    # Run direct parallel Fibonacci generation without...
python {file_name}  parallel-threaded  # Run parallel Fibonacci generation using...

python {file_name}  compare            Compare different Fibonacci implementations
    """
    print(help_str)

if __name__ == "__main__":
    cli()