"""vector319_tapbot_gesture.py - Tapbot Gesture Vector

Purpose: Simulate human-like tap and swipe gestures with randomized timing.
Anti-detection: variable delays and path noise, full audit logging.
"""

from __future__ import annotations

import os
import random
import time
from typing import List, Dict, Tuple

AUDIT_LOG = "/test/tapbot_gesture_audit.log"


def audit_log(event: str) -> None:
    """Append an event to the tapbot gesture audit log."""
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class DummyInputAPI:
    """Fallback input API for tests."""

    def tap(self, x: int, y: int) -> None:
        del x, y

    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration: float) -> None:
        del x1, y1, x2, y2, duration


class TapbotGestureVector:
    """Send taps and swipes with human-like timing."""

    def __init__(self, input_api: DummyInputAPI | None = None) -> None:
        self.input_api = input_api or DummyInputAPI()

    def tap(self, x: int, y: int) -> None:
        self.input_api.tap(x, y)
        audit_log(f"tap {x},{y}")

    def swipe(self, start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.2) -> None:
        self.input_api.swipe(start[0], start[1], end[0], end[1], duration)
        audit_log(f"swipe {start}->{end} dur={duration:.2f}")

    def run(self, actions: List[Dict] | None = None) -> None:
        audit_log("TapbotGesture start")
        if actions is None:
            actions = [
                {"type": "tap", "pos": (500, 1400)},
                {"type": "swipe", "start": (400, 1400), "end": (600, 1200), "duration": 0.3},
            ]
        for act in actions:
            if act["type"] == "tap":
                self.tap(*act["pos"])
            elif act["type"] == "swipe":
                self.swipe(act["start"], act["end"], act.get("duration", 0.2))
            time.sleep(random.uniform(0.1, 0.25))
        audit_log("TapbotGesture end")


if __name__ == "__main__":  # pragma: no cover
    TapbotGestureVector().run()
