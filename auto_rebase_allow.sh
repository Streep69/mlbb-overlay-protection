#!/usr/bin/env bash
set -e
cd "$(git rev-parse --show-toplevel)" || { echo '❌ Repo not found'; exit 1; }
BRANCH="${1:-${BRANCH:-$(git symbolic-ref --quiet --short HEAD || echo '')}}"
if [ -z "$BRANCH" ]; then
  echo "❌ No branch specified" >&2
  exit 1
fi

git fetch origin

git checkout "$BRANCH"

git merge --abort 2>/dev/null || true
git rebase --abort 2>/dev/null || true


git rebase origin/main --allow-unrelated-histories -X theirs

REMOTE_URL=$(git config --get remote.origin.url 2>/dev/null || echo "")
if [ -n "$GH_PAT" ] && [[ $REMOTE_URL == https://* ]]; then
  REMOTE_URL="${REMOTE_URL/https:\/\//https:\/\/$GH_PAT@}"
fi
if [ -n "$REMOTE_URL" ]; then
  git push "$REMOTE_URL" "$BRANCH" --force-with-lease
else
  git push origin "$BRANCH" --force-with-lease
fi

echo "✅ Rebase with unrelated histories complete and pushed for $BRANCH."
