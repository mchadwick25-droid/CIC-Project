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

    python Build/worlds/_cross-world/gen_wants_register.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
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
