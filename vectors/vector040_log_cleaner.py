"""vector040_log_cleaner.py - Log Cleaner

Purpose: Wipe overlay logs and audit files after sessions. Provides optional
removal of files matching a pattern.
"""

from __future__ import annotations

import glob
import os
import time
from typing import Iterable

AUDIT_LOG = "/test/vector040_log_cleaner.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class LogCleanerAgent:
    def clean(self, directory: str, pattern: str = "*.log") -> int:
        paths = glob.glob(os.path.join(directory, pattern))
        for path in paths:
            try:
                open(path, "w").close()
                audit_log(f"cleaned {path}")
            except Exception as e:  # pragma: no cover - file permission issues
                audit_log(f"error {path} {e}")
        return len(paths)

    def run(self, directory: str = "/test") -> int:
        audit_log("logcleaner start")
        count = self.clean(directory)
        audit_log("logcleaner end")
        return count


def run(directory: str = "/test") -> int:
    return LogCleanerAgent().run(directory)


if __name__ == "__main__":  # pragma: no cover
    run()
