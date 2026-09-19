"""The engine-owned Transparency Plan (Build-Plan.md Stage 3a): one
complete, deterministic list of every record a turn actually cited,
computed once here instead of left for the frontend to reconstruct with
its own dedup rules.

**The defect this closes.** `citations` (engine.m4.turn.apply_net) is
per-sentence: `{sentence, record_ids, sources}`, one entry per surviving,
verified sentence. `VoiceTurnBody.tsx` turns that into inline marks by
finding each contiguous run of sentences citing the same story/witness
record and placing one mark at the run's end - correct for the first run.
A second, non-consecutive citation of the same record later in the same
turn has nowhere to go: `renderedStoryIds`/`renderedWitnessIds` (that
component's own turn-scoped dedup sets) suppress a second inline mark,
which is the right call, but story/witness sources are never passed to
`addReference` (only `otherSources` is) - so the second citation's
sourcing is silently dropped, not moved to General References. A
participant reads a sentence built on a real, verified record with no
mark anywhere near it, in a turn where that exact record already has a
mark - just earlier, and easy to miss as belonging to this later claim.

**The fix.** `references` below is built to make that structurally
impossible: every `record_id` appearing anywhere in `citations` appears
in `references` exactly once, by construction - not by the renderer
remembering to call a fallback. `set(r["record_id"] for r in references)
== set(rid for c in citations for rid in c["record_ids"])` holds for any
input, which is this module's own completeness-invariant test. Whatever
the renderer decides to do with a repeat (Rulings-Pending.md R10 -
inline "ibid" glyph, general-references-only, or something else) is a
later, separately-ruled decision; this module guarantees the data is
never lost regardless of which way that ruling goes.

**Anchors.** One entry per contiguous run of citation-list positions that
all name the same `record_id` - `run_start_sentence`/`run_end_sentence`
are indexes into the `citations` list (not character offsets: citations
already carry sentence *text*, not spans, and this module adds nothing
that would require re-finding it in the raw answer). A record's second or
later run in the same turn carries `repeat: true`. Each anchor is
single-record on purpose: a citation entry can name more than one
`record_id` (a sentence citing two records at once), and collapsing that
into one multi-record anchor would have to invent an ordering or a
"weakest confidence" aggregation rule nothing has actually ruled on yet
(see Rulings-Pending.md's open items) - safer to keep every anchor
traceable to exactly one record and let a future ruling decide how the
renderer groups same-sentence anchors, than to bake an unruled aggregation
choice into the data shape now.

**Confidence.** Each anchor and reference carries the cited record's own
`confidence` envelope field verbatim (`citation_specificity`,
`verification_state`, `evidentiary_weight`, `formation_confidence`,
`divergence_note`) when the record has one - computed and attached, never
rendered by anything in this module. Whether/how a participant ever sees
it is Stage 6, gated on Mark's own ruling (R9) and the D1 grounding
measurement (Stage 1) landing first.

**unverified_claims** is a plain count plus which `net_result["sentences"]`
indexes failed verification - for M7's own reporting, never for a
participant. Opus finding D3: the project's own measurement found most
withheld sentences are honest prose the check was merely uncertain about,
so a count implying "N unverifiable claims" would itself mislead. This
field exists so that measurement can keep happening; nothing renders it.

Additive only: stored as `voice_event["transparency"]`, never added to
`engine.m4.events.REQUIRED_KEYS["voice_turn"]`. `citations` itself,
`apply_net`, and `_replay_text` are untouched - this module only reads
their output after the fact and does not feed back into anything upstream.
"""
from __future__ import annotations

from engine.m4.citation_cards import resolve_source_card


def build_transparency_plan(
    *,
    citations: list[dict],
    net_result: dict,
    repository_records: dict[str, dict],
    world_key: str,
) -> dict:
    """citations: engine.m4.turn.apply_net's per-sentence output, already
    carrying resolved `sources` (engine.m4.citation_cards.
    resolve_citation_sources) - this function does not re-resolve them,
    only groups the record_ids and rebuilds one deduped card per id via
    resolve_source_card (cheap: a dict lookup and a label lookup, not a
    second pass over the corpus). net_result: engine.m4.turn.apply_net's
    third return value, read only for unverified_claims. Deterministic:
    identical input always produces identical output, byte for byte."""
    seen_order: list[str] = []
    seen_set: set[str] = set()
    runs_by_record: dict[str, list[list[int]]] = {}

    for idx, citation in enumerate(citations):
        for record_id in citation.get("record_ids") or []:
            if record_id not in seen_set:
                seen_set.add(record_id)
                seen_order.append(record_id)
            runs = runs_by_record.setdefault(record_id, [])
            if runs and runs[-1][1] == idx - 1:
                runs[-1][1] = idx
            else:
                runs.append([idx, idx])

    anchors = []
    for record_id in seen_order:
        record = repository_records.get(record_id) or {}
        for run_index, (start, end) in enumerate(runs_by_record[record_id]):
            anchors.append({
                "record_id": record_id,
                "record_type": record.get("record_type"),
                "world_key": world_key,
                "run_start_sentence": start,
                "run_end_sentence": end,
                "repeat": run_index > 0,
                "confidence": record.get("confidence"),
            })

    references = []
    for record_id in seen_order:
        card = resolve_source_card(record_id, repository_records)
        if card is None:
            continue
        card = {**card, "world_key": world_key, "confidence": (repository_records.get(record_id) or {}).get("confidence")}
        references.append(card)

    unverified_sentences = [
        i for i, s in enumerate(net_result.get("sentences") or []) if s.get("verdict") != "ok"
    ]

    return {
        "world_key": world_key,
        "anchors": anchors,
        "references": references,
        "unverified_claims": {"count": len(unverified_sentences), "sentence_indexes": unverified_sentences},
    }
