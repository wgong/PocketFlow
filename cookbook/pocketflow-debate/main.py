import click
from flow import create_debate_flow


@click.command()
@click.option("--claim", default="Remote work is more productive than office work",
              show_default=True, help="Claim to debate")
@click.option("--out", default=None, help="File path to save the debate summary (e.g. output/debate.md)")
def main(claim, out):
    click.echo(f'🤔 Debating claim: "{claim}"')
    shared = {"claim": claim}
    create_debate_flow().run(shared)

    summary = (
        f"=== Debate Summary ===\n"
        f"Claim:   {shared['claim']}\n"
        f"Winner:  {shared.get('winner', 'N/A')}\n"
        f"Scores:  FOR {shared.get('score_for','N/A')}/10 | AGAINST {shared.get('score_against','N/A')}/10\n"
        f"Verdict: {shared.get('verdict', 'N/A')}\n"
    )
    click.echo(f"\n{summary}")
    if out:
        from pathlib import Path
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(summary, encoding="utf-8")
        click.echo(f"✅ Saved to: {out}")


if __name__ == "__main__":
    main()
