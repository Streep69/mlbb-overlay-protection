"""vector315_overlay_loadtest.py - Overlay Load Test Vector
Purpose: Rapidly spawn and remove overlay handles to stress test memory usage.
"""
import time


def audit_log(event: str) -> None:
    """Append event to the load test audit log."""
    with open("/test/overlay_loadtest_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def run(cycles: int = 5, per_cycle: int = 10) -> int:
    """Run the overlay load test.

    Creates and removes overlay handles per cycle.
    Returns number of remaining handles (expected to be 0).
    """
    handles = []
    for c in range(cycles):
        for i in range(per_cycle):
            handle = {"id": f"{c}-{i}"}
            handles.append(handle)
            audit_log(f"Spawned {handle}")
        handles.clear()
        audit_log(f"Cycle {c} cleaned")
    return len(handles)

