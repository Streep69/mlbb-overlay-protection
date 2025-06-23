"""vector001_maphack.py - Basic map reveal agent.

This module scans incoming frames for enemy locations and draws
ESP boxes on the overlay. Audit logs are written to ``/test/vector001_maphack.log``.
"""

from __future__ import annotations

import os
import random
import time
from typing import Iterable, List, Tuple


AUDIT_LOG = "/test/vector001_maphack.log"


def audit_log(event: str) -> None:
    """Append an audit event to the log file."""
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {event}\n")


class DummyOverlayAPI:
    """Placeholder overlay API used for testing."""

    def draw_rect(self, x: int, y: int, w: int = 32, h: int = 32, *, color: str = "red", alpha: float = 0.6) -> None:
        del x, y, w, h, color, alpha

    def clear(self) -> None:
        pass


class MaphackAgent:
    """Simple maphack overlay manager."""

    def __init__(self, overlay_api: DummyOverlayAPI | None = None) -> None:
        self.overlay_api = overlay_api or DummyOverlayAPI()

    def scan(self, frame: object) -> List[Tuple[int, int]]:
        """Fake enemy coordinate scan using random numbers."""
        coords = [(random.randint(100, 1000), random.randint(200, 1500)) for _ in range(random.randint(1, 4))]
        audit_log(f"detected enemies: {coords}")
        return coords

    def render(self, coords: Iterable[Tuple[int, int]]) -> None:
        """Render rectangles at enemy coordinates."""
        for x, y in coords:
            self.overlay_api.draw_rect(x, y, color="red", alpha=0.55)
            audit_log(f"draw {x},{y}")
            time.sleep(random.uniform(0.05, 0.15))

    def run(self, frames: Iterable[object] | None = None) -> None:
        """Execute the maphack scanning loop."""
        audit_log("start")
        if frames is None:
            frames = [None] * 3
        for frame in frames:
            self.render(self.scan(frame))
            time.sleep(random.uniform(0.5, 1.0))
        audit_log("stop")


def run() -> None:
    """Entry point used by tests."""
    MaphackAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
