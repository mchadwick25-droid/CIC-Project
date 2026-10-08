"""The live-test guard (System Hub decision 56). No network and no model
call: the SDK client and the Bedrock control plane are fakes that record
what reaches them."""
import ast
import re
import runpy
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from engine.m8.usage import record_usage
from engine.provider import anthropic_direct, bedrock, guard, preflight, route
from engine.provider.bedrock import NormalizedUsage

ENGINE = Path(__file__).resolve().parents[2]
HAIKU = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
SONNET_GLOBAL = "global.anthropic.claude-sonnet-5-5-20260101-v1:0"
APPROVED = ["--live-test", "guard proof", "--cap-usd", "1.00"]


class _Recorder:
    """One ordered log shared by the printed header and the fake client's
    calls, so the order between them is observable."""

    def __init__(self):
        self.events: list[tuple[str, object]] = []

    @property
    def calls(self):
        return [e for e in self.events if e[0] == "call"]

    @property
    def constructions(self):
        return [e for e in self.events if e[0] == "constructed"]


def _usage(input_tokens=1000, output_tokens=100):
    return SimpleNamespace(input_tokens=input_tokens, output_tokens=output_tokens, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeStream:
    def __init__(self, usage):
        self._usage = usage

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(["ok"]), get_final_message=lambda: SimpleNamespace(usage=self._usage))

    def __exit__(self, *exc):
        return False


def _fake_sdk(recorder, usage):
    class FakeSdkClient:
        def __init__(self, **kwargs):
            recorder.events.append(("constructed", kwargs))
            self.models = SimpleNamespace(list=lambda **kw: SimpleNamespace(data=[]))
            self.messages = SimpleNamespace(
                create=lambda **kw: (recorder.events.append(("call", kw)), SimpleNamespace(usage=usage, content=[]))[1],
                stream=lambda **kw: (recorder.events.append(("call", kw)), _FakeStream(usage))[1],
            )

    return FakeSdkClient


@pytest.fixture(autouse=True)
def _clean_guard():
    guard.reset_for_tests()
    yield
    guard.reset_for_tests()


@pytest.fixture
def seam(monkeypatch):
    """Bedrock's SDK client and control plane replaced by recording fakes;
    the printed header lands in the same log."""
    recorder = _Recorder()
    monkeypatch.setattr(bedrock, "AnthropicBedrock", _fake_sdk(recorder, _usage()))
    monkeypatch.setattr(
        bedrock.boto3, "client",
        lambda *a, **kw: SimpleNamespace(list_inference_profiles=lambda **k: {"inferenceProfileSummaries": [
            {"inferenceProfileId": HAIKU, "inferenceProfileName": "Claude Haiku 4.5"},
            {"inferenceProfileId": SONNET_GLOBAL, "inferenceProfileName": "Claude Sonnet 5.5 (global)"},
        ]}),
    )
    monkeypatch.setattr(guard, "_emit", lambda text: recorder.events.append(("header", text)))
    monkeypatch.setattr(sys, "argv", ["prog"])
    return recorder


def _approve(monkeypatch, extra=()):
    monkeypatch.setattr(sys, "argv", ["prog", *extra, *APPROVED])


# ---- the rule: no client without both flags ---------------------------------

@pytest.mark.parametrize("argv", [
    [],
    ["--live-test", "only a name"],
    ["--cap-usd", "1.00"],
    ["--live-test", "", "--cap-usd", "1.00"],
    ["--live-test", "name", "--cap-usd", "0"],
    ["--live-test", "name", "--cap-usd", "-3"],
    ["--live-test", "name", "--cap-usd", "nan"],
    ["--live-test", "name", "--cap-usd", "lots"],
])
def test_a_command_without_both_flags_is_refused_before_a_client_exists(seam, monkeypatch, capsys, argv):
    monkeypatch.setattr(sys, "argv", ["prog", *argv])
    with pytest.raises(SystemExit) as refused:
        bedrock.make_client("us-east-1")
    assert refused.value.code not in (0, None)
    assert "decision 56" in capsys.readouterr().err
    assert seam.constructions == [] and seam.calls == []


def test_the_anthropic_route_is_refused_the_same_way(seam, monkeypatch):
    monkeypatch.delenv("RENDER", raising=False)
    monkeypatch.setenv(route.ROUTE_ENV, "anthropic")
    monkeypatch.setenv(anthropic_direct.KEY_ENV, "k")
    monkeypatch.setattr(anthropic_direct, "Anthropic", _fake_sdk(seam, _usage()))
    with pytest.raises(SystemExit):
        anthropic_direct.make_client()
    assert seam.constructions == []


