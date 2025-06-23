# AGENTS.md - Akademie Modular Systems

This document lists the primary automation agents used in the project.

| Agent                | Module File                  | Responsibility                               | Inputs        | Outputs       |
|----------------------|------------------------------|----------------------------------------------|---------------|---------------|
| MaphackAgent         | `vectors/vector001_maphack.py` | Detect bright pixels and render ESP boxes   | Frame stream  | Overlay rects |
| OverlayManagerAgent  | `vectors/vector002_overlay.py` | Manage overlay visibility with entropy delays | Frame stream  | Rendered UI   |
| TapBotAgent          | `vectors/vector004_tapbot.py`  | Send jittered tap commands with optional paths | None          | Touch events  |
| EntropyAgent         | `vectors/vector005_entropy.py` | Rotate PRNG seed and provide entropy delays | None          | New entropy   |
| AntiBanOverlayAgent  | `vectors/vector010_antiban_overlay.py` | Hide overlay on screenshot events and clean logs | Events        | Clean state   |
| LoadTestAgent        | `vector315_overlay_loadtest.py`        | Stress test overlay handle lifecycle            | Cycles config | Remaining handles |

All agents record audit logs under `/test/` and offer `audit()` and `self_clean()` helpers for post-session review and cleanup.
