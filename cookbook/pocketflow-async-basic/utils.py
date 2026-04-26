import asyncio
import aiohttp
from openai import AsyncOpenAI

import sys
from pathlib import Path
# [SPL-SHIM-ON]
# SPL shim: set SPL_ADAPTER (ollama|claude_cli) and SPL_MODEL env vars
# Revert: change 'if False' back to 'if True' in the block below
sys.path.insert(0, str(Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name == 'utils' else Path(__file__).resolve().parents[1]))
from call_llm_shim import call_llm, call_llm_async
# [SPL-SHIM-OFF]

async def fetch_recipes(ingredient):
    """Fetch recipes from an API asynchronously."""
    print(f"Fetching recipes for {ingredient}...")
    
    # Simulate API call with delay
    await asyncio.sleep(1)
    
    # Mock recipes (in real app, would fetch from API)
    recipes = [
        f"{ingredient} Stir Fry",
        f"Grilled {ingredient} with Herbs",
        f"Baked {ingredient} with Vegetables"
    ]
    
    print(f"Found {len(recipes)} recipes.")
    
    return recipes

if False:  # [SPL-SHIM] original — revert: change to 'if True'
    async def call_llm_async(prompt):
        """Make async LLM call."""
        print("\nSuggesting best recipe...")
        
        # Simulate LLM call with delay
        await asyncio.sleep(1)
        
        # Mock LLM response (in real app, would call OpenAI)
        recipes = prompt.split(": ")[1].split(", ")
        suggestion = recipes[1]  # Always suggest second recipe
        
        print(f"How about: {suggestion}")
        return suggestion
    
async def get_user_input(prompt):
    """Get user input asynchronously."""
    # Create event loop to handle async input
    loop = asyncio.get_event_loop()
    
    # Get input in a non-blocking way
    answer = await loop.run_in_executor(None, input, prompt)

    return answer.lower() 