from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector315_overlay_loadtest as v315


def test_overlay_loadtest_cleanup():
    os.makedirs('/test', exist_ok=True)
    remaining = v315.run(cycles=2, per_cycle=3)
    assert remaining == 0
