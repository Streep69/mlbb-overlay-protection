#!/usr/bin/env bash
set -e
cd ~/mlbb-overlay-protection || exit 1
BRANCH='0ipigq-codex/add-agents.md-to-mlbb-cheat-project'

git fetch origin

git checkout "$BRANCH"

git merge --abort 2>/dev/null || true
git rebase --abort 2>/dev/null || true

git merge --no-edit --allow-unrelated-histories -X theirs origin/main

git push origin "$BRANCH" --force-with-lease

echo 'DONE Auto rebase with unrelated histories applied and pushed'
