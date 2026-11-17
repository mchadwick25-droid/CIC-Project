"""Readability check for Church Family Tree profile briefs (Who and council).

Grade is counted on the full text and must not pass PROFILE_FK_CEILING; a
grade under PROFILE_FK_FLOOR is printed as a note and does not fail. Reading
ease is counted with proper names left out of the syllable count and must
reach PROFILE_FRE_FLOOR. The longest sentence is printed. The limits are the
ones in Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Standard.md.

    python -m engine.m1.profile_readability PATH [PATH ...]
    python -m engine.m1.profile_readability --base REF
    python -m engine.m1.profile_readability --base REF --list
    python -m engine.m1.profile_readability --report PATH [PATH ...]

A PATH is a brief file or a folder searched for *.brief.txt. --base grades
the profile briefs added or changed since the merge-base with REF; a brief
that was only moved is not graded, and one that was moved and edited is.
--list prints those paths and grades nothing. The exit status is 1 when a
graded brief fails, unless --report is given, and 2 when a brief cannot be
read or git cannot answer.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from .fk import _SENTENCE_END, _count_syllables, fk_grade

PROFILE_FK_FLOOR = 8
PROFILE_FK_CEILING = 10
PROFILE_FRE_FLOOR = 60
MIN_WORDS = 12
SHORT_SENTENCE_WORDS = 8

REPO = Path(__file__).resolve().parents[2]
PROFILE_ROOTS = (
    "Build/Ministry/Features/Church-Family-Tree/Who-Profiles",
    "Build/Ministry/Features/Church-Family-Tree/Council-Profiles",
)
BRIEF_SUFFIX = ".brief.txt"
_PURE_RENAME = "R100"

_TOKEN = re.compile(r"[A-Za-z']+|[.!?]+|[\"“‘(\[]|\n+")
_WORD = re.compile(r"[A-Za-z']+")
_JOINING_WORDS = re.compile(r"\b(because|since|though|although|so that|until|yet|even so)\b")
_JOINING_COMMAS = re.compile(r", (so|for) ")


def normalize(text: str) -> str:
    return (text or "").replace("’", "'").strip()


def _base(form: str) -> str:
    if form.endswith("'s"):
        return form[:-2]
    return form.rstrip("'")


def _forms(text: str) -> list[tuple[str, str, bool]]:
    """(raw word, form, is an opening word) for every word, in order.

    A straight double quote opens and closes by turns; only the opening one
    makes the next word an opening word. A token of apostrophes alone keeps
    its place with an empty form, so the word count matches fk.py's.
    """
    out = []
    opening = True
    quote_open = False
    for match in _TOKEN.finditer(text):
        token = match.group()
        if token == '"':
            quote_open = not quote_open
            opening = opening or quote_open
            continue
        if not _WORD.fullmatch(token):
            if "\n" in token:
                quote_open = False
            opening = True
            continue
        form = token.strip("'")
        if not form:
            out.append((token, "", False))
            continue
        out.append((token, form, opening or token.startswith("'")))
        opening = False
    return out


def _can_be_name(form: str) -> bool:
    return bool(form) and form[0].isupper() and form.split("'")[0] != "I"


def proper_name_forms(text: str) -> set[str]:
    """The word forms that count as proper names in `text`."""
    forms = [entry for entry in _forms(normalize(text)) if entry[1]]
    lower = {_base(form) for _, form, _ in forms if form[0].islower()}
    seen_inside = {
        _base(form)
        for _, form, opening in forms
        if not opening and _can_be_name(form) and _base(form).lower() not in lower
    }
    return {form for _, form, _ in forms if _can_be_name(form) and _base(form) in seen_inside}


@dataclass(frozen=True)
class ProfileScore:
    words: int
    sentences: int
    fk: float
    fk_names_out: float
    fre_names_out: float
    words_per_sentence: float
    joining_per_100: float
    short_sentence_share: float
    longest_sentence: int

    @property
    def notes(self) -> tuple[str, ...]:
        if self.fk < PROFILE_FK_FLOOR:
            return (f"grade {self.fk:.1f} is under {PROFILE_FK_FLOOR}: the listener read checks it is not flat",)
        return ()

    @property
    def failures(self) -> tuple[str, ...]:
        found = []
        if self.fk > PROFILE_FK_CEILING:
            found.append(f"grade {self.fk:.1f} on the full text, above the ceiling of {PROFILE_FK_CEILING}")
        if self.fre_names_out < PROFILE_FRE_FLOOR:
            found.append(f"reading ease {self.fre_names_out:.1f} with names left out, below the floor of {PROFILE_FRE_FLOOR}")
        return tuple(found)

    @property
    def passed(self) -> bool:
        return not self.failures


def grade_profile_text(text: str) -> ProfileScore | None:
    """Score one brief, or None when it is under MIN_WORDS words."""
    text = normalize(text)
    words = _WORD.findall(text)
    if len(words) < MIN_WORDS:
        return None
    sentences = [s for s in _SENTENCE_END.split(text) if s.strip()]
    n_sentences = max(len(sentences), 1)
    per_sentence = len(words) / n_sentences
    names = proper_name_forms(text)
    plain = [raw for raw, form, _ in _forms(text) if form not in names]
    syllables_per_plain_word = sum(_count_syllables(w) for w in plain) / max(len(plain), 1)
    lowered = text.lower()
    joining = len(_JOINING_WORDS.findall(lowered)) + len(_JOINING_COMMAS.findall(lowered))
    lengths = [len(_WORD.findall(s)) for s in sentences]
    short = sum(1 for n in lengths if n <= SHORT_SENTENCE_WORDS)
    return ProfileScore(
        words=len(words),
        sentences=n_sentences,
        fk=fk_grade(text),
        fk_names_out=0.39 * per_sentence + 11.8 * syllables_per_plain_word - 15.59,
        fre_names_out=206.835 - 1.015 * per_sentence - 84.6 * syllables_per_plain_word,
        words_per_sentence=per_sentence,
        joining_per_100=100 * joining / len(words),
        short_sentence_share=short / n_sentences,
        longest_sentence=max(lengths, default=0),
    )


def profile_readability_failures(text: str) -> list[str]:
    score = grade_profile_text(text)
    return [] if score is None else list(score.failures)


def is_profile_brief(rel: str) -> bool:
    return rel.endswith(BRIEF_SUFFIX) and any(rel.startswith(root + "/") for root in PROFILE_ROOTS)


def changed_brief_names(base: str, repo: Path = REPO) -> list[str]:
    """Repo-relative paths of the profile briefs added or edited since the
    merge-base with `base`. A brief that was only moved is left out."""

    def git(*args: str) -> str:
        return subprocess.run(
            ["git", "-c", "core.quotePath=false", *args], cwd=repo, check=True, capture_output=True, text=True
        ).stdout

    merge_base = git("merge-base", base, "HEAD").strip()
    names = []
    for line in git("diff", "--name-status", "-M", "--diff-filter=AMR", merge_base, "HEAD").split("\n"):
        fields = line.split("\t")
        if len(fields) < 2 or fields[0] == _PURE_RENAME:
            continue
        if is_profile_brief(fields[-1]):
            names.append(fields[-1])
    return names


def _collect(paths: list[str]) -> list[Path]:
    found = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            found.extend(sorted(path.rglob("*" + BRIEF_SUFFIX)))
        else:
            found.append(path)
    return found


def _line(path: Path, score: ProfileScore | None) -> str:
    if score is None:
        return f"{path}: under {MIN_WORDS} words, not scored"
    verdict = "pass" if score.passed else "FAIL: " + "; ".join(score.failures)
    if score.notes:
        verdict += " (note: " + "; ".join(score.notes) + ")"
    return (
        f"{path}: {score.words} words, grade {score.fk:.1f} (names out {score.fk_names_out:.1f}), "
        f"reading ease names out {score.fre_names_out:.1f}, {score.words_per_sentence:.1f} words a sentence, "
        f"{score.joining_per_100:.1f} joining words per 100, "
        f"{round(100 * score.short_sentence_share)}% short sentences, "
        f"longest sentence {score.longest_sentence} words - {verdict}"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--base")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args(argv)
    if bool(args.base) == bool(args.paths):
        parser.error("give either paths or --base")
    if args.list and not args.base:
        parser.error("--list needs --base")
    if args.base:
        try:
            names = changed_brief_names(args.base)
        except subprocess.CalledProcessError as error:
            print(f"git could not list the changed briefs: {error.stderr.strip()}", file=sys.stderr)
            return 2
        if args.list:
            print("\n".join(names), end="\n" if names else "")
            return 0
        briefs = [REPO / name for name in names]
    else:
        briefs = _collect(args.paths)
    failed = 0
    for path in briefs:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            print(f"{path}: cannot be read: {error}", file=sys.stderr)
            return 2
        score = grade_profile_text(text)
        print(_line(path, score))
        if score is not None and not score.passed:
            failed += 1
    print(f"{len(briefs)} brief(s) graded, {failed} failing", file=sys.stderr)
    return 1 if failed and not args.report else 0


if __name__ == "__main__":
    sys.exit(main())
