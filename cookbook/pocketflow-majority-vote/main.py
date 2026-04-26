import collections
import click
import yaml
from pocketflow import BatchNode, Flow
from utils import call_llm

DEFAULT_PROBLEM = (
    'You work at a shoe factory. In front of you, there are three pairs of shoes '
    '(six individual shoes) with sizes: two size 4s, two size 5s, and two size 6s. '
    'An "acceptable pair" means two shoes that differ by at most one size. '
    'If you randomly pick three pairs without replacement, what is the probability '
    'that all three are acceptable pairs?'
)


class MajorityVoteNode(BatchNode):
    def prep(self, shared):
        q = shared.get("question", "(No question provided)")
        return [q for _ in range(shared.get("num_tries", 3))]

    def exec(self, question):
        prompt = (
            f"You are a helpful assistant. Answer the question below.\n"
            f"Question: {question}\n\n"
            f"Return strictly using:\n```yaml\nthinking: |\n    (your reasoning)\nanswer: 0.123\n```"
        )
        raw = call_llm(prompt)
        yaml_part = raw.split("```yaml")[1].split("```")[0].strip()
        parsed = yaml.safe_load(yaml_part)
        if not isinstance(parsed, dict) or "answer" not in parsed:
            raise RuntimeError(f"Missing 'answer' in YAML: {parsed}")
        return str(parsed["answer"])

    def exec_fallback(self, prep_res, exc):
        return None

    def post(self, shared, prep_res, exec_res_list):
        valid = [r for r in exec_res_list if r is not None]
        best, freq = collections.Counter(valid).most_common(1)[0]
        shared["majority_answer"] = best
        click.echo("========================")
        click.echo(f"All answers: {valid}")
        click.echo(f"Majority:    {best}  (freq={freq})")
        click.echo("========================")
        return "end"


@click.command()
@click.option("--question", default=DEFAULT_PROBLEM, show_default=False,
              help="Reasoning problem to solve via majority vote (default: shoe factory probability)")
@click.option("--tries", default=5, show_default=True,
              help="Number of independent LLM attempts for majority vote")
def main(question, tries):
    shared = {"question": question, "num_tries": tries}
    Flow(start=MajorityVoteNode()).run(shared)
    click.echo("\n=== Final Answer ===")
    click.echo(shared.get("majority_answer", "N/A"))
    click.echo("====================")


if __name__ == "__main__":
    main()
