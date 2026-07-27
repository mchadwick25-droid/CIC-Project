"""
The anachronism bridge (a.k.a. the reverse lexicon) — the third classify-then-
route intercept, mirroring classify_frame_breaker / classify_relational_safety.

This is FACILITATOR behavior and is WORLD-AGNOSTIC: it works the exact same way
for every world, with no per-world authoring. When a participant asks a seated
Representative about a modern theological term that Representative's world never
held, the Facilitator names it as later, gives its modern sense neutrally, and
hands the Representative only the term-free UNDERLYING SUBJECT — never the modern
term. The Representative then answers from its own world's life and terms (or says
honestly that its world held nothing like it). The participant draws the line
between then and now themselves.

What makes it world-agnostic:
- definitions.json is a world-agnostic dictionary - since S4.5 a GENERATED VIEW
  over the modern_term records (wrs/records/facilitator/modern_term/, Pass 1
  §3.11), carrying each term's distinguishing_claim and native_subject_map.
- Whether the bridge fires is DERIVED, not authored: a term bridges for a world
  only when its origin_year postdates that world's end year. S4.5 (Pass 1 §6.6):
  anachronism is evaluated against EVERY seated world - migrated worlds' own
  `world_core.time_window.end_year` is authoritative; unmigrated worlds keep the
  manifest `period` parse exactly as before (compatibility classification). When
  seated worlds differ ("the Trinity" at a pre-Nicaea house-church beside a
  conciliar-era world), the bridge speaks the SPLIT honestly - later vocabulary
  for one, native to the other's window - which is a better formation moment
  than either wrong answer.
- The classifier sees each term's distinguishing_claim (§9.4's structural fix):
  a bare universal question is NONE because no distinguishing formula is
  present, not because a hand-written example said so.
- The reframed question persists as a `bridge_reframe` event every
  Representative reads as the question actually asked (§6.6/§6.7) - ending the
  asymmetry where world 1 answered the reframe while worlds 2..n answered the
  raw modern-term question.

Design: Ministry/Technology/CiC_Anachronism_Bridge_Spec_V0_1.md, superseded in
        the four ways above by Pass 1 §6.6/§3.11 (blueprint S4.5).
Data:   backend/data/modern_term_bridge/definitions.json  (generated view)
"""

import json
import re
from functools import lru_cache
from pathlib import Path

import yaml
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.graph.state import ConversationState

_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "modern_term_bridge"
_RECORDS_ROOT = Path(__file__).resolve().parents[2] / "wrs" / "records"


_CLASSIFIER_PROMPT = """You are classifying a single incoming participant message for the anachronism bridge. This classifier has no Representative-generation role - it only decides routing, and it runs before any Representative is invoked.

Your only job: decide whether the participant is asking about ONE specific MODERN theological term from the list below - a term/concept from a later period of Christianity.

Each candidate below carries its DISTINGUISHING CLAIM - the specific formula that separates the narrow, period-specific term from the universal root word it is built on. The distinguishing claim is your test, term by term.

Candidate terms:
{candidates}

Rules:
- Output the single term_id (exactly as written above) ONLY IF the message is genuinely asking about that term or its concept - "what's your view of X", "do you believe in X", "how does X work", or clearly invoking the concept in other words.
- Output NONE for anything else - above all for a world's OWN native topics (the meal, the letters, who leads, martyrdom, mercy, the desert cell, the covenant, scholarship). Those are not modern terms and must never be bridged.
- A message may mention a word in passing without asking about the modern doctrine - that is NONE. Fire only when the modern term/concept is what the participant actually wants addressed.
- The structural test: a bare question about a universal Christian concept that merely SHARES A WORD with a term's name is NONE - every era has discussed faith, grace, sin, love, hope; only later eras coined the specific formulas below. Match a term ONLY when the participant's own words invoke that term's stated distinguishing claim, not just its root word. If no candidate's distinguishing claim is present in the message, the answer is NONE - structurally, whatever the topic.
- When unsure, output NONE. A missed term is caught later by drift monitoring; a wrong interruption is not recoverable.
- Match at most ONE term, the closest. Output nothing but that term_id, or NONE.

Message:
{message}
"""


