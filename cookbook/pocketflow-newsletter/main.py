import click
from pathlib import Path
from flow import create_newsletter_flow
from nodes import TOPICS


@click.command()
@click.option("--topics", default=None,
              help="Comma-separated extra topics (appended to built-in list)")
@click.option("--out", default="output/newsletter.md", show_default=True,
              help="File path to save the newsletter")
def main(topics, out):
    topic_list = list(TOPICS)
    if topics:
        topic_list.extend(t.strip() for t in topics.split(","))

    shared = {"topics": topic_list}
    click.echo(f"🤔 Curating newsletter from {len(topic_list)} topics...\n")
    create_newsletter_flow().run(shared)

    newsletter = shared.get("newsletter", "No newsletter generated.")
    click.echo("\n📰 Newsletter:\n")
    click.echo(newsletter)

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(newsletter, encoding="utf-8")
    click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
