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
(that workstream's own Entry 28) naming the divergence inventory and the
promotion PR set now in front of Mark, per the launch brief's own
instruction to hand this to both Mark and that workstream. No file inside
that workstream's own directory was edited beyond that one append.
