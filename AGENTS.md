# AGENTS.md – Modular Overlay Protection Agents

This project’s automation and vector logic are managed by modular agents.

## Core Agents

| Agent Name             | Module/File               | Purpose                       | Input                   | Output         | Dependencies   |
|------------------------|--------------------------|-------------------------------|-------------------------|----------------|---------------|
| OverlayManagerAgent    | vectors/vector002_overlay.py   | Handles ESP/map overlays      | Game state, config      | Rendered UI    | EntropyAgent  |
| MapHackAgent           | vectors/vector001_maphack.py   | Reveals minimap info          | Raw map memory          | Entity list    |               |
| EntropyAgent           | vectors/vector005_entropy.py   | Adds entropy, session random  | Overlay state           | New entropy    | OverlayManager|
| AntiBanAgent           | vectors/vector010_antiban_overlay.py | Hide overlay/screens, log clean | System events         | Clean state    |               |
| EventTriggerAgent      | vector/vector055.py            | Detect in-game trigger events   | Event list              | Matched events |               |
| TapBotAgent            | vectors/vector004_tapbot.py    | Simulates human tap entropy   | Tap command             | Touch event    | EntropyAgent  |
| ESPAgent               | vectors/vector003_esp.py       | Draw entity boxes on overlay  | Frame stream            | Box count      | OverlayManager |
| AutoComboAgent         | vectors/vector020_auto_combo.py | Execute skill combos          | Combo list              | Skill log      | TapBotAgent   |
| ScreenshotBlockerAgent | vectors/vector021_screenshot_blocker.py | Hide overlay during screenshots | Events                  | Blocks         | OverlayManager |
| InjectorAgent          | vectors/vector030_injector.py  | Dynamically load modules      | Module list            | Loaded count   |               |
| LogCleanerAgent        | vectors/vector040_log_cleaner.py | Remove overlay/audit logs     | Directory              | Files cleaned  |               |
| ObfuscatorAgent        | vectors/vector050_obfuscator.py | Rename files for stealth      | File list              | New paths      |               |
| APIProxyAgent          | vectors/vector060_api_proxy.py | Proxy and log API calls       | Requests              | Responses      |               |
| EntropyRotatorAgent    | vectors/vector070_entropy_rotator.py | Rotate overlay seeds        | None                   | Seed list      | EntropyAgent  |
| OverlaySpooferAgent    | vectors/vector080_overlay_spoofer.py | Spoof overlay window names  | Name opt               | New name       | OverlayManager |
| SessionSpooferAgent    | vectors/vector090_session_spoofer.py | Generate fake session IDs   | None                   | Session ID     |               |
| LoadTestAgent         | vector315_overlay_loadtest.py   | Overlay stress/load test cycles | cycles config        | Remaining handles | OverlayManager |
| SessionObfuscatorAgent| vector316_session_obfuscator.py | Randomize session IDs and overlay names | None | New session ID | OverlayManager |
| OverlayIntelAgent     | vector317_overlay_intelligence.py | Monitor overlay FPS and memory usage | None | Metric list    | OverlayManager |
| EntropyManagerAgent   | vector318_entropy_manager.py | Rotate seeds for overlay and tap modules | None | Seed list      |               |
| TapbotGestureAgent    | vector319_tapbot_gesture.py | Simulate taps and swipes with entropy | Gesture plan | Touch events   | EntropyManager |
| MapIntelligenceAgent  | vector320_map_intelligence.py | Build heatmap of enemy sightings | Frame stream | Heatmap data   | OverlayManager |
| RepoReportAgent       | vector321_repo_report.py | Summarize repo categories from `mlbb_repos.json` | JSON index | Category counts | None |

## Extension/Onboarding Instructions

- **All new agents must:**
    - Be listed here with module, I/O, and dependencies.
    - Provide `run()` and (if needed) `self_clean()`, `audit()` functions.
    - Log major actions for auditing and Codex retracing.
    - Register themselves in `/docs/FUNCTION_INDEX.md` and update `/docs/WCTRA_context.md` as needed.

## Example: Creating a New Agent

1. Create `vectors/vectorNNN_newagent.py` with `run()` function and docstring explaining the logic.
2. Add entry to this file, noting module, I/O, dependencies.
3. Update manifest and function index.

## Agent Collaboration

- Agents communicate via shared events or files in `/shared/` or via direct function calls.
- OverlayManagerAgent listens for EntropyAgent state before updating UI.
- AntiBanAgent can pause all other agents during system event triggers.
## Project Overview
Non-root Mobile Legends: Bang Bang overlay cheats for S23 Ultra streamed to Raspberry Pi.

## Directory Structure
- `pi/` – Raspberry Pi support and helpers
- `overlay-app/` – Android overlay app modules (placeholder)
- `termux/` – Termux scripts and utilities
- `ci/` – CI configurations and pipelines
- `tests/` – Unit/integration tests
- `sandbox/` – experimental or scratch scripts
- `docs/` – documentation assets

## Agent Role Instructions
- Generate `vector001`–`vector163` modules when requested
- Sanitize Unicode and auto-fix detectable errors
- Run tests before committing and commit only clean code

## Security Measures
- Use sanitizers in builds and CI to detect memory and thread issues
- Enforce CI checks on every push and pull request
- Implement robust error handling and structured logging

## Testing Standards
- Use `pytest` to test vision, macros, overlay, network, AI, and UI modules

## CI Expectations
- Sanitize and run tests on every push and pull request
- Workflows use a Personal Access Token (`GH_PAT`) with `repo` scope. Checkout uses `persist-credentials: false` and the PAT to push sanitized, tested code back to the protected branch.
- Pull requests labeled `automerge` merge automatically when CI succeeds.
- Before pushing, the workflow checks if the branch is synced with `main`. If merging `main` results in conflicts, the job fails and instructs you to update the branch manually.
- Comment `/rebase` or add the `rebase` label on a pull request to trigger the *auto_rebase* workflow. This rebases the branch onto `main`, removes the label, runs sanitizers and tests, and merges if labeled `automerge`.

## Documentation Updates
- Whenever code changes require docs, update `README.md` and `full_chat_log.md` or create new files for reference 

## Workflow Rules
1. Sanitize changes
2. Run tests
3. Commit clean code with concise messages
4. CI must pass before merge; label pull requests `automerge` to trigger automatic merging

## Coding Conventions
- Follow PEP8 style with type hints
- Use structured logs and docstrings for all modules

## Security Mindset
Treat the project as an adversarial AI/anti-cheat system with RL adaptation. Maintain high standards for security and defensive programming and active testing and emhace development 

## Rebase Automation
- Execute `./auto_rebase_allow.sh` in Termux when the feature branch falls behind
  `main`.
- The script rebases with `--allow-unrelated-histories -X theirs`, replacing
  conflicting files from `main` with those on the branch.

