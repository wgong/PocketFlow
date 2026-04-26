import click
from flow import create_tao_flow


@click.command()
@click.option("--query", default="I need to understand the latest developments in artificial intelligence",
              show_default=True, help="Research query for the TAO reasoning agent")
@click.option("--out", default=None, help="File path to save the answer (e.g. output/answer.md)")
def main(query, out):
    shared = {
        "query": query,
        "thoughts": [],
        "observations": [],
        "current_thought_number": 0,
    }
    create_tao_flow().run(shared)

    if "final_answer" in shared:
        click.echo("\nFinal Answer:")
        click.echo(shared["final_answer"])
        if out:
            from pathlib import Path
            Path(out).parent.mkdir(parents=True, exist_ok=True)
            Path(out).write_text(f"Query: {query}\n\n{shared['final_answer']}\n", encoding="utf-8")
            click.echo(f"\n✅ Saved to: {out}")
    else:
        click.echo("\nFlow did not produce a final answer.")


if __name__ == "__main__":
    main()
