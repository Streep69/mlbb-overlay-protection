"""vector322_repo_fetcher.py - Repository Fetcher Vector

Purpose: Use the GitHub API to search for MLBB repositories and update
`mlbb_repos.json`. This wraps ``mlbb_repo_fetcher.run`` so the process
can be invoked from other modules or tests.
"""
from __future__ import annotations

import logging
import time
from pathlib import Path

import mlbb_repo_fetcher

AUDIT_LOG = Path("/test/vector322_repo_fetcher.log")
LOGGER = logging.getLogger(__name__)


def audit_log(event: str) -> None:
    """Append an event to the repo fetcher audit log."""
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def run() -> str:
    """Update the repository index using the GitHub API."""
    audit_log("fetch start")
    try:
        mlbb_repo_fetcher.run()
    except Exception as exc:  # pragma: no cover - network failure
        LOGGER.error("fetch failed: %s", exc)
        audit_log(f"error {exc}")
        return "vector322 error"
    audit_log("fetch complete")
    return "vector322 executed"


if __name__ == "__main__":  # pragma: no cover
    run()
