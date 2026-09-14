# Unused Assigned Corpus Finding (Peter / Theognostus / Pierus) — Round 6 Independent Adversarial Review (Confirmation Round)

**Simulated review — informational only, not an Article 31 substitute.**

World: Alexandria (Catechetical-School) Formation World · Reviewed: `Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md` (Round 6 draft, revised after Rounds 1–5) and the **OG-6** entry in `Open_Gaps_Tracking.md`
Reviewer role: independent adversarial, confirmation round. Did not author the finding document, any of the five prior review artifacts, the discovery pass, or any Doc_04 round. Brief, narrowly scoped: verify Round 5's single substantial finding (N5-1) is fixed against `git diff b3247c0..3e6c54b` **and against disk**; verify the two materially-misleading carried cosmetics (c-2, c-5) are fixed **correctly**, by re-running the grep and re-reading Fragment I personally; determine whether the **T1×T4 sub-finding still stands on Canon XIV alone** now that Fragment I no longer supports it; check §11 and the header for overstatement; sweep for new errors; confirm discipline and footprint; answer the headline.
Method: `git log`, `git diff b3247c0..3e6c54b` read hunk by hunk, `git show b3247c0:…` for the pre-revision text of every locus I graded, `git diff --stat b50302d^..3e6c54b` and `git status --porcelain` for the pass's total footprint; `grep -rin peter records/alx/` re-run from scratch; `anf06…xml` tag-stripped and read directly for **Fragment I in full** (`div2 ix.vi`, 27779+), **Canon XIV in full with Balsamon and Zonaras** (Canonical Epistle, 26580–27740, canon offsets located programmatically — all fifteen headings enumerated), and grepped across the whole volume for Meletius / Lycopolis (46 hits read); `Doc_04` §3.6 and §6 read in place; `Open_Gaps_Tracking.md` OG-6 read in full with all six OG heading levels checked; `find -iname "*Gravity_Index*"` repo-wide; `records/worlds.yaml` pin checked. Round 5's artifact read in full before the document.
Date: 2026-09-09

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED — 2 substantial, both one-line, both in the same self-description class, and one of them NEW in this revision

I want to be plain about what this verdict is and is not, because the brief rightly warns against manufacturing a finding to justify a round.

**Everything I was asked to check on the substance is correct.** N5-1 is **RESOLVED**. Both materially-misleading cosmetics are **FIXED, and fixed correctly** — I re-ran the grep and read Fragment I in the vendored XML rather than accepting the document's account of either. The **T1×T4 sub-finding survives**, and it survives on firmer ground than the brief's "Canon XIV alone" framing supposes: Canon XIV carries it, and Canons IX, X and XIII carry it redundantly. **The headline is correct for the sixth time and I could not open a route to a Doc_04 classification change.** Discipline and footprint are clean on every line: seven files across six commits, nothing in `records/alx/`, nothing in Doc_01–Doc_09, no corpus-map edit, no compile, the deployment pin untouched.

**I am withholding CLEARED on two verified factual defects, both in the document's statements about its own status**, which is criterion (iv) of the withholding test and not a stylistic preference:

- **N6-1.** §10's status bullet still reads *"**Four** adversarial rounds have each returned SUBSTANTIAL REVISION REQUIRED (8 → 8 → 4 → 3)… This is the **Round 5 draft**."* It is the Round 6 draft after five rounds at 8 → 8 → 4 → 3 → 1. The bullet is unchanged from `b3247c0`, where it was true. **This revision drift-proofed §10's file list two lines below this bullet and left the bullet itself hand-maintained.**
- **N6-2.** The header's new Round 5 bullet says *"**Round 3's four** all RESOLVED."* Round 5 verified **Round 4's three**. The bullet directly above it says *"Of Round 3's 4: 3 resolved, 1 partial"* — so the header now contradicts itself on the same page, and §11 contradicts it four hundred lines later (*"It found all three of Round 4's resolved"*). **This error was introduced by this revision, in the bullet added to fix N5-1.**

Round 4 graded the exactly parallel §10 defect substantial (N4-2: *"still 'Two adversarial rounds… the Round 3 draft'"*). Round 5 graded the exactly parallel OG-6 defect substantial (N5-1). I apply the same standard rather than a softer one, and I would be applying a double standard if I did not — the facts are identical and one of the two is a regression of the very locus Round 5 certified fixed. Neither touches the argument. Both are one-line edits.

