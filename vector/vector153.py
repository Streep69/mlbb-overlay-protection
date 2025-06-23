"""Vector module 153: tap automation utilities."""
from __future__ import annotations

import logging
import random
import time
from typing import Iterable

LOGGER = logging.getLogger(__name__)


def generate_tap_sequence(base: Iterable[tuple[int, int]], jitter: int = 2) -> list[tuple[int, int]]:
    """Return tap coordinates with random jitter."""
    seq: list[tuple[int, int]] = []
    for x, y in base:
        jx = x + random.randint(-jitter, jitter)
        jy = y + random.randint(-jitter, jitter)
        seq.append((jx, jy))
        LOGGER.debug("Generated tap at (%s, %s)", jx, jy)
    return seq


def simulate_taps(seq: Iterable[tuple[int, int]], delay: float = 0.05) -> None:
    """Log simulated tap events."""
    for x, y in seq:
        LOGGER.info("Tap at (%s, %s)", x, y)
        time.sleep(delay)


def run() -> str:
    """Generate and run tap sequence."""
    base = [(100, 200), (150, 250), (200, 300)]
    seq = generate_tap_sequence(base)
    simulate_taps(seq, delay=0)
    return 'vector153 executed'


if __name__ == '__main__':  # pragma: no cover - manual execution
    print(run())
