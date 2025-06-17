# mlbb-overlay-protection

This project provides a non-root overlay cheat framework for Mobile Legends: Bang Bang streamed from an S23 Ultra to a Raspberry Pi.

## Vector Modules
Placeholder modules `vector001`–`vector163` implement individual anti-cheat checks. Each exposes a `run()` function returning a status string.

## REST Server
`pi/rest_server.py` provides a small aiohttp service exposing a `/health` endpoint. The server runs until the provided stop event is triggered.

## Development
Run sanitizers and tests before committing:

```bash
python ci/remove_cjk.py $(git ls-files '*.py')
python ci/remove_bidi.py $(git ls-files '*.py')
pytest -q
```
