import click
from flow import flow


@click.command()
def main():
    """Text Converter — demonstrates a basic PocketFlow pipeline."""
    click.echo("\nWelcome to Text Converter!")
    click.echo("=========================")
    flow.run({})
    click.echo("\nThank you for using Text Converter!")


if __name__ == "__main__":
    main()
