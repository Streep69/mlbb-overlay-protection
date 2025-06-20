#!/usr/bin/env bash
set -e
cd ~/mlbb-overlay-protection || { echo '❌ Repo not found'; exit 1; }
BRANCH='0mjgdv-codex/add-agents.md-to-mlbb-cheat-project'

git fetch origin

git checkout "$BRANCH"

git merge --abort 2>/dev/null || true
git rebase --abort 2>/dev/null || true

git rebase origin/main --allow-unrelated-histories -X theirs

git push origin "$BRANCH" --force-with-lease

echo '✅ Rebase with unrelated histories complete and pushed.'
