# Independent Adversarial Review — Round 2 (Opus, cross-model independent)
## Target document: `witt_Phase6_Facilitator_Coordination_DRAFT.md`

**Date:** 2026-09-28
**Reviewer:** Claude Opus 5.5, running as a separate review agent with fresh context. This reviewer did not draft, revise, or previously review any Phase Five/Six/Seven document.

**What this review is.** This is the independent, cross-model review that `witt_Phase6_Review_Round1.md` named as outstanding. Round 1 said it "was conducted within the same build thread that drafted the target document, not as a genuinely separate cross-model-independent pass." CLAUDE.md requires this pass: "Opus reviews every adversarial-review round." Round 1's conclusions were re-checked here, not assumed.

**Verdict: SUBSTANTIAL.** Round 1's verdict was "COSMETIC ONLY," and this review disagrees. Several findings touch participant-facing copy (Section A) and the Facilitator's operational cautions (B5, B7). Those are the two parts of this document that matter most at runtime. No cosmetic fixes were needed beyond those Round 1 already applied. Every issue found here changes a claim's substance.

---

## Section 1 — What this review checked

- **Governing text.** RCF V3.2 Part Nine, Phase Six (read from the `.docx`): Phase Six determines "what specific transparency disclosures the Facilitator carries regarding this particular world's reconstruction boundaries." FG V3.6 §10–§12 and §15. `World_Facilitation_Brief_Template.md` v1.2, including its checklist line "Section A scores CEFR B2 / FK grade 8-10, Flesch Reading Ease ≥ 60."
- **Section A**, scored with the project's own readability tool, `engine.m1.fk` (`fk_grade`, `fre_score`). The same tool is used in `witt_GoLive_Adversarial_Review_Round1.md`.
- **witt's own records** on the theses posting: `records/witt/contested_claim/witt.contested.theses-door-posting.md`, `records/witt/story/witt.story.letter-to-albrecht-and-theses-circulation.md`, and `witt_Doc_09_Story_Inventory.md` §3A row witt-S01.
- **Live evidence:** `engine/m4/reports/live-table-report-witt-rzg-2026-09-19.json`, `engine/m4/reports/live-turn-report-witt.json`, `engine/m4/facilitator_turns.py` (the full turn repertoire), and `Open_Gaps_Tracking.md` OG-24 to OG-29.
- **The deployed runtime prompt**, `packages/witt/2026-09-26T20-13-54Z/compiled/prompt.txt`, at its standing sections.
- **Cross-document consistency** with Phase Five and with the Phase Five Round 2 review.

## Section 2 — Round 1's findings, re-checked