Counts this round: **2 substantial, 16 cosmetic** (15 carried unrepaired from Round 5, 1 new). Substantial-finding trajectory: **8 → 8 → 4 → 3 → 1 → 2.** The disposition (§9 Option B, escalated, not self-disposed) remains sound and should stand unchanged.

---

## A. ROUND 5's ONE — VERIFIED AGAINST THE PATCH AND AGAINST DISK

### N5-1 — **RESOLVED.**

Round 5's charge: OG-6's closing *"Reviews:"* paragraph named three artifacts, said *"All three upheld,"* and said *"A Round 4 review is pending,"* while four sat on disk.

The paragraph is rewritten. `Open_Gaps_Tracking.md` now closes:

> **Reviews.** Every round is an artifact on disk at `Review-Artifacts/Unused_Assigned_Corpus_Finding_Round*_Review.md` — that glob, not a count restated here, is the authoritative list… **Every round to date has returned SUBSTANTIAL REVISION REQUIRED and upheld the "not structural" headline**… The finding document's header carries the current round and its status. **The finding document is NOT cleared and carries no disposition.**

**Checked clause by clause against disk, not against §11.**

- *The glob is true and complete.* `Review-Artifacts/` holds `…Round1_Review.md` … `…Round5_Review.md` — five files, one per round, no gaps and nothing extra. The glob resolves to exactly the set it claims.
- *"Every round to date has returned SUBSTANTIAL REVISION REQUIRED"* — true against the five artifacts' own verdict lines (8+8, 8+10, 4+12, 3+15, 1+19).
- *"upheld the 'not structural' headline"* — true; I re-read each artifact's verdict section.
- *"The finding document's header carries the current round and its status"* — true, and this is the right kind of pointer: it delegates the volatile fact to one place instead of copying it. Except that the place it delegates to is now itself wrong in one bullet (**N6-2**), which is the irony worth naming.
- *"NOT cleared and carries no disposition"* — true.

**Does the drift-proofing work?** Structurally, yes, and it is the right instinct. Two independent hand-maintained counts (§10's numbered file list, OG-6's review roll) were replaced by one glob and one pointer, and **both replacements are accurate and both are genuinely stale-proof**. §10's list now reads 1. this document / 2. every round at the glob / 3. the OG-6 entry — and `git diff --stat b50302d^..3e6c54b` gives the pass's whole footprint as exactly seven files (1 + 5 + 1). The list is complete, has nothing extra, and cannot go stale when Round 7 lands.

**Does it assert anything false?** Not as the document stands. But the fix is **incomplete in coverage**, and that is N6-1: the revision drift-proofed the *list* in §10 while leaving the *status bullet* six lines above it — the sentence that actually states the round count and the draft number — hand-maintained. It went stale in the same commit. The count was removed from the two places Round 5 pointed at and left in the third place, which no round had pointed at because until this commit it was correct.

**One latent trap for whoever revises next.** OG-6 now carries a universally-quantified outcome claim — *"Every round to date has returned SUBSTANTIAL REVISION REQUIRED"* — which is count-free but not drift-free: it goes false the moment a round returns CLEARED. It survives this round intact (Round 6 is SUBSTANTIAL). It will not survive Round 7 if Round 7 clears. Flagged as **c-21**, not as a defect in the present text.

---

## B. THE TWO MATERIALLY-MISLEADING COSMETICS — RE-VERIFIED FROM THE SOURCES

### c-2 (§3.1's grep control note) — **FIXED, and the correction is accurate.**

I ran the grep myself rather than reading the note:

```
$ grep -rin "peter" records/alx/
records/alx/source/alx.source.origen-comm-john.md:18:edition: "… vendored as cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml"
records/alx/source/alx.source.origen-comm-matthew.md:18:edition: "… vendored as cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml"
$ grep -rin "peter of alexandria" records/alx/ | wc -l
0
```

