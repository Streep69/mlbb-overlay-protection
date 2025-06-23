from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector320_map_intelligence as v320


def test_map_intelligence_heatmap():
    heatmap = v320.MapIntelligenceVector().run(iterations=2)
    assert len(heatmap) > 0
