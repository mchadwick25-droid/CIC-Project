"""What a participant reads when the net flags sentences in a real reply
shape, in the voice's own words. Nothing is regenerated. A quotation the
voice gave on its own, or a quote marker the turn did not offer, is cut with
its lead-in, and a sentence beside it that pointed back stays as written. Any
other flagged sentence is shown as written. Fake clients only."""
import pytest

from engine.m4 import grounding_net
from engine.m4.tests.test_turn import FakeBedrockClient, _directive_text, _reader, _safety
from engine.m4.turn import apply_net, run_voice_turn_for_world
from engine.m4.world_loader import LoadedWorld

RID = "fix.witness.w"
QUOTE_RID = "fix.quote.creed"

# (sentences kept, each tagged to the world's one witness record; the
# flagged sentence; where it sits among the kept ones)
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
    ),
    "alx-t4-that-was-the-deposit": (
        ["That was the deposit we were given to keep.", "We inherited him."],
        "The apostles handed it down: baptism into Father, Son, and Holy Spirit, the bread broken, the scriptures read, "
        "the teaching given to those being formed.",
        0,
    ),
    "ijc-t4-that-is-a-bishop": (
        [
            "A century of councils spent itself making the words exact because everything hung on them.",
            "That is a bishop putting his standing on the line over one word's exactness.",
        ],
        "Eusebius of Caesarea hesitated at Nicaea over the word homoousios, thought it through, and signed - then "
        "wrote home to explain himself, so no one would question his motives.",
        1,
    ),
    "ijc-t1-our-creed-answers-first": (
        [
            "Our own creed, the one from Nicaea in 325, answers first.",
            "A century of councils spent itself making those words exact, because everything hung on them.",
        ],
        "In substance it says: very God of very God, of one substance with the Father, who for us men and for our "
        "salvation came down and was made man; he suffered, and the third day he rose again.",
        1,
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


def _cut_as_written(name):
    cut = CASES[name][1]
    if name.startswith("ijc-t1"):
        return _tagged(cut, QUOTE_RID)  # tagged to a quote record that is never placed
    return cut


def _draft(name):
    kept, _cut, at = CASES[name]
    tagged = [_tagged(s) for s in kept]
    return " ".join(tagged[:at] + [_cut_as_written(name)] + tagged[at:])


def _turn(name, scripts):
    kept = CASES[name][0]
    client = FakeBedrockClient(safety_response=_safety(), reader_response=_reader(), stream_scripts=scripts)
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(kept),
        participant_message="who was Jesus", directive=None, session_id="test-session",
    )
    return voice_event, client


@pytest.mark.parametrize("name", list(CASES))
def test_one_call_shows_the_reply_with_only_a_quotation_cut(name):
    kept, _cut, _at = CASES[name]
    draft = _draft(name)
    voice_event, client = _turn(name, [[draft]])
    assert len(client.messages.captured_stream_calls) == 1
    expected = " ".join(kept) if name.startswith("ijc-t1") else grounding_net.strip_tags(draft)
    assert voice_event["text"] == expected
    assert voice_event["answer_record_fallback"] is None


def test_a_clean_reply_makes_no_extra_call_and_is_shown_whole():
    name = "ijc-t4-that-is-a-bishop"
    whole = " ".join(_tagged(s) for s in CASES[name][0])
    voice_event, client = _turn(name, [[whole]])
    assert len(client.messages.captured_stream_calls) == 1
    assert voice_event["text"] == " ".join(CASES[name][0])


# Quote markers the turn did not offer. Each draft gives a quote marker the
# way the voice wrote it: after its own lead-in, or standing alone in its
# paragraph, where the sentence a participant would have seen is empty.
# (kept sentences, tagged to the witness record; the marker as written;
# the draft)
QUOTE_CASES = {
    "cappadocian-t1-lead-in-and-marker": (
        ["We counted three: Father, Son, and Holy Spirit, each a real someone."],
        "Our teachers said it this way: [[quote:cappadocian.quote.ousia-and-hypostasis]]",
        "{kept0} Our teachers said it this way: [[quote:cappadocian.quote.ousia-and-hypostasis]]",
    ),
    "cappadocian-t2-marker-alone": (
        ["Our preaching held his words about the hungry and the naked at full strength."],
        "[[quote:cappadocian.quote.basil-on-common-life]]",
        "{kept0}\n\n[[quote:cappadocian.quote.basil-on-common-life]]",
    ),
    "gallic-t1-lead-in-and-marker": (
        ["At Tours he was the one who sought the unpitied."],
        "Among the brethren at Marseilles the fathers of Egypt taught us this of him: "
        "[[quote:gallic.quote.cassian-adapts-egypt-to-gaul]]",
        "{kept0}\n\nAmong the brethren at Marseilles the fathers of Egypt taught us this of him: "
        "[[quote:gallic.quote.cassian-adapts-egypt-to-gaul]]",
    ),
    "gallic-t2-marker-alone": (
        ["He went among the poor and healed them."],
        "[[quote:gallic.quote.gennadius-martin-famous-for-signs]]",
        "{kept0}\n\n[[quote:gallic.quote.gennadius-martin-famous-for-signs]]",
    ),
    "ijc-t2-marker-alone": (
        ["He came for us and for our salvation, and we held it as the ground of everything."],
        "[[quote:ijc.quote.nicene-creed]]",
        "{kept0}\n\n[[quote:ijc.quote.nicene-creed]]",
    ),
}


def _quote_turn(name, scripts):
    kept = QUOTE_CASES[name][0]
    client = FakeBedrockClient(safety_response=_safety(), reader_response=_reader(), stream_scripts=scripts)
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(kept),
        participant_message="who was Jesus", directive=None, session_id="test-session",
    )
    return voice_event, client


def _quote_draft(name):
    kept, _marker, template = QUOTE_CASES[name]
    return template.format(kept0=_tagged(kept[0]))


@pytest.mark.parametrize("name", list(QUOTE_CASES))
def test_an_unoffered_quote_marker_is_cut_with_its_lead_in_in_one_call(name):
    kept, _marker, _template = QUOTE_CASES[name]
    voice_event, client = _quote_turn(name, [[_quote_draft(name)]])
    assert len(client.messages.captured_stream_calls) == 1
    assert voice_event["text"] == kept[0]
    assert voice_event["reply_shape"]["placed"] == []
