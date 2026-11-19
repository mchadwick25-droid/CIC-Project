import argparse
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path[:] = [p for p in sys.path if Path(p or ".").resolve() != _HERE]
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parents[2]))

from engine.provider import guard  # noqa: E402
from index import card, catalog, contract, estimate, generate, report, retrieve, sample, store  # noqa: E402
from index.pricing import MODEL_ID  # noqa: E402

DEFAULT_SAMPLE_WORLD = "lpc"


def _out_dir(args) -> Path:
    return Path(args.out_dir) if args.out_dir else catalog.DEFAULT_OUT_DIR


def _selection_path(args) -> Path:
    return _out_dir(args) / "sample" / f"{args.world}_sample.json"


def _scope_entries(args, shelves):
    if getattr(args, "union", False):
        return "union", list(shelves.values())
    return args.world, catalog.world_files(shelves, args.world)


def _jobs_for(args, shelves) -> tuple[str, list[generate.Job]]:
    out_dir = _out_dir(args)
    if getattr(args, "sample", None):
        world, items = sample.read_selection(_out_dir(args) / "sample" / f"{args.sample}_sample.json")
        passages = sample.selection_passages(out_dir, items)
        return f"sample:{world}", [generate.Job(shelves[name], ps) for name, ps in passages.items()]
    name, entries = _scope_entries(args, shelves)
    jobs = []
    for entry in entries:
        passages = contract.read_file_passages(out_dir, entry.file)
        if not passages:
            raise SystemExit(f"no segmenter output for {entry.file}; the run does not guess passages")
        jobs.append(generate.Job(entry, passages))
    return name, jobs


def cmd_estimate(args) -> int:
    out_dir = _out_dir(args)
    shelves = catalog.load_shelves()
    plans = {name: estimate.plan_file(entry, out_dir) for name, entry in shelves.items()}
    union = estimate.reuse_scope("union", plans, list(shelves.values()))
    scopes = [union]
    for world in catalog.BUILT_WORLDS:
        scopes.append(estimate.reuse_scope(f"world {world}", plans, catalog.world_files(shelves, world)))
    selection = _selection_path(args)
    if selection.is_file():
        world, items = sample.read_selection(selection)
        scopes.append(estimate.ScopeEstimate(f"sample ({world})", sample.plan_selection(shelves, out_dir, items)))
    else:
        scopes.append(estimate.ScopeEstimate(f"sample ({args.world}, modeled from the file list)", sample.modeled_plans(shelves, out_dir)))
    print(report.render_estimate(scopes, union, top=args.top))
    if args.json:
        Path(args.json).write_text(json.dumps({"scopes": [s.summary() for s in scopes], "files": union.by_file()}, indent=1), encoding="utf-8")
    return 0


def cmd_sample_select(args) -> int:
    out_dir = _out_dir(args)
    shelves = catalog.load_shelves()
    entries = catalog.world_files(shelves, args.world)
    if not contract.has_segmenter_output(out_dir):
        print(f"no segmenter output under {contract.passages_dir(out_dir)}; the sample cannot be selected yet", file=sys.stderr)
        return 3
    chosen = sample.select_sample(entries, out_dir, args.per_file)
    sample.write_selection(_selection_path(args), args.world, chosen)
    print(f"sample for {args.world}: {sum(len(s.passage_ids) for s in chosen)} passages in {len(chosen)} files -> {_selection_path(args)}")
    for item in chosen:
        print(f"  {item.role}: {item.file} ({len(item.passage_ids)} passages)")
    return 0


