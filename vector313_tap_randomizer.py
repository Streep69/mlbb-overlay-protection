
"""
vector313_tap_randomizer.py — Tap Randomizer
Purpose: Randomizes all tap/gesture input for added entropy and anti-detection.
"""
import random, time

def audit_log(event):
    with open("/test/tap_randomizer_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")

class TapRandomizerVector:
    def __init__(self, tap_api) -> None:
        self.tap_api = tap_api

    def run(self, reps: int = 12) -> None:
        audit_log("TapRandomizer started.")
        for _ in range(reps):
            x = random.randint(200, 1100)
            y = random.randint(350, 1700)
            duration = random.uniform(0.07, 0.25)
            self.tap_api.tap(x, y, duration=duration)
            audit_log(f"Random tap at {x},{y}, {duration:.2f}s")
            time.sleep(random.uniform(0.08, 0.22))
        audit_log("TapRandomizer finished.")


class DummyTapAPI:
    def tap(self, x, y, duration=0.1) -> None:
        del x, y, duration


def run() -> None:
    TapRandomizerVector(DummyTapAPI()).run(reps=1)


if __name__ == "__main__":  # pragma: no cover
    run()
