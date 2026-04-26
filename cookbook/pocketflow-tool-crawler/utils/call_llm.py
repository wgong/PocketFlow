from openai import OpenAI
import os

import sys
from pathlib import Path
# [SPL-SHIM-ON]
# SPL shim: set SPL_ADAPTER (ollama|claude_cli) and SPL_MODEL env vars
# Revert: change 'if False' back to 'if True' in the block below
sys.path.insert(0, str(Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name == 'utils' else Path(__file__).resolve().parents[1]))
from call_llm_shim import call_llm
# [SPL-SHIM-OFF]

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if False:  # [SPL-SHIM] original — revert: change to 'if True'
    def call_llm(prompt: str) -> str:
        """Call OpenAI API to analyze text
        
        Args:
            prompt (str): Input prompt for the model
            
        Returns:
            str: Model response
        """
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error calling LLM API: {str(e)}")
            return ""
    
if __name__ == "__main__":
    # Test LLM call
    response = call_llm("What is web crawling?")
    print("Response:", response)
