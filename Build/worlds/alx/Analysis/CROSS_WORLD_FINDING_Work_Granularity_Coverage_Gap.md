# Cross-World Finding — assigned works invisible to a volume-level discovery sweep

**Produced:** 2026-09-09 · **Origin:** OG-6 (`Unused_Assigned_Corpus_Finding_2026-09-09.md`) §7
**Instrument:** `cic/corpus-map/work_coverage_diff.py` (built for this pass)
**Scope:** all seven worlds holding both a corpus map and a record store
**Filed here** following this world's own precedent for a cross-world finding
(`CROSS_WORLD_FINDING_Lexicon_Confidence_Gap.md`, 2026-07-19), which likewise recommends
routing to each world's own maintainer rather than editing their files from here.

**Status:** finding recorded; **no world's records, documents or corpus map were changed by
this pass.** Alexandria's own remediation is OG-6's, and is separate.

---

## 1. The defect, in one paragraph

The discovery sweeps ask a **volume**-level question — "which vendored volumes does this world
name an author of, while never opening that author's own works?" (`alx.search.unopened-volume-sweep`
states its query verbatim). That instrument is structurally blind to an **assigned work sitting
inside a volume the world has already opened**. Alexandria opens `anf06` for two works, so anf06
was never an "unopened volume," while twelve further anf06 works assigned to it — including Peter
of Alexandria's *Canonical Epistle* — had zero records.

The inference in that sweep's own `divergence_note` is backwards for this failure mode: it reads a
short unopened-volume list as evidence of a well-sourced world. **The more volumes a world opens,
the more of its assigned works hide inside opened volumes, and the shorter that list becomes.**
Alexandria is the fleet's most-opened world and its worst offender.

The corpus map is already work-granular data (`work`, `author`, `locus`, `confidence`,
`source_file`). Nothing diffed it against the records. Now something does.

## 2. Result

Run: `python3 cic/corpus-map/work_coverage_diff.py --assigned-only`
(`confidence: assigned` rows only — the world's own map asserting the work belongs to it.)

| World | Opened | **AUTHOR-ABSENT** | Work-unconfirmed | Volume-unopened |
|---|---|---|---|---|
| **alx** | 14 | **6** | 0 | 0 |
| ijc | 23 | **4** | 1 | 0 |
| pahc | 44 | **3** | 0 | 0 |
| desert | 18 | **1** | 0 | 0 |
| hal | 4 | **1** | 0 | 0 |
| syr | 28 | 0 | 3 | 1 |
| cappadocian | 7 | 0 | 0 | 0 |

**15 assigned works fleet-wide whose author's name appears nowhere in the owning world's
records.** Alexandria carries 6 of them — but the defect is not Alexandria's alone, which is the
result worth having.

**AUTHOR-ABSENT** is the hard class: the assigned author is named nowhere in that world's record
store. Every non-Alexandria row below was **hand-verified by grep** before being reported here.

- **ijc** — *Julian, Letters 1–73* (including **Letter 36, the Rescript on Christian Teachers**)
  and *Letter to the Athenians*; *Canons of the Council of Sardica*; Sulpicius Severus, *Chronica*.
  Julian's Rescript is a first-order imperial-juridical document — an emperor legislating
  Christians out of the teaching profession — and the world named for imperial-juridical
  Christianity has no record of it.
- **pahc** — ***Epistle to Diognetus*** (author slug `mathetes`); *Apology of Aristides*;
  *Acts of Xanthippe and Polyxena*.
- **desert** — Sulpicius Severus, *Dialogues*.
- **hal** — Gennadius, *Lives of Illustrious Men* (the continuation of Jerome's *De Viris*, in a
  volume `hal` already opens for Jerome).

**Work-unconfirmed** (author present, this work not evidenced) and **volume-unopened** rows are
weaker signals and are listed in the tool's output; `syr`'s four are the bulk of them.

**INDETERMINATE** rows are expected and are not a defect: a world's own principal authors
(Athanasius in `alx`, Origen) appear in so many records that their names cannot discriminate
between their individual works. This instrument does not resolve those. Only reading does.

## 3. The instrument, and what it is not

`cic/corpus-map/work_coverage_diff.py`. Mechanical, no network, seconds to run.

It classifies each assigned row as AUTHOR-ABSENT / WORK-UNCONFIRMED / VOLUME-UNOPENED / OPENED /
INDETERMINATE, on the author's name as the load-bearing signal, with two guards that were added
because **both false-positive modes fired during its own construction and would have made it
report a clean bill of health for Alexandria**:

1. **Document-frequency ceiling.** The author slug `peter_alexandria` yields the token
   `alexandria`, present in all 192 Alexandria records. Without the ceiling every assigned work
   matched and the diff reported **49 opened, 0 gaps** for a world with six real ones.
2. **Filename-only detection.** Grepping `peter` in `records/alx` matches
   `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` inside two `edition:` fields, on
   lines mentioning no Peter at all. This is not hypothetical — that exact false positive is
   recorded in OG-6's own revision log as an error a human reviewer made and a later round caught.

**Title words are deliberately not sufficient on their own.** Matching them reported Peter of
Alexandria as OPENED via `paschal`, `godhead` and `canonical` — all present in Alexandria's
records for unrelated reasons (Athanasius's paschal letters; the Alexandrian canonical answers).

**Validation:** run against Alexandria it reproduces, exactly, the six absences established by
hand over seven adversarial review rounds in OG-6 — Peter (three rows), Theognostus, Pierus, and
Alexander of Alexandria. That is the only calibration it has, and it is a single world's worth.

**It is triage, not adjudication.** An AUTHOR-ABSENT row is a *question*: it cannot distinguish
"assigned and overlooked" from "assigned and deliberately declined." Several of Alexandria's
declines are correct and documented. Only reading the records settles it.

## 4. Recommended action — routed, not executed

Per the precedent this file follows: **route to each world's own maintainer; do not rewrite their
files from here.** Concretely:

1. **Adjudicate the 15.** Each is a yes/no question for the owning world: draw it in, or record a
   documented decline. Alexandria's six are OG-6's business and are already escalated.
2. **Correct the sweep's inference, not just its results.** `alx.search.unopened-volume-sweep`'s
   note that a short list is "what a well-sourced world looks like" is the reasoning that let this
   through, and the same reasoning will be reachable for by any future sweep record.
3. **Add the work-level check to the discovery step** so the volume-level sweep stops being the
   only instrument. It is cheap enough to run on every world every time.
4. **Consider whether `confidence: assigned` should mean something enforceable.** Today a world's
   map can assert a work belongs to it and nothing ever checks. That is a governance question, and
   therefore the project lead's.

Item 4, and whether to act on this fleet-wide at all, are **portfolio-level decisions**
(`cic-build-cycle` escalation category 2). This document records the finding and stops there.
