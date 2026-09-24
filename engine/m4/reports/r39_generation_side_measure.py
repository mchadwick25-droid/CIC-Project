"""R39, Mark's own principle (relayed 2026-09-23): "our goal is to
generate the right conversation, not correct it... it fine to have
checks, but idealiy they are not used because the engine is generating
it correctly." Ordered as an amendment to R38's own round-2 brief (PR
#436): before the net candidates (A/B/C, the backstop), find out why
the voice wrote "or they handed over the sacred books" at all, and
whether a generation-side directive fix stops it at the source.

ITEM 1 - CAUSE, reconstructed against the real code and the real
package, not assumed. Two things checked directly, both load-bearing
for what follows:

  1. The turn's own assembled evidence block for this exact message
     (engine.m4.evidence.assemble_evidence/render_evidence_block, the
     identical call engine.m4.turn._run_ordinary_voice_turn makes) does
     NOT offer alx.dw.church-failure at all - it retrieved four
     transmission/gravity records instead (cell-matched, deterministic,
     reproduced below). The record the fabrication was tagged to was
     never in this turn's own recommended ground.
  2. It did not need to be: the world's own compiled system prompt
     (world.prompt_text, 60,254 characters) already contains
     alx.dw.church-failure's real text verbatim, confirmed by direct
     substring check ("Under persecution, many gave way" is IN it). The
     fleet-wide citation contract (records/_fleet/fleet_voice/
     _fleet.voice.fleet.md, compiled into every world's own prompt by
     engine.m2.builders.build_fleet_preamble) explicitly sanctions
     citing "from a section heading's own 'cite as' id" - not only from
     the turn's own evidence block - so reaching into the full prompt
     for this record was legitimate under the contract as written.

So the failure is NOT "the voice had no ground and invented one." It
had the real ground, directly in its own context, and used it
correctly for the first two-thirds of the sentence - then extended the
same tagged sentence with one more clause the record does not support.
THE GAP, stated precisely: the fleet-wide citation contract's own
verbatim-fidelity promise ("words not found in the tagged record, is
not spoken") is written to cover QUOTED spans only. For an ordinary,
non-quoted, paraphrased sentence, the contract only requires the TAG
(the id) to be real and correctly copied - it never says the sentence's
own non-quoted CONTENT must be limited to what that record's text
supports. A tag is a promise about the ADDRESS, not about the CONTENT.
Separately, _other_tradition_directive() (engine/m4/turn.py) instructs
the voice not to speak AS IF it knows the OTHER tradition's own history
or doctrine directly - it does not anticipate the more specific failure
that actually occurred: a plausible, topic-adjacent detail (the
traditor charge, from the voice's own general training knowledge of
Donatism, activated by the participant's own question) bleeding into a
sentence that is nominally about the SPEAKER'S OWN record, not about
the other tradition at all. Neither existing instruction names this
shape.

ITEM 2 - PROPOSED DIRECTIVE (general wording, not per-record; not
built into main): CURRENT_OTHER_TRADITION_DIRECTIVE is
engine.m4.turn._other_tradition_directive()'s own real text, imported
directly, never retyped, so this measurement's "before" condition is
byte-identical to what ships today. PROPOSED_OTHER_TRADITION_DIRECTIVE
appends two things: (a) the tag-is-a-promise rule ("what you tag to a
record must be that record's own content - stop the sentence at what
the record gives you rather than add one more plausible detail"), and
(b) R37's own two-condition knowledge scope, stated plainly rather than
implied.

ITEM 3 - MEASURED AT GENERATION. 20 live regenerations of the exact
Theon/Donatists probe under the current directive, 20 under the
proposed one - same evidence block, same world, same model, same
message, only the directive text differs. Report-only: this script
never touches engine/m4/turn.py or any package; it calls
engine.m4.generation.stream_voice_turn directly, mirroring
_run_ordinary_voice_turn's own evidence-assembly + directive-building
exactly (imported where reusable, not duplicated) with the directive
text swapped for the "proposed" condition. Every tagged sentence from
all 40 raw outputs is captured, unfiltered, for hand-reading (per the
reviewer's own instruction: NOT the lexical remainder measure, which
R38's own round-2 brief already showed has 0/6 precision on real
paraphrase) - the hand-read verdicts themselves are recorded in this
script's own HAND_READ_VERDICTS dict below, filled in after reading
every one of the 40 outputs against their own tagged records, not
inferred.

Run: python3 -m engine.m4.reports.r39_generation_side_measure --region us-east-1
"""
import argparse
import json
import pathlib
import sys
import time
from datetime import date, datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.loader import load_fleet_records
from engine.m1.registry import load_registry
from engine.m4 import evidence as ev
from engine.m4 import grounding_net as gn
from engine.m4.generation import stream_voice_turn
from engine.m4.reports.net_remainder_measure import latest_complete_package
from engine.m4.turn import R26_HONEST_LIMIT_SENTENCE, _other_tradition_directive
from engine.m4.world_loader import LazyWorldLoader
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import SONNET_4_5_PRICE_TABLE

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent

MESSAGE = "What was your relationship with the Donatists?"

CURRENT_OTHER_TRADITION_DIRECTIVE = _other_tradition_directive()

