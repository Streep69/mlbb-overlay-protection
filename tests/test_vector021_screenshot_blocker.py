from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector021_screenshot_blocker as v021


def test_screenshot_blocker():
    count = v021.ScreenshotBlockerAgent().run(["screenshot", "none"])
    assert count == 1
