"""What a voiced round and a safety check really cost, read from the usage log.

Aggregate numbers only: no session id, no world, no address leaves this module.
Every call is priced with the approved price tables, a call on a model with no
approved price at the dearest approved price (engine.m8.price_tables.DEAREST).

The log keeps, for each model call, its kind, its model, its token counts
(cache reads and cache writes among them) and the time it was written. It does
not keep which message a call belonged to, so a message is rebuilt: every call
from one session's safety check up to the next safety check is one message. A
message with a voice call is a voiced round, and its round number is how many
voiced messages the session has had. A round's cache was warm when its voice call
read cached tokens, and cold when it did not. The pause before a round is the
time between the end of the previous round's last voice call and the end of this
round's first one, which includes the model's own time and the person's.
Interview (solo) sessions only: a Table's calls are priced in the totals, not in
the per-round tables.
"""
import statistics
from collections import defaultdict
from datetime import datetime, timedelta

from engine.m8 import price_tables
from engine.m8.cost import estimate_cost
from engine.m7.session_reader import read_session
from engine.m8.price_tables import DEAREST
from engine.m8.usage import SYSTEM_SESSION_ID, UsageRecord

ROUND_COLUMNS = 10
PAUSE_BUCKETS = (("under_5_min", 300.0), ("5_to_60_min", 3600.0), ("over_60_min", None))
SOLO = "interview"


def _price(record: UsageRecord) -> tuple[float, bool]:
    """The call's list-price dollars, and whether it fell back to the dearest price."""
    table = price_tables.price_for_call(record.call_kind, record.model_id)
    dollars = estimate_cost(record.usage, table or DEAREST).dollars or 0.0
    return dollars, table is None


def _mean(values: list[float]) -> float | None:
    return round(statistics.fmean(values), 5) if values else None


def _median(values: list[float]) -> float | None:
    return round(statistics.median(values), 5) if values else None


class _Message:
    __slots__ = ("start", "voice", "voice_usd", "other_usd", "safety_usd", "warm")

    def __init__(self, start: datetime):
        self.start = start
        self.voice: list[datetime] = []
        self.voice_usd = 0.0
        self.other_usd = 0.0
        self.safety_usd = 0.0
        self.warm = False


def _messages(calls: list[tuple[datetime, UsageRecord]]) -> tuple[list[_Message], int]:
    """One session's calls, oldest first, split into messages, and how many calls had no approved price."""
    messages: list[_Message] = []
    fallback = 0
    for when, record in calls:
        dollars, unpriced = _price(record)
        fallback += unpriced
        if record.call_kind == "safety_call" or not messages:
            messages.append(_Message(when))
        message = messages[-1]
        if record.call_kind == "voice_generation":
            message.voice.append(when)
            message.voice_usd += dollars
            message.warm = message.warm or record.usage.cache_read_input_tokens > 0
        else:
            message.other_usd += dollars
            if record.call_kind == "safety_call":
                message.safety_usd += dollars
    return messages, fallback


def _bucket(seconds: float) -> str:
    for name, limit in PAUSE_BUCKETS:
        if limit is None or seconds < limit:
            return name
    return PAUSE_BUCKETS[-1][0]


def _window_totals(rows: list[tuple[datetime, str, _Message]], since: datetime) -> dict:
    voice = gate = unvoiced = 0.0
    messages = voiced = 0
    for when, _session, message in rows:
        if when < since:
            continue
        messages += 1
        voice += message.voice_usd
        gate += message.other_usd
        if message.voice:
            voiced += 1
        else:
            unvoiced += message.other_usd
    return {
        "messages": messages, "voiced_rounds": voiced, "unvoiced_messages": messages - voiced,
        "total_usd": round(voice + gate, 4), "voice_usd": round(voice, 4), "safety_and_other_usd": round(gate, 4),
        "unvoiced_messages_usd": round(unvoiced, 4),
    }


def kinds_of(store, session_ids) -> dict[str, str]:
    """Each session's kind from the conversation store: "internal" for our own test
    sessions, otherwise its mode. A session the store does not hold is left out."""
    kinds: dict[str, str] = {}
    for session_id in session_ids:
        session = read_session(store, session_id)
        if session is not None:
            kinds[session_id] = "internal" if session.internal else session.mode
    return kinds


def report_for(store, usage_store, now: datetime) -> dict:
    """The report over the last 30 days of the usage log."""
    timed = usage_store.read_timed_since((now - timedelta(days=30)).isoformat())
    return build(timed, kinds_of(store, {record.session_id for _written, record in timed}), now)


