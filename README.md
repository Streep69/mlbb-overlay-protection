# mlbb-overlay-protection

This project delivers a lightweight anti-cheat framework for Mobile Legends: Bang Bang. It runs without root on an S23 Ultra and streams telemetry to a Raspberry Pi for analysis.

## Installation
Install system and Python dependencies then install packages from `requirements.txt`:

```bash
sudo apt update && sudo apt install -y adb ffmpeg libusb-1.0-0-dev
pip install -r requirements.txt
```

## Vector Modules
Modules `vector001`–`vector163` implement detection vectors. Example advanced modules include:

- `vector149` – Tkinter security dashboard with a REST endpoint.
- `vector150` – IsolationForest anomaly detector using sandbox session data.

## Setup
Use **Python 3.12** or newer. Create a virtual environment and install the dependencies listed in `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Development
Run sanitizers and tests before committing:

```bash
python ci/remove_cjk.py $(git ls-files '*.py')
python ci/remove_bidi.py $(git ls-files '*.py')
pytest -q
```

## Continuous Integration
> ⚠ We enforce ASCII-only content. CI workflows use a Personal Access Token (`GH_PAT`) with `repo` scope. Checkouts use `persist-credentials: false` and the PAT to push back to protected branches. Pull requests labeled `automerge` merge automatically when CI passes. Before pushing, the workflow checks if the branch is synced with `main` and fails if conflicts occur.

- Use `./gh_auth_login.sh` to install GitHub CLI, authenticate with `GH_PAT`, and verify authentication.
- Run `./codex_cli_setup.sh` to configure git identity and fetch all branches.
- CI sets the git committer identity to `github-actions[bot]` so workflow commits are attributed correctly.
- After logging in, update the git remote to push using the PAT:

```bash
git remote set-url origin https://x-access-token:${GH_PAT}@github.com/Streep69/mlbb-overlay-protection.git
```

## Contributing
* Sanitize Python files with `ci/remove_cjk.py` and `ci/remove_bidi.py`.
* Execute `pytest -q` before committing.
* Commit only clean code with concise messages.
* Update `full_chat_log.md` whenever changes are made.
* See `AGENTS.md` for detailed project workflow and security guidelines.

## Auto Rebase
Run the automated rebase script when histories diverge:

```bash
./auto_rebase_allow.sh my-feature-branch
```

It executes `git rebase origin/main --allow-unrelated-histories -X theirs`. Conflicts are resolved in favor of the feature branch.

## Auto Resolve Conflicts
If merging `main` results in conflicts you want to resolve quickly, run:

```bash
./auto_resolve_conflicts.sh
```

It merges `main` with `-X theirs`, renames conflicted files with a `2` suffix, and pushes the result using `GH_PAT`.

## Auto Sync Branch
Use the sync script to merge `main` into your branch automatically when simple conflicts occur:

```bash
./auto_sync_branch.sh
```

It merges `main` using `git merge -X ours` to prefer the branch's version and pushes back with `--force-with-lease`.
CI performs the same sync automatically using `.github/scripts/auto_sync.sh` and the `GH_PAT` token.

## Merge Codex Branches
When several `codex-*` branches exist on the remote, you can consolidate them
into `main` with:

```bash
./merge_codex_branches.sh
```

The script creates a backup branch for each merge, resolves conflicts by
renaming both versions, sanitizes files for ASCII compliance, logs diffs and
commit history to the `vector/` folder, runs the tests, regenerates
`requirements.txt`, and force pushes the updated `main` branch.
