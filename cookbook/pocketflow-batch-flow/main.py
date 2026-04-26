import click
from flow import create_flow


@click.command()
def main():
    """Batch image processing with filters (reads from images/, writes to output/)."""
    click.echo("Processing images with filters...")
    create_flow().run({})
    click.echo("\nAll images processed successfully!")
    click.echo("Check the 'output' directory for results.")


if __name__ == "__main__":
    main()
