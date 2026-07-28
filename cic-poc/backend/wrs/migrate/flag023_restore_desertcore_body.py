"""FLAG-023 restoration - desertcore001's lost body provenance chain.

Defect: `s25_gravity_force.py` (and its CO-P2-02 re-run) updated the
Desert world_core with `split("\\n---", 2)` and `parts[2]` - but a record
file contains ONE "\\n---" occurrence, so parts[2] never existed and the
body was written back empty. Losses, from git:
  - at S2.5 (553a403): the S2.1 migration provenance note (and S2.5's
    intended "gravities[] populated" edit never landed);
  - at CO-P2-02 (6bd5d74): the S2.7a note that had replaced the empty body;
  - CO-P2-05 (e4580d9) then appended its note to the emptied body.

Restoration: the full provenance chain, verbatim from the commits named
above, with S2.5's intended gravities[] edit applied as it was meant to
read (Desert classified all ten candidates - no not-advanced set), plus
the FLAG-023 marker. Alexandria's S2.5 script uses a partition-based
reader with fence asserts instead; store-wide sweep found no other
empty-body record.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

import yaml
from s62_alx_source_rows import emit_record

CORE = BACKEND / "wrs" / "records" / "desert_world" / "world_core" / "desertcore001.md"

CO_P2_05_NOTE = ("CO-P2-05 (2026-07-27, Alternative A): telos added - Doc10 S5's own "
                 "paragraph verbatim, provisional flag carried.")

RESTORED = """Migrated at S2.1 (2026-07-26) from `World-Builds/Desert-Monasticism/CiC_W3_Doc01_World_Identification.md` (SS1, SS2) and `cic-poc/backend/app/world_manifest.py` (period). gravities[] populated at S2.5 (all ten Doc_04 candidates); pairing_guidance/cautions arrive at S2.7a.

S2.7a (2026-07-27): pairing_guidance + cautions authored as records per Pass 1 SS4.5 - each guidance entry reflects a documented cross-lens finding with evidence links; cautions from Doc_09b/c's own named gaps and the Doc10/LiveTest record.

""" + CO_P2_05_NOTE + """

FLAG-023 (2026-07-27): this body was silently emptied twice by world_core rewrites in `s25_gravity_force.py` (at S2.5 and again at the CO-P2-02 re-run) - a front/body split whose parts[2] never existed. Restored from git (40be5ab's S2.1 note with S2.5's intended gravities[] edit applied; 0633a2d's S2.7a note; e4580d9's CO-P2-05 note kept). Frontmatter untouched. See FLAGS.md FLAG-023."""


def main():
    txt = CORE.read_text(encoding="utf-8")
    assert txt.startswith("---\n"), "no opening fence"
    front, sep, body = txt[4:].partition("\n---\n")
    assert sep, "no closing fence"
    rec = yaml.safe_load(front)
    assert rec["id"] == "desertcore001"
    if "FLAG-023" in body:  # idempotent re-run
        print("already restored")
        return
    # the current body must be exactly the orphaned CO-P2-05 note -
    # anything else means the situation changed and needs re-diagnosis
    assert body.strip() == CO_P2_05_NOTE, f"unexpected current body: {body.strip()[:120]!r}"
    emit_record(rec, RESTORED, CORE)
    print("desertcore001 body restored (FLAG-023)")


if __name__ == "__main__":
    main()
