#!/usr/bin/env python3
"""
patch_call_llm.py — patch PocketFlow cookbook recipes to use call_llm_shim.

Strategy: wrap the original call_llm() in `if False:` to disable it,
then import the shim. To revert, change `if False:` back to `if True:`.

Usage:
    python patch_call_llm.py            # patch all active recipes
    python patch_call_llm.py --dry-run  # preview without writing
    python patch_call_llm.py --revert   # restore originals
    python patch_call_llm.py --recipe pocketflow-hello-world
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COOKBOOK   = Path(__file__).parent
MARKER_ON  = "# [SPL-SHIM-ON]"
MARKER_OFF = "# [SPL-SHIM-OFF]"


def find_call_llm_file(recipe_dir: Path) -> Path | None:
    for candidate in ["utils.py", "utils/call_llm.py"]:
        p = recipe_dir / candidate
        if p.exists() and "def call_llm" in p.read_text(encoding="utf-8"):
            return p
    return None


def _shim_import(utils_file: Path, has_async: bool) -> str:
    """Build the shim import block with correct sys.path resolution."""
    # utils/call_llm.py → parents[2] is cookbook root
    # utils.py          → parents[1] is cookbook root
    path_expr = (
        "str(Path(__file__).resolve().parents[2] "
        "if Path(__file__).resolve().parent.name == 'utils' "
        "else Path(__file__).resolve().parents[1])"
    )
    import_line = (
        "from call_llm_shim import call_llm, call_llm_async"
        if has_async else
        "from call_llm_shim import call_llm"
    )
    return (
        f"\nimport sys\n"
        f"from pathlib import Path\n"
        f"{MARKER_ON}\n"
        f"# SPL shim: set SPL_ADAPTER (ollama|claude_cli) and SPL_MODEL env vars\n"
        f"# Revert: change 'if False' back to 'if True' in the block below\n"
        f"sys.path.insert(0, {path_expr})\n"
        f"{import_line}\n"
        f"{MARKER_OFF}\n"
    )


def _wrap_in_if_false(src: str) -> str:
    """
    Find every `def call_llm` / `async def call_llm` / `async def call_llm_async`
    block and wrap it in `if False:` by indenting the body.
    Returns modified source.
    """
    lines = src.splitlines(keepends=True)
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\s*)(async\s+)?def\s+(call_llm(?:_async)?)\s*\(', line)
        if m:
            base_indent = m.group(1)
            # Emit the if False: guard
            result.append(f"{base_indent}if False:  # [SPL-SHIM] original — revert: change to 'if True'\n")
            # Indent this line and the whole function body by 4 spaces
            result.append("    " + line)
            i += 1
            # Continue indenting until we leave the function body
            while i < len(lines):
                next_line = lines[i]
                stripped = next_line.lstrip()
                is_empty = not stripped.strip()
                if not is_empty:
                    current_indent = len(next_line) - len(next_line.lstrip())
                    if current_indent <= len(base_indent) and not stripped.startswith("@"):
                        break
                result.append("    " + next_line)
                i += 1
        else:
            result.append(line)
            i += 1
    return "".join(result)


def patch_file(path: Path, dry_run: bool = False) -> bool:
    src = path.read_text(encoding="utf-8")
    if MARKER_ON in src:
        print(f"  SKIP (already patched): {path.relative_to(COOKBOOK)}")
        return False

    has_async = bool(re.search(r'async\s+def\s+call_llm', src))

    # 1. Find last TOP-LEVEL import in the original source and insert shim there.
    #    Must be done first so the shim lands before the if-False block and
    #    _wrap_in_if_false never sees shim lines as part of the function body.
    lines = src.splitlines(keepends=True)
    last_import = 0
    for idx, line in enumerate(lines):
        if re.match(r'(import |from \w)', line):  # top-level only (no indent)
            last_import = idx
    shim = _shim_import(path, has_async)
    lines.insert(last_import + 1, shim)
    with_shim = "".join(lines)

    # 2. Wrap original call_llm definition in if False:
    patched = _wrap_in_if_false(with_shim)

    if dry_run:
        print(f"  DRY-RUN: {path.relative_to(COOKBOOK)}  ({src.count(chr(10))} → {patched.count(chr(10))} lines)")
    else:
        path.write_text(patched, encoding="utf-8")
        print(f"  Patched: {path.relative_to(COOKBOOK)}")
    return True


def revert_file(path: Path, dry_run: bool = False) -> bool:
    src = path.read_text(encoding="utf-8")
    if MARKER_ON not in src:
        print(f"  SKIP (not patched): {path.relative_to(COOKBOOK)}")
        return False

    lines = src.splitlines(keepends=True)
    result = []
    in_shim = False
    in_if_false = False

    for line in lines:
        # Remove shim import block
        if MARKER_ON in line:
            in_shim = True
            continue
        if MARKER_OFF in line:
            in_shim = False
            continue
        if in_shim:
            continue

        # Undo if False: wrapper — restore original indentation
        if re.match(r'\s*if False:.*\[SPL-SHIM\]', line):
            in_if_false = True
            continue
        if in_if_false:
            # Strip the 4-space indent we added
            if line.startswith("    "):
                stripped = line[4:]
            else:
                stripped = line
            # Detect end of if-False block
            if stripped.strip() and not stripped.startswith(" ") and not re.match(r'\s+(async\s+)?def |    ', line):
                in_if_false = False
                result.append(stripped)
            else:
                result.append(stripped)
            continue

        result.append(line)

    # Remove the sys/Path imports we added (simple heuristic: only if they weren't there originally)
    reverted = "".join(result)

    if dry_run:
        print(f"  DRY-RUN revert: {path.relative_to(COOKBOOK)}")
    else:
        path.write_text(reverted, encoding="utf-8")
        print(f"  Reverted: {path.relative_to(COOKBOOK)}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run",  action="store_true")
    parser.add_argument("--revert",   action="store_true")
    parser.add_argument("--recipe",   default=None)
    args = parser.parse_args()

    dirs = [COOKBOOK / args.recipe] if args.recipe else sorted(COOKBOOK.glob("pocketflow-*"))

    patched = skipped = 0
    for d in dirs:
        if not d.is_dir():
            continue
        f = find_call_llm_file(d)
        if f is None:
            print(f"  SKIP (no call_llm): {d.name}")
            skipped += 1
            continue
        print(d.name)
        fn = revert_file if args.revert else patch_file
        if fn(f, dry_run=args.dry_run):
            patched += 1
        else:
            skipped += 1

    action = "reverted" if args.revert else "patched"
    print(f"\n{action}: {patched}  skipped: {skipped}")


if __name__ == "__main__":
    main()
