import click
from flow import qa_flow


@click.command()
@click.option("--question", default="In one sentence, what's the end of universe?",
              show_default=True, help="Question to answer")
@click.option("--out", default=None, help="File path to save the answer (e.g. output/answer.md)")
def main(question, out):
    shared = {"question": question, "answer": None}
    qa_flow.run(shared)
    click.echo(f"Question: {shared['question']}")
    click.echo(f"Answer:   {shared['answer']}")
    if out:
        from pathlib import Path
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(f"Q: {shared['question']}\nA: {shared['answer']}\n", encoding="utf-8")
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
