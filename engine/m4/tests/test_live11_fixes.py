"""The 13 October eleven-world live test, replayed offline: each case is a
real turn from that test's live-turn reports, its draft rebuilt
(engine.m4.tests.live11_replay)
and run back through the reply shaping a turn applies, with the world's own
records. No model call."""
from functools import lru_cache

import pytest

from engine.m4 import evidence, grounding_net, turn_prep
from engine.m4.quote_placement import REASON_PLACED_MISMATCH, PlacementContext
from engine.m4.tests import live11_replay
from engine.m4.turn import apply_net, settle_reply
from engine.m5.routing import Directive
from engine.shape import shape_text


@lru_cache(maxsize=None)
def _turns():
    return {(t["world"], t["q"]): t for t in live11_replay.turns()}


@lru_cache(maxsize=None)
def _replayed(world, q):
    return live11_replay.replay(_turns()[(world, q)])


def _cut(world, q):
    return [r["sentence"] for r in _replayed(world, q)["first_net"]["reply_shape"]["removed"]]


def _shown(world, q, sentence):
    return live11_replay._shown(sentence, _replayed(world, q)["text"])


def _net(world, raw, *, offered=frozenset()):
    records = live11_replay.records(world)
    return apply_net(raw, repository_records=records, thin_topics=None, placement=PlacementContext(offered=offered))


# ---- 1. what the voice is told about quotes ------------------------------


def _directive(**kwargs):
    return turn_prep._build_turn_directive(Directive(asks=[{"text": "Who is Jesus?"}], kind="who"), **kwargs)


def test_a_turn_that_offers_no_quote_says_so_and_asks_for_none():
    # witt Q1 and Q2 and most worlds' Q1/Q2 offered no quote, yet were told
    # "One quote in full", and wrote markers for ids no record has
    assert _turns()[("witt", 1)]["voice_event"]["offered_ids"] == {}
    text = _directive(quote_offers=[], has_ground=False)
    assert turn_prep.NO_QUOTE_LINE in text
    assert turn_prep.QUOTE_DUE_LINE not in text and "[[quote:" not in text.replace("[[quote:...]]", "")
    assert turn_prep.NO_GROUND_LINE in text


def test_a_turn_that_offers_quotes_lists_exactly_those_ids_with_speaker_and_gist():
    records = live11_replay.records("syr")
    offered = _turns()[("syr", 4)]["voice_event"]["offered_ids"]["quote"]
    candidates = [evidence._with_quote_index({"id": rid, "record_type": "quote"}, records) for rid in offered]
    text = _directive(quote_offers=candidates)
    for rid in offered:
        assert f"[[quote:{rid}]]" in text
    assert "[[quote:syr.quote.nativity-this-is-the-day]], its sentence naming Ephrem (" in text
    assert turn_prep.QUOTE_DUE_LINE in text and turn_prep.QUOTE_SPEAKER_LINE in text
    assert turn_prep.NO_QUOTE_LINE not in text and turn_prep.NO_GROUND_LINE not in text


def test_a_speaker_field_with_a_work_after_it_is_named_by_the_name():
    assert turn_prep._speaker_name("the Augsburg Confession, Article II -- the same confession") == "the Augsburg Confession"
    assert turn_prep._speaker_name("Martin, bishop of Tours") == "Martin"


# ---- 2 and 3. the standing rules: name the speaker, copy the id whole -----


def test_the_shape_asks_for_the_speaker_in_the_markers_own_sentence_and_whole_ids():
    shape = shape_text()
    assert "names the quote's speaker, then [[quote:id]] as the last thing in that same sentence" in shape
    assert "never follows 'he' or 'she' or an unnamed teacher" in shape
    assert "COPIED whole, its type part included" in shape
    assert "What a person did or taught we tell in our own words, never as their words." in shape


# ---- 5. the net: false cuts narrowed -------------------------------------


@pytest.mark.parametrize("world, q, sentence", [
    ("rzg", 5, "What it does hold is the doctrine itself, in his own words, and the institutions he shaped."),
    ("ijc", 6, "What an ordinary believer would have said to you, in their own words, we cannot show you; "
               "no such words were saved."),
    ("pahc", 2, "Beyond that - what he taught, where he walked, the particular things he said and did before the "
                "cross - our own record does not lay those out the way a connected account would."),
])
def test_in_his_own_words_and_things_he_said_in_narration_are_not_attributions(world, q, sentence):
    assert sentence not in _cut(world, q)
    assert _shown(world, q, sentence)


