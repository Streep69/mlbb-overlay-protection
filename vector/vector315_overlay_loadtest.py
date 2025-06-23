"""Vector module 315: overlay load test."""
from __future__ import annotations
import logging
import time

LOGGER = logging.getLogger(__name__)


def run_load_test(iterations: int = 100, delay: float = 0.01) -> float:
    """Simulate overlay updates and measure elapsed time.

    Parameters
    ----------
    iterations:
        Number of overlay updates to simulate. Must be positive.
    delay:
        Seconds to wait between updates.
    Returns
    -------
    float
        Total elapsed time in seconds.
    """
    if iterations <= 0:
        raise ValueError("iterations must be positive")
    if delay < 0:
        raise ValueError("delay must be non-negative")

    start = time.monotonic()
    for i in range(iterations):
        LOGGER.debug("Overlay update %s", i)
        time.sleep(delay)
    elapsed = time.monotonic() - start
    LOGGER.info("Load test finished in %.3f seconds", elapsed)
    return elapsed


def run() -> str:
    """Execute overlay load test."""
    run_load_test()
    return "vector315 executed"
