"""vector321_repo_report.py - Repository Report Vector

Purpose: Summarize categories from mlbb_repos.json for analysis.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict

AUDIT_LOG = Path("/test/vector321_repo_report.log")


def audit_log(event: str) -> None:
    """Append an event to the audit log."""
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def generate_report(json_path: str | Path = "mlbb_repos.json") -> Dict[str, int]:
    """Return a mapping of category to repository count."""
    index_file = Path(json_path)
    if not index_file.exists():
        audit_log("index not found")
        return {}
    data = json.loads(index_file.read_text(encoding="utf-8"))
    counts: Dict[str, int] = {}
    for entry in data:
        cat = entry.get("category", "uncategorized")
        counts[cat] = counts.get(cat, 0) + 1
    audit_log(json.dumps(counts, ensure_ascii=False))
    return counts


def run(json_path: str | Path = "mlbb_repos.json") -> str:
    """Generate a repo category report."""
    generate_report(json_path)
    return "vector321 executed"


if __name__ == "__main__":  # pragma: no cover
    run()
