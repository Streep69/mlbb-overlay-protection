from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from vector import vector154


def test_find_path():
    grid = [
        [0, 0],
        [0, 0],
    ]
    path = vector154.find_path((0, 0), (1, 1), grid)
    assert path[0] == (0, 0)
    assert path[-1] == (1, 1)
