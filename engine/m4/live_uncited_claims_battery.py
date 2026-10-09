"""The uncited-claims rule's own live measurement: a real, billed live
run measuring the report-only uncited-claims check's actual catch rate
per world, and simulating the enforcement shape battery-only (no
participant path) so the threshold can be set against a
post-regeneration number, not the raw rate. Like engine/m4/live_table_battery.py and
engine/m8/live_cost_run.py, a by-hand, credentialed run - not a CI job.

Interview mode, TWO SEPARATE fresh single-turn sessions per admitted
formation world (not two turns of one session - an earlier run's own
disclosed bug):
  A. A generic in-scope conflict-history ask - the kind of substantive,
     citation-heavy answer the check exists to watch, with no built-in
     bias toward either offense class.
  B. A direct, context-free other-tradition ask: "Use a
     direct first-turn ask that needs no history, the staging one: 'What
     was your relationship with the Donatists?' for alx, and per world a
     named neighbour from the registry." Being turn 1 of its own fresh
     session (not turn 2 riding on turn 1's dangling "this"), the reader
     sees a complete, self-contained other-tradition question and can
     actually fire out_of_scope_class == "other_tradition" - the thing
     an earlier run's own probe never managed.

For every turn that produces at least one offense (after the fixed
exemptions), this simulation regenerates once, in the same turn
(same world, same participant message, same directive, same
is_other_tradition_first_ask), with a correction naming the exact
offending sentences (engine.m4.turn._run_ordinary_voice_turn's new,
opt-in `correction` parameter - unset on every real caller; see that
function's own docstring). Re-check the regenerated answer and report
BOTH the raw and the post-regeneration offense count/rate, per world -
the threshold is meant to be set against that post-regeneration
number; the raw rate is not.

The paragraph-unit numbers the
enforcement threshold is set on, replacing an earlier heuristic substring
metric below with the real mechanism -
engine.m4.grounding_net.check_turn_with_paragraph_coverage and
engine.m4.uncited_claims.find_uncited_paragraphs, called directly here
(battery-only, the same "call the real function a second time on
captured raw text" pattern already used below, now pointed at the
real module instead of a local approximation). Reports, per world: raw
and post-regeneration turn rates by paragraph class
(wholly_uncited_paragraph, inherited_ungrounded), the sentence-level
numbers beside them, how many wholly-uncited paragraphs are exactly
one sentence long, the net's own verdict distribution on inherited
sentences (how many would be withheld under the paragraph-check's
option (a), had it been chosen instead of (b)), and - per world, alx on the Donatists
probe first - whether the B-other-tradition probe's raw answer actually
said the honest-limit rule's own fixed sentence or answered as if it knew.
The correction-and-regenerate simulation now fires on either a
sentence-level or a paragraph-level raw offense (previously sentence-
level only), naming the union of both in the correction, since a
paragraph-unit enforcement would regenerate on either.

SUPERSEDED above: the first, heuristic version of this same idea,
kept only as prior art in this docstring's own history - a sentence
counted as covered when its own paragraph carried a citation tag
ANYWHERE, found by substring match on the raw text rather than the
real net's own paragraph-coverage/inheritance logic. Uses
engine.m4.turn._run_ordinary_voice_turn's own `debug_capture`
parameter to get the real raw tagged text (paragraphs split on blank
lines, same text apply_net itself checks) - no second model call, no
re-derivation; this measurement still keeps this same capture, only
replaces what runs on it.

The flag-gated enforcement mode: `--enforce` runs a SEPARATE, simpler mode (run_enforced
below) against the SAME probes, with the flag actually on
(enforcement on) - a real generation call, one regeneration if a
wholly_uncited_paragraph or neighbour_named offense fires, then the
Facilitator if that survives, exactly as engine.m4.turn's own
enforcement now runs for a real participant. No external correction
loop here (unlike the report-only run() above) - the correction and
the one retry are internal to _run_ordinary_voice_turn itself when
enforcement on, so this mode calls it once per probe, not twice, and
reads the regeneration and exhaustion fields in the result's own
attempts_meta rather than re-deriving them.

Calls engine.m4.turn.run_gate and _run_ordinary_voice_turn directly
(rather than the top-level run_turn) so this script can drive the exact
same voice call twice with an added correction on the second - the same
private-helper-reuse precedent engine.m4.live_table_battery.py already
sets by importing engine.api.wiring._load_world directly rather than
re-deriving world loading.

Plus one small table session (3 worlds, 2 rounds), unchanged from an
earlier run - the table caller path already proved
correct there.

Cost, M8-style (engine.m8.cost, same published rate card
engine.m8.live_cost_run already cites) - reused, not re-priced from
scratch.
"""
import argparse
import json
import sys
import tempfile
from pathlib import Path

