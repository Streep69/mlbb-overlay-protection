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
    def __init__(self, tap_api: DummyTapAPI | None = None) -> None:
        self.tap_api = tap_api or DummyTapAPI()

    def random_point(self) -> Tuple[int, int]:
        x = random.randint(300, 900)
        y = random.randint(400, 1500)
        return x, y

    def send_tap(self) -> None:
        x, y = self.random_point()
        duration = random.uniform(0.08, 0.25)
        self.tap_api.tap(x, y, duration)
        audit_log(f"tap {x},{y} {duration:.2f}s")
        time.sleep(duration)

    def run(self, reps: int = 5) -> None:
        audit_log("tapbot start")
        for _ in range(reps):
            self.send_tap()
            time.sleep(random.uniform(0.1, 0.3))
        audit_log("tapbot stop")


def run() -> None:
    TapBotAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
