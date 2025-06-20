#!/usr/bin/env bash
# Setup Git identity and authenticate GitHub CLI using GH_PAT
set -e

# 1. Git identity
if ! git config user.name >/dev/null; then
  git config user.name "codex-bot"
fi
if ! git config user.email >/dev/null; then
  git config user.email "codex-bot@noreply.github.com"
fi

# 2. Authenticate GitHub CLI with PAT
if [ -z "$GH_PAT" ]; then
  echo "\u274c GH_PAT is not set. Please add it as a repo secret or set it in your environment." >&2
  exit 1
fi

echo "$GH_PAT" | gh auth login --with-token

# 3. Add remote and fetch
if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin https://github.com/Streep69/mlbb-overlay-protection.git
fi

git fetch origin --all

echo '✅ Codex CLI: Full control granted (via injected PAT, not leaked)!'
