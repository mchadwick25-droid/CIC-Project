from typing import Sequence

from .catalog import FileEntry
from .contract import Passage
from .windows import NEIGHBOR_WORDS, Window, neighbor_outside

PROMPT_VERSION = "ctx-1"
MAX_OUTPUT_TOKENS = 160
CONTEXT_WORD_LIMIT = 60

SYSTEM_PROMPT = (
    "You write the one-line context for a passage of an old text, so a search index can find the passage.\n"
    "You receive the work header, a stretch of the work in which every passage sits in a <passage> tag with an id, "
    "and the id of one target passage.\n"
    f"Write one sentence of at most {CONTEXT_WORD_LIMIT} words that says which work and author the passage belongs to, "
    "which division it sits in, and what it does in relation to the passages around it.\n"
    "Use only what the work header and the supplied passages state. Do not add any name, date, place, doctrine, "
    "event or claim that they do not contain. Do not quote the passage. Do not explain or comment.\n"
    "If the speaker or the subject cannot be told from what you were given, say less.\n"
    "Reply with the sentence only."
)


def window_block(entry: FileEntry, window: Window, passages: Sequence[Passage]) -> str:
    lines = ["<work_header>", entry.header(), "</work_header>", "<stretch>"]
    for index in window.indices():
        p = passages[index]
        title = f' title="{p.division_title}"' if p.division_title else ""
        lines.append(f'<passage id="{p.passage_id}" division="{p.division_locus}"{title}>')
        lines.append(p.text)
        lines.append("</passage>")
    lines.append("</stretch>")
    return "\n".join(lines)


def _edge(text: str, from_end: bool) -> str:
    words = text.split()
    chosen = words[-NEIGHBOR_WORDS:] if from_end else words[:NEIGHBOR_WORDS]
    return " ".join(chosen)


def fresh_block(window: Window, passages: Sequence[Passage], index: int) -> str:
    target = passages[index]
    lines = [f'Write the context line for the passage with id "{target.passage_id}".']
    previous, following = neighbor_outside(window, passages, index)
    if previous is not None:
        lines.append(f'The passage just before the stretch ends: "{_edge(previous.text, True)}"')
    if following is not None:
        lines.append(f'The passage just after the stretch begins: "{_edge(following.text, False)}"')
    return "\n".join(lines)


def build_request(
    model_id: str, entry: FileEntry, window: Window, passages: Sequence[Passage], index: int, *, cache: bool = True,
) -> dict:
    prefix = {"type": "text", "text": window_block(entry, window, passages)}
    if cache and window.cacheable:
        prefix["cache_control"] = {"type": "ephemeral"}
    return {
        "model": model_id,
        "max_tokens": MAX_OUTPUT_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": [prefix, {"type": "text", "text": fresh_block(window, passages, index)}]}],
    }


def allowed_text(entry: FileEntry, window: Window, passages: Sequence[Passage], index: int) -> str:
    parts = [entry.registry_vocabulary(), window_block(entry, window, passages), fresh_block(window, passages, index)]
    return "\n".join(parts)


def response_text(response) -> str:
    chunks = [block.text for block in getattr(response, "content", []) if getattr(block, "type", "text") == "text"]
    return " ".join(" ".join(chunks).split())
