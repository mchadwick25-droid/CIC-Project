"""CO-P2-17 (Mark, 2026-07-28) - telos + living_traditions onto
alexcore001, verbatim from the deployed prompt's two closing paragraphs
(CO-P2-05's Alexandria application + the living-traditions companion).

The S2.8 completeness proof's two named GAPs close: paragraph 29 (the
Christ-Ward Telos) -> world_core.telos (the CO-P2-05 field, provisional
status + review flag per the Desert convention); paragraph 30 (the
Living-Traditions distinction) -> world_core.living_traditions (the
CO-P2-17 field, same shape). Both texts verbatim from
data/alexandria_world/alex_Representative_Permanent_Prompt_Theon.txt -
mechanical backfill, anchored and asserted; no authoring.

Idempotent; fence-asserting reader; single-file touch (alexcore001).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

CORE = (BACKEND / "wrs" / "records" / "alexandria_world" / "world_core"
        / "alexcore001.md")
PROMPT = (BACKEND / "data" / "alexandria_world"
          / "alex_Representative_Permanent_Prompt_Theon.txt")

REVIEW_FLAG = ("Backfilled verbatim from the deployed Permanent Prompt's "
               "own Article-35 vision section (built at the original "
               "deployment-artifact phase); provisional pending the "
               "project-lead freeze gates (Article 29 Living-Tradition "
               "confirmation; Article 31 external review - Doc_08 SS9).")

BODY_NOTE = ("\n\nCO-P2-17 (2026-07-28): telos + living_traditions "
             "backfilled verbatim from the deployed prompt's two closing "
             "paragraphs (the S2.8 coverage GAPs closed); see "
             "wrs/migrate/s62_alx_s29_co17.py.")


def main():
    paras = [p.strip() for p in
             PROMPT.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    telos = paras[-2]
    living = paras[-1]
    assert telos.startswith("The Scriptures we read are not, in the end,"), telos[:60]
    assert living.startswith("What has grown from the life we"), living[:60]

    rec, body = read_record(CORE)
    want_t = {"text": telos, "status": "provisional", "review_flag": REVIEW_FLAG}
    want_l = {"text": living, "status": "provisional", "review_flag": REVIEW_FLAG}
    if rec.get("telos") == want_t and rec.get("living_traditions") == want_l:
        print("already applied (idempotent re-run)")
        return
    rec["telos"] = want_t
    rec["living_traditions"] = want_l
    if "CO-P2-17" not in body:
        body += BODY_NOTE
    emit_record(rec, body, CORE)
    print("alexcore001: telos + living_traditions set (verbatim, provisional)")


if __name__ == "__main__":
    main()
