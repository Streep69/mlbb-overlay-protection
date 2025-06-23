"""vector010_antiban_overlay.py - Screenshot anti-detection agent.

Hides the overlay whenever a screenshot event is detected and performs
self-clean after use. Audit logs are written to ``/test/vector010_antiban.log``.
"""

from __future__ import annotations

import os
import time
from typing import Iterable

AUDIT_LOG = "/test/vector010_antiban.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class DummyOverlayAPI:
    def hide(self) -> None: pass
    def show(self) -> None: pass


class AntiBanOverlayAgent:
    def __init__(self, overlay_api: DummyOverlayAPI | None = None) -> None:
        self.overlay_api = overlay_api or DummyOverlayAPI()

    def self_clean(self) -> None:
        audit_log("self clean")
        # additional cleanup could be added here

    def handle_event(self, event: str) -> None:
        if event == "screenshot":
            self.overlay_api.hide()
            audit_log("overlay hidden")
            time.sleep(1)
            self.overlay_api.show()
            audit_log("overlay restored")

    def run(self, event_stream: Iterable[str] | None = None) -> None:
        audit_log("antiban start")
        if event_stream is None:
            event_stream = ["screenshot"]
        for event in event_stream:
            self.handle_event(event)
        self.self_clean()
        audit_log("antiban end")


def self_clean() -> None:
    AntiBanOverlayAgent().self_clean()


def run() -> None:
    AntiBanOverlayAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
