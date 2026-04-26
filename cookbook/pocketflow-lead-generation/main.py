import click
from pathlib import Path
from flow import create_lead_generation_flow


@click.command()
@click.option("--out", default="output/emails.md", show_default=True,
              help="File path to save the generated emails")
def main(out):
    """Lead-generation pipeline: scrape -> enrich -> score -> personalize emails."""
    shared = {}
    click.echo("🚀 Starting Lead-Generation Pipeline")
    click.echo("=" * 50)
    click.echo("\n📋 Step 1 — Scraping leads")
    click.echo("🔍 Step 2 — Enriching leads")
    click.echo("🤔 Step 3 — Scoring leads with LLM")
    click.echo("✍️  Step 4 — Personalizing emails\n")
    create_lead_generation_flow().run(shared)

    lines = []
    click.echo("\n" + "=" * 50)
    click.echo("📧 Generated Emails")
    click.echo("=" * 50)
    for item in shared.get("emails", []):
        lead = item["lead"]
        header = f"--- {lead['name']} ({lead['title']} @ {lead['company']}) | Score: {lead['score']}/10 ---"
        click.echo(f"\n{header}")
        click.echo(item["email"])
        lines.append(f"## {header}\n\n{item['email']}\n")

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text("\n".join(lines), encoding="utf-8")
    click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