def cmd_sample_card(args) -> int:
    out_dir = _out_dir(args)
    shelves = catalog.load_shelves()
    plans = {name: estimate.plan_file(entry, out_dir) for name, entry in shelves.items()}
    union = estimate.reuse_scope("union", plans, list(shelves.values()))
    selection = _selection_path(args)
    segmented = selection.is_file()
    if segmented:
        _, items = sample.read_selection(selection)
        sample_plans = sample.plan_selection(shelves, out_dir, items)
    else:
        sample_plans = sample.modeled_plans(shelves, out_dir)
    text = card.render_card(estimate.ScopeEstimate("sample", sample_plans), union, shelves, segmented=segmented,
                            out_dir=catalog.DEFAULT_OUT_DIR, live_test_name=args.name)
    Path(args.out).write_text(text, encoding="utf-8")
    print(f"card written to {args.out} ({'segmented' if segmented else 'modeled'})")
    return 0


def cmd_run(args) -> int:
    live_test = None
    if not args.dry_run:
        live_test = guard.admit()
        if live_test is None:
            raise SystemExit("this command runs only as an approved live test")
    out_dir = _out_dir(args)
    shelves = catalog.load_shelves()
    scope, jobs = _jobs_for(args, shelves)
    plans = [estimate.plan_from_passages(job.entry, job.passages) for job in jobs]
    scope_estimate = estimate.ScopeEstimate(scope, plans)
    _, pending = generate.pending_count(jobs, out_dir, MODEL_ID)
    name = live_test.name if live_test else args.live_test
    cap = live_test.cap_usd if live_test else args.cap_usd
    print(report.render_settings(scope_estimate, live_test=name, cap_usd=cap, out_dir=out_dir, pending=pending))
    if args.dry_run:
        return 0
    from engine.provider import anthropic_direct

    guard.note_model(MODEL_ID)
    client = anthropic_direct.make_client()
    result = generate.run_jobs(client, jobs, out_dir, MODEL_ID, live_test.name, (guard.LiveTestCapReached,))
    summary = guard.run_summary() or {}
    record = {**result.__dict__, "run": summary, "scope": scope}
    log = generate.context_dir(out_dir) / "_runs.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    with open(log, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, default=str) + "\n")
    print(json.dumps(record, indent=1, default=str))
    return 0 if result.stopped is None else 4


def cmd_build_index(args) -> int:
    out_dir = _out_dir(args)
    shelves = catalog.load_shelves()
    scope, entries = _scope_entries(args, shelves)
    missing = [e.file for e in entries if not (contract.passages_dir(out_dir) / f"{contract.file_stem(e.file)}.jsonl").is_file()]
    if missing:
        raise SystemExit(f"no segmenter output for {len(missing)} file(s), first {missing[0]}; the index does not guess passages")

    def groups():
        for entry in entries:
            file_passages = contract.read_file_passages(out_dir, entry.file) or []
            usable = store.usable_contexts(generate.read_context_lines(out_dir, entry.file), file_passages)
            yield entry.file, file_passages, usable

    db_path = Path(args.db) if args.db else out_dir / "index" / f"{scope}.sqlite"
    stats = store.build_index_stream(db_path, groups(), shelves, MODEL_ID)
    print(f"index {db_path}: {stats.files} files, {stats.passages} passages, {stats.contexts} context lines, "
          f"version {stats.version}, built in {stats.seconds:.1f} s")
    return 0


def cmd_bench(args) -> int:
    from index import bench, benchreport

    db = Path(args.db)
    evidence = bench.load_record_evidence(catalog.REPO_ROOT / "records" / args.world)
    cells = bench.load_cells(args.world)
    subquestions = bench.load_subquestions()
    questions = bench.load_questions()
    cases, gold, ungrounded = bench.run_bench(db, args.world, evidence, cells, subquestions, questions)
    floor = None
    if args.ocr_floor is not None:
        floor = (args.ocr_floor, bench.run_bench(db, args.world, evidence, cells, subquestions, questions, min_ocr=args.ocr_floor)[0])
    text = benchreport.render_report(db, args.world, cases, gold, ungrounded, benchreport.load_cluster_names(), subquestions,
                                     store.read_meta(db), floor)
    Path(args.out).write_text(text, encoding="utf-8")
    print(f"bench written to {args.out}: {len(cases)} cases")
    return 0


