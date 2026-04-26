import click
from flow import create_heartbeat_flow


@click.command()
@click.option("--cycles", default=4, show_default=True,
              help="Number of polling cycles to run")
def main(cycles):
    shared = {"max_cycles": cycles}
    click.echo("🚀 Starting Heartbeat Email Monitor")
    click.echo(f"   Polling every 2 seconds for {cycles} cycles...\n")
    create_heartbeat_flow().run(shared)
    click.echo("\n✅ Monitor stopped.")
    click.echo(f"📊 Total emails processed: {len(shared.get('processed', []))}")


if __name__ == "__main__":
    main()