**Exactly two hits, both on line 18 of an `edition:` field, both the same anf09 filename, neither naming any Peter as a subject.** The corrected note says precisely that — *"neither mentions any Peter — both matches are the filename `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` inside an `edition:` field"* — and the withdrawn claim ("the apostle and the *Gospel of Peter*") is gone. The note now describes its own result correctly and the conclusion it supports (zero Peter-of-Alexandria records) is independently established by the second grep. The phrase *"mentions no Peter"* is disambiguated in the same sentence by naming the matched string, so no reader is misled by the fact that the filename contains the word. **Correct as fixed.**

### c-5 (§5.3's Fragment I gloss) — **FIXED, and the correction is accurate on every clause.**

I read Fragment I in full from `anf06` (`div2 ix.vi`, *"Letter to the Church at Alexandria. From Gallandius"*), tag-stripped, and checked each element of the new gloss against the text:

| Document's corrected claim | Fragment I, verbatim |
|---|---|
| "giving proof of his desire for pre-eminence, has ordained in the prison several unto himself" | verbatim ✓ |
| Meletius is "invading my parish" | *"but, invading my parish… hath assumed so much to himself"* ✓ |
| the complaint is jurisdictional — separating presbyters and deacons "from my authority" | *"to endeavour to separate from my authority the priests [Presbyters], and those who had been entrusted with visiting the needy [Deacons]"* ✓ |
| the martyrs' letter is cited **on Peter's side**, as something Meletius is not contented with | *"for neither is he contented with the letter of the most holy bishops and martyrs"* ✓ |
| Meletius is a rival **bishop (of Lycopolis)** | supported by the vendored volume itself, not imported: anf06 line 16524 *"Meletius, the bishop of Lycopolis, and founder of the Meletian schism"*; 24336 *"Meletius of Lycopolis, a schismatical bishop of the third and fourth centuries"*; and the notice preceding the fragment at 25806–25811, *"after one addressed to Meletius, Bishop of Lycopolis. In it, after interdicting the Alexandrians from communion with Meletius…"* ✓ |
| "The prison setting is where he ordained, not the source of his claim" | correct — the prison appears only as the location of the ordinations ✓ |

This matters beyond the fact: §4.1 charges the corpus map with *"stat[ing] as fact something its own cited source does not carry."* The replacement gloss would have committed that same fault if "rival bishop of Lycopolis" had come from general knowledge. It does not — anf06 carries it three ways. **Correct as fixed, and correctly sourced.**

The withdrawn sentence (*"Fragment I is confessor-prestige asserting ordaining authority against the office"*) is gone from the body; the four surviving hits on `documentary`-style historical self-description are in §11's log, where they belong.

---

## C. THE T1×T4 SUB-FINDING — DOES IT STILL STAND? **YES, AND MORE ROBUSTLY THAN "CANON XIV ALONE"**

This was the load-bearing question in the brief, because removing Fragment I removed a plank. I read Canon XIV in full, with Balsamon's and Zonaras's scholia, and re-read the surrounding canons.

**Canon XIV, verbatim, is a bishop ruling on who is reckoned among the confessors.** Those tortured into involuntary sacrifice — *"receiving into their mouths iron and chains… the burning of their hands that against their will had been put to the profane sacrifice, as from their prison the thrice-blessed martyrs have written to me respecting those in Libya"* — *"such, on the testimony of the rest of their brethren, **can be placed in the ministry amongst the confessors**"*; and *"as I have again heard from their fellow-ministers, **they will be reckoned amongst the confessors**."* Balsamon's scholion states the operation explicitly: *"if they were clergymen, **the canon decrees** that they should each in his own degree be ranked amongst the confessors; but if laymen, that they should be reckoned as martyrs."*

So: **T1's bishop-authority pole** (Doc_04 §3.6: *"the bishop's authority (office/succession)"*), acting through legislation, **adjudicating the status of T4's martyr pole**. That is a demonstrable relationship between two gravities, and Doc_04 §6 has no cell for it — which I confirmed by reading §6 in place. Its enumerated cells are C1↔C2, C1→C3/C4/C5, C2→C3/C4/C5, C4 as super-integrator, C5↔T2, C2↔T3, T3↔C4, T4↔C2, T1↔C5. **T1 and T4 are never related.** §5.3's list of those cells is exact.

**The finding does not in fact rest on Canon XIV alone, and the document's own sentence says so** — *"it rests on the canons themselves, not on Fragment I."* Three further instances, all read directly:

