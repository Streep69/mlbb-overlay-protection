from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vector import vector315_overlay_loadtest as v315


def test_run_load_test():
    elapsed = v315.run_load_test(iterations=5, delay=0)
    assert elapsed >= 0


def test_run_wrapper():
    assert v315.run() == "vector315 executed"
