import click
from pathlib import Path
from flow import create_vision_flow


@click.command()
@click.option("--out", default="output/extracted_text.md", show_default=True,
              help="File path to save the extracted text")
def main(out):
    """Extract text from PDF files in the data/ folder using vision LLM."""
    shared = {}
    create_vision_flow().run(shared)

    lines = []
    for result in shared.get("results", []):
        click.echo(f"\nFile: {result['filename']}")
        click.echo("-" * 50)
        click.echo(result["text"])
        lines.append(f"## {result['filename']}\n\n{result['text']}\n")

    if lines:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text("\n".join(lines), encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
