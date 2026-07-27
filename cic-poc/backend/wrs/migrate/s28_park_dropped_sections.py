"""S2.8 - park the S2.4-dropped story sections verbatim (FLAG-004, FLAG-002 precedent).

Appends each deployed story chunk's `## Formation Ecology Connection`
section (and, for desertstory008, the `## Source Identification` section)
VERBATIM to the corresponding story record's free-text body, under an
explicit marked delimiter. The body is not schema-governed - no schema
edit occurs; the restructure decision (typed story->gravity links vs. an
ecology_connection field; sources[] backfill for 008 per SS3.3's tier-4
rule) stays open for Mark at S2.9. The story-chunk view renders the
section back out of this parking, restoring render parity and the
measured B-RETR baseline (DES-TH-05).

Idempotent: skips a record whose body already carries the delimiter.
"""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
RECORDS = BACKEND / "wrs" / "records" / "desert_world" / "story"
CHUNKS = BACKEND / "data" / "desert_world" / "story_chunks"

DELIM_FEC = ("[Formation Ecology Connection — parked at S2.8 per FLAG-004; "
             "awaiting S2.9 restructure]")
DELIM_SRC = ("[Source Identification — parked at S2.8 per FLAG-004; SS3.3's "
             "tier-4 rule names sources[] as the home; awaiting S2.9]")


def section(text: str, name: str) -> str:
    m = re.search(rf"## {name}\s*\n(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1).strip().strip("-").strip() if m else ""


def main() -> None:
    parked = 0
    for chunk in sorted(CHUNKS.glob("*.md")):
        rid = chunk.stem.split("_")[0]
        rec_path = RECORDS / f"{rid}.md"
        text = rec_path.read_text(encoding="utf-8")
        if DELIM_FEC in text:
            continue
        ctext = chunk.read_text(encoding="utf-8")
        fec = section(ctext, "Formation Ecology Connection")
        add = f"\n\n{DELIM_FEC}\n{fec}"
        src = section(ctext, "Source Identification")
        if src:
            add += f"\n\n{DELIM_SRC}\n{src}"
        rec_path.write_text(text.rstrip("\n") + add + "\n", encoding="utf-8")
        parked += 1
    print(f"parked dropped sections into {parked} story record bodies")


if __name__ == "__main__":
    main()
