# Decision Log — Tech-Readiness Package 2 (Operations)

Append-only, per `CLAUDE.md`. One entry per finding or decision this
package made while producing `Report.md`.

---

**Entry 1 — 2026-09-21.** The launch brief's divergence claim (main carries
the transparency engine, live carries atlas-sync/card-redesign) was checked
before anything was built on it, per this package's own "verify first, not
assume" instruction. First check (`git ls-tree origin/main -- Ministry/
Features/Conversation-Transparency-Engine/`) came back empty — the opposite
of the brief. Reported to the user as a blocker before proceeding further;
the user asked for a re-run with `git fetch origin main live` first. The
re-run found `origin/main` had advanced (`b7eae354` → `c9b09ea1`) between
the two checks — new commits landed on `main` in the interim, which is why
the first pass caught it empty. On the fresh fetch, both branches carry all
5 transparency-engine files; `main`'s own Decision-Log has 27 entries,
`live`'s has 3 — confirming the brief's overall shape (main ahead on the
transparency engine) was correct, and the first check's contradiction was a
timing artifact, not a factual error in the brief. Diff-filter counts
(43 live-only / 158 main-only / 1,300 both-differ) matched exactly what the
user separately supplied. Logged here because the lesson — treat every
factual claim in a dispatched brief as a hypothesis to verify, including
after it's already been re-verified once — is the user's own explicit
instruction for this and future packages, not just this one check.

**Entry 2 — 2026-09-21.** Found, while building the divergence inventory:
`main`'s `CLAUDE.md` is missing a default-actions row `live`'s copy still
carries (`Representative identity, title, or voice decision | Always ask`).
Traced to commit `6f3a4e6e` (2026-09-20) — Mark's own direct instruction to
remove it, given in-session, for reasons stated in full in that commit's own
message. Not an open question: `live` simply predates this authorized edit.
Logged here rather than only in `Report.md` because a `CLAUDE.md` diff is
exactly the kind of thing this package's own governance discipline requires
surfacing explicitly, resolved or not.

**Entry 3 — 2026-09-21.** Design decision: DB backups (`engine/api/
db_backup.py`) use a bucket and credentials **separate** from
`CIC_API_PACKAGE_BUCKET` (compiled world packages). Reasoning: backups carry
real participant transcripts and cost records, a different sensitivity
class from public-ish compiled packages; sharing a credential would widen
the package-fetch path's own blast radius for no benefit. Not escalated —
this is an infra/credential-scoping call within this package's own hard-rule
scope (render.yaml, a backup script), not a governance or portfolio
decision.

**Entry 4 — 2026-09-21.** Verified against Render's own documentation
(`https://render.com/docs/disks`) before designing the backup schedule: a
Persistent Disk attaches to exactly one running service; neither a Cron Job
nor a one-off Job can reach a disk already attached elsewhere (both run on
separate compute). `engine/m7/scheduler.py`'s own module docstring
independently documents hitting this same constraint and resolving it the
same way (an in-process daily thread) — `engine/api/db_backup.py`'s
scheduler is a third sibling of that established pattern, not a new design.
This ruled out the launch brief's own literal phrasing ("a scheduled-job
spec for Render (cron or one-off job)") as written; the actual deliverable
is an in-process thread plus the dashboard steps for the one-time R2 bucket
setup, which is what `CiC_Backup_Restore_Runbook.md` specifies.

