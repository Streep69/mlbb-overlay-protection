from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector319_tapbot_gesture as v319


class Dummy(v319.DummyInputAPI):
    def __init__(self):
        self.taps = []
        self.swipes = []

    def tap(self, x: int, y: int) -> None:
        super().tap(x, y)
        self.taps.append((x, y))

    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration: float) -> None:
        super().swipe(x1, y1, x2, y2, duration)
        self.swipes.append(((x1, y1), (x2, y2)))


def test_tapbot_gesture():
    api = Dummy()
    bot = v319.TapbotGestureVector(api)
    bot.run(actions=[{"type": "tap", "pos": (1, 2)}])
    assert api.taps == [(1, 2)]
