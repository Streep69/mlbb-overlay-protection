from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector080_overlay_spoofer as v080


def test_overlay_spoofer():
    name = v080.OverlaySpooferAgent().run("test")
    assert isinstance(name, str)
