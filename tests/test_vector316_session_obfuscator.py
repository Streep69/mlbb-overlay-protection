from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector316_session_obfuscator as v316


def test_session_obfuscator_run():
    session_id = v316.SessionObfuscatorVector().run()
    assert isinstance(session_id, str) and len(session_id) == 16
