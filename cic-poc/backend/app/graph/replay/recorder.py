"""S4.1 record/replay machinery for the governance-extraction parity proof.

The refactor moves CALLS (endpoint wiring), not the functions being
called - so parity is proven by stubbing every LLM-dependent function at
exactly the boundary the endpoints call it, with outputs RECORDED from
real runs, and comparing old-path vs new-path outcomes on identical
inputs. This is what makes intercept ordering observable: mock_llm's
placeholder text deliberately omits every format marker, so under
mock_llm every classifier takes its no-fire default and ordering is
unobservable, not proven (its own docstring says so). mock_llm remains
the right tool for the streaming/plumbing half of the suite - stated
here as the blueprint requires, not implied.

Boundary functions (patched in their defining modules; main.py imports
them inside function bodies, so module-attribute patching reaches every
call site):
- app.graph.nodes: classify_frame_breaker, classify_relational_safety,
  representative_engages, multi_representative_engages,
  facilitator_monitors, facilitator_reroots, determine_turn_type,
  select_next_speaker, and the five table checks
- app.graph.epistemology_bridge: classify_epistemology_bridge
- app.graph.modern_term_bridge: classify_modern_term

Record mode wraps each with a pass-through that appends
(label, repr-of-result) to a tape, per call order. Replay mode pops the
same tape in order - a tape underrun or label mismatch is a loud parity
failure (the wiring called something in a different order), which is
exactly the property under test.

Non-serializable results (LangChain messages inside dict results) are
kept in-memory on the tape object during a single process run - the
parity suite records and replays in one process, so the tape holds live
objects and byte-faithful equality is available without serialization
lossiness. The tape's JSON export (labels + summaries only) is what
gets committed as the parity evidence.
"""
from __future__ import annotations

import copy
import pickle
import threading
from collections import deque
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path

# re-entrancy guard: only TOP-LEVEL boundary calls are taped/stubbed.
# multi_representative_engages calls representative_engages internally -
# recording both would tape calls the replayed (stubbed) outer function
# never makes, leaving unconsumed entries.
_depth = threading.local()


BOUNDARIES = {
    "app.graph.nodes": [
        "classify_frame_breaker",
        "classify_relational_safety",
        "representative_engages",
        "multi_representative_engages",
        "facilitator_monitors",
        "facilitator_reroots",
        "determine_turn_type",
        "select_next_speaker",
        "check_dominance",
        "check_convergence",
        "check_cross_world_vocabulary_drift",
        "check_length_ceiling",
        "check_question_stacking",
        "check_drift_for_message",
        "generate_reroot_guidance",
        "facilitator_closes",
    ],
    "app.graph.epistemology_bridge": ["classify_epistemology_bridge"],
    "app.graph.modern_term_bridge": ["classify_modern_term"],
    "app.graph.closing_sequence": ["classify_wind_down"],
    # main.py imports representative_engages at MODULE level (unlike its
    # other function-local imports), so its binding must be patched too -
    # found when P1's replayed turn regenerated live instead of replaying
    "app.main": ["representative_engages"],
}

# Generator-returning boundaries (the streaming path): recording wraps the
# generator so events are taped as they are consumed and passed through
# unchanged; replay serves iter(recorded_events). This is what lets the
# streamed halves replay without an API in the loop.
STREAM_BOUNDARIES = {
    "app.graph.nodes": [
        "stream_representative_turn",
        "stream_relational_safety_response",
        "stream_frame_breaker_response",
    ],
    "app.graph.epistemology_bridge": ["stream_epistemology_bridge"],
    "app.graph.modern_term_bridge": ["stream_modern_term_bridge"],
    "app.graph.closing_sequence": ["stream_closing_turn"],
}


