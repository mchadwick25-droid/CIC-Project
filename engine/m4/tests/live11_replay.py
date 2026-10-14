"""Offline replay of the eleven-world live tests of 13 October and of the 14
October retest: each recorded reply rebuilt as the voice wrote it, run back
through the reply shaping a turn applies (engine.m4.turn.settle_reply), with
no model call. A run is named in RUNS.

The reports keep every sentence of each draft, with its tags and quote
marker, but not the draft whole: the sentences shown are kept in order with
their paragraph sizes, and the sentences cut are listed apart, in the order
they were cut. `rebuild_draft` puts the cut sentences back. A placement-cut
lead-in goes back before the marker sentence cut with it, words cut after an
attribution go back after that attribution, a stray closing mark rejoins the
marker sentence it was cut from, and any other cut sentence goes back after
the shown sentence that shares the most tags and words with it. The order of
the cut sentences among the shown ones is therefore rebuilt, not recorded.
Run under the engine each test ran on, the rebuilt drafts give back every
recorded reply (66 on 13 October, 42 on 14 October).

Records are the world's own records under records/, which the tests'
packages were compiled from."""
import json
import re
from functools import lru_cache
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m4 import evidence, grounding_net
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import apply_net, settle_reply
from engine.prose import quote_aware_sentences