from engine.api.table_wiring import continue_table_round, create_table_session, handle_table_message
from engine.m1.registry import load_registry
from engine.m4 import evidence
from engine.m4.grounding_net import check_turn_with_paragraph_coverage
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.turn import _append_r27_correction, _run_ordinary_voice_turn, run_gate
from engine.m4.uncited_claims import R26_HONEST_LIMIT_SENTENCE, build_uncited_claims_event, find_uncited_paragraphs, known_tradition_names
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, PRICE_TABLE_SOURCE, SONNET_4_5_PRICE_TABLE
from engine.m8.log_store import UsageLogStore
from engine.provider import guard
from engine.provider.bedrock import make_client, resolve_model_id

# The two closed paragraph-offense classes (engine.m4.uncited_claims'
# own _PARAGRAPH_OFFENSE_CLASSES) - named here once so every per-world
# and overall tally below is built off the same list, not four separate
# literals that could drift.
_PARAGRAPH_OFFENSE_CLASSES = ("wholly_uncited_paragraph", "inherited_ungrounded")

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = Path(__file__).resolve().parent / "reports" / "live-uncited-claims-battery-report.json"

CONFLICT_TURN = (
    "Tell me about a real conflict or controversy inside your own community's own history - "
    "who was on each side, and how did it end?"
)

# The staging repro sentence, verbatim - reused exactly for alx
# rather than paraphrased, since it is the specific sentence already known
# to matter.
_ALX_STAGING_OTHER_TRADITION_TURN = "What was your relationship with the Donatists?"


def _other_tradition_turn(world_key: str, registry: dict) -> str:
    if world_key == "alx":
        return _ALX_STAGING_OTHER_TRADITION_TURN
    # A real, named neighbour from the registry - a
    # direct, self-contained ask, same "What was your relationship with
    # X?" shape as the alx staging sentence. No inserted "the": a
    # card_name that already carries one ("The Church of the Martyrs")
    # reads correctly bare, and one that doesn't ("Alexandrian
    # Christianity") would read wrong with one added.
    card_names = sorted(
        entry["card_name"]
        for key, entry in registry.items()
        if key != world_key and entry.get("kind") == "formation" and entry.get("card_name")
    )
    return f"What was your relationship with {card_names[0]}?"


def _price_for_call_kind(call_kind: str):
    return HAIKU_4_5_PRICE_TABLE if call_kind in ("safety_call", "reader_call", "turn_selector") else SONNET_4_5_PRICE_TABLE


def _offenses_for(voice_event: dict | None, *, registry: dict, world_key: str, is_other_tradition_turn: bool) -> list[dict]:
    if voice_event is None:
        return []
    event = build_uncited_claims_event(voice_event, registry=registry, is_other_tradition_turn=is_other_tradition_turn)
    return event["offenses"] if event else []


def _paragraph_check(raw_tagged_text: str | None, *, repository_records: dict[str, dict], thin_topics: list[dict] | None) -> dict | None:
    """The real-mechanism replacement for the earlier substring heuristic
    above: the
    real check_turn_with_paragraph_coverage, called directly on the
    captured raw text - the identical function turn.py itself now calls,
    so this battery measures the actual mechanism, not
    an approximation of it. None when there is no raw text to check
    (routing never reached voice)."""
    if not raw_tagged_text:
        return None
    return check_turn_with_paragraph_coverage(raw_tagged_text, repository_records, thin_topics=thin_topics)


def _one_sentence_wholly_uncited_paragraphs(paragraph_check: dict | None) -> int:
    """How many of this turn's own paragraphs are wholly uncited AND
    exactly one sentence long - a shape question about the paragraph
    itself, independent of whether that
    paragraph actually produced a reported offense (an exempt one-
    sentence paragraph - a question, an honest-limit line - still
    counts here)."""
    if paragraph_check is None:
        return 0
    return sum(1 for p in paragraph_check["paragraph_coverage"] if p["wholly_uncited"] and p["sentence_count"] == 1)


def _inherited_verdict_counts(paragraph_check: dict | None) -> dict[str, int]:
    """The net's own verdict distribution on every inherited-check call
    this turn ran (how many would be withheld
    under option (a), had that been chosen over (b) instead) - tallied
    directly off inherited_verdicts, not re-derived."""
    counts = {"ok": 0, "withhold": 0}
    if paragraph_check is None:
        return counts
    for p in paragraph_check["paragraph_coverage"]:
        for verdict in p["inherited_verdicts"].values():
            counts[verdict["verdict"]] = counts.get(verdict["verdict"], 0) + 1
    return counts


