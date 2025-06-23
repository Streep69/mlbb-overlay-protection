#!/usr/bin/env python3
"""Remove CJK characters from given files."""
import sys
import re
from pathlib import Path

CJK_RE = re.compile(r"[\u3000-\u9FFF]")


def sanitize_file(path: Path) -> bool:
    try:
        text = path.read_text(encoding='utf-8')
        sanitized = CJK_RE.sub('', text)
        if text != sanitized:
            path.write_text(sanitized, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"[remove_cjk] error processing file {path}: {e}")
        return False


def main(files):
    safe_root = Path("/safe/root/directory").resolve()
    changed = False
    for file in files:
        file_path = Path(file).resolve()
        if not str(file_path).startswith(str(safe_root)):
            print(f"[remove_cjk] skipping unsafe file path: {file}")
            continue
        if sanitize_file(file_path):
            print(f"[remove_cjk] sanitized {file}")
            changed = True
    if changed:
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
