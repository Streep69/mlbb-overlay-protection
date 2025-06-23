from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector002_overlay as v002

def test_overlay_run():
    v002.OverlayManagerAgent().run(frame_stream=[None])
