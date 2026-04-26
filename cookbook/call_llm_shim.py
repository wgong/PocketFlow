"""
call_llm_shim.py — shared LLM adapter shim for SPL benchmark.

Drop-in replacement for each recipe's call_llm() that routes through
the adapter and model specified by environment variables:

    SPL_ADAPTER  — "ollama" (default) | "claude_cli"
    SPL_MODEL    — model name (default depends on adapter)

This preserves the original call_llm() signatures used by each recipe:
    call_llm(prompt)         — standard single-turn prompt
    call_llm(messages)       — chat-style list of {"role", "content"} dicts
    async call_llm(prompt)   — async variant (async-basic, parallel-batch)

To switch back to the original OpenAI/Anthropic implementation:
    uncomment the original code in the recipe's utils.py or utils/call_llm.py
    and comment out the line: from call_llm_shim import call_llm
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import urllib.request
from pathlib import Path

# ── Config from environment ───────────────────────────────────────────────────

SPL_ADAPTER = os.environ.get("SPL_ADAPTER", "ollama")
SPL_MODEL   = os.environ.get("SPL_MODEL", "")

_OLLAMA_DEFAULTS = "gemma3"
_CLAUDE_DEFAULTS = "claude-sonnet-4-6"


def _effective_model() -> str:
    if SPL_MODEL:
        return SPL_MODEL
    if SPL_ADAPTER == "claude_cli":
        return _CLAUDE_DEFAULTS
    return _OLLAMA_DEFAULTS


# ── Ollama backend ────────────────────────────────────────────────────────────

def _ollama(prompt: str) -> str:
    model = _effective_model()
    payload = json.dumps({
        "model":  model,
        "prompt": prompt,
        "stream": False,
    }).encode()
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())["response"].strip()


# ── claude_cli backend ────────────────────────────────────────────────────────

def _claude_cli(prompt: str) -> str:
    """Call Claude via the claude CLI subprocess (no API key needed — uses claude auth)."""
    import subprocess
    model = _effective_model()
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model, "--output-format", "text"],
            capture_output=True, text=True, timeout=120,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError("Claude CLI timeout after 120s")

    if result.returncode != 0:
        out = result.stdout.strip()
        err = result.stderr.strip()
        combined = f"{out}\n{err}".strip()
        
        if "hit your limit" in combined.lower():
            raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
        
        if "login" in combined.lower() or "auth" in combined.lower():
            raise RuntimeError("Claude CLI Session Inactive: Please run 'claude login'")
            
        raise RuntimeError(f"Claude CLI error (code {result.returncode}): {combined if combined else 'Unknown error'}")
    
    return result.stdout.strip()


# ── Public API ────────────────────────────────────────────────────────────────

def call_llm(prompt_or_messages) -> str:
    """
    Unified call_llm for both prompt (str) and messages (list) signatures.

    If a list of messages is passed (chat-style), they are flattened into a
    single prompt string:
        system content → "System: ..."
        user content   → "User: ..."
        assistant      → "Assistant: ..."
    """
    # Normalise messages → prompt string
    if isinstance(prompt_or_messages, list):
        parts = []
        for m in prompt_or_messages:
            role    = m.get("role", "user").capitalize()
            content = m.get("content", "")
            parts.append(f"{role}: {content}")
        prompt = "\n".join(parts)
    else:
        prompt = str(prompt_or_messages)

    if SPL_ADAPTER == "claude_cli":
        return _claude_cli(prompt)
    return _ollama(prompt)


async def call_llm_async(prompt_or_messages) -> str:
    """Async wrapper — runs call_llm in a thread so event loops stay happy."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, call_llm, prompt_or_messages)


# ── Smoke test ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    adapter = SPL_ADAPTER
    model   = _effective_model()
    print(f"SPL_ADAPTER={adapter}  SPL_MODEL={model}")
    response = call_llm("In one sentence, what is the meaning of life?")
    print(f"Response: {response}")
