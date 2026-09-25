# Round 2 targeted recheck: `aec` (Antiochene Exegetical Christianity, Chrysostom-centered), Step 0, Doc_01, Doc_02 + Source Registry

Per the `cic-build-cycle` skill, round 2 onward is a targeted recheck of the prior (Round 1) findings and the diff since, not a full re-review from scratch. Run by an independent Opus subagent (agent id `a626448370c664cca`, 2026-09-25) against the Round 1-revised documents. Every finding below was independently re-verified by the build thread against the vendored primary texts during fix application, not merely applied on the reviewer's word — per this project's own "a review finding is never dismissed... without independent re-verification" discipline, applied here in the affirmative direction as well: a finding is not treated as fixed until the fix itself is independently re-checked against source.

**What held up from Round 1:** all Round 1 HIGH findings' core corrections (the World #8/`lpc` premise, the Theodoret condemnation disclosure, the invented family detail) remained sound on recheck. The issues below are Round 1's own fixes propagating incompletely, one further overclaim introduced while fixing Round 1's H2, and a handful of items Round 1 did not reach.

---

## Step 0: SUBSTANTIAL REVISION REQUIRED

**H1 (HIGH), §3.** The Round 1 fix itself overstated `lpc` Doc_04's own review history — "cleared after nine independent review rounds." Verified directly against `worlds/lpc/Doc_04_Gravity_Discovery.md`: it went **eleven** rounds, and **never cleared**; every round returned SUBSTANTIAL REVISION REQUIRED or REVISION REQUIRED. It was disposed "Approved to proceed" on the project lead's own direct instruction, with open findings explicitly inherited by any document that draws on it. Fix: correct the round count and clearance claim throughout, and have this document's own argument say plainly that it inherits `lpc` Doc_04's own open findings rather than treating the four Primary/one Supporting classification as settled.

**M1 (MEDIUM), §3.** Candidate 4 ("Preaching and Catechesis as Primary Formation Mode") was called "a fifth candidate" and cited at "§5" — it is Candidate 4, in `lpc` Doc_04's own §4. Fix: correct the numbering throughout.

**M2 (MEDIUM), §3.** The B3 argument does not engage the Meletian schism material Doc_01 itself adds in this same revision cycle — a real complication (this world does have a collegial-communion-under-schism episode, contrary to B3's original "no comparable thread" framing) that should be named and tested, not omitted. Fix: engage it directly as a hypothesis for Doc_04, not a settled distinction.

**L1 (LOW), §3.** "Passes B3" is stated more flatly than the hypothesis framing the rest of the paragraph actually supports. Fix: soften to match.

---

## Doc_01: SUBSTANTIAL REVISION REQUIRED

**M1 (MEDIUM), §2 (Ending point).** Still carries the withdrawn "closed to avoid the Nestorian controversy" framing that Step 0 §2 itself already corrected. Fix: propagate the corrected account.

**M2 (MEDIUM), §2 (Cultural Environment).** "Libanius's own former fellow-students" has the direction backwards — Socrates VI.3 names Theodore and Maximus as Chrysostom's own fellow-students under Libanius, not the reverse. Fix: correct the direction.

**M3 (MEDIUM), §2 (Historical Pressures, the Meletian schism).** Two problems: (a) the schism is described as "already running when this world's own window opens (350)," but Meletius was not elected until 360 and the rival Paulinus not consecrated until 362 — the schism began a decade after the window opens, not before it; (b) an unsourced "resolved 415" date is asserted with no citation. Fix: correct the start date, remove the unsourced resolution date, and give the Flavian alternative (from `npnf109`'s own prolegomena) its own direct citation rather than "some later accounts."

**M4 (MEDIUM), §3.** The "Lenten preaching sequence" description of the Statues homilies, already withdrawn in Step 0 §3 B2, was not propagated here. Fix: match Step 0's corrected wording.

**M5 (MEDIUM), §6.** The "deliberately kept outside" framing for material shared with World #6 is stale after other corrections this revision. Fix: reword to match the corrected account.

**M6 (MEDIUM), §1.** Describes `lpc` as "nine-round-reviewed" — imprecise and, for Doc_04 specifically, wrong (eleven rounds, never cleared; see Step 0 H1 above). Fix: use accurate wording or drop the round-count claim.

**H1 (HIGH), §4.** The Theodoret per-work boundary section mixes two different tests without naming either as the rule: composition date for the *Eranistes* and Letters, but the span of events narrated for the *Ecclesiastical History*. A boundary test has to be one consistent criterion, not a different one per work chosen to fit the desired conclusion for each. Separately, this section's own closing paragraph ("Doc_02 should apply this finding directly...") contradicts §7's open-items list, which sends the same strand/inclusion question to Doc_04 for resolution — the document cannot both close the question and defer it. Fix: apply one criterion (subject matter, per the Source Registry Template's own Boundary Check definition) to all four works consistently, and resolve the §4/§7 contradiction by stating plainly whether the question is closed here or deferred.

---

## Doc_02 + Source Registry: SUBSTANTIAL REVISION REQUIRED

**M1 (MEDIUM), §3, §7, Registry.** Doc_02 says the core characterization now rests on "the ancient self-description (Socrates VI.3) … Documented." That is wrong on two counts: Socrates describes Diodore, not Chrysostom — Doc_01 itself says Chrysostom's own link to Diodore is Widely Accepted but not independently verified against a primary text naming him. And the "literal and historical meaning in preference to the allegorical … Origen and the Alexandrians" wording is the 19th-century NPNF endnote, not Socrates' own words. Socrates' own actual line, about Diodore, reads: "he limited his attention to the literal sense of scripture, avoiding that which was mystical" (`npnf202`, `ii.ix.iv-p6`, independently re-verified against the vendored XML this round). Fix: describe it accurately, as an ancient description of Diodore's own method, not a Chrysostom self-description.

**M2 (MEDIUM), §8.** Holdings triage remains incomplete: Codex Theodosianus (×2) and Boyd remain unassessed tier-2 files, left inside a generic "not individually assessed" catch-all rather than named specifically. More significantly, `palladius_lausiac-history_clarke1918.txt` — a different, already-vendored Palladius work, distinct from the still-wanted *Dialogue Concerning the Life of Chrysostom* — was missed entirely from the prior triage. It holds a full chapter on Olympias (Chapter LVI) and, in a separate chapter (Chapter XLI, "Holy Women," independently re-verified this round — not Chapter LVI as an earlier characterization of this finding had it), a clause naming "the deaconess Sabaniana, aunt of John the bishop of Constantinople." Directly relevant to §6's own gender/Olympias analysis. Fix: name the file, add it to holdings disposition, and draw on the Olympias/Sabaniana material in §6.

**L1 (LOW), §2.** The magister militum quote is truncated — drops "of Syria" and closes on a period the source does not have; the source's own sentence continues ("...in the imperial army of Syria, and died during the infancy of John..."). Fix: quote in full, with a proper ellipsis if truncating.

**L2 (LOW), §6.** "Theodoret adds a second voice only provisionally" is stale after Doc_01 §4's per-work finding (his material is now Native/context-like, a live condemned-content edge case, or out-of-boundary, per work — not a uniform provisional second voice). Fix: reword to match.

---

## Disposition

All findings above addressed in this revision, marked inline in each affected document; see each document's own §8/§10 Disposition section for the corresponding revision-history entry. Per the cic-build-cycle skill's 3-round cap, this was Round 2 of at most 3 substantial-revision rounds. A Round 3 targeted recheck is the final round available before this must be treated as an unresolved tension requiring escalation rather than a fourth review round.
