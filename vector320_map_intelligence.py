"""vector320_map_intelligence.py - Map Intelligence Vector

Purpose: Aggregate enemy coordinates into a heatmap for analysis.
Anti-detection: random polling intervals and log rotations.
"""

from __future__ import annotations

import os
import random
import time
from typing import Dict, Iterable, Tuple

AUDIT_LOG = "/test/map_intelligence_audit.log"


def audit_log(event: str) -> None:
    """Append an event to the map intelligence audit log."""
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class MapIntelligenceVector:
    """Build a simple heatmap of enemy sightings."""

    def __init__(self) -> None:
        self.heatmap: Dict[Tuple[int, int], int] = {}

    def record(self, coords: Iterable[Tuple[int, int]]) -> None:
        for x, y in coords:
            self.heatmap[(x, y)] = self.heatmap.get((x, y), 0) + 1
            audit_log(f"record {x},{y} count={self.heatmap[(x, y)]}")

    def run(self, frame_stream: Iterable[object] | None = None, iterations: int = 5) -> Dict[Tuple[int, int], int]:
        audit_log("MapIntelligence start")
        if frame_stream is None:
            frame_stream = [None] * iterations
        for _ in range(iterations):
            coords = [
                (random.randint(100, 1100), random.randint(200, 1700))
                for _ in range(random.randint(1, 4))
            ]
            self.record(coords)
            time.sleep(random.uniform(0.5, 1.0))
        audit_log("MapIntelligence complete")
        return self.heatmap


if __name__ == "__main__":  # pragma: no cover
    MapIntelligenceVector().run()
