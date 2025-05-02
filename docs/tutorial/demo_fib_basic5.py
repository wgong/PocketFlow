#!/usr/bin/env python3
"""
PocketFlow Basic Fibonacci Demo

A simplified demonstration of generating Fibonacci sequences using PocketFlow.
"""

import time
import click
import copy  # Required for the Flow class

# ===== SIMPLIFIED POCKETFLOW IMPLEMENTATION =====

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
        return None
    
    def exec(self, prep_res):
        """Execute node logic."""
        pass
    
    def _exec(self, prep_res):
        """Internal method to execute the node logic."""
        return self.exec(prep_res)
    
    def post(self, shared, prep_res, exec_res):
        """Post-processing after execution."""
        return "default"
    
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
        curr = self.start_node  # Don't copy the node
        p = params or self.params  # Just reference the params
        last_action = None
        
        print(f"Starting flow orchestration with node: {curr.__class__.__name__}")
        
        while curr:
            # Set parameters if needed
            if params:
                curr.set_params(p)
                
            # Run the current node
            print(f"Running node: {curr.__class__.__name__}")
            last_action = curr.run(shared)  # Use run instead of _run
            print(f"Node returned action: {last_action}")
            
            # Get the next node
            curr = self.get_next_node(curr, last_action)
            if curr:
                print(f"Next node: {curr.__class__.__name__}")
        
        print(f"Flow orchestration completed with action: {last_action}")
        return last_action
    
    def run(self, shared):
        """Run the flow with the given shared context."""
        # Always use orchestration for this flow
        print("Using orchestration for flow")
        return self._orch(shared)
    

# ===== FIBONACCI IMPLEMENTATION =====

def create_basic_fibonacci_flow(limit=10):
    """Create a flow for generating Fibonacci sequence."""
    
    # Create a node that will generate the Fibonacci sequence
    generate_node = Node()
    
    def generate_exec(prep_res):
        """Generate the Fibonacci sequence."""
        print("Generating Fibonacci sequence...")
        sequence = [0, 1]
        
        for i in range(2, limit):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
            
        print(f"Generated sequence with {len(sequence)} terms")
        return sequence
    
    def generate_post(shared, prep_res, exec_res):
        """Store the generated sequence in shared context."""
        sequence = exec_res
        
        if sequence is None:
            print("ERROR: No sequence generated!")
            return "error"
            
        print(f"Storing sequence in shared context ({len(sequence)} terms)")
        shared["sequence"] = sequence.copy()  # Make a copy to ensure it's stored
        shared["count"] = len(sequence)
        shared["last"] = sequence[-1] if sequence else None
        
        print(f"Shared context after update: {shared}")
        return "done"
    
    # Configure the node
    generate_node.exec = generate_exec
    generate_node.post = generate_post
    
    # Create and return the flow
    flow = Flow(start=generate_node)
    # Explicitly set the exec attribute to None to prevent direct execution
    flow.exec = None
    return flow

def generate_direct_fibonacci(limit=10):
    """Generate Fibonacci sequence directly without flow framework."""
    
    sequence = [0, 1]
    for i in range(2, limit):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    return {"sequence": sequence, "count": limit}


# ===== CLI COMMANDS =====

@click.group()
def cli():
    """Demo for Fibonacci sequence generation using PocketFlow."""
    pass


@cli.command()
@click.option('--limit', '-l', default=10, help='Number of Fibonacci numbers to generate')
def flow(limit):
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
    print(f"Flow returned: {result}")
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
    else:
        print("\nERROR: No sequence found in shared context!")


@cli.command()
@click.option('--limit', '-l', default=10, help='Number of Fibonacci numbers to generate')
def direct(limit):
    """Generate Fibonacci sequence directly without PocketFlow."""
    print("\n=== DIRECT FIBONACCI GENERATION ===")
    
    # Generate directly
    start_time = time.time()
    result = generate_direct_fibonacci(limit=limit)
    end_time = time.time()
    
    # Show results
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print("Result:")
    print(result)
    
    # Show sequence details
    if "sequence" in result:
        seq = result["sequence"]
        print("\nFibonacci sequence:")
        print(f"  First few numbers: {seq[:min(5, len(seq))]}...")
        print(f"  Last number: {seq[-1]}")
        print(f"  Length: {len(seq)}")


@cli.command()
@click.option('--limit', '-l', default=10, help='Number of Fibonacci numbers to generate')
def compare(limit):
    """Compare flow-based and direct Fibonacci generation."""
    print("\n=== FIBONACCI IMPLEMENTATION COMPARISON ===")
    
    # Flow-based generation
    print("\nRunning flow-based generation...")
    flow_context = {}
    flow = create_basic_fibonacci_flow(limit=limit)
    
    flow_start = time.time()
    flow.run(flow_context)
    flow_end = time.time()
    flow_time = flow_end - flow_start
    
    # Direct generation
    print("\nRunning direct generation...")
    direct_start = time.time()
    direct_result = generate_direct_fibonacci(limit=limit)
    direct_end = time.time()
    direct_time = direct_end - direct_start
    
    # Compare results
    print("\n=== RESULTS COMPARISON ===")
    print(f"Flow-based time:  {flow_time:.6f} seconds")
    print(f"Direct time:      {direct_time:.6f} seconds")
    print(f"Speed difference: {flow_time/direct_time:.2f}x")
    
    flow_seq = flow_context.get("sequence", [])
    direct_seq = direct_result.get("sequence", [])
    
    print(f"\nFlow sequence length:   {len(flow_seq)}")
    print(f"Direct sequence length: {len(direct_seq)}")
    
    if flow_seq == direct_seq:
        print("\nBoth methods produced identical sequences.")
    else:
        print("\nWARNING: Sequences differ!")
        print(f"Flow sequence: {flow_seq}")
        print(f"Direct sequence: {direct_seq}")


if __name__ == "__main__":
    cli()