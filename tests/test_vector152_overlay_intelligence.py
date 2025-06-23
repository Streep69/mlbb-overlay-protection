from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from vector import vector152


def test_detect_overlay_shift():
    prev = [(0, 0), (5, 5)]
    new = [(3, 3), (5, 5)]
    assert vector152.detect_overlay_shift(prev, new, tolerance=2)
    assert not vector152.detect_overlay_shift(prev, prev, tolerance=2)
