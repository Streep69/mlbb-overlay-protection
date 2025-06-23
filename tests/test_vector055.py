from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vector import vector055


def test_detect_triggers():
    events = [
        {"id": 1, "trigger": True},
        {"id": 2},
        {"id": 3, "trigger": True},
    ]
    matched = vector055.detect_triggers(events)
    assert len(matched) == 2


def test_run_returns_string():
    assert vector055.run([]) == "vector055 executed"

