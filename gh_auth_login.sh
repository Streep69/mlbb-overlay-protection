#!/usr/bin/env bash
# Login to GitHub CLI using a Personal Access Token with repo scope
if ! command -v gh >/dev/null; then
    echo "Installing GitHub CLI..."
    sudo apt-get update && sudo apt-get install -y gh
fi
if [ -z "$GH_PAT" ]; then
    echo "GH_PAT environment variable not set"
    exit 1
fi
echo "$GH_PAT" | gh auth login --with-token
# Configure git to use gh auth
gh auth setup-git
gh auth status

echo "✅ GitHub CLI is authenticated with full repo access."
