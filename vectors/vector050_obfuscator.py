"""vector050_obfuscator.py - File Obfuscator

Purpose: Rename and obfuscate specified files to reduce detection surface. The
new names are returned for reference.
"""

from __future__ import annotations

import os
import random
import string
import time
from pathlib import Path
from typing import Iterable, List

AUDIT_LOG = "/test/vector050_obfuscator.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


def _rand_name(length: int = 8) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class ObfuscatorAgent:
    def obfuscate(self, paths: Iterable[str]) -> List[str]:
        new_paths: List[str] = []
        for path in paths:
            p = Path(path)
            new_name = p.with_name(_rand_name() + p.suffix)
            try:
                p.rename(new_name)
                audit_log(f"renamed {p} -> {new_name}")
                new_paths.append(str(new_name))
            except Exception as e:  # pragma: no cover - file perms
                audit_log(f"error {p} {e}")
        return new_paths

    def run(self, paths: Iterable[str]) -> List[str]:
        audit_log("obfuscator start")
        result = self.obfuscate(paths)
        audit_log("obfuscator end")
        return result


def run(paths: Iterable[str]) -> List[str]:
    return ObfuscatorAgent().run(paths)


if __name__ == "__main__":  # pragma: no cover
    run([])
