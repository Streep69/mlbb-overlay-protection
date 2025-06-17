# mlbb-overlay-protection

This project provides a non-root overlay cheat framework for Mobile Legends: Bang Bang streamed from an S23 Ultra to a Raspberry Pi.

## Installation
Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

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

## Contributing (Mitmachen)
* Sanitize all Python files with `ci/remove_cjk.py` and `ci/remove_bidi.py`.
* Execute `pytest -q` before committing to ensure the test suite passes.
* Commit only clean code and follow concise commit messages.
* Remember to update `full_chat_log.md` whenever changes are made.