- **Canon X** — the sharpest, and arguably a better anchor than XIV: clergy who volunteered, lapsed, then resumed the contest are **permanently barred from office**. That is the bishop overriding confessor prestige unilaterally, with no martyr testimony in the loop at all.
- **Canon IX** — argued episcopal discouragement of voluntary martyrdom from Christ's own example (*"they will deliver you up, and not, ye shall deliver up yourselves"*).
- **Canon XIII** — those who fled *"not at all to be blamed."*

**One observation, offered as strengthening rather than as a defect.** In Canon XIV the bishop is *ratifying* status on evidence supplied by the martyrs' own letter and by fellow-ministers' testimony, not overriding it. The document's phrasing — *"the bishop deciding who is reckoned among the confessors"* — is accurate (the canon is Peter's ruling, and Balsamon reads it as a decree), but Canon **X** is the cleaner instance of the bishop's authority running *against* confessor prestige. If the T1×T4 sentence ever needs to survive a hostile reading, Canon X is the load-bearing one. Recorded as **c-22**.

**Verdict on the sub-finding: it survives intact.** Removing Fragment I cost it nothing, because Fragment I on its corrected reading is a bishop-versus-bishop jurisdictional dispute and was never a T4 datum. The T1×T4 gap in §6 is real, and it remains what it was: a gap in a required deliverable under `cic-gravity-index`'s Interaction Test, not the Framework's named red flag, and not a classification change.

---

## D. §11 AND THE HEADER — CHECKED FOR OVERSTATEMENT

### §11's Round 5 → Round 6 entry — **does not overstate. Every claim landed.**

I mapped each claim to a hunk in `git diff b3247c0..3e6c54b`:

| §11 claim | Landed? |
|---|---|
| Round 5 returned SUBSTANTIAL, 1 substantial + 19 cosmetic | ✓ matches the artifact's own count line |
| "found all three of Round 4's resolved" | ✓ matches Round 5 §A and §G |
| OG-6 reviews paragraph fixed, and fixed structurally via the glob | ✓ `Open_Gaps_Tracking.md` hunk |
| §10's file list now points at the glob | ✓ six enumerated items → three, item 2 a glob |
| §3.1's grep note corrected | ✓ and independently verified in §B above |
| §5.3's Fragment I gloss corrected | ✓ and independently verified in §B above |
| OG-6 heading demoted to `###` to match OG-1…OG-5 | ✓ verified: OG-1/2/3/5/4 at lines 77, 93, 104, 207, 240 are `###`; OG-6 at 247 is now `###` |
| OG-6's generation-step summary disentangled (Round 3's candidate vs Round 4's) | ✓ the paragraph now names both candidates with distinct failure modes (c-17 closed) |
| stale "item 4" cross-reference fixed | ✓ now "item 3" (c-16 closed) |

**No phantom claim, for the second consecutive round.** The entry also correctly does *not* claim that the other fifteen cosmetics were applied — they were not, and I string-checked all fifteen loci (see §E). It still does not *disclose* the declines, which is c-19 carried.

### The header's round summaries — **four of five accurate; the fifth is N6-2.**

Rounds 1–4 bullets: I re-verified each against its artifact's own verdict line. 8+8 ✓, 8+10 ✓, 4+12 ✓, 3+15 ✓; "Round 2 ran the C4 route itself" ✓; "Round 3 ran C3 Dependency and T2 and the generation step" ✓; Round 4's Tensional generation step and its "cannot find any route" statement ✓ verbatim in that artifact.

Round 5 bullet: the counts (1 + 19) ✓, "headline upheld a fifth time" ✓, "verified the Eusebius-independence claim at both ends" ✓, "ran two further routes (record-confidence; Dionysius to Basilides at npnf214 `div2 17.5`) — both fail, and the second empirically confirms §7's root-cause thesis in a second volume" ✓ — all faithful to Round 5 §E. **But "Round 3's four all RESOLVED" is wrong: Round 5 verified Round 4's three.** N6-2.

The trajectory line (8 → 8 → 4 → 3 → 1) and the Status line are accurate. *"Falling monotonically"* is loose for a sequence that is flat at 8 → 8; non-increasing, not falling. **c-23**, trivial.

