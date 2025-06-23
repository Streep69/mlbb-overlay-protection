"""vector080_overlay_spoofer.py - Overlay Spoofer

Purpose: Change overlay window identifiers to mimic benign apps and reduce
detection. Logs each spoofed handle.
"""

from __future__ import annotations

import os
import random
import string
import time
from typing import Optional

AUDIT_LOG = "/test/vector080_overlay_spoofer.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def _random_handle() -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


class DummyOverlayAPI:
    def rename_handle(self, name: str) -> None:
        del name


class OverlaySpooferAgent:
    def __init__(self, overlay_api: DummyOverlayAPI | None = None) -> None:
        self.overlay_api = overlay_api or DummyOverlayAPI()

    def run(self, name: Optional[str] = None) -> str:
        audit_log("spoofer start")
        if name is None:
            name = _random_handle()
        self.overlay_api.rename_handle(name)
        audit_log(f"handle {name}")
        audit_log("spoofer end")
        return name


def run(name: Optional[str] = None) -> str:
    return OverlaySpooferAgent().run(name)


if __name__ == "__main__":  # pragma: no cover
    run()
