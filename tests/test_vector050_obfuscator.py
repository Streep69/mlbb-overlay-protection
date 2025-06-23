from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector050_obfuscator as v050


def test_obfuscator(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("x")
    new_paths = v050.ObfuscatorAgent().run([str(file)])
    assert len(new_paths) == 1 and not file.exists()
