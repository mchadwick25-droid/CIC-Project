"""The compile-time check that a package's own compiled prompt survives the
LIVE grounding net (engine.m4.grounding_net.check_turn) - the invariant
engine/m2/builders.py's demonstration-tagging note has always asserted
("a demo that would pass its own net if it were live output is exactly the
demo that gets tagged here") and that nothing, until now, ever enforced.

It was false. Run against the seven packages as they shipped on 2026-08-22,
the net withheld 47 of 377 sentences (12.5%) from the fleet's own hand-
authored, correctly-reviewed demonstrations - including BOTH quoted lines of
alx.demo.c-i-who-was-jesus (Clement's New Song, Athanasius's "made man that
we might be made God"), the two lines register statement 6 exists to
protect. Three separate defects, none of them visible from either side
alone, because no one check ever looked at both:

  * tags emitted AFTER the terminal punctuation instead of before it, so
    the live splitter carried every tag onto the following sentence;
  * the citation contract's placeholder ids (`world.term.example`) shipped
    unsubstituted into live model input;
  * quote sentences ranked to a paraphrasing record rather than the record
    holding the quote verbatim.

This module checks the COMPILED BYTES, not a recomputation of them - the
prompt.txt and repository.json that actually ship - so it cannot pass by
agreeing with itself. Pure and deterministic: no wall clock, no randomness,
no model call, same inputs in, same report out, exactly like every other
builder the compiler calls.

Two distinct findings are reported, and they are not the same severity:

  unresolvable_tag - a tag naming a record the package does not contain.
      There is no reading of this that is correct. A placeholder, a typo, or
      a stale id; it withholds its sentence at runtime and, worse, it is
      what the live model imitates.

  withheld_sentence - a demonstration sentence the live net would refuse to
      speak. A real defect in every case measured so far, but the residual
      class after the three fixes above is the compiler and the net
      disagreeing about which sentences NEED a tag, not about the content -
      so it is reported, not silently repaired.
"""
import json
import re

from engine.m4.grounding_net import check_turn

# The live net's own tag grammar, narrowed to a DOTTED id. The citation
# contract's prose illustrates the grammar itself - "A tag is the record's
# own id, written [[id]], with no space inside it" - and that bare `[[id]]`
# is record-authored explanation, not a citation to resolve. Every real
# record id is `world.type.slug`, so requiring a dot separates the two
# without special-casing the sentence it appears in.
_TAG = re.compile(r"\[\[([a-z0-9_-]+(?:\.[a-z0-9_-]+)+)\]\]")
_DEMO_BLOCK = re.compile(r"^## Demonstration: (\S+)\s*$", re.M)
_SPEAKER = re.compile(r"^(participant|representative): ", re.M)


def _repository_by_id(repository_json: bytes) -> dict[str, dict]:
    payload = json.loads(repository_json)
    records = payload.get("records", payload) if isinstance(payload, dict) else payload
    if isinstance(records, dict):
        return records
    return {record["id"]: record for record in records}


def _demonstration_turns(prompt_text: str) -> list[tuple[str, str]]:
    """(demo_id, representative_text) for EVERY representative turn in every
    demonstration, in file order - which is build_prompt's own sorted-by-id
    order, so this is deterministic.

    Sliced between speaker markers rather than matched with one regex from
    the first `representative:` to the end of the block. That earlier shape
    assumed a demonstration has exactly one representative turn, and
    engine/m1/schemas.py's `demonstration.exchange` bounds neither the
    number of turns nor the number of representative turns. Given a legal
    participant/representative/participant/representative exchange it
    swallowed the whole tail, so the literal text "participant: And what
    about Clement?" was handed to check_turn as though the voice had said
    it - producing a withheld_sentence finding against a line no voice ever
    spoke, on a demonstration that is entirely compliant. None of the 52
    demonstrations shipped today has a second representative turn, so it
    was latent rather than live; the schema is what permits it, and the
    schema is what this now follows."""
    out = []
    for match in _DEMO_BLOCK.finditer(prompt_text):
        block = prompt_text[match.end() :]
        next_header = block.find("\n## ")
        if next_header != -1:
            block = block[:next_header]
        marks = list(_SPEAKER.finditer(block))
        for i, mark in enumerate(marks):
            if mark.group(1) != "representative":
                continue
            end = marks[i + 1].start() if i + 1 < len(marks) else len(block)
            turn = block[mark.end() : end].strip()
            if turn:
                out.append((match.group(1), turn))
    return out


