# mlbb-overlay-protection

This project provides a non-root overlay cheat framework for Mobile Legends: Bang Bang streamed from an S23 Ultra to a Raspberry Pi.

## Vector Modules
Placeholder modules `vector001`–`vector163` implement individual anti-cheat checks. Each exposes a `run()` function returning a status string.

## Setup
Install Python dependencies with `pip`:

```bash
pip install -r requirements.txt
```

### Usage
Run a vector module directly:

```bash
python -c "import vector.vector001 as v; print(v.run())"
```

Execute the test suite:

```bash
pytest -q
```

## Development
Run sanitizers and tests before committing:

```bash
python ci/remove_cjk.py $(git ls-files '*.py')
python ci/remove_bidi.py $(git ls-files '*.py')
pytest -q
```

Further documentation will be available in the `docs/` directory once populated.
