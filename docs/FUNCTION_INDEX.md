# FUNCTION_INDEX.md

## Purpose
Every function in all vectors/scripts, indexed for Codex/LLM context and AI onboarding.

## Example:
- run(): Main entry for all vectors
- self_clean(): Removes all logs/artifacts for anti-ban
- audit(): Records key steps and hashes
- overlay(): Draws overlay/ESP for MLBB
- rotate_entropy(): Randomizes overlay session state
- inject_module(): Loads cheats into memory
- handle_screenshot(): Hides overlay on screenshot
- relay_command(): Relays tapbot/overlay commands to device
- overlay_loadtest(): Stress test overlay spawn and cleanup cycles

## Akademie Modules
- `vector001_maphack.py` - `MaphackAgent.run(frames)` detects bright pixels and draws ESP boxes. Includes `audit()` and `self_clean()`.
- `vector002_overlay.py` - `OverlayManagerAgent.run(frame_stream)` renders frames with entropy-driven delays. Provides `audit()` and `self_clean()`.
- `vector004_tapbot.py` - `TapBotAgent.run(reps, path)` sends jittered tap events. Provides `audit()` and `self_clean()`.
- `vector005_entropy.py` - `EntropyAgent.run(cycles)` rotates seeds and returns entropy delays. Provides `audit()` and `self_clean()`.
- `vector010_antiban_overlay.py` - `AntiBanOverlayAgent.run(event_stream)` hides overlays and cleans logs. Includes `audit()` and `self_clean()`.
- `vector315_overlay_loadtest.py` - `run(cycles, per_cycle)` spawns and cleans overlay handles for stress testing. Includes `audit()` and `self_clean()`.
