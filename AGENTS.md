# Codex Agents Guidance

## Project Overview
Non-root Mobile Legends: Bang Bang overlay cheats for S23 Ultra streamed to Raspberry Pi.

## Directory Structure
- `pi/` - Raspberry Pi support and helpers
- `overlay-app/` - Android overlay app modules
- `termux/` - Termux scripts and utilities
- `ci/` - CI configurations and pipelines
- `tests/` - Unit/integration tests
- `sandbox/` - experimental or scratch scripts
- `docs/` - documentation assets

## Agent Role Instructions
- Generate `vector001`-`vector163` modules when requested
- Sanitize Unicode and auto-fix detectable errors
- Run tests before committing and commit only clean code

## Security Measures
- Use sanitizers in builds and CI to detect memory and thread issues
- Install system packages with `sudo apt update && sudo apt install -y adb ffmpeg libusb-1.0-0-dev`
- Install Python packages with `pip install -r requirements.txt`
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
- Whenever code changes require docs, update `README.md` and `full_chat_log.md`

## Workflow Rules
1. Sanitize changes
2. Run tests
3. Commit clean code with concise messages
4. CI must pass before merge; label pull requests `automerge` to trigger automatic merging

## Coding Conventions
- Follow PEP8 style with type hints
- Use structured logs and docstrings for all modules

## Security Mindset
Treat the project as an adversarial AI/anti-cheat system with RL adaptation. Maintain high standards for security and defensive programming.

## Rebase Automation
- Execute `./auto_rebase_allow.sh` when the feature branch falls behind `main`.
- The script rebases with `--allow-unrelated-histories -X theirs`, pushes the result, and resolves conflicts in favor of the branch.
