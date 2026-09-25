"""The engine-side streaming module (Decision-Log.md Entry 53, "Shape B",
the design of record for participant-facing streaming): buffers the
model's own token stream to sentence boundaries, runs the same
per-sentence grounding check the whole-turn path already runs on each
completed sentence, and yields a cleared sentence immediately. A
sentence that fails the check never reaches this function's own caller
at all - stricter than the whole-turn path's own "checks gate
decoration, never the text" rule (engine.m4.turn.apply_net), and
deliberately so: once a sentence has streamed to a participant it can
never be un-shown, which is exactly why Shape C (raw token streaming
with retraction) was rejected outright in favor of this one. Nothing
here is enforced today - a withheld sentence is silently dropped, not
regenerated - because per-sentence regeneration is its own later,
already-named stage (R27-A moved into per-sentence mode is Stage 7d,
not this one), and R27-A's own enforcement (CIC_R27_ENFORCE) is
currently off by ruling regardless.

Deliberately separate from engine.m4.turn._run_ordinary_voice_turn:
callable, testable, and removable on its own, never woven into the
existing whole-turn path (which this file does not import from and
does not change). Reuses, rather than reimplements, the exact
per-sentence machinery the whole-turn path already runs:
engine.m4.grounding_net.verdict_for_sentence for the grounding check
(identical logic, one already-split sentence at a time instead of a
whole finished text) and engine.m4.transparency_plan.ElementBuilder for
citation-element placement (that class's own docstring already
documents being fed one cleared sentence at a time for exactly this
reason - this module and the whole-turn path produce the same elements
for the same text, which this module's own parity test checks
directly).

SENTENCE BOUNDARIES: the model's token stream arrives as arbitrary
chunks with no sentence structure of their own. This module appends
each chunk to a growing buffer and re-splits the buffer with
engine.prose.quote_aware_sentences (the same splitter grounding_net
itself uses) after every chunk; quote_aware_sentences already merges
text until quotation marks balance, so a chunk boundary landing mid-
quote does not falsely end a sentence early. Every segment the split
returns except the LAST is treated as finished (more text could still
extend that last one); the last segment is re-buffered and re-checked
on the next chunk. When the stream itself ends, whatever remains in the
buffer is the final sentence, checked and (if it clears) emitted like
any other - generation actually stopped there, so there is no "next
chunk" left to wait for.

R30 (Decision-Log, ruled): the opening is held back - buffered and
checked against the seat-identity guard - before anything streams at
all, so a participant can never see a prefix later found to violate it.
`opening_sentence_count` sentences are buffered this way; a guard
failure on the opening triggers exactly one full regeneration (a
second, fresh model call with the violation named in the retry's own
directive - the same one-retry shape the whole-turn path's own
_append_seat_identity_correction already uses, applied here to the
buffered opening instead of a finished answer); a second failure yields
"opening_guard_exhausted" with no sentence ever emitted, for the caller
to substitute a Facilitator turn - the same fallback
seat_identity_guard_exhausted already triggers on the whole-turn path
today. Passing no `guard_labels` (every interview call, matching the
whole-turn path's own convention) skips this check entirely and starts
streaming from the first sentence.

NOT in this module, by design: an HTTP/SSE transport wiring this into
the live API (this file yields plain dicts; the transport and the
question of how to reach it without duplicating
engine.api.wiring.handle_message's own session/evidence-assembly setup
is this change's own open question - see its PR description); self-
revision's own draft-then-revise pair (engine.m4.self_revision) - the
caller runs that first and passes this function whatever it returns,
exactly as that module's own docstring already specifies for 7b/R30
compatibility, since nothing here ever sees the pre-revision draft;
table-round multi-seat streaming (only ever one seat's own voice turn
streams; round/selector mechanics are entirely unchanged and untouched
here); and moving the seat-identity guard itself into genuine
per-sentence mode for every sentence, not just the opening (Stage 7d,
named separately in the recorded build order).
"""
from dataclasses import dataclass
from typing import Iterator

from anthropic import APIError, APITimeoutError

from engine.m4.grounding_net import _TAG, build_figure_lexicon, strip_tags, verdict_for_sentence
from engine.m4.seat_identity_guard import find_seat_identity_violation
from engine.m4.transparency_plan import ElementBuilder
from engine.prose import WITHHOLD_FLOOR, quote_aware_sentences


