# mlbb-overlay-protection

This project delivers a lightweight anti-cheat framework for Mobile Legends: Bang Bang. It runs without root on an S23 Ultra and streams telemetry to a Raspberry Pi for analysis.

## Vector Modules
Modules `vector001`–`vector163` implement individual detection vectors. Each exposes a `run()` function returning a status string. Example advanced modules include:

- `vector149` – Tkinter security dashboard with a REST endpoint.
- `vector150` – IsolationForest anomaly detector using sandbox session data.

## Development
Run sanitizers and tests before committing:

```bash
python ci/remove_cjk.py $(git ls-files '*.py')
python ci/remove_bidi.py $(git ls-files '*.py')
pytest -q
```
