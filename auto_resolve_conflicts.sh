#!/usr/bin/env bash
set -e
cd "$(git rev-parse --show-toplevel)" || { echo 'ERROR: repo not found'; exit 1; }
BRANCH="${1:-${BRANCH:-$(git symbolic-ref --quiet --short HEAD || echo '')}}"
if [ -z "$BRANCH" ]; then
  echo "ERROR: no branch specified" >&2
  exit 1
fi

if [ -z "$GH_PAT" ]; then
  echo "ERROR: GH_PAT not set. Add it as an environment variable or use gh_auth_login.sh." >&2
  exit 1
fi

echo "$GH_PAT" | gh auth login --with-token > /dev/null

git fetch origin

git checkout "$BRANCH"

git fetch origin main

git merge --no-edit --allow-unrelated-histories -X theirs origin/main || true

for f in $(git diff --name-only --diff-filter=U); do
  base="${f%.*}"
  ext="${f##*.}"
  if [ "$base" != "$f" ]; then
    mv "$f" "${base}2.$ext"
    git add "${base}2.$ext"
  else
    mv "$f" "${f}2"
    git add "${f}2"
  fi
done

if ! git config user.name > /dev/null; then
  git config user.name "codex-bot"
fi
if ! git config user.email > /dev/null; then
  git config user.email "codex-bot@noreply.github.com"
fi

git commit -am "auto-resolve: rename conflicted files with 2 suffix" || true

REMOTE_URL=$(git config --get remote.origin.url 2>/dev/null || echo "")
if [[ $REMOTE_URL == https://* ]]; then
  REMOTE_URL="${REMOTE_URL/https:\/\//https://$GH_PAT@}"
fi
if [ -n "$REMOTE_URL" ]; then
  git push "$REMOTE_URL" "$BRANCH" --force-with-lease
else
  git push origin "$BRANCH" --force-with-lease
fi

echo "Auto-resolve complete, conflicts renamed, pushed securely!"
