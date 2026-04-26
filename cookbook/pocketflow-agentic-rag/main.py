import click
from flow import create_agentic_rag_flow


@click.command()
@click.option("--question", default="How do nodes work in PocketFlow?",
              show_default=True, help="Question to answer using agentic RAG")
@click.option("--out", default=None, help="File path to save the answer (e.g. output/answer.md)")
def main(question, out):
    shared = {"question": question}
    click.echo(f"🤔 Question: {question}\n")
    create_agentic_rag_flow().run(shared)
    answer = shared.get("answer", "No answer generated.")
    click.echo("\n🎯 Final Answer:")
    click.echo(answer)
    if out:
        from pathlib import Path
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(f"Q: {question}\nA: {answer}\n", encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
