"""The one place in this codebase authorized to read
canon/sealed_probes/plaintext/ - M3 (this package) is exactly the harness
canon/sealed_probes/README.md names as the sole authorized reader.
engine/canon/check_seal_isolation.py's guarded directory list does not
include engine/m3, by deliberate omission, not oversight.
"""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PLAINTEXT_DIR = REPO_ROOT / "canon" / "sealed_probes" / "plaintext"


def read_probe(probe_id: str, plaintext_dir: Path = PLAINTEXT_DIR) -> dict:
    raw = (plaintext_dir / f"{probe_id}.md").read_text(encoding="utf-8")
    _, front_matter, body = raw.split("---", 2)
    fields = dict(re.findall(r"^(\w+): (.*)$", front_matter, re.MULTILINE))
    return {**fields, "text": body.strip()}
