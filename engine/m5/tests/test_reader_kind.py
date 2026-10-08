"""The reader's tool schema names the kind of question asked."""
from types import SimpleNamespace

from engine.m5 import live_calls
from engine.m5.routing import QUESTION_KINDS, assemble_directive

KIND_LINES = (
    "who", "what_is", "what_did", "what_happened", "what_means", "why", "how", "did_it_happen", "other",
)


def test_the_reader_schema_requires_kind_and_lists_every_value():
    schema = live_calls._READER_TOOL["input_schema"]
    assert "kind" in schema["required"]
    assert schema["properties"]["kind"] == {"type": "string", "enum": list(KIND_LINES)}
    assert tuple(QUESTION_KINDS) == KIND_LINES


def test_the_reader_prompt_gives_one_line_of_guidance_per_value():
    section = live_calls.READER_SYSTEM_PROMPT.split("- kind:")[1].split("- clarity:")[0]
    for kind in KIND_LINES:
        assert f"{kind} (" in section


class _Client:
    def __init__(self, kind):
        self.kind = kind
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        assert kwargs["tools"][0]["input_schema"]["properties"]["kind"]["enum"]
        value = {
            "asks": [{"order": 1, "text": "who was he"}], "register": "informational", "kind": self.kind,
            "clarity": "clear", "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": [],
        }
        block = SimpleNamespace(type="tool_use", name="submit_reader_output", input=value)
        return SimpleNamespace(content=[block], usage=None)


def test_a_fake_reader_returns_each_kind_and_it_reaches_the_directive():
    for kind in KIND_LINES:
        outcome = live_calls.call_reader(_Client(kind), "model", message="Who was he?")
        assert outcome.value["kind"] == kind
        assert assemble_directive(outcome.value).kind == kind
