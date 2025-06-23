from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from vector import vector153


def test_generate_tap_sequence():
    base = [(0, 0)]
    seq = vector153.generate_tap_sequence(base, jitter=0)
    assert seq == base
