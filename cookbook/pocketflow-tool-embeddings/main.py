import click
from pathlib import Path
from flow import create_embedding_flow


@click.command()
@click.option("--input", "input_path", default=None,
              help="Path to a text file to embed (default: use --text)")
@click.option("--text", default="What's the meaning of life?", show_default=True,
              help="Literal text to embed (ignored if --input is given)")
@click.option("--out", default=None,
              help="File path to save the embedding (e.g. output/embedding.txt)")
def main(input_path, text, out):
    if input_path:
        text = Path(input_path).read_text(encoding="utf-8").strip()

    shared = {"text": text}
    create_embedding_flow().run(shared)

    embedding = shared.get("embedding", [])
    click.echo(f"Text:                {text[:80]}")
    click.echo(f"Embedding dimension: {len(embedding)}")
    click.echo(f"First 5 values:      {embedding[:5]}")

    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(str(embedding), encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
