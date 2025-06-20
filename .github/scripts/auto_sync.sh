#!/usr/bin/env bash
set -Eeuo pipefail; IFS=$'\n\t'

git config --global user.name  "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"

branch=$(git rev-parse --abbrev-ref HEAD)
git fetch --quiet origin main

if git merge-base --is-ancestor origin/main "$branch"; then
  echo "Up-to-date"; exit 0; fi

if git merge -X ours --no-edit origin/main; then
  echo "Merge clean"
else
  echo "Resolving add/add conflicts"
  for f in $(git diff --name-only --diff-filter=U); do
    git checkout --ours  -- "$f"
    git checkout --theirs -- "$f"
    mv "$f" "${f}.from-main"
    git add "$f" "${f}.from-main"
  done
  git commit -m "ci: auto-resolve add/add (ours + .from-main)"
fi

git remote set-url origin \
  "https://x-access-token:${GH_PAT}@github.com/${GITHUB_REPOSITORY}.git"
git push --force-with-lease origin "$branch"
echo "Auto-sync done"
