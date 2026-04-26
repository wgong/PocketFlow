import asyncio
import time
import os
import click
from pathlib import Path
from pocketflow import AsyncFlow, AsyncParallelBatchNode
from utils import call_llm

DEFAULT_LANGUAGES = "Chinese,Spanish,Japanese,German,Russian,Portuguese,French,Korean"


class TranslateTextNodeParallel(AsyncParallelBatchNode):
    """Translates text into multiple languages in parallel and saves files."""

    async def prep_async(self, shared):
        text = shared.get("text", "(No text provided)")
        languages = shared.get("languages", [])
        return [(text, lang) for lang in languages]

    async def exec_async(self, data_tuple):
        text, language = data_tuple
        prompt = f"""Please translate the following markdown file into {language}.
But keep the original markdown format, links and code blocks.
Directly return the translated text, without any other text or comments.

Original:
{text}

Translated:"""
        result = await call_llm(prompt)
        click.echo(f"Translated {language} text")
        return {"language": language, "translation": result}

    async def post_async(self, shared, prep_res, exec_res_list):
        output_dir = shared.get("output_dir", "output/translations")
        os.makedirs(output_dir, exist_ok=True)
        for result in exec_res_list:
            if isinstance(result, dict):
                language = result.get("language", "unknown")
                translation = result.get("translation", "")
                filename = os.path.join(output_dir, f"README_{language.upper()}.md")
                try:
                    import aiofiles
                    async with aiofiles.open(filename, "w", encoding="utf-8") as f:
                        await f.write(translation)
                except ImportError:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(translation)
                click.echo(f"Saved: {filename}")
        return "default"


def create_parallel_translation_flow():
    return AsyncFlow(start=TranslateTextNodeParallel(max_retries=3))


@click.command()
@click.option("--input", "input_path", default=None,
              help="Path to a markdown file to translate (default: ../../README.md)")
@click.option("--languages", default=DEFAULT_LANGUAGES, show_default=True,
              help="Comma-separated list of target languages")
@click.option("--out-dir", default="output/translations", show_default=True,
              help="Directory to save translated files")
def main(input_path, languages, out_dir):
    """Translate a markdown file into multiple languages in parallel."""
    source_path = input_path or "../../README.md"
    try:
        text = Path(source_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        click.echo(f"Error: Could not find source file at {source_path}")
        raise SystemExit(1)

    lang_list = [l.strip() for l in languages.split(",")]
    shared = {"text": text, "languages": lang_list, "output_dir": out_dir}

    click.echo(f"Starting parallel translation into {len(lang_list)} languages...")
    start_time = time.perf_counter()

    asyncio.run(create_parallel_translation_flow().run_async(shared))

    duration = time.perf_counter() - start_time
    click.echo(f"\nTotal parallel translation time: {duration:.4f} seconds")
    click.echo(f"Translations saved to: {out_dir}")


if __name__ == "__main__":
    main()