def demonstration_net_findings(prompt_txt: bytes, repository_json: bytes) -> list[dict]:
    """Every finding the compiled prompt produces against its own package.
    Sorted for determinism; empty list means the package's own teaching
    surface would survive the net it teaches."""
    prompt_text = prompt_txt.decode("utf-8")
    repository = _repository_by_id(repository_json)
    findings: list[dict] = []

    # 1. Every tag ANYWHERE in the prompt must resolve - not only the ones
    #    inside demonstrations. The placeholder that cost 46% of live tags
    #    lived in the citation contract paragraph, outside every demo.
    for record_id in sorted(set(_TAG.findall(prompt_text))):
        if record_id not in repository:
            findings.append(
                {
                    "kind": "unresolvable_tag",
                    "record_id": record_id,
                    "detail": f"prompt.txt cites [[{record_id}]], which is not a record in this package",
                }
            )

    # 2. Every demonstration must survive the live net verbatim.
    for demo_id, text in _demonstration_turns(prompt_text):
        if "[[" not in text:
            continue
        for sentence in check_turn(text, repository)["sentences"]:
            if sentence["verdict"] == "ok":
                continue
            findings.append(
                {
                    "kind": "withheld_sentence",
                    "demonstration_id": demo_id,
                    "tags": sentence["tags"],
                    "why": sentence["why"],
                    "sentence": sentence["sentence"],
                }
            )
    return findings


class DemonstrationNetFailure(Exception):
    """A compile that would ship a citation the package cannot resolve.

    Raised by compile_world, so the bad package never becomes bytes on
    disk. Scoped to `unresolvable_tag` deliberately, and only that:

      * `unresolvable_tag` has no correct reading. A tag naming a record
        the package does not contain is withheld at runtime AND is what a
        live model imitates - it is how [[world.term.example]] taught seven
        worlds' voices to invent a namespace. Nothing legitimate produces
        one, so nothing legitimate is blocked by refusing it.

      * `withheld_sentence` is reported, and does NOT stop a compile. The
        residual class after the §9.7 fixes is a real content question -
        syr's heresiological sentence has no single record clearing the
        floor, and the honest answer is either a new record or a revised
        sentence, both human decisions. A compiler that refuses to build
        the world until a person makes that call would make the check
        something to switch off rather than something to read.

    The asymmetry is the same one this module's own docstring draws
    between the two finding kinds, now with teeth on the half that has no
    legitimate reading. Whether `withheld_sentence` should ALSO block was
    put to the project lead on PR #24 and RULED, 2026-08-23: it stays a
    read-not-gate signal for now (LIVE-GENERATION-DESIGN.md §9.7 ruling
    7k). Not an oversight, and not a default that drifted into place - a
    decision, with the conditions for revisiting it written down.
    """


def raise_on_unresolvable(report: dict, world_key: str) -> None:
    unresolvable = [f for f in report["findings"] if f["kind"] == "unresolvable_tag"]
    if not unresolvable:
        return
    detail = "; ".join(f["detail"] for f in unresolvable)
    raise DemonstrationNetFailure(
        f"{world_key}: compiled prompt cites {len(unresolvable)} record id(s) this package does not "
        f"contain, so the compile is refused rather than shipped - {detail}"
    )


def build_demonstration_net_report(prompt_txt: bytes, repository_json: bytes) -> dict:
    findings = demonstration_net_findings(prompt_txt, repository_json)
    unresolvable = [f for f in findings if f["kind"] == "unresolvable_tag"]
    withheld = [f for f in findings if f["kind"] == "withheld_sentence"]
    return {
        "pass": not findings,
        "unresolvable_tag_count": len(unresolvable),
        "withheld_sentence_count": len(withheld),
        "findings": findings,
    }
