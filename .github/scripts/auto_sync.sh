#!/usr/bin/env bash
set -Eeuo pipefail; IFS=$'\n\t'

git config --global user.name  "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
branch=$(git rev-parse --abbrev-ref HEAD)
echo "🔄 syncing $branch with origin/main"

git fetch --quiet origin main
if git merge-base --is-ancestor origin/main "$branch"; then
  echo "✅ up-to-date"; exit 0; fi

echo "↻ merging origin/main (prefer ours)…"
if git merge -X ours --no-edit origin/main; then
  echo "✅ merge clean"
else
  echo "⚠ resolving add/add conflicts"
  for f in $(git diff --name-only --diff-filter=U); do
    echo " • $f"
    git checkout --ours  -- "$f"
    git checkout --theirs -- "$f"
    mv "$f" "${f}.from-main"
    git add "$f" "${f}.from-main"
  done
  git commit -m "ci: auto-resolve add/add (ours + .from-main)"
fi

git push --force-with-lease origin "$branch"
echo "🚀 branch updated"
