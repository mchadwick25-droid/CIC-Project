# Targeted re-check #2 (post-P0-2-resolution, Section 4 split): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus targeted re-check, dispatched 2026-08-07. Not a sixth full round — scoped to the two commits that landed after `18c4830e` and have never been reviewed: `b1fc74c6` (launch-prompt round-count update) and `b6959d04` (the Section 4 split into §4.1 "What's actually fixed" and §4.2 "Context for the open redesign"). Rounds 1–5 and the first targeted re-check read; round 5's P0-2 and Mark's resolution read in full first, per the Standard Practice's point 4. The rest of the document was deliberately not re-reviewed.*

*Verification method, per the Standard Practice's points 1 and 3: `b6959d04` diffed directly; pre-split and post-split copies extracted with `git show` and compared three ways — token-frequency delta over Section 4 only, sentence-level near-match detection (difflib, 0.72 similarity floor) of every pre-split sentence against the post-split section, and manual read of both. Every file/line citation, quoted string and count inside Section 4 checked for survival individually. All 22 external `§4` pointers enumerated and 12 of them opened and checked against what §4 now says at the cited place (the dispatch asked for six). Balance ratio and pointer count recomputed with a tokenizer first validated against the pre-split text — it reproduces round 5's **47.1 / 52.9** and **100 pointers** exactly, so the deltas below are directly comparable. Diff sized: **92 insertions, 104 deletions, all inside Section 4**; §4 goes 1,765 → 1,600 words, every other section byte-identical.*

---

## Bottom line

**The reorganization is 90% clean and the split itself is a genuine improvement — but it is not "no content changes," and one of the things it deleted is the sentence carrying Mark's own P0-2 resolution. Not ready to send.**

Three things are true at once and need to be held together:

1. **As a reorganization, it is unusually faithful.** Every file/line citation, every quoted string, every count, and every named-world claim survived intact — I checked each individually and found **zero** silent alterations. No citation drifted, no number changed, no quote was paraphrased. §4.1's four items now match §7's enumeration at line 822 and the launch prompt's at line 22 *exactly*, which closes round 5's "three different, non-matching enumerations" complaint outright. The structure is better: separating "four fixed goals" from "here's what currently exists" is the right cut, and it is the cut Mark asked for.

2. **But it is not content-neutral, and the commit message's "No content removed" is false.** Fifteen sentences were dropped rather than moved. Most are tonal or redundant. **One is not**: the sentence *"Nothing else is untouchable by default, including things this brief has elsewhere called untouchable — the fabrication-guard blocks' specific wording, the three-level sourcing apparatus's specific implementation, **the fabrication-rate check's specific mechanism**, every governance/monitoring check below"* was deleted and replaced with §4.2's *"None of it is a limit"* — which is scoped to **"Everything below"**, i.e. §4.2's own bullets. The old sentence reached the whole document by design ("elsewhere"). The new one does not. Two of the three mechanisms the old sentence named — fabrication-rate tracking, and the fabrication check §5 protects — **are not in §4.2 at all**, so nothing now overrides them.

3. **Which means the answer to the dispatch's second question is no.** §4.1's four-item list is complete *as a list*, but the document still carries absolute protections for two specific mechanisms outside those four, in §7 and §5, and §4 no longer contradicts either. The split did not move the problem into a different bucket — it deleted the sentence that was solving it. That is a straight regression against `18c4830e`, i.e. against Mark's own direct resolution.

**The pattern, stated for the next fix pass.** The prior targeted re-check named the operating rule as "deletions and re-points hold; new positive assertions don't." This commit is a *third* class, and it fails differently: **a pure reorganization is safe for facts and unsafe for scope.** Nothing factual moved wrong. What moved wrong is the *reach* of a governing sentence — the old preamble governed the document; its replacement governs a subsection. Reorganizations should be checked for what each rewritten rule still covers, not just for whether the claims underneath it survived.

`b1fc74c6` is **clean** — exactly what it claims, nothing more (verdict item 4 below).

---

## Findings

### P0-1. The split deleted the only sentence in the brief that applied Mark's P0-2 resolution to fabrication-rate tracking. §7's "not a candidate for dropping" now stands unchallenged — and self-contradicts five lines later.

