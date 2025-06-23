from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector004_tapbot as v004

def test_tapbot_run():
    v004.TapBotAgent().run(reps=1)
