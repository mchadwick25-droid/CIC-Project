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

## "Fully implemented" (Mark's own bar) — the concrete checklist

Atlas, Interview, multi-voice Table with cards, selection function, same as the current live
worlds, on the website. Four surfaces, four real registration points — a world can be
correctly wired into three and silently missing from the fourth, which is exactly what
happened to gallic (admitted 2026-09-13, missing from the Table's own picker until
2026-09-17 — four days live and broken, caught only because Mark tried it himself). As of
2026-09-17, `python -m engine.m1.cross_world` checks all four automatically — run it, don't
eyeball the site:

| Surface | File(s) | Check |
|---|---|---|
| Atlas listing | `cic-website/data/world-census.json` `status: "Built & Live"` | `check_census_agreement` |
| Traditions page + portrait | `cic-website/traditions/<census_id>.html` | `check_site_portraits` |
| App registration (Interview) | `cic-poc/frontend/src/data/worlds.ts` `WORLD_ORDER`/`WORLD_ASSETS` | `check_app_world_assets` |
| **Table seat-picker** | `cic-website/table.html`'s own hand-maintained `WORLDS` array | `check_table_html_worlds` — **added 2026-09-17**, closing the exact gap above |

None of these four are auto-generated from the registry — each carries real hand-authored
prose (a `desc` line, a portrait alt-text, a card tile) that a template can't invent
honestly, so each stays a manual add with a check behind it, not a sync job. A clean
`cross_world` run is now a real, checkable definition of "fully implemented" — treat a world
as ready for this bar only once it reports 0 new defects, not once it looks right on one page.

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
| don (Donatism) | **fully implemented — Atlas, traditions page, Interview, Table, and selection all wired, same as the other 8 live worlds** | **CORRECTED 2026-09-17: this row was written before `table.html`'s own separate world list was discovered.** That third registration point (the Table's seat-picker, independent of the app and the traditions page) was missing don too — found only after Mark caught the identical gap live on gallic. Closed the same day: don added to `cic-website/table.html`'s `WORLDS` array, and a real fleet check (`check_table_html_worlds`) now catches this automatically for every future world, so this bar is checkable, not eyeballed, going forward. See the "Fully implemented" checklist above. — **OPEN 2026-09-16**, registry+census (as before) — but Mark's own bar for "fully implemented" (Atlas, Interview, multi-voice Table with cards, selection function, same as the current live worlds, on the website) was not yet met by the registry/census flip alone, and he caught it. Closed the real gap: the already-**approved** Fidelis portrait (locked by Mark 2026-09-10, sitting unshipped in `Ministry/Communication/Brand-Assets/Representative-Portraits/donatism/` ever since) shipped to both live-serving asset locations; don registered in `cic-poc/frontend/src/data/worlds.ts` (`WORLD_ORDER`, `WORLD_ASSETS` — accent `#6A2525`, checked for hue-distinctness against the app's other 8); `cic-website/traditions/donatism.html` built, grounded directly in don's own records (voice_craft, honest_limit, quote records — not invented copy), following the fleet's own template; a homepage card added to `index.html`'s era-2 group, inserted *ahead of* Church and Empire per this project's own documented chronological-ordering rule (311 predates 312); a stale census `why` sentence ("has not yet cleared... safety validation") corrected to match reality. **Caught and fixed a real color collision along the way**: a first website-tint pick (`#AA3C3C`) sat on the identical hue as Church and Empire's own existing card color — checked properly against the actual adjacent palette (not assumed), replaced with a distinct stone/ruin green (`#346548`/`#4C946A`, grounded in Timgad's surviving basilica ruins) applied consistently across the traditions page, homepage card, and census `entry.color`. Verified: `tsc --noEmit` clean, a real `vite build` succeeds with the portrait asset included, HTML tag-balance checked on both edited/new pages, `cross_world` 0 new defects (14 accepted-open — the three deployment-wiring waivers this pass closed are gone, not left stale), `validate-census.mjs` 0 errors, 45 tests pass. | WO-1 upload (R2 status unchecked), `main`→`live` promotion PR; **not yet done: an actual live click-through of Interview/Table mode in a browser** — the wiring is verified structurally (build succeeds, asset resolves, backend already serves don per `ADMITTED_STATES`) but not confirmed by driving the real app, since that needs the full stack running | No further Mark call needed for don's own state; promotion bundling is a separate later ask |
| lpc (Latin Pastoral-Congregational) | **ON HOLD — branch is actively live, see item 3 below** | `worlds/lpc/` on `main` (older line, through Doc_05) vs. PR #197 `lpc-doc04-round2` (newer line, old path, Doc_04-09 disposed, Representative Datus resolved). **Confirmed 2026-09-16 (Mark asked to "start the lpc reconciliation"): the branch is not stale — it picked up 3 new commits since first flagged, latest 2026-09-16T06:43:44Z, an in-progress Round 4 adversarial review (5 HIGH findings, not disposition-eligible, one finding needing Mark's own call on a Doc_04/Doc_08/Doc_09 disagreement).** Mark's explicit choice: **wait, then reconcile** — not now. | Check the branch again before starting any reconciliation | Mark's word to actually begin, once the branch looks stable |
| grkap (2nd-c. Greek Apologists, Atlas I.35) | pre-build | Step0 drafted, 5 independent joint adversarial review rounds (shared with latap — real boundary conflicts found: Tatian vs. `syr`, Justin vs. `pahc`), Mark's rulings on both incorporated (Rev. 6-7). Explicitly **"Not self-disposed. Not Approved to proceed... no build thread has been opened."** | Get Mark's explicit sign-off to open a build thread and disposition Step0, then start Doc_01 | Yes — no build thread exists yet |
| latap (Latin Apologists, Atlas I.43) | pre-build | Same shape as grkap: Step0 drafted through Rev. 6, Tertullian-merge ruling incorporated, same 5 joint review rounds. Explicitly not self-disposed, no build thread opened | Same as grkap | Yes — no build thread exists yet |

## Fleet-wide checks run this session (2026-09-16)

- `python -m engine.m2.cli staleness-check`: **all 10 built worlds (incl. don, fix) report `stale: false`** — every pinned package matches its current `records/`.
- `python -m engine.m1.cross_world`: **0 new defects**, 17 accepted-open waivers (pre-existing, not re-enumerated here), 72 informational observations. Fleet is clean.
- don's M1 gate battery carries a known, named, pre-existing `reciprocity` finding (52 one-directional `associated-with` links) — confirmed unchanged since the 2026-09-14 ordinary-believer merge, not a new defect, not blocking admission by this project's own precedent (pahc/gallic admitted with equivalent-class findings disclosed rather than blocking).

## Open items surfaced, not resolved here

1. **pahc M3 re-admission** — flagged since 2026-09-09 (`records/WORLDS_REGISTRY_LOG.md`), still not run. Real AWS Bedrock spend; needs Mark's explicit per-run authorization.
2. **don is OPEN and census-synced (2026-09-16).** M3 ran clean (28/28); admitted, then flipped open, both on Mark's explicit word; census synced the same pass (`engine.m6.cli sync` — a module that turned out to already exist, contradicting this doc's own earlier note that it didn't). don is now genuinely live on the public Atlas/homepage. Remaining: WO-1 object-storage upload (R2 configuration status still unchecked) and bundling into a `main`→`live` promotion PR — neither attempted, both separate asks.
3. **lpc has two diverged build lines, and the newer one is still an active, moving target — do not touch yet.** `worlds/lpc/` on `main` is the *older* line (through Doc_05, not self-disposed). PR #197 (`lpc-doc04-round2`) is the *newer* line, at the old path `World-Builds/Latin-Pastoral-Congregational-Christianity/`. Root cause of the divergence: the repo-structure-cleanup rename (`main` commit `9b1ee5f5`, 2026-09-15 21:35:32Z) renamed the old-path *lagging* snapshot to `worlds/lpc/` and never merged this branch's later commits.

   **2026-09-16, Mark asked to start reconciliation — checked the branch first, found it had moved again.** Since first flagged (tip `f076ba0b`, 2026-09-16T03:32:51Z), three more commits landed, tip now `0eff399c`, 2026-09-16T06:43:44Z: an in-progress Round 4 adversarial review of the World Profile document across three dimensions, verdict **SUBSTANTIAL REVISION REQUIRED, 5 HIGH / 6 MEDIUM / 6 LOW / 1 COSMETIC — not disposition-eligible**. One HIGH is a fabricated-quotation defect (a build thread's own bolded conclusion misattributed to Mark as a direct quote, now corrected). One finding is explicitly named as not a build thread's to close: **Doc_04, Doc_08, and Doc_09 — three separately Approved-to-proceed documents — disagree on how many distinct mechanisms cross lpc's 133-year documentary gap** (Doc_04's World Profile now says two; Doc_08 and Doc_09 both still say only one). Filed under CO-022's fourth escalation category (unresolved tension between cleared documents) and reserved for Mark.

   `ListAgents` shows no other session reachable from this machine, so whatever is pushing to that branch is running elsewhere (very plausibly Mark's own separate, long-running lpc build thread, matching the launch prompt's own description of it). **Mark's explicit decision: wait, then reconcile — not now.** Check the branch's tip again before starting; do not assume `0eff399c` is final either.
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

**don is OPEN and live on the public Atlas/census — 2026-09-16.** M3 ran clean (28/28), Mark
admitted it, then flipped it open; census synced the same pass. Fleet is now 9 live worlds.

Two of the remaining three non-admitted worlds still only need Mark's word to move, not more
build work — **pahc** (re-run M3 given real content added since last admission) and
**grkap/latap** (explicit go-ahead to open a build thread, since Step0 is genuinely done and
reviewed). **lpc is confirmed on hold, by Mark's own explicit choice (item 3)** — the
reconciliation was asked for, then paused once the branch turned out to still be actively
receiving commits (an in-progress Round 4 review, not yet clean). Re-check the branch before
raising this again; don't assume it's ready just because time has passed.

Next candidates, in order of readiness: (1) **pahc's M3 re-run** authorization; (2)
**grkap/latap** go-ahead; (3) whether to check R2 configuration and run don's **WO-1 upload**,
and whether to bundle don into a **`main`→`live`** promotion PR now or hold for other worlds to
land first; (4) checking back on **lpc's branch** when Mark wants to revisit it. None of these
block each other.