Round 5's P0-2 named exactly two items as needing Mark's decision rather than an edit: **"A Turn Has a Measure"** and **fabrication-rate tracking** (Round5, lines 82 and 415). Mark resolved it: end goals fixed, form not, **no exceptions for any specific mechanism including ones this brief previously called untouchable.** `18c4830e` applied that to §4's preamble by naming the fabrication-rate check's mechanism explicitly. It did **not** touch §7.

`b6959d04` then deleted §4's naming sentence. What survives is only §7:

> **§7 Part A, lines 810–812:** *"Fabrication-rate tracking is the only real instrument for Objective 4, one of this brief's two non-negotiables — **not a candidate for dropping**."*

Five lines below it, in the same paragraph:

> **§7 Part A, lines 817–819:** *"**This license covers everything in this section, without named exceptions for specific mechanisms** — per Mark's own direct correction (2026-08-07)... See §4's single governing rule."*

These two sentences cannot both be true. Before the split, §4 broke the tie in Mark's direction. After the split it is silent, and §4.1 line 176 affirmatively asserts *"four things, no more"* — which a reader will take to mean the §7 protection is void, while §7's own words say the opposite. Fable is told at line 820 to *"See §4's single governing rule"* to resolve this, and §4's rule no longer addresses it.

Note also that the §7 sentence is *itself* now false on its own terms: it calls Objective 4 one of "this brief's two non-negotiables," but §6:597 defines the two non-negotiables as **Objectives 3 and 4 as objectives**, not as any instrument measuring them, and §6:712 (post-`18c4830e`) says of Objective 4: *"No fabrication, ever, is fixed — the goal, **not any particular mechanism teaching it** (§4)."*

**Fix.** Either (a) restore the doc-wide reach in §4 — one clause in the governing rule at lines 167–174, e.g. *"This rule governs the whole document, including anything elsewhere in this brief still worded as a protection for a specific mechanism — the fabrication-rate check's mechanism included"* — or (b) correct §7:810–812 directly to *"Fabrication-rate tracking is the only real instrument this brief has for Objective 4 — Design may replace or simplify it, but not leave Objective 4 with no instrument at all,"* which is what the resolution actually implies. (b) is better; do both if in doubt. **This is the one item on this list that reverses a decision Mark made personally.**

### P0-2. §5 tells Fable that a governance check is "completely out of scope and non-negotiable," cites §4 for it, and §4 has said the opposite since `2aa12b15`.

> **§5, lines 524–527:** *"the same pilot produced a `fabrication_adjudication` signal — **the one governance check this brief names as completely out of scope and non-negotiable (§4, Objective 4)** — on the exact turn where the prototype told the Marcella story concretely..."*

Three separate failures in one clause, verified directly:

- **`fabrication_adjudication` is not named in §4 at all** — not before the split, not after. §4's governance content names `over_settling`, `citation_grounding`, `drift_detection` (§4.2:232–267) and `confirmed_glosses` (§4.2:268–274). Grepped the whole section: zero occurrences. The pointer has never resolved.
- **§4 names *no* governance check as out of scope.** It did until `2aa12b15` ("Open the governance/monitoring layer to full scrutiny, per Mark's direct instruction"); §4.2's preamble now reads *"**None of it is a limit.** Rewrite, replace, simplify, or drop any of it."*
- **The "Objective 4" half is contradicted too.** §6:712 says Objective 4 fixes the goal, *"not any particular mechanism teaching it."*

Introduced in `e2eb7f7a` (round-1 fix pass) and untouched since — it survived rounds 2–5, the governance opening, and the P0-2 resolution. Round 5's cross-reference audit listed six non-resolving pointers (§6:703, §3:63, §8:1047, §7:929, §8:1097, §4:188); **this one is not among them.** It is a genuine miss, not a re-litigation.

It is a P0 rather than a stale-pointer P2 because of what it does in combination with P0-1: after the split, these are the **two surviving statements in the brief that protect a fabrication-checking mechanism as a mechanism**, and neither is contradicted anywhere. Fable reading §4.1's "four things, no more" and then hitting §5:527 will reasonably conclude §4.1 is incomplete.

**Fix.** Replace with *"the one governance check most directly tied to Objective 4"* and drop the `(§4, Objective 4)` pointer, or re-point to §8:1051's `fabrication_adjudication` rate bullet, which is where the brief actually discusses it.

