"""Vector module 152: overlay intelligence utilities."""
from __future__ import annotations

import logging
import math
from typing import Iterable

LOGGER = logging.getLogger(__name__)


def detect_overlay_shift(prev: Iterable[tuple[int, int]],
                         new: Iterable[tuple[int, int]],
                         tolerance: int = 5) -> bool:
    """Return ``True`` if overlay positions moved beyond *tolerance*.

    Parameters
    ----------
    prev:
        Previous overlay coordinates.
    new:
        New overlay coordinates.
    tolerance:
        Acceptable movement in pixels before reporting a shift.

    Returns
    -------
    bool
        ``True`` when a significant shift is detected.
    """
    prev_list = list(prev)
    new_list = list(new)
    if len(prev_list) != len(new_list):
        LOGGER.warning("Coordinate length mismatch: %s vs %s",
                       len(prev_list), len(new_list))
        return True
    for (x1, y1), (x2, y2) in zip(prev_list, new_list):
        dist = math.hypot(x1 - x2, y1 - y2)
        LOGGER.debug("Delta %.2f for (%s,%s)->(%s,%s)", dist, x1, y1, x2, y2)
        if dist > tolerance:
            return True
    return False


def run() -> str:
    """Demonstrate overlay shift detection."""
    sample_prev = [(0, 0), (10, 10)]
    sample_new = [(1, 1), (20, 20)]
    shifted = detect_overlay_shift(sample_prev, sample_new)
    LOGGER.info("Overlay shifted: %s", shifted)
    return 'vector152 executed'


if __name__ == '__main__':  # pragma: no cover - manual execution
    print(run())
