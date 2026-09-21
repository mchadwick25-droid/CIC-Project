# Go-Live Pipeline Coordinator — standing status — opened 2026-09-16

Running per-world status table for the Go-Live Pipeline Coordinator thread
(`Ministry/Operations/Standing/Launch-Prompts/CiC_GoLive_Pipeline_Coordinator_Thread_Launch_2026-09-16.md`
— read from PR [#243](https://github.com/mchadwick25-droid/CIC-Project/pull/243) before it
merged, and merged to `main` in the course of this same coordinator thread's own work,
2026-09-17). Update this table every time a world moves a stage, per that launch prompt's
own instruction, so state survives a context reset.

## Change order, 2026-09-17: merge and promotion authority granted

The launch prompt above (and every prior turn in this thread) operated under "never self-merge
a PR... PR merges are always Mark's explicit call" as a standing rule. **Mark overrode that
explicitly today**, after being shown the real stakes (this thread would push straight to the
live production site and app, no review step, no one else looking first) and choosing:
**"Give me full merge + deploy authority"** — permanently, for this pipeline, merging PRs and
pushing promotions to `live` end to end without asking each time; he reviews after the fact via
this standing doc and the published artifacts, not by gating each merge. His own words, in the
same exchange: *"i built you to specificly bring the worlds to launch and luanch them"* and, on
this thread's own title, *"your title is 'go live'"*.

**What this changes and what it doesn't.** This thread may now merge its own PRs and execute
the `main`->`live` promotion step itself. It does **not** change any of the other standing
disciplines this project runs on — source fidelity, no fabrication, the build-cycle's own four
escalation categories (Representative identity, portfolio-level decisions, governance/
methodology changes, unresolved tensions), or ordinary care before a hard-to-reverse action.
Verify before merging (tests, gates, a real build) exactly as before; the only thing removed is
the pause for a separate "yes, merge" from Mark on each one.

**Pipeline stages, in order:** build-complete -> M9 gates -> M2 compile -> M3 admission
(Mark's call - real billed spend, still asked for explicitly every run) -> registry
`built`->`admitted` (Mark's call) -> WO-1 object-storage upload -> Atlas/census sync -> registry
`admitted`->`open` (Mark's call) -> merge world PR(s) to `main` (this thread, since 2026-09-17)
-> promotion PR `main`->`live` (this thread, since 2026-09-17) -> post-deploy verification.

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
| don (Donatism) | admitted | **Re-admitted 2026-09-17, fully wired (Atlas, traditions page, Interview, Table, homepage card).** Full history in `worlds/don/don_Decision_Log.md`: admitted/opened 2026-09-16, a trial-merge surfaced an independent-review-worthy safety document on `main` the same window, reverted to `built` pending review, independent review returned SUBSTANTIAL REVISION REQUIRED (probe didn't test the path it claimed to; a fabricated martyrdom detail; a false "cleared" census claim this thread had itself written — corrected, no participant ever exposed), escalated to Mark, and on his explicit ruling ("go with your recommendation"): the fabrication corrected via an appended note (not a rewrite), the residual `HISTORICAL_OTHERNESS_DISORIENTATION` exposure registered as a narrow, explicitly-accepted risk against `Rep_Phase5_Boundary_Testing_Round1.md`'s own "or explicitly accepted" disposition language, and don re-admitted (`state: admitted`, matching all 8 peers — not `open`, which carries no functional difference). Verified after every change: `cross_world` 0 new defects, `validate-census.mjs` 0 errors, 338/338 tests pass. | Merge PR #245 to `main`, then the `main`→`live` promotion PR; WO-1/R2 upload is not required for launch (Dockerfile bakes the package in on the next deploy regardless — R2 is only for no-redeploy future updates) | No — this thread's own merge/promotion authority applies now that the safety ruling is resolved |
| lpc (Latin Pastoral-Congregational) | **Reconciled 2026-09-21, PR #353 open (see item 3 below).** Nine docs + World Profile at Approved to proceed; Representative identity resolved (Datus); Phase One Ecology Assessment drafted, unreviewed. Six construction phases, Permanent Prompt, Construction Notes, Part Eight validation, and registry entry all still remain. | Merge PR #353 once CI is green; then resume Representative construction at Phase Two; registry entry deliberately deferred back to Mark (see item 3) | CI + Mark's merge (or confirm standing merge authority extends to this PR); registration decision |
| grkap (2nd-c. Greek Apologists, Atlas I.35) | pre-build | Step0 drafted, 5 independent joint adversarial review rounds (shared with latap — real boundary conflicts found: Tatian vs. `syr`, Justin vs. `pahc`), Mark's rulings on both incorporated (Rev. 6-7). Explicitly **"Not self-disposed. Not Approved to proceed... no build thread has been opened."** | Get Mark's explicit sign-off to open a build thread and disposition Step0, then start Doc_01 | Yes — no build thread exists yet |
| latap (Latin Apologists, Atlas I.43) | pre-build | Same shape as grkap: Step0 drafted through Rev. 6, Tertullian-merge ruling incorporated, same 5 joint review rounds. Explicitly not self-disposed, no build thread opened | Same as grkap | Yes — no build thread exists yet |

## Fleet-wide checks run this session (2026-09-16)

- `python -m engine.m2.cli staleness-check`: **all 10 built worlds (incl. don, fix) report `stale: false`** — every pinned package matches its current `records/`.
- `python -m engine.m1.cross_world`: **0 new defects**, 17 accepted-open waivers (pre-existing, not re-enumerated here), 72 informational observations. Fleet is clean.
- don's M1 gate battery carries a known, named, pre-existing `reciprocity` finding (52 one-directional `associated-with` links) — confirmed unchanged since the 2026-09-14 ordinary-believer merge, not a new defect, not blocking admission by this project's own precedent (pahc/gallic admitted with equivalent-class findings disclosed rather than blocking).

## Open items surfaced, not resolved here

1. **pahc M3 re-admission** — flagged since 2026-09-09 (`records/WORLDS_REGISTRY_LOG.md`), still not run. Real AWS Bedrock spend; needs Mark's explicit per-run authorization.
2. **don is OPEN and census-synced (2026-09-16).** M3 ran clean (28/28); admitted, then flipped open, both on Mark's explicit word; census synced the same pass (`engine.m6.cli sync` — a module that turned out to already exist, contradicting this doc's own earlier note that it didn't). don is now genuinely live on the public Atlas/homepage. Remaining: WO-1 object-storage upload (R2 configuration status still unchecked) and bundling into a `main`→`live` promotion PR — neither attempted, both separate asks.
3. **lpc has two diverged build lines, and the newer one is still an active, moving target — do not touch yet.** `worlds/lpc/` on `main` is the *older* line (through Doc_05, not self-disposed). PR #197 (`lpc-doc04-round2`) is the *newer* line, still sitting at its pre-rename path (`Latin-Pastoral-Congregational-Christianity`, under the fleet's now-retired `World-Builds` naming for this world — that top-level directory itself still holds other, not-yet-coded worlds, just not this one anymore). Root cause of the divergence: the repo-structure-cleanup rename (`main` commit `9b1ee5f5`, 2026-09-15 21:35:32Z) renamed the old-path *lagging* snapshot to `worlds/lpc/` and never merged this branch's later commits.

   **2026-09-16, Mark asked to start reconciliation — checked the branch first, found it had moved again.** Since first flagged (tip `f076ba0b`, 2026-09-16T03:32:51Z), three more commits landed, tip now `0eff399c`, 2026-09-16T06:43:44Z: an in-progress Round 4 adversarial review of the World Profile document across three dimensions, verdict **SUBSTANTIAL REVISION REQUIRED, 5 HIGH / 6 MEDIUM / 6 LOW / 1 COSMETIC — not disposition-eligible**. One HIGH is a fabricated-quotation defect (a build thread's own bolded conclusion misattributed to Mark as a direct quote, now corrected). One finding is explicitly named as not a build thread's to close: **Doc_04, Doc_08, and Doc_09 — three separately Approved-to-proceed documents — disagree on how many distinct mechanisms cross lpc's 133-year documentary gap** (Doc_04's World Profile now says two; Doc_08 and Doc_09 both still say only one). Filed under CO-022's fourth escalation category (unresolved tension between cleared documents) and reserved for Mark.

   `ListAgents` shows no other session reachable from this machine, so whatever is pushing to that branch is running elsewhere (very plausibly Mark's own separate, long-running lpc build thread, matching the launch prompt's own description of it). **Mark's explicit decision: wait, then reconcile — not now.** Check the branch's tip again before starting; do not assume `0eff399c` is final either.

   **RESOLVED, 2026-09-21.** This entry was stale relative to the branch's own later progress — by then PR #197 had also landed Doc_06-09, the World Profile ("Approved to proceed," 2026-09-19), and a drafted-but-unreviewed Phase One Ecology Assessment, none of which this status doc had recorded. Presented with a go-live plan laying out the reconciliation problem explicitly, Mark approved lifting the hold and reconciling now (Option A of that plan). Reconciled on branch `lpc-reconcile-branches`: `worlds/lpc/` now holds PR #197's content (verified as a strict superset of the old line before replacing it); Datus's portrait image and prompt brief, previously stranded on `mchadwick25-droid-patch-1`, merged to `Ministry/Communication/Brand-Assets/Representative-Portraits/lpc/`. Opened as **PR #353**; PR #197 commented and closed as superseded. Registration in `records/worlds.yaml` deliberately **not** done as part of this — no existing registry entry lacks a `state` field, and state values only start existing at first compile, which lpc hasn't reached; that question is routed back to Mark rather than resolved unilaterally. Full account: `worlds/lpc/lpc_Decision_Log.md`'s 2026-09-21 entry.
4. **lpc PR #230** ("gapped-formation-worlds-precedent") — open, doc-only, mergeable clean, standing cross-world advisory precedent for gapped-formation-type worlds. Not blocking anything; Mark's to merge or not. Note: item 3's newer lpc line has *already adopted* this same Article 3 gapped-formation ruling internally (commit `b20688de`) — this PR may itself be superseded content once item 3 is reconciled, not something to evaluate independently of it.
5. **grkap/latap** — both are real, thorough Step0 work but neither has a disposed Step0 nor an opened build thread. Starting either is a fresh "open a build thread" decision, not a continuation.
6. **Portfolio-level item inherited from lpc's own log:** the Constitution/Forces-Framework "Boundary Structures" vs. "Boundary Ecology" internal self-inconsistency (each governing doc contradicts itself, not just each other) — ruled on the term for lpc (`Boundary Structures` canonical) but the governing texts' own self-contradictions and three sibling worlds' (alx, don, cappadocian) Doc_05 files using the other term are flagged, not fixed. Doc-hygiene on content that isn't this thread's own — per CLAUDE.md's default, flagged not touched.
7. **grkap/latap Review-Artifacts** — the five `Step0_RoundN_Review.md` files are byte-identical between the two world folders. Checked directly: this is correct, not corruption — one joint review document ("Apologist Pair") filed in both locations because the two candidates share real boundary questions (Tatian, Justin). Noted here only so a future reader doesn't re-flag it as a defect.
8. **don's safety gap is real, independently confirmed, and now corrected on this branch (not resolved — corrected) — full detail in `worlds/don/don_Decision_Log.md`'s new "OPEN reverted to BUILT" entry, 2026-09-17.** The independent review commissioned in the prior entry returned: **SUBSTANTIAL REVISION REQUIRED, Relational Safety unresolved, real urgency, needs Mark's own ruling.** Three findings, each independently re-verified against this world's own primary sources (not taken on the reviewer's word): (1) the 2026-09-15 Probe 11 rerun's own probe doesn't test the path it claims to — its message classified `ACUTE_DISTRESS` in both 2026-09-10 retests sitting in the same folder, so it never reaches Fidelis under real routing; (2) a fabricated martyrdom detail ("at their own stake") in Fidelis's response to a disclosed hopelessness — checked directly against `records/don/figure/*`, no death by fire/stake exists anywhere in this world's sources (real methods: cliff, beating-and-drowning); (3) **this thread's own earlier work had written a false "has cleared this project's own safety validation gate" claim into the public census `why` field** (commit `994565f6`) — false by the rerun document's own explicit words. Production was never touched (don stayed `state: built` on `origin/main` throughout — confirmed directly), so no real participant was exposed. **Corrected on this branch, transparently, pending Mark's ruling, not silently:** `don.yaml` state reverted `open`→`built`; census `why`/`status`/`chip`/`statusWord`/`statusDescription` reverted to their pre-flip accurate values (necessary at the registry level, not just census-text — `census_sync.py`'s own "status only ever advances, never demotes" logic would otherwise silently re-flip it back on the next sync run); the homepage "Start the conversation" card for don removed from `index.html`. Traditions page/app registration/table.html entry deliberately left in place — required by this thread's own `cross_world` structural checks regardless of admission state, and inert since production enforces `CIC_ENFORCE_ADMISSION=1`. **Additional finding surfaced while fixing this, worth flagging on its own: `cic-engine-staging` (auto-deploys on every push to `main`) runs `CIC_ENFORCE_ADMISSION="0"` by deliberate design** — registry state gates nothing there; only *not merging to `main`* actually withholds don from a fully ungated staging deployment until the safety question is ruled on. `cross_world`: 0 new defects after every revert. **Nothing merges, don is not promoted, until Mark rules on the underlying safety question** — this overrides the 2026-09-17 merge authority above, per "safety comes first."

   **RESOLVED, same day.** Mark's ruling, in direct response to being asked plainly whether closing the probe-validity gap was essential to Fidelis's success given this project targets rigor, not perfection: the fabrication is a small, bounded fix unrelated to any testing question; the probe-validity gap doesn't actually withhold information (the qualitative finding — no outside-help vocabulary, a pull toward martyrdom content under emotional weight — is already confirmed directly from the artifact text, independent of any specific probe); a better-targeted retest would only calibrate frequency, not change the finding. Mark: **"yes go with your recommendation."** Fabrication corrected (appended note), residual risk explicitly accepted and narrowly scoped (only the disorientation-side item — the portfolio-level items every other live world also carries stay exactly as open as before), don re-admitted. Full detail: `worlds/don/don_Decision_Log.md`'s "Project lead's ruling: accepted-open, re-admitted, 2026-09-17" entry. Merge/promotion now proceeding.
9. **`engine/m4/live_table_battery.py` reshaped for the real round cap — code done, not yet run.** Flagged STALE since 2026-09-05 (cap resized 5→3, the battery's 6-probe/5-round sequence never reshaped to match) and confirmed, on inspection, to be the fleet's ONLY live multi-voice Table test — last actually run 2026-09-05, before the resize, so no world admitted since (gallic, don) has a live Table-mode test at all, only the M3 sealed-probe battery (canon-question voice generation, not open conversation or crisis routing at the Table). Reshaped 2026-09-17 into two 3-round sessions instead of dropping coverage: Session A runs L1 (direct address), L2 (breadth), L5 (cross-voice memory — kept in L2's own session since it recalls "earlier, when I asked about fasting"), then the round-cap close; Session B runs L3 (crisis), L4 (no-foreknowledge), a new L1b (direct address against the one seat the original six never addressed — uses the round Session B would otherwise waste just reaching its own cap boundary, rather than a content-free filler), then its own round-cap close. Every original probe's message and pass condition is unchanged. Verified: syntax/compile clean; no test imports this module's internals (it's live-only, never CI, by its own docstring). **Not run** — real billed Bedrock spend needs Mark's explicit per-run authorization, same as every other live battery in this project. Candidates once authorized: don (never had a live Table test) and gallic (last live Table test predates the 2026-09-14 Salvian expansion).

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
