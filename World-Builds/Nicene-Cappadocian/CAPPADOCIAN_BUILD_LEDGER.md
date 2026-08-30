# Cappadocian Build Ledger
## Record-Native World Build Process V1.2 — recovery, audit, and gate status

**Read this first if resuming.** This world is being recovered and audited per V1.2 Appendix C item 3 ("the Cappadocian orphan"), not built fresh. Current position: **G1 and G2 both decided (Mark, 2026-08-30); cost envelope approved; build proceeding under CO-022 autonomy on the review/rework lane.** One real handoff is still outstanding and blocks Phase B's B-1: Mark's own download of the approved manifest files into `cic/texts/` (this session cannot fetch them — see the G1 file's closing note).

---

## 1. Recovery (2026-08-30)

`origin/CiC-Fable-Cappadocian` shares **no git history with `main`** (disjoint commit graphs — confirmed via `git merge-base`, which returns nothing; the branch's own root commit does not exist on `main`). A normal merge is not meaningful here. Recovery was done as a targeted checkout of the world's own folder:

```
git checkout origin/CiC-Fable-Cappadocian -- World-Builds/Nicene-Cappadocian
```

This pulled in the complete, self-contained world folder (~41 files: Doc_01–Doc_09, World Profile, Doc_10 Construction Notes + Permanent Prompt, two Critic checkpoints, Build Record, Final Report, Deployment Package Status, partial deployment chunks, DOCX mirrors). Nothing else from that branch (its separate, older copies of the Construction Framework, Blueprint, and templates) was pulled in — this build stays on `main`'s current V7.4/V3.2/V1.2 governance, not the V7.3/V3.1 the orphan branch carried.

## 2. What was found (full detail in the recovered documents themselves)

Built as a **single unattended Fable run**, forked from `CiC-Fable-Experiment`, under CF **V7.3** and RCF **V3.1** (both one governing revision behind current). Sequence run: Doc_01 → Doc_02 → Doc_03/04 → Doc_05 → Doc_06 → Doc_07 → Doc_08 → Critic Checkpoint 1 → Doc_09 → World Profile → Doc_10 (Representative "Eumathios") → deployment core outputs → Critic Checkpoint 2 → status/report docs. This is **structurally the most complete orphaned Phase A in the project** — genuinely argued (not asserted) gravity classification, an honest and unusually severe self-critique, alternatives weighed on the record at the identity decision, zero fabricated sources detected on the build's own re-read.

**What it is not:** verified, tested, or record-native.
- **Every citation is unverified** — "genuine and identifiable... none is checked" is the build's own standing caveat, repeated in every document (Critic Finding 1, restated at Finding 19). This is the single largest carried risk and the reason G1 leads with sources, not scope.
- **Zero live testing** of any kind — the Permanent Prompt has had zero blind rounds; validation is entirely OUTSTANDING (Doc_10 Construction Notes §7).
- **Pre-dates the register bar and transparency-ground birth conditions (V1.1/V1.2, 2026-08-30)** by definition — the Permanent Prompt is described by its own Critic Checkpoint 2 as "still a lyrical document," ~11% over its token target, with named trim candidates never applied. It has not been read against `CiC_Register_Bar_2026-08-29.md` and should be assumed to need real rework, not a light pass, before Phase B's B-7.
- **Pre-dates the WRS record store entirely.** The "deployment outputs" (Capsule Core, Priority Layer, chunks, Activation set) are the old CO-013 authored-artifact model, PARTIAL at best (2–3 exemplar chunks against an 18-entry story inventory and a 38-entry lexicon). None of this is reused directly — Phase B generates equivalent artifacts from WRS records, and the chunking work already done does not carry forward as a shortcut.
- **The world was explicitly declared not freeze-eligible by its own builder** (World Profile §9/§11): Article 29 confirmation PENDING, Article 31 external review not occurred, all runtime testing OUTSTANDING. Nothing here is a green light being rediscovered — it's the same red light the original build already raised, now reaching the person who can actually clear it.
- **Depth is deliberately bounded** ("a disciplined kernel, not full production depth," Critic Finding 18): 38 lexicon entries against an estimated 80–120 for full production; 2 of 18 story-inventory entries chunked; 3 of 38 lexicon entries chunked. Whether to expand before or after Phase B conversion is a real scope call, not assumed here.

**Open questions the recovered build itself could not close (all named on the record, none resolved by this run):** the female-voice question (now G2, Option 2 above); Gravity 3's Primary-with-situational-annotation classification (Doc_04 §3/§6 — flagged for external review, same open shape as the Early Latin build's analogous call); the circle-vs-world identification risk (Critic Finding 2 — the deepest exposure, bearing directly on both G1's scope question and G2's identity question); Article 29 (now G4, unchanged in shape from every other world).

## 3. Gate status

| Gate | Status | Artifact |
|---|---|---|
| G1 — Scope & Sources | **DECIDED, 2026-08-30** — scope confirmed, manifest approved; file download from Mark still outstanding (blocks Phase B B-1 only) | `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` |
| G2 — Representative identity | **DECIDED, 2026-08-30** — Option 1 (Eumathios, guest-door elder); Option 2 left open, not foreclosed, not built now | `cappadocian_Representative_Identity_Options.md` |
| G3 — Bar read | not reached | — |
| G4 — Article 29 | not reached (carried `provisional`, unchanged) | — |
| G5 — Admission & freeze | not reached | — |
| Cost envelope | **APPROVED, 2026-08-30, ≈$60–110** | this file, §4 |

Per CO-022, both decisions are now settled and the build proceeds autonomously within the approved envelope: independent review of Doc_01/Doc_02, Doc_02's structural rework into the V7.4 Source Registry Template, currency checks of Doc_03–09, and Doc_10 rework toward Eumathios/guest-door-elder under the register bar. **Not started yet, and blocked on Mark specifically:** Phase B's B-1 (source rows), which needs the actual files in `cic/texts/`.

## 4. Cost envelope estimate — for Mark's one approval, before further billed work

**Confidence key**, matching this project's own convention in `CiC_LLM_Provider_Cost_Options_2026-08-09.md`: **[M]** measured/policy figure from this project's own committed documents; **[E]** estimated from comparable historical build shapes (the six fleet worlds' Phase B/C/D work); **[S]** speculative, no comparable data.

This session's own recovery + audit + web research (everything above and the two decision artifacts) has been reasoning and search-tool work, not agent/subagent API spend, and is not counted against this envelope — the envelope below is what remains, gated on Mark's decisions in §2's two open artifacts.

| Lane | What it covers | Estimate | Basis |
|---|---|---|---|
| Review & currency rework | Fresh-context adversarial review of Doc_01 and Doc_02 (the existing Critic checkpoints are same-session/simulated and don't satisfy independent review); Doc_02 rework into the V7.4 Source Registry Template; light currency check of Doc_03–09/World Profile against V7.4 + the four index-discipline skills (lexicon/gravity/forces/story) | **$15–30** | [E] |
| Source verification sweep | Independent check of the structurally load-bearing named-detail claims Critic Finding 1/19 lists (the 381 communion-law bishops, Eunomius' birthplace, the Forty-of-Sebaste family shrine, the Asketikon locus, Gangra's canon content, the famine date, the 372 provincial division) against the acquired texts once Mark downloads them | **$10–20** | [E] |
| Phase B — record-native conversion (B-1–B-9) | Mechanical scripts (cheap) + Fable component calls for lexicon/story/gravity/forces authoring and — the largest single item — a real voice/Permanent Prompt rebuild to the register bar and transparency-ground birth conditions, since the existing prompt was never read against either | **$25–45** | [E], the widest range here — depends on how much Doc_10 survives a register-bar read intact |
| Phase C — deployment wiring | Manifest entry, frontend union, indices, Dockerfile audit, ceiling/guard wiring, live smoke test — mostly mechanical | **$2–5** | [E] |
| Phase D — lean validation | Free floor (gates/schema/parities) + ~10–14 single-trial blind-graded probes (cents each) + one extended live Deep Interview | **$5–10** | [M] for the Deep Interview shape and per-probe cost (policy doc, `2026-08-01_M_lean_validation_interview_spend.md`); [E] for the probe count actually needed here |
| **Total envelope** | | **≈ $60–110** | |

**Two things this figure does not include, both flagged rather than buried:** (1) claude-sonnet-5's intro pricing ends 2026-08-31 (tomorrow, from this session's date) — costs measured under it are already optimistic by ~50% for anything run after; the range above assumes post-increase rates throughout, which is why it reads higher than the fleet's earlier per-world figures. (2) The "honest gaps" section of the Source Acquisition Manifest names real citations (the anti-slaveholding homily chief among them) with no verified open edition found this session — if Mark chooses to close that gap with a licensed purchase rather than accept the scope reduction, that is a real dollar decision outside this envelope, made explicitly, not folded in.

**What happens within the envelope once approved:** the build runs without per-call asks, per the launch prompt's cost policy. A projected overrun or exhausted allocation is a halt at the last green checkpoint, stated plainly with a revised estimate — never silent continuation.

## 5. Model routing note specific to this recovery

Doc_10's existing voice-construction reasoning (Section 2's eloquence calibration, the ventriloquism risk) is genuinely good analysis and should inform the Phase B-7 rebuild rather than being discarded — but the rebuild itself is Fable's lane per the pinned routing (voice construction, Doc_10 + B-7), run against the register bar's approved sample, not against the V3.1-era RCF template alone.