def test_flags_are_read_with_the_equals_form_too(seam, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "--live-test=with equals", "--cap-usd=2.5"])
    assert guard.parse_live_test(sys.argv[1:]) == guard.LiveTest("with equals", 2.5)


# ---- an approved run: header first, then calls, stops at the cap ------------

def test_an_approved_run_prints_its_settings_before_its_first_call(seam, monkeypatch):
    _approve(monkeypatch)
    model_id = bedrock.resolve_model_id("haiku-4-5", "us-east-1")
    client = bedrock.make_client("us-east-1")
    assert seam.events[0][0] == "constructed"  # a client exists, no call and no header yet
    client.messages.create(model=model_id, max_tokens=16, system="s", messages=[{"role": "user", "content": "hi"}])
    client.messages.create(model=model_id, max_tokens=16, system="s", messages=[{"role": "user", "content": "hi"}])
    kinds = [e[0] for e in seam.events]
    assert kinds == ["constructed", "header", "call", "call"]
    header = seam.events[1][1]
    assert "guard proof" in header and "$1.00" in header and model_id in header
    assert "Bedrock, regional inference profile, us-east-1" in header


def test_the_header_names_a_global_profile_as_global(seam, monkeypatch):
    _approve(monkeypatch)
    model_id = bedrock.resolve_model_id("sonnet-5-5", "us-east-1")
    bedrock.make_client("us-east-1").messages.create(model=model_id, max_tokens=16, messages=[])
    assert "Bedrock, global inference profile, us-east-1" in seam.events[1][1]


def test_the_anthropic_route_header_says_anthropic_api(seam, monkeypatch):
    monkeypatch.delenv("RENDER", raising=False)
    monkeypatch.setenv(route.ROUTE_ENV, "anthropic")
    monkeypatch.setenv(anthropic_direct.KEY_ENV, "k")
    monkeypatch.setattr(anthropic_direct, "Anthropic", _fake_sdk(seam, _usage()))
    _approve(monkeypatch)
    client = anthropic_direct.make_client()
    client.messages.create(model="claude-haiku-4-5-20251001", max_tokens=16, messages=[])
    assert "ROUTE: Anthropic API" in seam.events[1][1]


def test_the_run_stops_before_a_call_that_could_pass_the_cap(seam, monkeypatch):
    big = _usage(input_tokens=100_000, output_tokens=10_000)  # $0.165 a call on haiku at the regional rate
    monkeypatch.setattr(bedrock, "AnthropicBedrock", _fake_sdk(seam, big))
    monkeypatch.setattr(sys, "argv", ["prog", "--live-test", "guard proof", "--cap-usd", "0.50"])
    model_id = bedrock.resolve_model_id("haiku-4-5", "us-east-1")
    client = bedrock.make_client("us-east-1")
    prompt = "x" * 300_000  # about the 100,000 input tokens the fake reports
    made = 0
    with pytest.raises(guard.LiveTestCapReached):
        for _ in range(20):
            client.messages.create(model=model_id, max_tokens=10_000, system=prompt, messages=[{"role": "user", "content": "hi"}])
            made += 1
    assert made == len(seam.calls) == 2
    assert 0.32 < guard.priced_total() <= 0.50
    with pytest.raises(guard.LiveTestCapReached):  # and it stays stopped
        client.messages.create(model=model_id, max_tokens=10_000, system=prompt, messages=[])
    assert len(seam.calls) == 2
    headers = [e[1] for e in seam.events if e[0] == "header"]
    assert len(headers) == 2 and "CAP REACHED" in headers[1]


def test_a_streamed_call_is_counted_against_the_cap(seam, monkeypatch):
    _approve(monkeypatch)
    model_id = bedrock.resolve_model_id("haiku-4-5", "us-east-1")
    client = bedrock.make_client("us-east-1")
    with client.messages.stream(model=model_id, max_tokens=16, messages=[]) as stream:
        assert list(stream.text_stream) == ["ok"]
    assert guard.priced_total() > 0
    assert guard.run_summary()["priced_total_usd"] > 0


def test_a_model_not_in_the_printed_settings_is_refused(seam, monkeypatch):
    _approve(monkeypatch)
    model_id = bedrock.resolve_model_id("haiku-4-5", "us-east-1")
    client = bedrock.make_client("us-east-1")
    client.messages.create(model=model_id, max_tokens=16, messages=[])
    with pytest.raises(guard.LiveTestGuardError):
        client.messages.create(model="us.anthropic.claude-opus-5-5-20260101-v1:0", max_tokens=16, messages=[])
    assert len(seam.calls) == 1


