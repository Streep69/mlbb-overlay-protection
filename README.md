# mlbb-overlay-protection

This project delivers a lightweight anti-cheat framework for Mobile Legends: Bang Bang. It runs without root on an S23 Ultra and streams telemetry to a Raspberry Pi for analysis.

## Installation
Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
The file now includes `requests` for sending webhook notifications.

## Vector Modules
Modules `vector001`–`vector163` implement individual detection vectors. Each exposes a `run()` function returning a status string. Example advanced modules include:

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
The GitHub Actions workflow requires a Personal Access Token (PAT) stored as `GH_PAT` in the repository secrets. Generate a token with **repo** scope and add it via *Settings → Secrets → Actions*. The workflow checks out with `persist-credentials: false` and uses this PAT to push changes back to protected branches.
The workflow labels pull requests with `automerge` and automatically merges them when CI passes. After sanitization and tests succeed, the workflow pushes the cleaned code back to the protected branch using the PAT. Before pushing, it checks whether the branch is synced with `main`; if not, the job fails with instructions to merge or rebase `main` manually. Once the branch is up to date, the workflow pushes the sanitized code and merges the pull request. To update a pull request automatically, comment `/rebase` or add the `rebase` label. The *auto_rebase* workflow rebases the branch onto `main` using `cirrus-actions/rebase` and then removes the label.

## Contributing (Mitmachen)
* Sanitize all Python files with `ci/remove_cjk.py` and `ci/remove_bidi.py`.
* Execute `pytest -q` before committing to ensure the test suite passes.
* Commit only clean code and follow concise commit messages.
* Remember to update `full_chat_log.md` whenever changes are made.

## Auto Rebase
Run the automated rebase script when histories diverge. Pass the branch name as
an argument or set `BRANCH` to override the default of the current branch. If
`GH_PAT` is set, the script uses it to authenticate pushes:

```bash
./auto_rebase_allow.sh my-feature-branch
```

The script executes `git rebase origin/main --allow-unrelated-histories -X theirs`.
Conflicts are resolved in favor of the feature branch, overwriting files from
`main` if necessary.

## Continuous Integration
> ⚠ We enforce ASCII-only content. CI blocks hidden or malicious Unicode. Workflows require a Personal Access Token stored as `GH_PAT` in repository secrets. Generate a token with **repo** scope and add it via *Settings → Secrets → Actions*. Checkouts use `persist-credentials: false` and this PAT to push back to protected branches. Pull requests labeled `automerge` merge automatically when CI passes. Before pushing, the workflow checks if the branch is synced with `main`; if conflicts occur, it fails and instructs you to update.

- Use `./gh_auth_login.sh` to install GitHub CLI, authenticate with `GH_PAT`, and confirm with `gh auth status`.
- After authenticating, update the git remote:

```bash
git remote set-url origin https://x-access-token:${GH_PAT}@github.com/Streep69/mlbb-overlay-protection.git
```

## Auto Resolve Conflicts
If merging `main` results in conflicts you want to resolve quickly, run the auto-resolve script:

```bash
./auto_resolve_conflicts.sh
```

It merges `main` with `-X theirs`, renames conflicted files with a `2` suffix, and pushes the result using `GH_PAT`.
