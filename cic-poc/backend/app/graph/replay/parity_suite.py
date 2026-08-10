"""S4.1 replay-parity suite.

Two modes:
  record : drive the CURRENT endpoints live (real API) with every
           boundary function taped; save per-case tape (pickle) +
           outcome snapshot (JSON). Run BEFORE the refactor - this
           freezes the old paths' behavior.
  replay : drive the (refactored) endpoints with boundaries served from
           the tapes; compare outcomes against the snapshots. The ONLY
           tolerated extra calls are the declared-delta table checks on
           the plain path (served canned no-signal results and logged).

Cases cover: ordinary single-world flows on both endpoints, all four
intercepts FIRING (frame-breaker, relational-safety, epistemology
bridge, modern-term bridge - recorded real outputs, which is what makes
ordering observable), and the multi-world selector + table checks.

Usage (from cic-poc/backend):
  python -m app.graph.replay.parity_suite record
  python -m app.graph.replay.parity_suite replay
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BACKEND))

FIXDIR = Path(__file__).with_name("suite")

CASES = [
 ("P1-plain-ordinary", "plain", ["desert-monasticism"],
  "Why did you leave ordinary village life for the desert?"),
 ("P2-plain-framebreaker", "plain", ["desert-monasticism"],
  "Are you a real person or an AI? Be honest."),
 ("P3-plain-relational", "plain", ["post-apostolic-house-church"],
  "I don't really know why I'm even talking to you. Nothing matters "
  "anymore. Honestly I've been thinking about ending things. I don't "
  "think anyone would even notice if I was gone."),
 ("P4-plain-multiworld", "plain",
  ["post-apostolic-house-church", "desert-monasticism",
   "syriac-edessa-nisibis"],
  "How did each of your communities understand prayer?"),
 ("S1-stream-ordinary", "stream", ["desert-monasticism"],
  "What is the discernment you speak of?"),
 ("S2-stream-epistemology", "stream", ["desert-monasticism"],
  "How do we actually know any of this really happened? What's "
  "documented versus guessed?"),
 ("S3-stream-modernterm", "stream", ["post-apostolic-house-church"],
  "What did your community believe about transubstantiation?"),
 ("S4-stream-multiworld", "stream",
  ["post-apostolic-house-church", "desert-monasticism",
   "syriac-edessa-nisibis"],
  "What did each of you fear most?"),
]


def outcome_plain(resp_json: dict, mask_facilitator_text: bool = False) -> dict:
    # mask_facilitator_text: P2's frame-breaker facilitator answer is
    # generated INLINE in the endpoint (not a boundary function), so its
    # text is real-API nondeterministic on both old and new paths. The
    # routing (who spoke, in what order) is the property under test; the
    # text is masked and the masking is declared in the parity report.
    # scope to THE TURN: the response echoes the whole conversation, and
    # everything before the participant's message (the session-start
    # reception/handoff) is live-generated per run - not the unit under
    # test. Compare only what this turn produced.
    all_msgs = resp_json["messages"]
    last_user = max(i for i, m in enumerate(all_msgs) if m["role"] == "user")
    msgs = []
    for m in all_msgs[last_user + 1:]:
        content = m["content"]
        if mask_facilitator_text and m.get("name") == "facilitator":
            content = "<masked: inline-generated, nondeterministic>"
        msgs.append({"name": m.get("name"), "role": m["role"],
                     "content": content})
    return {
        "kind": "plain",
        "phase": resp_json["phase"],
        "turn_count": resp_json["turn_count"],
        "messages": msgs,
    }


def outcome_stream(sse_text: str) -> dict:
    events = []
    for block in sse_text.split("\n\n"):
        for line in block.splitlines():
            if line.startswith("data: "):
                try:
                    ev = json.loads(line[len("data: "):])
                except Exception:
                    continue
                # token events are collapsed into per-speaker text so the
                # snapshot is chunking-insensitive but content-exact
                events.append(ev)
    collapsed, buf, speaker = [], [], None
    for ev in events:
        if ev.get("type") == "token":
            if speaker != ev.get("speaker") and buf:
                collapsed.append({"type": "text", "speaker": speaker,
                                   "text": "".join(buf)})
                buf = []
            speaker = ev.get("speaker")
            buf.append(ev.get("text", ""))
        else:
            if buf:
                collapsed.append({"type": "text", "speaker": speaker,
                                   "text": "".join(buf)})
                buf, speaker = [], None
            collapsed.append(ev)
    if buf:
        collapsed.append({"type": "text", "speaker": speaker,
                           "text": "".join(buf)})
    return {"kind": "stream", "events": collapsed}


def run_case(client, case, mode_tag):
    name, kind, worlds, message = case
    r = client.post("/api/session/start",
                    json={"world_ids": worlds} if len(worlds) > 1
                          else {"world_id": worlds[0]})
    r.raise_for_status()
    body = r.json()
    sid = body["session_id"]
    # session_auth.py: /message and /message/stream are possession-gated on
    # X-Session-Token since this suite's tapes/snapshots were built - a
    # request without it now 403s before reaching any of the boundaries
    # this suite actually exists to check.
    auth_headers = {"X-Session-Token": body["session_token"]}
    if kind == "plain":
        resp = client.post(f"/api/session/{sid}/message",
                           json={"message": message}, headers=auth_headers)
        resp.raise_for_status()
        return outcome_plain(resp.json(),
                             mask_facilitator_text=(name == "P2-plain-framebreaker"))
    resp = client.post(f"/api/session/{sid}/message/stream",
                       json={"message": message}, headers=auth_headers)
    resp.raise_for_status()
    return outcome_stream(resp.text)


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "record"
    only = set(sys.argv[2:])
    FIXDIR.mkdir(exist_ok=True)

    from fastapi.testclient import TestClient
    from app.main import app
    from app.graph.replay.recorder import Tape, recording, replaying

    client = TestClient(app)
    failures = []
    for case in CASES:
        name = case[0]
        if only and name not in only:
            continue
        tape_path = FIXDIR / f"{name}.tape.pkl"
        snap_path = FIXDIR / f"{name}.outcome.json"
        if mode == "record":
            tape = Tape()
            with recording(tape):
                outcome = run_case(client, case, "record")
            tape.save(tape_path)
            (FIXDIR / f"{name}.tape.json").write_text(
                json.dumps(tape.export(), indent=1), encoding="utf-8")
            snap_path.write_text(json.dumps(outcome, indent=1,
                                             ensure_ascii=False),
                                 encoding="utf-8")
            print(f"[record] {name}: {len(tape.entries)} taped calls")
        else:
            tape = Tape.load(tape_path)
            # declared delta: the plain path gains the five table checks
            if case[1] == "plain":
                tape.delta_labels = {
                    "check_dominance": list,
                    "check_convergence": list,
                    "check_cross_world_vocabulary_drift": list,
                    "check_length_ceiling": list,
                    "check_question_stacking": list,
                }
            expected = json.loads(snap_path.read_text(encoding="utf-8"))
            try:
                with replaying(tape):
                    outcome = run_case(client, case, "replay")
                    tape.assert_consumed()
            except AssertionError as exc:
                failures.append((name, f"tape assertion: {exc}"))
                print(f"[replay] {name}: FAIL ({exc})")
                continue
            if outcome != expected:
                failures.append((name, "outcome mismatch"))
                diff_path = FIXDIR / f"{name}.replay-diff.json"
                diff_path.write_text(json.dumps(outcome, indent=1,
                                                 ensure_ascii=False),
                                     encoding="utf-8")
                print(f"[replay] {name}: OUTCOME MISMATCH -> {diff_path.name}")
            else:
                extra = f"; delta calls: {tape.delta_calls}" if tape.delta_calls else ""
                print(f"[replay] {name}: PARITY OK{extra}")
    if mode == "replay":
        print(f"\n{len(CASES) - len(failures)}/{len(CASES)} cases at parity")
        return 1 if failures else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
