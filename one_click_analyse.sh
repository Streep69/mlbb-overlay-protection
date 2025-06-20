#!/usr/bin/env bash
# Merge & sanitize all codex branches in one step
set -Eeuo pipefail
IFS=$'\n\t'

: "${GH_PAT:?GH_PAT secret missing (Settings ➜ Secrets ➜ Actions ➜ GH_PAT)}"

git config --global user.name  "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"

repo=$(git config --get remote.origin.url | sed -E 's#https://[^/]+/##;s#\.git$##')
git remote set-url origin "https://x-access-token:${GH_PAT}@github.com/${repo}.git"

# Ensure dependencies are installed
pip install -r requirements.txt >/dev/null

# Run the merge helper
dir=$(dirname "$0")
"${dir}/merge_codex_branches.sh"

echo "One-click analyse complete"
