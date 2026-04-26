import click
from pathlib import Path
from flow import flow

DEFAULT_TEXT = (
    "PocketFlow is a minimalist LLM framework that models workflows as a Nested Directed Graph. "
    "Nodes handle simple LLM tasks, connecting through Actions for Agents. "
    "Flows orchestrate these nodes for Task Decomposition, and can be nested. "
    "It also supports Batch processing and Async execution."
)


@click.command()
@click.option("--input", "input_path", default=None,
              help="Path to a text file to summarize (default: built-in PocketFlow description)")
@click.option("--out", default=None, help="File path to save the summary (e.g. output/summary.md)")
def main(input_path, out):
    if input_path:
        text = Path(input_path).read_text(encoding="utf-8")
    else:
        text = DEFAULT_TEXT

    shared = {"data": text}
    flow.run(shared)

    summary = shared.get("summary", "")
    click.echo(f"\nInput:   {text[:80]}...")
    click.echo(f"\nSummary: {summary}")
    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(summary, encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
