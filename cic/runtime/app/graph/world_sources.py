"""Loading a world's two STATIC source documents, with a correct cache.

A world's capsule and permanent prompt are files on disk that do not change
while a conversation is running. Every source-fed adjudication re-read both
from disk: roughly 30-40 KB per world per adjudication, on a path that can run
several times per turn across a multi-world table.

That is the repeated work in evidence gathering, and it is keyed by world_id
alone - six possible keys, effectively a 100% hit rate across a conversation.

It is worth being explicit about what is NOT cached here, because an earlier
attempt cached the wrong thing. Memoizing the whole evidence tuple on
(world_id, response_text) looks like it collapses duplicate work, but:

  * response_text is a representative's own generated turn. It never repeats,
    so the hit rate on the intended case is zero.
  * The case it was written for - "one turn trips both the fabrication and the
    over-settling screens, so both adjudicators gather the same evidence" -
    cannot occur. _detect_drift_signal reaches the over-settling path ONLY in
    its `not result.startswith("DRIFT_DETECTED")` branch, and reaches the
    fabrication adjudicator ONLY inside the DRIFT_DETECTED branch. The two are
    mutually exclusive by construction, and the code comment at that branch
    says so in as many words ("Only reached when the general monitor is
    clean"). Verified by executing the real function against a scripted
    monitor: one gather call on the fabrication path, one on the over-settling
    path, never two.
  * It would hold generated turn text in a process-global cache for the life
    of the process, which is a retention cost with no measured benefit.

So: cache the static files, keyed by identity AND (mtime, size) so an edited
file invalidates itself rather than serving a stale record for as long as the
process lives. Do not cache anything keyed by a participant's or a
representative's text.
"""

from pathlib import Path

from app.config import settings

PERMANENT_PROMPT_UNAVAILABLE = "(permanent prompt unavailable)"

# path -> (mtime_ns, size, text). Bounded by the number of world source files
# (two per world, six worlds), so it needs no eviction policy.
_CACHE: dict[str, tuple[int, int, str]] = {}


def _read_cached(path: Path) -> str:
    """Read `path`, reusing the last read when the file is provably unchanged.

    Keying on (mtime_ns, size) rather than path alone is what makes this a
    cache rather than a staleness bug: editing a world's capsule mid-process -
    routine during a build - invalidates the entry instead of pinning the old
    text until restart.
    """
    key = str(path)
    stat = path.stat()
    cached = _CACHE.get(key)
    if cached is not None and cached[0] == stat.st_mtime_ns and cached[1] == stat.st_size:
        return cached[2]
    text = path.read_text(encoding="utf-8")
    _CACHE[key] = (stat.st_mtime_ns, stat.st_size, text)
    return text


def load_world_sources(world_id: str) -> tuple[str, str] | None:
    """(capsule, permanent_prompt) for `world_id`, or None.

    None means the capsule could not be read at all - the one failure that
    leaves an adjudicator nothing to judge against, and which its callers
    turn into "could not adjudicate" rather than a false verdict.

    An unreadable permanent prompt is NOT fatal and returns the
    PERMANENT_PROMPT_UNAVAILABLE placeholder: the capsule and retrieval can
    still settle most cases, and failing the whole adjudication here would
    keep a stage 1 finding this stage might have cleared.
    """
    try:
        world_config = settings.get_world_config(world_id)
        capsule = _read_cached(world_config.world_capsule_path)
    except Exception:
        return None

    # The permanent prompt is the third source FABRICATION's own definition
    # names ("grounded in the permanent prompt, world capsule, or retrieved
    # context"), and it is where each Representative's core formation and
    # world facts live. Adjudicating against only the capsule and retrieval
    # left content grounded ONLY in the permanent prompt still reading as
    # fabricated - the same false-positive class this stage exists to close,
    # surviving in a narrower band.
    try:
        permanent_prompt = _read_cached(world_config.permanent_prompt_path)
    except Exception:
        permanent_prompt = PERMANENT_PROMPT_UNAVAILABLE

    return capsule, permanent_prompt
