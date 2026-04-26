#!/usr/bin/env python3
"""run_all.py — PocketFlow Cookbook batch runner for SPL benchmark.

Each recipe's main.py is run as a subprocess from its own directory.
LLM backend is controlled via SPL_ADAPTER / SPL_MODEL env vars (see call_llm_shim.py).

Usage
-----
  cd ~/projects/wgong/PocketFlow/cookbook

  # List / inspect
  python run_all.py list
  python run_all.py list --all
  python run_all.py catalog

  # Check prerequisites (Ollama running, models pulled)
  python run_all.py check

  # Run all active recipes
  SPL_ADAPTER=ollama  SPL_MODEL=llama3.2          python run_all.py
  SPL_ADAPTER=claude_cli SPL_MODEL=claude-sonnet-4-6 python run_all.py

  # Run by ID or range
  python run_all.py --ids 6
  python run_all.py --ids 1-10
  python run_all.py --ids 2,5,8

  # Run by category
  python run_all.py --category basics

  # Parallel workers
  python run_all.py --workers 4

  # Save to log
  python run_all.py 2>&1 | tee logs/run_$(date +%Y%m%d_%H%M%S).md
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import click

COOKBOOK_DIR = Path(__file__).resolve().parent

# ── Catalog ───────────────────────────────────────────────────────────────────

def load_catalog() -> list[dict]:
    path = COOKBOOK_DIR / "cookbook_catalog.json"
    with open(path) as f:
        data = json.load(f)
    return data["recipes"]


def apply_filters(
    recipes: list[dict],
    category: str,
    ids: set[str],
    include_inactive: bool,
) -> list[dict]:
    out = []
    for r in recipes:
        if ids and r["id"] not in ids:
            continue
        if not include_inactive and not r.get("is_active"):
            continue
        if category and r.get("category") != category:
            continue
        out.append(r)
    return out


def parse_id_filter(ids: str) -> set[str]:
    result: set[str] = set()
    for part in ids.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            lo, hi = part.split("-", 1)
            for n in range(int(lo), int(hi) + 1):
                result.add(f"{n:02d}")
        else:
            result.add(f"{int(part):02d}")
    return result


# ── Prerequisite check ────────────────────────────────────────────────────────

def check_prerequisites() -> tuple[bool, list[str]]:
    issues: list[str] = []
    adapter = os.environ.get("SPL_ADAPTER", "ollama")
    model   = os.environ.get("SPL_MODEL", "")

    click.echo(f"  SPL_ADAPTER = {adapter}")
    click.echo(f"  SPL_MODEL   = {model or '(default)'}")

    if adapter == "ollama":
        default_model = model or "llama3.2"
        try:
            import urllib.request
            with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3) as resp:
                available = {m["name"] for m in json.loads(resp.read()).get("models", [])}
            base = default_model.split(":")[0]
            matches = [m for m in available if m.startswith(base)]
            if matches:
                click.echo(f"  ✓  ollama {default_model} available ({matches[0]})")
            else:
                issues.append(f"  ✗  ollama model '{default_model}' not pulled  →  ollama pull {default_model}")
        except Exception:
            issues.append("  ✗  Ollama not reachable  →  run: ollama serve")

    elif adapter == "claude_cli":
        result = subprocess.run(["claude", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            click.echo(f"  ✓  claude CLI available: {result.stdout.strip()}")
        else:
            issues.append("  ✗  claude CLI not found  →  install Claude Code CLI")

    return len(issues) == 0, issues


# ── Runner ────────────────────────────────────────────────────────────────────

def run_recipe(recipe: dict, log_path: Path, env: dict) -> tuple[bool, float]:
    recipe_dir = COOKBOOK_DIR / recipe["dir"]
    cmd = [sys.executable, "-W", "ignore::RuntimeWarning", recipe["main_file"]]
    log_path.parent.mkdir(parents=True, exist_ok=True)
    start = datetime.now()
    try:
        with open(log_path, "w") as lf:
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=str(recipe_dir),
                env=env,
            )
            for line in (proc.stdout or []):
                lf.write(line)
                sys.stdout.write(f"     | {line.rstrip()}\n")
            proc.wait()
            ok = proc.returncode == 0
    except Exception as e:
        click.echo(f"     | ERROR: {e}")
        ok = False
    elapsed = (datetime.now() - start).total_seconds()
    return ok, elapsed


def run_recipe_parallel(recipe: dict, log_path: Path, env: dict) -> dict:
    rid, name = recipe["id"], recipe["name"]
    recipe_dir = COOKBOOK_DIR / recipe["dir"]
    cmd = [sys.executable, "-W", "ignore::RuntimeWarning", recipe["main_file"]]
    log_path.parent.mkdir(parents=True, exist_ok=True)
    start = datetime.now()
    click.echo(f"[{rid}] {name}  →  started")
    sys.stdout.flush()
    try:
        with open(log_path, "w") as lf:
            proc = subprocess.Popen(
                cmd, stdout=lf, stderr=subprocess.STDOUT,
                text=True, cwd=str(recipe_dir), env=env,
            )
            proc.wait()
        ok = proc.returncode == 0
    except Exception as e:
        click.echo(f"[{rid}] ERROR: {e}")
        ok = False
    elapsed = (datetime.now() - start).total_seconds()
    click.echo(f"[{rid}] {name}  →  {'SUCCESS' if ok else 'FAILED'}  ({elapsed:.1f}s)")
    sys.stdout.flush()
    return {"id": rid, "name": name, "ok": ok, "elapsed": elapsed}


# ── Display ───────────────────────────────────────────────────────────────────

def print_list(recipes: list[dict]) -> None:
    click.echo(f"\n{'ID':<6} {'Name':<36} {'Status':<10} {'Category'}")
    click.echo("-" * 72)
    for r in recipes:
        active = "active" if r.get("is_active") else "inactive"
        click.echo(f"{r['id']:<6} {r['name']:<36} {active:<10} {r.get('category', '')}")


def print_catalog(recipes: list[dict]) -> None:
    click.echo(f"\n{'ID':<6} {'Name':<36} {'Category':<16} {'Status'}")
    click.echo("-" * 80)
    for r in recipes:
        active = "active" if r.get("is_active") else "inactive"
        click.echo(f"{r['id']:<6} {r['name']:<36} {r.get('category',''):<16} {active}")
        click.echo(f"       {r['description'][:100]}")
        click.echo()


# ── Main ──────────────────────────────────────────────────────────────────────

@click.command()
@click.argument("command", default="run",
                type=click.Choice(["run", "list", "catalog", "check"]))
@click.option("--ids",      default=None, help="IDs or ranges, e.g. 1-10 or 2,5,8")
@click.option("--category", default=None, help="Filter by category (e.g. basics, agentic)")
@click.option("--all",      "include_all", is_flag=True, help="Include inactive recipes")
@click.option("--workers",  default=1, show_default=True, type=int,
              help="Parallel workers (1 = sequential)")
@click.option("--timeout",  default=120, show_default=True, type=int,
              help="Seconds before a recipe is killed (0 = no limit)")
def main(command, ids, category, include_all, workers, timeout) -> None:
    """PocketFlow Cookbook batch runner for SPL benchmark."""
    recipes  = load_catalog()
    id_set   = parse_id_filter(ids) if ids else set()

    filtered = apply_filters(
        recipes,
        category=category or "",
        ids=id_set,
        include_inactive=include_all or bool(id_set),
    )

    if command == "list":
        print_list(filtered)
        click.echo(f"\n{len(filtered)} recipe(s)")
        return

    if command == "catalog":
        print_catalog(filtered)
        return

    if command == "check":
        click.echo(f"\nChecking prerequisites...\n")
        ok, issues = check_prerequisites()
        if issues:
            click.echo("\nIssues found:")
            for issue in issues:
                click.echo(issue)
            sys.exit(1)
        click.echo("\nAll prerequisites satisfied.")
        return

    # ── run ──────────────────────────────────────────────────────────────────
    if not filtered:
        click.echo("No recipes match. Use --all to include inactive recipes.")
        sys.exit(0)

    # Pass current environment (includes SPL_ADAPTER / SPL_MODEL)
    env = os.environ.copy()

    adapter = env.get("SPL_ADAPTER", "ollama")
    model   = env.get("SPL_MODEL", "gemma3" if adapter == "ollama" else "claude-sonnet-4-6")

    ts      = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = COOKBOOK_DIR / "logs"
    log_dir.mkdir(exist_ok=True)

    click.echo(f"\n{'='*60}")
    click.echo(f"PocketFlow Cookbook — {len(filtered)} recipe(s)  [{ts}]")
    click.echo(f"Adapter: {adapter}  Model: {model}")
    click.echo(f"{'='*60}\n")

    results: list[dict] = []

    if workers > 1:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            log_paths = {
                r["id"]: log_dir / f"{r['id']}_{r['dir']}_{ts}.md"
                for r in filtered
            }
            futures = {
                pool.submit(run_recipe_parallel, r, log_paths[r["id"]], env): r
                for r in filtered
            }
            for fut in as_completed(futures):
                results.append(fut.result())
        results.sort(key=lambda x: x["id"])
    else:
        for r in filtered:
            rid, name = r["id"], r["name"]
            log_path = log_dir / f"{rid}_{r['dir']}_{ts}.md"
            click.echo(f"[{rid}] {name}")
            ok, elapsed = run_recipe(r, log_path, env)
            status_str = "SUCCESS" if ok else "FAILED"
            click.echo(f"[{rid}] {status_str}  ({elapsed:.1f}s)  log: {log_path.name}\n")
            results.append({"id": rid, "name": name, "ok": ok, "elapsed": elapsed})

    passed = [r for r in results if r["ok"]]
    failed = [r for r in results if not r["ok"]]
    total_s = sum(r["elapsed"] for r in results)

    click.echo(f"\n{'='*60}")
    click.echo(f"Summary: {len(passed)}/{len(results)} passed  ({total_s:.1f}s total)")
    click.echo(f"Adapter: {adapter}  Model: {model}")
    if failed:
        click.echo(f"\nFailed:")
        for r in failed:
            click.echo(f"  [{r['id']}] {r['name']}")
    click.echo(f"{'='*60}\n")

    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
