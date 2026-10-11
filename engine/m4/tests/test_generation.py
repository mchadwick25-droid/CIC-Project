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
