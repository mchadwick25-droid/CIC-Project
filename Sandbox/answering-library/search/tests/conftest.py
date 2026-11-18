import sys
from pathlib import Path

LIBRARY = Path(__file__).resolve().parents[2]
ROOT = Path(__file__).resolve().parents[4]
for path in (str(LIBRARY), str(ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)
