"""CO-P2-04 (Mark, 2026-07-27) - FLAG-004 resolved: FEC prose into typed links.

For each of the eight Desert story records:
- parse the S2.8-parked Formation Ecology Connection text out of the
  record body, extract the gravity numbers it names, and write
  `gravity_links[]`: the FIRST link's note carries the full FEC prose
  VERBATIM (the chunk view renders the section from it); each further
  named gravity gets a pointer note. Nothing is re-authored - this is a
  restructure of preserved text into the queryable shape Mark approved.
- desertstory008 additionally: the parked Source Identification table
  (SS3.3's own tier-4 rule: every element sourced) becomes per-element
  `sources[]` entries. The element line and the build-doc locus ride
  VERBATIM in each entry's note; the source_id anchors each element to
  the nearest primary work-row (Kellia srcDES009 / Nepheros srcDES010
  for the material elements; the narrative-source rows srcDES005/007
  for the liturgical-rhythm elements, whose build-doc evidence is
  collective). The Round-1 diet-removal Note is preserved on the last
  element entry.
- both parking blocks (and their delimiters) are removed from the body.

Idempotent: records already carrying gravity_links are skipped.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
STORIES = BACKEND / "wrs" / "records" / "desert_world" / "story"

FEC_DELIM_RE = re.compile(
    r"\n*\[Formation Ecology Connection[^\]]*\]\n(.*?)(?=\n*\[Source Identification|\Z)",
    re.S)
# NOTE: the delimiter text itself contains "sources[]", so a naive
# [^\]]* match terminates early on that inner "]" - match the exact
# literal delimiter instead (the bug this script's first run hit on 008)
_SRC_DELIM = ("[Source Identification — parked at S2.8 per FLAG-004; "
              "SS3.3's tier-4 rule names sources[] as the home; awaiting S2.9]")
SRC_DELIM_RE = re.compile(r"\n*" + re.escape(_SRC_DELIM) + r"\n(.*)\Z", re.S)

# story008 element -> anchor work-row (locus rides verbatim in the note)
S8_ANCHORS = {
    "Continuous Psalter recitation": "srcDES005",
    "Manual labor in the cell": "srcDES009",
    "Cell as basic architectural unit": "srcDES009",
    "Weekly Saturday-to-Sunday synaxis": "srcDES007",
}
S8_EXTRA = {"Manual labor in the cell": "srcDES010"}


def body_probe(parts):
    return "---\n".join(parts[2:])


def main() -> None:
    converted = 0
    for p in sorted(STORIES.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        parts = text.split("---\n")
        fm = yaml.safe_load(parts[1])
        if fm.get("gravity_links") and "[Source Identification" not in body_probe(parts):
            continue
        body = "---\n".join(parts[2:])
        m = FEC_DELIM_RE.search(body)
        if not m and not fm.get("gravity_links"):
            continue
        fec = m.group(1).strip() if m else ""
        nums = sorted({int(n) for grp in
                       re.findall(r"gravit\w+ (\d+(?:,\s*\d+)*(?:,? and \d+)?)", fec)
                       for n in re.findall(r"\d+", grp)}) if fec else []
        links = []
        for i, n in enumerate(nums):
            gid = f"desertgrav{n:03d}"
            if i == 0:
                links.append({"gravity_id": gid, "note": fec})
            else:
                links.append({"gravity_id": gid,
                              "note": ("Named in this story's Formation "
                                       "Ecology Connection - full text on "
                                       "the first gravity_links note "
                                       "(CO-P2-04).")})
        if links:
            fm["gravity_links"] = links
        body = FEC_DELIM_RE.sub("", body)

        sm = SRC_DELIM_RE.search(body)
        if sm:
            table = sm.group(1).strip()
            note_m = re.search(r"\*\*Note:\*\* (.*)\Z", table, re.S)
            trailing_note = " ".join(note_m.group(1).split()) if note_m else ""
            elements = re.findall(
                r"\*\*Element from Story Text:\*\* (.*?)\n\*\*Source:\*\* (.*?)(?=\n\n|\Z)",
                table, re.S)
            srcs = fm.setdefault("sources", [])
            for i, (el, loc) in enumerate(elements):
                el, loc = " ".join(el.split()), " ".join(loc.split())
                anchor = next((sid for key, sid in S8_ANCHORS.items()
                               if el.startswith(key)), "srcDES005")
                note = (f"Element from Story Text: {el} || Source: {loc} "
                        f"(SS3.3 tier-4 rule backfill, CO-P2-04; anchored "
                        f"to the nearest primary work-row - the build-doc "
                        f"locus is the operative citation)")
                if i == len(elements) - 1 and trailing_note:
                    note += f" || Note: {trailing_note}"
                srcs.append({"source_id": anchor, "author_gravity_note": note})
                extra = next((sid for key, sid in S8_EXTRA.items()
                              if el.startswith(key)), None)
                if extra:
                    srcs.append({"source_id": extra,
                                 "author_gravity_note":
                                     f"Element from Story Text: {el} || "
                                     f"papyrological side of the same "
                                     f"element (Doc_02 SS5.2)"})
            body = SRC_DELIM_RE.sub("", body)

        if "CO-P2-04 (2026-07-27): parked" not in body:
            body = body.rstrip("\n") + ("\n\nCO-P2-04 (2026-07-27): parked "
                   "FLAG-004 sections restructured into gravity_links[] (FEC "
                   "verbatim on the first link) and, for this record's "
                   "tier-4 table, per-element sources[] entries.\n")
        else:
            body = body.rstrip("\n") + "\n"
        p.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                               allow_unicode=True, width=100)
                     + "---\n" + body, encoding="utf-8")
        converted += 1
    print(f"converted {converted} story records")


if __name__ == "__main__":
    main()
