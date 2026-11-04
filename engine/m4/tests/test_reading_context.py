"""The reading context behind the `reading_context` frame flag: off, the
evidence block is today's byte for byte; on, the same records are offered,
each carrying its rendering, card or lens note, and the top two quotes or
stories their context windows, within the 12,000-character budget."""
import dataclasses

import pytest

from engine.m1.loader import RECORDS_ROOT, load_fleet_records
from engine.m1.registry import load_registry
from engine.m3 import protocol, sealed_probes
from engine.m4 import evidence as m4_evidence
from engine.m4 import fit_step, reading_context
from engine.m4.reading_cards import load_reading_context
from engine.m4.story_placement import with_placeable_stories
from engine.m4.turn import apply_net
from engine.m4.world_loader import LazyWorldLoader

WORLD = "alx"
SINGLE_CARD = {
    "setting": "A letter to one friend.",
    "source_says": "He argues that the rite is the sign.",
    "historians_conclude": {"text": "Read as his own teaching.", "confidence": "Widely Accepted"},
    "whose_view": "One author's own view, not the community's.",
    "reads_differently_today": "Today the word sign sounds weaker than he meant.",
    "sources": {"setting": "x", "source_says": "x", "historians_conclude": "x", "whose_view": "x", "reads_differently_today": "x"},
}


@pytest.fixture(scope="module")
def world():
    entry = load_registry()[WORLD]
    from engine.m3.v7_run import REPO_ROOT

    loaded, _ = LazyWorldLoader().load(WORLD, package_dir=REPO_ROOT / entry["package"]["location"],
                                       expected_manifest_hash=entry["package"]["manifest_hash"])
    return loaded


@pytest.fixture(scope="module")
def on(world):
    return dataclasses.replace(world, frame={**world.frame, reading_context.READING_CONTEXT: True})


@pytest.fixture(scope="module")
def records(world):
    return m4_evidence.repository_records_by_id(world.repository)


@pytest.fixture(scope="module")
def reading():
    return load_reading_context(RECORDS_ROOT, WORLD)


@pytest.fixture(scope="module")
def evidences(world, records):
    canon_questions = load_fleet_records()
    thin = m4_evidence.thin_topics_for(records)
    out = []
    for seal in protocol.battery():
        text = sealed_probes.read_probe(seal["probe_id"])["text"]
        turn_evidence = m4_evidence.assemble_evidence(
            message=text, asks=None, canon_questions=canon_questions, coverage=world.coverage, repository_records=records,
            thin_topics=thin,
        )
        if world.frame.get("story_placement"):
            turn_evidence = with_placeable_stories(turn_evidence, records)
        out.append(turn_evidence)
    return out


def _quote(records):
    return next(r for r in records.values() if r["record_type"] == "quote")


def _evidence_for(records, ids):
    return {"candidates": [{"id": rid, "record_type": records[rid]["record_type"], "head": "", "speaker": "S"} for rid in ids],
            "thin_ground": [], "figures_already_named": []}


def test_with_the_flag_off_the_block_is_byte_equal_for_every_alx_probe(world, reading, evidences, monkeypatch):
    assert len(evidences) == 28
    for turn_evidence in evidences:
        today = m4_evidence.render_evidence_block(turn_evidence)
        assert m4_evidence.render_evidence_block(turn_evidence, world=world, reading=reading) == today
        assert m4_evidence.render_evidence_block(turn_evidence, world=world) == today
    monkeypatch.setattr(reading_context, "plan_additions", lambda *a: reading_context.ReadingPlan(guidance=[]))
    for turn_evidence in evidences:
        assert m4_evidence.render_evidence_block(turn_evidence, world=dataclasses.replace(
            world, frame={**world.frame, reading_context.READING_CONTEXT: True})) == m4_evidence.render_evidence_block(turn_evidence)


def test_with_the_flag_on_taking_the_additions_out_gives_today_back(world, on, reading, records, evidences):
    with_renderings = 0
    for turn_evidence in evidences:
        if not turn_evidence["candidates"]:
            continue
        today = m4_evidence.render_evidence_block(turn_evidence)
        block = m4_evidence.render_evidence_block(turn_evidence, world=on, reading=reading)
        plan = reading_context.plan_additions(turn_evidence["candidates"], records, reading)
        assert block.startswith("".join(f"## {line}\n" for line in reading_context.GUIDANCE))
        assert 0 < len(block) - len(today) == plan.chars() <= reading_context.ADDITIONS_CAP
        with_renderings += bool(plan.renderings)
        added = set(plan.guidance) | {line for c in turn_evidence["candidates"] for line in plan.under(c["id"])}
        stripped = "".join(line + "\n" for line in block.splitlines() if line not in added)
        for suffix in plan.renderings.values():
            stripped = stripped.replace(suffix, "", 1)
        assert stripped == today
    assert with_renderings >= 20


