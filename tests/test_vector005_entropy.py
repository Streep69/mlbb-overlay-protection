from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector005_entropy as v005

def test_entropy_run():
    v005.EntropyAgent().run(cycles=1)
