
"""
vector304_antiscreenshot.py — Anti-Screenshot Logic
Purpose: Prevent overlays appearing in screenshots.
Anti-detection: Framebuffer swap, Pi relay, log and verify.
"""
import time

def audit_log(event):
    with open("/test/antiscreenshot_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")

class AntiScreenshotVector:
    def __init__(self, overlay_api, manifest="vector_manifest.json"):
        self.name = "vector304_antiscreenshot"
        self.overlay_api = overlay_api
        self.manifest = manifest

    def on_screenshot(self):
        self.overlay_api.hide()
        audit_log("Overlay hidden for screenshot event.")
        time.sleep(0.8)
        self.overlay_api.show()
        audit_log("Overlay restored after screenshot.")

    def run(self, event_stream):
        audit_log("AntiScreenshot running.")
        for event in event_stream:
            if event == "screenshot":
                self.on_screenshot()
