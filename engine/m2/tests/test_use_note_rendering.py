"""A record's use note rides beside it: in the compiled prompt's section and
on its evidence-block line, with its not-for claims joining the claim guards."""
from engine.m1.loader import load_world_records
from engine.m2 import builders
from engine.m4.evidence import render_evidence_block


def test_the_prompt_section_carries_the_note_beside_the_record():
    records = load_world_records("fix")
    prompt = builders.build_prompt(records, {"display_name": "Testland"}).decode()
    note = records["fix.term.the-three"]["use_note"]
    assert f"Means: {note['means']}" in prompt
    assert "Not for: " + "; ".join(note["not_for"]) in prompt


def test_a_record_without_a_note_renders_as_before():
    assert builders._with_note("Body text.", {"id": "x"}) == "Body text."


def test_the_evidence_line_carries_the_meaning_and_the_not_for_claims():
    block = render_evidence_block({"candidates": [{
        "id": "w.term.a", "record_type": "term", "head": "The Way. More.", "means": "The community's shared life.",
        "claim_guards": ["a formal creed"],
    }], "thin_ground": []})
    assert "| means: The community's shared life." in block
    assert "MUST NOT ASSERT: a formal creed" in block