def test_narration_after_an_attribution_that_held_its_own_words_stays():
    # desert Q5: Moses' words are still cut, because the voice reworded the
    # saying ("the errors of another man"; the story says "faults that are
    # not mine"); the story's outcome is not
    cut = _cut("desert", 5)
    assert any(s.startswith("When the others asked what he was doing, he said:") for s in cut)
    assert _shown("desert", 5, "The elders heard him and released the brother without punishment.")


def test_words_that_run_on_after_an_attribution_are_still_cut():
    # desert Q2: the second sentence is still the elder's words
    assert "It is Christ who works them, by means of those who believe in him." in _cut("desert", 2)


def test_direct_speech_of_a_quotes_words_is_that_quote_even_when_a_witness_repeats_them():
    # desert Q4: desert.dw.god says the same words, but after "said:" they
    # are the Antony formula's, a quote record: placed, or not said
    assert any(s.startswith("He stood up in Alexandria and said:") for s in _cut("desert", 4))
    assert "There was never a time when he was not." in _cut("desert", 4)


def test_the_world_stating_its_own_doctrine_is_read_against_its_paragraphs_records():
    # cappadocian Q1: untagged, it shares wording with a Basil passage; its
    # paragraph cites the world's own terms for one being and three persons
    assert _shown("cappadocian", 1, "The Father, the Son, and the Holy Spirit are one ousia - one being, what God is.")


def test_a_sentence_tagged_to_a_quote_not_placed_is_still_dropped():
    # ijc Q2 tagged its creed lines to the creed quote record, which the turn
    # did not offer (decision 61, option A). The directive now says to tag no
    # quote record on such a turn.
    assert "He came down from heaven, was made man of the Virgin Mary, suffered under Pontius Pilate, was crucified, " \
        "died, and was buried." in _cut("ijc", 2)


def test_a_term_glossed_in_its_own_records_words_keeps_its_marks():
    # ijc Q3
    assert _shown("ijc", 3, 'Homoousios - "of one substance with the Father".')


def test_words_only_a_quote_holds_are_still_its_words():
    # desert Q1: "Wisdom" and "Essence" stand only in the Antony formula,
    # not in desert.dw.god, the record the sentence cites
    removed = _replayed("desert", 1)["first_net"]["reply_shape"]["removed"]
    assert any(r["sentence"].startswith("To us Jesus is the eternal Word and Wisdom") for r in removed)


def test_a_quoted_phrase_put_in_someones_mouth_is_no_term_gloss():
    # don Q3: the petition's words, quoted, with "and said". don.term.ecclesia
    # holds them only inside its own quotation marks, as the petition's.
    assert any("of the party of Donatus" in s for s in _cut("don", 3))


# ---- 6. quote placement --------------------------------------------------


@pytest.mark.parametrize("world, q", [("cappadocian", 6), ("alx", 4)])
def test_a_cut_typed_quotation_leaves_no_stray_quotation_mark(world, q):
    shown = [s["sentence"] for s in _replayed(world, q)["first_net"]["sentences"]]
    assert not [s for s in shown if live11_replay._STRAY.match(s)]
    assert not _replayed(world, q)["text"].rstrip().endswith('"')


def test_a_quote_the_net_refuses_does_not_take_the_replys_one_place():
    # ijc Q4: the Leo quote's lead-in ("He wrote of one Mediator...") names
    # no one, so it is refused; the Chalcedon definition, offered and next,
    # is placed under a lead-in that names the council
    net_result = _replayed("ijc", 4)["first_net"]
    assert net_result["reply_shape"]["placed"] == ["ijc.quote.chalcedon-definition"]
    whys = [(r["draft"], r["why"]) for r in net_result["reply_shape"]["removed"]]
    assert [why for draft, why in whys if "leo-tome-each-form" in draft] == [grounding_net.REASON_SPEAKER_UNNAMED]
    assert not [why for _draft, why in whys if why == "second placed quote in one reply"]


def test_quotes_whose_lead_in_names_another_person_are_refused():
    # hal Q4: eyes-of-faith is introduced as Paula's words (Jerome's record),
    # and hail-bethlehem after "Then she cried out": both name Paula, and the
    # speaker of both records is Jerome
    net_result = _replayed("hal", 4)["first_net"]
    assert net_result["reply_shape"]["placed"] == []
    whys = [(r["draft"], r["why"]) for r in net_result["reply_shape"]["removed"]]
    assert [why for draft, why in whys if "eyes-of-faith" in draft] == [REASON_PLACED_MISMATCH]
    assert [why for draft, why in whys if "hail-bethlehem" in draft] == [grounding_net.REASON_SPEAKER_UNNAMED]


