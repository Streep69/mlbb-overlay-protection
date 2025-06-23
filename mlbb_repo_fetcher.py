#!/usr/bin/env python3
"""
mlbb_repo_fetcher.py

Search GitHub for Mobile Legends: Bang Bang repositories using the GH_PAT secret,
update mlbb_repos.json, and scaffold integration stubs under vector/integrations/.
"""

import os
import json
from pathlib import Path

from github import Github, BadCredentialsException

# 1. Read and validate the GitHub PAT from environment (injected by Codex Web)
GH_PAT = os.getenv("GH_PAT")
if not GH_PAT:
    raise RuntimeError("GH_PAT environment variable is not set")

try:
    gh = Github(GH_PAT)
    # Simple call to verify credentials
    gh.get_user().login
except BadCredentialsException:
    raise RuntimeError("Invalid GH_PAT provided")

# 2. Define search parameters
QUERY = "mobile legends in:name,description stars:>50"

# 3. Load or initialize the index file
INDEX_PATH = Path("mlbb_repos.json")
if INDEX_PATH.exists():
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        existing = { entry["full_name"]: entry for entry in json.load(f) }
else:
    existing = {}

# 4. Search GitHub and update index
new_count = 0
for repo in gh.search_repositories(query=QUERY, sort="stars", order="desc"):
    name = repo.full_name
    if name not in existing:
        existing[name] = {
            "full_name": name,
            "url": repo.html_url,
            "description": repo.description or "",
            "stars": repo.stargazers_count,
            "language": repo.language or ""
        }
        new_count += 1

# 5. Write back updated mlbb_repos.json
with INDEX_PATH.open("w", encoding="utf-8") as f:
    json.dump(list(existing.values()), f, indent=2)

print(f"Index updated: {new_count} new repositories added")

# 6. Scaffold integration stubs
STUB_DIR = Path("vector/integrations")
STUB_DIR.mkdir(parents=True, exist_ok=True)

for full_name in existing:
    module_name = full_name.replace("/", "_")
    stub_file = STUB_DIR / f"{module_name}_integration.py"
    if not stub_file.exists():
        stub_file.write_text(
            f'''"""
Integration stub for {full_name}
"""

def setup():
    """
    Prepare integration for {full_name}.
    """
    pass

def integrate(config):
    """
    Execute integration logic with the provided configuration.
    """
    pass
''',
            encoding="utf-8"
        )
        print(f"Created stub: {stub_file}")
