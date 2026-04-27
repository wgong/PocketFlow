🎨 PocketFlow Self-Healing Mermaid Generator

🤔 Task: A flowchart showing a CI/CD pipeline: code push triggers build, then parallel test and lint, then deploy to staging, manual approval, deploy to production

/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py:44: UserWarning: Flow ends: 'done' not found in ['fix']
  if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
✍️  Generating Mermaid diagram...
  Generated chart (167 chars)
🔍 Compiling Mermaid diagram...
  Compilation failed (attempt 1/3)
  Error: Compilation timed out after 60 seconds
  💡 Will retry with error feedback...
✍️  Generating Mermaid diagram...
  Generated chart (252 chars)
🔍 Compiling Mermaid diagram...
  Compilation failed (attempt 2/3)
  Error: Compilation timed out after 60 seconds
  💡 Will retry with error feedback...
✍️  Generating Mermaid diagram...
  Generated chart (223 chars)
🔍 Compiling Mermaid diagram...
  Compilation failed (attempt 3/3)
  Error: Compilation timed out after 60 seconds
  Max retries reached. Giving up.

=== Result ===
  Status: FAILED after 3 attempts
  Last error: Compilation timed out after 60 seconds

  Mermaid code:

    graph TD
        A[Code Push] --> B(Build);
        B --> C{Test & Lint (Parallel)};
        C --> D{Staging Deploy};
        D --> E[Manual Approval];
        E -- Approved --> F{Production Deploy};
        E -- Rejected --> G[Rollback to Build];

✅ Saved to: output/diagram.md
