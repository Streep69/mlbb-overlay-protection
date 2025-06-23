"""vector005_entropy.py - Overlay entropy rotation agent.

Randomizes internal seeds and timings for other modules. Logs are
written to ``/test/vector005_entropy.log``.
"""

from __future__ import annotations

import os
import random
import time
from typing import Iterable

AUDIT_LOG = "/test/vector005_entropy.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class EntropyAgent:
    def rotate_entropy(self) -> int:
        seed = random.getrandbits(32)
        random.seed(seed)
        audit_log(f"seed {seed}")
        time.sleep(0.1)
        return seed

    def run(self, cycles: int = 3) -> None:
        audit_log("entropy start")
        for _ in range(cycles):
            self.rotate_entropy()
        audit_log("entropy end")


def run() -> None:
    EntropyAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
