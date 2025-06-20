#!/usr/bin/env python3
"""Utilities for cleaning temporary files on the Raspberry Pi."""

from __future__ import annotations

import logging

LOGGER = logging.getLogger(__name__)


def run() -> str:
    """Execute the cleaner routine."""
    LOGGER.info("Running cleaner")
    return "cleaner executed"


if __name__ == "__main__":  # pragma: no cover - manual execution
    run()

