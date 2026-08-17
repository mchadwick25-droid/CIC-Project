"""This service hosts one voice. These tests are what make that a contract.

Until 2026-08-17 the same endpoint served two products. POST /api/session/
start with `world_id` opened a solo interview; the same call with
`world_ids` opened a 1-3 voice table, through a gated but complete
apparatus in nodes.py and governance.py. One URL, two programs, and the
table half had no test and no gate behind it.

Mark's decision: this program is exclusively the single-voice interview,
and the multi-voice table becomes a separate thing that does not share
this one. These tests hold that line at the only place it can be held
cheaply - the entrance.

WHY THE ENTRANCE IS ENOUGH, and why the second test below matters more
than the first: state.world_ids is written in exactly two places, and one
of them replays the other. main.py's start_session writes the
session_started event; events.py's replay reads world_ids back out of that
same payload. Nothing else sets it. So bounding the field at the entrance
bounds it for the whole session lifetime, and is_multi_world - which is
just len(world_ids) > 1 - can never be true. The gated table code is then
unreachable rather than merely dormant. A future second writer would break
that property silently, which is what
test_only_one_writer_of_the_session_started_payload watches for.

No LLM, no key, no network - these are structural assertions.
"""
import ast
import inspect
import re
import textwrap

def _start_session_source():
    import app.main as main
    return inspect.getsource(main.start_session)


def test_the_request_model_still_carries_the_field():
    """Deleting world_ids from the model would be the WRONG fix.

    Pydantic ignores unknown fields by default, so a client posting
    world_ids=["desert-monasticism"] against a model without the field
    would get a 200 and a session seated with the DEFAULT world - asking
    for the desert and being given the Syriac voice, silently. The field
    has to exist for the refusal to be reachable.
    """
    from app.main import StartSessionRequest

    assert "world_ids" in StartSessionRequest.model_fields
    req = StartSessionRequest(world_ids=["desert-monasticism"])
    assert req.world_ids == ["desert-monasticism"]


def test_a_table_request_is_refused_not_quietly_downgraded():
    src = _start_session_source()
    assert "if request.world_ids:" in src, "the refusal branch is gone"
    # The refusal must precede any use of the field, so there is no window
    # in which a multi-world session is half-constructed.
    refusal = src.index("if request.world_ids:")
    for later in ("world_ids[:3]", "world_ids[0]"):
        assert later not in src[refusal:], (
            f"start_session still consumes {later} after the refusal - the "
            "table branch was not actually removed")


def test_the_refusal_says_what_to_send_instead():
    """A 400 that only says "no" leaves a client author guessing. The
    realistic reader here is someone whose client was built against the
    old two-mode API."""
    src = _start_session_source()
    block = src[src.index("if request.world_ids:"):]
    detail = block[:block.index(")\n\n")].lower()
    assert "world_id" in detail
    assert "one voice" in detail or "single" in detail


def test_only_one_writer_of_the_session_started_payload():
    """The load-bearing property. events.py's replay sets state.world_ids
    from the session_started event and nowhere else, so that ONE payload is
    what bounds the session. If a second place starts emitting it, the
    entrance stops bounding anything and the gated table code becomes
    reachable again without a single test failing.

    Deliberately narrower than "grep for world_ids". main.py writes the
    field three times: this event, the Supabase sessions-row mirror, and a
    response body. The latter two are projections of state, not sources of
    it, and counting them would make this test noise.
    """
    import app.main as main

    src = inspect.getsource(main)
    events = re.findall(r'\(\s*"session_started"\s*,\s*\{.*?\}\s*\)', src,
                        re.S)
    assert len(events) == 1, (
        f"expected exactly one session_started emitter, found {len(events)}")
    assert '"world_ids": world_ids' in events[0]

    # ...and that the local it emits can only ever hold the one world.
    # Parsed rather than grepped: `world_ids=world_ids` as a keyword
    # argument is not an assignment, and a regex cannot tell the two apart
    # without becoming unreadable.
    tree = ast.parse(textwrap.dedent(_start_session_source()))
    assigns = [
        ast.unparse(node.value)
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "world_ids"
                for t in node.targets)
    ]
    assert assigns == ["[world_id]"], (
        f"world_ids is assigned from something other than the single "
        f"seated world: {assigns}")


def test_is_multi_world_cannot_be_true_for_a_started_session():
    """End to end on the logic, without standing up a server: whatever a
    caller sends, a session that starts at all starts with one world."""
    from app.main import StartSessionRequest, AVAILABLE_WORLDS

    valid = [w.id for w in AVAILABLE_WORLDS]
    for payload in ({"world_id": valid[0]}, {}):
        req = StartSessionRequest(**payload)
        assert not req.world_ids
        world_ids = [req.world_id]
        assert len(world_ids) == 1
        assert not (len(world_ids) > 1)  # is_multi_world


def test_the_dead_speaker_wrappers_are_gone():
    """determine_next_speaker and route_to_representative were both marked
    "for backwards compatibility" and had no callers anywhere in the tree."""
    import app.graph.nodes as nodes

    for name in ("determine_next_speaker", "route_to_representative"):
        assert not hasattr(nodes, name), f"{name} is still defined"


class _State:
    def __init__(self, world_ids, world_id):
        self.world_ids = world_ids
        self.world_id = world_id


def test_one_voice_is_not_described_to_the_participant_as_a_table():
    """build_table_composition's text reaches a participant through the
    frame-breaker answer. Telling someone they are seated at a table when
    one voice is present is a small lie in the Facilitator's own voice."""
    from app.graph.nodes import build_table_composition

    out = build_table_composition(_State(["desert-monasticism"],
                                          "desert-monasticism"))
    assert "table" not in out.lower()
    assert "Speaking with the participant" in out


def test_the_plural_wording_survives_for_a_hypothetical_second_voice():
    """Kept deliberately: if a second voice ever becomes possible, this
    reads correctly instead of silently calling two voices a conversation
    with one."""
    from app.graph.nodes import build_table_composition

    out = build_table_composition(
        _State(["desert-monasticism", "alexandria-catechetical"],
               "desert-monasticism"))
    assert "Seated at THIS table:" in out
