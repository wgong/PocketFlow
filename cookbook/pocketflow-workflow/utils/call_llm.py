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

if False:  # [SPL-SHIM] original — revert: change to 'if True'
    def call_llm(prompt):    
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return r.choices[0].message.content
    
# Example usage
if __name__ == "__main__":
    print(call_llm("Tell me a short joke")) 