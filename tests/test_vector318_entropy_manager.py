from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector318_entropy_manager as v318


def test_entropy_manager_cycles():
    seeds = v318.EntropyManagerVector().run(cycles=3)
    assert len(seeds) == 3
    assert all(isinstance(s, int) for s in seeds)
