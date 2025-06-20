#!/usr/bin/env python3
"""Simple heartbeat monitor for remote systems."""

from __future__ import annotations

import logging
import time

LOGGER = logging.getLogger(__name__)


def run(iterations: int | None = None, interval: float = 15.0) -> None:
    """Log a heartbeat message at regular intervals.

    Parameters
    ----------
    iterations:
        Number of times to send the heartbeat. ``None`` means infinite.
    interval:
        Seconds to wait between heartbeats.
    """

    count = 0
    while iterations is None or count < iterations:
        LOGGER.info("[heartbeat] alive")
        count += 1
        if iterations is None or count < iterations:
            time.sleep(interval)


if __name__ == "__main__":  # pragma: no cover - manual execution
    run()

