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
    """Detect enemy coordinates and draw ESP boxes."""

    def __init__(self, overlay_api: DummyOverlayAPI | None = None) -> None:
        self.overlay_api = overlay_api or DummyOverlayAPI()

    def scan(self, frame: object) -> List[Tuple[int, int]]:
        """Scan a frame for bright spots representing enemies."""
        coords: List[Tuple[int, int]] = []
        if isinstance(frame, list):
            for y, row in enumerate(frame):
                for x, pixel in enumerate(row):
                    if isinstance(pixel, int) and pixel > 230:
                        coords.append((x * 10, y * 10))
        if not coords:
            coords = [
                (random.randint(100, 1000), random.randint(200, 1500))
                for _ in range(random.randint(1, 3))
            ]
        audit_log(f"detected {len(coords)} enemies")
        return coords

    def render(self, coords: Iterable[Tuple[int, int]]) -> None:
        """Render ESP rectangles for each detected coordinate."""
        for x, y in coords:
            try:
                self.overlay_api.draw_rect(x, y, color="red", alpha=0.55)
                audit_log(f"draw {x},{y}")
            except Exception as exc:  # pragma: no cover - defensive
                audit_log(f"error {exc}")
            time.sleep(random.uniform(0.05, 0.15))

    def run(self, frames: Iterable[object] | None = None) -> None:
        """Execute the maphack scanning loop."""
        audit_log("start")
        if frames is None:
            frames = [[0] * 10 for _ in range(3)]
        for frame in frames:
            coords = self.scan(frame)
            self.render(coords)
            time.sleep(random.uniform(0.5, 1.0))
        audit_log("stop")

    def audit(self) -> str:
        """Return the current audit log contents."""
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
    """Entry point used by tests."""
    MaphackAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
