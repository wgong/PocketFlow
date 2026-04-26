import click
from flow import create_database_flow


@click.command()
@click.option("--title", default="Example Task", show_default=True,
              help="Title of the task to create")
@click.option("--description", default="This is an example task created using PocketFlow",
              show_default=True, help="Task description")
def main(title, description):
    shared = {"task_title": title, "task_description": description}
    create_database_flow().run(shared)
    click.echo(f"Database Status: {shared.get('db_status')}")
    click.echo(f"Task Status:     {shared.get('task_status')}")
    click.echo("\nAll Tasks:")
    for task in shared.get("tasks", []):
        click.echo(f"  [{task[0]}] {task[1]} | {task[3]} | {task[4]}")
        click.echo(f"       {task[2]}")


if __name__ == "__main__":
    main()
