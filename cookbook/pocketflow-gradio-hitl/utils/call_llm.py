import os

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

import sys
from pathlib import Path
# [SPL-SHIM-ON]
# SPL shim: set SPL_ADAPTER (ollama|claude_cli) and SPL_MODEL env vars
# Revert: change 'if False' back to 'if True' in the block below
sys.path.insert(0, str(Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name == 'utils' else Path(__file__).resolve().parents[1]))
from call_llm_shim import call_llm
# [SPL-SHIM-OFF]

api_key = os.getenv("OPENAI_API_KEY")
base_url = "https://api.openai.com/v1"
model = "gpt-4o"


if False:  # [SPL-SHIM] original — revert: change to 'if True'
    def call_llm(message: str):
        print(f"Calling LLM with message: \n{message}")
        client = OpenAI(api_key=api_key, base_url=base_url)
        response: ChatCompletion = client.chat.completions.create(
            model=model, messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    
    
if __name__ == "__main__":
    print(call_llm("Hello, how are you?"))
