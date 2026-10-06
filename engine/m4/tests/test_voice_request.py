from engine.m4.voice_request import DIRECTIVE_CLOSE, DIRECTIVE_OPEN, build_voice_request
from engine.shape import shape_text

EPHEMERAL = {"type": "ephemeral"}
HISTORY = [
    {"role": "user", "content": "who is jesus"},
    {"role": "assistant", "content": "He was God's own Word."},
    {"role": "user", "content": "and then"},
    {"role": "assistant", "content": "He died and rose."},
]


def test_the_system_blocks_are_the_shape_segment_and_world_prompt_cached_then_the_directive_uncached():
    system, _ = build_voice_request(system_prompt="WORLD", message="hi", turn_directive="DIRECTIVE")
    assert system == [{"type": "text", "text": shape_text(), "cache_control": EPHEMERAL},
                      {"type": "text", "text": "WORLD", "cache_control": EPHEMERAL},
                      {"type": "text", "text": "DIRECTIVE"}]


def test_no_directive_and_no_history_sends_the_bare_message_and_two_system_blocks():
    system, messages = build_voice_request(system_prompt="WORLD", message="hi")
    assert messages == [{"role": "user", "content": "hi"}]
    assert len(system) == 2


def test_the_directive_stays_out_of_the_user_message_by_default():
    _, messages = build_voice_request(system_prompt="WORLD", message="the question", turn_directive="Speak plainly.")
    assert messages == [{"role": "user", "content": "the question"}]


def test_under_the_flag_the_directive_leads_the_final_user_message_in_a_framed_block(monkeypatch):
    monkeypatch.setenv("CIC_DIRECTIVE_IN_USER_MESSAGE", "1")
    system, messages = build_voice_request(system_prompt="WORLD", message="the question", turn_directive="Speak plainly.")
    assert [b["text"] for b in system] == [shape_text(), "WORLD"]
    assert messages == [{"role": "user", "content": [
        {"type": "text", "text": f"{DIRECTIVE_OPEN}\nSpeak plainly.\n{DIRECTIVE_CLOSE}"},
        {"type": "text", "text": "the question"},
    ]}]


def test_only_the_last_history_block_carries_the_history_breakpoint():
    _, messages = build_voice_request(system_prompt="WORLD", message="next", turn_directive="D", history=HISTORY)
    assert [m["role"] for m in messages] == ["user", "assistant", "user", "assistant", "user"]
    assert messages[:3] == HISTORY[:3]
    assert messages[3]["content"] == [{"type": "text", "text": "He died and rose.", "cache_control": EPHEMERAL}]
    assert messages[4]["content"] == "next"


def test_the_history_prefix_is_byte_identical_across_turns_with_different_directives():
    first = build_voice_request(system_prompt="WORLD", message="q1", turn_directive="D1", history=HISTORY[:2])
    second = build_voice_request(system_prompt="WORLD", message="q2", turn_directive="D2", history=HISTORY)
    assert first[0] == second[0]
    assert first[1][0] == second[1][0]
    assert first[1][1] == {"role": "assistant", "content": [{"type": "text", "text": "He was God's own Word.", "cache_control": EPHEMERAL}]}
    assert second[1][1] == HISTORY[1]


def test_the_callers_history_is_never_mutated():
    history = [dict(m) for m in HISTORY]
    build_voice_request(system_prompt="WORLD", message="next", turn_directive="D", history=history)
    assert history == HISTORY


def test_a_history_block_list_keeps_its_earlier_blocks_and_marks_the_last():
    history = [
        {"role": "user", "content": "q"},
        {"role": "assistant", "content": [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]},
    ]
    _, messages = build_voice_request(system_prompt="WORLD", message="next", history=history)
    assert messages[1]["content"] == [{"type": "text", "text": "a"}, {"type": "text", "text": "b", "cache_control": EPHEMERAL}]
    assert history[1]["content"] == [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]
