"""The live-test guard (System Hub decision 56): the only model spend is
conversations. A model client is handed out in exactly two cases:

  (a) to the conversation path in engine/api, which declares itself with
      conversation_scope() and gets the SDK client itself, unwrapped, as it
      always has; and
  (b) to a command that carries both --live-test "<name>" and --cap-usd <n>.

A command without both prints RULE and exits non-zero before any network
call. An approved command gets a client that prints its settings before the
first call, refuses any call that could carry the priced total past the cap,
and tags every usage record with the live-test name.

The check runs where a client is built (and where a model id is resolved),
never per call or per turn on the conversation path. Credentials are not
read here.
"""
import argparse
import contextvars
import json
import math
import sys
import threading
from contextlib import contextmanager
from dataclasses import dataclass

LIVE_TEST_FLAG = "--live-test"
CAP_FLAG = "--cap-usd"
EXIT_REFUSED = 2

RULE = (
    "Model calls outside a conversation need an approved live test (System Hub decision 56).\n"
    "The only model spend is conversations: a participant's on the live engine, or a test\n"
    "conversation the project lead runs or approves by name with a dollar cap.\n"
    f"Run this command again with both {LIVE_TEST_FLAG} \"<name>\" and {CAP_FLAG} <dollars>.\n"
    "It prints its settings first, stops before the cap, and logs the name."
)

# What a guarded client may still reach: a metadata listing, never a model call.
_PASSTHROUGH_ATTRIBUTES = frozenset({"models"})
_DEFAULT_MAX_TOKENS = 4096
_CHARS_PER_TOKEN_FLOOR = 3  # fewer chars per token than English runs at, so the input estimate errs high


class LiveTestRefused(SystemExit):
    """The command does not carry an approved live test. Exits non-zero."""

    def __init__(self, message: str):
        super().__init__(EXIT_REFUSED)
        self.message = message


class LiveTestGuardError(Exception):
    """A call an approved run may not make: a model id it did not announce,
    a model with no approved price, a client surface other than messages."""


class LiveTestCapReached(Exception):
    """The next call could carry the priced total past the cap. Raised
    instead of making it, for this call and every call after."""


@dataclass(frozen=True)
class LiveTest:
    name: str
    cap_usd: float


_conversation: contextvars.ContextVar[bool] = contextvars.ContextVar("cic_conversation_scope", default=False)
_resolved_models: set[str] = set()
_run: "_Run | None" = None
_state_lock = threading.Lock()


def _emit(text: str) -> None:
    print(text, flush=True)


@contextmanager
def conversation_scope():
    """The conversation path in engine/api builds its client inside this. A
    test conversation Mark runs goes through the live engine and needs no
    flags; nothing outside engine/api opens this scope (a test enforces it)."""
    token = _conversation.set(True)
    try:
        yield
    finally:
        _conversation.reset(token)


def add_arguments(parser: argparse.ArgumentParser) -> None:
    """Both flags on a command's own parser, so --help shows them and the
    parser accepts them. The guard reads them from the process arguments
    itself; a command that forgets this line is refused, never unguarded."""
    group = parser.add_argument_group("live test (System Hub decision 56)")
    group.add_argument(LIVE_TEST_FLAG, metavar="NAME", help="the approved live test's name; required with --cap-usd for any model call")
    group.add_argument(CAP_FLAG, metavar="USD", type=float, help="the approved dollar cap; the run stops before it")


def parse_live_test(argv: list[str]) -> LiveTest | None:
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False, exit_on_error=False)
    parser.add_argument(LIVE_TEST_FLAG, default=None)
    parser.add_argument(CAP_FLAG, default=None)
    try:
        known, _ = parser.parse_known_args(argv)
    except argparse.ArgumentError:
        return None
    name = (known.live_test or "").strip()
    if not name or known.cap_usd is None:
        return None
    try:
        cap = float(known.cap_usd)
    except ValueError:
        return None
    if not math.isfinite(cap) or cap <= 0:
        return None
    return LiveTest(name=name, cap_usd=cap)