def test_the_offered_ids_do_not_depend_on_the_flag(world, on, records):
    from engine.m3.v7_run import V7Answerer

    canon_questions = load_fleet_records()
    seal = protocol.battery()[0]
    text = sealed_probes.read_probe(seal["probe_id"])["text"]
    kwargs = {"canon_questions": canon_questions, "client": None, "model_id": "m", "max_tokens": 1}
    off = V7Answerer(world=world, reading_context=False, **kwargs).prepare(text)
    b = V7Answerer(world=on, reading_context=True, reading={}, **kwargs).prepare(text)
    assert [c["id"] for c in off["turn_evidence"]["candidates"]] == [c["id"] for c in b["turn_evidence"]["candidates"]]


def test_a_quote_with_no_card_shows_its_rendering_and_its_lens_note(on, records):
    quote = _quote(records)
    reading = {quote["id"]: {"reading_card": None, "modern_lens_note": "It meant  more then."}}
    block = m4_evidence.render_evidence_block(_evidence_for(records, [quote["id"]]), world=on, reading=reading)
    (line,) = [line for line in block.splitlines() if line.startswith(f"- [[quote:{quote['id']}]]")]
    assert line.endswith(" | in modern English: " + " ".join(quote["modern_rendering"].split()))
    assert "  Reads differently today: It meant more then." in block.splitlines()


def test_a_lens_note_is_kept_with_the_renderings_when_the_cap_drops_card_lines(on, records, monkeypatch):
    quotes = [rid for rid, r in records.items() if r["record_type"] == "quote"][:3]
    reading = {quotes[0]: {"reading_card": None, "modern_lens_note": "It meant more then."},
               quotes[1]: {"reading_card": SINGLE_CARD, "modern_lens_note": "Not shown."}}
    monkeypatch.setattr(reading_context, "ADDITIONS_CAP", 1)
    plan = reading_context.plan_additions(_evidence_for(records, quotes)["candidates"], records, reading)
    assert not plan.cards and not plan.context
    assert plan.today == {quotes[0]: "  Reads differently today: It meant more then.",
                          quotes[1]: "  Reads differently today: Today the word sign sounds weaker than he meant."}
    summary = plan.summary()
    assert summary["renderings"] == 3 and summary["reads_differently_today"] == 2 and summary["card_lines"] == 0
    assert summary["chars"] == plan.chars()


def test_a_card_gives_its_lines_and_its_reads_differently_today_over_the_lens_note(on, records):
    quote = _quote(records)
    reading = {quote["id"]: {"reading_card": SINGLE_CARD, "modern_lens_note": "The lens note."}}
    lines = m4_evidence.render_evidence_block(_evidence_for(records, [quote["id"]]), world=on, reading=reading).splitlines()
    assert "  Historians conclude (Widely Accepted): Read as his own teaching." in lines
    assert "  Whose view: One author's own view, not the community's." in lines
    assert "  Reads differently today: Today the word sign sounds weaker than he meant." in lines
    assert not any("The lens note." in line for line in lines)


def _texts(tmp_path, records, ids):
    """Each record cites its own fixture text, 600 words long, at lines 300-301."""
    rewritten = {}
    for n, rid in enumerate(ids):
        path = tmp_path / "cic" / "texts" / f"t{n}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(f"line {i} " + "word " * 3 for i in range(1, 601)), encoding="utf-8")
        rewritten[rid] = {**records[rid], "sources": [{"source_id": "s", "locus": f"cic/texts/t{n}.txt, lines 300-301"}]}
    return {**records, **rewritten}


def test_the_cap_holds_dropping_context_first_then_cards_and_keeping_renderings(on, records, tmp_path, monkeypatch):
    cap = reading_context.ADDITIONS_CAP
    assert cap == 12000
    monkeypatch.setattr(reading_context, "TEXTS_ROOT", tmp_path)
    quotes = [rid for rid, r in records.items() if r["record_type"] == "quote"][:8]
    patched = _texts(tmp_path, records, quotes)
    world = dataclasses.replace(on, repository={**on.repository, "records": list(patched.values())})
    long_card = {**SINGLE_CARD, "source_says": "word " * 150}
    reading = {rid: {"reading_card": long_card, "modern_lens_note": None} for rid in quotes}
    evidence = _evidence_for(patched, quotes)

    def plan(cap):
        monkeypatch.setattr(reading_context, "ADDITIONS_CAP", cap)
        return reading_context.plan_additions(evidence["candidates"], patched, reading)

    full = plan(10 ** 9)
    assert list(full.context) == quotes[:2] and list(full.cards) == quotes and list(full.renderings) == quotes
    one_context = plan(full.chars() - 1)
    assert list(one_context.context) == quotes[:1] and list(one_context.cards) == quotes
    context_chars = sum(len(line) + 1 for lines in full.context.values() for line in lines)
    no_context = plan(full.chars() - context_chars)
    assert not no_context.context and list(no_context.cards) == quotes
    fewer_cards = plan(full.chars() - context_chars - 1)
    assert not fewer_cards.context and list(fewer_cards.cards) == quotes[:-1]
    bare = plan(1)
    assert not bare.context and not bare.cards and list(bare.renderings) == quotes and list(bare.today) == quotes
    assert all(line == "  Reads differently today: Today the word sign sounds weaker than he meant." for line in bare.today.values())

    full = plan(cap)
    assert full.chars() <= cap and list(full.renderings) == quotes and list(full.today) == quotes
    assert list(full.cards) == quotes[:len(full.cards)] and list(full.context) == quotes[:len(full.context)]
    assert not full.context or list(full.cards) == quotes
    today = m4_evidence.render_evidence_block(evidence)
    block = m4_evidence.render_evidence_block(evidence, world=world, reading=reading)
    assert len(block) - len(today) == full.chars() <= reading_context.ADDITIONS_CAP
    assert block.count("CONTEXT ctx.") == len(full.context)


