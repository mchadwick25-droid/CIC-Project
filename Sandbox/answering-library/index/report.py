from pathlib import Path

from .catalog import REPO_ROOT
from .status import PENDING_OPTION
from .estimate import BANDS, EDGE_TOKENS, FRESH_OVERHEAD_TOKENS, PASSAGE_WORDS, ScopeEstimate
from .pricing import BATCH_DISCOUNT_SOURCE, MODEL_ID, price_table
from .prompting import CONTEXT_WORD_LIMIT, PROMPT_VERSION
from .windows import MAX_PREFIX_TOKENS, MIN_PREFIX_TOKENS, NEIGHBOR_WORDS

WINDOW_DEFINITION = (
    f"one call per passage; cached prefix = system instruction + work header + the whole division (or, for a division "
    f"over {MAX_PREFIX_TOKENS} tokens, the run of passages that fits), merged with neighbouring divisions until the prefix "
    f"reaches {MIN_PREFIX_TOKENS} tokens (the cache minimum, with margin); fresh part = the target's id plus, at a window edge, "
    f"the last/first {NEIGHBOR_WORDS} words of the passage just outside; reply of at most {CONTEXT_WORD_LIMIT} words"
)


def money(value: float) -> str:
    return f"${value:,.2f}"


def band_range(values: dict[str, float], fmt=money) -> str:
    return f"{fmt(values['low'])} to {fmt(values['high'])}"


def counts_block(estimate: ScopeEstimate) -> list[str]:
    s = estimate.summary()
    tokens = lambda d: f"{d['low']:,} (low band) / {d['high']:,} (high band)"
    return [
        f"- Files: {s['files']} ({s['files_segmented']} with segmenter output, {s['files'] - s['files_segmented']} modeled from word counts)",
        f"- Passages: {s['passages']:,}" + ("" if s["files_segmented"] == s["files"] else " (modeled at about "
                                                  f"{PASSAGE_WORDS} words each where not segmented)"),
        f"- Windows (cached prefixes): {s['windows']:,}",
        f"- Passage text tokens: {tokens(s['text_tokens'])}",
        f"- Input tokens, cached prefix (written once, then read): {tokens(s['input_tokens_cached_prefix'])}",
        f"- Input tokens, fresh: {tokens(s['input_tokens_fresh'])}",
        f"- Output tokens: {tokens(s['output_tokens'])}",
        f"- Estimated cost, standard path (low to high): {band_range(s['dollars_sync'])}",
    ]


def render_settings(
    estimate: ScopeEstimate, *, live_test: str | None, cap_usd: float | None, out_dir: Path, pending: int | None = None,
    model_id: str = MODEL_ID,
) -> str:
    table = price_table(model_id)
    lines = [
        "CONTEXTUAL INDEXING RUN SETTINGS",
        f"live test: {live_test or '(none: estimate only)'}",
        f"cap: {money(cap_usd) if cap_usd is not None else '(none)'}",
        f"model id: {model_id} (priced from engine/m8/price_tables.py: ${table.input_per_token * 1e6:g} in, "
        f"${table.output_per_token * 1e6:g} out, ${table.cache_write_per_token * 1e6:g} cache write, "
        f"${table.cache_read_per_token * 1e6:g} cache read, per million tokens)",
        f"prompt version: {PROMPT_VERSION}",
        f"window definition: {WINDOW_DEFINITION}",
        *counts_block(estimate),
    ]
    if pending is not None:
        lines.append(f"- Passages still to do (resume skips the rest): {pending:,}")
    if cap_usd is not None:
        high = estimate.summary()["dollars_sync"]["high"]
        lines.append(
            f"- Cap against the estimate: {money(cap_usd)} {'covers' if cap_usd >= high else 'does not cover'} the high estimate "
            f"{money(high)}" + ("" if cap_usd >= high else "; the run will stop at the cap and can be resumed"))
    target = out_dir / "context"
    shown = target.relative_to(REPO_ROOT) if target.is_relative_to(REPO_ROOT) else target
    lines.append(f"output path: {shown}")
    return "\n".join(lines)


def render_estimate(estimates: list[ScopeEstimate], union: ScopeEstimate, top: int = 15) -> str:
    out = ["# Contextual indexing: cost estimate", "", PENDING_OPTION, ""]
    out.append("Prices: Haiku 4.5 from engine/m8/price_tables.py. Batch discount: " + BATCH_DISCOUNT_SOURCE + ".")
    out.append("")
    out.append(
        f"Assumptions behind every modeled row (replaced by the segmenter's real passages file by file as they exist): about {PASSAGE_WORDS} "
        f"words a passage; characters per token Latin script 4.0 (low band) to 3.2 (high band), Greek and other scripts 2.4 to 1.5; "
        f"output {BANDS['low'].output_tokens} (low) to {BANDS['high'].output_tokens} (high) tokens per context line; cache prefix "
        f"{MIN_PREFIX_TOKENS} (low band) to {MAX_PREFIX_TOKENS} (high band) tokens per window, {MIN_PREFIX_TOKENS} being the assumed Haiku "
        f"cache minimum of 4,096 plus margin; {BANDS['high'].miss_rate:.0%} of high-band calls re-write the cache instead of reading it; "
        f"{FRESH_OVERHEAD_TOKENS} fresh tokens a call plus {EDGE_TOKENS} per window for the edge neighbours. Shared files count once in "
        f"the union and once in each world that holds them, so the world rows add up to more than the union.")
    out += ["", "| Scope | Files | Passages | Text tokens (low-high) | Standard path | Batch path (assumed) | One call per window, standard |",
            "|---|---:|---:|---|---|---|---|"]
    for e in estimates:
        s = e.summary()
        out.append(
            f"| {s['scope']} | {s['files']} | {s['passages']:,} | {s['text_tokens']['low'] / 1e6:.1f}M to {s['text_tokens']['high'] / 1e6:.1f}M "
            f"| {band_range(s['dollars_sync'])} | {band_range(s['dollars_batch_assumed'])} | {band_range(s['dollars_one_call_per_window_sync'])} |")
    s = union.summary()
    out += ["", "## What drives the union cost", "", "| Component | Low | High |", "|---|---:|---:|"]
    for key in s["cost_drivers_high"]:
        out.append(f"| {key} | {money(s['cost_drivers_low'][key])} | {money(s['cost_drivers_high'][key])} |")
    out += ["", f"## Largest files in the union (by high estimate, top {top})", "",
            "| File | Worlds | Source | Passages | Windows | Low | High |", "|---|---|---|---:|---:|---:|---:|"]
    for row in union.by_file()[:top]:
        out.append(f"| {row['file']} | {row['worlds']} | {row['source']} | {row['passages']:,} | {row['windows']:,} | "
                   f"{money(row['dollars_low'])} | {money(row['dollars_high'])} |")
    return "\n".join(out)
