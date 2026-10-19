from engine.m4.generation import stream_voice_turn


class _Stream:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    text_stream = ["We answer."]

    def get_final_message(self):
        return type("Message", (), {"usage": None})()


class _Client:
    def __init__(self):
        self.calls = []
        self.messages = self

    def stream(self, **kwargs):
        self.calls.append(kwargs)
        return _Stream()


def test_the_voice_call_allows_two_thousand_and_forty_eight_tokens():
    client = _Client()
    stream_voice_turn(client, "m", system_prompt="WORLD", message="hi")
    assert client.calls[0]["max_tokens"] == 2048


def test_a_voice_call_past_the_limit_fails_at_once_without_calling_the_model(monkeypatch):
    import threading

    from engine.m4 import generation

    monkeypatch.setattr(generation, "_voice_slots", threading.BoundedSemaphore(1))
    held = generation._voice_slots.acquire(blocking=False)
    client = _Client()
    outcome = stream_voice_turn(client, "m", system_prompt="WORLD", message="hi")
    assert held and client.calls == []
    assert (outcome.status, outcome.value) == ("error", {"error": generation.VOICE_CAPACITY_FULL})


def test_a_voice_call_gives_its_slot_back_when_it_ends_or_fails(monkeypatch):
    import threading

    from engine.m4 import generation

    monkeypatch.setattr(generation, "_voice_slots", threading.BoundedSemaphore(1))

    class _Broken(_Client):
        def stream(self, **kwargs):
            raise ValueError("unexpected")

    try:
        stream_voice_turn(_Broken(), "m", system_prompt="WORLD", message="hi")
    except ValueError:
        pass
    assert stream_voice_turn(_Client(), "m", system_prompt="WORLD", message="hi").status == "ok"
    assert stream_voice_turn(_Client(), "m", system_prompt="WORLD", message="hi").status == "ok"


def test_the_production_limit_is_sixteen():
    from engine.m4 import generation

    assert generation.MAX_CONCURRENT_VOICE_CALLS == 16


def test_a_connection_dropped_mid_stream_ends_the_call_as_an_error_not_a_crash():
    from engine.m4 import generation

    class _Dropped(_Client):
        def stream(self, **kwargs):
            raise generation._TRANSPORT_ERRORS[0]("peer closed connection without sending complete message body")

    outcome = stream_voice_turn(_Dropped(), "m", system_prompt="WORLD", message="hi")
    assert outcome.status == "error"
    assert "connection dropped" in outcome.value["error"]
