import click
from pathlib import Path
from flow import create_code_generator_flow

DEFAULT_PROBLEM = """\
Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. Each input has exactly one solution.

Example 1: nums = [2,7,11,15], target = 9  -> [0,1]
Example 2: nums = [3,2,4],     target = 6  -> [1,2]
Example 3: nums = [3,3],       target = 6  -> [0,1]\
"""


@click.command()
@click.option("--input", "input_path", default=None,
              help="Path to a file containing the coding problem (e.g. data/problem.txt)")
@click.option("--problem", default=None,
              help="Coding problem as a literal string (overrides --input; default: Two Sum)")
@click.option("--max-iterations", default=5, show_default=True,
              help="Max self-healing iterations")
@click.option("--out", default="output/solution.py", show_default=True,
              help="File path to save the generated function code")
def main(input_path, problem, max_iterations, out):
    if problem:
        prob_text = problem
    elif input_path:
        prob_text = Path(input_path).read_text(encoding="utf-8")
    else:
        prob_text = DEFAULT_PROBLEM

    click.echo("Starting PocketFlow Code Generator...")
    shared = {
        "problem": prob_text,
        "test_cases": [],
        "function_code": "",
        "test_results": [],
        "iteration_count": 0,
        "max_iterations": max_iterations,
    }
    create_code_generator_flow().run(shared)

    passed = len([r for r in shared["test_results"] if r["passed"]])
    total  = len(shared["test_results"])
    click.echo("\n=== Final Results ===")
    click.echo(f"Problem:    {prob_text[:60]}...")
    click.echo(f"Iterations: {shared['iteration_count']}")
    click.echo(f"Tests:      {passed}/{total} passed")
    click.echo(f"Function:\n{shared['function_code']}")

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(shared["function_code"], encoding="utf-8")
    click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
