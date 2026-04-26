import os
import time
import click
from pathlib import Path
from pocketflow import BatchNode, Flow
from utils import call_llm

DEFAULT_LANGUAGES = ["Chinese", "Spanish", "Japanese", "German", "Russian", "Portuguese", "French", "Korean"]


class TranslateTextNode(BatchNode):
    def prep(self, shared):
        text = shared.get("text", "(No text provided)")
        languages = shared.get("languages", DEFAULT_LANGUAGES)
        return [(text, lang) for lang in languages]

    def exec(self, data_tuple):
        text, language = data_tuple
        prompt = (
            f"Please translate the following markdown file into {language}.\n"
            f"Keep the original markdown format, links and code blocks.\n"
            f"Return the translated text only, no other comments.\n\n"
            f"Original:\n{text}\n\nTranslated:"
        )
        result = call_llm(prompt)
        click.echo(f"  Translated: {language}")
        return {"language": language, "translation": result}

    def post(self, shared, prep_res, exec_res_list):
        output_dir = shared.get("output_dir", "output/translations")
        os.makedirs(output_dir, exist_ok=True)
        for result in exec_res_list:
            lang = result["language"]
            fname = os.path.join(output_dir, f"README_{lang.upper()}.md")
            with open(fname, "w", encoding="utf-8") as f:
                f.write(result["translation"])
            click.echo(f"  Saved: {fname}")


@click.command()
@click.option("--input", "input_path", default=None,
              help="Markdown file to translate (default: ../../README.md)")
@click.option("--languages", default=",".join(DEFAULT_LANGUAGES), show_default=True,
              help="Comma-separated list of target languages")
@click.option("--out-dir", default="output/translations", show_default=True,
              help="Directory to save translated files")
def main(input_path, languages, out_dir):
    src = Path(input_path) if input_path else Path("../../README.md")
    if not src.exists():
        click.echo(f"Error: '{src}' not found.")
        raise SystemExit(1)

    text = src.read_text(encoding="utf-8")
    lang_list = [l.strip() for l in languages.split(",") if l.strip()]

    shared = {"text": text, "languages": lang_list, "output_dir": out_dir}
    click.echo(f"Starting sequential translation into {len(lang_list)} languages...")
    start = time.perf_counter()
    Flow(start=TranslateTextNode(max_retries=3)).run(shared)
    elapsed = time.perf_counter() - start

    click.echo(f"\nTotal time: {elapsed:.2f}s")
    click.echo(f"Translations saved to: {out_dir}")


if __name__ == "__main__":
    main()