def _append_opening_guard_correction(turn_directive: str | None, offending_prefix: str) -> str:
    """This module's own one regeneration for a failed opening - same
    wording and the same append-not-replace channel as
    engine.m4.turn._append_seat_identity_correction (that function is
    module-private to turn.py, so this is a small, deliberately-matching
    copy rather than a cross-module import of a private helper)."""
    correction = (
        "\n## Correction (your last attempt failed this)\n"
        f'Your previous answer opened a new line or sentence with "{offending_prefix}" - writing as if you '
        "were the Facilitator or another seat at this Table. You are only ever yourself: answer strictly in "
        "your own voice, with no speaker labels, no \"Name:\" prefixes, and no attributed dialogue for anyone "
        "else at the Table."
    )
    return (turn_directive or "") + correction


@dataclass(frozen=True)
class _RawSentence:
    raw: str  # tag-bearing, exactly as the model wrote it
    text: str  # tag-stripped, participant-facing
    tags: list[str]


def _split_ready(buffer: str) -> tuple[list[_RawSentence], str]:
    """Every sentence quote_aware_sentences finds in `buffer` except the
    last (which may still grow), each parsed into its own tags/text, plus
    the unconsumed remainder to keep buffering. An empty buffer, or a
    buffer holding exactly one still-open sentence, returns ([], buffer)
    unchanged.

    engine.prose.sentences() (which quote_aware_sentences is built on)
    strips each piece and drops the whitespace the split pattern itself
    consumed - summing len(piece) across the ready sentences would not
    land back on the true offset into `buffer`. Locating the still-open
    remainder's own text instead (rfind, since it is the LAST piece and
    a short sentence could legitimately repeat earlier in the buffer)
    sidesteps reconstructing that lost whitespace at all."""
    parts = quote_aware_sentences(buffer)
    if len(parts) < 2:
        return [], buffer
    ready, remainder = parts[:-1], parts[-1]
    sentences_out = [_RawSentence(raw=p, text=strip_tags(p).strip(), tags=_TAG.findall(p)) for p in ready]
    tail_start = buffer.rfind(remainder)
    return sentences_out, buffer[tail_start:] if tail_start != -1 else remainder


def _open_stream(client, model_id, *, system_prompt, directive, message, history, max_tokens, timeout):
    system = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]
    if directive:
        system.append({"type": "text", "text": directive})
    return client.messages.stream(
        model=model_id, max_tokens=max_tokens, system=system,
        messages=[*(history or []), {"role": "user", "content": message}], timeout=timeout,
    )


