"""A participant never reads a reply that is broken because sentences were
cut out of it. Each case is a real reply shape, in the voice's own words: a
sentence the net flags, and a sentence beside it that leans on it. Cutting
the flagged one leaves the other pointing at nothing. The one regeneration
is a rewrite of the voice's own answer that mends what leaned on the
flagged material; a rewrite that still carries a flagged sentence is set
aside for the Facilitator's line, never shown cut. Fake clients only."""
import pytest

from engine.m4 import grounding_net
from engine.m4.tests.test_turn import FakeBedrockClient, _directive_text, _reader, _safety
from engine.m4.turn import apply_net, run_voice_turn_for_world
from engine.m4.world_loader import LoadedWorld

RID = "fix.witness.w"
QUOTE_RID = "fix.quote.creed"

# (sentences kept, each tagged to the world's one witness record; the
# flagged sentence; where it sits among the kept ones; a whole rewrite
# without it)
CASES = {
    "alx-t6-both-were-real": (
        [
            "What reached everyone was the water and the table: baptism, the bread and cup, the calendar.",
            "Those asked nothing of letters.",
            "Both were real.",
            "Both mattered.",
        ],
        "The depth-formation Gregory walked belonged to the few who could read and argue.",
        0,
        "What reached everyone was the water and the table: baptism, the bread and cup, the calendar [[fix.witness.w]]. "
        "Those asked nothing of letters [[fix.witness.w]].",
    ),
    "alx-t4-that-was-the-deposit": (
        ["That was the deposit we were given to keep.", "We inherited him."],
        "The apostles handed it down: baptism into Father, Son, and Holy Spirit, the bread broken, the scriptures read, "
        "the teaching given to those being formed.",
        0,
        "We were given a deposit to keep [[fix.witness.w]]. We inherited him [[fix.witness.w]].",
    ),
    "ijc-t4-that-is-a-bishop": (
        [
            "A century of councils spent itself making the words exact because everything hung on them.",
            "That is a bishop putting his standing on the line over one word's exactness.",
        ],
        "Eusebius of Caesarea hesitated at Nicaea over the word homoousios, thought it through, and signed - then "
        "wrote home to explain himself, so no one would question his motives.",
        1,
        "A century of councils spent itself making the words exact because everything hung on them [[fix.witness.w]].",
    ),
    "ijc-t1-our-creed-answers-first": (
        [
            "Our own creed, the one from Nicaea in 325, answers first.",
            "A century of councils spent itself making those words exact, because everything hung on them.",
        ],
        "In substance it says: very God of very God, of one substance with the Father, who for us men and for our "
        "salvation came down and was made man; he suffered, and the third day he rose again.",
        1,
        "A century of councils spent itself making those words exact, because everything hung on them [[fix.witness.w]].",
    ),
    "cappadocian-t5-cost-him-a-friendship": (
        [
            "Basil lived it, and it cost him a friendship.",
            "Both sides loved the same Spirit.",
            "And underneath the argument lay a wound that never healed in our years.",
        ],
        "The teacher from whom many of us first learned the whole ordered life -- Eustathius of Sebaste -- became our "
        "adversary over this same Spirit.",
        2,
        "Basil lived it [[fix.witness.w]]. Both sides loved the same Spirit [[fix.witness.w]].",
    ),
}


def _world(kept):
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [
            {"id": RID, "record_type": "doctrinal_witness", "text": " ".join(kept)},
            {"id": QUOTE_RID, "record_type": "quote", "speaker_or_author": "fix.figure.council",
             "modern_rendering": "We believe in one God."},
        ]},
        quotes={"quotes": []},
        figures={},
        coverage={},
        frame={"representative": {"name": "Vera", "role_label": "Witness"}},
    )


def _tagged(sentence, rid=RID):
    return f"{sentence[:-1]} [[{rid}]]{sentence[-1]}"


def _draft(name):
    kept, cut, at, _rewrite = CASES[name]
    if name.startswith("ijc-t1"):
        cut = _tagged(cut, QUOTE_RID)  # tagged to a quote record that is never placed
    tagged = [_tagged(s) for s in kept]
    return " ".join(tagged[:at] + [cut] + tagged[at:])


def _turn(name, scripts):
    kept = CASES[name][0]
    client = FakeBedrockClient(safety_response=_safety(), reader_response=_reader(), stream_scripts=scripts)
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(kept),
        participant_message="who was Jesus", directive=None, session_id="test-session",
    )
    return voice_event, client


@pytest.mark.parametrize("name", list(CASES))
def test_cutting_the_flagged_sentence_leaves_the_broken_reply_the_re_reading_showed(name):
    """The hazard itself: the flagged sentence cut out of this reply leaves
    exactly the kept sentences, one of which leans on what was cut, as the
    reply a participant would have read."""
    kept, cut, _at, _rewrite = CASES[name]
    records = {r["id"]: r for r in _world(kept).repository["records"]}
    shown, _citations, _net_result = apply_net(
        grounding_net.drop_flagged_sentences(_draft(name), {cut}), repository_records=records, thin_topics=None,
    )
    assert shown == " ".join(kept)


@pytest.mark.parametrize("name", list(CASES))
def test_a_rewrite_still_carrying_the_flagged_sentence_is_set_aside_not_cut(name):
    kept, cut, _at, _rewrite = CASES[name]
    draft = _draft(name)
    voice_event, client = _turn(name, [[draft], [draft]])
    assert len(client.messages.captured_stream_calls) == 2  # one regeneration, never a second
    assert voice_event["sentence_enforcement"]["flagged"] == [cut]
    assert voice_event["sentence_enforcement"]["still_flagged"] == [cut]
    assert voice_event["sentence_enforcement_exhausted"] is True
    assert voice_event["text"] == ""
    assert voice_event["citations"] == []


@pytest.mark.parametrize("name", list(CASES))
def test_a_whole_rewrite_without_the_flagged_sentence_is_shown_as_written(name):
    _kept, cut, _at, rewrite = CASES[name]
    voice_event, client = _turn(name, [[_draft(name)], [rewrite]])
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["sentence_enforcement"]["still_flagged"] == []
    assert voice_event["sentence_enforcement_exhausted"] is False
    assert voice_event["text"] == grounding_net.strip_tags(rewrite)


@pytest.mark.parametrize("name", list(CASES))
def test_the_one_regeneration_asks_for_a_whole_rewrite_of_the_voices_own_answer(name):
    _kept, cut, _at, rewrite = CASES[name]
    draft = _draft(name)
    _voice_event, client = _turn(name, [[draft], [rewrite]])
    retry_system, _messages = client.messages.captured_stream_calls[1]
    directive = _directive_text(retry_system)
    assert f'"{cut}"' in directive  # the flagged sentence, named
    assert f"YOUR LAST ANSWER:\n{draft}" in directive  # the voice's own answer, given back whole, tags and all
    assert "mend every sentence that introduced, pointed back to, counted on or finished what you took out" in directive
    first_system, _m = client.messages.captured_stream_calls[0]
    assert "YOUR LAST ANSWER" not in _directive_text(first_system)


def test_a_clean_reply_makes_no_extra_call_and_is_shown_whole():
    name = "ijc-t4-that-is-a-bishop"
    whole = " ".join(_tagged(s) for s in CASES[name][0])
    voice_event, client = _turn(name, [[whole]])
    assert len(client.messages.captured_stream_calls) == 1
    assert voice_event["sentence_enforcement"]["regenerated"] is False
    assert voice_event["text"] == " ".join(CASES[name][0])
