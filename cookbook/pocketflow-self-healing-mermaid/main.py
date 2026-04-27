import click
from pathlib import Path
from flow import create_mermaid_flow

DEFAULT_TASK = (
    "A flowchart showing a CI/CD pipeline: code push triggers build, "
    "then parallel test and lint, then deploy to staging, "
    "manual approval, deploy to production"
)


@click.command()
@click.option("--task", default=DEFAULT_TASK, show_default=False,
              help="Description of the Mermaid diagram to generate")
@click.option("--out", default="output/diagram.md", show_default=True,
              help="File path to save the Mermaid code")
def main(task, out):
    click.echo("🎨 PocketFlow Self-Healing Mermaid Generator\n")
    click.echo(f"🤔 Task: {task}\n")
    shared = {"task": task}
    create_mermaid_flow().run(shared)

    click.echo("\n=== Result ===")
    chart = shared.get("chart", "")
    if chart:
        attempts = shared.get("attempts", [])
        if attempts and len(attempts) >= 3:
            click.echo(f"  Status: FAILED after {len(attempts)} attempts")
            click.echo(f"  Last error: {attempts[-1]['error'][:200]}")
        else:
            n = len(attempts)
            retry_word = "y" if n == 1 else "ies"
            status_detail = "(first attempt)" if n == 0 else f"(after {n} retr{retry_word})"
            click.echo(f"  Status: SUCCESS  {status_detail}")
        click.echo("\n  Mermaid code:\n")
        for line in chart.split("\n"):
            click.echo(f"    {line}")
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(chart, encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