def _run_probe_turn(*, client, voice_model_id, safety_model_id, world, world_key, registry, session_id, message, usage_store):
    """run_gate + _run_ordinary_voice_turn directly (module docstring) -
    the same two calls run_turn makes internally for voice_with_directive/
    voice_pass_through, exposed here so the correction regeneration below
    can reuse the identical directive/is_other_tradition_first_ask a
    second time. Returns a dict: raw_offenses, post_regen_offenses,
    raw_paragraph_offenses, post_regen_paragraph_offenses (the
    real paragraph-unit check; None on each *_regen_* key when nothing
    was regenerated), raw_paragraph_check (the full
    check_turn_with_paragraph_coverage result, for the one-sentence-
    paragraph and inherited-verdict-distribution reporting only), plus
    raw_tagged_text, out_of_scope_class, routing_action - usage cost
    already appended to usage_store.

    The regeneration simulation fires on EITHER a raw sentence-level
    offense or a raw paragraph-level one (previously sentence-level
    only) - a paragraph-unit enforcement would regenerate on
    either, and the correction below names the union of both so the
    simulated regeneration sees the same violation list a real
    paragraph-unit enforcement would name."""
    gate_run = run_gate(
        session_id=session_id, safety_client=client, safety_model_id=safety_model_id,
        participant_message=message, pressed={}, anachronistic_term_ids=set(), world_key=world_key,
    )
    for rec in gate_run.usage_records:
        usage_store.append(rec)
    action = gate_run.gate_result.routing.action
    out_of_scope_class = (gate_run.gate_result.routing.out_of_scope_class if action == "voice_with_directive" else None)
    if action not in ("voice_with_directive", "voice_pass_through"):
        return {
            "raw_offenses": [], "post_regen_offenses": None,
            "raw_paragraph_offenses": [], "post_regen_paragraph_offenses": None,
            "raw_paragraph_check": None, "raw_tagged_text": None,
            "out_of_scope_class": out_of_scope_class, "routing_action": action,
        }

    is_other_tradition = out_of_scope_class == "other_tradition"
    repository_records = evidence.repository_records_by_id(world.repository)
    thin_topics = evidence.thin_topics_for(repository_records)

    raw_capture: dict = {}
    voice_event, usage_records = _run_ordinary_voice_turn(
        voice_client=client, voice_model_id=voice_model_id, world=world,
        participant_message=message, directive=gate_run.gate_result.routing.directive,
        session_id=session_id, usage_world_key=world_key, is_other_tradition_first_ask=is_other_tradition,
        debug_capture=raw_capture, sentence_enforce=False,
    )
    for rec in usage_records:
        usage_store.append(rec)
    raw_tagged_text = raw_capture.get("raw_tagged_text")
    raw_offenses = _offenses_for(voice_event, registry=registry, world_key=world_key, is_other_tradition_turn=is_other_tradition)
    raw_paragraph_check = _paragraph_check(raw_tagged_text, repository_records=repository_records, thin_topics=thin_topics)
    raw_paragraph_offenses = find_uncited_paragraphs(raw_paragraph_check) if raw_paragraph_check else []

    post_regen_offenses = None
    post_regen_paragraph_offenses = None
    if raw_offenses or raw_paragraph_offenses:
        # Union, deduplicated by sentence text - a sentence the paragraph
        # check flagged but the base sentence check didn't (or vice
        # versa) still needs naming in the correction.
        seen = {o["sentence"] for o in raw_offenses}
        named = list(raw_offenses) + [o for o in raw_paragraph_offenses if o["sentence"] not in seen]
        regen_capture: dict = {}
        regen_event, regen_usage = _run_ordinary_voice_turn(
            voice_client=client, voice_model_id=voice_model_id, world=world,
            participant_message=message, directive=gate_run.gate_result.routing.directive,
            session_id=session_id, usage_world_key=world_key, is_other_tradition_first_ask=is_other_tradition,
            sentence_enforce=False,
            # `correction=` is appended onto _run_ordinary_voice_turn's own
            # turn_directive internally, so only the suffix is wanted here -
            # _append_r27_correction(None, ...) returns exactly that
            # ("" + suffix). engine.m4.turn._append_r27_correction is the
            # single, canonical owner of this wording now - no
            # local duplicate.
            correction=_append_r27_correction(None, named), debug_capture=regen_capture,
        )
        for rec in regen_usage:
            usage_store.append(rec)
        post_regen_offenses = _offenses_for(regen_event, registry=registry, world_key=world_key, is_other_tradition_turn=is_other_tradition)
        post_regen_paragraph_check = _paragraph_check(regen_capture.get("raw_tagged_text"), repository_records=repository_records, thin_topics=thin_topics)
        post_regen_paragraph_offenses = find_uncited_paragraphs(post_regen_paragraph_check) if post_regen_paragraph_check else []

    return {
        "raw_offenses": raw_offenses, "post_regen_offenses": post_regen_offenses,
        "raw_paragraph_offenses": raw_paragraph_offenses, "post_regen_paragraph_offenses": post_regen_paragraph_offenses,
        "raw_paragraph_check": raw_paragraph_check, "raw_tagged_text": raw_tagged_text,
        "out_of_scope_class": out_of_scope_class, "routing_action": action,
    }


