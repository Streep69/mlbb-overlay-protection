from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector040_log_cleaner as v040


def test_log_cleaner(tmp_path):
    log = tmp_path / "a.log"
    log.write_text("data")
    count = v040.LogCleanerAgent().run(str(tmp_path))
    assert count == 1 and log.read_text() == ""
