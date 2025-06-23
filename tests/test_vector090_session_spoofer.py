from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector090_session_spoofer as v090


def test_session_spoofer():
    sid = v090.SessionSpooferAgent().run()
    assert isinstance(sid, str) and len(sid) == 16
