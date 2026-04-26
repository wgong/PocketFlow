import click
from flow import create_resume_processing_flow


@click.command()
def main():
    """Map-reduce pipeline: evaluate resumes in parallel and reduce to a ranked summary."""
    shared = {}
    click.echo("Starting resume qualification processing...")
    create_resume_processing_flow().run(shared)
    if "summary" in shared:
        click.echo("\nDetailed evaluation results:")
        for filename, evaluation in shared.get("evaluations", {}).items():
            qualified = "✓" if evaluation.get("qualifies", False) else "✗"
            name = evaluation.get("candidate_name", "Unknown")
            click.echo(f"  {qualified} {name} ({filename})")
    click.echo("\nResume processing complete!")


if __name__ == "__main__":
    main()
