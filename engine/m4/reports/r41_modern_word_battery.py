"""R41 measurement (Rulings-Pending.md R41 and R41-A, both ruled
2026-09-23): when a participant's own question carries a modern word
with no equivalent in the Representative's world, does the voice name it
as the participant's own word and answer from its record - or does it
define the word, falsely map it onto its world's nearest concept, or
date the term from outside its record? R41-A: the Facilitator bridge
turn retires once this measurement ("definitions, false mappings, dating
claims, out of twenty") comes back near zero. Whether a result is "near
zero" is Mark's reading, never this script's - it counts and quotes.

WHAT THE VOICE SEES TODAY. The fleet modern_term registry holds exactly
one record (_fleet.modern.trinity, origin_year 325), anachronistic only
for pahc among the real worlds. Every other modern word already reaches
the voice unbridged, under the fleet voice record's own pronoun_rule
clause. For the one registered case (pahc, "Trinity") this harness
replaces engine.api.wiring.compute_anachronistic_term_ids with an empty
set for the duration of the call - harness-side only, no production
code changed - so routing falls through to the voice exactly as the R41
build would make it. The safety and reader gate calls still run for
real. The real (unpatched) registered set is recorded per probe.

PROBES. 11 real worlds (not fix). Per world, two test probes carrying a
modern word, and one in-window control using a word from that world's
own term records (world_word), which the voice should use plainly, not
treat as the participant's foreign word. Each test word's only claim
here is "later than this world's window end", by centuries in every
case; the anchor recorded in MODERN_WORDS is the standard reference
point for the word's coining or defining moment, not a first-attestation
study. "Transubstantiation" is excluded on purpose: pronoun_rule's own
clause uses it as its example, so it would measure recall of the prompt,
not the behaviour. "The Rapture" is excluded: 1 Thessalonians 4:17's
"caught up" gives an honest in-record answer that would read as a false
mapping. pahc's "Trinity" is reported separately (registered term, and
the fleet record's origin_year is itself open to question - see the PR).

GRADER. Haiku 4.5 via forced tool use, the engine.m1.rendering_fidelity
idiom. Each reply is graded twice. A risk counts only when both runs
flag it AND at least one quoted evidence span appears verbatim in the
reply; a split vote, or a flag whose evidence is not verbatim, is
reported as unsettled for a human read - never scored by the model.

COST. 33 live voice turns (each = safety + reader + voice, Haiku/Sonnet
priced as in engine.m8.live_cost_run) plus 66 grader calls. The run
aborts before the next probe once the running total passes COST_CAP.

Run: python3 -m engine.m4.reports.r41_modern_word_battery --region us-east-1
"""
import argparse
import json
import pathlib
import re
import sys
import tempfile
import time
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from anthropic import APIError, APITimeoutError, RateLimitError

from engine.api import wiring
from engine.api.wiring import create_session, handle_message, _load_world
from engine.m1.loader import load_fleet_records
from engine.m1.registry import load_registry
from engine.m4.store import Store
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.live_cost_run import HAIKU_4_5_PRICE_TABLE, SONNET_4_5_PRICE_TABLE
from engine.m8.log_store import UsageLogStore
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPORT_PATH = pathlib.Path(__file__).resolve().parent / "r41-modern-word-battery-2026-09-24.json"
COST_CAP = 3.00
GRADER_MODEL_PATTERN = "us.anthropic.claude-haiku-4-5"
GRADES_PER_REPLY = 2
_RATE_LIMIT_MAX_RETRIES = 5
_RATE_LIMIT_BASE_DELAY_SECONDS = 2.0

# word -> (question template, anchor for "later than the window").
MODERN_WORDS = {
    "Protestant": ("{name}, would you call your community Protestant?",
                   "the Protestation at the Diet of Speyer, 1529"),
    "papal infallibility": ("{name}, did your church believe in papal infallibility?",
                            "defined at the First Vatican Council (Pastor Aeternus), 1870"),
    "sola scriptura": ("{name}, did your people hold to sola scriptura?",
                       "sixteenth-century Reformation formula"),
    "liberation theology": ("{name}, was your faith a kind of liberation theology?",
                            "Gustavo Gutierrez, A Theology of Liberation, 1971"),
    "fundamentalism": ("{name}, were your people fundamentalists?",
                       "'fundamentalist' coined by Curtis Lee Laws, 1920"),
    "Pentecostal": ("{name}, was your church Pentecostal?",
                    "the Pentecostal movement, Topeka 1901 / Azusa Street 1906"),
    "secularism": ("{name}, how did your people deal with secularism?",
                   "'secularism' coined by George Jacob Holyoake, 1851"),
    "Trinity": ("{name}, what did your households believe about the Trinity?",
                "fleet record _fleet.modern.trinity, origin_year 325 (registered, bridged today)"),
}

