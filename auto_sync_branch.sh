#!/usr/bin/env bash
###############################################################################
# Auto-sync PR branch with origin/main, resolving simple conflicts automatically
# Strategy: keep *this branch's* version on overlap (git merge -X ours).
# Safe because we push back with --force-with-lease.
###############################################################################
set -Eeuo pipefail
IFS=$'\n\t'

# 0. Bot identity for commits
git config --global user.name  "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"

branch=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: ${branch}"

# 1. Sync refs
git fetch --quiet origin main

# Fast-forward check
if git merge-base --is-ancestor origin/main "${branch}"; then
  echo "Branch already up-to-date with origin/main"
  exit 0
fi

echo "Branch behind main - attempting auto-merge"

# 2. Merge with ours-preference
set +e
git merge -X ours --no-edit origin/main
merge_rc=$?
set -e

if [ $merge_rc -ne 0 ]; then
  echo "Complex conflict encountered - manual rebase still required."
  git merge --abort || true
  exit 1
fi

echo "Auto-merge completed."

# 3. Show summary of touched files
echo "Files merged:"
git diff --name-only HEAD~1 HEAD

# 4. Push back (safe force)
git push --force-with-lease origin "${branch}"

echo "Branch updated; CI can continue."
