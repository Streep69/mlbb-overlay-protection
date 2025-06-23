"""vector020_auto_combo.py - Auto Combo Agent

Purpose: Execute a pre-defined sequence of skill taps with randomized delays to
mimic human input. Audit logs are stored for review.
"""

from __future__ import annotations

import os
import random
import time
from typing import Iterable, List

AUDIT_LOG = "/test/vector020_auto_combo.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class DummyTapAPI:
    def tap_skill(self, skill: int) -> None:
        del skill


class AutoComboAgent:
    def __init__(self, tap_api: DummyTapAPI | None = None) -> None:
        self.tap_api = tap_api or DummyTapAPI()

    def execute_combo(self, combo: Iterable[int]) -> List[int]:
        executed: List[int] = []
        for skill in combo:
            self.tap_api.tap_skill(skill)
            audit_log(f"skill {skill}")
            executed.append(skill)
            time.sleep(random.uniform(0.08, 0.25))
        return executed

    def run(self, combo: Iterable[int] | None = None) -> List[int]:
        audit_log("combo start")
        if combo is None:
            combo = [1, 2, 3]
        result = self.execute_combo(combo)
        audit_log("combo end")
        return result


def run() -> List[int]:
    return AutoComboAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
