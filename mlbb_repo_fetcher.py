#!/usr/bin/env python3
"""
mlbb_repo_fetcher.py

Search GitHub for Mobile Legends: Bang Bang repositories using the GH_PAT secret,
update mlbb_repos.json, and scaffold integration stubs under vector/integrations/.
"""

import os
import json
from pathlib import Path

from github import Github, BadCredentialsException, GithubException


def categorize_repo(name: str, description: str = "", language: str | None = None) -> str:
    """Return a simple category based on repo metadata."""
    text = f"{name} {description} {language or ''}".lower()
    if any(k in text for k in ("maphack", "esp")):
        return "maphack"
    if "drone" in text:
        return "drone"
    if any(k in text for k in ("unlocker", "fps")):
        return "performance"
    if "api" in text:
        return "api"
    if "analytic" in text:
        return "analytics"
    return "misc"

def run() -> None:
    """Fetch MLBB repositories and update integration stubs."""
    # 1. Read and validate the GitHub PAT from environment (injected by Codex Web)
    gh_pat = os.getenv("GH_PAT")
    if not gh_pat:
        raise RuntimeError("GH_PAT environment variable is not set")

    try:
        gh = Github(gh_pat)
        # Simple call to verify credentials
        gh.get_user().login
    except BadCredentialsException:
        raise RuntimeError("Invalid GH_PAT provided")

    # 2. Define search parameters
    query = "mobile legends in:name,description stars:>50"

    # 3. Load or initialize the index file
    index_path = Path("mlbb_repos.json")
    if index_path.exists():
        with index_path.open("r", encoding="utf-8") as f:
            existing = {entry["full_name"]: entry for entry in json.load(f)}
    else:
        existing = {}

    # Ensure all existing entries have a category
    for entry in existing.values():
        if "category" not in entry:
            entry["category"] = categorize_repo(
                entry.get("full_name", ""),
                entry.get("description", ""),
                entry.get("language"),
            )

    # 4. Search GitHub and update index
    new_count = 0
    try:
        repos = gh.search_repositories(query=query, sort="stars", order="desc")
    except GithubException as exc:  # network or auth errors
        print(f"GitHub search failed: {exc}")
        return

    for repo in repos:
        name = repo.full_name
        category = categorize_repo(name, repo.description or "", repo.language)
        entry = {
            "full_name": name,
            "url": repo.html_url,
            "description": repo.description or "",
            "stars": repo.stargazers_count,
            "language": repo.language or "",
            "category": category,
        }
        if name not in existing:
            existing[name] = entry
            new_count += 1
        elif "category" not in existing[name]:
            existing[name]["category"] = category

    # 5. Write back updated mlbb_repos.json
    with index_path.open("w", encoding="utf-8") as f:
        json.dump(list(existing.values()), f, indent=2)

    print(f"Index updated: {new_count} new repositories added")

    # 6. Scaffold integration stubs
    stub_dir = Path("vector/integrations")
    stub_dir.mkdir(parents=True, exist_ok=True)

    for full_name in existing:
        module_name = full_name.replace("/", "_")
        stub_file = stub_dir / f"{module_name}_integration.py"
        if not stub_file.exists():
            stub_file.write_text(
                f'''"""
Integration stub for {full_name}
"""

def setup():
    """Prepare integration for {full_name}."""
    pass

def integrate(config):
    """Execute integration logic with the provided configuration."""
    pass
''',
                encoding="utf-8",
            )
            print(f"Created stub: {stub_file}")


if __name__ == "__main__":  # pragma: no cover - manual execution
    run()
