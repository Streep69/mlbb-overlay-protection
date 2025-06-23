"""vector055.py - Event Trigger Detection Vector

Detect in-game events that are marked with a ``trigger`` flag.
This module provides a simple example of scanning an event
sequence for trigger occurrences. Any matched event is logged
for later inspection.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Dict, List, Any


AUDIT_LOG = Path("/test/event_trigger_audit.log")


def audit_log(event: str) -> None:
    """Append an event to the event trigger audit log."""
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as fh:
        fh.write(event + "\n")


def detect_triggers(events: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return a list of events that contain a ``trigger`` flag."""
    matched: List[Dict[str, Any]] = []
    for ev in events:
        if ev.get("trigger"):
            matched.append(ev)
            audit_log(json.dumps(ev, ensure_ascii=False))
    return matched


def run(events: Iterable[Dict[str, Any]] | None = None) -> str:
    """Scan ``events`` for trigger occurrences and log them."""
    if events is None:
        events = []
    detect_triggers(events)
    return "vector055 executed"


if __name__ == "__main__":  # pragma: no cover
    run()
