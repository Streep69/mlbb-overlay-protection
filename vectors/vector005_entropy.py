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
    """Rotate Python's PRNG seed for entropy."""

    def rotate_entropy(self) -> int:
        """Set a new random seed and log it."""
        seed = random.getrandbits(32)
        random.seed(seed)
        audit_log(f"seed {seed}")
        return seed

    @staticmethod
    def entropy_delay(base: float = 0.1) -> float:
        """Return a randomized delay using a Gaussian distribution."""
        delay = abs(random.gauss(base, base / 2))
        audit_log(f"delay {delay:.3f}s")
        return delay

    def run(self, cycles: int = 3) -> None:
        """Rotate entropy multiple times with delays."""
        audit_log("entropy start")
        for _ in range(cycles):
            try:
                self.rotate_entropy()
                time.sleep(self.entropy_delay())
            except Exception as exc:  # pragma: no cover - defensive
                audit_log(f"error {exc}")
        audit_log("entropy end")

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
    EntropyAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
