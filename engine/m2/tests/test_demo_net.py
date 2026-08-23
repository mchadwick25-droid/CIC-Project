"""Hermetic tests for engine.m2.demo_net - the compile-time check that a
package's own compiled prompt survives the live grounding net.

The check exists because that invariant was asserted in a docstring and
enforced nowhere, and was false: 47 of 377 sentences withheld from the
fleet's own hand-authored demonstrations, and two unsubstituted placeholder
ids in every one of the seven shipped packages.
"""
import json

from engine.m2.demo_net import build_demonstration_net_report, demonstration_net_findings

WITNESS = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "canon_cells": ["C-I"],
    "text": "We did not claim to have seen him ourselves.",
}
REPOSITORY_JSON = json.dumps({"records": [WITNESS]}).encode("utf-8")


def _prompt(body: str) -> bytes:
    return f"## Citation contract\n\nA tag is written [[id]].\n\n{body}\n".encode("utf-8")


CLEAN = _prompt(
    "## Demonstration: fix.demo.c-i\n\n"
    "participant: Who was Jesus?\n"
    "representative: We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
)


def test_a_clean_package_produces_no_findings():
    report = build_demonstration_net_report(CLEAN, REPOSITORY_JSON)
    assert report["pass"] is True
    assert report["findings"] == []
    assert report["withheld_sentence_count"] == 0
    assert report["unresolvable_tag_count"] == 0


def test_the_contracts_own_grammar_illustration_is_not_read_as_a_citation():
    """`[[id]]` in "A tag is the record's own id, written [[id]]" is record-
    authored prose explaining the grammar, not a record to resolve. Every
    real id is dotted; that is what separates them."""
    assert not [f for f in demonstration_net_findings(CLEAN, REPOSITORY_JSON) if f["record_id"] == "id"]


def test_an_unresolvable_tag_is_caught_anywhere_in_the_prompt_not_only_in_demos():
    """The placeholder that cost 46% of live tags lived in the citation
    contract paragraph, outside every demonstration block. A check that
    only walked demos would have missed it completely."""
    prompt = _prompt("## Demonstration: fix.demo.c-i\n\nparticipant: hi\nrepresentative: Nothing here.").replace(
        b"A tag is written [[id]].", b"For example [[world.term.example]]."
    )
    findings = demonstration_net_findings(prompt, REPOSITORY_JSON)
    assert [f["record_id"] for f in findings if f["kind"] == "unresolvable_tag"] == ["world.term.example"]


def test_a_tag_emitted_after_the_terminal_punctuation_is_caught():
    """The original defect, as the gate now sees it: the tag is carried
    onto the next sentence, leaving the claim it belonged to untagged and
    withheld."""
    prompt = _prompt(
        "## Demonstration: fix.demo.c-i\n\n"
        "participant: Who was Jesus?\n"
        "representative: We did not claim to have seen him ourselves. [[fix.witness.who-is-jesus]] "
        "Clement of Alexandria taught in the school."
    )
    findings = demonstration_net_findings(prompt, REPOSITORY_JSON)
    withheld = [f for f in findings if f["kind"] == "withheld_sentence"]
    assert withheld, "a tag after the stop must not pass the gate"
    assert "Clement" in withheld[0]["sentence"] or "seen him ourselves" in withheld[0]["sentence"]


def test_findings_are_stable_across_runs():
    """The compiler is a pure function and this report ships inside the
    package, so it has to be byte-stable or it breaks the determinism
    check."""
    first = build_demonstration_net_report(CLEAN, REPOSITORY_JSON)
    second = build_demonstration_net_report(CLEAN, REPOSITORY_JSON)
    assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)


def test_a_demonstration_with_no_tags_at_all_is_skipped_not_flagged():
    """An untagged demo is a separate, already-known state (several worlds
    have them); this check is about tagged demos disagreeing with the net,
    and must not drown in that other signal."""
    prompt = _prompt(
        "## Demonstration: fix.demo.c-i\n\nparticipant: Who?\nrepresentative: Clement of Alexandria taught here."
    )
    assert [f for f in demonstration_net_findings(prompt, REPOSITORY_JSON) if f["kind"] == "withheld_sentence"] == []
