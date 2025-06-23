from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector070_entropy_rotator as v070


def test_entropy_rotator():
    seeds = v070.EntropyRotatorAgent().run(cycles=2)
    assert len(seeds) == 2
