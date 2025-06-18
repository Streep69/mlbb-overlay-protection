"""Integration for https://github.com/hunternblz/Moonton-Checker"""
from __future__ import annotations
import subprocess
import tempfile
from pathlib import Path

def setup() -> Path:
    """Clone the repository."""
    temp = Path(tempfile.mkdtemp(prefix='Moonton_Checker_'))
    subprocess.run(['git', 'clone', '--depth', '1', 'https://github.com/hunternblz/Moonton-Checker.git', str(temp)], check=True)
    return temp

def integrate(config):
    """Integrate detected modules.

    Detected symbols: none
    TODO: wire into overlay lifecycle.
    """
    raise NotImplementedError
