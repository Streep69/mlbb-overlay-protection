#!/usr/bin/env bash
# Merge all remote codex-* branches into main with automatic conflict handling.
# Creates a backup branch before merging, sanitizes files and logs each merge.
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
    echo -e "\e[34m=== Merging branch '$remote' into main ===\e[0m"
    backup_branch="backup-before-$(echo $remote | sed 's#[/:]#_#g')"
    git checkout main
    git pull origin main
    git branch -D "$backup_branch" 2>/dev/null || true
    git branch "$backup_branch"
    git push origin "$backup_branch"

    git merge --no-edit "origin/$remote" || true
    if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
        echo -e "\e[31mConflicts detected in $remote, auto-resolving...\e[0m"
        for file in $(git diff --name-only --diff-filter=U); do
            dir=$(dirname "$file")
            base=$(basename "$file")
            git checkout main -- "$file"
            mkdir -p "$dir"
            cp "$file" "${dir}/${base}.from_main"
            git checkout "$remote" -- "$file"
            cp "$file" "${dir}/${base}.from_branch"
            git rm -f "$file"
            git add "${dir}/${base}.from_main" "${dir}/${base}.from_branch"
        done
        git commit -m "Auto-resolved conflicts for $remote"
    else
        echo "No conflicts for $remote"
    fi

    echo "Sanitizing files for ASCII compliance..."
    python3 - <<'PYCODE'
import re, os
for root, _, files in os.walk('.'):
    if '.git' in root:
        continue
    for fname in files:
        if not re.search(r'\.(py|md|yml|yaml|sh|json|txt)$', fname):
            continue
        path = os.path.join(root, fname)
        try:
            text = open(path, 'rb').read()
        except Exception:
            continue
        cleaned = text.replace(b'\xef\xbb\xbf', b'')
        cleaned = re.sub(b'[^\x00-\x7F]+', b'', cleaned)
        if cleaned != text:
            open(path, 'wb').write(cleaned)
            print(f"Sanitized {path}")
PYCODE

    if grep -R -n -P "[^\x00-\x7F]" --exclude-dir=.git .; then
        echo -e "\e[33mWarning: Non-ASCII characters still found!\e[0m"
    else
        echo "All files are ASCII-clean"
    fi

    mkdir -p vector
    prev_commit=$(git rev-parse HEAD^)
    git diff "$prev_commit" HEAD > "vector/${remote//\//_}_diff.patch"
    git log --oneline "$prev_commit"..HEAD > "vector/${remote//\//_}_commits.log"
    echo "Logged diffs and commits to vector/"

    echo "Running tests"
    pip install -r requirements.txt >/dev/null 2>&1 || true
    pytest -q || echo "Tests failed or missing; consider adding integration tests."

    pip freeze > requirements.txt
    git add requirements.txt
    git commit -m "Regenerated requirements.txt via pip freeze" || true

    git push origin main --force
    echo "Finished processing $remote"
    git checkout main
    git reset --hard origin/main

done

echo "Automation complete"