### P1-1. §4.2's blanket "None of it is a limit — drop any of it" is applied to four process/scope notes that *are* limits, including one §7 cites §4 as authority for.

§4.2's preamble (lines 206–210) is a single license over the whole subsection:

> *"Everything below describes a mechanism currently achieving one of §4.1's four fixed goals, **or a process/scope note relevant to the rebuild**. **None of it is a limit.** Rewrite, replace, simplify, or drop any of it — provided whatever replaces it is verified to still achieve the goal it existed for."*

The commit message correctly identifies that four items in §4.2 "were never about protection at all." Then the preamble licenses dropping them anyway. The sentence names the two categories and applies one rule to both. Concretely, §4.2 now says all four of these are droppable:

- **Line 315–316:** *"§7 Part A's edit **has to preserve** 'A Turn Has a Measure' deliberately"* — the direct object of round 5's P0-2, and §8 still has no turn-length instrument to catch its loss.
- **Lines 283–292:** *"The `wrs/` record layer **must** move in lockstep with `data/`... §7's per-world passes **must** update both files in the same pass."* §7:919 cites this: *"Update the matching `wrs/records/<world>/voice_profile/` entry in the same pass, not as separate cleanup **(see §4)**."* §7 now cites as a requirement something §4.2's preamble labels non-binding.
- **Lines 281–282:** *"**Note it, don't build it**, unless the blueprint stage finds a compelling reason"* (retrieval ordering) — a scope exclusion, now licensed away.
- **Lines 319–321:** *"deliberately not bundled here — **log them** for Mark's own separate triage **rather than fixing them as part of this thread**"* — same.

None of these achieves a §4.1 goal, so the proviso ("verified to still achieve the goal it existed for") does not even constrain dropping them.

**Fix.** One sentence in the preamble: *"The mechanism notes below are open in the sense above. The process and scope notes — retrieval ordering, the `wrs/` lockstep requirement, 'A Turn Has a Measure', and the two handed-off defects — are working instructions for this thread, not protections and not optional."*

### P1-2. Mark's attributed scope line is now absent from the entire brief.

Deleted from §4's preamble by the split, and present nowhere else — grepped the full document for "voice interaction", "how a voice gets built", "voice generating", "off limits": **zero hits.**

> Deleted: *"...the same as anything else \"Representative creation and voice interaction\" touches (**Mark's own scope line: not the worlds, but everything about how a voice gets built and how a conversation unfolds**)."*

This was the brief's only statement of the **outer boundary** of what the rebuild may touch. Without it, §4.1 defines what is fixed and §4.2 says everything else is open, but nothing says what "everything else" is bounded by. It also removes Mark's attribution for the scope, which is the kind of provenance rounds 1–3 caught the assistant fabricating. The parallel quote in the launch prompt (line 22, *"yes we want fabrication guards, but how they are built and worded is open..."*) is a **different** quote and does not carry the scope definition.

**Fix.** Restore one clause to §4's governing rule (167–174) or to §4.2's preamble.

### P1-3. A grammatically incomplete sentence in §7 Part A — the mandate sentence carrying one of the §4 pointers I was asked to check.

> **§7 Part A, lines 766–769:** *"The records above are still the right thing for Design to build from; they are not yet what the live system actually runs on **— and from this brief's own principles (§1, §2, §6), and writes the *prose, register, and delivery* fresh.**"*

There is no subject for "writes" and no verb for the "from this brief's own principles" clause. `git blame` shows the break was introduced by `bf08b68f` (the round-4 targeted-re-check fix pass) — a partial replacement that left a dangling fragment. Round 5 did not flag it.

Not caused by the split, and outside its blast radius — reported only because it is the sentence immediately carrying the `(§4)` pointer at line 770 that the dispatch asked me to verify, and because the sentence it breaks is the one telling Design what Part A actually does. **Fix:** restore the missing clause (something on the order of *"Design reads them alongside each world's own sources and from this brief's own principles (§1, §2, §6), and writes the prose, register, and delivery fresh"*).

### P2-1. §7:770 quotes §4 near-verbatim for a sentence §4 no longer contains.

