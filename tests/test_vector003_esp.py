from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector003_esp as v003


def test_esp_run_count():
    count = v003.ESPAgent().run(frame_stream=[None])
    assert count > 0
