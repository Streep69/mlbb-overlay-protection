"""Vector module 154: simple map pathfinder."""
from __future__ import annotations

import logging
from collections import deque
from typing import Iterable

LOGGER = logging.getLogger(__name__)


def find_path(start: tuple[int, int], goal: tuple[int, int], grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return a shortest path avoiding cells with value ``1``.

    Parameters
    ----------
    start, goal:
        ``(x, y)`` grid coordinates.
    grid:
        Matrix with ``0`` for free cells and ``1`` for obstacles.

    Returns
    -------
    list[tuple[int, int]]
        Path including start and goal. Empty if unreachable.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    prev: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
    q: deque[tuple[int, int]] = deque([start])
    visited[start[1]][start[0]] = True
    while q:
        x, y = q.popleft()
        if (x, y) == goal:
            break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx] and grid[ny][nx] == 0:
                visited[ny][nx] = True
                prev[(nx, ny)] = (x, y)
                q.append((nx, ny))

    path: list[tuple[int, int]] = []
    cur = goal if visited[goal[1]][goal[0]] else None
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    path.reverse()
    LOGGER.debug("Path: %s", path)
    return path


def run() -> str:
    """Demonstrate map pathfinder."""
    grid = [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    path = find_path((0, 0), (4, 4), grid)
    LOGGER.info("Found path length %s", len(path))
    return 'vector154 executed'


if __name__ == '__main__':  # pragma: no cover - manual execution
    print(run())