TEST_PROBES = {
    "alx": ["papal infallibility", "liberation theology"],
    "cappadocian": ["Protestant", "sola scriptura"],
    "desert": ["Protestant", "liberation theology"],
    "don": ["papal infallibility", "sola scriptura"],
    "gallic": ["papal infallibility", "Protestant"],
    "hal": ["sola scriptura", "liberation theology"],
    "ijc": ["papal infallibility", "Protestant"],
    "lpc": ["papal infallibility", "sola scriptura"],
    "pahc": ["Trinity", "sola scriptura"],
    "syr": ["Protestant", "liberation theology"],
    "rzg": ["fundamentalism", "Pentecostal"],
    "witt": ["secularism", "Pentecostal"],
}

# world -> (term record id, the word a participant would type). The word
# is taken from that record's own world_word field.
CONTROL_PROBES = {
    "alx": ("alx.term.allegoria", "allegoria"),
    "cappadocian": ("cappadocian.term.apatheia", "apatheia"),
    "desert": ("desert.term.geron-abba-amma", "abba"),
    "don": ("don.term.confessor", "confessor"),
    "gallic": ("gallic.term.anchorite-hermit", "anchorite"),
    "hal": ("hal.term.hebraica-veritas", "Hebraica veritas"),
    "ijc": ("ijc.term.homoousios", "homoousios"),
    "lpc": ("lpc.term.libelli", "libelli"),
    "pahc": ("pahc.term.episkopos", "episkopos"),
    "syr": ("syr.term.madrasha", "madrasha"),
    "rzg": ("rzg.term.consistory", "Consistory"),
    "witt": ("witt.term.catechism", "catechism"),
}
CONTROL_TEMPLATE = "{name}, what did {word} mean to your people?"

TEST_RISKS = ("defines_modern_word", "false_mapping", "dating_claim_outside_record", "etic_seam")

TEST_SYSTEM_PROMPT = """You are grading one reply from a historical Representative: a voice speaking \
only from the recorded life of one historical Christian world, within a fixed window of years. The \
participant's question used a modern word that did not exist in that world. The project's rule: the \
Representative names the word as the participant's own word, and answers only from what its own world \
actually had. It never explains the modern word.

Report each of these as true or false:
- names_as_participants_word: the reply treats the word as the participant's, not its own (e.g. "the \
word you are using", "your word").
- defines_modern_word: the reply explains or defines what the modern word means, in whole or in part \
(e.g. "Protestants are those who broke with Rome"). Merely repeating the word, or saying it is not a \
word the world used, is NOT a definition.
- false_mapping: the reply equates the modern word with something in its own world, as if they were \
the same thing or a version of it (e.g. "what you call X, we called Y", "yes, we were X in our way"). \
Answering the underlying question from the world's own practice, without saying the modern word is \
that practice, is NOT a false mapping.
- dating_claim_outside_record: the reply places the modern word or what it names in time from a vantage \
the world could not have had (e.g. "that came a thousand years after us", "that belongs to the Reformation"). \
Saying only that the world did not have or use the word is NOT a dating claim.
- etic_seam: the reply steps outside the world's own voice to speak as a modern narrator, historian, or \
assistant (e.g. "historians note", "in modern terms").

For every item you mark true, add an evidence entry naming that item and copying the exact words \
from the reply that show it, character for character. Judge only what the reply says, not whether it is historically correct."""

CONTROL_SYSTEM_PROMPT = """You are grading one reply from a historical Representative: a voice speaking \
only from the recorded life of one historical Christian world. The participant's question used a word \
that this world itself used. The Representative should use it plainly as its own word.

Report each of these as true or false:
- treated_as_foreign: the reply treats the word as the participant's word, or as a word its world did \
not have (e.g. "the word you are using", "that is not our word").
- etic_seam: the reply steps outside the world's own voice to speak as a modern narrator, historian, or \
assistant.

For every item you mark true, add an evidence entry naming that item and copying the exact words \
from the reply that show it, character for character."""


def _verdict_tool(fields):
    props = {f: {"type": "boolean"} for f in fields}
    props["evidence"] = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {"item": {"type": "string", "enum": list(fields)}, "quote": {"type": "string"}},
            "required": ["item", "quote"],
        },
    }
    props["reasoning"] = {"type": "string"}
    return {
        "name": "submit_r41_verdict",
        "description": "Submit the verdict for one Representative reply.",
        "input_schema": {"type": "object", "properties": props, "required": list(fields) + ["evidence", "reasoning"]},
    }


