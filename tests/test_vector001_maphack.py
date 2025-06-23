from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector001_maphack as v001

def test_maphack_run():
    v001.MaphackAgent().run(frames=[None])
