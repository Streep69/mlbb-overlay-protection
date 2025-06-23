
"""
vector312_overlay_relay.py — Overlay Relay
Purpose: Relays overlay commands/events between Pi (AI) and Android/Termux in a memory-safe way.
Anti-detection: Hides overlay on trigger, logs events, session-aware.
"""
import time

def audit_log(event):
    with open("/test/overlay_relay_audit.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")

class OverlayRelayVector:
    def __init__(self, pi_api, termux_api) -> None:
        self.pi_api = pi_api
        self.termux_api = termux_api

    def run(self) -> None:
        audit_log("OverlayRelay started.")
        while True:
            overlay_cmd = self.pi_api.get_overlay_cmd()
            self.termux_api.send_overlay_cmd(overlay_cmd)
            audit_log(f"Relayed: {overlay_cmd}")
            if overlay_cmd.get("hide", False):
                time.sleep(1)
            else:
                time.sleep(0.2)


class DummyPiAPI:
    def __init__(self) -> None:
        self.count = 0

    def get_overlay_cmd(self):
        self.count += 1
        if self.count > 1:
            raise KeyboardInterrupt
        return {"hide": False}


class DummyTermuxAPI:
    def send_overlay_cmd(self, cmd) -> None:
        del cmd


def run() -> None:
    OverlayRelayVector(DummyPiAPI(), DummyTermuxAPI()).run()


if __name__ == "__main__":  # pragma: no cover
    run()
