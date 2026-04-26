import sys
import click
from pathlib import Path
from flow import create_text_to_sql_flow
from populate_db import populate_database, DB_FILE


@click.command()
@click.option("--query", default="total products per category",
              show_default=True, help="Natural-language SQL query")
@click.option("--db", default=DB_FILE, show_default=True, help="SQLite database path")
@click.option("--max-retries", default=3, show_default=True,
              help="Max debug retries on SQL error")
def main(query, db, max_retries):
    if not Path(db).exists() or Path(db).stat().st_size == 0:
        click.echo(f"Database '{db}' missing or empty — populating...")
        populate_database(db)

    shared = {
        "db_path": db,
        "natural_query": query,
        "max_debug_attempts": max_retries,
        "debug_attempts": 0,
        "final_result": None,
        "final_error": None,
    }
    click.echo(f"\n=== Text-to-SQL ===")
    click.echo(f"Query:    {query}")
    click.echo(f"Database: {db}")
    click.echo("=" * 36)
    create_text_to_sql_flow().run(shared)

    if shared.get("final_error"):
        click.echo(f"\n❌ Error: {shared['final_error']}")
        sys.exit(1)
    else:
        click.echo("\n✅ Completed successfully.")


if __name__ == "__main__":
    main()