def test_a_removed_marker_sentence_is_reported_once():
    removed = _replayed("witt", 1)["first_net"]["reply_shape"]["removed"]
    assert [r["sentence"] for r in removed if "christ-redeemer" in r["draft"]] == ["That is who he is:"]


# ---- 7. the backstop -----------------------------------------------------


def test_witt_q1_falls_back_to_its_answer_record_instead_of_shipping_unsourced():
    result = _replayed("witt", 1)
    assert not result["first_net"]["substantive_survives"]
    assert result["fallback"] == "witt.dw.truly-god-and-truly-man"
    assert result["net_result"]["substantive_survives"]
    assert result["text"].startswith("Our catechism gave every household these words")


FIX = {
    "fix.witness.w": {"id": "fix.witness.w", "record_type": "doctrinal_witness", "text": "We keep the fast because we are asked to keep it."},
    "fix.term.t": {"id": "fix.term.t", "record_type": "term", "world_word": "fast", "plain_meaning": "Going without food."},
}


def _settle(raw, offered=None):
    def net(text):
        return apply_net(text, repository_records=FIX, thin_topics=None)

    text, _c, net_result = net(raw)
    return settle_reply(raw, text, net_result, offered or {}, FIX, net)


def test_a_reply_that_claimed_ground_and_kept_none_shows_the_answer_record():
    settled = _settle("We keep it because the moon tells us to [[fix.nowhere.x]].", {"doctrinal_witness": ["fix.witness.w"]})
    assert settled["answer_record_fallback"] == "fix.witness.w"
    assert settled["text"] == "We keep the fast because we are asked to keep it."


def test_a_reply_that_claimed_ground_kept_none_and_has_no_answer_record_is_not_shown():
    settled = _settle("We keep it because the moon tells us to [[fix.nowhere.x]].")
    assert settled["answer_record_fallback"] is None
    assert settled["text"] == "" and settled["citations"] == []


def test_a_reply_that_never_claimed_ground_stands():
    settled = _settle("You are welcome to ask more.", {"doctrinal_witness": ["fix.witness.w"]})
    assert settled["answer_record_fallback"] is None and settled["citations"] is None
    assert settled["text"] == "You are welcome to ask more."


def test_a_reply_with_a_verified_citation_stands():
    settled = _settle("We keep the fast because we are asked to keep it [[fix.witness.w]].")
    assert settled["answer_record_fallback"] is None and settled["citations"] is None


def test_a_mistyped_type_part_names_the_answer_record_only_for_the_fallback():
    records = live11_replay.records("witt")
    from engine.m4.turn import _answer_record_fallback

    raw = "Both, and in the same breath [[witt.term.truly-god-and-truly-man]]."
    assert _answer_record_fallback(raw, {}, records) == "witt.dw.truly-god-and-truly-man"
    # the voice's own sentence still cites only what it named
    _text, citations, net_result = apply_net(raw, repository_records=records, thin_topics=None)
    assert citations == [] and net_result["sentences"][0]["verdict"] == "withhold"


# ---- the regression replay over all 66 recorded drafts --------------------


def test_every_rebuilt_draft_puts_every_recorded_sentence_back():
    for (world, q), turn in _turns().items():
        draft = live11_replay.rebuild_draft(turn["voice_event"])
        for entry in turn["voice_event"]["grounding"]["sentences"] + turn["voice_event"]["reply_shape"]["removed"]:
            assert grounding_net.strip_tags(entry["draft"]).strip()[:40] in grounding_net.strip_tags(draft), (world, q)


def test_the_replay_over_all_66_drafts():
    counts = live11_replay.summary(live11_replay.run_all())
    assert counts["turns"] == 66
    # nothing ungrounded is sent: witt Q1 falls back to its answer record
    assert counts["degraded_sent"] == 0 and counts["fallbacks"] == 1
    # 51 and 5 after the first fix slice. The second slice releases wording
    # the cited records hold as their own (3 sentences), refuses quotes whose
    # lead-in names no speaker (9 lead-ins), and cuts desert Q4's direct
    # speech of the Antony formula as that quote's words (2 sentences that
    # had stood); hal Q4's lead-in, listed as an overcut, names Paula for
    # Jerome's record and goes with its quote.
    assert counts["cuts"] == 56
    assert counts["overcuts_still_cut"] == 6
    assert counts["placed_quotes"] == 4 and counts["placed_without_speaker_named"] == 0
    assert counts["stray_punctuation_sentences"] == 1


