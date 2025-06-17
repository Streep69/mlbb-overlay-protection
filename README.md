# mlbb-overlay-protection

This project provides a non-root overlay cheat framework for Mobile Legends: Bang Bang streamed from an S23 Ultra to a Raspberry Pi.

## Vector Modules
Placeholder modules `vector001`–`vector163` implement individual anti-cheat checks. Each exposes a `run()` function returning a status string.

## Setup
Use **Python 3.12** or newer. Create a virtual environment and install the
dependencies listed in `requirements.txt`:

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

## CI with Personal Access Token
GitHub Actions uses a `GH_PAT` secret with a personal access token to push
changes back to protected branches. Generate a token with **repo** scope from the
GitHub settings page and add it as a repository secret. The workflow checks out
code with `persist-credentials: false` to ensure pushes use the PAT.

## Contributing (Mitmachen)
* Sanitize all Python files with `ci/remove_cjk.py` and `ci/remove_bidi.py`.
* Execute `pytest -q` before committing to ensure the test suite passes.
* Commit only clean code and follow concise commit messages.
* Remember to update `full_chat_log.md` whenever changes are made.
