from dataclasses import dataclass
from typing import Callable, Sequence

from .contract import Passage

MIN_PREFIX_TOKENS = 4300
MAX_PREFIX_TOKENS = 9000
MARKER_TOKENS = 24
NEIGHBOR_WORDS = 60


@dataclass(frozen=True)
class Window:
    file: str
    start: int
    end: int
    body_tokens: int
    base_tokens: int

    @property
    def prefix_tokens(self) -> int:
        return self.base_tokens + self.body_tokens

    @property
    def cacheable(self) -> bool:
        return self.prefix_tokens >= MIN_PREFIX_TOKENS

    @property
    def size(self) -> int:
        return self.end - self.start

    def indices(self) -> range:
        return range(self.start, self.end)


def _groups(passages: Sequence[Passage], tokens: Sequence[int], max_body: int) -> list[tuple[int, int, int]]:
    groups: list[tuple[int, int, int]] = []
    division_start = 0
    count = len(passages)
    for index in range(1, count + 1):
        if index == count or passages[index].division_locus != passages[division_start].division_locus:
            start = division_start
            running = 0
            for cursor in range(division_start, index):
                weight = tokens[cursor] + MARKER_TOKENS
                if running and running + weight > max_body:
                    groups.append((start, cursor, running))
                    start, running = cursor, 0
                running += weight
            groups.append((start, index, running))
            division_start = index
    return groups


def oversize_divisions(passages: Sequence[Passage], token_of: Callable[[Passage], int], base_tokens: int) -> int:
    max_body = MAX_PREFIX_TOKENS - base_tokens
    totals: dict[str, int] = {}
    for p in passages:
        totals[p.division_locus] = totals.get(p.division_locus, 0) + token_of(p) + MARKER_TOKENS
    return sum(1 for total in totals.values() if total > max_body)


def build_windows(
    file_name: str,
    passages: Sequence[Passage],
    token_of: Callable[[Passage], int],
    base_tokens: int,
) -> list[Window]:
    if not passages:
        return []
    tokens = [token_of(p) for p in passages]
    max_body = MAX_PREFIX_TOKENS - base_tokens
    min_body = MIN_PREFIX_TOKENS - base_tokens
    merged: list[list[int]] = []
    for start, end, body in _groups(passages, tokens, max_body):
        if merged and merged[-1][2] < min_body and merged[-1][2] + body <= max_body:
            merged[-1][1] = end
            merged[-1][2] += body
        else:
            merged.append([start, end, body])
    if len(merged) > 1 and merged[-1][2] < min_body and merged[-2][2] + merged[-1][2] <= max_body + min_body:
        tail = merged.pop()
        merged[-1][1] = tail[1]
        merged[-1][2] += tail[2]
    return [Window(file_name, start, end, body, base_tokens) for start, end, body in merged]


def neighbor_outside(window: Window, passages: Sequence[Passage], index: int) -> tuple[Passage | None, Passage | None]:
    previous = passages[index - 1] if index == window.start and index > 0 else None
    following = passages[index + 1] if index == window.end - 1 and index + 1 < len(passages) else None
    return previous, following