def test_a_model_with_no_approved_price_is_refused_before_the_call(seam, monkeypatch):
    _approve(monkeypatch)
    client = bedrock.make_client("us-east-1")
    with pytest.raises(guard.LiveTestGuardError):
        client.messages.create(model="us.anthropic.claude-mystery-9-20260101-v1:0", max_tokens=16, messages=[])
    assert seam.calls == []


def test_a_guarded_client_offers_nothing_but_messages_and_the_model_listing(seam, monkeypatch):
    _approve(monkeypatch)
    client = bedrock.make_client("us-east-1")
    assert client.models is not None
    with pytest.raises(guard.LiveTestGuardError):
        client.beta
    with pytest.raises(guard.LiveTestGuardError):
        client.messages.batches


# ---- usage records carry the name; the conversation's carry none ------------

def test_usage_records_from_an_approved_run_carry_the_name(seam, monkeypatch):
    _approve(monkeypatch)
    bedrock.make_client("us-east-1")
    record = record_usage(usage=NormalizedUsage(1, 1, 0, 0), session_id="s", call_kind="voice_generation", model_id=HAIKU)
    assert record.live_test == "guard proof"


def test_usage_records_from_a_conversation_carry_none(seam):
    with guard.conversation_scope():
        bedrock.make_client("us-east-1")
    record = record_usage(usage=NormalizedUsage(1, 1, 0, 0), session_id="s", call_kind="voice_generation", model_id=HAIKU)
    assert record.live_test is None


def test_the_conversation_path_gets_the_sdk_client_itself(seam):
    with guard.conversation_scope():
        client = bedrock.make_client("us-east-1")
    assert type(client).__name__ == "FakeSdkClient"
    assert not isinstance(client, guard._GuardedClient)
    assert [e[0] for e in seam.events] == ["constructed"]


def test_the_routed_conversation_client_is_unwrapped_too(seam, monkeypatch):
    monkeypatch.delenv(route.ROUTE_ENV, raising=False)
    with guard.conversation_scope():
        client, voice_id, safety_id = route.build_route("us-east-1", "haiku-4-5", "haiku-4-5")
    assert type(client).__name__ == "FakeSdkClient" and voice_id == safety_id == HAIKU
    assert guard.active_live_test_name() is None


def test_the_engine_api_builds_its_client_inside_the_conversation_scope():
    tree = ast.parse((ENGINE / "api" / "app.py").read_text(encoding="utf-8"))
    builder = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_build_real_app")
    scoped = [
        w for w in ast.walk(builder) if isinstance(w, ast.With)
        and any(isinstance(i.context_expr, ast.Call) and getattr(i.context_expr.func, "attr", "") == "conversation_scope" for i in w.items)
    ]
    assert scoped, "_build_real_app must build its client inside guard.conversation_scope()"
    assert any(isinstance(c, ast.Call) and getattr(c.func, "id", "") == "build_route" for w in scoped for c in ast.walk(w))


# ---- every entry point: refused without the flags, no client call -----------

_REGION = ["--region", "us-east-1"]
_M3 = _REGION + ["--max-usd", "1", "--authorized-by", "test"]
ENTRY_POINTS = [
    ("engine.provider.preflight", ["--model-pattern", "haiku-4-5"] + _REGION),
    ("engine.m8.lapsed_cache_window_measure", _REGION + ["--phase", "write"]),
    ("engine.m8.live_memory_growth_run", _REGION),
    ("engine.m8.cache_economics_measure", _REGION),
    ("engine.m8.live_cost_run", _REGION),
    ("engine.m1.rendering_fidelity", _REGION),
    ("engine.m1.reports.rendering_grader_model_study", _REGION),
    ("engine.m3.dossier_citation_grade", _M3 + ["--grader-model", "haiku-4-5", "--per-world", "1", "--seed", "1"]),
    ("engine.m3.e2_run", _M3 + ["--worlds", "fix"]),
    ("engine.m3.e3_attach", _M3 + ["--worlds", "fix"]),
    ("engine.m3.live_admission_run", _REGION + ["--authorized-by", "test"]),
    ("engine.m4.live_turn_run", _REGION),
    ("engine.m4.live_table_run", _REGION),
    ("engine.m4.live_table_battery", _REGION),
    ("engine.m4.live_uncited_claims_battery", _REGION),
    ("engine.m4.reports.g1_citation_contract_battery", _REGION),
    ("engine.m4.reports.g1_precision_sample_measure", _REGION),
    ("engine.m4.reports.net_support_check_measure", _REGION),
    ("engine.m4.reports.r37_live_battery", _REGION),
    ("engine.m4.reports.r38_self_revision_measure", _REGION),
    ("engine.m4.reports.r39_d1_d2_measure", _REGION),
    ("engine.m4.reports.r39_generation_side_measure", _REGION),
    ("engine.m4.reports.r41_modern_word_battery", _REGION),
    ("engine.m4.reports.table_other_tradition_battery", _REGION),
    ("engine.m5.safety_script_run", _REGION + ["--all"]),
]


