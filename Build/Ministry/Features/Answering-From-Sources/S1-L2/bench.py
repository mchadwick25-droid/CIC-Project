"""S1-L2 replay bench: selection-and-insertion quoting on the saved drafts of
fleet graded run 1. No model call.

For each saved draft the bench rebuilds the turn's evidence the way the run did
and checks that engine.m4.turn.apply_net reproduces the shipped answer. It then
repairs each sentence apply_net removed for a quotation reason, in three
cumulative steps, and runs apply_net again on the repaired draft:

  V1  a quote marker refused for its lead-in is placed with a lead-in code
      writes from the record's speaker name
  V2  V1, and a quotation the voice typed is replaced by the offered quote
      record it matches word for word
  V3  V2, and a removed sentence that cites an offered quote record is
      replaced by that record, placed by code

A reply may carry one placed quote, so a draft whose quote was already placed
takes no repair. Placement and the net are the engine's own, unchanged.

Usage: python bench.py <fleet-run-dir> <out-dir>
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))

from engine.m1.loader import load_fleet_records  # noqa: E402
from engine.m1.registry import load_registry  # noqa: E402
from engine.m3 import sealed_probes  # noqa: E402
from engine.m4 import evidence as ev  # noqa: E402
from engine.m4 import grounding_net as gn  # noqa: E402
from engine.m4 import quote_placement as qp  # noqa: E402
from engine.m4 import turn as turn_module  # noqa: E402
from engine.m4.story_placement import with_placeable_stories  # noqa: E402
from engine.m4.world_loader import LazyWorldLoader  # noqa: E402
from engine.prose import quote_aware_sentences  # noqa: E402

FILES = {
    "alx": "alx.json", "desert": "desert.json", "don": "don.json", "gallic": "gallic.json", "hal": "hal.json",
    "ijc": "ijc.json", "lpc": "lpc.json", "pahc": "pahc.json", "syr": "syr.json", "witt": "witt.json",
    "rzg": "rzg-attempt2.json",
}
LEAD_REFUSALS = {gn.REASON_SPEAKER_UNNAMED, gn.REASON_PLACED_MISMATCH, gn.REASON_LEAD_TYPES_QUOTATION}
CITED_QUOTE_REASONS = {
    gn.REASON_TYPED_QUOTATION, gn.REASON_ATTRIBUTION, gn.REASON_UNPLACED_WORDS, gn.REASON_QUOTE_RECORD_UNVOICED,
    gn.REASON_QUOTE_WORDS, gn.REASON_QUOTE_RECORD_UNPLACED, gn.REASON_ATTRIBUTION_LEAD, gn.REASON_LEAD_IN,
}
MIN_TYPED_WORDS = 4
MAX_ROUNDS = 3
ORPHAN_OPENERS = re.compile(
    r"^(he|she|it|they|his|her|its|their|him|them|this|that|these|those|such|here|there|so|but|yet|and|then|thus|for|also|still"
    r"|in that|by this|the same)\b", re.IGNORECASE)
MARKER_ID = re.compile(r"\[\[\s*quote\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")


def norm(text: str) -> str:
    return " ".join(re.findall(r"[\w']+", gn.strip_tags(text).lower()))


class Repairer:
    def __init__(self, records: dict, context: qp.PlacementContext):
        self.records = records
        self.context = context
        self.index = gn.QuotationIndex(records)
        self.quotes = {
            rid: r for rid, r in records.items()
            if r.get("record_type") == "quote" and rid in context.offered and rid not in context.voiced
            and (r.get("modern_rendering") or "").strip()
        }

    def code_sentence(self, record: dict) -> str:
        name = self.index.speaker_name(record)
        return f"{name[:1].upper()}{name[1:]} puts it this way: [[quote:{record['id']}]]"

    def repairs(self, removed: list[dict], step: int) -> list[dict]:
        """One repair per round: the first removed sentence a step can turn
        into a placed quote."""
        for entry in removed:
            draft, why = entry["draft"], entry["why"]
            found = MARKER_ID.search(draft)
            if found and why in LEAD_REFUSALS:
                record = self.quotes.get(found.group(1).lower())
                if record:
                    return [{"step": 1, "draft": draft, "record": record["id"], "with": self.code_sentence(record)}]
            if step >= 2 and why == gn.REASON_TYPED_QUOTATION:
                for _o, _c, inner in gn.quoted_span_positions(gn.strip_tags(draft)):
                    if len(inner.split()) < MIN_TYPED_WORDS:
                        continue
                    for rid, record in self.quotes.items():
                        if norm(inner) in {norm(gn.quotable_rendering(record)), norm(record.get("text") or "")}:
                            return [{"step": 2, "draft": draft, "record": rid, "with": self.code_sentence(record)}]
            if step >= 3 and why in CITED_QUOTE_REASONS:
                for tag in TAG.findall(draft):
                    if tag in self.quotes:
                        return [{"step": 3, "draft": draft, "record": tag, "with": self.code_sentence(self.quotes[tag])}]
        return []


def run_net(raw, records, thin, text, context, window_end):
    return turn_module.apply_net(
        raw, repository_records=records, thin_topics=thin, quotable_texts=[text], placement=context, window_end=window_end,
    )


def orphans(raw: str, shown: str) -> int:
    """Shipped sentences that open with a pronoun, demonstrative or connective
    right after a sentence that did not ship: the replay report's rule."""
    shown_key = gn.placed_key(shown)
    count = 0
    for paragraph in re.split(r"\n\s*\n", gn.strip_markdown(raw)):
        previous_shipped = True
        for sentence in quote_aware_sentences(paragraph):
            plain = gn.placed_key(gn.strip_tags(MARKER_ID.sub("", sentence))).rstrip(".:;!?, ")
            shipped = bool(plain) and plain in shown_key
            if shipped and not previous_shipped and ORPHAN_OPENERS.match(plain):
                count += 1
            previous_shipped = shipped
    return count