> **§7:769–773:** *"**This changes how something is said, never the facts being spoken** (§4) — identity, era, and vocabulary *content* stay exactly what the records attest... the same distinction **§4 already draws** for the rest of this rebuild."*

The source sentence — *"This rebuild changes how something is said and what gets reached for, never the facts being spoken"* — was deleted from §4 by the split. The **substance** survives in §4.1's fourth bullet (identity/era/vocabulary content is fixed) and in *"Prose style... is explicitly in scope (§7); their content/sourcing is not"*, so the citation is not false. But it is a bolded quotation attributed to a section that no longer says it, and *"the same distinction §4 already draws"* now points at a weaker paraphrase.

### P2-2. The governance bullet's header was reworded into a new prioritization claim, contrary to "no content changes, no new claims."

- Before: *"**The governance/monitoring layer — open to full evaluation, not a protected category.**"*
- After: *"**The governance/monitoring layer — the biggest open question here, and the one worth the most Design attention.**"*

"Open to full evaluation, not a protected category" was `2aa12b15`'s exact language, applied per Mark's direct instruction. The replacement asserts a **ranking** ("biggest," "the most") that appears nowhere else in the document and was not in the source. §4.2's preamble covers the "not protected" half, so nothing is lost — but a new editorial claim was added by a commit that says it added none. Low harm; worth naming because it is the single place in this diff where the assistant wrote a fresh assertion rather than moving one, and that is historically where this document breaks.

### P2-3. "Yes, fabrication guards — the requirement demands them" was deleted; nothing now states that the fixed goal entails having guards at all.

§4.1 says no fabrication ever is fixed. §4.2 says the guards' wording is open and anything replacing them must be verified. Neither says the goal *requires* guards to exist. The deleted sentence did, in Mark's own framing. A literal reader of §4.2's *"Rewrite, replace, simplify, or **drop** any of it"* could drop the guards entirely and claim the proviso is satisfied by verification alone. Restore the clause; it is six words.

### P2-4. The split deleted §4's most permissive sentence and replaced it with a more cautionary one — the opposite of the commit's stated purpose.

- Before: *"Whatever replaces a current mechanism has to actually still achieve the goal it existed for — verified, not assumed — **but achieving it a different, better, or cheaper way is the point of this rebuild, not a risk to guard against**."*
- After: *"...provided whatever replaces it is verified to still achieve the goal it existed for, **not just assumed to because it reads better or costs less**."*

The old sentence ended on invitation; the new one ends on suspicion of exactly the motive the rebuild exists to serve. A commit whose whole purpose was to stop §4 reading as "a page of restrictions" removed the one sentence that said cheaper-and-better *is the point*. Restore that clause to §4.2's preamble.

### P2-5. Provenance dropped from the witness-not-recruitment item.

*"Corrected directly by Mark (2026-08-07)"* and *"the same tier as no-fabrication"* were both deleted. §4.1 keeps the Foundational Documents citation (Encounter Over Persuasion, §3), which is the load-bearing half, so this is genuinely minor — but this correction was a round-4 finding and the dated attribution was how the document recorded that it had been made.

### P2-6. §2:43 says "One thing does not move"; §4.1:176 says "four things, no more."

> **§2, lines 43–46:** *"**One thing does not move, stated by Mark twice, in these exact terms: no fabrication.**... Register, structure, and entry-point can all change."*

The tension predates the split (the old §4 preamble also listed more than one), but the split sharpens it into a direct numerical clash between two bolded headline sentences 130 lines apart. **Fix:** *"One thing above all does not move..."* or point §2 at §4.1.

### P2-7. §3:63's "the two adjacent defects (§4) this brief carves out of scope" is half-stale.

§4.2's second defect (`over_settling_adjudication`'s firing rate) now says explicitly it is *"**no longer out of scope by default**"* and must be evaluated under the governance license (lines 330–337). Only defect 1 (the `key_sources` leak) is still carved out. Round 5 already listed §3:63 among its six non-supporting pointers; still unapplied. Noted for completeness, not re-litigated.

### P2-8. Three parallel copies of the four-item fixed list, all currently in agreement.

§4.1:178–191, §7:822–825, and the launch prompt line 22 each enumerate the four fixed goals independently. **They match exactly right now** — I compared them item by item, and this is a real improvement over round 5's finding of three non-matching enumerations. But round 5's fix (ii) asked for *one* canonical list cited from the other two sites, and this is three copies that can drift on the next edit. Optional.

