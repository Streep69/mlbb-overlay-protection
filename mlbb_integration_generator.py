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
    import socket
    
    def is_valid_url(url):
        try:
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ["http", "https"]:
                return False
            if not parsed_url.netloc:
                return False
            if not (parsed_url.netloc == "discord.com" or parsed_url.netloc.endswith(".discord.com")):
                return False
            # Resolve hostname to IP and check if it's public
            ip = socket.gethostbyname(parsed_url.hostname)
            private_ranges = [
                ("10.0.0.0", "10.255.255.255"),
                ("172.16.0.0", "172.31.255.255"),
                ("192.168.0.0", "192.168.255.255"),
                ("127.0.0.0", "127.255.255.255"),
                ("169.254.0.0", "169.254.255.255"),
                ("::1", "::1"),  # IPv6 localhost
                ("fc00::", "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"),  # IPv6 private
            ]
            ip_addr = socket.inet_aton(ip)
            for start, end in private_ranges:
                if socket.inet_aton(start) <= ip_addr <= socket.inet_aton(end):
                    return False
            return True
        except Exception:
            return False
    
    if is_valid_url(DISCORD_WEBHOOK_URL):
        requests.post(DISCORD_WEBHOOK_URL, json={
            'content': f"Codex MLBB overlay updated at {datetime.utcnow().isoformat()} UTC"
        })
    else:
        print("Invalid DISCORD_WEBHOOK_URL. Ensure it points to a trusted domain and resolves to a public IP.")

print('Done. Review changes and commit.')
