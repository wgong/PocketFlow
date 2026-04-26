import os
import click
from pathlib import Path
from flow import create_flow


@click.command()
@click.option("--input", "input_file", default="data/sales.csv", show_default=True,
              help="CSV file to process in chunks")
def main(input_file):
    os.makedirs("data", exist_ok=True)
    if not Path(input_file).exists():
        click.echo(f"Creating sample {input_file}...")
        import pandas as pd
        import numpy as np
        np.random.seed(42)
        n = 10000
        df = pd.DataFrame({
            "date":    pd.date_range("2024-01-01", periods=n),
            "amount":  np.random.normal(100, 30, n).round(2),
            "product": np.random.choice(["A", "B", "C"], n),
        })
        df.to_csv(input_file, index=False)

    click.echo(f"Processing {input_file} in chunks...")
    create_flow().run({"input_file": input_file})


if __name__ == "__main__":
    main()
