#!/usr/bin/env python3
"""Automate Codex runs for the MLBB overlay engine."""
import os
import subprocess
import sys
from datetime import datetime

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
REPO_PATH = os.getenv('REPO_PATH', os.getcwd())

if not all([OPENAI_API_KEY, GITHUB_TOKEN]):
    print('Missing OPENAI_API_KEY or GITHUB_TOKEN.')
    sys.exit(1)

prompt = """
Refactor MLBB overlay engine ...
1. dynamic zoom overlay for drone map
...
"""

subprocess.run([
    'codex',
    '--full-auto',
    '--approval-mode', 'full-auto',
    '--prompt', prompt
], cwd=REPO_PATH)

if DISCORD_WEBHOOK_URL:
    import requests
    requests.post(DISCORD_WEBHOOK_URL, json={
        'content': f"Codex MLBB overlay updated at {datetime.utcnow().isoformat()} UTC"
    })

print('Done. Review changes and commit.')
