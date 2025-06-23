"""vector004_tapbot.py - Tapbot entropy agent.

Generates human-like tap events with random delays. Audit logs
are stored in ``/test/vector004_tapbot.log``.
"""

from __future__ import annotations

import os
import random
import time
from typing import Iterable, Tuple

AUDIT_LOG = "/test/vector004_tapbot.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class DummyTapAPI:
    def tap(self, x: int, y: int, duration: float = 0.1) -> None:
        del x, y, duration


class TapBotAgent:
    """Generate human-like tap events."""

    def __init__(self, tap_api: DummyTapAPI | None = None) -> None:
        self.tap_api = tap_api or DummyTapAPI()

    def random_point(self) -> Tuple[int, int]:
        """Return a random coordinate within the screen bounds."""
        x = random.randint(300, 900)
        y = random.randint(400, 1500)
        return x, y

    def send_tap(self, x: int | None = None, y: int | None = None) -> None:
        """Perform a single randomized tap."""
        if x is None or y is None:
            x, y = self.random_point()
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        duration = random.uniform(0.08, 0.25)
        try:
            self.tap_api.tap(x + dx, y + dy, duration)
            audit_log(f"tap {x+dx},{y+dy} {duration:.2f}s")
        except Exception as exc:  # pragma: no cover - defensive
            audit_log(f"error {exc}")
        time.sleep(duration)

    def run(self, reps: int = 5, path: Iterable[Tuple[int, int]] | None = None) -> None:
        """Run the tapbot for a number of repetitions."""
        audit_log("tapbot start")
        points = list(path) if path else []
        for i in range(reps):
            if points:
                x, y = points[i % len(points)]
                self.send_tap(x, y)
            else:
                self.send_tap()
            time.sleep(random.uniform(0.1, 0.3))
        audit_log("tapbot stop")

    def audit(self) -> str:
        """Return audit log contents."""
        try:
            with open(AUDIT_LOG, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return ""

    def self_clean(self) -> None:
        """Remove audit log for anti-detection."""
        audit_log("self clean")
        try:
            os.remove(AUDIT_LOG)
        except FileNotFoundError:
            pass
        except Exception as exc:  # pragma: no cover - defensive
            audit_log(f"error {exc}")


def run() -> None:
    TapBotAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