def test_context_goes_to_the_top_two_quotes_or_stories_only(on, records, tmp_path, monkeypatch):
    monkeypatch.setattr(reading_context, "TEXTS_ROOT", tmp_path)
    term = next(rid for rid, r in records.items() if r["record_type"] == "term")
    quotes = [rid for rid, r in records.items() if r["record_type"] == "quote"][:3]
    patched = _texts(tmp_path, records, quotes)
    plan = reading_context.plan_additions(_evidence_for(patched, [term, *quotes])["candidates"], patched, {})
    assert list(plan.context) == quotes[:2]
    assert all(line.startswith(f"  CONTEXT {fit_step.CONTEXT_PREFIX}") for lines in plan.context.values() for line in lines)


def test_a_sentence_tagged_to_a_context_id_is_treated_as_one_tagged_to_an_unknown_record(world, records):
    rid = next(rid for rid, r in records.items() if r["record_type"] == "term")
    thin = m4_evidence.thin_topics_for(records)

    def net(tag):
        text, entries, _ = apply_net(f"We read the scriptures together every week. [[{tag}]]", repository_records=records,
                                     thin_topics=thin, quotable_texts=[], window_end=None)
        return text, entries

    context_text, context_entries = net(f"{fit_step.CONTEXT_PREFIX}{rid}.1")
    unknown_text, unknown_entries = net("alx.term.no-such-record")
    assert context_entries == unknown_entries
    assert context_text == unknown_text
    assert not any(e["record_ids"] for e in context_entries if any(i.startswith(fit_step.CONTEXT_PREFIX) for i in e["record_ids"]))


def test_the_signal_counts_a_whole_world_sentence_bound_only_to_single_author_cards():
    reading = {
        "w.quote.one": {"reading_card": SINGLE_CARD, "modern_lens_note": None},
        "w.quote.wide": {"reading_card": {**SINGLE_CARD, "whose_view": "Shared across the churches of Egypt."}, "modern_lens_note": None},
    }
    entries = [
        {"sentence": "We held that the rite is the sign.", "record_ids": ["w.quote.one"]},
        {"sentence": "Our churches kept the fast.", "record_ids": ["w.quote.one", "w.quote.wide"]},
        {"sentence": "He wrote this to a friend.", "record_ids": ["w.quote.one"]},
        {"sentence": "We held it too.", "record_ids": ["w.quote.plain"]},
        {"sentence": "We held it.", "record_ids": []},
    ]
    before = [dict(e) for e in entries]
    signal = reading_context.whole_world_signal(entries, reading)
    assert signal == {"count": 1, "sentences": ["We held that the rite is the sign."]}
    assert entries == before


@pytest.mark.parametrize("view, single", [
    ("Origen's own case, made outside Alexandria; it is not automatically the community's.", True),
    ("A bishop's ruling for all Egypt: the line he drew, not what every congregation read.", True),
    ("One gifted pupil's praise, at Caesarea, not the ordinary student's experience.", True),
    ("Only Dionysius's side survives; Nepos's book is lost.", True),
    ("Origen argues against literal readers in his own church.", True),
    ("Athanasius's wording, but the hope runs through all three main literate authors.", False),
    ("Clement's rhetoric for outsiders. The Logos centre is shared, but only the literate attest it.", False),
    ("A later Alexandrian church headnote, not Athanasius's own words.", False),
    ("A bishop deferring to his people's esteem, against earlier critics.", False),
    ("Remembered by others, not in her words; one of few named women here.", False),
])
def test_the_single_author_marks_read_whose_view_prose(view, single):
    assert reading_context.single_author({"reading_card": {"whose_view": view}}) is single


def test_a_trimmed_window_says_so_to_the_voice():
    whole = {"id": "ctx.w.quote.a.1", "text": "some words", "trimmed": False}
    cut = {**whole, "id": "ctx.w.quote.a.2", "trimmed": True}
    plain, opening = reading_context.window_lines([whole, cut])
    assert plain == fit_step.context_lines({"context": [whole]})[0]
    assert opening.startswith("  CONTEXT ctx.w.quote.a.2, the opening of a longer passage (read to understand")
    assert opening.endswith(": some words")


@pytest.mark.parametrize("view", ["Alexandria's own practice.", "Christians' view in Egypt.", "Egypt's own custom.", "The Church's own ruling."])
def test_a_place_or_group_possessive_is_not_single_author(view):
    assert reading_context.single_author({"reading_card": {"whose_view": view}}) is False

