#!/usr/bin/env python3
"""Fallback rendering utilities when hardware acceleration fails."""

from __future__ import annotations

import logging

LOGGER = logging.getLogger(__name__)


def run() -> str:
    """Execute the fallback renderer."""
    LOGGER.info("Running render_fallback")
    return "render_fallback executed"


if __name__ == "__main__":  # pragma: no cover - manual execution
    run()

