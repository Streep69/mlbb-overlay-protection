from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector010_antiban_overlay as v010

def test_antiban_overlay_run():
    v010.AntiBanOverlayAgent().run(event_stream=["screenshot"])
