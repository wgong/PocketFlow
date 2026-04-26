import asyncio
import time
import os
import click
from flow import create_flows


@click.command()
@click.option("--input-dir", default="images", show_default=True,
              help="Directory containing images to process (.jpg/.jpeg/.png)")
def main(input_dir):
    """Compare sequential vs parallel image processing using PocketFlow."""
    if not os.path.exists(input_dir):
        click.echo(f"Error: Directory '{input_dir}' not found.")
        raise SystemExit(1)

    image_paths = [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    if not image_paths:
        click.echo(f"Error: No images found in '{input_dir}'.")
        raise SystemExit(1)

    click.echo(f"Found {len(image_paths)} images:")
    for path in image_paths:
        click.echo(f"  - {path}")

    shared = {"images": image_paths}
    batch_flow, parallel_batch_flow = create_flows()

    click.echo("\nRunning sequential batch flow...")
    start = time.time()
    asyncio.run(batch_flow.run_async(shared))
    batch_time = time.time() - start

    click.echo("\nRunning parallel batch flow...")
    start = time.time()
    asyncio.run(parallel_batch_flow.run_async(shared))
    parallel_time = time.time() - start

    click.echo("\nTiming Results:")
    click.echo(f"  Sequential: {batch_time:.2f}s")
    click.echo(f"  Parallel:   {parallel_time:.2f}s")
    click.echo(f"  Speedup:    {batch_time / parallel_time:.2f}x")
    click.echo("\nProcessing complete! Check the output/ directory for results.")


if __name__ == "__main__":
    main()
