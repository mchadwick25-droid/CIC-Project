from collections import defaultdict
from pathlib import Path

import yaml

from .bench import DEPTH, KS, QUESTION_COVERAGE, Case, diagnose, recall


def load_cluster_names(repository: Path = QUESTION_COVERAGE / "Repository") -> dict[str, str]:
    return yaml.safe_load((repository / "00-frame.yaml").read_text(encoding="utf-8"))["clusters"]


def _row(label: str, cases: list[Case]) -> str:
    return f"| {label} | {len(cases)} | " + " | ".join(f"{recall(cases, k):.0%}" for k in KS) + " |"


def best_wording(cases: list[Case]) -> list[Case]:
    best: dict[tuple[str, str], Case] = {}
    for c in cases:
        key = (c.sub_question, c.record_id)
        held = best.get(key)
        if held is None or (c.best_rank is not None and (held.best_rank is None or c.best_rank < held.best_rank)):
            best[key] = c
    return list(best.values())


def render_report(
    db_path: Path, world: str, cases: list[Case], gold_cache: dict[str, dict[str, str]], ungrounded: dict[str, list[str]],
    cluster_names: dict[str, str], subquestions: dict[str, dict], index_meta: dict[str, str],
) -> str:
    pairs = best_wording(cases)
    out = [
        f"# S1-05 retrieval bench: no-context BM25 on {world}'s shelf",
        "",
        f"Index {index_meta.get('version', '')[:12]}: {index_meta.get('passages', '?')} passages in {index_meta.get('files', '?')} files, "
        f"context column empty. Lens: files on {world}'s shelf. Ranking: SQLite FTS5 bm25 over passage text, query terms ORed after dropping English "
        "function words. No model call.",
        "",
        "Ground truth: each record the coverage maps list for a sub-question (the `records` of the world's cell), and the vendored file and line "
        "ranges its `sources` cite (plus, for quote records, the passage holding the quote's first ten words). A case is one question wording against "
        f"one such record; it is reached at k when a passage holding the record's cited text is among the top k. Ranks are searched to depth {DEPTH}. "
        "Records with no resolvable citation in the index are left out and listed at the end.",
        "",
        f"Cases: {len(cases)} wording-by-record cases over {len(pairs)} sub-question-by-record pairs and {len({c.record_id for c in cases})} records.",
        "",
        "## Recall",
        "",
        "| Level | Cases | recall@5 | recall@10 | recall@20 |",
        "|---|---:|---:|---:|---:|",
        _row("Every wording against every cited record", cases),
        _row("Best wording per sub-question and record", pairs),
        "",
        "## By category",
        "",
        "| Cluster | Cases | recall@5 | recall@10 | recall@20 |",
        "|---|---:|---:|---:|---:|",
    ]
    for cluster in sorted({c.cluster for c in cases}, key=lambda x: int(x[1:])):
        out.append(_row(f"{cluster} {cluster_names.get(cluster, '')}", [c for c in cases if c.cluster == cluster]))
    out += ["", "## By sub-question (every wording)", "", "| Sub-question | Cases | recall@5 | recall@10 | recall@20 |", "|---|---:|---:|---:|---:|"]
    for sub in sorted({c.sub_question for c in cases}, key=lambda s: (int(s.split(".")[0][1:]), int(s.split("S")[-1]))):
        out.append(_row(f"{sub} {subquestions[sub]['label'][:70]}", [c for c in cases if c.sub_question == sub]))
    groups: dict[tuple[str, str], list[Case]] = defaultdict(list)
    for c in cases:
        groups[(c.sub_question, c.record_id)].append(c)
    misses = [(key, group) for key, group in groups.items()
              if not any(c.best_rank is not None and c.best_rank <= max(KS) for c in group)]
    reasons: dict[str, int] = defaultdict(int)
    rows = []
    for (sub, rid), group in sorted(misses):
        reason, detail = diagnose(db_path, group, gold_cache[rid])
        reasons[reason] += 1
        ranks = [c.best_rank for c in group if c.best_rank is not None]
        rows.append(f"| {sub} | `{rid}` | {min(ranks) if ranks else f'beyond {DEPTH}'} | {reason} | {detail} |")
    summary = ", ".join(f"{k} {v}" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1]))
    out += ["", f"## Misses: pairs no wording reaches within {max(KS)}", "",
            f"{len(misses)} of {len(groups)} pairs. By reason: {summary or 'none'}.",
            "", "| Sub-question | Record | Best rank | Reason | Detail |", "|---|---|---:|---|---|", *rows]
    skipped = sorted((cell, rid) for cell, rids in ungrounded.items() for rid in rids)
    out += ["", "## Records left out (no resolvable citation in the index)", "",
            f"{len(skipped)} cell-by-record entries, {len({r for _, r in skipped})} records.", ""]
    out += [f"- {cell} `{rid}`" for cell, rid in skipped]
    return "\n".join(out) + "\n"