def run(region: str, *, world_keys: list[str], table_world_keys: list[str]) -> dict:
    registry = load_registry()
    loader = LazyWorldLoader()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    per_world = {}
    with tempfile.TemporaryDirectory() as tmp:
        usage_store = UsageLogStore(Path(tmp) / "live-uncited-claims-battery-usage.db")

        for world_key in world_keys:
            entry = registry[world_key]
            world, _timing = loader.load(
                world_key, package_dir=REPO_ROOT / entry["package"]["location"],
                expected_manifest_hash=entry["package"]["manifest_hash"],
            )
            probes = {"A-conflict": CONFLICT_TURN, "B-other-tradition": _other_tradition_turn(world_key, registry)}
            probe_results = {}
            raw_with_offense = post_with_offense = 0
            raw_offense_total = post_offense_total = 0
            probes_run = 0
            # The paragraph-unit tallies, by class
            # (wholly_uncited_paragraph, inherited_ungrounded), raw and
            # post-regeneration - turn counts (a turn counts once per
            # class even if it carries several offenses of that class)
            # and offense totals, the same raw/post-regen split the
            # sentence-level numbers above already use, for direct
            # side-by-side comparison.
            raw_paragraph_turns_by_class = {c: 0 for c in _PARAGRAPH_OFFENSE_CLASSES}
            post_paragraph_turns_by_class = {c: 0 for c in _PARAGRAPH_OFFENSE_CLASSES}
            raw_paragraph_offense_total_by_class = {c: 0 for c in _PARAGRAPH_OFFENSE_CLASSES}
            post_paragraph_offense_total_by_class = {c: 0 for c in _PARAGRAPH_OFFENSE_CLASSES}
            one_sentence_wholly_uncited_paragraphs = 0
            inherited_verdict_counts = {"ok": 0, "withhold": 0}
            # Enforcement-at-the-paragraph-unit simulation: would this
            # turn have regenerated at all (a
            # real raw paragraph-level offense), and would it still have
            # one left for the Facilitator after that one regeneration.
            would_regenerate_turns = 0
            would_reach_facilitator_turns = 0
            other_tradition_said_honest_limit_sentence = None  # bool, set only for B-other-tradition below

            for probe_id, message in probes.items():
                # Each probe is turn 1 of its own fresh session (a direct
                # first-turn ask needing no history) -
                # never the same session_id twice.
                session_id = f"uncited-claims-battery-{world_key}-{probe_id}"
                result = _run_probe_turn(
                    client=client, voice_model_id=voice_model_id, safety_model_id=safety_model_id,
                    world=world, world_key=world_key, registry=registry,
                    session_id=session_id, message=message, usage_store=usage_store,
                )
                raw_offenses, post_offenses = result["raw_offenses"], result["post_regen_offenses"]
                raw_para_offenses = result["raw_paragraph_offenses"]
                post_para_offenses = result["post_regen_paragraph_offenses"]
                raw_paragraph_check = result["raw_paragraph_check"]
                probes_run += 1
                if raw_offenses:
                    raw_with_offense += 1
                    raw_offense_total += len(raw_offenses)
                if post_offenses is not None and post_offenses:
                    post_with_offense += 1
                    post_offense_total += len(post_offenses)

                raw_classes_here = {o["class"] for o in raw_para_offenses}
                for cls in raw_classes_here:
                    raw_paragraph_turns_by_class[cls] += 1
                for o in raw_para_offenses:
                    raw_paragraph_offense_total_by_class[o["class"]] += 1
                # Scoped to raw_para_offenses (the would_regenerate_turns
                # population below), not merely "was regenerated at all" -
                # a turn regenerated only because of a sentence-level raw
                # offense, with no raw paragraph offense, was never part
                # of what a paragraph-unit enforcement would have
                # touched, so its post-regen paragraph classes don't
                # belong in this numerator either (would otherwise
                # outrun would_regenerate_turns, the rate's own
                # denominator below).
                if raw_para_offenses and post_para_offenses is not None:
                    post_classes_here = {o["class"] for o in post_para_offenses}
                    for cls in post_classes_here:
                        post_paragraph_turns_by_class[cls] += 1
                    for o in post_para_offenses:
                        post_paragraph_offense_total_by_class[o["class"]] += 1

                one_sentence_wholly_uncited_paragraphs += _one_sentence_wholly_uncited_paragraphs(raw_paragraph_check)
                turn_inherited_counts = _inherited_verdict_counts(raw_paragraph_check)
                for k, v in turn_inherited_counts.items():
                    inherited_verdict_counts[k] += v

                if raw_para_offenses:
                    would_regenerate_turns += 1
                    if post_para_offenses:
                        would_reach_facilitator_turns += 1

                said_honest_limit = None
                if probe_id == "B-other-tradition":
                    said_honest_limit = bool(result["raw_tagged_text"]) and R26_HONEST_LIMIT_SENTENCE in result["raw_tagged_text"].lower()
                    other_tradition_said_honest_limit_sentence = said_honest_limit

                probe_results[probe_id] = {
                    "message": message,
                    "routing_action": result["routing_action"],
                    "out_of_scope_class": result["out_of_scope_class"],
                    "raw_offenses": raw_offenses,
                    "post_regeneration_offenses": post_offenses,
                    "raw_paragraph_offenses": raw_para_offenses,
                    "post_regeneration_paragraph_offenses": post_para_offenses,
                    **({"said_honest_limit_sentence": said_honest_limit} if probe_id == "B-other-tradition" else {}),
                }

            records = usage_store.read_for_session(f"uncited-claims-battery-{world_key}-A-conflict") + usage_store.read_for_session(
                f"uncited-claims-battery-{world_key}-B-other-tradition"
            )
            session_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in records) if records else 0.0
            per_world[world_key] = {
                "card_name": entry.get("card_name"),
                "probes": probe_results,
                "probes_run": probes_run,
                # Sentence-level numbers, unchanged, kept beside the
                # paragraph-level ones below for direct comparison.
                "raw_turns_with_offense": raw_with_offense,
                "raw_offense_total": raw_offense_total,
                "raw_turn_rate": raw_with_offense / probes_run,
                "post_regeneration_turns_with_offense": post_with_offense,
                "post_regeneration_offense_total": post_offense_total,
                # Denominator is the turns that had a raw offense at all
                # (the ones a regeneration was even attempted on) - a turn
                # with no raw offense was never regenerated and stays
                # clean by construction, not something this rate should
                # dilute.
                "post_regeneration_residual_rate": (post_with_offense / raw_with_offense) if raw_with_offense else 0.0,
                # The paragraph-unit numbers, real mechanism,
                # by class.
                "raw_paragraph_turn_rate_by_class": {c: raw_paragraph_turns_by_class[c] / probes_run for c in _PARAGRAPH_OFFENSE_CLASSES},
                "raw_paragraph_offense_total_by_class": raw_paragraph_offense_total_by_class,
                "post_regeneration_paragraph_turn_rate_by_class": {
                    c: (post_paragraph_turns_by_class[c] / would_regenerate_turns) if would_regenerate_turns else 0.0
                    for c in _PARAGRAPH_OFFENSE_CLASSES
                },
                "post_regeneration_paragraph_offense_total_by_class": post_paragraph_offense_total_by_class,
                "one_sentence_wholly_uncited_paragraphs": one_sentence_wholly_uncited_paragraphs,
                "inherited_verdict_counts": inherited_verdict_counts,
                # The paragraph-unit enforcement simulation itself.
                "paragraph_unit_would_regenerate_turns": would_regenerate_turns,
                "paragraph_unit_would_reach_facilitator_turns": would_reach_facilitator_turns,
                "other_tradition_said_honest_limit_sentence": other_tradition_said_honest_limit_sentence,
                "session_dollars": session_dollars,
            }

        # The table path (the real caller wiring), unchanged from
        # an earlier run - already proven correct there.
        store = Store(Path(tmp) / "live-uncited-claims-battery-events.db")
        table_session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=table_world_keys)
        call_kwargs = dict(
            store=store, usage_store=usage_store, world_loader=loader, registry=registry,
            voice_client=client, voice_model_id=voice_model_id,
            safety_client=client, safety_model_id=safety_model_id, session_id=table_session_id,
        )
        table_turns = []
        for message in (CONFLICT_TURN, f"{registry[table_world_keys[1]].get('representative', {}).get('name')}, what do you make of that?"):
            results = [handle_table_message(**call_kwargs, text=message)]
            while results[-1].round_open:
                results.append(continue_table_round(**{k: v for k, v in call_kwargs.items() if k != "text"}))
            table_turns.extend(results)

        table_state = project_fresh(table_session_id, store)
        table_uncited_events = [e.payload for e in table_state.raw_events if e.event_type == "uncited_claims"]
        table_records = usage_store.read_for_session(table_session_id)
        table_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in table_records) if table_records else 0.0

    total_probes = sum(w["probes_run"] for w in per_world.values())
    total_raw_with_offense = sum(w["raw_turns_with_offense"] for w in per_world.values())
    total_post_with_offense = sum(w["post_regeneration_turns_with_offense"] for w in per_world.values())
    total_dollars = sum(w["session_dollars"] for w in per_world.values()) + table_dollars

    overall_raw_paragraph_turns_by_class = {
        c: sum(round(w["raw_paragraph_turn_rate_by_class"][c] * w["probes_run"]) for w in per_world.values()) for c in _PARAGRAPH_OFFENSE_CLASSES
    }
    overall_raw_paragraph_offense_total_by_class = {
        c: sum(w["raw_paragraph_offense_total_by_class"][c] for w in per_world.values()) for c in _PARAGRAPH_OFFENSE_CLASSES
    }
    overall_post_paragraph_offense_total_by_class = {
        c: sum(w["post_regeneration_paragraph_offense_total_by_class"][c] for w in per_world.values()) for c in _PARAGRAPH_OFFENSE_CLASSES
    }
    total_one_sentence_wholly_uncited_paragraphs = sum(w["one_sentence_wholly_uncited_paragraphs"] for w in per_world.values())
    overall_inherited_verdict_counts = {
        "ok": sum(w["inherited_verdict_counts"]["ok"] for w in per_world.values()),
        "withhold": sum(w["inherited_verdict_counts"]["withhold"] for w in per_world.values()),
    }
    total_would_regenerate = sum(w["paragraph_unit_would_regenerate_turns"] for w in per_world.values())
    total_would_reach_facilitator = sum(w["paragraph_unit_would_reach_facilitator_turns"] for w in per_world.values())

    return {
        "region": region, "voice_model_id": voice_model_id, "safety_model_id": safety_model_id,
        "price_table_source": PRICE_TABLE_SOURCE,
        "interview": {
            "worlds": per_world,
            "overall_probes_run": total_probes,
            # Sentence-level, unchanged.
            "overall_raw_turns_with_offense": total_raw_with_offense,
            "overall_raw_turn_rate": total_raw_with_offense / total_probes if total_probes else 0.0,
            "overall_post_regeneration_turns_with_offense": total_post_with_offense,
            "overall_post_regeneration_residual_rate": (total_post_with_offense / total_raw_with_offense) if total_raw_with_offense else 0.0,
            # The paragraph-unit numbers, real mechanism, by class.
            "overall_raw_paragraph_turn_rate_by_class": {c: overall_raw_paragraph_turns_by_class[c] / total_probes if total_probes else 0.0 for c in _PARAGRAPH_OFFENSE_CLASSES},
            "overall_raw_paragraph_offense_total_by_class": overall_raw_paragraph_offense_total_by_class,
            "overall_post_regeneration_paragraph_offense_total_by_class": overall_post_paragraph_offense_total_by_class,
            "overall_one_sentence_wholly_uncited_paragraphs": total_one_sentence_wholly_uncited_paragraphs,
            "overall_inherited_verdict_counts": overall_inherited_verdict_counts,
            "overall_paragraph_unit_would_regenerate_turns": total_would_regenerate,
            "overall_paragraph_unit_would_regenerate_rate": total_would_regenerate / total_probes if total_probes else 0.0,
            "overall_paragraph_unit_would_reach_facilitator_turns": total_would_reach_facilitator,
            "overall_paragraph_unit_would_reach_facilitator_rate": (total_would_reach_facilitator / total_would_regenerate) if total_would_regenerate else 0.0,
        },
        "table": {
            "world_keys": table_world_keys,
            "session_id": table_session_id,
            "voice_turns": sum(1 for r in table_turns if r.voice),
            "uncited_claims_events": table_uncited_events,
            "session_dollars": table_dollars,
        },
        "total_dollars": total_dollars,
        "note": (
            "Priced against a published rate card, not a reconciled AWS invoice (spec principle 13). "
            "2 fresh single-turn probes per world x 11 worlds (each with a regeneration where the raw probe "
            "had a sentence-level OR paragraph-level offense) + one small table session - an order-of-"
            "magnitude first look, not a statistically powered sample. The paragraph-unit numbers "
            "(raw_paragraph_turn_rate_by_class, post_regeneration_paragraph_turn_rate_by_class, "
            "paragraph_unit_would_regenerate/reach_facilitator_turns), not the sentence-level "
            "post_regeneration_residual_rate, are what the enforcement threshold is meant to "
            "be set against - the sentence-level numbers ride beside them for "
            "comparison only. one_sentence_wholly_uncited_paragraphs and inherited_verdict_counts are "
            "measurement only (the option (a) vs (b) question), and "
            "other_tradition_said_honest_limit_sentence is a per-world, per-probe boolean inside "
            "interview.worlds.<key>.probes['B-other-tradition'], not aggregated here - "
            "alx on the Donatists probe is reported first."
        ),
    }


