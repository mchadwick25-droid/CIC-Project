"""Fusing rankings and reranking. Pure functions over lists of internal passage ids."""
from typing import Callable, Collection, Sequence

RRF_K = 60


def reciprocal_rank_fusion(rankings: Sequence[Sequence[int]], k: int = RRF_K, seeds: Collection[int] = ()) -> list[int]:
    """Each ranking gives a passage 1/(k + rank); the sums order the passages. Of equal sums a reviewed seed comes first,
    then the lower internal id."""
    scores: dict[int, float] = {}
    for ranking in rankings:
        for position, item in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + position)
    return [i for i, _ in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0] not in seeds, kv[0]))]


def rerank(candidates: Sequence[int], score: Callable[[Sequence[int]], Sequence[float]], keep: int,
           seeds: Collection[int] = ()) -> list[int]:
    """The first `keep` candidates re-ordered by the reranker's score, then the rest in their incoming order.
    Of two equal scores a reviewed seed comes first; seeds are rank help, never a limit."""
    head, tail = list(candidates[:keep]), list(candidates[keep:])
    if not head:
        return tail
    scores = score(head)
    order = sorted(range(len(head)), key=lambda n: (-scores[n], head[n] not in seeds, n))
    return [head[n] for n in order] + tail