**Entry 5 — 2026-09-21.** Scope decision: `PR 1` (reconciling `live`-only
atlas-sync tooling and the card redesign back onto `main`) is drafted in
`Report.md` §2 but **not performed** in this package. It touches
`engine/m2/`, `engine/m6/`, and `cic-website/`, all outside this package's
own hard-rule scope ("touches render.yaml, docs, a backup script, and
runbooks only") and outside the Conversation & Transparency Engine
workstream's own coordination boundary too — it belongs to neither
workstream cleanly and is handed to Mark to assign, not claimed by this one.

**Entry 6 — 2026-09-21.** Report and this log published; an entry appended
to `Ministry/Features/Conversation-Transparency-Engine/Decision-Log.md`
(drafted as that workstream's own Entry 28, landed as **Entry 30** — a
merge from `origin/main` picked up two of that workstream's own entries,
R19's ruling and ten more rulings (Entries 28–29), concurrently added while
this report was being written; renumbered on merge, per that file's own
"never renumber a past entry" rule, since this package's entry was the
later arrival) naming the divergence inventory and the promotion PR set now
in front of Mark, per the launch brief's own instruction to hand this to
both Mark and that workstream. No file inside that workstream's own
directory was edited beyond that one append.

**Entry 7 — 2026-09-21.** While resolving the Entry 6 merge conflict, noted
that `origin/main` had advanced again since the divergence inventory in
`Report.md` §1 was written (`c9b09ea1` → `4bd45804`, the R19/R5–R18 rulings
above) — a normal, expected consequence of an active concurrent workstream,
not a defect in the report. `Report.md`'s own commit-hash citations
(`c9b09ea1`/`e693b048`) are left as the commits actually compared, not
updated to chase a moving target; the divergence categories and the
promotion PR sequencing they support are unaffected by this specific
advance (none of the four new commits touch `engine/m2/`, `engine/m6/`,
`cic-website/`, or the `lpc` world's own registration status).

**Entry 8 — 2026-09-21.** `origin/main` advanced twice more
(`4bd45804` → `5834aae3`, the R8/R9/R10/R13/R19-guard-fix rulings) before
this PR merged, each landing its own append to the transparency-engine's
Decision-Log.md concurrently with this package's own single append. Merged
both times; this package's entry moved from Entry 28 (first draft) to
Entry 30 (Entry 6 above) to its final number **Entry 32**, renumbered each
time on merge per that file's own "never renumber a past entry" rule — the
later arrival renumbers itself, never the entries already on `main`. Entry
6 above is left as originally written (its own "Entry 30" was accurate at
the time) rather than edited, per this log's own append-only rule; this
entry is the correction.

**Entry 9 — 2026-09-21.** Mark found `CiC_Alerting_Runbook.md` §2 cited
`.github/workflows/health-check.yml` as if it already existed — it doesn't
(signal 2 is spec-only, "Not built this pass," same as signals 3/5/6) — and
`tools/check_paths.py`'s CI job (`Cited paths resolve; retired paths
absent`) correctly failed on it: that file only exempts paths in dated
records, and this runbook isn't one. Fixed by rewording the example to
describe the workflow rather than name a specific, not-yet-created path
(no baseline-entry addition — the citation was simply wrong to make, not a
real pre-existing gap worth tracking). Verified locally: `python3
tools/check_paths.py --baseline tools/check_paths_baseline.txt` exits 0,
"0 new unresolved path citation(s)" (the run also reports one unrelated,
pre-existing baseline entry that now resolves — `Ministry/Communication/
CiC_Demo_Conversation_Captures_V0_1.md`'s own citation of
`.claude/launch.json` — left untouched: it predates this package, belongs
to whichever thread owns that file, and the check tool itself only reports
it rather than failing on it).

**Entry 10 — 2026-09-22.** Change of plan from the reviewer thread, after an
unshallowed check: the real `main`/`live` merge base is `20264dec` (PR #327,
2026-09-20) and a plain merge is textually clean in both directions —
directed doing the full reconciliation as one merge PR instead of Entry
32/33's own three-PR reconciliation-then-promote plan. Verified before
acting, not taken on faith (per this package's own standing rule, Entry 1):
the merge-base commit checked out exactly as stated; a real dry-run merge
(`git merge origin/live --no-commit --no-ff` off `main`, then aborted
cleanly) found actual conflicts the "textually clean" framing didn't
predict — reported back before proceeding rather than silently reconciling
the discrepancy either way.

**Entry 11 — 2026-09-22.** The dry-run merge's real conflicts, and how each
was handled — full detail and file list in
`Ministry/Features/Conversation-Transparency-Engine/Decision-Log.md` Entry
34, logged there since the conflicts sit in that workstream's own files.
Summary: `cic-poc/frontend` genuinely was clean (verified against the real
base, correcting this package's own prior turn's wrong claim that it needed
three-way judgment); 4 code files had real, resolvable conflicts (unioned
or the more-complete/accurate side kept, reasoned individually); 12
registry files' package pins were resolved toward `main` then all 12 worlds
rebuilt fresh rather than trusting either side's pin; 4
`Open_Gaps_Tracking.md` files were add/add and unioned (nothing dropped);
6 further add/add record conflicts, first framed to the user as needing
fleet-build-thread scholarly judgment, turned out on full-file diffing to
be false alarms (5 a completed schema migration `main` already had, 1 a
line-wrap) — that framing was this package's own error, corrected before
resolving them. One real regression (a blanket registry-pin resolution
briefly re-broke an already-fixed `hal.yaml` field) was caught by the
existing `engine/m1/tests/test_cross_world.py` drift check before this PR
opened, not after. Final state: full suite 895/895, `engine.m1.cross_world`
0 new defects, `engine.m9.cli check` clean, `tools/check_paths.py` 0 new
unresolved citations.
