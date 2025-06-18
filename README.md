# mlbb-overlay-protection

This project delivers a lightweight anti-cheat framework for Mobile Legends: Bang Bang. It runs without root on an S23 Ultra and streams telemetry to a Raspberry Pi for analysis.

## Installation
Install system and Python dependencies then install packages from `requirements.txt`:

```bash
sudo apt update && sudo apt install -y adb ffmpeg libusb-1.0-0-dev
pip install -r requirements.txt
```

## Vector Modules
Modules `vector001`-`vector163` implement individual detection vectors. Each exposes a `run()` function returning a status string. Example advanced modules include:

- `vector149` - Tkinter security dashboard with a REST endpoint.
- `vector150` - IsolationForest anomaly detector using sandbox session data.

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
> ⚠ We enforce ASCII-only content. CI will block hidden or malicious Unicode. The GitHub Actions workflow requires a Personal Access Token (PAT) stored as `GH_PAT` in the repository secrets. Generate a token with **repo** scope and add it via *Settings → Secrets → Actions*. The workflow checks out with `persist-credentials: false` and uses this PAT to push changes back to protected branches. The workflow labels pull requests with `automerge` and automatically merges them when CI passes. After sanitization and tests succeed, the workflow pushes the cleaned code back to the protected branch using the PAT. Before pushing, it checks whether the branch is synced with `main`; if not, the job fails with instructions to merge or rebase `main` manually. To update a pull request automatically, comment `/rebase` or add the `rebase` label. The *auto_rebase* workflow rebases the branch onto `main` using `cirrus-actions/rebase` and then removes the label.
- Use `./gh_auth_login.sh` to install GitHub CLI if needed, authenticate with `GH_PAT`, setup git, and show `gh auth status`.
- Run `./codex_cli_setup.sh` to configure git identity, authenticate, and fetch all branches when you need full CLI control.
- After logging in, update the git remote to push using the PAT:

```bash
git remote set-url origin https://x-access-token:${GH_PAT}@github.com/Streep69/mlbb-overlay-protection.git
```

## Contributing (Mitmachen)
* Sanitize all Python files with `ci/remove_cjk.py` and `ci/remove_bidi.py`.
* Execute `pytest -q` before committing to ensure the test suite passes.
* Commit only clean code and follow concise commit messages.
* Remember to update `full_chat_log.md` whenever changes are made.
* See `AGENTS.md` for detailed project workflow and security guidelines.

## Auto Rebase
Run the automated rebase script when histories diverge:

```bash
./auto_rebase_allow.sh
```

The script executes `git rebase origin/main --allow-unrelated-histories -X theirs`. Conflicts are resolved in favor of the feature branch, overwriting files from `main` if necessary.

## Auto Resolve Conflicts
If a merge with `main` results in conflicts you do not wish to resolve manually,
run the auto-resolve script:

```bash
./auto_resolve_conflicts.sh
```

It merges `main` using `-X theirs`, renames conflicted files with a `2` suffix,
and pushes the result using `GH_PAT`.
