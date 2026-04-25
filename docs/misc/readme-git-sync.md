# Syncing your Fork with the Original Repository

If your branch is ahead of and behind the original repository (upstream), follow these steps to bring it in sync while preserving your valuable changes.

## 1. Configure Upstream Remote

If you haven't already, add the original repository as a remote named `upstream`.

```bash
# Add the original repository as a remote
git remote add upstream https://github.com/The-Pocket/PocketFlow.git

# Verify your remotes
git remote -v
```

## 2. Fetch the Latest Changes

Fetch all branches and tags from the upstream repository without modifying your local code.

```bash
git fetch upstream
```

## 3. Merge Upstream Changes into Your Branch

Ensure you are on the branch you want to sync (usually `main`).

```bash
# Switch to your main branch
git checkout main

# Merge the upstream changes into your local branch
git merge upstream/main
```

```output
Auto-merging cookbook/README.md
CONFLICT (content): Merge conflict in cookbook/README.md
Auto-merging cookbook/pocketflow-workflow/nodes.py
CONFLICT (content): Merge conflict in cookbook/pocketflow-workflow/nodes.py
Automatic merge failed; fix conflicts and then commit the result.
```

## 4. Resolve Conflicts Manually

Since you have changes that are not in the upstream repo, git might report conflicts.

1.  **Identify conflicted files**: Run `git status` to see which files have "both modified" markers.
2.  **Edit the files**: Open the conflicted files and look for the conflict markers:
    ```text
    <<<<<<< HEAD
    Your valuable changes
    =======
    Changes from the original repo
    >>>>>>> upstream/main
    ```
3.  **Choose the desired code**: Keep your valuable changes, incorporate the new upstream logic, or combine both. Remove the markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4.  **Mark as resolved**:
    ```bash
    git add <file-name>
    ```

## 5. Complete the Sync

Once all conflicts are resolved and added:

```bash
# Commit the merge
git commit -m "chore: sync with upstream/main and resolve conflicts"

# Push the updated branch to your GitHub fork
git push origin main
```

---

### Alternative: Rebase (Cleaner History)

If you prefer a linear history and want your 13 commits to appear *after* the 94 upstream commits, you can use rebase. **Note:** This rewrites history, so use with caution if others are collaborating on your fork.

```bash
git fetch upstream
git rebase upstream/main
# Resolve conflicts for each commit as prompted
# git add <file>
# git rebase --continue
git push origin main --force
```
