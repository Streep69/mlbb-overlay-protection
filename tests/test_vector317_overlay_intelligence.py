from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector317_overlay_intelligence as v317


def test_overlay_intel_metrics():
    metrics = v317.OverlayIntelVector().run(iterations=2)
    assert len(metrics) == 2
    for m in metrics:
        assert 'fps' in m and 'memory' in m
