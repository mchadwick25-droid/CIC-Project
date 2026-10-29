"""Stage 3 stories replay: how the saved drafts of fleet graded run 1 handle
stories today. No model call.

Per world: the stories the evidence offered, the story-tagged and story-marked
sentences in the raw drafts, the stories code placed, the story sentences the
net or placement removed (with reason), the story-tagged sentences that shipped
as the voice's own wording, how many of those restate their record, and the
orphan flags in drafts that lost a story sentence.

Usage: python story_bench.py <dir of the world json files> <out.json>
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE.parent / "S1-L2"))

import bench  # noqa: E402
from engine.m1.loader import load_fleet_records  # noqa: E402
from engine.m1.registry import load_registry  # noqa: E402
from engine.m3 import sealed_probes  # noqa: E402
from engine.m4 import evidence as ev  # noqa: E402
from engine.m4 import grounding_net as gn  # noqa: E402
from engine.m4 import quote_placement as qp  # noqa: E402
from engine.m4.story_placement import STORY_MARKER, with_placeable_stories  # noqa: E402
from engine.m4.world_loader import LazyWorldLoader  # noqa: E402

STORY_REASON = re.compile(r"story|retell", re.IGNORECASE)
WORD = re.compile(r"[a-z']{4,}")


def content_words(text: str) -> set[str]:
    return set(WORD.findall(gn.strip_tags(text).lower()))


def story_text(record: dict) -> str:
    return " ".join(str(record.get(k) or "") for k in ("telling", "tellable_as", "text"))


def main(fleet_dir: Path, out: Path) -> None:
    registry = load_registry()
    loader = LazyWorldLoader()
    canon_questions = load_fleet_records()
    rows = {}
    for world, filename in bench.FILES.items():
        data = json.loads((fleet_dir / filename).read_text(encoding="utf-8"))
        entry = registry[world]
        loaded, _ = loader.load(world, package_dir=ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
        records = ev.repository_records_by_id(loaded.repository)
        stories = {rid for rid, r in records.items() if r.get("record_type") == "story"}
        thin = ev.thin_topics_for(records)
        window_end = (loaded.frame.get("time_window") or {}).get("end")
        stat = Counter(world_stories=len(stories), places_stories=bool(loaded.frame.get("story_placement")))
        reasons = Counter()
        for probe in data["worlds"][world]["per_probe"]:
            raw = probe["transcript"]["raw_text"]
            text = sealed_probes.read_probe(probe["probe_id"])["text"]
            evidence = ev.assemble_evidence(
                message=text, asks=None, canon_questions=canon_questions, coverage=loaded.coverage,
                repository_records=records, thin_topics=thin,
            )
            if loaded.frame.get("story_placement"):
                evidence = with_placeable_stories(evidence, records)
            offered = [c["id"] for c in evidence["candidates"] if c["id"] in stories]
            placeable = [c["id"] for c in evidence["candidates"] if c.get("placeable")]
            context = qp.PlacementContext.for_evidence(evidence["candidates"], offered_stories=frozenset(placeable))
            shown, citations, net = bench.run_net(gn.strip_markdown(raw), records, thin, text, context, window_end)
            sentences = [s for p in re.split(r"\n\s*\n", gn.strip_markdown(raw)) for s in bench.quote_aware_sentences(p)]
            tagged = [s for s in sentences if stories & set(bench.TAG.findall(s)) or STORY_MARKER.search(s)]
            story_cuts = [r for r in net["reply_shape"]["removed"] if STORY_REASON.search(r["why"])]
            placed = [i for i in net["reply_shape"]["placed"] if i in stories]
            shipped_own = [c for c in citations if stories & set(c["record_ids"]) and gn.placed_key(c["sentence"]) not in net_placed(net)]
            restated = 0
            for c in shipped_own:
                tags = stories & set(c["record_ids"])
                source = content_words(" ".join(story_text(records[t]) for t in tags))
                words = content_words(c["sentence"])
                restated += bool(words) and len(words & source) / len(words) >= 0.6
            stat["probes"] += 1
            stat["probes_offered_a_story"] += bool(offered)
            stat["stories_offered"] += len(offered)
            stat["stories_placeable"] += len(placeable)
            stat["draft_story_sentences"] += len(tagged)
            stat["probes_with_a_story_marker"] += bool(STORY_MARKER.search(raw))
            stat["stories_placed_by_code"] += len(placed)
            stat["story_sentences_cut"] += len(story_cuts)
            stat["story_sentences_shipped_as_voice_wording"] += len(shipped_own)
            stat["of_which_restate_their_record"] += restated
            stat["drafts_that_lost_a_story_sentence"] += bool(story_cuts)
            if story_cuts:
                stat["orphan_flags_in_those_drafts"] += bench.orphans(gn.strip_markdown(raw), shown)
            for r in story_cuts:
                reasons[r["why"]] += 1
        rows[world] = {**stat, "cut_reasons": dict(reasons)}
        print(world, rows[world])
    out.write_text(json.dumps(rows, indent=1), encoding="utf-8")


def net_placed(net: dict) -> set[str]:
    return {gn.placed_key(s["sentence"]) for s in net["sentences"] if gn.placed_by_code(s)}


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