# ---- reading top fix 6: untagged claims about a person; what withhold does ----


def test_the_shape_asks_for_a_tag_on_every_claim_about_what_someone_did_named_or_not():
    # pahc Q5: "The one who walked him to the stake is remembered as a brother
    # who regretted it afterward." names no one, so the old contract (tag
    # "only a sentence naming a person, place, text, number") let it go untagged
    shape = shape_text()
    assert "only a sentence naming a person" not in shape
    assert "or what someone did, said, held or was, is tagged to the record it comes from, whether or not it names them" in shape


def test_an_untagged_claim_that_names_no_one_is_still_read_as_framing_by_the_net():
    # The net finds no claim marker in it; the instruction above is the fix.
    sentence = "The one who walked him to the stake is remembered as a brother who regretted it afterward."
    entry = next(e for e in _replayed("pahc", 5)["net_result"]["sentences"] if e["sentence"] == sentence)
    assert (entry["verdict"], entry["why"]) == ("ok", "no checkable claim - interpretive/connective framing")


def test_a_withheld_sentence_is_shown_without_its_citation():
    # syr Q2: "He healed the sick and taught in parables" shares no word with
    # syr.dw.gospel-harmony. A sentence withheld for a reason other than a
    # quotation is shown as written and only loses its citation; the
    # quotation reasons alone remove a sentence.
    sentence = "He healed the sick and taught in parables."
    result = _replayed("syr", 2)
    entry = next(e for e in result["net_result"]["sentences"] if e["sentence"] == sentence)
    assert entry["verdict"] == "withhold" and entry["why"] not in grounding_net.QUOTATION_DROP_REASONS
    assert _shown("syr", 2, sentence)
    records = live11_replay.records("syr")
    _text, citations, _n = apply_net(live11_replay.rebuild_draft(_turns()[("syr", 2)]["voice_event"]),
                                     repository_records=records, thin_topics=None)
    assert sentence not in [c["sentence"] for c in citations]


# ---- rhythm: varied sentence length, no added connections ----------------


def test_the_shape_asks_for_varied_rhythm_and_no_added_reasons():
    shape = shape_text()
    assert "8. Vary the rhythm." in shape
    assert "never add a reason, motive, cause or 'because' that the record does not give" in shape


def test_rhythm_counts_runs_of_three_short_sentences_and_the_spread():
    flat = live11_replay.rhythm("He came. He saw. He left. Then the whole household followed him across the sea to Bethlehem.")
    assert flat["short_runs"] == 1 and flat["sentences"] == 4 and flat["spread"] > 3
    assert live11_replay.rhythm("One two three. Four five six.")["short_runs"] == 0


def test_a_connective_the_tagged_record_does_not_use_is_counted():
    sentences = [
        {"sentence": "We keep the fast because we are asked to keep it.", "tags": ["fix.witness.w"]},
        {"sentence": "We keep the fast because the moon commands it.", "tags": []},
    ]
    assert live11_replay.connective_claims(sentences, FIX) == ["We keep the fast because the moon commands it."]


def test_in_a_named_speakers_own_words_is_always_an_attribution():
    records = live11_replay.records("desert")
    for raw in (
        "In Antony's own words, we must always breathe Christ and trust in him.",
        "Antony, in his own words, we are not the doers of these things.",
    ):
        text, _c, net_result = apply_net(raw, repository_records=records, thin_topics=None)
        assert text == "" and net_result["reply_shape"]["removed"], raw


def test_a_stream_releases_nothing_before_a_grounded_sentence():
    # witt Q1: every tag names a record that does not exist, so the reply
    # falls back to its answer record; none of the draft may show first
    from engine.m4.sentence_stream import SentenceStream

    records = live11_replay.records("witt")
    draft = live11_replay.rebuild_draft(_turns()[("witt", 1)]["voice_event"])
    stream = SentenceStream(repository_records=records, world_key="witt")
    events = [e for i in range(0, len(draft), 7) for e in stream.feed(draft[i:i + 7])]
    assert events == [] and stream.released == 0
    grounded = "We keep the catechism every week [[witt.dw.truly-god-and-truly-man]]. " + draft
    stream = SentenceStream(repository_records=records, world_key="witt")
    assert stream.feed(grounded) and stream.released >= 1
