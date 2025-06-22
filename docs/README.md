# /docs/ README

This folder contains:
- All exported chat logs, anti-ban guides, onboarding, architecture docs, vector manifests, and test logs.
- Always chunk and rotate docs after major updates.
- Update this README with any new document types or file structure changes.

## CI/CD & Personal Access Token
Continuous integration uses `${{ secrets.GH_PAT }}` with `persist-credentials: false`.
Workflows sanitize code, run tests, and push back using `ad-m/github-push-action@v0.8.0`.
Ensure `GH_PAT` is stored as a repo secret with `repo` scope before running CI.

### Overlay Load Testing
`vector315_overlay_loadtest.py` stresses overlay handle creation and cleanup.
Logs are written to `/test/overlay_loadtest_audit.log` by default. Override the location with the `LOADTEST_LOG_PATH` environment variable when running tests. Use `scripts/overlay_loadtest_analyzer.py` to parse the audit log and output cycle and spawn counts in JSON format.