### P2-9. The launch prompt's "the targeted re-check" (singular) goes stale the moment this file lands.

`b1fc74c6` correctly updated it to *"five full Opus adversarial rounds plus a targeted re-check."* With this file on disk there are two. **Fix:** *"plus two targeted re-checks (`..._TargetedRecheck_2026-08-07.md` and `..._TargetedRecheck2_2026-08-07.md`)."*

---

## Verdict on each dispatch item

**1. Is the reorganization actually reorganization?** **Substantially yes on facts, no on scope.**

Fact-level survival is **perfect**. Every one of these survived byte-identical, checked individually: `app/prompts/facilitator_prompts.py:224`, `:261`, `app/graph/nodes.py`, `nodes.py:1936`, `app/graph/state.py`'s `DriftSignal.signal_type`, `wrs/parameters.yaml:116-121`, FLAG-016, `Decision-Log.md:63`, `app/prompts/confirmed_glosses.py`, `app/rag/indexer.py:227`, `app/rag/retriever.py:192`, `main.py:156`, `app/prompts/table_discourse.py:75`, `representative_prompts.py:59-60`, `nodes.py:1140`, `CitationModal.tsx`, `CitationMarker.tsx`, `LexiconHighlight.tsx`, `wrs/views/probe_parity.py`. Every quoted string survived: *"one who keeps the reading of a school long since scattered"*, *"SECTION 6 — WITNESS-NOT-RECRUITMENT"*, Papnoute's *"you do not argue as an advocate arguing a case..."*, *"weighs ten signals at once"*, *"sounds like educated generic Christian voice with historical accent"*, *"museum guide"*, `REACTIVE_TURN_GUIDANCE`'s full three-clause quote, *"A Turn Has a Measure"*, *"default short: most turns are one to two short paragraphs..."*, Mark's *"we could still add some more codes to prioritize things"*, and the `key_sources` leak example. Every count survived: **Yausep's and Marius's** only; **all six**; **10 of 12**; **twenty** signal types; **roughly ten** invisible calls; **two stages**. **Zero silent alterations found.**

Scope-level: fifteen sentences dropped rather than moved. One is P0-1. Two more are P1-2 and P2-3. The rest are tonal or redundant. **"No content removed" in the commit message is not accurate and should not be relied on by the next reviewer.**

**2. Is §4.1's four-item list complete and non-contradicted?** **The list is complete; the document is not consistent with it.** Two surviving absolute protections for specific mechanisms sit outside §4.1 and the scope boundary: §7:810–812 (*"not a candidate for dropping"* — P0-1) and §5:524–527 (*"completely out of scope and non-negotiable"* — P0-2). Inside §4.2, four process instructions are mislabeled as non-limits (P1-1). The dispatch's own hypothesis — that the split may have moved the same problem into a different-looking bucket — is **half right and worse than that**: for fabrication-rate tracking it did not move the problem, it deleted the fix.

**3. Do the internal self-references still resolve?** **Twelve checked against §4's actual current text (six requested); ten resolve cleanly, two do not.**

| Site | Cites §4 for | Now resolves to | Verdict |
|---|---|---|---|
| §3:63 | two defects carved out of scope | §4.2:319–337 | **Half-stale** (P2-7, pre-existing) |
| §3:162 | `table_discourse.py` finding | §4.2:293–318 | Clean |
| §5:402 | retrieval-ordering note | §4.2:275–282 | Clean |
| **§5:527** | a governance check being non-negotiable | **nothing — §4 says the opposite** | **Broken (P0-2)** |
| §6:712 | no-fabrication goal ≠ mechanism | §4.1:178–179 | Clean |
| §6:717 | front-end scope note | §4.1:193–202 | Clean |
| §6:719 | `key_sources` leak | §4.2:322–327 | Clean |
| **§7:770** | *"how something is said, never the facts"* | **substance yes, sentence deleted** | **Weak (P2-1)** |
| §7:820 | "§4's single governing rule" | §4:167–174 | Clean |
| §7:832 | front-end UI is another workstream | §4.1:193–202 | Clean |
| §7:835 | 10-of-12-turns cost finding | §4.2:239–241 | Clean |
| §7:885 | facts given, not rebuilt | §4.1:185–191 | Clean |
| §7:888 | fabrication-guard block is open | §4.2:212–221 | Clean |
| §7:895 | witness block's current wording | §4.2:222–231 | Clean |
| §7:919 | `wrs/` same-pass requirement | §4.2:283–292 | Resolves, **but see P1-1** |
| §8:987 | twenty drift signals, not ten | §4.2:245–249 | Clean |
| §8:1003 | `probe_parity.py` cited in §4 | §4.2:285 | Clean |
| §8:1060 | `over_settling` firing count | §4.2:239–241 | Clean |
| §8:1067 | governance note | §4.2:232–267 | Clean |
| §9:1200 | the four governance mechanisms | §4.2:232–274 | Clean — all four present |
| §9:1202 | the evaluation §4 calls for | §4.2:254–262 | Clean |

