# AGENTS.md - Akademie Modular Systems

This document lists the primary automation agents used in the project.

| Agent                | Module File                  | Responsibility                               | Inputs        | Outputs       |
|----------------------|------------------------------|----------------------------------------------|---------------|---------------|
| MaphackAgent         | `vectors/vector001_maphack.py` | Reveal enemy positions and draw ESP boxes   | Frame stream  | Overlay rects |
| OverlayManagerAgent  | `vectors/vector002_overlay.py` | Manage overlay visibility and frame updates | Frame stream  | Rendered UI   |
| TapBotAgent          | `vectors/vector004_tapbot.py`  | Send randomized tap commands                | None          | Touch events  |
| ESPAgent             | `vectors/vector003_esp.py`     | Draw entity boxes on overlay                | Frame stream  | Box count     |
| AutoComboAgent       | `vectors/vector020_auto_combo.py` | Execute skill combos                       | Combo list    | Skill log     |
| ScreenshotBlockerAgent | `vectors/vector021_screenshot_blocker.py` | Hide overlay during screenshots | Events        | Blocks        |
| InjectorAgent        | `vectors/vector030_injector.py` | Dynamically load modules                    | Module list   | Loaded count  |
| LogCleanerAgent      | `vectors/vector040_log_cleaner.py` | Remove overlay/audit logs                 | Directory     | Files cleaned |
| ObfuscatorAgent      | `vectors/vector050_obfuscator.py` | Rename files for stealth                   | File list     | New paths     |
| APIProxyAgent        | `vectors/vector060_api_proxy.py` | Proxy and log API calls                    | Requests      | Responses     |
| EntropyRotatorAgent  | `vectors/vector070_entropy_rotator.py` | Rotate overlay seeds                      | None          | Seed list     |
| RepoFetcherAgent | `vector322_repo_fetcher.py` | Update `mlbb_repos.json` from GitHub | None | Repo index |
| OverlaySpooferAgent  | `vectorvector080_overlay_spoofer.py` | Spoof overlay window names                | Name opt      | New name      |
| SessionSpooferAgent  | `vectors/vector090_session_spoofer.py` | Generate fake session IDs                 | None          | Session ID    |
| EntropyAgent         | `vectors/vector005_entropy.py` | Rotate random seeds for other modules       | None          | New entropy   |
| AntiBanOverlayAgent  | `vectors/vector010_antiban_overlay.py` | Hide overlay on screenshot events         | Events        | Clean state   |
| EventTriggerAgent | `vector/vector055.py` | Detect in-game trigger events | Event list | Matched events |
| LoadTestAgent        | `vector315_overlay_loadtest.py`        | Overlay stress/load cycles                | cycles config | Remaining handles |
| SessionObfuscatorAgent | `vector316_session_obfuscator.py` | Randomize session IDs and overlay names | None | New session ID |
| qzvjrp-codex/develop-and-document-modular-agents-for-akademie-system
| LoadTestAgent        | `vector315_overlay_loadtest.py`        | Overlay stress/load cycles                | cycles config | Remaining handles |
| SessionObfuscatorAgent | `vector316_session_obfuscator.py` | Randomize session IDs and overlay names | None | New session codex/develop-and-document-modular-agents-for-akademie-system
| OverlayIntelAgent | `vector317_overlay_intelligence.py` | Monitor overlay FPS and memory usage | None | Metric list |
| EntropyManagerAgent | `vector318_entropy_manager.py` | Rotate seeds for overlay and tap modules | None | Seed list |
| TapbotGestureAgent | `vector319_tapbot_gesture.py` | Simulate taps and swipes with entropy | Gesture plan | Touch events |
| MapIntelligenceAgent | `vector320_map_intelligence.py` | Build heatmap of enemy sightings | Frame stream | Heatmap data |
| RepoReportAgent | `vector321_repo_report.py` | Summarize repo categories from `mlbb_repos.json` | JSON index | Category counts |
| 2o37x5-codex/develop-and-document-modular-agents-for-akademie-system

