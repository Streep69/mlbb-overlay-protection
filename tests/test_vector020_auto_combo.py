from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector020_auto_combo as v020


def test_auto_combo_exec():
    executed = v020.AutoComboAgent().run([1, 2])
    assert executed == [1, 2]
