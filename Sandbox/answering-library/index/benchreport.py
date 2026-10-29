from collections import defaultdict
from pathlib import Path

import yaml

from .bench import CONDITIONS, DEPTH, KS, QUESTION_COVERAGE, Case, diagnose, recall

RAW, LABELLED, ROUTING = CONDITIONS


def load_cluster_names(repository: Path = QUESTION_COVERAGE / "Repository") -> dict[str, str]:
    return yaml.safe_load((repository / "00-frame.yaml").read_text(encoding="utf-8"))["clusters"]


def of(cases: list[Case], condition: str) -> list[Case]:
    return [c for c in cases if c.condition == condition]


def best_wording(cases: list[Case]) -> list[Case]:
    best: dict[tuple[str, str], Case] = {}
    for c in cases:
        key = (c.sub_question, c.record_id)
        held = best.get(key)
        if held is None or (c.best_rank is not None and (held.best_rank is None or c.best_rank < held.best_rank)):
            best[key] = c
    return list(best.values())


def _cells(cases: list[Case]) -> str:
    raw, labelled, routing = of(cases, RAW), of(cases, LABELLED), of(cases, ROUTING)
    return (f"{len(raw)} | " + " | ".join(f"{recall(raw, k):.0%}" for k in KS) + " | "
            + " | ".join(f"{recall(labelled, k):.0%}" for k in KS[1:]) + " | "
            + " | ".join(f"{recall(routing, k):.0%}" for k in KS[1:]) + " |")


HEADER = ("| {0} | Cases (wording) | wording @5 | @10 | @20 | wording+label @10 | @20 | record routing @10 | @20 |\n"
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|")


def render_report(
    db_path: Path, world: str, cases: list[Case], gold_cache: dict[str, dict[str, str]], ungrounded: dict[str, list[str]],
    cluster_names: dict[str, str], subquestions: dict[str, dict], index_meta: dict[str, str],
) -> str:
    raw = of(cases, RAW)
    pairs = best_wording(raw)
    out = [
        f"# S1-05 retrieval bench: no-context BM25 on {world}'s shelf",
        "",
        f"Index {index_meta.get('version', '')[:12]}: {index_meta.get('passages', '?')} passages in {index_meta.get('files', '?')} files, "
        f"context column empty. Lens: files on {world}'s shelf. Ranking: SQLite FTS5 bm25 over passage text, query terms ORed after dropping English "
        "function words. No model call.",
        "",
        "Ground truth: each record the coverage maps list for a sub-question (the `records` of the world's cell), and the vendored file and line "
        "ranges its `sources` cite (plus, for quote records, the passage holding the quote's first ten words). A case is one query against one such "
        f"record; it is reached at k when a passage holding the record's cited text is among the top k. Ranks are searched to depth {DEPTH}. "
        "Records with no resolvable citation in the index are left out and listed at the end.",
        "",
        "Three queries are scored. `wording` is the visitor's question as written in the repository. `wording+label` adds the sub-question's label "
        "(a topic gloss the system holds). `record routing` is the record's own `retrieve_when` text, which is what a routing layer that already "
        "knows the record would send; it shows what the index can reach, not what raw visitor words reach.",
        "",
        f"Cases: {len(raw)} wording-by-record cases over {len(pairs)} sub-question-by-record pairs and {len({c.record_id for c in raw})} records.",
        "",
        "## Recall",
        "",
        HEADER.format("Level"),
        f"| Every wording against every cited record | {_cells(cases)}",
        f"| Best wording per sub-question and record | {_cells(best_wording_all(cases))}",
        "",
        "## By category",
        "",
        HEADER.format("Cluster"),
    ]
    for cluster in sorted({c.cluster for c in cases}, key=lambda x: int(x[1:])):
        out.append(f"| {cluster} {cluster_names.get(cluster, '')} | {_cells([c for c in cases if c.cluster == cluster])}")
    out += ["", "## By sub-question", "", HEADER.format("Sub-question")]
    for sub in sorted({c.sub_question for c in cases}, key=lambda s: (int(s.split(".")[0][1:]), int(s.split("S")[-1]))):
        out.append(f"| {sub} {subquestions[sub]['label'][:60]} | {_cells([c for c in cases if c.sub_question == sub])}")
    groups: dict[tuple[str, str], list[Case]] = defaultdict(list)
    for c in raw:
        groups[(c.sub_question, c.record_id)].append(c)

    def best(sub, rid, condition):
        ranks = [c.best_rank for c in cases if c.condition == condition and c.sub_question == sub and c.record_id == rid and c.best_rank]
        return str(min(ranks)) if ranks else f">{DEPTH}"

    misses = [(key, group) for key, group in groups.items()
              if not any(c.best_rank is not None and c.best_rank <= max(KS) for c in group)]
    reasons: dict[str, int] = defaultdict(int)
    rows = []
    for (sub, rid), group in sorted(misses):
        reason, detail = diagnose(db_path, group, gold_cache[rid])
        reasons[reason] += 1
        rows.append(f"| {sub} | `{rid}` | {best(sub, rid, RAW)} | {best(sub, rid, LABELLED)} | {best(sub, rid, ROUTING)} | {reason} | {detail} |")
    summary = ", ".join(f"{k} {v}" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1]))
    out += ["", f"## Misses: pairs no visitor wording reaches within {max(KS)}", "",
            f"{len(misses)} of {len(groups)} pairs. By reason: {summary or 'none'}. Best rank over the sub-question's wordings, under each query.",
            "", "| Sub-question | Record | wording | wording+label | record routing | Reason | Detail |",
            "|---|---|---:|---:|---:|---|---|", *rows]
    skipped = sorted((cell, rid) for cell, rids in ungrounded.items() for rid in rids)
    out += ["", "## Records left out (no resolvable citation in the index)", "",
            f"{len(skipped)} cell-by-record entries, {len({r for _, r in skipped})} records.", ""]
    out += [f"- {cell} `{rid}`" for cell, rid in skipped]
    return "\n".join(out) + "\n"


def best_wording_all(cases: list[Case]) -> list[Case]:
    result = []
    for condition in CONDITIONS:
        result += best_wording(of(cases, condition))
    return result