**The split did not break a single otherwise-working pointer.** Both failures pre-date it: §5:527 has never resolved (since `e2eb7f7a`), and §7:770's target was deleted *by* the split but its substance survives. Renumbering §4 → §4.1/§4.2 was safe precisely because the section number was kept — good judgment in the commit.

**4. Is `b1fc74c6` exactly what it claims?** **Yes. Clean.** One file, two lines, both round-count. `four full Opus adversarial rounds` → `five`; `four-round review history` → `five-round`, `Read all four review files` → `Read all five`, and the file range corrected from `Round1... through ..._TargetedRecheck_2026-08-07.md` to `Round1... through ..._Round5_2026-08-07.md, plus ..._TargetedRecheck_2026-08-07.md`. Verified all six named audit files exist on disk with exactly those names and dates. Nothing else in the file changed. The only residue is P2-9, which this file creates.

**5. Structural check.** **Essentially the same document, reorganized.** Balance ratio **47.1 / 52.9 → 46.3 / 53.7** — 0.8 points toward the ask side, entirely from §4 shrinking 1,765 → 1,600 words. §1, §2, §3, §5, §6, §7, §8, §9 are **byte-identical**. Round 1's 68/32 failure mode remains absent for a sixth commit and the ask side has now led for three. Cross-references **100 → 103**, and the arithmetic is exactly what a clean split predicts: +2 `§4.1`, +2 `§4.2`, −1 `§4` (line 187's self-referential *"§4's defect-log note below"* correctly simplified to *"below"*). No pointer was added to or removed from any other section. This is the cleanest structural signature of any commit in this document's history.

---

## What to fix, in order

1. **§4 governing rule (167–174) or §4.2 preamble (206–210)** — restore the doc-wide reach: no mechanism anywhere in this brief is protected as a mechanism, the fabrication-rate check included. **(P0-1)**
2. **§7:810–812** — correct *"not a candidate for dropping"* to match, so the license paragraph stops contradicting itself five lines apart. **(P0-1)**
3. **§5:527** — drop or re-point *"the one governance check this brief names as completely out of scope and non-negotiable (§4, Objective 4)"*; `fabrication_adjudication` has never been named in §4 and §4 has said the opposite since `2aa12b15`. **(P0-2)**
4. **§4.2 preamble** — carve the four process/scope notes out of "None of it is a limit." **(P1-1)**
5. **§4** — restore Mark's scope line. **(P1-2)**
6. **§7:766–769** — repair the broken sentence. **(P1-3)**
7. P2s at discretion: §7:770's quote (P2-1); the governance header's new ranking claim (P2-2); *"the requirement demands them"* (P2-3); the deleted permissive clause (P2-4); the Mark/2026-08-07 attribution (P2-5); §2:43's "One thing" (P2-6); §3:63 (P2-7); the launch prompt's re-check count (P2-9).

**Is a third targeted re-check warranted after this?** Items 1–3 and 5–6 are restorations and re-points — the class that has held 100% across five fix commits. Item 4 needs one new sentence, which is the class that has produced every recent regression. **If the fix commit is confined to these, a spot-check of item 4's replacement sentence alone is proportionate. A sixth full round is not, and neither is another whole-section rewrite** — the split is structurally sound and should not be re-litigated. What it needs is four sentences put back and two corrected, not another reorganization.