def _extract_piece(content) -> str:
    if isinstance(content, list):
        return "".join(
            b.get("text", "") for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return content or ""


@lru_cache(maxsize=1)
def _load_definitions() -> dict:
    """term_id -> definition dict (world-agnostic)."""
    with open(_DATA_DIR / "definitions.json", encoding="utf-8") as f:
        data = json.load(f)
    return {t["term_id"]: t for t in data.get("terms", [])}


@lru_cache(maxsize=1)
def _world_core_end_years() -> dict[str, int]:
    """world_id -> time_window.end_year for every MIGRATED world (one that
    carries a world_core record). S4.5: for these worlds the record is
    authoritative (Pass 1 §3.10); unmigrated worlds fall through to the
    manifest parse below - the compatibility classification."""
    out: dict[str, int] = {}
    try:
        for p in _RECORDS_ROOT.glob("*/world_core/*.md"):
            try:
                front = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
                tw = (front or {}).get("time_window") or {}
                if front.get("world_id") and tw.get("end_year"):
                    out[front["world_id"]] = int(tw["end_year"])
            except Exception:
                continue
    except Exception:
        pass
    return out


@lru_cache(maxsize=None)
def _world_end_year(world_id: str) -> int | None:
    """
    The last year of a world's span. Migrated worlds: their own
    world_core.time_window.end_year (S4.5). Unmigrated worlds: parsed
    generically from the manifest `period` string exactly as before
    (e.g. "70–200 CE" -> 200, "c. 382–420 CE" -> 420). None if nothing
    can be read - in which case the bridge treats every dictionary term
    as anachronistic (safe default for the pre-modern worlds shipped so
    far).
    """
    from_record = _world_core_end_years().get(world_id)
    if from_record is not None:
        return from_record
    try:
        from app.world_manifest import get_manifest_entry
        period = get_manifest_entry(world_id).period or ""
        years = [int(y) for y in re.findall(r"\d{1,4}", period)]
        return max(years) if years else None
    except Exception:
        return None


def _is_anachronistic(term: dict, world_id: str) -> bool:
    """A term is anachronistic for a world when it originated AFTER the world's
    span ended. If the world's end year is unknown, default to True (bridge)."""
    end_year = _world_end_year(world_id)
    if end_year is None:
        return True
    return int(term.get("origin_year", 99999)) > end_year


def classify_modern_term(message: str, seated_world_ids: list[str]) -> dict | None:
    """
    Decide whether `message` asks about a modern term anachronistic for a seated
    world. Returns None (-> normal flow) or a match dict:

      {"term_id", "world_id",            # world_id = the world that answers beat 3
       "anachronistic_for": [...],       # S4.5: evaluated per EVERY seated world
       "native_for": [...],
       "split": bool}                    # some seated worlds native, some not

    S4.5 semantics (Pass 1 §6.6): no seated world anachronistic -> None (before,
    only the FIRST seated world was consulted - a native-first-world table
    silently skipped the bridge even when a later-seated world needed it, and
    vice versa). All anachronistic -> classic bridge, first seated world answers
    the term-free subject (unchanged). Split -> the honest split: the FIRST
    NATIVE world answers the term from inside its own era; the Facilitator
    names the split; the anachronistic worlds join on the underlying subject in
    the round's continuation. Fails toward None (a false positive has no
    backstop; a false negative is caught by the temporal_bleed drift monitor).
    """
    try:
        definitions = _load_definitions()
        if not definitions or not seated_world_ids:
            return None

        lines = [
            f"- {tid}: forms: {'; '.join(d.get('display_terms', [tid]))}\n"
            f"  distinguishing claim: {d.get('distinguishing_claim', '(none recorded)')}"
            for tid, d in definitions.items()
        ]
        from app.graph.nodes import CLASSIFIER_MAX_TOKENS, _MONITORING_MODEL, get_monitoring_llm
        from app.usage_logging import log_llm_usage

        llm = get_monitoring_llm(max_tokens=CLASSIFIER_MAX_TOKENS)
        response = llm.invoke([
            SystemMessage(content=_CLASSIFIER_PROMPT.format(
                candidates="\n".join(lines), message=message)),
            HumanMessage(content="Classify the message above."),
        ])
        log_llm_usage("modern_term_bridge", response, _MONITORING_MODEL)
        result = (response.content or "").strip()
        if not result:
            return None

        first = result.split()[0].strip().strip(".:,").lower()
        term_id = None
        if first in definitions:
            term_id = first
        else:
            low = result.lower()
            for tid in definitions:
                if tid in low:
                    term_id = tid
                    break
        if term_id is None:
            return None

        # S4.5: the date gate runs per seated world, not first-world-only
        term = definitions[term_id]
        anach = [w for w in seated_world_ids if _is_anachronistic(term, w)]
        native = [w for w in seated_world_ids if w not in anach]
        if not anach:
            return None
        answering = native[0] if native else seated_world_ids[0]
        return {"term_id": term_id, "world_id": answering,
                "anachronistic_for": anach, "native_for": native,
                "split": bool(native)}
    except Exception:
        return None


def stream_modern_term_bridge(state: ConversationState, match: dict):
    """
    Beats 1-2 (Facilitator: name-as-later + neutral modern sense), then the
    Representative answers the term-free UNDERLYING SUBJECT in its own world's
    terms - or says honestly its world held nothing like it. World-agnostic: the
    subject and definition come from the shared dictionary; the Representative
    supplies its own world's content. Yields normalized events. The handback
    message injected for the Representative is NEVER persisted to the transcript
    (spec section 5) - only the `complete` messages yielded here are.
    """
    from app.config import settings
    from app.graph.nodes import (
        REACTIVE_TURN_MAX_TOKENS,
        get_llm,
        stream_representative_turn,
    )
    from app.usage_logging import log_llm_usage
    from app.prompts.facilitator_prompts import (
        FACILITATOR_MODERN_TERM_BRIDGE_PROMPT,
        get_representative_message_name,
        get_representative_name,
    )

    definitions = _load_definitions()
    term = definitions[match["term_id"]]
    rep_name = get_representative_name(match["world_id"])
    subject = term.get("underlying_subject", "what your world actually held here")
    is_split = bool(match.get("split")) and match.get("native_for")

    display_term = (term.get("display_terms") or [term["term_id"]])[0]
    if is_split:
        # S4.5 (Pass 1 §6.6): the honest split - the term is native to one
        # seated world's window and later vocabulary for another. The
        # Facilitator says exactly that; the native world answers the term
        # from inside its own era; the others join on the underlying
        # subject as the round continues.
        native_names = ", ".join(get_representative_name(w)
                                  for w in match["native_for"])
        anach_names = ", ".join(get_representative_name(w)
                                 for w in match["anachronistic_for"])
        handback = (
            f"Then say plainly that this is where the worlds at this table part "
            f"in time: for {native_names}'s era this way of putting it is their "
            f"own vocabulary, while {anach_names}'s world came before it was "
            f"worked out - so you will let {rep_name} answer it from inside "
            f"their own era first, and the others will speak to {subject} from "
            "their own ground. Do not answer it yourself."
        )
        prompt = FACILITATOR_MODERN_TERM_BRIDGE_PROMPT.format(
            term=display_term,
            modern_sense=term["modern_sense"],
            period=term.get("period_originated", "a later period"),
            representative_name=(
                f"{anach_names} (while {native_names} lived in the term's own era)"),
            handback=handback,
        )
    else:
        handback = (
            f"Then hand back to {rep_name}: say you will ask what {rep_name}'s own world "
            f"actually held about {subject}, in {rep_name}'s own terms - and that if "
            f"{rep_name}'s world had nothing like it, {rep_name} will say so plainly. Do "
            "not answer it yourself."
        )
        prompt = FACILITATOR_MODERN_TERM_BRIDGE_PROMPT.format(
            term=display_term,
            modern_sense=term["modern_sense"],
            period=term.get("period_originated", "a later period"),
            representative_name=rep_name,
            handback=handback,
        )

    # --- Beats 1-2: the Facilitator, alone. ---
    yield {"type": "speaker_start", "speaker": "facilitator"}
    llm = get_llm(max_tokens=REACTIVE_TURN_MAX_TOKENS)
    full_text = ""
    usage_chunk = None
    for chunk in llm.stream([
        SystemMessage(content=prompt),
        HumanMessage(content="Respond as the Facilitator, per your instructions above."),
    ]):
        usage_chunk = chunk if usage_chunk is None else usage_chunk + chunk
        piece = _extract_piece(chunk.content)
        if piece:
            full_text += piece
            yield {"type": "token", "speaker": "facilitator", "text": piece}
    log_llm_usage("modern_term_bridge_facilitator_turn", usage_chunk,
                  settings.llm_model, session_id=state.session_id)
    yield {"type": "speaker_end", "speaker": "facilitator", "citations": None}
    yield {
        "type": "complete",
        "speaker": "facilitator",
        "message": AIMessage(content=full_text, name="facilitator"),
    }

    # --- Beat 3: the answering Representative. Classic bridge: the
    # term-free underlying subject. Split (S4.5): the NATIVE world answers
    # the term itself, from inside its own era - it needs no reframe. ---
    # The reframed table question is emitted as a `reframe` event below and
    # persisted by the caller as a bridge_reframe event + transcript entry
    # (§6.6: every Representative reads the question actually asked) - the
    # injected per-turn handback message itself is still never persisted.
    rep_message_name = get_representative_message_name(match["world_id"])
    reframed_question = (
        f"For each world at this table, in its own words: what did your community "
        f"actually hold about {subject}? Answer only from your world's own life and "
        "terms. If your world had nothing like this, say so plainly - that silence "
        "is itself worth naming."
    )
    yield {
        "type": "reframe",
        "question": reframed_question,
        "term_id": match["term_id"],
        "subject": subject,
        "split": bool(is_split),
        "anachronistic_for": match.get("anachronistic_for", [match["world_id"]]),
        "native_for": match.get("native_for", []),
        # §3.11: the per-world native-record pointers, carried on the event
        # for audit and for Phase 5's assembly/quick-reach consumption -
        # the bridge itself consumes the map's *evaluation* (who answers,
        # and how), declared in the S4.5 artifact
        "native_subject_map": term.get("native_subject_map") or {},
    }
    if is_split:
        handback_message = (
            f"The participant has asked about {display_term} - vocabulary of your "
            f"own world's era. Answer it from inside your own world's life and "
            "terms, as your own; the other worlds at this table will speak to the "
            "underlying matter from their own ground."
        )
        retrieval_query = subject
    else:
        handback_message = (
            f"In your own world, and in your own words: what did your community actually "
            f"hold about {subject}? Answer only from your world's own life and terms. If "
            "your world had nothing like this, say so plainly - that silence is itself "
            "worth naming."
        )
        retrieval_query = subject
    working_state = ConversationState(
        messages=list(state.messages) + [HumanMessage(content=handback_message)],
        # S3.5 (Pass 1 R9): retrieval searches the extracted SUBJECT, not
        # this handback boilerplate - the bridge already computed the
        # underlying subject deterministically, no extra call needed
        retrieval_query_override=retrieval_query,
        phase=state.phase,
        current_speaker="representative",
        current_world_id=match["world_id"],
        turn_count=state.turn_count,
        retrieved_context=state.retrieved_context,
        worlds_at_table=state.worlds_at_table,
        world_capsule_core=state.world_capsule_core,
        permanent_prompt=state.permanent_prompt,
        session_id=state.session_id,
        world_id=state.world_id,
        world_ids=state.world_ids,
    )

    yield {"type": "speaker_start", "speaker": rep_message_name}
    rep_message = None
    for event in stream_representative_turn(working_state, is_reactive=False):
        if event["type"] == "token":
            yield {"type": "token", "speaker": event["speaker"], "text": event["text"]}
        elif event["type"] == "complete":
            rep_message = event["message"]
    yield {
        "type": "speaker_end",
        "speaker": rep_message_name,
        "citations": rep_message.additional_kwargs.get("citations") if rep_message else None,
    }
    if rep_message is not None:
        yield {"type": "complete", "speaker": rep_message_name, "message": rep_message}
