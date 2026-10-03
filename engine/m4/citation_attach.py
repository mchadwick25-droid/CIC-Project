"""Verified citation attachment: after a voice turn settles, give an
uncited claim sentence a citation when one of the world's records carries
it. One call proposes, for every uncited claim sentence at once, the
single record that carries it (or none); a second, short call per
proposal checks the sentence against that record's own text, and only a
"carries" verdict is attached. Both calls run on the safety model.

The voice's text is never changed: this adds decoration only, so any
failed or malformed call attaches nothing further and the turn goes out
exactly as the voice wrote it.
"""
import json
import re

import anthropic

from engine.m4.grounding_net import _groundable_text
from engine.m4.uncited_claims import find_uncited_claims
from engine.m8.usage import UsageRecord, record_usage
from engine.provider.bedrock import normalize_usage

PROPOSE_MAX_TOKENS = 2000
VERIFY_MAX_TOKENS = 5

PROPOSE_INSTRUCTION = (
    "You check citations for the Representative whose world is described above. Below are sentences it said "
    "without a citation. For each one, find the single record in the world above whose own text carries the "
    "sentence's specific claim, and give that record's id copied exactly from the list of valid ids at the end of "
    "these instructions (the same ids the world above shows inside [[...]]). Never build an id from a heading, a "
    "cell code or a title. Choose a record only when its text actually states or directly entails the claim; a "
    "record on the same topic that does not carry the claim is not enough. If no record carries the claim, answer "
    'null. Answer with JSON only: [{"id": "S1", "record_id": "world.type.slug" or null}, ...], one entry per '
    "sentence, nothing else."
)
VERIFY_INSTRUCTION = (
    "You check one citation. You get a sentence and the text of the record it cites. Answer \"carries\" only if the "
    "record's text itself states or directly entails every specific claim in the sentence (people, places, dates, "
    "numbers, events, practices, teachings). Paraphrase and modern wording are fine. Answer \"partly\" if the record "
    "carries the core but the sentence adds any specific detail the record does not state. Answer \"no\" if the "
    "record does not carry the main claim. Use only the record text, never outside knowledge. Reply with one word: "
    "carries, partly or no."
)

_PROMPT_ID = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")


def citable_ids(prompt_text: str, repository_records: dict[str, dict]) -> list[str]:
    """Ids the world's prompt offers for citation that are also real records."""
    return sorted(set(_PROMPT_ID.findall(prompt_text)) & set(repository_records))


def parse_proposals(text: str) -> list[dict]:
    """The first JSON array in the reply, tolerating text after it; [] when
    there is none. Entries that are not objects are dropped."""
    start = text.find("[")
    if start < 0:
        return []
    try:
        value, _ = json.JSONDecoder().raw_decode(text[start:])
    except json.JSONDecodeError:
        return []
    return [p for p in value if isinstance(p, dict)] if isinstance(value, list) else []


def first_word(text: str) -> str:
    words = re.findall(r"[a-z]+", text.lower())
    return words[0] if words else ""


def _usage(response, *, session_id: str, call_kind: str, model_id: str, world_key: str | None) -> UsageRecord:
    return record_usage(usage=normalize_usage(response.usage), session_id=session_id, call_kind=call_kind,
                        model_id=model_id, world_key=world_key)


def attach_citations(
    *,
    client,
    model_id: str,
    prompt_text: str,
    repository_records: dict[str, dict],
    net_result: dict,
    session_id: str,
    world_key: str | None = None,
) -> tuple[list[dict], list[UsageRecord], list[dict]]:
    """Returns (citations to add, usage records, trail). Each added citation
    has the shape apply_net gives its own: {"sentence", "record_ids"}, plus
    "attached": True. The trail records every proposal and its verdict for
    the turn's audit."""
    sentences = [s["sentence"] for s in net_result["sentences"]]
    uncited = [o["sentence"] for o in find_uncited_claims(net_result["sentences"])]
    valid = citable_ids(prompt_text, repository_records)
    if not uncited or not valid:
        return [], [], []

    usage: list[UsageRecord] = []
    trail: list[dict] = []
    added: list[dict] = []
    try:
        lines = []
        for n, sentence in enumerate(uncited, 1):
            i = sentences.index(sentence)
            before = sentences[i - 1] if i else "(start of reply)"
            lines.append(f'S{n}: "{sentence}" (just before it: "{before}")')
        proposal = client.messages.create(
            model=model_id, max_tokens=PROPOSE_MAX_TOKENS,
            system=[{"type": "text", "text": prompt_text, "cache_control": {"type": "ephemeral"}},
                    {"type": "text", "text": PROPOSE_INSTRUCTION + "\n\nValid ids:\n" + "\n".join(valid)}],
            messages=[{"role": "user", "content": "\n".join(lines)}],
        )
        usage.append(_usage(proposal, session_id=session_id, call_kind="citation_propose", model_id=model_id, world_key=world_key))
        for p in parse_proposals(proposal.content[0].text):
            match = re.fullmatch(r"S(\d+)", str(p.get("id", "")))
            n = int(match.group(1)) if match else 0
            record_id = p.get("record_id")
            if not 1 <= n <= len(uncited):
                continue
            sentence = uncited[n - 1]
            if record_id is None:
                trail.append({"sentence": sentence, "proposed": None, "verdict": "none"})
                continue
            if record_id not in valid:
                trail.append({"sentence": sentence, "proposed": record_id, "verdict": "rejected"})
                continue
            check = client.messages.create(
                model=model_id, max_tokens=VERIFY_MAX_TOKENS, system=VERIFY_INSTRUCTION,
                messages=[{"role": "user", "content": f"Sentence: {sentence}\n\nRecord {record_id}:\n{_groundable_text(repository_records[record_id])}"}],
            )
            usage.append(_usage(check, session_id=session_id, call_kind="citation_verify", model_id=model_id, world_key=world_key))
            verdict = first_word(check.content[0].text)
            trail.append({"sentence": sentence, "proposed": record_id, "verdict": verdict})
            if verdict == "carries" and sentence not in {a["sentence"] for a in added}:
                added.append({"sentence": sentence, "record_ids": [record_id], "attached": True})
    except anthropic.APIError as exc:
        # Decoration only: a failed call ends attachment for this turn and
        # keeps what was already verified; the text is untouched either way.
        trail.append({"error": f"{type(exc).__name__}: {exc}"[:300]})
    return added, usage, trail
