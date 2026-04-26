import click
from flow import create_coding_agent_flow
from setup_test_project import setup_test_project, WORKDIR

DEFAULT_TASK = (
    "Implement the skeleton functions to make all tests pass. "
    "Run: python -m pytest test_tokenizer.py test_parser.py test_executor.py -v"
)


@click.command()
@click.option("--task", default=DEFAULT_TASK, show_default=False,
              help="Coding task for the agent (default: implement skeleton functions)")
def main(task):
    setup_test_project()
    shared = {"task": task, "workdir": WORKDIR}
    click.echo("🤖 Coding Agent starting...")
    click.echo(f"📋 Task: {task}")
    click.echo(f"📁 Working in: {WORKDIR}\n")
    create_coding_agent_flow().run(shared)
    click.echo(f"\n🎯 Result: {shared.get('result', '')}")


if __name__ == "__main__":
    main()