def replay_variant(raw, step, records, thin, text, context, window_end, repairer):
    applied = []
    current = gn.strip_markdown(raw)
    shown, citations, net = run_net(current, records, thin, text, context, window_end)
    for _ in range(MAX_ROUNDS if step else 0):
        if net["reply_shape"]["placed"]:
            break
        fixes = repairer.repairs(net["reply_shape"]["removed"], step)
        if not fixes or fixes[0]["draft"] not in current:
            break
        current = current.replace(fixes[0]["draft"], fixes[0]["with"], 1)
        applied.append(fixes[0])
        shown, citations, net = run_net(current, records, thin, text, context, window_end)
    return {
        "text": shown,
        "removed": [{"why": r["why"], "draft": r["draft"]} for r in net["reply_shape"]["removed"]],
        "placed": net["reply_shape"]["placed"],
        "placed_ok": sum(1 for s in net["sentences"] if s.get("placed_quote") and s["verdict"] == "ok"),
        "orphans": orphans(current, shown),
        "repairs": applied,
    }


def main(fleet_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    registry = load_registry()
    loader = LazyWorldLoader()
    canon_questions = load_fleet_records()
    rows = []
    for world, filename in FILES.items():
        data = json.loads((fleet_dir / filename).read_text(encoding="utf-8"))
        entry = registry[world]
        loaded, _ = loader.load(world, package_dir=ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
        records = ev.repository_records_by_id(loaded.repository)
        thin = ev.thin_topics_for(records)
        window_end = (loaded.frame.get("time_window") or {}).get("end")
        for probe in data["worlds"][world]["per_probe"]:
            raw = probe["transcript"]["raw_text"]
            text = sealed_probes.read_probe(probe["probe_id"])["text"]
            evidence = ev.assemble_evidence(
                message=text, asks=None, canon_questions=canon_questions, coverage=loaded.coverage,
                repository_records=records, thin_topics=thin,
            )
            if loaded.frame.get("story_placement"):
                evidence = with_placeable_stories(evidence, records)
            context = qp.PlacementContext.for_evidence(
                evidence["candidates"], offered_stories=frozenset(c["id"] for c in evidence["candidates"] if c.get("placeable")),
            )
            repairer = Repairer(records, context)
            variants = {step: replay_variant(raw, step, records, thin, text, context, window_end, repairer) for step in (0, 1, 2, 3)}
            rows.append({
                "world": world, "probe": probe["probe_id"], "cell": probe["cell"],
                "shipped": probe["transcript"]["answer_text"],
                "reproduces_shipped": variants[0]["text"] == probe["transcript"]["answer_text"],
                "variants": variants,
            })
    (out_dir / "results.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(rows)} drafts replayed; reproduced: {sum(r['reproduces_shipped'] for r in rows)}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
