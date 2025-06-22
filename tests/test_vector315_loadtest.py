import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector315_overlay_loadtest as v315  # noqa: E402


def test_overlay_loadtest_cleanup(tmp_path):
    log_path = tmp_path / "overlay.log"
    os.environ["LOADTEST_LOG_PATH"] = str(log_path)
    remaining = v315.run(cycles=2, per_cycle=3)
    assert remaining == 0
    assert not log_path.exists()
    os.environ.pop("LOADTEST_LOG_PATH")