def stream_voice_turn_sentences(
    client, model_id: str, *,
    system_prompt: str,
    message: str,
    turn_directive: str | None = None,
    history: list[dict] | None = None,
    max_tokens: int = 1024,
    timeout: float = 90.0,
    repository_records: dict[str, dict],
    thin_topics: list[dict] | None = None,
    grounding_floor: float = WITHHOLD_FLOOR,
    world_key: str,
    guard_labels: list[str] | None = None,
    opening_sentence_count: int = 1,
) -> Iterator[dict]:
    """Yields one dict per event, in order:
      {"type": "sentence", "index", "text", "tags", "elements"} - a
        cleared sentence, ready to display and append to the transcript.
      {"type": "opening_guard_retry"} - the opening failed the seat-
        identity guard once; a fresh regeneration is underway. Additive
        signal only, same shape as attempts_meta["r27_regenerated"] on
        the whole-turn path - a caller that ignores it sees only that
        the first "sentence" event arrived a little later.
      {"type": "opening_guard_exhausted"} - the retry's own opening also
        failed; the stream ends here with no "sentence" event ever
        emitted. The caller substitutes a Facilitator turn, the same
        fallback seat_identity_guard_exhausted already triggers today.
      {"type": "done", "answer_text", "citations", "elements"} - the
        finished, participant-facing text (exactly the sentences that
        were actually emitted, joined - never the model's own full raw
        output, which may hold more than what cleared), its per-sentence
        citations (engine.m4.turn.apply_net's own {sentence, record_ids}
        shape) and inline elements (engine.m4.transparency_plan's own
        shape, via the same ElementBuilder the whole-turn path uses).
        Always the last event on a clean stream.
      {"type": "error", "status"} - "timeout" or "error", mirroring
        engine.m5.failure.CallOutcome's own status vocabulary (this
        module raises nothing of its own; a caller that only reads
        "sentence"/"done" events still terminates cleanly on failure,
        the same event ending the generator).

    A withheld sentence (verdict != "ok") is silently dropped - never a
    "sentence" event, never part of answer_text - per this module's own
    docstring on why streaming holds a stricter bar than the whole-turn
    path. guard_labels=None (every interview call) skips the opening
    guard-check and R30 hold entirely; the first sentence streams as
    soon as it clears the grounding check, same as every sentence after
    it."""
    figure_names = build_figure_lexicon(repository_records)

    def _verdict(text: str, tags: list[str]) -> dict:
        return verdict_for_sentence(
            text, tags, repository_records=repository_records, figure_names=figure_names,
            thin_topics=thin_topics, grounding_floor=grounding_floor,
        )

    directive = turn_directive
    for attempt in range(2):  # the opening's own one allowed regeneration (R30)
        try:
            with _open_stream(
                client, model_id, system_prompt=system_prompt, directive=directive,
                message=message, history=history, max_tokens=max_tokens, timeout=timeout,
            ) as stream:
                chunks = stream.text_stream
                buffer = ""
                opening: list[_RawSentence] = []
                opening_checked = guard_labels is None  # nothing to check - skip straight to streaming
                builder = ElementBuilder(repository_records=repository_records, world_key=world_key)
                emitted: list[_RawSentence] = []
                index = 0
                violation: str | None = None

                def _emit_ready(ready: list[_RawSentence]) -> Iterator[dict]:
                    nonlocal index
                    for sent in ready:
                        verdict = _verdict(sent.text, sent.tags)
                        if verdict["verdict"] != "ok":
                            index += 1
                            continue
                        elements = builder.add_sentence(index=index, sentence=sent.text, tags=sent.tags, verdict="ok")
                        emitted.append(sent)
                        yield {"type": "sentence", "index": index, "text": sent.text, "tags": sent.tags, "elements": elements}
                        index += 1

                for chunk in chunks:
                    buffer += chunk
                    ready, buffer = _split_ready(buffer)
                    if not opening_checked:
                        opening.extend(ready)
                        if len(opening) < opening_sentence_count:
                            continue
                        opening_text = "".join(s.text for s in opening)
                        violation = find_seat_identity_violation(opening_text, guard_labels)
                        if violation:
                            break  # abandon this stream entirely - nothing was ever emitted
                        opening_checked = True
                        yield from _emit_ready(opening)
                        opening = []
                        continue
                    yield from _emit_ready(ready)

                if not opening_checked and not violation:
                    # The stream ended before opening_sentence_count
                    # sentences ever accumulated as their own "ready"
                    # piece (a short answer, sometimes just one sentence
                    # total) - _split_ready only ever finalizes a sentence
                    # once something ELSE follows it, so a short answer
                    # can reach here with its entire text still sitting
                    # unchecked in `buffer`. Fold it into the opening
                    # before checking: generation actually stopped there,
                    # so it counts as finished, and this is the only
                    # remaining chance to guard-check it before anything
                    # streams.
                    if buffer.strip():
                        opening.append(_RawSentence(raw=buffer, text=strip_tags(buffer).strip(), tags=_TAG.findall(buffer)))
                        buffer = ""
                    if opening:
                        violation = find_seat_identity_violation("".join(s.text for s in opening), guard_labels)
                        if not violation:
                            yield from _emit_ready(opening)
                    opening_checked = True

                if violation:
                    if attempt == 0:
                        yield {"type": "opening_guard_retry"}
                        directive = _append_opening_guard_correction(turn_directive, violation)
                        continue
                    yield {"type": "opening_guard_exhausted"}
                    return

                if buffer.strip():
                    yield from _emit_ready([_RawSentence(raw=buffer, text=strip_tags(buffer).strip(), tags=_TAG.findall(buffer))])

                # A story's own mark finalizes only once the turn ends
                # without a later sentence continuing it (ElementBuilder's
                # own docstring) - it belongs to no single sentence of its
                # own, so it rides on "done" rather than a fake "sentence"
                # event with nothing in it.
                trailing_elements = builder.finish()

                answer_text = " ".join(s.text for s in emitted)
                citations = [{"sentence": s.text, "record_ids": s.tags} for s in emitted if s.tags]
                yield {"type": "done", "answer_text": answer_text, "citations": citations, "trailing_elements": trailing_elements}
                return
        except APITimeoutError:
            yield {"type": "error", "status": "timeout"}
            return
        except APIError as e:
            yield {"type": "error", "status": "error", "detail": str(e)}
            return
