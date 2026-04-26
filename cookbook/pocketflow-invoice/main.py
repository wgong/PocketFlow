import sys
import click
from pathlib import Path
from flow import create_invoice_flow


@click.command()
@click.option("--input", "input_path", default="data/invoice.pdf", show_default=True,
              help="Path to the invoice PDF file")
@click.option("--out", default="output/invoice_result.md", show_default=True,
              help="File path to save the extraction result")
def main(input_path, out):
    click.echo("🧾 PocketFlow Invoice Processor\n")
    if not Path(input_path).exists():
        click.echo(f"Error: '{input_path}' not found.")
        click.echo("Run 'python create_invoice.py' first to generate a sample invoice.")
        sys.exit(1)

    click.echo(f"📄 Processing: {input_path}\n")
    shared = {"pdf_path": input_path}
    create_invoice_flow().run(shared)

    click.echo("\n=== Summary ===")
    result_lines = []
    if "extracted" in shared:
        d = shared["extracted"]
        click.echo(f"  Invoice #: {d.get('invoice_number')}")
        click.echo(f"  Total:     ${d.get('total', 0):.2f}")
        result_lines.append(f"Invoice #: {d.get('invoice_number')}")
        result_lines.append(f"Total: ${d.get('total', 0):.2f}")
    errors = shared.get("validation_errors", [])
    status = f"FAILED ({len(errors)} error(s))" if errors else "PASSED"
    click.echo(f"  Status:    {status}")
    result_lines.append(f"Status: {status}")

    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text("\n".join(result_lines), encoding="utf-8")
    click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
