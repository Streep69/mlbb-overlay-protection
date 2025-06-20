#!/usr/bin/env python3
"""Utilities to synchronize files to the Raspberry Pi."""

from __future__ import annotations

import logging

LOGGER = logging.getLogger(__name__)


def run() -> str:
    """Synchronize files to the Pi."""
    LOGGER.info("Running sync_to_pi")
    return "sync_to_pi executed"


if __name__ == "__main__":  # pragma: no cover - manual execution
    run()

