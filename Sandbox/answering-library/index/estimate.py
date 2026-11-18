import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from . import contract
from .catalog import FileEntry
from .contract import Passage
from .pricing import BATCH_DISCOUNT, Usage, price_table
from .prompting import SYSTEM_PROMPT
from .tokens import TextStats, estimate_tokens, file_stats
from .windows import MARKER_TOKENS, MAX_PREFIX_TOKENS, MIN_PREFIX_TOKENS, build_windows, oversize_divisions

PASSAGE_WORDS = 275
FRESH_OVERHEAD_TOKENS = 45
EDGE_TOKENS = 220
LIST_OVERHEAD_TOKENS = 18


@dataclass(frozen=True)
class Band:
    name: str
    output_tokens: int
    miss_rate: float


BANDS = {"low": Band("low", 55, 0.0), "high": Band("high", 100, 0.02)}


def window_usage(prefix: float, n: float, cacheable: bool, band: Band) -> Usage:
    fresh = n * FRESH_OVERHEAD_TOKENS + 2 * EDGE_TOKENS
    output = n * band.output_tokens
    if not cacheable:
        return Usage(calls=n, fresh_input=fresh, uncached_input=n * prefix, output=output)
    rewritten = band.miss_rate * (n - 1)
    return Usage(
        calls=n, fresh_input=fresh, cache_write=prefix * (1 + rewritten),
        cache_read=prefix * (n - 1 - rewritten), output=output,
    )


def window_one_call_usage(prefix: float, n: float, band: Band) -> Usage:
    return Usage(calls=1, fresh_input=prefix + FRESH_OVERHEAD_TOKENS, output=n * (band.output_tokens + LIST_OVERHEAD_TOKENS))


@dataclass
class FilePlan:
    file: str
    worlds: tuple[str, ...]
    source: str
    passages: float
    windows: float
    body_tokens: dict[str, int]
    usage: dict[str, Usage]
    alt_usage: dict[str, Usage]
    uncached_windows: float = 0.0
    split_divisions: int = 0
    oversize_passages: int = 0
    notes: list[str] = field(default_factory=list)

    def dollars(self, band: str, table) -> float:
        return self.usage[band].dollars(table)


def base_tokens(entry: FileEntry, band: str) -> int:
    return estimate_tokens(SYSTEM_PROMPT + "\n" + entry.header(), band) + 40


def plan_from_passages(entry: FileEntry, passages: Sequence[Passage]) -> FilePlan:
    usage, alt, body = {}, {}, {}
    windows_count = uncached = split = 0
    for name, band in BANDS.items():
        base = base_tokens(entry, name)
        windows = build_windows(entry.file, passages, lambda p: estimate_tokens(p.text, name), base)
        body[name] = sum(w.body_tokens for w in windows)
        total, total_alt = Usage(), Usage()
        for window in windows:
            total.add(window_usage(window.prefix_tokens, window.size, window.cacheable, band))
            total_alt.add(window_one_call_usage(window.prefix_tokens, window.size, band))
        usage[name], alt[name] = total, total_alt
        if name == "high":
            windows_count = len(windows)
            uncached = sum(1 for w in windows if not w.cacheable)
            split = oversize_divisions(passages, lambda p: estimate_tokens(p.text, name), base)
    oversize = sum(1 for p in passages if estimate_tokens(p.text, "high") > MAX_PREFIX_TOKENS - MARKER_TOKENS - 400)
    return FilePlan(entry.file, tuple(sorted(entry.worlds)), "segmented", len(passages), windows_count, body, usage, alt,
                    uncached_windows=uncached, split_divisions=split, oversize_passages=oversize)


