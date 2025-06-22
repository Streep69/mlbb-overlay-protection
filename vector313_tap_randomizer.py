
"""
vector313_tap_randomizer.py — Tap Randomizer
Purpose: Randomizes all tap/gesture input for added entropy and anti-detection.
"""
import random, time

def audit_log(event):
    with open("/test/tap_randomizer_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")

class TapRandomizerVector:
    def __init__(self, tap_api):
        self.tap_api = tap_api

    def run(self, reps=12):
        audit_log("TapRandomizer started.")
        for _ in range(reps):
            x = random.randint(200, 1100)
            y = random.randint(350, 1700)
            duration = random.uniform(0.07, 0.25)
            self.tap_api.tap(x, y, duration=duration)
            audit_log(f"Random tap at {x},{y}, {duration:.2f}s")
            time.sleep(random.uniform(0.08, 0.22))
        audit_log("TapRandomizer finished.")
