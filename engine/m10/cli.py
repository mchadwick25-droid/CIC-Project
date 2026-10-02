"""Build gates: `python -m engine.m10.cli <sub> <world_code> [options]`.

Exit code 0 is a pass, 1 a failure. Findings print one per line as
`path: check-id: reason`; `--json` prints the same as one JSON document.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import json
import sys
from pathlib import Path

from .blind import blind, reveal
from .common import REPO_ROOT, Report, emit, registry_entry, rel
from .gaps import check_gaps
from .handoff import Deps, run_handoff
from .prereview import git_head, brief_path, run_prereview
from .rebaseline import draft_declaration
from .reviewfile import check_review_file
from .rounds import ROUTE_MESSAGE, check_rounds

OPTIONAL_MODULES = (
    "engine.m10.deployed",
    "engine.m10.validation",
    "engine.m10.regate",
    "engine.m10.claims",
    "engine.m10.integrity",
)


def _load_optional() -> list:
    loaded = []
    for name in OPTIONAL_MODULES:
        try:
            loaded.append(importlib.import_module(name))
        except ModuleNotFoundError as exc:
            if exc.name != name:
                raise
    return loaded


def cmd_handoff(args: argparse.Namespace) -> int:
    if args.draft_declaration:
        print(draft_declaration(args.world_code, args.root), end="")
        return 0
    reports = run_handoff(args.world_code, Deps(root=args.root), quotes=not args.skip_quotes)
    return emit(reports, as_json=args.json)


def cmd_prereview(args: argparse.Namespace) -> int:
    reports = run_prereview(args.world_code, args.doc, args.root)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        code = emit(reports, as_json=args.json)
    output = captured.getvalue()
    if registry_entry(args.world_code, args.root) is None:
        print(output, end="")
        return code
    saved = brief_path(args.world_code, args.doc, args.root)
    where = rel(saved, args.root)
    saved.parent.mkdir(parents=True, exist_ok=True)
    saved.write_text(f"prereview {args.world_code}" + ("" if args.doc is None else f" --doc {args.doc}") + f" at commit {git_head(args.root)[:12]}\n" + output, encoding="utf-8")
    if args.json:
        document = json.loads(output)
        document["saved"] = where
        print(json.dumps(document, indent=2))
    else:
        print(output, end="")
        print(f"review brief saved: {where}")
    return code


def cmd_roundcount(args: argparse.Namespace) -> int:
    findings, count = check_rounds(args.world_code, args.doc, args.root, check_new=args.check_new)
    report = Report("roundcount", findings, [f"{count} review file(s) on record for {'Step 0' if args.doc == 0 else f'Doc_{args.doc:02d}'}"])
    code = emit([report], as_json=args.json)
    if findings and not args.json:
        print(ROUTE_MESSAGE)
    return code


def cmd_reviewfile(args: argparse.Namespace) -> int:
    reports = []
    for raw in args.paths:
        path = Path(raw)
        path = path if path.is_absolute() else Path.cwd() / path
        reports.append(Report(f"reviewfile {raw}", check_review_file(path, REPO_ROOT)))
    return emit(reports, as_json=args.json)


def cmd_gaps(args: argparse.Namespace) -> int:
    return emit([Report("gaps", check_gaps(args.world_code, args.root))], as_json=args.json)


def cmd_blind(args: argparse.Namespace) -> int:
    if args.reveal:
        if not (args.mapping and args.checksum):
            print("blind --reveal needs --mapping and --checksum", file=sys.stderr)
            return 2
        findings, mapping = reveal(args.mapping, args.checksum, args.root)
        lines = [f"{label}: {drafter}" for label, drafter in sorted(mapping["labels"].items())] if mapping else []
        lines += [f"seed: {mapping['seed']}"] if mapping else []
    else:
        if not (args.sonnet and args.fable):
            print("blind needs --sonnet and --fable (or --reveal)", file=sys.stderr)
            return 2
        findings, mapping, checksum = blind(
            args.world_code, args.sonnet, args.fable, seed=args.seed, out_dir=args.out_dir,
            root=args.root, allow_body_mentions=args.allow_body_mentions, force=args.force,
        )
        lines = []
        if mapping:
            lines = [
                f"seed: {mapping['seed']}",
                f"MAPPING CHECKSUM: {checksum}",
                "Record this checksum in the world's cost ledger before any grading.",
            ]
            recorded = sum(1 for e in mapping["scrub_report"] if e["kind"] == "mention")
            if recorded:
                lines.append(f"{recorded} name mention(s) left unaltered and recorded in the mapping's scrub_report")
    report = Report("blind", findings, lines if args.json else [])
    if not args.json:
        for line in lines:
            print(line)
    return emit([report], as_json=args.json)


def _common_flags(p: argparse.ArgumentParser, *, root: bool = True) -> None:
    p.add_argument("--json", action="store_true", help="print one JSON document instead of lines")
    if root:
        p.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root to check (default: this repository)")


def main(argv: list[str] | None = None) -> int:
    modules = _load_optional()
    extra = ", ".join(m.__name__.rsplit(".", 1)[1] for m in modules)
    parser = argparse.ArgumentParser(
        prog="python -m engine.m10.cli",
        description="Build gates. Exit 0 passes, 1 fails." + (f" Also available: {extra}." if extra else ""),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("handoff", help="the twelve handoff checks, including quote re-verification")
    p.add_argument("world_code")
    p.add_argument("--skip-quotes", action="store_true", help="skip check 8, the quote re-verification; the run then exits non-zero as incomplete (local iteration only)")
    p.add_argument("--draft-declaration", action="store_true", help="print a pre-filled re-baseline declaration from the current disk state, without running the checks or writing a file")
    _common_flags(p)
    p.set_defaults(func=cmd_handoff)

    p = sub.add_parser("prereview", help="compile and gates, bar screen, cross-world check, holdings; stops at the first hard failure and saves the output as the review brief")
    p.add_argument("world_code")
    p.add_argument("--doc", type=int, help="the document's number, 0 for Step 0; a missing document fails")
    _common_flags(p)
    p.set_defaults(func=cmd_prereview)

    p = sub.add_parser("roundcount", help="count the review files of a document; more than three routes to the project lead")
    p.add_argument("world_code")
    p.add_argument("doc", type=int)
    p.add_argument("--check-new", action="store_true", help="run before writing a new round file")
    _common_flags(p)
    p.set_defaults(func=cmd_roundcount)

    p = sub.add_parser("reviewfile", help="check a review file's label and header fields")
    p.add_argument("paths", nargs="+")
    _common_flags(p, root=False)
    p.set_defaults(func=cmd_reviewfile)

    p = sub.add_parser("gaps", help="every open item in review and phase documents has an Open_Gaps_Tracking.md entry")
    p.add_argument("world_code")
    _common_flags(p)
    p.set_defaults(func=cmd_gaps)

    p = sub.add_parser("blind", help="blind two Doc_10 drafts as A and B, or reveal the mapping after grading")
    p.add_argument("world_code")
    p.add_argument("--sonnet", type=Path, help="the Sonnet-drafted Doc_10")
    p.add_argument("--fable", type=Path, help="the Fable-drafted Doc_10")
    p.add_argument("--seed", help="fixes the label assignment; generated and recorded when omitted")
    p.add_argument("--out-dir", type=Path, help="where Doc_10_A.md, Doc_10_B.md and the mapping go (default: Build/worlds/<code>/build/)")
    p.add_argument("--allow-body-mentions", action="store_true", help="record drafter or model names found in prose in the mapping's scrub_report instead of failing; the prose is never altered")
    p.add_argument("--force", action="store_true", help="overwrite an existing mapping file or A/B files")
    p.add_argument("--reveal", action="store_true", help="print which label is which drafter, after checking the mapping file's checksum")
    p.add_argument("--mapping", type=Path, help="with --reveal: the mapping file")
    p.add_argument("--checksum", help="with --reveal: the sha256 recorded in the cost ledger")
    _common_flags(p)
    p.set_defaults(func=cmd_blind)

    owners = {}
    for module in modules:
        before = set(sub.choices)
        module.add_parser(sub)
        for name in set(sub.choices) - before:
            owners[name] = module

    args = parser.parse_args(argv)
    if args.command in owners:
        return owners[args.command].run(args)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
