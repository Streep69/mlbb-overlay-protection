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
| SessionObfuscatorAgent | `vector316_session_obfuscator.py` | Randomize session IDs and overlay names | None | New session codex/develop-and-document-modular-agents-for-akademie-system
| OverlayIntelAgent | `vector317_overlay_intelligence.py` | Monitor overlay FPS and memory usage | None | Metric list |
| EntropyManagerAgent | `vector318_entropy_manager.py` | Rotate seeds for overlay and tap modules | None | Seed list |
| TapbotGestureAgent | `vector319_tapbot_gesture.py` | Simulate taps and swipes with entropy | Gesture plan | Touch events |
| MapIntelligenceAgent | `vector320_map_intelligence.py` | Build heatmap of enemy sightings | Frame stream | Heatmap data |



