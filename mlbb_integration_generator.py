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
    from urllib.parse import urlparse
    
    # Validate DISCORD_WEBHOOK_URL
    parsed_url = urlparse(DISCORD_WEBHOOK_URL)
    if parsed_url.scheme in ["http", "https"] and parsed_url.netloc.endswith("discord.com"):
        requests.post(DISCORD_WEBHOOK_URL, json={
            'content': f"Codex MLBB overlay updated at {datetime.utcnow().isoformat()} UTC"
        })
    else:
        print("Invalid DISCORD_WEBHOOK_URL. Ensure it points to a trusted domain.")

print('Done. Review changes and commit.')