def run_enforced(region: str, *, world_keys: list[str], table_world_keys: list[str]) -> dict:
    """The flag-gated enforcement mode's own live run: the SAME probes as
    run() above,
    with enforcement actually on - one real generation call per probe
    (not two; the one allowed regeneration is internal to
    _run_ordinary_voice_turn when enforcement on), reporting whether
    it regenerated, whether it reached the Facilitator, and cost. See
    this module's own docstring for the full shape."""
    registry = load_registry()
    loader = LazyWorldLoader()
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    client = make_client(region)

    per_world = {}
    with tempfile.TemporaryDirectory() as tmp:
        usage_store = UsageLogStore(Path(tmp) / "live-uncited-claims-enforced-battery-usage.db")

        for world_key in world_keys:
            entry = registry[world_key]
            world, _timing = loader.load(
                world_key, package_dir=REPO_ROOT / entry["package"]["location"],
                expected_manifest_hash=entry["package"]["manifest_hash"],
            )
            names = known_tradition_names(registry, exclude_world_key=world_key)
            probes = {"A-conflict": CONFLICT_TURN, "B-other-tradition": _other_tradition_turn(world_key, registry)}
            probe_results = {}
            probes_run = regenerated_turns = facilitator_takeover_turns = 0

            for probe_id, message in probes.items():
                session_id = f"uncited-claims-enforced-battery-{world_key}-{probe_id}"
                gate_run = run_gate(
                    session_id=session_id, safety_client=client, safety_model_id=safety_model_id,
                    participant_message=message, pressed={}, anachronistic_term_ids=set(), world_key=world_key,
                )
                for rec in gate_run.usage_records:
                    usage_store.append(rec)
                action = gate_run.gate_result.routing.action
                out_of_scope_class = gate_run.gate_result.routing.out_of_scope_class if action == "voice_with_directive" else None
                probes_run += 1
                if action not in ("voice_with_directive", "voice_pass_through"):
                    probe_results[probe_id] = {"message": message, "routing_action": action, "out_of_scope_class": out_of_scope_class}
                    continue
                is_other_tradition = out_of_scope_class == "other_tradition"
                voice_event, usage_records = _run_ordinary_voice_turn(
                    voice_client=client, voice_model_id=voice_model_id, world=world,
                    participant_message=message, directive=gate_run.gate_result.routing.directive,
                    session_id=session_id, usage_world_key=world_key, is_other_tradition_first_ask=is_other_tradition,
                    r27_enforce=True, known_tradition_names=names, sentence_enforce=False,
                )
                for rec in usage_records:
                    usage_store.append(rec)
                regenerated = bool(voice_event["attempts_meta"]["r27_regenerated"])
                exhausted = bool(voice_event["r27_enforcement_exhausted"])
                if regenerated:
                    regenerated_turns += 1
                if exhausted:
                    facilitator_takeover_turns += 1
                probe_results[probe_id] = {
                    "message": message, "routing_action": action, "out_of_scope_class": out_of_scope_class,
                    "regenerated": regenerated, "facilitator_takeover": exhausted,
                }

            records = usage_store.read_for_session(f"uncited-claims-enforced-battery-{world_key}-A-conflict") + usage_store.read_for_session(
                f"uncited-claims-enforced-battery-{world_key}-B-other-tradition"
            )
            session_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in records) if records else 0.0
            per_world[world_key] = {
                "card_name": entry.get("card_name"), "probes": probe_results, "probes_run": probes_run,
                "regenerated_turns": regenerated_turns, "facilitator_takeover_turns": facilitator_takeover_turns,
                "session_dollars": session_dollars,
            }

        # The table path, enforcement on threaded straight through the
        # same real caller signatures wiring.py/table_wiring.py now
        # accept - no battery-specific table code path, unlike the
        # interview loop above (which calls run_gate/_run_ordinary_voice_
        # turn directly, the same private-helper-reuse precedent this
        # module's own docstring already sets).
        store = Store(Path(tmp) / "live-uncited-claims-enforced-battery-events.db")
        table_session_id, _code = create_table_session(store=store, world_loader=loader, registry=registry, world_keys=table_world_keys)
        call_kwargs = dict(
            store=store, usage_store=usage_store, world_loader=loader, registry=registry,
            voice_client=client, voice_model_id=voice_model_id,
            safety_client=client, safety_model_id=safety_model_id, session_id=table_session_id,
            r27_enforce=True,
        )
        table_turns = []
        for message in (CONFLICT_TURN, f"{registry[table_world_keys[1]].get('representative', {}).get('name')}, what do you make of that?"):
            results = [handle_table_message(**call_kwargs, text=message)]
            while results[-1].round_open:
                results.append(continue_table_round(**{k: v for k, v in call_kwargs.items() if k != "text"}))
            table_turns.extend(results)

        table_voice_turns = [r.voice for r in table_turns if r.voice]
        table_regenerated = sum(1 for v in table_voice_turns if v["attempts_meta"]["r27_regenerated"])
        table_facilitator_takeovers = sum(1 for v in table_voice_turns if v["r27_enforcement_exhausted"])
        table_records = usage_store.read_for_session(table_session_id)
        table_dollars = sum(estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars for r in table_records) if table_records else 0.0

    total_probes = sum(w["probes_run"] for w in per_world.values())
    total_regenerated = sum(w["regenerated_turns"] for w in per_world.values())
    total_facilitator_takeovers = sum(w["facilitator_takeover_turns"] for w in per_world.values())
    total_dollars = sum(w["session_dollars"] for w in per_world.values()) + table_dollars

    return {
        "region": region, "voice_model_id": voice_model_id, "safety_model_id": safety_model_id,
        "price_table_source": PRICE_TABLE_SOURCE, "r27_enforce": True,
        "interview": {
            "worlds": per_world,
            "overall_probes_run": total_probes,
            "overall_regenerated_turns": total_regenerated,
            "overall_regenerated_rate": total_regenerated / total_probes if total_probes else 0.0,
            "overall_facilitator_takeover_turns": total_facilitator_takeovers,
            "overall_facilitator_takeover_rate": (total_facilitator_takeovers / total_regenerated) if total_regenerated else 0.0,
        },
        "table": {
            "world_keys": table_world_keys, "session_id": table_session_id,
            "voice_turns": len(table_voice_turns),
            "regenerated_turns": table_regenerated, "facilitator_takeover_turns": table_facilitator_takeovers,
            "session_dollars": table_dollars,
        },
        "total_dollars": total_dollars,
        "note": (
            "Priced against a published rate card, not a reconciled AWS invoice (spec principle 13). "
            "Real enforcement (CIC_R27_ENFORCE equivalent, r27_enforce=True), same probes as the report-only "
            "run() - 2 fresh single-turn probes per world x 11 worlds + one small table session. "
            "overall_facilitator_takeover_rate is out of overall_regenerated_turns (the turns a regeneration "
            "was even attempted on), not overall_probes_run, same denominator discipline the report-only "
            "run's own post_regeneration_residual_rate already uses. This is a live proof the flag-gated "
            "mechanism works end to end, and a staging look at the numbers before the flag is flipped "
            "anywhere - not a second threshold-setting run."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    guard.add_arguments(parser)
    parser.add_argument("--region", required=True)
    parser.add_argument(
        "--worlds", default="alx,cappadocian,desert,don,gallic,hal,ijc,pahc,rzg,syr,witt",
        help="comma-separated formation world keys (interview mode)",
    )
    parser.add_argument("--table-worlds", default="alx,don,rzg", help="2-3 comma-separated world keys (table mode)")
    parser.add_argument("--out", default=str(REPORT_PATH))
    parser.add_argument(
        "--enforce", action="store_true",
        help="run with r27_enforce=True (run_enforced) instead of the report-only run()",
    )
    args = parser.parse_args()
    world_keys = [k.strip() for k in args.worlds.split(",") if k.strip()]
    table_world_keys = [k.strip() for k in args.table_worlds.split(",") if k.strip()]
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.enforce:
        print(
            f"LIVE, BILLED battery: uncited-claims enforcement (r27_enforce=True), {len(world_keys)} worlds x 2 fresh probes "
            f"+ 1 table session, region {args.region}", flush=True,
        )
        report = run_enforced(args.region, world_keys=world_keys, table_world_keys=table_world_keys)
        out = out.with_name(out.stem + "-enforced" + out.suffix) if out == REPORT_PATH else out
        out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"report written: {out}")
        interview = report["interview"]
        print(
            f"regenerated: {interview['overall_regenerated_rate']:.0%} "
            f"({interview['overall_regenerated_turns']}/{interview['overall_probes_run']}); "
            f"reached Facilitator: {interview['overall_facilitator_takeover_rate']:.0%} "
            f"({interview['overall_facilitator_takeover_turns']}/{interview['overall_regenerated_turns']}); "
            f"table regenerated/takeover: {report['table']['regenerated_turns']}/{report['table']['facilitator_takeover_turns']} "
            f"of {report['table']['voice_turns']} voice turns; "
            f"total cost: ${report['total_dollars']:.4f}"
        )
        return 0

    print(
        f"LIVE, BILLED battery: uncited-claims rate + enforcement simulation, {len(world_keys)} worlds x 2 fresh probes "
        f"+ 1 table session, region {args.region}", flush=True,
    )
    report = run(args.region, world_keys=world_keys, table_world_keys=table_world_keys)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"report written: {out}")
    interview = report["interview"]
    raw_by_class = interview["overall_raw_paragraph_turn_rate_by_class"]
    print(
        f"raw turn rate (sentence): {interview['overall_raw_turn_rate']:.0%} "
        f"({interview['overall_raw_turns_with_offense']}/{interview['overall_probes_run']}); "
        f"post-regen residual (sentence): {interview['overall_post_regeneration_residual_rate']:.0%}; "
        f"raw paragraph turn rate: wholly_uncited_paragraph {raw_by_class['wholly_uncited_paragraph']:.0%}, "
        f"inherited_ungrounded {raw_by_class['inherited_ungrounded']:.0%}; "
        f"paragraph-unit would-regenerate: {interview['overall_paragraph_unit_would_regenerate_rate']:.0%} "
        f"({interview['overall_paragraph_unit_would_regenerate_turns']}/{interview['overall_probes_run']}); "
        f"would reach Facilitator after one regen: {interview['overall_paragraph_unit_would_reach_facilitator_rate']:.0%} "
        f"({interview['overall_paragraph_unit_would_reach_facilitator_turns']}/{interview['overall_paragraph_unit_would_regenerate_turns']}); "
        f"table uncited_claims events: {len(report['table']['uncited_claims_events'])}; "
        f"total cost: ${report['total_dollars']:.4f}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
