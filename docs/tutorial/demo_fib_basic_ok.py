#!/usr/bin/env python3
"""
PocketFlow Basic Fibonacci Demo

A simplified demonstration of generating Fibonacci sequences using PocketFlow.
"""

import time
import click

# ===== SIMPLIFIED POCKETFLOW IMPLEMENTATION =====

class Node:
    """Basic node for processing."""
    
    def __init__(self):
        """Initialize a node."""
        self.params = {}
        self.successors = {}
    
    def next(self, node, action="default"):
        """Connect this node to another with an action."""
        self.successors[action] = node
        return node
    
    def prep(self, shared):
        """Prepare for execution."""
        return None
    
    def exec(self, prep_res):
        """Execute node logic."""
        pass
    
    def post(self, shared, prep_res, exec_res):
        """Post-process results."""
        return "default"
    
    def run(self, shared):
        """Run the node."""
        prep_res = self.prep(shared)
        exec_res = self.exec(prep_res)
        return self.post(shared, prep_res, exec_res)


class Flow:
    """Orchestrates node execution."""
    
    def __init__(self, start=None):
        """Initialize with a starting node."""
        self.start_node = start
    
    def get_next_node(self, curr, action):
        """Get the next node based on the action."""
        return curr.successors.get(action or "default")
    
    def run(self, shared):
        """Run the flow with shared context."""
        curr = self.start_node
        action = None
        
        while curr:
            action = curr.run(shared)
            curr = self.get_next_node(curr, action)
        
        return action


# ===== FIBONACCI IMPLEMENTATION =====

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