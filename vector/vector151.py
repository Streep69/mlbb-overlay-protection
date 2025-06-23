"""Vector module 151: overlay entropy manager."""
from __future__ import annotations
import logging
import random
import time

LOGGER = logging.getLogger(__name__)


def randomize_overlay_positions(count: int = 10,
                                width: int = 1080,
                                height: int = 2400) -> list[tuple[int, int]]:
    """Generate random overlay coordinates.

    Parameters
    ----------
    count:
        Number of positions to generate.
    width:
        Maximum screen width.
    height:
        Maximum screen height.
    Returns
    -------
    list[tuple[int, int]]
        Random ``(x, y)`` coordinate pairs.
    """
    positions: list[tuple[int, int]] = []
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        positions.append((x, y))
        LOGGER.debug("Generated overlay position (%s, %s)", x, y)
        time.sleep(0.01)
    return positions


def run() -> str:
    """Run the entropy manager."""
    randomize_overlay_positions()
    return 'vector151 executed'
