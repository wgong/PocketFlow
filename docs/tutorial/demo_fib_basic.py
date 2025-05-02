#!/usr/bin/env python3
"""
PocketFlow Basic Fibonacci Demo

A focused demonstration of generating Fibonacci sequences using PocketFlow.
This script focuses on correctly passing shared context and generating sequences.
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
            print(f"Running node: {curr.__class__.__name__}")
            action = curr.run(shared)
            print(f"  Action returned: {action}")
            print(f"  Current shared context: {shared}")
            
            # Get the next node
            curr = self.get_next_node(curr, action)
        
        return action


# ===== FIBONACCI IMPLEMENTATIONS =====

def create_basic_fibonacci_flow(limit=10):
    """Create a flow for generating Fibonacci sequence."""
    print(f"Creating Fibonacci flow with limit={limit}")
    
    # Define individual nodes
    init_node = Node()
    generate_node = Node()
    check_node = Node()
    
    # Initialize node
    def init_exec(prep_res):
        print("Initializing sequence...")
        return [0, 1]
    
    def init_post(shared, prep_res, exec_res):
        sequence = exec_res
        shared["sequence"] = sequence
        shared["index"] = 1  # We've already generated 0 and 1
        print(f"Initialized sequence: {sequence}")
        return "check"
    
    init_node.exec = init_exec
    init_node.post = init_post
    
    # Generate node
    def generate_exec(prep_res):
        sequence = prep_res
        next_num = sequence[-1] + sequence[-2]
        print(f"Generating next number: {next_num}")
        return next_num
    
    def generate_prep(shared):
        return shared["sequence"]
    
    def generate_post(shared, prep_res, exec_res):
        next_num = exec_res
        shared["sequence"].append(next_num)
        shared["index"] += 1
        print(f"Added {next_num} to sequence. New length: {len(shared['sequence'])}")
        return "check"
    
    generate_node.prep = generate_prep
    generate_node.exec = generate_exec
    generate_node.post = generate_post
    
    # Check limit node
    def check_exec(prep_res):
        index = prep_res
        print(f"Checking if index {index} has reached limit {limit}...")
        return index >= limit - 1  # -1 because we start with 2 numbers
    
    def check_prep(shared):
        return shared["index"]
    
    def check_post(shared, prep_res, exec_res):
        is_done = exec_res
        if is_done:
            print("Reached limit. Sequence generation complete.")
            return "done"
        else:
            print("Limit not reached. Continuing generation.")
            return "continue"
    
    check_node.prep = check_prep
    check_node.exec = check_exec
    check_node.post = check_post
    
    # Connect nodes
    init_node.next(check_node, "check")
    check_node.next(generate_node, "continue")
    check_node.next(None, "done")  # End flow when done
    generate_node.next(check_node, "check")
    
    # Create flow
    flow = Flow(start=init_node)
    return flow


def generate_direct_fibonacci(limit=10):
    """Generate Fibonacci sequence directly without flow framework."""
    print(f"Generating Fibonacci sequence directly with limit={limit}")
    
    sequence = [0, 1]
    for i in range(2, limit):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    return {"sequence": sequence, "index": limit - 1}


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
    print("\nInitial shared context:", shared_context)
    
    # Execute flow
    start_time = time.time()
    result = fib_flow.run(shared_context)
    end_time = time.time()
    
    # Show results
    print("\nFlow execution complete.")
    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print("\nFinal shared context:")
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
    print("\nResult:")
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