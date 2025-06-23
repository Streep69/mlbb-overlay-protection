"""vector070_entropy_rotator.py - Entropy Rotator

Purpose: Generate and apply new random seeds for overlay timing variations.
Audit log entries store each seed value.
"""

from __future__ import annotations

import os
import random
import time
from typing import List

AUDIT_LOG = "/test/vector070_entropy_rotator.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class EntropyRotatorAgent:
    def rotate_once(self) -> int:
        seed = random.getrandbits(32)
        random.seed(seed)
        audit_log(f"seed {seed}")
        time.sleep(random.uniform(0.05, 0.15))
        return seed

    def run(self, cycles: int = 3) -> List[int]:
        audit_log("rotator start")
        seeds = [self.rotate_once() for _ in range(cycles)]
        audit_log("rotator end")
        return seeds


def run(cycles: int = 3) -> List[int]:
    return EntropyRotatorAgent().run(cycles)


if __name__ == "__main__":  # pragma: no cover
    run()
