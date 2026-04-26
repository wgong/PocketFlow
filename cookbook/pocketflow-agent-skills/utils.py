from pathlib import Path
import os
from openai import OpenAI

import sys
from pathlib import Path
# [SPL-SHIM-ON]
# SPL shim: set SPL_ADAPTER (ollama|claude_cli) and SPL_MODEL env vars
# Revert: change 'if False' back to 'if True' in the block below
sys.path.insert(0, str(Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name == 'utils' else Path(__file__).resolve().parents[1]))
from call_llm_shim import call_llm
# [SPL-SHIM-OFF]


def load_skills(skills_dir: str) -> dict[str, str]:
    skills = {}
    for md_file in sorted(Path(skills_dir).glob("*.md")):
        skills[md_file.stem] = md_file.read_text(encoding="utf-8")

    if not skills:
        raise ValueError(f"No skill files found in {skills_dir}")
    return skills


if False:  # [SPL-SHIM] original — revert: change to 'if True'
    def call_llm(prompt: str) -> str:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