def plan_from_stats(entry: FileEntry, stats: TextStats) -> FilePlan:
    n_passages = max(1.0, stats.words / PASSAGE_WORDS)
    usage, alt, body = {}, {}, {}
    windows_count = uncached = 0.0
    for name, band in BANDS.items():
        base = base_tokens(entry, name)
        text_tokens = stats.tokens(name) + n_passages * MARKER_TOKENS
        window_body = (MIN_PREFIX_TOKENS if name == "low" else MAX_PREFIX_TOKENS) - base
        rounding = math.floor if name == "low" else math.ceil
        count = max(1.0, rounding(text_tokens / window_body))
        prefix = base + text_tokens / count
        cacheable = prefix >= MIN_PREFIX_TOKENS
        body[name] = int(text_tokens)
        usage[name] = window_usage(prefix, n_passages / count, cacheable, band).scaled(count)
        alt[name] = window_one_call_usage(prefix, n_passages / count, band).scaled(count)
        if name == "high":
            windows_count, uncached = count, 0.0 if cacheable else count
    return FilePlan(entry.file, tuple(sorted(entry.worlds)), "modeled", n_passages, windows_count, body, usage, alt,
                    uncached_windows=uncached, notes=["no segmenter output: passages and windows are modeled from word count"])


def plan_file(entry: FileEntry, out_dir: Path, passages: Sequence[Passage] | None = None) -> FilePlan:
    if passages is None:
        passages = contract.read_file_passages(out_dir, entry.file)
    if passages:
        return plan_from_passages(entry, passages)
    return plan_from_stats(entry, file_stats(entry.path, out_dir / "filestats.json"))


@dataclass
class ScopeEstimate:
    name: str
    plans: list[FilePlan]

    def usage(self, band: str, alt: bool = False) -> Usage:
        total = Usage()
        for plan in self.plans:
            total.add((plan.alt_usage if alt else plan.usage)[band])
        return total

    @property
    def passages(self) -> int:
        return round(sum(p.passages for p in self.plans))

    def body_tokens(self, band: str) -> int:
        return sum(p.body_tokens[band] for p in self.plans)

    def dollars(self, band: str, *, batch: bool = False, alt: bool = False) -> float:
        value = self.usage(band, alt).dollars(price_table())
        return value * BATCH_DISCOUNT if batch else value

    def summary(self) -> dict:
        table = price_table()
        return {
            "scope": self.name,
            "files": len(self.plans),
            "files_segmented": sum(1 for p in self.plans if p.source == "segmented"),
            "passages": self.passages,
            "windows": round(sum(p.windows for p in self.plans)),
            "text_tokens": {b: self.body_tokens(b) for b in BANDS},
            "input_tokens_cached_prefix": {b: round(self.usage(b).cache_write + self.usage(b).cache_read) for b in BANDS},
            "input_tokens_fresh": {b: round(self.usage(b).fresh_input + self.usage(b).uncached_input) for b in BANDS},
            "output_tokens": {b: round(self.usage(b).output) for b in BANDS},
            "dollars_sync": {b: round(self.dollars(b), 2) for b in BANDS},
            "dollars_batch_assumed": {b: round(self.dollars(b, batch=True), 2) for b in BANDS},
            "dollars_one_call_per_window_sync": {b: round(self.dollars(b, alt=True), 2) for b in BANDS},
            "cost_drivers_high": {k: round(v, 2) for k, v in self.usage("high").breakdown(table).items()},
            "cost_drivers_low": {k: round(v, 2) for k, v in self.usage("low").breakdown(table).items()},
        }

    def by_file(self, band: str = "high") -> list[dict]:
        table = price_table()
        rows = [
            {
                "file": p.file, "worlds": ",".join(p.worlds), "source": p.source, "passages": round(p.passages),
                "windows": round(p.windows), "text_tokens": p.body_tokens[band],
                "dollars_low": round(p.dollars("low", table), 2), "dollars_high": round(p.dollars("high", table), 2),
            }
            for p in self.plans
        ]
        rows.sort(key=lambda r: -r["dollars_high"])
        return rows


def estimate_scope(name: str, entries: Sequence[FileEntry], out_dir: Path) -> ScopeEstimate:
    return ScopeEstimate(name, [plan_file(entry, out_dir) for entry in entries])


def reuse_scope(name: str, plans: dict[str, FilePlan], entries: Sequence[FileEntry]) -> ScopeEstimate:
    return ScopeEstimate(name, [plans[e.file] for e in entries])
