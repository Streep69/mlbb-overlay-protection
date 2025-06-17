#!/usr/bin/env python3
"""Remove BIDI control characters from given files."""
import sys
import re
from pathlib import Path

BIDI_RE = re.compile(r"[\u202A-\u202E\u2066-\u2069]")


def sanitize_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    sanitized = BIDI_RE.sub('', text)
    if text != sanitized:
        path.write_text(sanitized, encoding='utf-8')
        return True
    return False


def main(files):
    changed = False
    for file in files:
        if sanitize_file(Path(file)):
            print(f"[remove_bidi] sanitized {file}")
            changed = True
    if changed:
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
