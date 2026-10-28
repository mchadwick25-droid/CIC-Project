"""A retrieve_when line is a question a participant asks: a line that names a
record or describes the conversation is a finding. The gate is run by
engine/m9/enforce.py, not registered in GATES (that list is baked into every
package manifest)."""
from engine.m1 import gates
from engine.m1.hint_questions import non_question_reason


def _rec(*lines):
    return {"record_type": "quote", "retrieval": {"retrieve_when": list(lines)}}


def test_a_line_naming_a_record_is_not_a_question():
    assert non_question_reason("conversation reaches lpc.story.the-psalms-on-the-wall and needs the claim") is not None
    assert non_question_reason("participant asks how lpc.quote.bishop-of-bishops was read") == "names a record"


def test_a_line_describing_the_conversation_is_not_a_question():
    assert non_question_reason("conversation reaches conciliar authority theory") == "describes the conversation"
    assert non_question_reason("Representative needs the one story the insiders tell") == "describes the conversation"


def test_a_participant_question_passes():
    assert non_question_reason("participant asks how Augustine could say Cyprian's council was wrong") is None
    assert non_question_reason("what the church is, how these communities understood themselves") is None


def test_the_gate_names_each_bad_line_and_stays_out_of_gates():
    records = {"w.quote.a": _rec("participant asks about the font", "conversation reaches the font"), "w.quote.b": _rec("participant asks about the Creed")}
    found = gates.gate_retrieve_when_questions(records, {}, {})
    assert len(found) == 1 and found[0].startswith("w.quote.a: ") and "describes the conversation" in found[0]
    assert "retrieve-when-question" not in gates.GATES