def build(timed: list[tuple[str, UsageRecord]], session_kinds: dict[str, str], now: datetime) -> dict:
    """timed: (written-at ISO time, record), oldest first. session_kinds: session id to
    "interview", "table" or "internal"; a session not in it is of unknown kind."""
    by_session: dict[str, list[tuple[datetime, UsageRecord]]] = defaultdict(list)
    our_own: set[str] = set()
    for written, record in timed:
        if record.session_id == SYSTEM_SESSION_ID or record.live_test:
            continue
        if session_kinds.get(record.session_id) == "internal":
            our_own.add(record.session_id)
            continue
        by_session[record.session_id].append((datetime.fromisoformat(written), record))
    totals_only = 0

    rows: list[tuple[datetime, str, _Message]] = []
    rounds: dict[int, list[_Message]] = defaultdict(list)
    cache_rows: list[tuple[str, bool, float]] = []
    unpriced_calls = 0
    for session, calls in by_session.items():
        messages, fallback = _messages(calls)
        unpriced_calls += fallback
        solo = session_kinds.get(session) == SOLO
        if not solo:
            totals_only += 1
        previous_end: datetime | None = None
        round_no = 0
        for message in messages:
            rows.append((message.start, session, message))
            if not message.voice:
                continue
            round_no += 1
            if solo:
                rounds[min(round_no, ROUND_COLUMNS + 1)].append(message)
                if round_no >= 2 and previous_end is not None:
                    cache_rows.append((_bucket((message.voice[-1] - previous_end).total_seconds()), message.warm, message.voice_usd))
            previous_end = message.voice[-1]

    round_table = []
    for number in range(1, ROUND_COLUMNS + 2):
        group = rounds.get(number, [])
        round_table.append({
            "round": str(number) if number <= ROUND_COLUMNS else f"{ROUND_COLUMNS + 1} and later",
            "rounds": len(group),
            "voice_usd_mean": _mean([m.voice_usd for m in group]),
            "voice_usd_median": _median([m.voice_usd for m in group]),
            "voice_and_safety_usd_mean": _mean([m.voice_usd + m.other_usd for m in group]),
            "cache_warm_share": round(sum(m.warm for m in group) / len(group), 3) if group else None,
        })

    def split(group: list[tuple[str, bool, float]]) -> dict:
        warm = [usd for _b, w, usd in group if w]
        cold = [usd for _b, w, usd in group if not w]
        return {
            "rounds": len(group),
            "voice_usd_mean": _mean([usd for _b, _w, usd in group]),
            "warm": {"rounds": len(warm), "voice_usd_mean": _mean(warm)},
            "cold": {"rounds": len(cold), "voice_usd_mean": _mean(cold)},
        }

    cache = {"all_rounds_from_the_second": split(cache_rows)}
    cache["by_pause_before_the_round"] = [
        {"pause": name, **split([r for r in cache_rows if r[0] == name])} for name, _limit in PAUSE_BUCKETS
    ]

    checked = [m for _w, _s, m in rows]
    unvoiced = [m for m in checked if not m.voice]
    safety = {
        "messages": len(checked),
        "safety_call_usd_mean": _mean([m.safety_usd for m in checked]),
        "safety_and_other_calls_usd_mean": _mean([m.other_usd for m in checked]),
        "messages_with_no_voice_reply": len(unvoiced),
        "no_voice_message_usd_mean": _mean([m.other_usd for m in unvoiced]),
        "no_voice_messages_usd_total": round(sum(m.other_usd for m in unvoiced), 4),
    }

    return {
        "generated_at": now.isoformat(),
        "window_days": 30,
        "sessions": {
            "counted": len(by_session), "left_out_as_our_own": len(our_own), "counted_in_totals_only_not_per_round": totals_only,
        },
        "calls_priced_at_the_dearest_price": unpriced_calls,
        "voiced_rounds_by_round_number": round_table,
        "cache": cache,
        "safety_checks": safety,
        "totals": {
            "last_7_days": _window_totals(rows, now - timedelta(days=7)),
            "last_30_days": _window_totals(rows, now - timedelta(days=30)),
        },
        "how_it_is_read": (
            "A message is every call from one safety check to the next. A round is a message with a voice call. "
            "Warm means the voice call read cached tokens. The pause is from the end of the previous round's last voice call "
            "to the end of this round's first, so it includes the model's own time."
        ),
    }
