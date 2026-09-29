"""Build gates: `python -m engine.m10.cli <sub> <world_code> [options]`.

Exit code 0 is a pass, 1 a failure. Findings print one per line as
`path: check-id: reason`; `--json` prints the same as one JSON document.
"""
from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

from .common import REPO_ROOT, Report, emit
from .gaps import check_gaps
from .handoff import Deps, run_handoff
from .prereview import run_prereview
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
    reports = run_handoff(args.world_code, Deps(root=args.root), quotes=not args.skip_quotes)
    return emit(reports, as_json=args.json)


def cmd_prereview(args: argparse.Namespace) -> int:
    return emit(run_prereview(args.world_code, args.doc, args.root), as_json=args.json)


def cmd_roundcount(args: argparse.Namespace) -> int:
    findings, count = check_rounds(args.world_code, args.doc, args.root, check_new=args.check_new, new_round=args.round)
    report = Report("roundcount", findings, [f"{count} review round(s) on record for doc {args.doc}"])
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
    _common_flags(p)
    p.set_defaults(func=cmd_handoff)

    p = sub.add_parser("prereview", help="compile and gates, bar screen, cross-world check, holdings; stops at the first hard failure")
    p.add_argument("world_code")
    p.add_argument("--doc", type=int)
    _common_flags(p)
    p.set_defaults(func=cmd_prereview)

    p = sub.add_parser("roundcount", help="count review rounds for a document; more than three routes to the project lead")
    p.add_argument("world_code")
    p.add_argument("doc", type=int)
    p.add_argument("--check-new", action="store_true", help="run before writing a new round file")
    p.add_argument("--round", type=int, help="with --check-new: the round number about to be written")
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