def admit() -> LiveTest | None:
    """None inside the conversation scope; the LiveTest the command carries
    otherwise. Exits non-zero, with the rule printed, when it carries none."""
    if _conversation.get():
        return None
    live_test = parse_live_test(sys.argv[1:])
    if live_test is None:
        print(RULE, file=sys.stderr, flush=True)
        raise LiveTestRefused(RULE)
    return live_test


def note_model(model_id: str) -> None:
    """A model id the run resolved, so the header can name it before the
    first call."""
    with _state_lock:
        _resolved_models.add(model_id)


def active_live_test_name() -> str | None:
    run = _run
    return run.live_test.name if run is not None else None


def priced_total() -> float:
    return _run.spent if _run is not None else 0.0


def run_summary() -> dict | None:
    """The approved run's name, cap, route and priced total, for the report
    it writes. None when this process is not running a live test."""
    run = _run
    if run is None:
        return None
    with run.lock:
        announced = list(run.announced or [])
        return {
            "name": run.live_test.name,
            "cap_usd": run.live_test.cap_usd,
            "route": describe_route(run.provider, announced, run.region),
            "model_ids": announced,
            "priced_total_usd": round(run.spent, 6),
        }


def describe_route(provider: str, model_ids: list[str], region: str | None) -> str:
    if provider == "anthropic":
        return "Anthropic API"
    from engine.m8.price_tables import route_factor

    kinds = {"regional" if route_factor(provider, m) != 1.0 else "global" if m.lower().startswith("global.") else "other" for m in model_ids}
    kind = "/".join(sorted(kinds)) if kinds else "unresolved"
    where = f", {region}" if region else ""
    return f"Bedrock, {kind} inference profile{where}"


def wrap(client, live_test: LiveTest | None, *, provider: str, region: str | None = None):
    """The client itself for a conversation; a capped, announcing proxy for
    an approved live test."""
    global _run
    if live_test is None:
        return client
    with _state_lock:
        if _run is None or _run.live_test != live_test:
            _run = _Run(live_test, provider=provider, region=region)
        run = _run
    return _GuardedClient(client, run)


def reset_for_tests() -> None:
    global _run
    with _state_lock:
        _run = None
        _resolved_models.clear()


