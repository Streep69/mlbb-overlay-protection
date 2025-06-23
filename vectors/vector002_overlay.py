"""vector002_overlay.py - Overlay manager agent.

Manages showing and hiding the ESP overlay and records basic frame
render events for auditing. Audit logs are written to ``/test/vector002_overlay.log``.
"""

from __future__ import annotations

import os
import time
from typing import Iterable


AUDIT_LOG = "/test/vector002_overlay.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class DummyOverlayAPI:
    def show(self) -> None: pass
    def hide(self) -> None: pass
    def render_frame(self, frame: object) -> None: pass


class OverlayManagerAgent:
    """Control overlay visibility and frame rendering."""

    def __init__(self, overlay_api: DummyOverlayAPI | None = None) -> None:
        self.overlay_api = overlay_api or DummyOverlayAPI()
        self.visible = False

    def show_overlay(self) -> None:
        self.overlay_api.show()
        self.visible = True
        audit_log("overlay shown")

    def hide_overlay(self) -> None:
        self.overlay_api.hide()
        self.visible = False
        audit_log("overlay hidden")

    def update(self, frame: object) -> None:
        self.overlay_api.render_frame(frame)
        audit_log("frame rendered")

    def run(self, frame_stream: Iterable[object] | None = None) -> None:
        audit_log("manager start")
        if frame_stream is None:
            frame_stream = [None] * 5
        self.show_overlay()
        try:
            for frame in frame_stream:
                self.update(frame)
                time.sleep(0.1)
        finally:
            self.hide_overlay()
            audit_log("manager stop")


def run() -> None:
    OverlayManagerAgent().run()


if __name__ == "__main__":  # pragma: no cover
    run()
