
"""
vector308_session_cleaner.py — Session Cleaner Vector
Purpose: Terminates/cleans all overlays, tapbots, and logs after session end.
Anti-detection: Validates logs wiped, overlays closed.
"""
import time, os

def audit_log(event):
    with open("/test/session_cleaner_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")

class SessionCleanerVector:
    def __init__(self, overlay_api=None, tapbot_api=None, log_paths=None):
        self.overlay_api = overlay_api
        self.tapbot_api = tapbot_api
        if log_paths is None:
            log_paths = [
                "/test/maphack_audit.log", "/test/tapbot_audit.log",
                "/test/drone_audit.log", "/test/autocombo_audit.log"
            ]
        self.log_paths = log_paths

    def clean(self):
        audit_log("SessionCleaner started.")
        if self.overlay_api: self.overlay_api.clear()
        if self.tapbot_api: self.tapbot_api.terminate()
        for path in self.log_paths:
            if os.path.exists(path):
                os.remove(path)
                audit_log(f"Deleted {path}")
        audit_log("SessionCleaner complete.")

    def run(self):
        self.clean()
