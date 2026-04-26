import os
import click
from flow import create_flow


def create_sample_data():
    data = {
        "school/class_a/student1.txt": [7.5, 8.0, 9.0],
        "school/class_a/student2.txt": [8.5, 7.0, 9.5],
        "school/class_b/student3.txt": [6.5, 8.5, 7.0],
        "school/class_b/student4.txt": [9.0, 9.5, 8.0],
    }
    for path, grades in data.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.writelines(f"{g}\n" for g in grades)


@click.command()
def main():
    """Nested batch processing: iterate over classes, then students within each class."""
    create_sample_data()
    click.echo("Processing school grades...\n")
    create_flow().run({})


if __name__ == "__main__":
    main()
