# mlbb-overlay-protection

This project provides a non-root overlay cheat framework for Mobile Legends: Bang Bang streamed from an S23 Ultra to a Raspberry Pi.

## Vector Modules
Placeholder modules `vector001`–`vector163` implement individual anti-cheat checks. Each exposes a `run()` function returning a status string.

## Overlay App
The `overlay-app/` directory contains placeholder modules for an Android
application that renders overlay elements on top of the game. These files will
eventually be replaced with full Kotlin/Java implementations.

## Development
Run sanitizers and tests before committing:

```bash
python ci/remove_cjk.py $(git ls-files '*.py')
python ci/remove_bidi.py $(git ls-files '*.py')
pytest -q
```
