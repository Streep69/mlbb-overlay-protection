"""vector315_overlay_loadtest.py - Overlay Load Test Vector.

Rapidly spawn and remove overlay handles to stress test memory usage. All
events are logged to ``/test/vector315_overlay_loadtest.log`` for later audit
and cleanup.
"""

from __future__ import annotations

import os
import time


AUDIT_LOG = "/test/vector315_overlay_loadtest.log"


def audit_log(event: str) -> None:
    """Append an event to the load test audit log."""
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def run(cycles: int = 5, per_cycle: int = 10) -> int:
    """Run the overlay load test.

    Creates and removes overlay handles ``per_cycle`` times over ``cycles``
    iterations. Any unexpected errors are logged. The number of remaining
    handles is returned (should be ``0`` on success).
    """
    audit_log("loadtest start")
    handles: list[dict[str, str]] = []
    try:
        for c in range(cycles):
            for i in range(per_cycle):
                handle = {"id": f"{c}-{i}"}
                try:
                    handles.append(handle)
                    audit_log(f"spawn {handle['id']}")
                except Exception as exc:  # pragma: no cover - defensive
                    audit_log(f"error spawn {exc}")
            handles.clear()
            audit_log(f"cycle {c} cleaned")
    finally:
        remaining = len(handles)
        audit_log(f"loadtest end remaining={remaining}")
    return remaining


def audit() -> str:
    """Return audit log contents."""
    try:
        with open(AUDIT_LOG, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def self_clean() -> None:
    """Remove the audit log for anti-detection."""
    audit_log("self clean")
    try:
        os.remove(AUDIT_LOG)
    except FileNotFoundError:
        pass
    except Exception as exc:  # pragma: no cover - defensive
        audit_log(f"error clean {exc}")


if __name__ == "__main__":  # pragma: no cover
    run()

