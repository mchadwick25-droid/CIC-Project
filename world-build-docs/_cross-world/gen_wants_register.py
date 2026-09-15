"""Generates WANTS-REGISTER.md — sources the fleet already depends on and
cannot read, ranked by how much depends on them.

WHY. Mark, 2026-08-26: *"currently we are restricted to only open source, but
that doesnt mean we wont raise funds to purchase other sources in the future
so a list of other sources and their value would be helpful."*

Value here is not a guess. Every world already declares its sources, and a
`source` record whose `edition` names no vendored file is one the build
consulted but the pipeline cannot verify — the wording of anything resting on
it can never be re-checked by any session. The number of records depending on
such a source is a real, derived measure of what acquiring it would unlock,
and it is the number this report ranks on.

Three kinds get separated, because they need three different actions and
conflating them is how the desert Apophthegmata gap came to read as a
historical silence rather than an unfilled request:

  ACQUIRABLE, PUBLIC DOMAIN - a public-domain edition exists and simply was
      never obtained. Costs nothing but someone's attention. Budge's
      Apophthegmata is the standing example.
  PURCHASABLE - in copyright, buyable, and the reason this register exists.
      A modern critical translation cannot be vendored (redistribution), but
      it can be bought and consulted, which is what these records already do.
  NO EDITION EXISTS - no usable English translation is known. Money does not
      fix these; they stay honest limits.

The split cannot be read off the records mechanically, so this script reports
what it can measure and marks the rest `unclassified` for a human. It does not
guess which bucket a source belongs in.

SECOND HALF, added 2026-09-15: the Atlas's documented stories.

The register was generated from records/ alone, and so could not see the
largest single block of citations in the project. The 545 `documentedStories`
in cic-website/atlas-v3.html carry 1,111 primary-source citations, and the
field exists only in that file - world-census.json holds none of it. A
verification audit that month (Ministry/Operations/Audits/
CiC_Atlas_Documented_Stories_Verification_Audit_2026-09-15.md) found 490 of
the 545 stories declaring "primary text not yet read", 177 of those carrying
369 quoted spans, and - reading the one story whose source was vendored
completely enough to audit - four real corrections. The instrument meant to
surface exactly that condition was blind to it.

The same discipline applies here as above: a work is a want because the data
says so in its own words, never because this script inferred it. A story's
`verification` field states whether its primary text was read; that is the
signal used, and nothing is concluded from a work's title. In particular this
half does NOT try to decide whether a cited work is vendored: matching a
citation string to a file under cic/texts/ proved unreliable in the audit
(Gregory the Great's Register of Epistles passing for his Dialogues, Gregory
of Nyssa for Gregory of Nazianzus), and a check that quietly mismatches is
worse than one that abstains.

    python world-build-docs/_cross-world/gen_wants_register.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.m1.loader import load_world_records  # noqa: E402
from engine.m1.registry import formation_world_keys  # noqa: E402

# Phrases a source record uses about its own edition, mapped to what action
# the source needs. Read off the records' own words, never inferred from the
# work's title.
_PD_AVAILABLE = re.compile(r"public.domain english exists|PD English requested|Budge", re.I)
_CONSULT_ONLY = re.compile(r"consult(ation)?.only|copyrighted", re.I)
_NONE_POSSIBLE = re.compile(r"none possible|no english edition vendorable|not vendorable", re.I)
# The claim is attested entirely inside another source this world already
# vendored - the record names that source, not an edition of its own, so
# there is nothing left to acquire. Distinct from a record whose OWN edition
# names a cic/texts/ file (gather_rows filters those out before classify()
# ever runs); this is a second remove - e.g. a fact from Basil's letters that
# is only ever cited "within" or "attested via" another already-vendored
# source record.
_ATTESTED_VIA_VENDORED = re.compile(
    r"\b(within|attested (via|collectively via)|transmitted solely inside|accessed only via)\b", re.I
)
# The record itself says there is no document to hold rights over - a
# person, an institution, or a general historical pattern, not a text. Money
# and attention both fail here for the same reason "no edition exists" does,
# but for a different one: there is no work to find an edition of, ever.
_NOT_A_HELD_TEXT = re.compile(
    r"not applicable in the ordinary sense|no text exists to hold rights over", re.I
)


def classify(record: dict) -> str:
    edition = str(record.get("edition") or "")
    rights = str(record.get("rights_status") or "")
    blob = " ".join((edition, rights, str(record.get("discovery_channel") or "")))
    if "cic/texts/" in rights and _ATTESTED_VIA_VENDORED.search(edition):
        return "resolved (attested via a vendored source)"
    if _NOT_A_HELD_TEXT.search(rights):
        return "not a held text (nothing to acquire)"
    if _PD_AVAILABLE.search(blob):
        return "acquirable, public domain"
    if _NONE_POSSIBLE.search(blob):
        return "no edition exists"
    if _CONSULT_ONLY.search(blob):
        return "purchasable (in copyright)"
    return "unclassified"


def gather_rows() -> tuple[list, list]:
    """Every wanted source, classified, sorted - the data main() renders and
    the same data DOWNLOAD-QUEUE.md's generator draws on, split out
    2026-09-02 specifically so the queue doesn't have to scrape this
    module's own generated markdown table to get at data that already
    exists here as plain dicts. Returns (rows, worlds)."""
    worlds = formation_world_keys()
    rows = []
    for world_key in worlds:
        records = load_world_records(world_key)
        dependents: dict[str, int] = defaultdict(int)
        for record in records.values():
            for ref in record.get("sources") or []:
                if ref.get("source_id"):
                    dependents[ref["source_id"]] += 1
        for rid, record in records.items():
            if record.get("record_type") != "source":
                continue
            if "cic/texts/" in str(record.get("edition") or ""):
                continue  # vendored; nothing wanted
            rows.append({
                "world": world_key,
                "id": rid,
                "depends": dependents.get(rid, 0),
                "kind": classify(record),
                "author": str(record.get("author") or "").split("(")[0].strip()[:44],
                "work": str(record.get("work") or "").split(" - ")[0].strip()[:78],
            })
    rows.sort(key=lambda r: (-r["depends"], r["world"], r["id"]))
    return rows, worlds


ATLAS = ROOT / "cic-website" / "atlas-v3.html"
_UNREAD = "primary text not yet read"
# The stories quote with curly single quotes and contain no double quotes at
# all - a detail worth keeping in code, because searching for the wrong mark
# is what first reported this corpus as carrying zero quotations.
_QUOTE = re.compile(r"\u2018[^\u2018\u2019]{8,400}\u2019")


def _atlas_stories() -> list[dict]:
    """Every documentedStory in atlas-v3.html, with its owning entry id.

    The file is a web page with the census inlined, not a data file, so each
    record is located by its own `"id": "..."` and decoded from there.
    """
    import json
    text = ATLAS.read_text(encoding="utf-8")
    dec = json.JSONDecoder()
    out = []
    for wid in dict.fromkeys(re.findall(r'"id": "([a-z0-9\-]+)"', text)):
        i = text.find('"id": "%s"' % wid)
        start = text.rfind("{", 0, i)
        try:
            obj, _end = dec.raw_decode(text, start)
        except ValueError:
            continue
        if obj.get("id") != wid:
            continue
        for story in obj.get("documentedStories") or []:
            out.append({"world": wid, **story})
    return out


def gather_atlas_rows() -> tuple[list, int, int]:
    """Primary sources the Atlas's stories cite without having read, grouped by
    the citation's leading name. Returns (rows, story_count, entry_count).

    Grouped by name, not by work, because ranking individual works produced
    nothing usable: 1,885 distinct works, almost every one cited exactly once,
    so the "ranking" came out alphabetical. Acquisition works by author and
    volume anyway - obtaining Eusebius answers eleven stories at once, which
    is the number worth printing.

    Value is the number of citing stories that actually quote. A quotation is
    the sharpest thing that can rest on a source nobody has opened, and the one
    the 2026-09-15 audit found real errors in. Counts are per story and are
    never divided among the works a story cites - which quotation came from
    which of its four sources is not in the data, and apportioning it would be
    invention.
    """
    stories = _atlas_stories()
    agg: dict[str, dict] = {}
    for s in stories:
        if _UNREAD not in str(s.get("verification") or ""):
            continue
        quoting = bool(_QUOTE.search(s.get("text") or "") or _QUOTE.search(s.get("teaser") or ""))
        for ref in s.get("sources") or []:
            if str(ref.get("type") or "") != "primary":
                continue
            work = str(ref.get("work") or "").strip()
            # The leading name: an author where there is one, the work's own
            # title where there is not ("Russian Primary Chronicle").
            cited = re.split(r"[,(]", work)[0].strip()[:52]
            if len(cited) < 3:
                continue
            row = agg.setdefault(cited, {
                "cited": cited, "stories": 0, "quoting": 0,
                "entries": set(), "works": set(),
            })
            row["stories"] += 1
            row["quoting"] += int(quoting)
            row["entries"].add(s["world"])
            row["works"].add(work[:70])
    rows = []
    for row in agg.values():
        row["entries"] = len(row["entries"])
        row["works"] = len(row["works"])
        rows.append(row)
    rows.sort(key=lambda r: (-r["quoting"], -r["stories"], r["cited"]))
    return rows, len(stories), len({s["world"] for s in stories})


def atlas_totals(stories: list[dict]) -> dict:
    """The counts the Atlas section quotes about itself, measured not assumed."""
    unread = [s for s in stories if _UNREAD in str(s.get("verification") or "")]
    quoting = [s for s in unread
               if _QUOTE.search(s.get("text") or "") or _QUOTE.search(s.get("teaser") or "")]
    spans = sum(len(_QUOTE.findall(s.get("text") or "")) + len(_QUOTE.findall(s.get("teaser") or ""))
                for s in quoting)
    refs = {str(r.get("work") or "")[:96] for s in stories for r in (s.get("sources") or [])
            if str(r.get("type") or "") == "reference"}
    cites = sum(1 for s in stories for r in (s.get("sources") or [])
                if str(r.get("type") or "") == "primary")
    return {"unread": len(unread), "quoting": len(quoting), "spans": spans,
            "refs": len(refs), "cites": cites}


def main() -> None:
    rows, worlds = gather_rows()
    by_kind: dict[str, list] = defaultdict(list)
    for row in rows:
        by_kind[row["kind"]].append(row)

    out = ["# Wants register — sources the fleet depends on and cannot read\n"]
    out.append(
        "Generated by `gen_wants_register.py`. Every entry is a `source` record some world "
        "already consulted, whose `edition` names no file under `cic/texts/`. **Value is the "
        "number of records that depend on it** — a measure of what acquiring it would let the "
        "pipeline verify, not an opinion about the work's importance.\n"
    )
    out.append(
        "A record resting on an unreadable source is not wrong; it is unverifiable. Its wording "
        "can never be re-checked by a later session, which is the difference `CORPUS-USE.md` "
        "measures as each world's verifiability share.\n"
    )
    out.append(f"\n**{len(rows)} sources across {len(worlds)} worlds**, "
               f"carrying {sum(r['depends'] for r in rows)} record dependencies between them.\n")

    order = [
        "acquirable, public domain",
        "purchasable (in copyright)",
        "no edition exists",
        "resolved (attested via a vendored source)",
        "not a held text (nothing to acquire)",
        "unclassified",
    ]
    blurbs = {
        "acquirable, public domain":
            "**Costs nothing but attention.** A public-domain edition exists and was never "
            "obtained. The agents' sandbox blocks every text host, so these need a human to "
            "fetch them — exactly how the other 46 files arrived.",
        "purchasable (in copyright)":
            "**The reason this register exists.** In copyright, so they can never be vendored "
            "(redistribution), but they can be bought and consulted — which is what the records "
            "citing them already do. Buying one does not make its text verifiable; it makes the "
            "consultation legitimate and current.",
        "no edition exists":
            "**Money does not fix these.** No usable English translation is known to exist. They "
            "stay honest limits, and a world resting on one should say so.",
        "resolved (attested via a vendored source)":
            "**Nothing to do.** The claim is attested entirely inside a source this world has "
            "already vendored — the record names that source, not an edition of its own. "
            "Verifiable today; listed here only because its own `edition` field, read alone, "
            "names no `cic/texts/` file.",
        "not a held text (nothing to acquire)":
            "**An honest non-want.** The record itself says there is no document to hold rights "
            "over — a person, an institution, or a general historical pattern, not a text. There "
            "is nothing to ever acquire, at any price, in any language.",
        "unclassified":
            "Not classifiable from the record's own words. A human should sort these into the "
            "categories above rather than this script guessing.",
    }
    for kind in order:
        group = by_kind.get(kind)
        if not group:
            continue
        out.append(f"\n## {kind} — {len(group)}\n")
        out.append(blurbs[kind] + "\n")
        out.append("| value | world | author | work |")
        out.append("|---:|---|---|---|")
        for row in group:
            value = f"**{row['depends']}**" if row["depends"] >= 5 else str(row["depends"])
            out.append(f"| {value} | `{row['world']}` | {row['author'] or '—'} | {row['work']} |")

    # ---- second half: the Atlas's documented stories -----------------------
    arows, nstories, nentries = gather_atlas_rows()
    tot = atlas_totals(_atlas_stories())
    out.append("\n---\n")
    out.append("# The Atlas's documented stories\n")
    out.append(
        f"{nstories} `documentedStories` across {nentries} Atlas entries, carrying "
        f"**{tot['cites']} primary-source citations**. The field lives only in "
        "`cic-website/atlas-v3.html` — `world-census.json` holds none of it — which is why this "
        "register could not see any of it before 2026-09-15.\n"
    )
    out.append(
        f"**{tot['unread']} of those stories say their primary text was not read**, and "
        f"{tot['quoting']} of those put {tot['spans']} quoted spans into a historical figure's "
        "mouth. That is the condition this register exists to surface, and the table below is "
        "what it costs.\n"
    )
    out.append(
        "**Grouped by the citation's leading name, not by work.** Ranking works produced "
        "nothing usable — 1,885 distinct works, almost every one cited once — and acquisition "
        "works by author and volume anyway. **Value is citing stories that quote**, counted per "
        "story and never divided among the works a story cites; which quotation came from which "
        "of its sources is not in the data.\n"
    )
    out.append(
        "**This half does not say whether a work is vendored.** Matching a citation to a file "
        "under `cic/texts/` proved unreliable in the audit — Gregory the Great's *Register of "
        "Epistles* passed for his *Dialogues*, Gregory of Nyssa for Gregory of Nazianzus — and a "
        "check that quietly mismatches is worse than one that abstains. Settling it takes the "
        "audit's method: find the cited passage and read it.\n"
    )
    head = [r for r in arows if r["stories"] >= 2]
    tail = len(arows) - len(head)
    out.append(f"\n## Cited but not read — {len(arows)} names\n")
    out.append("| quoting | stories | entries | works | cited |")
    out.append("|---:|---:|---:|---:|---|")
    for row in head:
        q = f"**{row['quoting']}**" if row["quoting"] >= 3 else str(row["quoting"])
        out.append(f"| {q} | {row['stories']} | {row['entries']} | {row['works']} | {row['cited']} |")
    out.append(
        f"\nBelow this, **{tail} names are cited by a single story each** — the long tail of a "
        "corpus that spans ten eras, and not a ranking. They are in the data, not in this table, "
        "because a table of one-apiece rows sorted alphabetically is not a priority list.\n"
    )
    out.append(
        f"\n{tot['refs']} distinct **reference works** are also cited. They are modern secondary "
        "literature, mostly in copyright and not vendorable, and they are what the stories were "
        "actually written from — so they are counted here but not listed: nothing about them is "
        "acquirable in the sense this register means.\n"
    )

    out.append("\n---\n")
    out.append(
        "## Adding to this register\n\n"
        "It is generated, not maintained: a source becomes a want by being written as a `source` "
        "record with no vendored edition, which is what a build thread does anyway when it "
        "consults something it cannot vendor. Nothing extra to remember.\n\n"
        "A source that is *wanted but not yet consulted by any world* has no record and so "
        "will not appear here. If the corpus-assignment thread finds such things — and it will, "
        "working through a collection this size — they belong in the same place: a `source` "
        "record with `edition: \"not vendored\"` and a `discovery_channel` saying where it was "
        "seen. It then shows up with value 0, which is honest: nothing depends on it yet.\n"
    )

    target = Path(__file__).resolve().parent / "WANTS-REGISTER.md"
    target.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
