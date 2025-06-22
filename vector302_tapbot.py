
"""
vector302_tapbot.py — Tapbot Entropy Vector
Purpose: Automate safe tap/click patterns (AFK farm, skill spam).
Anti-detection: Humanized timing, entropy model, auto log-wipe.
"""
import random, time

def audit_log(event):
    with open("/test/tapbot_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")

def entropy_tap():
    return random.gauss(0.18, 0.06)

class TapbotVector:
    def __init__(self, tap_api, manifest="vector_manifest.json"):
        self.name = "vector302_tapbot"
        self.tap_api = tap_api
        self.manifest = manifest

    def run(self, duration=30):
        audit_log("Tapbot started.")
        t0 = time.time()
        while time.time() - t0 < duration:
            x, y = random.randint(300, 900), random.randint(400, 1500)
            self.tap_api.tap(x, y)
            audit_log(f"Tap at {x},{y}")
            time.sleep(abs(entropy_tap()))
        audit_log("Tapbot finished.")
