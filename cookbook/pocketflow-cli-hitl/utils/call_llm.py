from anthropic import Anthropic
import os

import sys
from pathlib import Path
# [SPL-SHIM-ON]
# SPL shim: set SPL_ADAPTER (ollama|claude_cli) and SPL_MODEL env vars
# Revert: change 'if False' back to 'if True' in the block below
sys.path.insert(0, str(Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name == 'utils' else Path(__file__).resolve().parents[1]))
from call_llm_shim import call_llm
# [SPL-SHIM-OFF]

if False:  # [SPL-SHIM] original — revert: change to 'if True'
    def call_llm(prompt: str) -> str:
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", "your-anthropic-api-key")) # Default if key not found
        response = client.messages.create(
            model="claude-3-haiku-20240307", # Using a smaller model for jokes
            max_tokens=150, # Jokes don't need to be very long
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    
if __name__ == "__main__":
    print("Testing Anthropic LLM call for jokes:")
    joke_prompt = "Tell me a one-liner joke about a cat."
    print(f"Prompt: {joke_prompt}")
    try:
        response = call_llm(joke_prompt)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling LLM: {e}")
        print("Please ensure your ANTHROPIC_API_KEY environment variable is set correctly.")