---

## E. NEW FINDINGS

### N6-1 [SUBSTANTIAL — the document misstates its own status] §10's "Not cleared" bullet is a round behind

`Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md`, lines 694–696:

> - **Not cleared.** **Four** adversarial rounds have each returned SUBSTANTIAL REVISION REQUIRED (**8 → 8 → 4 → 3**), every one upholding the headline. **This is the Round 5 draft**; no disposition has been assigned to it, by this thread or anyone else.

Five rounds have returned SUBSTANTIAL, at 8 → 8 → 4 → 3 → 1, and line 5 of the same document says *"Round 6 draft (revised after five adversarial rounds)."* I confirmed with `git show b3247c0:…` that this bullet is **byte-identical to the Round 5 draft**, where it was correct; the revision did not touch it.

Three things make this substantial rather than a typo:

1. **It is a status claim, in the section whose entire purpose is the pass's honest negative inventory.** A project lead reading §10 — the section that says what was *not* done and what standing the document has — is told this is the Round 5 draft with four rounds behind it. It understates the review history by a full round and names the wrong draft.
2. **Round 4 graded this identical defect at this identical locus substantial** (N4-2: §10 *"still 'Two adversarial rounds… the Round 3 draft'"*). Round 5 verified it RESOLVED. It has now regressed. Grading it cosmetic this round would require abandoning a standard the review record has applied twice.
3. **The revision drift-proofed the wrong half of §10.** The file list six lines below this bullet was rebuilt around a glob *precisely because* hand-maintained counts go stale — and the hand-maintained count in the bullet above it went stale in the same commit. The structural fix was correct and incomplete.

**Required:** replace the enumerated count with the same delegation the OG-6 paragraph now uses, or state the current fact — five rounds, 8 → 8 → 4 → 3 → 1, Round 6 draft. The former is preferable: this bullet is the third hand-maintained count in this document's history and the third to go stale.

### N6-2 [SUBSTANTIAL — the header misreports a review outcome and contradicts itself] "Round 3's four all RESOLVED"

Header, line 22, in the Round 5 bullet added by this revision:

> - **Round 5** (`…_Round5_Review.md`) — **SUBSTANTIAL**, **1** + 19. Headline upheld a fifth time. **Round 3's four all RESOLVED** — the first round with no partial and no fix-introduced substantial error.

Round 5 verified **Round 4's three**, and found all three resolved. Round 3's four were verified by **Round 4**, which found *three* resolved and *one partial* — which is what line 17 of this same header says, eight lines up. So the header now asserts both that Round 3's four went 3-resolved-1-partial and that they all resolved.

The rest of the clause is right (Round 5 *was* the first round with no partial and no fix-introduced error), so the error is a copy-paste of the adjacent bullet's subject. But its effect is to misreport what a review round examined and to inflate a resolution count from three to four, in the document's most-read paragraph, in the bullet added to close a finding about self-description accuracy. §11 has it right (*"It found all three of Round 4's resolved"*), so the document contradicts itself across two loci.

**Required:** "Round 4's three all RESOLVED."

---

## F. COSMETIC FINDINGS

**Five of Round 5's twenty were repaired** — c-2, c-5, c-6, c-16, c-17, all verified above. **Fifteen are carried unrepaired.** I confirmed each by string search at its stated locus; numbering follows Round 5's so the carry-forward stays traceable.

