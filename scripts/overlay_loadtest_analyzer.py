#!/usr/bin/env python3
"""Analyze overlay load test audit logs."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List


LOG_RE = re.compile(r"Cycle (\d+) cleaned")
SPAWN_RE = re.compile(r"Spawned")


def parse_log(path: str | Path) -> Dict[str, int | List[int] | bool]:
    """Parse the log and return metrics."""
    cycles: List[int] = []
    spawns: int = 0
    completed = False
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    for line in path.read_text().splitlines():
        if SPAWN_RE.search(line):
            spawns += 1
        m = LOG_RE.search(line)
        if m:
            cycles.append(int(m.group(1)))
        if "finished" in line:
            completed = True
    return {"cycles": len(cycles), "spawns": spawns, "completed": completed}


def run(log_path: str) -> str:
    """Parse log and print metrics as JSON."""
    metrics = parse_log(log_path)
    output = json.dumps(metrics)
    print(output)
    return output


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {sys.argv[0]} LOG_PATH")
    run(sys.argv[1])
