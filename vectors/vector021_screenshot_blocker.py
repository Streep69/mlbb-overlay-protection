"""vector021_screenshot_blocker.py - Screenshot Blocker Agent

Purpose: Monitor screenshot events and hide the overlay while a screenshot is
captured. This helps reduce detection risk. Events and actions are logged.
"""

from __future__ import annotations

import os
import time
from typing import Iterable

AUDIT_LOG = "/test/vector021_screenshot_blocker.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class DummyOverlayAPI:
    def hide(self) -> None: pass
    def show(self) -> None: pass


class ScreenshotBlockerAgent:
    def __init__(self, overlay_api: DummyOverlayAPI | None = None) -> None:
        self.overlay_api = overlay_api or DummyOverlayAPI()

    def run(self, events: Iterable[str] | None = None) -> int:
        audit_log("blocker start")
        if events is None:
            events = ["screenshot"]
        count = 0
        for event in events:
            if event == "screenshot":
                self.overlay_api.hide()
                audit_log("overlay hidden")
                time.sleep(0.5)
                self.overlay_api.show()
                audit_log("overlay restored")
                count += 1
        audit_log("blocker end")
        return count


def run() -> int:
    return ScreenshotBlockerAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
