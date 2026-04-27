import sys
import yaml
import click
from pathlib import Path
from pocketflow import Node, Flow
from utils import call_llm

DEFAULT_SKILLS = [
    "Team leadership & management",
    "CRM software",
    "Project management",
    "Public speaking",
    "Microsoft Office",
    "Python",
    "Data Analysis",
]


class ResumeParserNode(Node):
    def prep(self, shared):
        return {"resume_text": shared["resume_text"], "target_skills": shared.get("target_skills", [])}

    def exec(self, prep_res):
        skill_list = "\n".join(f"{i}: {s}" for i, s in enumerate(prep_res["target_skills"]))
        prompt = f"""Analyze the resume below. Output ONLY YAML.

**Resume:**
```
{prep_res['resume_text']}
```

**Target Skills (use these indexes):**
```
{skill_list}
```

```yaml
# comment explaining source
name: ...
# comment
email: ...
experience:
  - title: ...
    company: ...
skill_indexes:
  - 0
```"""
        response = call_llm(prompt)
        yaml_str = response.split("```yaml")[1].split("```")[0].strip()
        result = yaml.safe_load(yaml_str)
        assert result and "name" in result and "email" in result
        return result

    def post(self, shared, prep_res, exec_res):
        shared["structured_data"] = exec_res
        click.echo("\n=== STRUCTURED RESUME DATA ===\n")
        click.echo(yaml.dump(exec_res, sort_keys=False, allow_unicode=True))
        click.echo("✅ Extracted resume information.")


@click.command()
@click.option("--input", "input_path", default="data/data.txt", show_default=True,
              help="Path to the resume text file")
@click.option("--out", default="output/resume_parsed.yaml", show_default=True,
              help="File path to save the parsed YAML result")
def main(input_path, out):
    click.echo("=== Resume Parser — Structured Output ===\n")
    p = Path(input_path)
    if not p.exists():
        click.echo(f"Error: '{input_path}' not found.")
        sys.exit(1)

    shared = {
        "resume_text": p.read_text(encoding="utf-8"),
        "target_skills": DEFAULT_SKILLS,
    }
    Flow(start=ResumeParserNode(max_retries=3, wait=10)).run(shared)

    if "structured_data" in shared:
        raw_indexes = shared["structured_data"].get("skill_indexes") or []
        # gemma3 may return [{0: "name"}, ...] instead of [0, 1, ...]
        indexes = []
        for item in raw_indexes:
            if isinstance(item, int):
                indexes.append(item)
            elif isinstance(item, dict):
                indexes.extend(int(k) for k in item.keys())
        if indexes:
            click.echo("\n--- Found Target Skills ---")
            for idx in indexes:
                if 0 <= idx < len(DEFAULT_SKILLS):
                    click.echo(f"  - {DEFAULT_SKILLS[idx]} (index {idx})")

        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(
            yaml.dump(shared["structured_data"], sort_keys=False, allow_unicode=True),
            encoding="utf-8"
        )
        click.echo(f"\n✅ Saved to: {out}")


if __name__ == "__main__":
    main()
