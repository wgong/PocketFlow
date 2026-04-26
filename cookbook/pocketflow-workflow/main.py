import click
from pathlib import Path
from flow import create_article_flow


@click.command()
@click.option("--topic", default="AI Safety", show_default=True,
              help="Topic for the article writing workflow")
@click.option("--out", default="output/article.md", show_default=True,
              help="File path to save the final article")
def main(topic, out):
    shared = {"topic": topic}
    click.echo(f"\n=== Article Workflow: {topic} ===\n")
    create_article_flow().run(shared)

    click.echo("\n=== Workflow Completed ===")
    click.echo(f"Topic:          {shared['topic']}")
    click.echo(f"Outline length: {len(shared.get('outline', ''))} chars")
    click.echo(f"Draft length:   {len(shared.get('draft', ''))} chars")
    click.echo(f"Final length:   {len(shared.get('final_article', ''))} chars")

    article = shared.get("final_article", "")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(article, encoding="utf-8")
    click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
