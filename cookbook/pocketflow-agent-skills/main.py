from pathlib import Path

import click

from flow import create_flow


@click.command()
@click.option("--task", default="Summarize this text for a VP audience",
              show_default=True, help="What to do with the text")
@click.option("--text", default=None,
              help="Literal text string or path to a text/markdown file")
@click.option("--out", default=None,
              help="File path to write the output (default: print to stdout)")
def main(task, text, out):
    # Resolve --text: file path or literal string
    input_text = ""
    if text:
        p = Path(text)
        if p.exists():
            input_text = p.read_text(encoding="utf-8")
        else:
            input_text = text

    full_task = f"{task}\n\n{input_text}".strip() if input_text else task

    shared = {
        "task": full_task,
        "skills_dir": "skills",
    }

    flow = create_flow()

    click.echo(f"🧩 Task   : {task}")
    if text:
        click.echo(f"📄 Input  : {text}")
    flow.run(shared)

    skill = shared.get("selected_skill", "(none)")
    result = shared.get("result", "(no result)")

    click.echo(f"\n=== Skill Used ===\n{skill}")
    click.echo(f"\n=== Output ===\n{result}")

    if out:
        out_path = Path(out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(result, encoding="utf-8")
        click.echo(f"\n✅ Written to: {out}")


if __name__ == "__main__":
    main()