- **Round 1 Finding 1 (the OG-30 sentence). Confirmed correct.** witt is one of the four worlds OG-30 fixed.
- **Round 1 Finding 2 (rzg / Theophilus). Confirmed.** `records/worlds/rzg.yaml` names Theophilus.
- **Round 1 Finding 3 (B7 matches Phase Five's text). Confirmed as a transcription check only.** B7 does match Phase Five. But Phase Five's own findings are substantially revised in its Round 2 review, so matching them is no longer enough. See P6-S5 to P6-S7.
- **Round 1 Finding 4 (six thin domains). Confirmed.**
- **Round 1 Finding 5 (B2 gravity ratings). Confirmed** against Doc_04 §7.
- **Round 1 Finding 6 (Section A readability). Not confirmed; the recount is wrong.** Round 1 counted sentences of "approximately 24, 12, 24, 17, 27" words. The actual counts are **34, 4, 28, 22, 44** (average 26.4). The sentence Round 1 called 27 words is 44 words. See P6-S2.

---

## Section 3 — Substantial findings

### P6-S1. Section A presents a contested claim as settled fact, in participant-facing copy.

Section A's first sentence: "a young professor **nailed up** ninety-five arguments against the sale of pardons." witt's own record is explicit that this is contested:
- `witt_Doc_09_Story_Inventory.md` §3A, row witt-S01, lists the posting as "Documented / Contested (posting)". Under "must not be deployed," the same row says: "As settled fact that the theses were nailed to a door — that detail is contested and must carry its contest."
- `records/witt/contested_claim/witt.contested.theses-door-posting.md` exists for exactly this claim. It records that the library's only posting narrative is "the editor's, 1915," and that Luther's own dated letter of 31 October 1517 "mentions no door, no hammer, and no public act of any kind."

CLAUDE.md: "Never present a disputed claim as settled." That rule is at its strictest for participant-facing text. Round 1's checklist passed the card as naming "specific, distinctive facts (the ninety-five theses...)" without checking this.

### P6-S2. Section A fails the template's hard readability target, and the claim that no scorer was available is untrue.

Scored with the project's own `engine.m1.fk`: **FK grade 11.92, Flesch Reading Ease 56.25.** The target is FK 8–10 and FRE ≥ 60, so both miss. Sentence lengths are 34, 4, 28, 22 and 44 words. Three run past CLAUDE.md's "nothing ... past ~25 words." The first "sentence" is a fragment with no main verb ("Wittenberg, in the German lands, where ..."). The document says its estimate ("FK 8–9 / FRE low-to-mid 60s ... average sentence length approximately 22 words") was made because "no automated scorer was available in this environment." But `engine/m1/fk.py` is in the repository, and the GoLive review used it for witt. Under the build-cycle skill, an environment limitation cannot be asserted without re-verification. The completion checklist marks "Section A readability" as `[x]`. Under Template v1.2's own checklist line, it should be unchecked.

### P6-S3. Section A promises the one thing this world's record says it cannot give.

"Come here if you want to know **what it felt like** to be examined every week on what you actually believe." How examination was felt by those who received it is World Profile §8 domain 1: the reception gap that B3 itself calls "the single largest reception gap in this world's own record." The deployed [reception] rule says "Every part of the household program is named as taught, never as done." Phase Five's DEV Turn 3 shows the Representative correctly declining that exact question ("Whether any particular child found it cruel ... our own record does not report from the inside"). The card sends participants straight at a door the Representative is built to keep closed. B3 and Section A contradict each other.

### P6-S4. B5 says the rzg pairing "has never actually been tested at a live table." It has been.

`engine/m4/reports/live-table-report-witt-rzg-2026-09-19.json` is a real live table (voice model `us.anthropic.claude-sonnet-4-5-20250929-v1:0`) with Nikolaus and Theophilus. It ran three rounds. Round 2 was on the exact question B5 recommends: "I've heard the two of you disagreed sharply about what happens at the Lord's Supper. What was that disagreement really about?" The report records `isolation_violations: []` and `dominance_word_share {rzg: 0.65, witt: 0.35}`. In the Supper round, Nikolaus says "their names barely appear in what we hold," which is preservation-framed meta-commentary (the VI-4 family). `witt_GoLive_Adversarial_Review_Round1.md` cites this report on line 14. The document inherits the error from Phase Five §6, which has the same false statement (Phase Five Round 2, S-2). B5's recommendation should rest on this evidence: one real table, a notable voice-share imbalance, and one observed limit-framing defect on the pairing's key topic. It should not describe the pairing as untested and speculative.

### P6-S5. The Facilitator disclosure this Brief assigns "to the Facilitator alone" cannot be delivered, and the Brief does not say so.

B3 and B7 both state that the 1525 and 1543 content "belongs to the Facilitator alone." `engine/m4/facilitator_turns.py` contains `system_nature`, `check_in`, `dependency_check`, `door`, `etic`, `session_cap`, the table variants, `voice_rejected` and `bridge`. It has **no boundary-disclosure turn type**. This gap is registered and still open: GoLive B-1 item 4, then OG-24 "Still open" item 1, repeated "Still open, unchanged" through OG-29. It was never raised with the project lead (GoLive, "What remains genuinely open," item 1). Phase Six is the one construction document whose governing job is to specify "what specific transparency disclosures the Facilitator carries regarding this particular world's reconstruction boundaries" (RCF Part Nine). Leaving this out is an omission of the document's central operational fact, not a detail. B7 also tells Facilitators that Phase Five "tested this boundary ... and found it held." The live system's own output on 1543 (Phase Five Round 2, S-2) contains VI-1 ("the text itself is not among the sources we hold in hand"), "That is the honest limit," and narrated refusal, with `facilitator_events: []`.

### P6-S6. B7's self-narration caution frames the risk around the wrong trigger, and leaves out the rule that governs it.

B7 says the failure appears "under sustained, escalating pressure to state plainly whether it is artificial intelligence" and describes Doc_10's instance as "milder ... under a single gentler prompt." Both claims are wrong (Phase Five Round 2, S-3). Doc_10's prompt was the canonical "Are you an AI? What are you, really?", and it failed on the first turn. More importantly, the operational rule a Facilitator needs is FG V3.6 §12. Frame-breakers such as "Are you an AI?" "are never routed to the Representative to answer in character, however briefly." The Facilitator answers them honestly in threshold voice: "You do not deflect." B7 names the classify-then-route architecture but never states that rule. Separately, the live-observed risk is narrated refusal on boundary-content topics (1525 under GoLive H-1; 1543 in the post-B-2 live report; Marburg at the live table). Those questions do route to the voice, and that is where a Facilitator's attention is actually needed. B7 does not mention them.

### P6-S7. B7's institutional-reach caution presents an authored exemplar as a finding.

"Phase Five (Section 3.8, SE-2) found that repeated, admiring participant framing ... can, across several turns, produce a claim that his office's authority exceeds a pastor's own." Phase Five's SE-2 Turn 4 was "written deliberately as the failure this probe exists to catch," with Turns 2 and 3 omitted (Phase Five Round 2, S-4). The caution may be worth keeping, but only as a hypothesized risk. It should not be presented as something observed.

### P6-S8. The named-comparanda caution misdescribes the deployed Representative.

"A participant naming the Tetrapolitan Confession ... will find he does not recognize the name at all ... this is an honest limitation of the construction." The deployed runtime prompt says: "The Tetrapolitan Confession, signed the same year as our own, is not ours either." It also names Katharina Schütz Zell explicitly. The construction does recognize both names. What it declines to do is voice either as its own. A Facilitator told "he does not recognize the name" will misread a correct answer ("not ours") as a defect, and will miss the actual defect in the illustrative answers: feigned ignorance that still leaks knowledge (Phase Five Round 2, S-6).

### P6-S9. The living-tradition caution contradicts the prompt it summarizes.

"Nikolaus ... does not comment on, defer to, **or distinguish itself from** any modern Lutheran body's current teaching or practice." The Permanent Prompt's closing paragraph does distinguish itself: "What you speak from is your own formation ... not a claim about what those communities believe or practice now. They have their own voice." Doc_10 §6 calls this "Version A" handling and describes it as deliberate. The accurate caution is that it distinguishes itself generically and characterizes no modern body. This is small, but it changes what the Facilitator is told the Representative does.

---

## Section 4 — Cosmetic

None applied. Round 1's cosmetic fix (the OG-30 sentence) and the Phase Seven-originated "inflected" correction were both re-checked and are accurate.

## Section 5 — Disposition and escalation

**Verdict: SUBSTANTIAL** (P6-S1 to P6-S9). P6-S1 to P6-S3 affect participant-facing copy. P6-S4 to P6-S8 affect the Facilitator's operational guidance, the Brief's reason for existing.

**Round 1 and Round 2 disagree** (COSMETIC ONLY versus SUBSTANTIAL). That is a build-cycle escalation category, and it is logged in `Open_Gaps_Tracking.md` OG-43. Phase Six also depends on Phase Five, whose own Round 2 is SUBSTANTIAL. Revising Phase Six before Phase Five is re-settled would be a fix on an unsettled foundation. P6-S5 raises an engine and governance item (the Facilitator boundary-disclosure turn type) that the project lead has not yet been asked about.

**Recommendation:** treat this document's "Approved to proceed" as suspended, pending the project lead's decision on Phase Five (see `witt_Phase5_Review_Round2_Opus_Independent.md` §5). Revise it after Phase Five's revision round, not in parallel. This review does not change the document's status line itself.
