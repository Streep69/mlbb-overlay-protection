# AGENTS.md - Akademie Modular Systems

This document lists the primary automation agents used in the project.

| Agent                | Module File                  | Responsibility                               | Inputs        | Outputs       |
|----------------------|------------------------------|----------------------------------------------|---------------|---------------|
| MaphackAgent         | `vectors/vector001_maphack.py` | Reveal enemy positions and draw ESP boxes   | Frame stream  | Overlay rects |
| OverlayManagerAgent  | `vectors/vector002_overlay.py` | Manage overlay visibility and frame updates | Frame stream  | Rendered UI   |
| TapBotAgent          | `vectors/vector004_tapbot.py`  | Send randomized tap commands                | None          | Touch events  |
| EntropyAgent         | `vectors/vector005_entropy.py` | Rotate random seeds for other modules       | None          | New entropy   |
| AntiBanOverlayAgent  | `vectors/vector010_antiban_overlay.py` | Hide overlay on screenshot events         | Events        | Clean state   |
| LoadTestAgent        | `vector315_overlay_loadtest.py`        | Overlay stress/load cycles                | cycles config | Remaining handles |
| SessionObfuscatorAgent | `vector316_session_obfuscator.py` | Randomize session IDs and overlay names | None | New session ID |
