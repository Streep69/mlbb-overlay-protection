"""vector090_session_spoofer.py - Session Spoofer

Purpose: Generate random session identifiers to mask real user sessions. The
new ID is returned and logged.
"""

from __future__ import annotations

import os
import random
import string
import time
from typing import Optional

AUDIT_LOG = "/test/vector090_session_spoofer.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def _random_id(length: int = 16) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class SessionSpooferAgent:
    def run(self, sid: Optional[str] = None) -> str:
        audit_log("session start")
        if sid is None:
            sid = _random_id()
        audit_log(f"session {sid}")
        audit_log("session end")
        return sid


def run() -> str:
    return SessionSpooferAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
