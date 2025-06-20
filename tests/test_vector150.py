from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vector import vector150


def test_vector150_detect_anomalies():
    assert vector150.detect_anomalies() > 0
