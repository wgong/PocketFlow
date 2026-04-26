import click
from pathlib import Path
from flow import create_podcast_flow
from utils import DOCS


@click.command()
@click.option("--out", default="output/podcast.mp3", show_default=True,
              help="File path to save the generated podcast audio")
def main(out):
    """Generate a podcast from documents using TTS."""
    Path(out).parent.mkdir(parents=True, exist_ok=True)

    shared = {
        "docs": DOCS,
        "output_file": out,
    }

    click.echo("Starting Podcast Generation Pipeline")
    click.echo("=" * 50)
    click.echo(f"  {len(DOCS)} source documents")
    click.echo(f"  Output: {out}")
    click.echo()
    click.echo("Step 1 — Analyzing documents for interesting nuggets")
    click.echo("Step 2 — Writing conversational podcast script")
    click.echo("Step 3 — Converting script to audio with TTS")
    click.echo()

    create_podcast_flow().run(shared)

    audio_file = shared.get("audio_file", out)
    click.echo("=" * 50)
    click.echo(f"Podcast saved to: {audio_file}")
    click.echo("=" * 50)


if __name__ == "__main__":
    main()
