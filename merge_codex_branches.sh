#!/usr/bin/env bash
# Merge all remote codex-* branches into main with automatic conflict handling.
# Creates a backup branch before merging and sanitizes files.
set -Eeuo pipefail
IFS=$'\n\t'

# Ensure we start from a clean main branch
git fetch origin
git checkout main
git reset --hard origin/main

# Make sure pip is available
if ! command -v pip >/dev/null; then
    python3 -m ensurepip --upgrade
fi

for remote in $(git branch -r | grep '^ *origin/' | sed 's# *origin/##' | grep -vE '^(main|HEAD)$'); do
    if [[ ! "$remote" =~ ^codex ]]; then
        continue
    fi
    echo "=== Merging $remote into main ==="
    backup_branch="backup-before-$(echo $remote | tr '/' '_')"
    git checkout main
    git pull origin main
    git branch -D "$backup_branch" 2>/dev/null || true
    git branch "$backup_branch"
    git push origin "$backup_branch"

    git merge --no-edit "origin/$remote" || true
    if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
        echo "Resolving conflicts"
        for file in $(git diff --name-only --diff-filter=U); do
            dir=$(dirname "$file")
            base=$(basename "$file")
            git checkout main -- "$file"
            mkdir -p "$dir"
            cp "$file" "${dir}/${base}.from_main"
            git checkout "$remote" -- "$file"
            mv "$file" "${dir}/${base}.from_branch"
            git rm -f "$file"
            git add "${dir}/${base}.from_main" "${dir}/${base}.from_branch"
        done
        git commit -m "Auto-resolved conflicts for $remote"
    fi

    echo "Sanitizing files"
    python3 ci/remove_cjk.py $(git ls-files '*.py' '*.md' '*.yml' '*.sh') || true
    python3 ci/remove_bidi.py $(git ls-files '*.py' '*.md' '*.yml' '*.sh') || true

    echo "Running tests"
    pip install -r requirements.txt >/dev/null 2>&1 || true
    pytest -q || true

    pip freeze > requirements.txt
    git add requirements.txt
    git commit -m "Regenerated requirements.txt" || true

    git push origin main --force
    echo "Finished processing $remote"
    git checkout main
    git reset --hard origin/main

done

echo "Automation complete"