TEST_TOOL = _verdict_tool(("names_as_participants_word",) + TEST_RISKS)
CONTROL_TOOL = _verdict_tool(("treated_as_foreign", "etic_seam"))


def _norm(text: str) -> str:
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = text.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", text).strip().lower()


def quote_is_verbatim(quote: str, reply: str) -> bool:
    q = _norm(quote).strip(" .,\"'")
    return bool(q) and q in _norm(reply)


def grade_once(client, model_id, *, system, tool, user_content):
    delay = _RATE_LIMIT_BASE_DELAY_SECONDS
    for attempt in range(_RATE_LIMIT_MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=model_id, max_tokens=700, system=system, tools=[tool],
                tool_choice={"type": "tool", "name": tool["name"]},
                messages=[{"role": "user", "content": user_content}], timeout=30.0,
            )
            break
        except APITimeoutError:
            return {"status": "timeout"}, 0.0
        except RateLimitError as e:
            if attempt == _RATE_LIMIT_MAX_RETRIES:
                return {"status": "error", "error": f"rate limited: {e}"}, 0.0
            time.sleep(delay)
            delay *= 2
        except APIError as e:
            return {"status": "error", "error": str(e)}, 0.0
    dollars = estimate_cost(normalize_usage(response.usage), HAIKU_4_5_PRICE_TABLE).dollars or 0.0
    uses = [b for b in response.content if b.type == "tool_use" and b.name == tool["name"]]
    if not uses:
        return {"status": "parse_failure"}, dollars
    return {"status": "ok", **uses[0].input}, dollars


def settle(grades, fields, reply):
    """Per field: "yes"/"no" when every run succeeded and all agree, else
    "unsettled". A "yes" also needs at least one evidence quote for that
    same field found verbatim in the reply - a flag the grader cannot
    anchor in the reply's own words is not counted."""
    ok = [g for g in grades if g.get("status") == "ok"]
    out = {}
    for f in fields:
        votes = [bool(g.get(f)) for g in ok]
        if not grades or len(ok) < len(grades) or len(set(votes)) != 1:
            out[f] = "unsettled"
        elif votes[0]:
            anchored = any(
                e.get("item") == f and quote_is_verbatim(e.get("quote") or "", reply)
                for g in ok for e in (g.get("evidence") or [])
            )
            out[f] = "yes" if anchored else "unsettled"
        else:
            out[f] = "no"
    return out


def _price_for_call_kind(call_kind):
    return HAIKU_4_5_PRICE_TABLE if call_kind in ("safety_call", "reader_call", "turn_selector") else SONNET_4_5_PRICE_TABLE


def _run_turn(*, world_key, message, bypass_bridge, client, voice_model_id, safety_model_id, registry, loader):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix=f"cic-r41-{world_key}-"))
    store, usage_store = Store(tmp / "events.db"), UsageLogStore(tmp / "usage.db")
    session_id, _code = create_session(store=store, world_loader=loader, registry=registry, world_key=world_key)
    original = wiring.compute_anachronistic_term_ids
    if bypass_bridge:
        wiring.compute_anachronistic_term_ids = lambda *_a, **_k: set()
    try:
        result = handle_message(
            store=store, usage_store=usage_store, world_loader=loader, registry=registry,
            voice_client=client, voice_model_id=voice_model_id,
            safety_client=client, safety_model_id=safety_model_id,
            session_id=session_id, text=message,
        )
    finally:
        wiring.compute_anachronistic_term_ids = original
    records = usage_store.read_for_session(session_id)
    dollars = sum((estimate_cost(r.usage, _price_for_call_kind(r.call_kind)).dollars or 0.0) for r in records)
    return result, len(records), dollars


