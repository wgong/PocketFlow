import click
from flow import create_agent_flow


@click.command()
@click.option("--question", default="Who won the Nobel Prize in Physics 2024?",
              show_default=True, help="Question for the A2A agent to answer")
@click.option("--out", default=None, help="File path to save the answer (e.g. output/answer.md)")
def main(question, out):
    shared = {"question": question}
    click.echo(f"🤔 Processing question: {question}")
    create_agent_flow().run(shared)
    answer = shared.get("answer", "No answer found")
    click.echo("\n🎯 Final Answer:")
    click.echo(answer)
    if out:
        from pathlib import Path
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(f"Q: {question}\nA: {answer}\n", encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
