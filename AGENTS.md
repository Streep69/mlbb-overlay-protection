# Codex Agents Guidance

## Project Overview
Non-root Mobile Legends: Bang Bang overlay cheats for S23 Ultra streamed to Raspberry Pi.

## Directory Structure
- `pi/` – Raspberry Pi support and helpers
- `overlay-app/` – Android overlay app modules
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
- Workflows use a Personal Access Token (`GH_PAT`) with `repo` scope.
- Checkout is performed with `persist-credentials: false` and pushes back with this PAT.
- Pull requests labeled `automerge` will merge automatically when CI succeeds.

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

