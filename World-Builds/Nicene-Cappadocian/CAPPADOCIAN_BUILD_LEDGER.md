# Cappadocian Build Ledger
## Record-Native World Build Process V1.2 — recovery, audit, and gate status

**Read this first if resuming.** This world is being recovered and audited per V1.2 Appendix C item 3 ("the Cappadocian orphan"), not built fresh. Current position: **Doc_01, Doc_02, Doc_04, and Doc_06 have each been revised and independently re-checked (§7 below) — Mark asked for these four fixed, and they are, as far as three rounds of review can establish.** G2 stands unchanged. **G1 is still formally REOPENED**, awaiting Mark's actual look at the corrected scope and manifest (§5, §7) — the fixing is done; his re-confirmation is not, and nothing proceeds past it on this session's own authority. Cost envelope approved in principle but the review/rework lane ran past its original estimate (§4). One real handoff is still outstanding regardless: Mark's own download of the manifest files into `cic/texts/` (this session cannot fetch them) — hold this until the manifest is re-confirmed, since earlier versions of two rows pointed at the wrong content (both now fixed).

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
- **Pre-dates the WRS record store entirely.** The "deployment outputs" (Capsule Core, Priority Layer, chunks, Activation set) are the old CO-013 authored-artifact model, PARTIAL at best (2–3 exemplar chunks against an 18-entry story inventory and a 39-entry lexicon (corrected from an earlier miscount)). None of this is reused directly — Phase B generates equivalent artifacts from WRS records, and the chunking work already done does not carry forward as a shortcut.
- **The world was explicitly declared not freeze-eligible by its own builder** (World Profile §9/§11): Article 29 confirmation PENDING, Article 31 external review not occurred, all runtime testing OUTSTANDING. Nothing here is a green light being rediscovered — it's the same red light the original build already raised, now reaching the person who can actually clear it.
- **Depth is deliberately bounded** ("a disciplined kernel, not full production depth," Critic Finding 18): 39 lexicon entries against an estimated 80–120 for full production; 2 of 18 story-inventory entries chunked; 3 of 39 lexicon entries chunked. Whether to expand before or after Phase B conversion is a real scope call, not assumed here.

**Open questions the recovered build itself could not close (all named on the record, none resolved by this run):** the female-voice question (now G2, Option 2 above); Gravity 3's Primary-with-situational-annotation classification (Doc_04 §3/§6 — flagged for external review, same open shape as the Early Latin build's analogous call); the circle-vs-world identification risk (Critic Finding 2 — the deepest exposure, bearing directly on both G1's scope question and G2's identity question); Article 29 (now G4, unchanged in shape from every other world).

## 3. Gate status

| Gate | Status | Artifact |
|---|---|---|
| G1 — Scope & Sources | **REOPENED, 2026-08-30** — the approved scope argument and one manifest row were found materially wrong by independent review; corrected versions await Mark's actual re-confirmation, not carried over from the first approval | `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` |
| G2 — Representative identity | **DECIDED, 2026-08-30, standing** — Option 1 (Eumathios, guest-door elder); Option 2 left open, not foreclosed, not built now. Not reopened — the identity reviews didn't touch this decision's own reasoning | `cappadocian_Representative_Identity_Options.md` |
| G3 — Bar read | not reached | — |
| G4 — Article 29 | not reached (carried `provisional`, unchanged) | — |
| G5 — Admission & freeze | not reached | — |
| Cost envelope | **APPROVED in principle, 2026-08-30; the review/rework lane is now known to run past its original $15–30, see §4** | this file, §4 |

Per CO-022, this is a "finding cuts against an earlier decision" escalation, not a routine revision — the build thread is not self-dispositioning the reopened G1, even though most of the underlying fixes are mechanical. §5 below is the full finding; the manifest file carries the corrected Part A and Part B for Mark's actual re-look.

## 4. Cost envelope estimate — for Mark's one approval, before further billed work

