from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector030_injector as v030


def test_injector_import():
    count = v030.InjectorAgent().run(["json"])
    assert count == 1
