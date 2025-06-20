import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


def test_vectors_run():
    for i in range(1, 164):
        mod = importlib.import_module(f'vector.vector{i:03d}')
        assert mod.run() == f'vector{i:03d} executed'