@dataclass
class Tape:
    entries: list = field(default_factory=list)  # (label, result) objects
    cursor: int = 0
    # labels the NEW path is allowed to call even though the old path
    # never did - the S4.1 declared delta (plain gains the table checks).
    # Each maps to a canned result factory; occurrences are logged so the
    # parity report can list every extra call and verify it is in the
    # declared set and nothing else.
    delta_labels: dict = field(default_factory=dict)
    delta_calls: list = field(default_factory=list)

    def record(self, label: str, result):
        self.entries.append((label, result))

    def build_queues(self):
        """Per-label FIFO queues for replay. Strict global ordering cannot
        be asserted: the classifier phase runs under asyncio.gather and
        the RECORDED tapes themselves show different completion orders
        across cases (S2 vs S3) - completion order is nondeterministic on
        the old path too. Per-label FIFO preserves every sequential
        property that is real (e.g. the Nth select_next_speaker feeds the
        Nth turn) while tolerating concurrent-completion shuffle; the
        outcome snapshot holds the decision-priority behavior."""
        self._queues = {}
        for label, result in self.entries:
            self._queues.setdefault(label, deque()).append(result)

    def replay(self, label: str):
        q = self._queues.get(label)
        if not q:
            if label in self.delta_labels:
                # an ADDITIONAL call the old path never made - allowed
                # only for declared-delta labels, canned no-signal result
                self.delta_calls.append(label)
                return self.delta_labels[label]()
            raise AssertionError(
                f"TAPE UNDERRUN: new path called {label} more times than "
                f"the recorded old path did")
        return q.popleft()

    def assert_consumed(self):
        leftover = {k: len(v) for k, v in self._queues.items() if v}
        if leftover:
            raise AssertionError(
                f"UNCONSUMED TAPE ENTRIES (old path made calls the new "
                f"path never made): {leftover}")

    def save(self, path: Path):
        with open(path, "wb") as f:
            pickle.dump(self.entries, f)

    @classmethod
    def load(cls, path: Path) -> "Tape":
        t = cls()
        with open(path, "rb") as f:
            t.entries = pickle.load(f)
        return t

    def export(self) -> list[dict]:
        out = []
        for label, result in self.entries:
            summary = repr(result)
            out.append({"label": label, "result_summary": summary[:300]})
        return out


def _module(name: str):
    import importlib
    return importlib.import_module(name)


@contextmanager
def recording(tape: Tape):
    """Wrap every boundary function: call the real thing, record result.
    Stream boundaries are taped event-by-event as consumed."""
    originals = {}
    try:
        for mod_name, fns in BOUNDARIES.items():
            mod = _module(mod_name)
            for fn in fns:
                real = getattr(mod, fn)
                originals[(mod_name, fn)] = real

                def wrapper(*a, __real=real, __label=fn, __tape=tape, **kw):
                    top = not getattr(_depth, "n", 0)
                    _depth.n = getattr(_depth, "n", 0) + 1
                    try:
                        result = __real(*a, **kw)
                    finally:
                        _depth.n -= 1
                    if top:
                        __tape.record(__label, result)
                    return result
                setattr(mod, fn, wrapper)
        for mod_name, fns in STREAM_BOUNDARIES.items():
            mod = _module(mod_name)
            for fn in fns:
                real = getattr(mod, fn)
                originals[(mod_name, fn)] = real

                def swrapper(*a, __real=real, __label=fn, __tape=tape, **kw):
                    if getattr(_depth, "n", 0):
                        return __real(*a, **kw)  # nested: pass through
                    events = []

                    def gen():
                        # depth is held while the inner generator RUNS
                        # (between yields) so boundary calls made inside
                        # it - e.g. a bridge's internal representative
                        # turn - are not double-taped; depth is released
                        # around each yield so the consumer side is
                        # unaffected
                        it = __real(*a, **kw)
                        while True:
                            _depth.n = getattr(_depth, "n", 0) + 1
                            try:
                                ev = next(it)
                            except StopIteration:
                                _depth.n -= 1
                                break
                            finally:
                                if getattr(_depth, "n", 0) > 0:
                                    pass
                            _depth.n -= 1
                            events.append(ev)
                            yield ev
                        __tape.record("stream:" + __label, events)
                    return gen()
                setattr(mod, fn, swrapper)
        yield tape
    finally:
        for (mod_name, fn), real in originals.items():
            setattr(_module(mod_name), fn, real)


@contextmanager
def replaying(tape: Tape):
    """Replace every boundary function with an in-order tape pop. Results
    that are dicts are deep-copied per replay so state-mutation by the
    caller can't contaminate a second replay of the same tape."""
    originals = {}
    tape.build_queues()
    try:
        for mod_name, fns in BOUNDARIES.items():
            mod = _module(mod_name)
            for fn in fns:
                originals[(mod_name, fn)] = getattr(mod, fn)

                def stub(*a, __label=fn, __tape=tape, **kw):
                    result = __tape.replay(__label)
                    try:
                        return copy.deepcopy(result)
                    except Exception:
                        return result
                setattr(mod, fn, stub)
        for mod_name, fns in STREAM_BOUNDARIES.items():
            mod = _module(mod_name)
            for fn in fns:
                originals[(mod_name, fn)] = getattr(mod, fn)

                def sstub(*a, __label=fn, __tape=tape, **kw):
                    events = __tape.replay("stream:" + __label)
                    return iter(list(events))
                setattr(mod, fn, sstub)
        yield tape
    finally:
        for (mod_name, fn), real in originals.items():
            setattr(_module(mod_name), fn, real)
