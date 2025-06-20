#!/usr/bin/env python3
"""Generate integration modules for top Mobile Legends: Bang Bang repositories."""
from __future__ import annotations
import ast
import datetime as _dt
import json
import os
import subprocess
import tempfile
import unicodedata
from pathlib import Path
from typing import List
import urllib.parse
import urllib.request


def run_codex() -> None:
    """Invoke Codex for overlay refactoring if API key is set."""
    if not OPENAI_API_KEY:
        return
    prompt = (
        "Refactor MLBB overlay engine ...\n"
        "1. dynamic zoom overlay for drone map\n"
        "..."
    )
    subprocess.run(
        [
            "codex",
            "--full-auto",
            "--approval-mode",
            "full-auto",
            "--prompt",
            prompt,
        ],
        cwd=REPO_PATH,
        check=False,
    )


def notify_discord(message: str) -> None:
    """Send a message via Discord webhook if configured."""
    if not DISCORD_WEBHOOK_URL:
        return
    import requests

    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": message}, timeout=5)
    except Exception:
        pass

CATEGORY_KEYWORDS = {
    'maphack': ['maphack', 'wallhack'],
    'drone': ['drone', 'droneview'],
    'performance': ['fps', 'performance', 'optimiz'],
    'changer': ['skin', 'changer'],
    'streamer': ['stream', 'obs', 'broadcast'],
}

API_URL = "https://api.github.com/search/repositories"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
REPO_PATH = os.getenv("REPO_PATH", os.getcwd())


def fetch_repositories(token: str | None) -> List[dict]:
    """Fetch repositories by topic."""
    query = urllib.parse.quote("topic:mobile-legends")
    url = f"{API_URL}?q={query}&sort=stars&order=desc&per_page=100"
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    return data.get("items", [])


def is_safe(text: str) -> bool:
    """Return True if text contains only safe ASCII without BIDI or CJK."""
    for ch in text:
        if ord(ch) > 0x7F:
            return False
        if unicodedata.category(ch) == 'Cf':
            return False
        if '\u3000' <= ch <= '\u9FFF':
            return False
    return True


def categorize(name: str, description: str) -> str:
    text = f"{name} {description}".lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return cat
    return 'misc'


def analyze_python(path: Path) -> List[str]:
    symbols: List[str] = []
    for py in path.rglob('*.py'):
        try:
            tree = ast.parse(py.read_text(encoding='utf-8'))
        except Exception:
            continue
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                symbols.append(node.name)
    return symbols


def generate_module(repo: dict, category: str, symbols: List[str]) -> Path:
    mod_dir = Path('vector') / 'integrations' / category
    mod_dir.mkdir(parents=True, exist_ok=True)
    name = repo['name'].replace('-', '_')
    module_path = mod_dir / f"{name}_integration.py"
    sym_list = ', '.join(symbols) if symbols else 'none'
    code = f'''"""Integration for {repo['html_url']}"""
from __future__ import annotations
import subprocess
import tempfile
from pathlib import Path

def setup() -> Path:
    """Clone the repository."""
    temp = Path(tempfile.mkdtemp(prefix='{name}_'))
    subprocess.run(['git', 'clone', '--depth', '1', '{repo['clone_url']}', str(temp)], check=True)
    return temp

def integrate(config):
    """Integrate detected modules.\n\n    Detected symbols: {sym_list}\n    TODO: wire into overlay lifecycle.\n    """
    raise NotImplementedError
'''
    module_path.write_text(code, encoding='utf-8')
    return module_path


def main() -> None:
    token = os.getenv('GITHUB_TOKEN')
    repos = fetch_repositories(token)
    selected = []
    for repo in repos:
        name = repo.get('name', '')
        desc = repo.get('description') or ''
        if not (is_safe(name) and is_safe(desc)):
            continue
        category = categorize(name, desc)
        info = {
            'name': repo['full_name'],
            'stars': repo['stargazers_count'],
            'url': repo['html_url'],
            'category': category,
        }
        selected.append(info)
        if repo['stargazers_count'] >= 10:
            with tempfile.TemporaryDirectory() as td:
                subprocess.run(['git', 'clone', '--depth', '1', repo['clone_url'], td], check=False)
                symbols = analyze_python(Path(td))
            generate_module(repo, category, symbols)
    data = {
        'last_updated': _dt.datetime.utcnow().isoformat() + 'Z',
        'repos': selected,
    }
    Path('mlbb_repos.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
    changelog = Path('CHANGELOG.md')
    date = _dt.date.today().isoformat()
    entry = f"\n## Community Integrations ({date})\n- Version bump\n"
    if changelog.exists():
        changelog.write_text(changelog.read_text(encoding='utf-8') + entry, encoding='utf-8')
    else:
        changelog.write_text(f"# Changelog{entry}", encoding='utf-8')

    run_codex()
    timestamp = _dt.datetime.utcnow().isoformat() + 'Z'
    notify_discord(f"✅ MLBB integrations updated at {timestamp}")


if __name__ == '__main__':
    main()