def run(region: str) -> dict:
    voice_model_id = resolve_model_id("us.anthropic.claude-sonnet-4-5", region)
    safety_model_id = resolve_model_id("us.anthropic.claude-haiku-4-5", region)
    grader_model_id = resolve_model_id(GRADER_MODEL_PATTERN, region)
    client = make_client(region)
    registry = load_registry()
    loader = LazyWorldLoader()
    fleet = load_fleet_records()

    specs = []
    for world_key, words in TEST_PROBES.items():
        for i, word in enumerate(words, 1):
            specs.append(("test", f"{world_key}-T{i}", world_key, word, None))
    for world_key, (record_id, word) in CONTROL_PROBES.items():
        specs.append(("control", f"{world_key}-C", world_key, word, record_id))

    probes, running, aborted = [], 0.0, None
    for kind, probe_id, world_key, word, record_id in specs:
        if running > COST_CAP:
            aborted = f"cost cap ${COST_CAP} passed at ${running:.4f} before {probe_id}"
            print(aborted, flush=True)
            break
        world = _load_world(loader, registry, world_key)
        name = world.frame["representative"]["name"]
        window = world.frame["time_window"]
        registered = sorted(wiring.compute_anachronistic_term_ids(fleet, window))
        message = (MODERN_WORDS[word][0] if kind == "test" else CONTROL_TEMPLATE).format(name=name, word=word)
        print(f"{probe_id}: {message}", flush=True)
        result, calls, dollars = _run_turn(
            world_key=world_key, message=message, bypass_bridge=(kind == "test"), client=client,
            voice_model_id=voice_model_id, safety_model_id=safety_model_id, registry=registry, loader=loader,
        )
        voice = result.voice or {}
        reply = voice.get("text") or ""
        grades, settled = [], None
        if reply:
            system, tool = (TEST_SYSTEM_PROMPT, TEST_TOOL) if kind == "test" else (CONTROL_SYSTEM_PROMPT, CONTROL_TOOL)
            user_content = (
                f"World: {registry[world_key]['display_name']}, {window['start']}-{window['end']} AD.\n"
                f"The participant's word: {word}\nThe participant asked: {message}\n\nThe reply:\n{reply}"
            )
            for _ in range(GRADES_PER_REPLY):
                g, d = grade_once(client, grader_model_id, system=system, tool=tool, user_content=user_content)
                grades.append(g)
                dollars += d
            fields = (("names_as_participants_word",) + TEST_RISKS) if kind == "test" else ("treated_as_foreign", "etic_seam")
            settled = settle(grades, fields, reply)
        running += dollars
        probes.append({
            "probe_id": probe_id, "kind": kind, "world_key": world_key, "word": word,
            "word_anchor": MODERN_WORDS[word][1] if kind == "test" else None,
            "control_record_id": record_id, "registered_anachronistic_term_ids": registered,
            "bridge_bypassed": kind == "test" and bool(registered),
            "message": message, "routing_action": result.routing_action, "routing_reason": result.routing_reason,
            "voice_reached": bool(reply), "facilitator_text": (result.facilitator or {}).get("text"),
            "voice_text": reply, "citations": voice.get("citations", []),
            "grades": grades, "settled": settled, "calls_made": calls + len(grades), "dollars": round(dollars, 4),
        })
        print(f"  routing={result.routing_action} settled={settled} ${dollars:.4f} (running ${running:.4f})", flush=True)

    return summarize(probes, region, aborted)


def summarize(probes, region, aborted):
    def count(kind, field, value, only=None):
        return sum(1 for p in probes if p["kind"] == kind and p["settled"] and p["settled"][field] == value
                   and (only is None or only(p)))

    tests = [p for p in probes if p["kind"] == "test"]
    unregistered = lambda p: not p["registered_anachronistic_term_ids"]  # noqa: E731
    per_risk = {}
    for f in ("names_as_participants_word",) + TEST_RISKS:
        per_risk[f] = {
            "yes": count("test", f, "yes"), "unsettled": count("test", f, "unsettled"),
            "yes_unregistered_only": count("test", f, "yes", unregistered),
        }
    per_world = {}
    for p in probes:
        w = per_world.setdefault(p["world_key"], {"probes": [], "dollars": 0.0})
        w["probes"].append({"probe_id": p["probe_id"], "word": p["word"], "routing_action": p["routing_action"], "settled": p["settled"]})
        w["dollars"] = round(w["dollars"] + p["dollars"], 4)
    return {
        "asof": datetime.now(timezone.utc).isoformat(),
        "region": region,
        "aborted": aborted,
        "total_dollars": round(sum(p["dollars"] for p in probes), 4),
        "total_calls": sum(p["calls_made"] for p in probes),
        "voice_turns": len(probes),
        "test_probes": len(tests),
        "test_probes_voice_reached": sum(1 for p in tests if p["voice_reached"]),
        "control_probes": len(probes) - len(tests),
        "per_risk": per_risk,
        "controls_treated_as_foreign": {"yes": count("control", "treated_as_foreign", "yes"),
                                        "unsettled": count("control", "treated_as_foreign", "unsettled")},
        "controls_etic_seam": {"yes": count("control", "etic_seam", "yes"),
                               "unsettled": count("control", "etic_seam", "unsettled")},
        "per_world": per_world,
        "probes": probes,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default="us-east-1")
    args = parser.parse_args()
    start = time.monotonic()
    report = run(args.region)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nReal cost: ${report['total_dollars']} ({report['total_calls']} calls, {report['voice_turns']} voice turns), "
          f"{time.monotonic() - start:.1f}s")
    print(json.dumps(report["per_risk"], indent=2))
    print(f"Report: {REPORT_PATH}")