@pytest.mark.parametrize("module,argv", ENTRY_POINTS, ids=[m for m, _ in ENTRY_POINTS])
def test_every_non_conversation_entry_point_exits_before_any_client_call(seam, monkeypatch, tmp_path, module, argv):
    monkeypatch.setattr(bedrock, "resolve_model_id", lambda pattern, region: HAIKU)
    monkeypatch.setattr(sys, "argv", [module, *argv])
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit) as stopped:
        runpy.run_module(module, run_name="__main__")
    assert stopped.value.code not in (0, None)
    assert seam.constructions == [] and seam.calls == [], f"{module} reached the model client without a live-test name and cap"


def _entry_point_sources():
    for path in sorted(ENGINE.rglob("*.py")):
        rel = path.relative_to(ENGINE)
        if "tests" in rel.parts or rel.parts[0] == "provider":
            continue
        yield rel, path.read_text(encoding="utf-8")


def test_every_command_that_builds_a_client_accepts_the_two_flags():
    missing = [
        str(rel) for rel, text in _entry_point_sources()
        if "make_client(" in text and "ArgumentParser(" in text and "guard.add_arguments(" not in text
    ]
    assert not missing, f"these commands build a model client but do not accept --live-test and --cap-usd: {missing}"


def test_the_entry_point_list_covers_every_command_that_builds_a_client():
    listed = {m for m, _ in ENTRY_POINTS}
    found = {
        ("engine." + str(rel.with_suffix("")).replace("/", ".")) for rel, text in _entry_point_sources()
        if "make_client(" in text and "ArgumentParser(" in text
    } | {"engine.provider.preflight"}
    assert found <= listed, f"add these to ENTRY_POINTS: {sorted(found - listed)}"


# ---- the seam is the only place a model client is constructed ---------------

_CONSTRUCTOR = re.compile(
    r"\b(?:Async)?Anthropic(?:Bedrock|Vertex|Foundry|AWS)?\(|bedrock[-_]runtime|\.invoke_model\b|\.converse(?:_stream)?\("
)
_SEAM = {Path("provider/bedrock.py"), Path("provider/anthropic_direct.py")}


def test_no_file_outside_the_provider_seam_constructs_a_model_client():
    offenders = [
        f"{path.relative_to(ENGINE)}:{n}"
        for path in sorted(ENGINE.rglob("*.py"))
        if path.relative_to(ENGINE) not in _SEAM and "tests" not in path.relative_to(ENGINE).parts
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
        if _CONSTRUCTOR.search(line) and not line.lstrip().startswith("#")
    ]
    assert not offenders, f"a model client is built only in engine/provider/bedrock.py and anthropic_direct.py: {offenders}"


def test_the_grep_finds_a_constructor_where_there_is_one(tmp_path):
    assert _CONSTRUCTOR.search("client = AnthropicBedrock(aws_region=region)")
    assert _CONSTRUCTOR.search("boto3.client('bedrock-runtime')")
    assert not _CONSTRUCTOR.search("from anthropic import APIError, APITimeoutError")


def test_only_the_engine_api_opens_the_conversation_scope():
    offenders = [
        str(rel) for rel, text in _entry_point_sources()
        if "conversation_scope" in text and rel.parts[0] != "api"
    ]
    assert not offenders, f"conversation_scope() belongs to engine/api alone: {offenders}"


def test_the_preflight_cli_runs_end_to_end_under_a_cap(seam, monkeypatch, tmp_path):
    monkeypatch.setattr(preflight, "REPORT_PATH", tmp_path / "preflight.json")
    monkeypatch.setattr(sys, "argv", ["preflight", "--model-pattern", "haiku-4-5", "--region", "us-east-1", *APPROVED])
    preflight.main()
    kinds = [e[0] for e in seam.events]
    assert kinds[:3] == ["constructed", "header", "call"] and kinds.count("call") == 3
