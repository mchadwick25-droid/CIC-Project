# Go-Live Pipeline Coordinator — standing status — opened 2026-09-16

Running per-world status table for the Go-Live Pipeline Coordinator thread
(`Ministry/Operations/Standing/Launch-Prompts/CiC_GoLive_Pipeline_Coordinator_Thread_Launch_2026-09-16.md`,
still open as PR [#243](https://github.com/mchadwick25-droid/CIC-Project/pull/243) as of this
entry — read from the PR since it hasn't merged yet). Update this table every time a world
moves a stage, per that launch prompt's own instruction, so state survives a context reset.

**Pipeline stages, in order:** build-complete -> M9 gates -> M2 compile -> M3 admission
(Mark's call) -> registry `built`->`admitted` (Mark's call) -> WO-1 object-storage upload ->
Atlas/census sync -> registry `admitted`->`open` (Mark's call) -> merge world PR(s) to `main`
(Mark's call) -> promotion PR `main`->`live` (Mark's call) -> post-deploy verification.

## Per-world status, as of 2026-09-16

| World | Stage | Status | Next action | Needs Mark first? |
|---|---|---|---|---|
| alx | admitted | Live, package current | none pending | — |
| cappadocian | admitted | Live, package current | none pending | — |
| desert | admitted | Live, package current | none pending | — |
| gallic | admitted | Live, package current (re-admitted 2026-09-14 after Salvian expansion) | none pending | — |
| hal | admitted | Live, package current | none pending | — |
| ijc | admitted | Live, package current | none pending | — |
| pahc | admitted | Live, package current | M3 re-run flagged-not-run since the G05 supplemental-source recompile (2026-09-09) added real content | Yes — M3 re-admission is Mark's own authorized spend |
| syr | admitted | Live, package current | none pending | — |
| don (Donatism) | built | No build work left; merge-reconciliation and ordinary-believer coverage both merged to `main` (PR #190, PR #194) | Present M3 admission battery for Mark's read | Yes — admission read is Mark's own touchpoint |
| lpc (Latin Pastoral-Congregational) | **CORRECTED, see item 3 below** | `worlds/lpc/` on `main` shows only Doc_01-05 (Doc_05 Round 2, not self-disposed) — but a second, far more advanced build line exists on open PR #197 (`lpc-doc04-round2`, old path `World-Builds/Latin-Pastoral-Congregational-Christianity/`), last commit 2026-09-16T03:32:51Z: Doc_04 disposed, Doc_05-09 disposed, Representative (Datus) resolved, Article 29 Living Tradition confirmed, Article 3 gapped-formation ruling adopted. The repo-structure-cleanup rename (`main` commit `9b1ee5f5`) moved the *old, lagging* copy to `worlds/lpc/` and never merged this branch — the two lines diverged at the path level, not just in content. | **Do not touch either line until Mark decides how to reconcile them** — real risk of losing the more-advanced line's work, or colliding with a still-recent session | Yes — portfolio-level/unresolved-tension, plus real collision risk if another thread is still active on that branch |
| grkap (2nd-c. Greek Apologists, Atlas I.35) | pre-build | Step0 drafted, 5 independent joint adversarial review rounds (shared with latap — real boundary conflicts found: Tatian vs. `syr`, Justin vs. `pahc`), Mark's rulings on both incorporated (Rev. 6-7). Explicitly **"Not self-disposed. Not Approved to proceed... no build thread has been opened."** | Get Mark's explicit sign-off to open a build thread and disposition Step0, then start Doc_01 | Yes — no build thread exists yet |
| latap (Latin Apologists, Atlas I.43) | pre-build | Same shape as grkap: Step0 drafted through Rev. 6, Tertullian-merge ruling incorporated, same 5 joint review rounds. Explicitly not self-disposed, no build thread opened | Same as grkap | Yes — no build thread exists yet |

## Fleet-wide checks run this session (2026-09-16)

- `python -m engine.m2.cli staleness-check`: **all 10 built worlds (incl. don, fix) report `stale: false`** — every pinned package matches its current `records/`.
- `python -m engine.m1.cross_world`: **0 new defects**, 17 accepted-open waivers (pre-existing, not re-enumerated here), 72 informational observations. Fleet is clean.
- don's M1 gate battery carries a known, named, pre-existing `reciprocity` finding (52 one-directional `associated-with` links) — confirmed unchanged since the 2026-09-14 ordinary-believer merge, not a new defect, not blocking admission by this project's own precedent (pahc/gallic admitted with equivalent-class findings disclosed rather than blocking).

## Open items surfaced, not resolved here

1. **pahc M3 re-admission** — flagged since 2026-09-09 (`records/WORLDS_REGISTRY_LOG.md`), still not run. Real AWS Bedrock spend; needs Mark's explicit per-run authorization.
2. **don M3 admission** — never run against this world's current, fully-merged content. This is the only real gate between don and `admitted`.
3. **lpc has two diverged build lines — the most significant open item in this report, corrected after initial investigation.** `worlds/lpc/` on `main` is the *older* line (through Doc_05, not self-disposed). PR #197 (`lpc-doc04-round2`) is the *newer* line, at the old path `World-Builds/Latin-Pastoral-Congregational-Christianity/`, with commits through 2026-09-16T03:32:51Z showing Doc_04 disposed, Doc_05-09 disposed, Representative Datus resolved, Article 29 confirmed, Article 3 gapped-formation ruling adopted — none of which exists on `main`. Root cause: the repo-structure-cleanup rename (`main` commit `9b1ee5f5`, 2026-09-15 21:35:32Z) renamed the old-path *lagging* snapshot to `worlds/lpc/` and never merged this branch's later commits, so PR #197 now shows `mergeable_state: dirty` against a path that no longer exists on its base. **This needs Mark's decision on how to reconcile** (port the branch's later commits onto `worlds/lpc/`, most likely) before any further lpc work — self-reconciling risks silently discarding the more-advanced line's real disposition/review work, and there may still be a recent or active session on that branch worth checking before anything touches it.
4. **lpc PR #230** ("gapped-formation-worlds-precedent") — open, doc-only, mergeable clean, standing cross-world advisory precedent for gapped-formation-type worlds. Not blocking anything; Mark's to merge or not. Note: item 3's newer lpc line has *already adopted* this same Article 3 gapped-formation ruling internally (commit `b20688de`) — this PR may itself be superseded content once item 3 is reconciled, not something to evaluate independently of it.
5. **grkap/latap** — both are real, thorough Step0 work but neither has a disposed Step0 nor an opened build thread. Starting either is a fresh "open a build thread" decision, not a continuation.
6. **Portfolio-level item inherited from lpc's own log:** the Constitution/Forces-Framework "Boundary Structures" vs. "Boundary Ecology" internal self-inconsistency (each governing doc contradicts itself, not just each other) — ruled on the term for lpc (`Boundary Structures` canonical) but the governing texts' own self-contradictions and three sibling worlds' (alx, don, cappadocian) Doc_05 files using the other term are flagged, not fixed. Doc-hygiene on content that isn't this thread's own — per CLAUDE.md's default, flagged not touched.
7. **grkap/latap Review-Artifacts** — the five `Step0_RoundN_Review.md` files are byte-identical between the two world folders. Checked directly: this is correct, not corruption — one joint review document ("Apologist Pair") filed in both locations because the two candidates share real boundary questions (Tatian, Justin). Noted here only so a future reader doesn't re-flag it as a defect.

## Recommendation

**Lead item: lpc's two diverged build lines (open item 3) need Mark's decision before anything
else touches lpc.** If the newer line (PR #197) is confirmed sound, lpc may already be at or
near build-complete — Doc_09 disposed, Representative resolved, Article 29 confirmed — which
would make it the closest world to done in the entire fleet, not the furthest behind as first
reported. That correction changes the shape of this whole recommendation, so it's surfaced
first rather than folded in.

Independent of that: three of the other three non-admitted worlds only need Mark's word to
move, not more build work — **don** (present the M3 admission battery), **pahc** (re-run M3
given real content added since last admission), and **grkap/latap** (explicit go-ahead to open
a build thread, since Step0 is genuinely done and reviewed).

Recommend Mark's word on two things in parallel, since neither blocks the other: (1) how to
reconcile lpc's two lines, and (2) starting **don's admission read** in the meantime — it's
fully built, fully merged, confirmed non-stale, has no open divergence question, and presenting
that battery costs nothing to prepare. The grkap/latap go-ahead is similarly cheap to grant now
if Mark wants a third track running.
