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
- `vector001_maphack.py` – `MaphackAgent.run(frames)` scans frames and draws ESP boxes.
- `vector002_overlay.py` – `OverlayManagerAgent.run(frame_stream)` shows and updates overlays.
- `vector004_tapbot.py` – `TapBotAgent.run(reps)` sends randomized tap events.
- `vector005_entropy.py` – `EntropyAgent.run(cycles)` rotates random seeds for modules.
- `vector010_antiban_overlay.py` – `AntiBanOverlayAgent.run(event_stream)` hides overlay on screenshots.
