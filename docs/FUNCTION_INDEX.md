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
- `vector003_esp.py` – `ESPAgent.run(frame_stream)` detects entities and draws boxes.
- `vector020_auto_combo.py` – `AutoComboAgent.run(combo)` executes skill combos.
- `vector021_screenshot_blocker.py` – `ScreenshotBlockerAgent.run(events)` hides overlay during screenshots.
- `vector030_injector.py` – `InjectorAgent.run(modules)` dynamically imports modules.
- `vector040_log_cleaner.py` – `LogCleanerAgent.run(directory)` wipes audit logs.
- `vector050_obfuscator.py` – `ObfuscatorAgent.run(paths)` renames files for stealth.
- `vector060_api_proxy.py` – `APIProxyAgent.run(requests)` proxies API calls.
- `vector070_entropy_rotator.py` – `EntropyRotatorAgent.run(cycles)` rotates seeds.
- `vector080_overlay_spoofer.py` – `OverlaySpooferAgent.run(name)` spoof overlay handle.
- `vector090_session_spoofer.py` – `SessionSpooferAgent.run()` returns a fake session ID.
- `vector005_entropy.py` – `EntropyAgent.run(cycles)` rotates random seeds for modules.
- `vector010_antiban_overlay.py` – `AntiBanOverlayAgent.run(event_stream)` hides overlay on screenshots.
- `vector315_overlay_loadtest.py` – `LoadTestAgent.run(cycles, per_cycle)` stress tests overlay spawning.
- `vector316_session_obfuscator.py` – `SessionObfuscatorAgent.run()` rotates overlay handles and session IDs.
- `vector317_overlay_intelligence.py` – `OverlayIntelVector.run(iterations)` collects overlay FPS and memory metrics.
- `vector318_entropy_manager.py` – `EntropyManagerVector.run(cycles)` rotates global seeds.
- `vector319_tapbot_gesture.py` – `TapbotGestureVector.run(actions)` performs taps and swipes.
- `vector320_map_intelligence.py` – `MapIntelligenceVector.run(frame_stream, iterations)` builds enemy heatmap.
- `vector055.py` – `run(events)` scans event sequences for trigger flags and logs matches.
- `mlbb_repo_fetcher.py` – `categorize_repo(name, description, language)` assigns MLBB repositories to categories for integration.
- `mlbb_repo_fetcher.py` – `run()` fetches repository info and scaffolds integration stubs.
