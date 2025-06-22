"""vector315_overlay_loadtest.py - Overlay Load Test Vector
Purpose: Rapidly spawn and remove overlay handles to stress test memory usage.
"""

import os
import time
from typing import List, Dict

DEFAULT_LOG_PATH = "/test/overlay_loadtest_audit.log"


def get_log_path() -> str:
    """Return the current path for the audit log."""
    return os.getenv("LOADTEST_LOG_PATH", DEFAULT_LOG_PATH)


def audit_log(event: str, log_path: str) -> None:
    """Append event to the load test audit log."""
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class OverlayLoadTestVector:
    """Stress test overlay handle creation and cleanup."""

    def __init__(self, log_path: str) -> None:
        self.handles: List[Dict[str, str]] = []
        self.log_path = log_path

    def spawn_handle(self, handle_id: str) -> None:
        handle = {"id": handle_id}
        self.handles.append(handle)
        audit_log(f"Spawned {handle}", self.log_path)

    def cleanup_cycle(self, cycle: int) -> None:
        self.handles.clear()
        audit_log(f"Cycle {cycle} cleaned", self.log_path)

    def run(self, cycles: int = 5, per_cycle: int = 10) -> int:
        audit_log("OverlayLoadTestVector started", self.log_path)
        for c in range(cycles):
            for i in range(per_cycle):
                self.spawn_handle(f"{c}-{i}")
            self.cleanup_cycle(c)
            time.sleep(0.01)
        audit_log("OverlayLoadTestVector finished", self.log_path)
        return len(self.handles)

    def self_clean(self) -> None:
        if os.path.exists(self.log_path):
            os.remove(self.log_path)


def run(cycles: int = 5, per_cycle: int = 10) -> int:
    """Convenience wrapper to run the vector."""
    path = get_log_path()
    vector = OverlayLoadTestVector(path)
    remaining = vector.run(cycles=cycles, per_cycle=per_cycle)
    vector.self_clean()
    return remaining
