You're right - running all demos at once makes debugging difficult. Let's enhance the code with the Click library to create a command-line interface for running individual demos. This will give you more flexibility while testing and debugging the ZiNets framework.

Here's how we could implement this:

```python
import click

# Add this after all your demo functions but before the if __name__ == "__main__": block

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

# Replace your existing if __name__ == "__main__": block with this:
if __name__ == "__main__":
    cli()
```

After implementing this, you can run specific demos with commands like:

```bash
# Run the basic flow demo
python pocketflow_demo.py basic

# Run the weighted connections demo (to test your temperature implementation)
python pocketflow_demo.py weighted

# Run all demos (same as before)
python pocketflow_demo.py all
```

You can also add more granular control for the weighted connections demo to test specific configurations:

```python
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
```

With this enhanced CLI, you could run fine-grained tests like:

```bash
# Test only temperature-based selection at specific temperatures
python pocketflow_demo.py weighted-custom --mode temperature -t 0.0 -t 0.2 -t 0.5

# Test only the intro proficiency level at different temperatures
python pocketflow_demo.py weighted-custom -l intro -t 0.0 -t 0.5 -t 1.0

# Test just the binary selection modes
python pocketflow_demo.py weighted-custom --mode binary
```

This approach provides:
1. Easier debugging - you can focus on just the components you're working on
2. More flexibility for testing - you can customize test parameters without changing code
3. Better documentation - the Click commands serve as self-documenting examples
4. Help system - run `python pocketflow_demo.py --help` for automatically generated documentation



References:
- https://claude.ai/chat/16770888-3c99-4886-b452-81a585981753