class _Run:
    def __init__(self, live_test: LiveTest, *, provider: str, region: str | None):
        self.live_test = live_test
        self.provider = provider
        self.region = region
        self.spent = 0.0
        self.reserved = 0.0
        self.calls: list[dict] = []
        self.announced: list[str] | None = None
        self.cap_notice_given = False
        self.lock = threading.Lock()

    def _price(self, model_id: str):
        from engine.m8.price_tables import price_for_route

        table = price_for_route("voice_generation", model_id, self.provider)
        if table is None:
            raise LiveTestGuardError(f"no approved price for model {model_id!r}; a capped run cannot count its spend")
        return table

    def _announce(self, first_model: str) -> None:
        with _state_lock:
            ids = set(_resolved_models)
        ids.add(first_model)
        self.announced = sorted(ids)
        route = describe_route(self.provider, self.announced, self.region)
        _emit(
            f"LIVE TEST: {self.live_test.name}\n"
            f"CAP: ${self.live_test.cap_usd:.2f}\n"
            f"MODELS: {', '.join(self.announced)}\n"
            f"ROUTE: {route}"
        )

    def reserve(self, kwargs: dict) -> float:
        """Holds the most the call could cost against the cap before it is
        made, so parallel calls cannot jointly pass it. Returns the hold."""
        model_id = kwargs.get("model")
        if not isinstance(model_id, str) or not model_id:
            raise LiveTestGuardError("a capped run's call must name its model")
        table = self._price(model_id)
        with self.lock:
            if self.announced is None:
                self._announce(model_id)
            if model_id not in self.announced:
                raise LiveTestGuardError(f"model {model_id!r} was not in the settings printed before the first call: {', '.join(self.announced)}")
            input_tokens = len(json.dumps([kwargs.get("system"), kwargs.get("messages")], default=str)) / _CHARS_PER_TOKEN_FLOOR
            ceiling = input_tokens * max(table.input_per_token, table.cache_write_per_token) + (kwargs.get("max_tokens") or _DEFAULT_MAX_TOKENS) * table.output_per_token
            if self.spent + self.reserved + ceiling > self.live_test.cap_usd:
                if not self.cap_notice_given:
                    self.cap_notice_given = True
                    _emit(f"LIVE TEST CAP REACHED: {self.live_test.name}: priced total ${self.spent:.4f} of ${self.live_test.cap_usd:.2f}; no further calls.")
                raise LiveTestCapReached(f"live test {self.live_test.name!r}: the next call could pass the ${self.live_test.cap_usd:.2f} cap")
            self.reserved += ceiling
            return ceiling

    def settle(self, hold: float, model_id: str, usage) -> None:
        """Replaces the hold with the call's priced usage. No usage (a call
        that raised before answering) releases the hold at no cost."""
        from engine.m8.cost import estimate_cost
        from engine.provider.bedrock import normalize_usage

        dollars = 0.0
        entry = {"model_id": model_id, "priced_dollars": 0.0, "usage": None}
        if usage is not None:
            normalized = normalize_usage(usage)
            dollars = estimate_cost(normalized, self._price(model_id)).dollars
            entry = {
                "model_id": model_id, "priced_dollars": dollars,
                "usage": {
                    "input_tokens": normalized.input_tokens, "output_tokens": normalized.output_tokens,
                    "cache_creation_input_tokens": normalized.cache_creation_input_tokens, "cache_read_input_tokens": normalized.cache_read_input_tokens,
                },
            }
        with self.lock:
            self.reserved -= hold
            self.spent += dollars
            self.calls.append(entry)


class _GuardedStream:
    def __init__(self, manager, run: _Run, hold: float, model_id: str):
        self._manager = manager
        self._run = run
        self._hold = hold
        self._model_id = model_id
        self._stream = None

    def __enter__(self):
        try:
            self._stream = self._manager.__enter__()
        except BaseException:
            self._run.settle(self._hold, self._model_id, None)
            raise
        return self._stream

    def __exit__(self, exc_type, exc, tb):
        usage = None
        if self._stream is not None:
            try:
                usage = self._stream.get_final_message().usage if exc_type is None else self._stream.current_message_snapshot.usage
            except Exception:
                usage = None
        try:
            return self._manager.__exit__(exc_type, exc, tb)
        finally:
            self._run.settle(self._hold, self._model_id, usage)


class _GuardedMessages:
    def __init__(self, inner, run: _Run):
        self._inner = inner
        self._run = run

    def create(self, **kwargs):
        hold = self._run.reserve(kwargs)
        try:
            response = self._inner.create(**kwargs)
        except BaseException:
            self._run.settle(hold, kwargs["model"], None)
            raise
        self._run.settle(hold, kwargs["model"], getattr(response, "usage", None))
        return response

    def stream(self, **kwargs):
        hold = self._run.reserve(kwargs)
        try:
            manager = self._inner.stream(**kwargs)
        except BaseException:
            self._run.settle(hold, kwargs["model"], None)
            raise
        return _GuardedStream(manager, self._run, hold, kwargs["model"])

    def __getattr__(self, name):
        raise LiveTestGuardError(f"messages.{name} is not available to a capped live-test client")


class _GuardedClient:
    def __init__(self, inner, run: _Run):
        self._inner = inner
        self.messages = _GuardedMessages(inner.messages, run)

    def __getattr__(self, name):
        if name in _PASSTHROUGH_ATTRIBUTES:
            return getattr(self._inner, name)
        raise LiveTestGuardError(f"{name} is not available to a capped live-test client")
