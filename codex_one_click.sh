#!/usr/bin/env bash
# 1-CLICK CODEX SCRIPT - sanitize + auto-sync + push (PAT)
# ASCII-only

set -Eeuo pipefail
IFS=$'\n\t'

TARGET_BRANCH="main"
PAT_ENV_NAME="GH_PAT"
CODE_EXTS="py sh js ts go java rb rs c cpp h json yaml yml"

# Preconditions
: "${!PAT_ENV_NAME:?ERROR  Personal-access token not exported as ${PAT_ENV_NAME}}"
git rev-parse --is-inside-work-tree >/dev/null || { echo "Not a git repo"; exit 1; }

# Identity
git config --global user.name  "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"

# Unicode sanitization
echo "Cleaning files"
for f in $(git ls-files *.{${CODE_EXTS// /,}} 2>/dev/null); do
  perl -CSD -pe 's/[\x{202A}-\x{202E}\x{2066}-\x{2069}]//g;
                 s/[\x{200B}-\x{200F}\x{FEFF}]//g;
                 s/[^\x00-\x7F]//g' "$f" > "$f.ascii"
  mv "$f.ascii" "$f"
done

# ASCII guard
echo "Verifying ASCII-only code"
grep -R -nP '[^\x00-\x7F]' --include="*.{${CODE_EXTS// /,}}" --exclude-dir='.git' . \
  && { echo '[fail] non-ASCII bytes remain'; exit 1; } \
  || echo '[ok] code ASCII clean'

# Auto-sync with main
CURRENT=$(git rev-parse --abbrev-ref HEAD)
echo "Syncing $CURRENT with origin/${TARGET_BRANCH}"
git fetch --quiet origin "${TARGET_BRANCH}"

if git merge-base --is-ancestor "origin/${TARGET_BRANCH}" "$CURRENT"; then
  echo "- already up-to-date"
else
  if git merge -X ours --no-edit "origin/${TARGET_BRANCH}"; then
    echo "- merge clean"
  else
    echo "Resolving add/add conflicts"
    for p in $(git diff --name-only --diff-filter=U); do
      git checkout --ours  -- "$p"
      git checkout --theirs -- "$p"
      mv "$p" "${p}.from-main"
      git add "$p" "${p}.from-main"
    done
    git commit -m "ci: auto-resolve add/add (ours + .from-main)"
  fi
fi

# Push
TOKEN=${!PAT_ENV_NAME}
repo_path=$(git config --get remote.origin.url | sed -E 's#https://[^/]+/##' | sed 's#\.git$##')
git remote set-url origin "https://x-access-token:${TOKEN}@github.com/${repo_path}"
git push --force-with-lease origin "$CURRENT"
echo "Push complete to origin/$CURRENT"

echo "One-click script complete."