def cmd_search(args) -> int:
    db = Path(args.db)
    hits = retrieve.search(db, args.query, world=args.world, roles=args.role or None, speakers=args.speaker or None,
                           min_ocr=args.min_ocr, limit=args.limit)
    for hit in hits:
        s = hit.source
        print(f"{hit.score:.3f}  {hit.passage_id}  {s['path']} bytes {s['byte_start']}-{s['byte_end']}  locus {s['division_locus']}  "
              f"speaker {s['speaker']['state']}  ocr {s['ocr_score']}")
        print(f"  retrieval context (never source text): {hit.context or '(none)'}")
        print(f"  source text: {' '.join(hit.text.split())[:300]}")
    return 0


def cmd_verify(args) -> int:
    problems = retrieve.verify_sources(Path(args.db), limit=args.limit)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} passage(s) fail to resolve to the vendored file's byte span")
    return 1 if problems else 0


def cmd_show_sample(args) -> int:
    out_dir = _out_dir(args)
    world, items = sample.read_selection(_selection_path(args))
    passages = sample.selection_passages(out_dir, items)
    shown = 0
    for item in items:
        lines = generate.read_context_lines(out_dir, item.file)
        for passage in passages[item.file]:
            record = lines.get(passage.passage_id)
            if not record or shown >= args.n:
                continue
            step = max(1, len(passages[item.file]) // max(1, args.n // len(items)))
            if passage.ordinal % step:
                continue
            shown += 1
            print(f"[{item.role}] {passage.passage_id}  locus {passage.division_locus}  ocr {passage.ocr_score}  check {record['status']} {record['reasons']}")
            print(f"  CONTEXT LINE (retrieval only): {record['context']}")
            print(f"  PASSAGE (source): {' '.join(passage.text.split())[:420]}\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Contextual indexing for the answering library")
    parser.add_argument("--out-dir", default=None)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("estimate")
    p.add_argument("--world", default=DEFAULT_SAMPLE_WORLD)
    p.add_argument("--top", type=int, default=15)
    p.add_argument("--json", default=None)
    p.set_defaults(func=cmd_estimate)

    p = sub.add_parser("sample-select")
    p.add_argument("--world", default=DEFAULT_SAMPLE_WORLD)
    p.add_argument("--per-file", type=int, default=sample.PER_FILE_PASSAGES)
    p.set_defaults(func=cmd_sample_select)

    p = sub.add_parser("sample-card")
    p.add_argument("--world", default=DEFAULT_SAMPLE_WORLD)
    p.add_argument("--out", required=True)
    p.add_argument("--name", default="S1-05 contextual indexing lpc sample")
    p.set_defaults(func=cmd_sample_card)

    p = sub.add_parser("run")
    scope = p.add_mutually_exclusive_group(required=True)
    scope.add_argument("--sample", metavar="WORLD")
    scope.add_argument("--world")
    scope.add_argument("--union", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    guard.add_arguments(p)
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("build-index")
    scope = p.add_mutually_exclusive_group(required=True)
    scope.add_argument("--world")
    scope.add_argument("--union", action="store_true")
    p.add_argument("--db", default=None)
    p.set_defaults(func=cmd_build_index)

    p = sub.add_parser("bench")
    p.add_argument("--db", required=True)
    p.add_argument("--world", default=DEFAULT_SAMPLE_WORLD)
    p.add_argument("--out", required=True)
    p.add_argument("--ocr-floor", type=float, default=None, help="also score the bench with passages under this OCR score left out of the ranking")
    p.set_defaults(func=cmd_bench)

    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("--db", required=True)
    p.add_argument("--world")
    p.add_argument("--role", action="append")
    p.add_argument("--speaker", action="append")
    p.add_argument("--min-ocr", type=float)
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("verify")
    p.add_argument("--db", required=True)
    p.add_argument("--limit", type=int)
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("show-sample")
    p.add_argument("--world", default=DEFAULT_SAMPLE_WORLD)
    p.add_argument("--n", type=int, default=9)
    p.set_defaults(func=cmd_show_sample)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