**Confidence key**, matching this project's own convention in `CiC_LLM_Provider_Cost_Options_2026-08-09.md`: **[M]** measured/policy figure from this project's own committed documents; **[E]** estimated from comparable historical build shapes (the six fleet worlds' Phase B/C/D work); **[S]** speculative, no comparable data.

This session's own recovery + audit + web research (everything above and the two decision artifacts) has been reasoning and search-tool work, not agent/subagent API spend, and is not counted against this envelope — the envelope below is what remains, gated on Mark's decisions in §2's two open artifacts.

| Lane | What it covers | Original estimate | Revised, post-review | Basis |
|---|---|---|---|---|
| Review & currency rework | Fresh-context adversarial review of Doc_01 and Doc_02 (done — see §5); **substantial revision of both** (not "light currency check" — the reviews found 15 blocking items each); Doc_02 rework into the V7.4 Source Registry Template incorporating the corrections; Doc_04 real rework (3 of 11 gravities never tested); Doc_06 real rework (no master index exists, plus three factual corrections); light touch-ups to Doc_08/09; adding the now-required ethical/legal lens to Doc_05/07 | $15–30 | **$35–55** | [E] — three independent Opus review passes already spent (§5); this is what's left to actually fix what they found |
| Source verification sweep | Same scope as before, now informed by two review passes that already did much of this work from memory-cross-check; remaining: confirm against the real acquired texts once downloaded | $10–20 | $10–15 | [E], lower — the reviews already did the cheap part |
| Phase B — record-native conversion (B-1–B-9) | Unchanged in shape; still the largest single item, still dominated by the voice/Permanent Prompt rebuild to the register bar (the "last martyrs" opening line alone forces a rewrite regardless of the historical correction) | $25–45 | $25–45 | [E], unchanged |
| Phase C — deployment wiring | Unchanged | $2–5 | $2–5 | [E], unchanged |
| Phase D — lean validation | Unchanged | $5–10 | $5–10 | [M]/[E], unchanged |
| **Total envelope** | | **≈ $60–110** | **≈ $80–130** | |

**This is the "projected overrun, stated plainly" moment the launch prompt's cost policy requires, not silent continuation.** The overrun is entirely in one lane (review & rework) and has an identifiable cause: the original estimate assumed Doc_03–09 needed only a "light currency check," and the actual independent review found Doc_01, Doc_02, Doc_04, and Doc_06 all need real, substantive revision. The three review agents that produced this finding (§5) are themselves already-spent cost, included in the revised range, not an additional ask.

**Unchanged from the first version:** (1) claude-sonnet-5's intro pricing ends 2026-08-31 — the range already assumes post-increase rates. (2) The manifest's honest-gaps section (revised, §5) still names real citations with no open edition — that dollar decision, if Mark wants to close it with a licensed purchase, stays outside this envelope.

**What happens within the envelope once approved:** the build runs without per-call asks, per the launch prompt's cost policy. A projected overrun or exhausted allocation is a halt at the last green checkpoint, stated plainly with a revised estimate — never silent continuation.

## 5. Independent review findings (2026-08-30) — why G1 reopened

Three fresh-context Opus review agents ran after the first G1/G2 approval: one on Doc_01, one on Doc_02 (cross-checked against the approved manifest), one auditing Doc_03/04/06/08/09 against the four index-discipline skills and V7.4 currency. Full transcripts are not retained here; this is the consolidated finding.

**The headline result: the recovered build's reasoning is consistently better than its bookkeeping and its memory.** No reviewer found a fabricated source, an invented quotation from whole cloth, or a classification that looks wrong given the evidence the build presents. What they found instead is a real, recurring pattern: specific facts misremembered (both Doc_01 and Doc_02 independently gave Basil's redated death year as 378 instead of the correct 377 — two reviewers making the identical correction from different angles is a good sign about the review, not the document), scholarly positions misattributed (McGuckin assigned the opposite of his actual known view, and leaned on twice more after), sources overclaimed (a manifest row said a volume contained orations it doesn't), and a few real self-contradictions (the world refuses to equate itself with its three authors, then ends when those three authors die).

**Highest-priority findings:**
1. **The "last martyrs" self-description is very likely wrong**, and it's already the opening line of the deployed-style Permanent Prompt. Eupsychius of Caesarea was martyred under Julian in 362, inside this world's own span, with his feast attested in Basil's letters.
2. **A required Construction Framework section (World Separation Criteria) is missing from Doc_01 entirely** — this is the actual reason the c.394 ending is argued from personnel and politics rather than from any demonstrated change in formation, worship, authority, or interpretation, and it's the same root cause behind the strand-singular finding being under-argued.
3. **The world is written as both regional and confessional without choosing** — the region's own Homoian and Eunomian Christians get excluded as "external weather" or a "boundary" despite the world being framed as a regional formation ecology, not a confessional one.
4. **Doc_04 has three untested gravities** (Tensional 9/10/11) that appear only at classification, never generated as candidates or run through the six-test assessment — already propagated into Doc_08 and the World Profile as unearned confidence.
5. **Doc_06 has no master index** (the actual point of the lexicon-index discipline), a wrong entry count in its own header (38 claimed, 39 actual, propagated into three other files including this ledger's first version), and a false "reciprocity checked" claim (33 one-directional links found).
6. **The Source Acquisition Manifest itself had a real error**: one approved row claimed NPNF2 vol. 7 contains Gregory Nazianzen's Invectives against Julian — it doesn't. Caught before Mark downloaded anything. Full corrections are in the manifest file itself, including a materially expanded gap list (Basil's *Against Eunomius* has no open English translation at all, not just "not yet found") and one real structural decision (Doc_02 §4's regional-economic claims rest entirely on excluded copyrighted scholarship with no possible registry-row support — three options laid out there, Mark's call).

**What's holding up fine, worth naming so it isn't lost in the correction list:** the Author Gravity method and its "Macrina as Gregory presents her" rule; the Article 20 bounded-reconstruction principle; Doc_08's Forces Document (genuinely strong, light-touch-up only); Doc_09's Absent Stories answer; the reserve/*oikonomia* debate write-up; G2's identity reasoning (not touched by any of this — it was a methodology/judgment call, not a factual one, and stands).

**Full corrected scope and manifest:** `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md`, updated in place with `[CORRECTED 2026-08-30]` / `[NEW 2026-08-30]` markers so the diff from what Mark first approved is visible inline rather than requiring a separate diff.

## 7. The four-document fix (Mark's instruction: "fix Doc_01, Doc_02, Doc_04, and Doc_06 now") — completed, 2026-08-30

**Process, honestly stated rather than summarized as a clean pass:** Doc_04 and Doc_06 were reworked once each by Fable subagents (per the pinned model routing) and then independently verified against their own self-reports — nearly everything held, with one real defect found (a backwards claim in Doc_04 about its own interaction matrix) and fixed, plus a minor cross-document housekeeping question resolved. Doc_01 and Doc_02 took three rounds: a direct rewrite addressing the first review's 15 findings each, an independent follow-up review that confirmed most fixes held but found the rewrite itself had introduced new errors (including the closest thing to a fabricated source this build has produced — a claimed homily on Eupsychius of Caesarea that isn't actually attested, only his feast is), a second surgical fix round, and a final bounded spot-check of just that round's changes, which found one real remaining contradiction (a death date inconsistent with the document's own redating logic) and a mislabeled confidence level, both fixed.

**What this process itself demonstrates, worth being explicit about:** independent review caught real, substantive errors at every single round, including the round that was fixing errors the previous round had found. This is not a reason to distrust the current state more than an unreviewed document — it is why the review discipline exists, and each round's findings were smaller and more mechanical than the last (round 1: ~30 blocking historical/methodological errors across two documents; round 2: two new fabricated-adjacent or logic errors plus a dozen smaller ones, introduced by the act of fixing round 1; round 3: two real errors, both narrow, plus citation nits). That is convergence, not an open-ended process — but it is not the same as "verified correct," and nothing here should be read as a claim that a fourth round would find nothing.

**Known residual items, not fixed, explicitly not hidden:**
- The `.docx` mirrors of Doc_01 and Doc_02 (`cappadocian_Doc_01_World_Identification.docx`, `cappadocian_Doc_02_Source_Ecology.docx`) are two revision rounds stale — they reflect the original recovered content, not any of this session's fixes. The Build Record calls the `.md` files canonical for exactly this reason; regenerating the `.docx` mirrors mechanically (the same pandoc step the original build used) is a cheap follow-up, not done here since it's pure tooling, not content.
- A handful of very minor phrasing points the final spot-check flagged as optional (a slightly imprecise description of Hilary of Poitiers' exile timing relative to his conflict with Auxentius) were not worth a fourth edit round and are noted here rather than fixed.
- Doc_03's own pruning note doesn't record the Tier-2→Tier-3 placements Doc_06's rework surfaced (four terms); genuinely minor and deferred, since Doc_03 wasn't part of Mark's fix instruction and needs a Registry-based pass anyway once files are downloaded.

**Not done, and deliberately outside this instruction's scope:** Doc_02's actual conversion into the CF V7.4 Source Registry Template (machine-readable rows) — this still waits on the real files landing in `cic/texts/`, per the manifest's own closing sequence. The light touch-ups the original audit found for Doc_03/05/07/08/09 (the required ethical/legal lens, Material Culture promotion, Doc_09's dropped story and non-canonical tier, Doc_08's tabulation) are also not part of this fix — Mark asked for four specific documents, and those are what got the full review-and-revise treatment.

## 8. Model routing note specific to this recovery

Doc_10's existing voice-construction reasoning (Section 2's eloquence calibration, the ventriloquism risk) is genuinely good analysis and should inform the Phase B-7 rebuild rather than being discarded — but the rebuild itself is Fable's lane per the pinned routing (voice construction, Doc_10 + B-7), run against the register bar's approved sample, not against the V3.1-era RCF template alone.