REPO_ROOT = Path(__file__).resolve().parents[3]
REPORTS = REPO_ROOT / "engine" / "m4" / "reports"
AUDITS = REPO_ROOT / "Build" / "Ministry" / "Operations" / "Audits"
# Each run: its report files, the independent reading of it, and the worlds
# it completed.
RUNS = {
    "eleven-world-test": {
        "report": "live-turn-report-{world}-2026-10-13-eleven-world-test.json",
        "reading": AUDITS / "live11_eleven_world_test_reading_2026-10-13.json",
        "worlds": ("alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "rzg", "syr", "witt"),
    },
    "retest": {
        "report": "live-turn-report-{world}-2026-10-14-retest.json",
        "reading": AUDITS / "live11_retest_reading_2026-10-14.json",
        "worlds": ("alx", "desert", "hal", "ijc", "pahc", "rzg", "syr"),
    },
}
FIRST_RUN = "eleven-world-test"
WORLDS = RUNS[FIRST_RUN]["worlds"]

_PLACEMENT_LEAD_IN = "lead-in to a quote that was not placed"
_AFTER_ATTRIBUTION = "words after an attribution, not a placed quote"
_SECOND_QUOTE = "second placed quote in one reply"
_STRAY = re.compile(r"^[\s\"'“”‘’.,;:!?]+$")
# Where the rule above puts a cut sentence in the wrong place, the place it
# had, read from the recorded reply: the cut sentence's opening words, to the
# opening words of the shown sentence it followed.
CUT_PLACED_AFTER = {
    ("retest", "desert", 5): {"He said: these are my sins": "The elders who had called him asked"},
}
_WORD = re.compile(r"[a-z]+")


@lru_cache(maxsize=None)
def report(world: str, run: str = FIRST_RUN) -> dict:
    return json.loads((REPORTS / RUNS[run]["report"].format(world=world)).read_text())


@lru_cache(maxsize=None)
def records(world: str) -> dict:
    return load_world_records(world)


def _words(draft: str) -> set[str]:
    return set(_WORD.findall(draft.lower())) | set(grounding_net._TAG.findall(draft))


def rebuild_draft(voice_event: dict, placed_after: dict[str, str] | None = None) -> str:
    """The draft as the voice wrote it, rebuilt as the module docstring says.
    A cut marker sentence that opened a quotation the voice typed gets that
    quotation's closing mark back after its marker when no stray mark was
    left standing to rejoin it: the recorded draft ends at the marker, and
    placement cut the mark that followed it.
    `placed_after` is the turn's CUT_PLACED_AFTER entry."""
    grounding = voice_event["grounding"]
    sizes = [p["sentence_count"] for p in grounding["paragraph_coverage"]]
    shown = [s["draft"] for s in grounding["sentences"]]
    paragraphs, start = [], 0
    for size in sizes:
        paragraphs.append(list(shown[start : start + size]))
        start += size
    strays = [(p, i) for p, para in enumerate(paragraphs) for i, d in enumerate(para) if _STRAY.match(d)]
    placed: list[tuple[int, int]] = []

    def insert_after(p: int, i: int, draft: str) -> tuple[int, int]:
        paragraphs[p].insert(i + 1, draft)
        placed[:] = [(pp, ii + 1 if pp == p and ii > i else ii) for pp, ii in placed]
        strays[:] = [(pp, ii + 1 if pp == p and ii > i else ii) for pp, ii in strays]
        return p, i + 1

    def bare_marker(p: int, i: int) -> bool:
        return 0 <= i < len(paragraphs[p]) and not _words(grounding_net.QUOTE_MARKER.sub("", paragraphs[p][i]))

    cuts = voice_event["reply_shape"]["removed"]
    # A second marker was refused only because an earlier one had been placed:
    # it goes back after the last marker the reply carries.
    cuts = [c for c in cuts if c["why"] != _SECOND_QUOTE] + [c for c in cuts if c["why"] == _SECOND_QUOTE]
    for n, cut in enumerate(cuts):
        draft = cut["draft"]
        if grounding_net.QUOTE_MARKER.search(draft) and draft.rstrip().endswith("]]") and draft.count('"') % 2 and not strays:
            draft = draft.rstrip() + '."'
        anchor = next((after for head, after in (placed_after or {}).items() if draft.startswith(head)), None)
        # an attribution whose followers were cut took the rest of its
        # paragraph with it, so nothing shown followed it there
        opens_rest = n + 1 < len(cuts) and cuts[n + 1]["why"] == _AFTER_ATTRIBUTION
        if anchor is not None:
            at = next(insert_after(p, i, draft) for p, para in enumerate(paragraphs)
                      for i, d in enumerate(para) if d.startswith(anchor))
        elif cut["why"] == _SECOND_QUOTE:
            marked = [(p, i) for p, para in enumerate(paragraphs) for i, d in enumerate(para)
                      if grounding_net.QUOTE_MARKER.search(d)]
            at = insert_after(*marked[-1], draft) if marked else insert_after(len(paragraphs) - 1, len(paragraphs[-1]) - 1, draft)
        elif cut["why"] == _PLACEMENT_LEAD_IN and placed:
            p, i = placed[-1]
            at = insert_after(p, i - 1, draft)
        elif cut["why"] == _AFTER_ATTRIBUTION and placed:
            at = insert_after(*placed[-1], draft)
        elif grounding_net.QUOTE_MARKER.search(draft) and draft.rstrip().endswith("]]") and strays:
            p, i = strays.pop(0)
            paragraphs[p][i] = draft + paragraphs[p][i].strip()
            at = (p, i)
        else:
            own = _words(draft)
            best, best_score = None, 0
            for p, para in enumerate(paragraphs):
                for i, kept in enumerate(para):
                    score = len(own & _words(kept))
                    if score and score >= best_score:
                        best, best_score = (p, i), score
            if best is None:
                paragraphs.append([])
                best = (len(paragraphs) - 1, -1)
            if opens_rest:
                best = (best[0], len(paragraphs[best[0]]) - 1)
            if draft.lstrip()[:1] in "\"“":
                # a typed quotation standing alone, with no lead-in cut beside it, closed the reply
                best = (len(paragraphs) - 1, len(paragraphs[-1]) - 1)
            # never between a lead-in and the bare marker it introduces
            while bare_marker(best[0], best[1] + 1):
                best = (best[0], best[1] + 1)
            at = insert_after(*best, draft)
        placed.append(at)
    return "\n\n".join(" ".join(para) for para in paragraphs if para)


def turns(run: str = FIRST_RUN) -> list[dict]:
    """Every turn of every world in a run, with what the turn's net was
    given: the quotes offered, the quotes and stories the conversation had
    already cited, and the participant's words so far."""
    out = []
    for world in RUNS[run]["worlds"]:
        told: set[str] = set()
        asked: list[str] = []
        for number, result in enumerate(report(world, run)["results"], start=1):
            voice_event = result["result"]["voice_event"]
            asked.append(result["message"])
            out.append({
                "world": world, "q": number, "message": result["message"], "voice_event": voice_event,
                "told": frozenset(told), "asked": list(asked), "run": run,
            })
            told |= {rid for c in voice_event["citations"] for rid in c["record_ids"]}
    return out


def replay(turn: dict) -> dict:
    """The reply the rebuilt draft gives now: (text, net_result, fallback)."""
    world_records = records(turn["world"])
    voice_event = turn["voice_event"]
    kinds = {rid: (world_records.get(rid) or {}).get("record_type") for rid in turn["told"]}
    placement = PlacementContext(
        offered=frozenset(voice_event["offered_ids"].get("quote", [])),
        voiced=frozenset(r for r, k in kinds.items() if k == "quote"),
        told_stories=frozenset(r for r, k in kinds.items() if k == "story"),
    )
    thin = evidence.thin_topics_for(world_records)

    def net(raw):
        return apply_net(raw, repository_records=world_records, thin_topics=thin,
                         quotable_texts=turn["asked"], placement=placement)

    draft = rebuild_draft(voice_event, CUT_PLACED_AFTER.get((turn.get("run", FIRST_RUN), turn["world"], turn["q"])))
    text, _citations, net_result = net(draft)
    settled = settle_reply(draft, text, net_result, voice_event["offered_ids"], world_records, net)
    return {"draft": draft, "text": settled["text"], "net_result": settled["net_result"],
            "fallback": settled["answer_record_fallback"], "first_text": text, "first_net": net_result}


def _speaker_named(world: str, net_result: dict) -> list[bool]:
    world_records = records(world)
    index = grounding_net.QuotationIndex(world_records)
    named = []
    for entry in net_result["sentences"]:
        rid = entry.get("placed_quote")
        if rid:
            lead = grounding_net._outside_quotations(entry["sentence"], grounding_net._checked_pairs(entry["sentence"]))
            named.append(index.names_speaker(lead, world_records[rid]))
    return named


def overcut_sentences(run: str = FIRST_RUN) -> dict[tuple[str, int], list[str]]:
    """The cuts the run's independent reading judged wrong, by (world, q).
    The 14 October reading gives each cut a verdict; an "overcut" verdict
    whose sentence it quotes whole is one. A sentence it abridges ("...") is
    found again among the turn's recorded cuts by its opening words."""
    reading = json.loads(RUNS[run]["reading"].read_text())
    found: dict[tuple[str, int], list[str]] = {}
    for world, entry in reading["worlds"].items():
        for overcut in entry.get("cuts_overcut") or []:
            sentence = grounding_net.strip_tags(overcut["sentence"]).strip()
            found.setdefault((world, int(overcut["q"].lstrip("Q"))), []).append(sentence)
        for cut in entry.get("cut_list") or []:
            if not cut["verdict"].startswith("overcut"):
                continue
            q = int(cut["q"].lstrip("Q"))
            sentence = grounding_net.strip_tags(cut["sentence"]).strip()
            if "..." in sentence or "\u2026" in sentence:
                head = re.split(r"\.\.\.|\u2026", sentence)[0].strip()
                recorded = report(world, run)["results"][q - 1]["result"]["voice_event"]["reply_shape"]["removed"]
                sentence = next(r["sentence"] for r in recorded if r["sentence"].startswith(head))
            found.setdefault((world, q), []).append(sentence)
    return found


def _shown(sentence: str, text: str) -> bool:
    return " ".join(sentence.split()).rstrip(".") in " ".join(text.split())


def summary(results: list[tuple[dict, dict]], run: str = FIRST_RUN) -> dict:
    """The counts the PR reports, over (turn, replay) pairs of one run."""
    overcuts = overcut_sentences(run)
    counts = {
        "turns": len(results), "cuts": 0, "overcuts_still_cut": 0, "overcuts_listed": sum(map(len, overcuts.values())),
        "fallbacks": 0, "degraded_sent": 0, "placed_quotes": 0, "placed_without_speaker_named": 0,
        "stray_punctuation_sentences": 0,
    }
    for turn, result in results:
        net_result = result["first_net"]
        counts["cuts"] += len(net_result["reply_shape"]["removed"])
        counts["fallbacks"] += result["fallback"] is not None
        counts["degraded_sent"] += bool(result["text"].strip()) and not result["net_result"]["substantive_survives"]
        named = _speaker_named(turn["world"], net_result)
        counts["placed_quotes"] += len(named)
        counts["placed_without_speaker_named"] += named.count(False)
        counts["stray_punctuation_sentences"] += sum(bool(_STRAY.match(s["sentence"])) for s in net_result["sentences"])
        for sentence in overcuts.get((turn["world"], turn["q"]), []):
            counts["overcuts_still_cut"] += not _shown(sentence, result["first_text"])
    return counts


# A connective claim: a reason, motive or cause joined into a sentence.
_CONNECTIVE = re.compile(
    r"\b(because|so that|in order to|meaning to|which is why|that is why|for this reason|therefore|so as to)\b",
    re.IGNORECASE,
)
SHORT_SENTENCE_WORDS = 8


def rhythm(text: str) -> dict:
    """A reply's sentence lengths: their mean and spread (population
    standard deviation, in words), and how many runs of three or more
    sentences under SHORT_SENTENCE_WORDS words in a row it has."""
    lengths = [len(_WORD.findall(s.lower())) for s in quote_aware_sentences(text) if _WORD.search(s.lower())]
    if not lengths:
        return {"sentences": 0, "mean": 0.0, "spread": 0.0, "short_runs": 0}
    mean = sum(lengths) / len(lengths)
    spread = (sum((n - mean) ** 2 for n in lengths) / len(lengths)) ** 0.5
    runs, run = 0, 0
    for n in lengths + [SHORT_SENTENCE_WORDS]:
        if n < SHORT_SENTENCE_WORDS:
            run += 1
            continue
        runs += run >= 3
        run = 0
    return {"sentences": len(lengths), "mean": mean, "spread": spread, "short_runs": runs}


def connective_claims(sentences: list[dict], world_records: dict) -> list[str]:
    """Shown sentences that join a reason, motive or cause with a connective
    ("because", "so that", "meaning to"...) that none of the records the
    sentence is tagged to uses: a connection the voice made, not the record."""
    found = []
    for entry in sentences:
        match = _CONNECTIVE.search(entry["sentence"])
        if not match:
            continue
        held = " ".join(grounding_net.all_text(world_records[t]).lower() for t in entry["tags"] if t in world_records)
        if match.group(1).lower() not in held:
            found.append(entry["sentence"])
    return found


def reply_metrics(world: str, text: str, sentences: list[dict]) -> dict:
    return {**rhythm(text), "connective_claims": len(connective_claims(sentences, records(world)))}


def report_metrics(world: str, report_doc: dict) -> list[dict]:
    """reply_metrics for every reply a live-turn report recorded, for
    measuring a retest the same way."""
    out = []
    for result in report_doc["results"]:
        voice_event = (result.get("result") or {}).get("voice_event") or {}
        out.append(reply_metrics(world, voice_event.get("text") or "", (voice_event.get("grounding") or {}).get("sentences") or []))
    return out


def rhythm_summary(per_reply: list[dict]) -> dict:
    n = len(per_reply) or 1
    return {
        "mean_words_per_sentence": round(sum(r["mean"] for r in per_reply) / n, 1),
        "mean_spread": round(sum(r["spread"] for r in per_reply) / n, 1),
        "short_runs": sum(r["short_runs"] for r in per_reply),
        "replies_with_short_runs": sum(r["short_runs"] > 0 for r in per_reply),
        "connective_claims": sum(r["connective_claims"] for r in per_reply),
    }


def rhythm_before_after(results: list[tuple[dict, dict]]) -> dict:
    """The rhythm measures over the replies as recorded on 13 October, and
    over the same drafts as the reply shaping now gives them."""
    before = [reply_metrics(t["world"], t["voice_event"]["text"], t["voice_event"]["grounding"]["sentences"]) for t, _r in results]
    after = [reply_metrics(t["world"], r["text"], r["net_result"]["sentences"]) for t, r in results]
    return {"before": rhythm_summary(before), "after": rhythm_summary(after)}


def person_claim_flags_over_runs() -> list[dict]:
    """engine.m4.person_claims' flags over every sentence each run's
    replayed replies show, as {"run", "world", "q", "sentence", "flags"}:
    how the precision of that check was measured."""
    from engine.m4.person_claims import find_person_claim_flags

    out = []
    for run in RUNS:
        for turn, result in run_all(run):
            for entry in find_person_claim_flags(result["net_result"]["sentences"], repository_records=records(turn["world"])):
                out.append({"run": run, "world": turn["world"], "q": turn["q"], **entry})
    return out


def quote_sentence_scan(worlds: tuple[str, ...] = RUNS[FIRST_RUN]["worlds"]) -> dict:
    """Every sentence of every quote record's rendering, given without
    placement three ways - plain, as indirect speech, and as direct speech
    after the speaker's name - and tagged to the world's non-quote record
    whose wording shares most words with it. How many of each pass the net's
    quotation checks: what a cited record lets the voice say of a quote."""
    from engine.m4.evidence import _with_quote_index
    from engine.m4.turn_prep import _speaker_name

    counts = {"sentences": 0, "plain": 0, "indirect": 0, "direct": 0}
    for world in worlds:
        world_records = records(world)
        index = grounding_net.QuotationIndex(world_records)
        telling = [rid for rid, rec in world_records.items() if rec.get("record_type") not in ("quote", "demonstration", "voice_craft")]
        words = {rid: set(grounding_net._word_sequence(grounding_net.all_text(world_records[rid]))) for rid in telling}
        for rid, rec in sorted(world_records.items()):
            if rec.get("record_type") != "quote" or not rec.get("modern_rendering"):
                continue
            speaker = _speaker_name(_with_quote_index({"id": rid, "record_type": "quote"}, world_records).get("speaker"))
            for sentence in quote_aware_sentences(rec["modern_rendering"]):
                sentence = sentence.strip().strip('"\u201c\u201d').rstrip(".")
                own = set(grounding_net._word_sequence(sentence))
                if len(own) < grounding_net.QUOTE_WORDS_MIN:
                    continue
                cited = max(telling, key=lambda r: (len(own & words[r]), r))
                counts["sentences"] += 1
                for form, text in (("plain", f"{sentence}."), ("indirect", f"{speaker} said that {sentence[0].lower()}{sentence[1:]}."),
                                   ("direct", f"{speaker} said: {sentence}.")):
                    verdict = grounding_net._quotation_verdict(text, [cited], world_records, index)
                    counts[form] += verdict is None or bool(verdict.get("lead_only")) or verdict.get("verdict") != "withhold"
    return counts


def run_all(run: str = FIRST_RUN) -> list[tuple[dict, dict]]:
    return [(turn, replay(turn)) for turn in turns(run)]


if __name__ == "__main__":
    out = {}
    for run in RUNS:
        results = run_all(run)
        out[run] = {"replay": summary(results, run), "rhythm": rhythm_before_after(results)}
    print(json.dumps(out, indent=2))