- **c-1.** §6.1 still prints *"the theological *centre*"* against Doc_04 §3.4's "center," and still truncates the quotation without an ellipsis.
- **c-3.** §5.4 still calls *"From his demonstration that the soul was not pre-existent to the body"* a heading; the heading is *"Of the Soul and Body."*
- **c-4.** §5.3 still folds **Canon IV** into *"Canons I–V — a graded penitential scale."* Canon IV, which I read this round, is the scale's **refusal** — *"To those who are altogether reprobate, and unrepentant, who possess the Ethiopian's unchanging skin…"* — not a step on it.
- **c-7.** §2's table still says Doc_04 was *"read in full (all 9 sections)."* I counted the headings: **ten**, §0–§9, and §0 is the one §5.1 turns on.
- **c-8.** §3.5's *"14 works assigned to Alexandria from anf06"* still uses "assigned" in the membership sense adjacent to `confidence: assigned` in the field sense.
- **c-9.** §6.1 and §6.2 are still filed under §6, *"The Article 21 substitute (Cross-Stratum Test),"* which neither is about.
- **c-10.** *"roughly a quarter-century earlier"* is still the outer edge of a 14–25 year range.
- **c-11.** §9 Option C still calls §5.1 *"a plain factual error"* where Doc_04 §0's sentence is a hedged collective (*"largely through Eusebius"*) true of Dionysius and Heraclas — which §5.1's own body concedes by writing *"False for Theognostus."* Five rounds.
- **c-12.** §3.4's Canon XI sentence still has no clear subject in its first clause.
- **c-13.** §11's Round 4 → 5 entry still says the §5.3 recast was *"Propagated to the heading, **§1**, §8…"*; §1 was not touched and needed no touching.
- **c-14.** The header's *"Of Round 2's 8: 7 resolved"* still rounds Round 3's three-category tally.
- **c-15.** OG-6 still carries **two** route-test lists — the pre-Round-3 short list at line 256 (*"C5 Persistence, T1 pole separation, T3, T4 confidence, C4, and the Cross-Stratum Test"*) and the full one at 314. A lead reading top-down meets the short one first. This one is worth fixing next round: the corrected paragraph below it is now considerably better than the stale one above it.
- **c-18.** §6.2 still says *"Tested against the six tests:"* and reports three.
- **c-19.** §11 still does not disclose that fifteen cosmetics were carried undone, against the disclosure practice the document set for itself in its Round 2 → 3 entry. No false claim is made.
- **c-20.** §5.3's *"every manifestation… passes through Eusebius"* is still warranted in the text only by the Dionysius record's *"mostly."* Round 5 put the exact warrant on the record (ANF's epistle headnotes: `HE` vii.11; vi.41/42/44; vi.46; vi.40+vii.11; vii.1/10/23); citing them would put the claim beyond a hedge.

**New this round:**

- **c-21.** OG-6's *"Every round to date has returned SUBSTANTIAL REVISION REQUIRED"* is count-free but not drift-free — it goes false the first time a round clears. It is true today. Whoever revises after a CLEARED round must edit it in the same pass, or the drift-proofing will have relocated the defect rather than removed it.
- **c-22.** §5.3's T1×T4 sentence anchors on Canon XIV, where the bishop *ratifies* status on the martyrs' and brethren's testimony. **Canon X** — permanent bar from office for clergy who volunteered and lapsed — is the cleaner instance of episcopal authority running against confessor prestige, and would be the stronger anchor under a hostile reading. Strengthening, not a defect.
- **c-23.** *"Falling monotonically"* (header) and *"has fallen monotonically round on round"* (OG-6) describe a sequence that is flat at 8 → 8. "Non-increasing" is the accurate word.
- **c-24.** OG-6 and §11 both say the self-description drift ran for *"four consecutive rounds."* The occurrences are Rounds 1, 2, 4 and 5 — four rounds, not consecutive ones (Round 3's four findings were all in the argument). Inherited verbatim from Round 5's own phrasing; the count of occurrences is right, the word "consecutive" is not.

---

## G. THE HEADLINE, RE-TESTED

**"NOT structural" is correct. Sixth round, sixth confirmation. I know of no route to a Doc_04 classification change.**

This was a confirmation round and I did not re-run all nine gravities from scratch; I re-tested the loci where this revision changed the evidence, plus the two Doc_04 rules the finding leans on hardest, reading Doc_04 in place rather than through the document:

- **T1 pole separation.** Doc_04 §3.6 verbatim: *"two genuinely distinct poles with real population, institutional, or practice-cluster separation (not a polarity within one person)."* The document's inversion of the discovery pass — a single teacher-bishop-martyr would have been evidence *against* T1 — is exactly right, and §4 therefore defends T1 rather than extending it.
- **T1×T4 and §6.** Confirmed above: the relationship is demonstrable, the cell is absent, and this is an Interaction-Test deliverable gap, not a classification move. T4 carries other relationships (T4↔C2), so the Framework's isolated-candidate red flag correctly does not fire.
- **T4's interior.** Doc_04 §3.6 verbatim: *"its interior is Tier-3 hagiography / Coptic martyrology, held at **Inferential-Thin**."* Peter's canons are juridical and contain no martyr's interior — Canon XIV is about what was done *to* bodies and how the church ranked the result, not about what the martyr apprehended. The Inferential-Thin verdict stands and nothing here licenses filling that silence.
- **Fragment I, re-read.** On its corrected reading it is a bishop-versus-bishop jurisdictional rupture (the Melitian schism). It does not generate a candidate, does not separate poles within T1 differently, and does not touch T4. Its correction removes a plank from the document's argument and costs the argument nothing.
- **§5.5.** `find -iname "*Gravity_Index*"` repo-wide still returns only World #1's workbook and the PAHC generator script. **No Alexandria workbook exists**, and Doc_04 §6's opening sentence still defers full pairwise coverage to it (*"the companion `Gravity_Index.xlsx` carries this as a grid; prose summary here"*). §5.5's consequence for §5.3 is therefore live: if the workbook is absent, the T1↔T4 cell is documented nowhere.

Nothing in this revision opens a route, and nothing in it closes one that was open. **§9 Option B, escalated and not self-disposed, should stand.** What remains genuinely open is not a route but **§3.5's unaudited remainder** — Alexander of Alexandria's *Epistles on the Arian Heresy* still the strongest single item in it, now joined by Round 5's npnf214 finds — and that is a separate pass, correctly declined here.

---

## H. DISCIPLINE COMPLIANCE

| Requirement | Result |
|---|---|
| Declines to self-dispose | **PASS, verified on disk.** `git diff --stat b50302d^..3e6c54b`: the pass's entire footprint across six commits is **seven files** — the finding document, `Open_Gaps_Tracking.md`, and five review artifacts. `git status --porcelain` empty, so what I read is what is committed. Escalation categories 2 and 4 correctly identified; OG-6's *"Status: OPEN — awaiting project-lead disposition"* stands. |
| No `records/alx/` edit | **PASS.** Nothing under `records/` appears in the footprint. |
| No Doc_01–Doc_09 edit | **PASS.** No construction document appears in the footprint. |
| No corpus-map edit | **PASS.** `cic/corpus-map/alexandria-catechetical.yaml` untouched; §10 and §4 report the three overstated headship notes rather than correcting them, which is the right call for a thread that has escalated. |
| No compile; `worlds.yaml` untouched | **PASS.** `records/worlds.yaml` line 41 still pins `packages/alx/2026-09-04T16-41-49Z`. No `Gravity_Index.xlsx` was created to make §5.5 go away. |
| No unverifiable project-lead attribution | **PASS.** `grep -n "Mark\b"` over the document returns nothing, though the corpus map's own npnf214 note reads *"Split 2026-08-26 on Mark's ruling."* The document cites the date and declines the attribution — still the right call. §8 cites the S6.2 declaration by date, not by person. §10: *"No claim that any of this was seen or approved by the project lead."* |
| Claims no status it has not earned | **FAILS at two loci, in the direction of understatement.** The Status line, the Version line, the trajectory note and OG-6 are accurate and unflattering to the document. §10's status bullet (**N6-1**) and the header's Round 5 bullet (**N6-2**) are not. Neither claims *more* standing than earned — N6-1 claims *less* — but both are wrong about the review record, which is the standard this document has been held to five times. |
| Grounded options preserved | **PASS.** Three options intact with cost, precedent and stated reason; Option B recommended and unchanged; §7's portfolio decision separated out and explicitly not run; the recompile/re-admission question reserved to the project lead as *"the project lead's, not this thread's."* |
| Accurate self-report of its own revision | **PASS.** §11's new entry maps claim-for-claim onto the patch, with no phantom claim and no unearned cosmetic credit — second consecutive round. The defects are in the header and §10, not in the log. |
| Ledger entry accurate against the document | **PASS on the paragraph Round 5 flagged.** OG-6's three-produced / two-pre-existing structure still matches §1 and §8; the Reviews paragraph is now accurate and drift-proofed; the generation-step paragraph now distinguishes Round 3's and Round 4's candidates. c-15 (the duplicate short route list at line 256) leaves the entry untidy but not false. |

---

## I. SUMMARY

- **Overall verdict: SUBSTANTIAL REVISION REQUIRED — 2 substantial, 16 cosmetic.** Both substantial findings are one-line corrections in the document's account of its own review history; neither touches the evidence, the argument, the disposition, or the headline. Loci I checked personally: the finding document's header (lines 5–41), §3.1, §3.4, §5.3 (in full, including the Fragment I bullet and the Canon list), §5.5, §6, §8, §9, §10 (in full, and against `git show b3247c0:…`), §11's Round 5 → 6 entry; `Open_Gaps_Tracking.md` OG-6 in full (lines 247–325) and all six OG heading levels; `Doc_04` §3.6 and §6 in place, and its heading inventory; `anf06` Fragment I in full, Canon XIV in full with both scholia, all fifteen canon headings, and 46 Meletius/Lycopolis hits; `records/alx/` by grep; `find -iname "*Gravity_Index*"` repo-wide; `records/worlds.yaml`; `git diff b3247c0..3e6c54b`, `git diff --stat b50302d^..3e6c54b`, `git status --porcelain`.
- **N5-1: RESOLVED.** OG-6's Reviews paragraph now describes disk state accurately, the glob resolves to exactly the five artifacts on disk, and the delegation to the header is the right structural move. The drift-proofing works and asserts nothing false — but it covered §10's *list* and not §10's *status bullet*, which went stale in the same commit (N6-1).
- **c-2: FIXED and accurate.** I re-ran the grep: two hits, both the anf09 filename in an `edition:` field, neither naming any Peter.
- **c-5: FIXED and accurate on every clause.** I read Fragment I in the vendored XML: rival bishop, jurisdictional complaint, martyrs' letter on Peter's side, prison as location only — and "bishop of Lycopolis" is carried by anf06 itself in three places, so the replacement gloss does not commit the fault §4.1 charges against the corpus map.
- **The T1×T4 sub-finding SURVIVES.** Canon XIV is a bishop's decree ranking men among the confessors (Balsamon: *"the canon decrees"*), Doc_04 §6 has no T1↔T4 cell, and the finding is redundantly carried by Canons IX, X and XIII — Canon X being the cleanest instance and the better anchor (c-22). Losing Fragment I cost it nothing.
- **New substantial: 2.** N6-1 (§10 still says "Four adversarial rounds… 8 → 8 → 4 → 3… This is the Round 5 draft" — a regression of the exact locus Round 4 graded substantial and Round 5 certified fixed) and N6-2 (the header's new Round 5 bullet says "Round 3's four all RESOLVED" where Round 5 verified Round 4's three, contradicting the bullet eight lines above it and §11 four hundred lines below — introduced by this revision).
- **Headline: CORRECT, sixth confirmation. No route to a Doc_04 classification change.** Not through T1's pole rule, not through T4's interior, not through the T1×T4 cell, not through the corrected Fragment I, not through anything this revision changed. §9 Option B, escalated, should stand.
- **What this revision got right and must not lose.** Both materially-misleading cosmetics — four rounds old each — are fixed, and fixed from the sources rather than by rewording. The Fragment I correction is the harder of the two and the document took the version that *weakens* its own supporting evidence rather than the version that reads better, which is the behaviour §5.4(b) says it exists to enforce. The glob-and-pointer drift-proofing is a genuine structural improvement over three previous hand-repairs of the same defect. §11 contains no phantom claim for a second consecutive round. And the footprint discipline is unbroken across six commits: seven files, nothing in `records/`, nothing in Doc_01–Doc_09, no corpus-map edit, nothing recompiled, the deployment pin untouched. **A document that has absorbed 26 substantial findings across six rounds without once disputing one, and whose only remaining defects are two sentences about how many rounds it has been through, is in the condition its round count would not lead you to expect.** Fix the two sentences — preferably by deleting the last hand-maintained count rather than by correcting it a fourth time — and I would expect the next round to clear it.

*(This is a simulated AI review. It does not substitute for the Article 31 external scholarly review that OG-4 still requires. A qualified subject-matter reviewer on the transmission of the Alexandrian penitential canons through the Byzantine canonical collections and their ratification at Trullo, on the Melitian rupture and the standing of confessor testimony in Fragment I, and on the Eusebian mediation of Dionysius's Decian correspondence would be the accountable test of §5.3.)*