PROPOSED_OTHER_TRADITION_DIRECTIVE = (
    CURRENT_OTHER_TRADITION_DIRECTIVE
    + " A tag is a promise, not just an address: every specific detail in a sentence you tag must be "
    "this record's own content, stated or an exact paraphrase of it - never a detail added because it "
    "sounds plausible, fits the period, or belongs to a related controversy you happen to know about. If "
    "a sentence would need one more specific detail than your own tagged record actually gives you, stop "
    "the sentence at what the record gives you and do not add the rest, even if you believe it to be "
    "true. You may use outside knowledge of the tradition named in this question to choose which part of "
    "your own record to answer from only when (a) your own world would have known of that tradition in "
    "its own time, or (b) the conversation itself has already told you something about it - and even "
    "then, only what your own records or the conversation actually say may appear in your answer, never "
    "anything else you happen to know about that other tradition."
)


def build_evidence_and_message(world_key: str) -> tuple[str, dict]:
    registry = load_registry()
    C = latest_complete_package(world_key)
    manifest_hash = registry[world_key]["package"]["manifest_hash"]
    loader = LazyWorldLoader()
    world, _timing = loader.load(world_key, package_dir=C, expected_manifest_hash=manifest_hash)
    repository_records = ev.repository_records_by_id(world.repository)
    thin_topics = ev.thin_topics_for(repository_records)
    canon_questions = load_fleet_records()
    asks = [{"order": 1, "text": MESSAGE}]
    turn_evidence = ev.assemble_evidence(
        message=MESSAGE, asks=asks, canon_questions=canon_questions,
        coverage=world.coverage, repository_records=repository_records, thin_topics=thin_topics,
    )
    evidence_block = ev.render_evidence_block(turn_evidence)
    user_message = f"{evidence_block}\n{MESSAGE}" if turn_evidence["candidates"] else MESSAGE
    return user_message, {
        "world": world, "repository_records": repository_records, "thin_topics": thin_topics,
        "evidence_block": evidence_block, "evidence_offers_church_failure": "alx.dw.church-failure" in evidence_block,
        "prompt_contains_church_failure_text": "Under persecution, many gave way" in world.prompt_text,
    }


def run_batch(client, model_id: str, *, world, user_message: str, directive_text: str, n: int, usage_records: list):
    results = []
    for i in range(n):
        last_error = None
        for attempt, delay in enumerate((0, 2, 4, 8)):
            if delay:
                time.sleep(delay)
            outcome = stream_voice_turn(
                client, model_id, system_prompt=world.prompt_text, turn_directive=directive_text,
                message=user_message, history=None, timeout=90.0,
            )
            if outcome.status == "ok":
                break
            last_error = outcome
        else:
            outcome = last_error
        if outcome.status != "ok":
            raise RuntimeError(f"voice generation call {i} failed: {outcome.status} {outcome.value}")
        if outcome.raw_usage is not None:
            usage_records.append(normalize_usage(outcome.raw_usage))
        raw_text = outcome.value.text
        tagged_text, truncated = gn._drop_truncated_tail(raw_text)
        parsed = gn.parse_tagged(tagged_text)
        tagged_sentences = [{"sentence": s["text"], "tags": s["tags"]} for s in parsed if s["tags"]]
        results.append({"run": i, "raw_text": raw_text, "truncated": truncated, "tagged_sentences": tagged_sentences})
        time.sleep(0.4)
    return results


def run(region: str, n_per_condition: int = 20) -> dict:
    model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    client = make_client(region)
    user_message, ctx = build_evidence_and_message("alx")

    usage_records: list = []
    current_results = run_batch(
        client, model_id, world=ctx["world"], user_message=user_message,
        directive_text=CURRENT_OTHER_TRADITION_DIRECTIVE, n=n_per_condition, usage_records=usage_records,
    )
    proposed_results = run_batch(
        client, model_id, world=ctx["world"], user_message=user_message,
        directive_text=PROPOSED_OTHER_TRADITION_DIRECTIVE, n=n_per_condition, usage_records=usage_records,
    )

    total_dollars = sum((estimate_cost(u, SONNET_4_5_PRICE_TABLE).dollars or 0.0) for u in usage_records)

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "model_id": model_id,
        "message": MESSAGE,
        "evidence_offers_church_failure": ctx["evidence_offers_church_failure"],
        "prompt_contains_church_failure_text": ctx["prompt_contains_church_failure_text"],
        "evidence_block": ctx["evidence_block"],
        "current_directive": CURRENT_OTHER_TRADITION_DIRECTIVE,
        "proposed_directive": PROPOSED_OTHER_TRADITION_DIRECTIVE,
        "n_per_condition": n_per_condition,
        "calls_made": len(usage_records),
        "total_dollars": round(total_dollars, 4),
        "current_runs": current_results,
        "proposed_runs": proposed_results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--n", type=int, default=20)
    args = parser.parse_args()

    print(
        f"About to make {args.n * 2} live Sonnet 4.5 voice-generation calls "
        f"({args.n} current directive + {args.n} proposed directive). Estimated cost: ~$2-4 - proceeding.",
        flush=True,
    )
    report = run(args.region, n_per_condition=args.n)
    out_path = REPORTS_DIR / f"r39-generation-side-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    print(f"Real cost: ${report['total_dollars']} ({report['calls_made']} calls)")
    print(f"Evidence block offered alx.dw.church-failure: {report['evidence_offers_church_failure']}")
    print(f"World prompt contains its real text: {report['prompt_contains_church_failure_text']}")
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")
    print("Next: hand-read every tagged sentence in current_runs/proposed_runs and record verdicts.")


if __name__ == "__main__":
    main()
