# Doc_03 Review — Round 3 (independent narrow recheck, cold)

**Document under review:** `witt_Doc_03_Lexicon_Candidate_List.md` (DRAFT, Revision 2), Lutheran Wittenberg & Its Congregations (Atlas VI.1, `witt`).
**Reviewer:** independent, no drafting involvement, no involvement in Round 1 or Round 2, no prior context on this document or on how its fixes were made.
**Date:** 2026-09-15.
**Scope:** the five-item list Round 2 set for itself in "What a Round 3 check should and should not do," applied to Revision 2. **Not a re-review.** The 606-citation sweep and the 24-citation fresh sample were not re-run — Round 2 confirmed both clean and Revision 2 touched only §0, §11, §12, §13 and one Appendix cell, not the Evidence lines they depend on. S1–S14 and C1–C10 were not re-checked.

**Method.** §0, §10.1, §10.3, §11, §12, §13 and the Appendix read in full; entries 5.7, 6.7, 6.8, 7.4, 7.5 read in full. Doc_01 §8.4 and §8.5 read in full. Lexicon Framework V2.1 opened directly with python-docx and paragraph 97 read from the file rather than from either prior report's quotation of it. A body-vs-Appendix cross-check was written from scratch for this round, comparing Tier, Origin tag and Risk/Function tag; `verify_doc03.py` was neither used nor trusted. Every vendored locus named below was re-opened at its stated lines, and every disputed count re-run with my own `grep`/enumeration rather than read off the document.

---

# VERDICT: MINOR ISSUES REMAIN

**All six items on Round 2's Round 3 list pass.** N1, N2, N3, N4, N6, N7 and N8 are each fixed, and I could not falsify any of them. N5 is confirmed as a disclosed, reasoned deferral, not a silent drop.

**One new substantial finding (R3-1) and five cosmetic (R3-2 – R3-6).** R3-1 is the reason this is not CLEARS REVIEW: N3 was fixed at the symptom and not at the root. The identical defect N3 named sits one item away in the same sentence of §12, untouched, and is larger in magnitude than the one that was fixed.

**Nothing found in this round misquotes a source, miscites a locus, misstates a count, or misclassifies an entry.** Every substantive claim I tested reproduced. The findings below are about coverage statements, warrants and citation hygiene, not about the evidence.

**Disposition: none claimed.** This report is a finding, not a ruling; it does not dispose the document. Per the project's governance rule, none of the findings below may be closed by self-certification.

---

# The six items, checked

## 1. N1 — body-vs-Appendix cross-check on Tier, Origin and Risk/Function — **PASS**

I wrote my own extractor and comparator rather than trusting `verify_doc03.py` or §13's description of it. It parses the `- **Tags.**` and `- **Tier (est.).**` lines from each `### n.m` entry body, parses the Appendix table's Origin, Risk/Function and Tier cells, and compares the three as sets.

**Result: 72 entry bodies, 72 Appendix rows, no row present in one surface and missing from the other, and 72/72 agreement on Tier, Origin tag and Risk/Function tag together. Zero mismatches.**

Specifically confirmed:

- **Entry 7.4's Appendix row now carries PV.** The row reads `| 7.4 | insurrection / common man (1522) | SC | DR RT PV | 2 |`, matching the body's `[SC] [DR] [RT] **[PV]**`. This is the single cell N1 was about, and it is fixed.
- **PV is on exactly {5.6, 6.7, 7.4} in both surfaces** — the filtering surface now returns all three, which was N1's downstream concern.
- Tier counts reproduce independently in both surfaces: **39 Tier 1 / 27 Tier 2 / 6 Tier 3 = 72**.
- [AS] sits on exactly {2.6, 2.7, 4.2, 4.4, 5.3, 6.1, 7.1, 7.5, 8.2, 8.4} — ten entries, matching §11 item 5's enumerated list exactly (relevant to N6 below).
- [CT] sits on exactly {2.2, 7.1} in both surfaces.

One guard worth recording, since a naive extractor would have got this wrong: 7.4's Tags line contains `[PV]` twice — once in the tag run and once inside the prose justification. Set comparison makes that harmless, but a positional parser would double-count it.

See **R3-2** for the one thing about N1's fix that did not check out — the fix's *warrant*, not its result.

## 2. N2 — the Society of Jesus / Lollardy sentence in §0 — **PASS**

Doc_01 §8.4 and §8.5 read in full. §0's corrected sentence now states both positions accurately and, correctly, as two different cases:

- **Lollardy.** §0 says "Doc_01 §8.5 does find no documented direct contact." §8.5 reads: "This document finds no documented direct contact and, per the same discipline as §8.4, does not assert a 'forerunner' relationship it cannot source." Accurate.
- **The Society of Jesus.** §0 now states that §8.4 "states the opposite of what a prior draft of this sentence attributed to it," quotes VI.11's own Step 0 — "the direct, real rival relationship in this batch is Lutheran Wittenberg and the Reformed cities — the Jesuits were founded explicitly within, and as a response to, the same crisis those two candidates answer from the opposite direction" — records that §8.4 finds only that "no documented *personal* contact between Luther and the Society's founders exists," and quotes §8.4's "not a movement in mutual isolation from this one." **All three quotations verify verbatim against §8.4.** The superseded "no documented direct link" wording now appears only as the thing being corrected, attributed to the prior draft, which is where it belongs.
- **The reframing is right, not merely neutral.** §0 now concludes that the direct-rival profile "makes this the untested neighbour most likely to matter, not the one most safely skipped." That is Round 2's own recommended remedy, and it is the correct reading of a revised §8.4 that makes the gap larger rather than smaller.
- One incidental check: §0 quotes VI.11's Step 0 wording directly rather than Doc_01's paraphrase of it. Doc_01 §8.4 records that its own Round 2 (finding N11) caught a paraphrase of that sentence inverting its sense. Quoting the Step 0 wording keeps Doc_03 clear of that trap.

See **R3-3** for one loose word in the same sentence.

## 3. N3 — §12's Neve coverage claim — **PASS** (but see R3-1)

Checked against `cic/texts/luther_works-v1-selected_jacobs-spaeth1915.txt`:

| Fact | Line | Verified |
|---|---|---|
| Work title *A TREATISE ON THE NEW TESTAMENT* | 10629 | ✓ |
| `INTRODUCTION` heading | 10636 | ✓ |
| Prose still running past the declared range | 10746–10762 ("The object of faith is the Gospel...") | ✓ |
| Introduction's last prose line | 10827 | ✓ |
| Signature `J. L. NEVE.` | 10829 | ✓ |
| `FOOTNOTES` block | 10836 | ✓ |

So the introduction runs 10636–10835 plus footnotes, and the declared range 10600–10750 covers rather less than half of it. The document no longer claims otherwise:

- **"In full" is gone.** Neve's introduction has been moved out of §12's "Read in full this pass" list into the "Read in part" list, described as "v1 10600–10750, covering the three cited loci."
- **The stated reason matches the file.** §12's correction note states the heading at 10636, prose continuing past 10750, and the footnotes block at 10836 — all three verified above.
- **The three cited loci are genuinely inside the range.** 10661, 10681 and 10727 all fall within 10600–10750, so no citation is left unwarranted.
- **§12 and §13 now agree.** §13's v1 row describes the same range without "in full," and §12's closing sentence still excludes "Neve's introduction beyond the loci read" from the saturation claim.

## 4. N4 — the [PV] key, 5.7's decline, and §13's escalation check — **PASS**

### Framework paragraph 97, read directly from the .docx

```
The term or concept is important within some streams, voices, or periods of the world
but is not universally representative across the whole reconstructed ecology. This tag
should trigger explicit attention during Internal Plurality review (per the Template)
rather than silent flattening into one position.
```

The document's quotation of it is accurate in substance and includes "streams" and "periods." It drops one word — see **R3-4**.

### Do the three places now say the same thing? Yes.

- **§0** quotes para 97, states the operative test as "where the vendored **streams, voices, or periods** demonstrably differ," and then names the substitution openly: this world "has no streams in the Framework's sense to test — Doc_01 §6 found it strand-singular — so this document uses **register**... as the nearest available proxy for what a stream would test in a strand-plural world, and states that substitution explicitly here rather than silently."
- **5.7** states it was "re-reasoned Round 2 N4 against the Framework's own test (streams/voices/periods), not the register-count proxy Revision 1 used."
- **§10.1's PV paragraph** records 5.7 as "re-reasoned against the Framework's own streams/voices/periods test at Round 2 (N4) and declined as toleration of an outside opinion rather than a demonstrated internal split."
- **§13's escalation check** states that both narrowings are "resolved by restoring the Framework's own wording and explicitly naming and justifying the one substitution this world's strand-singular status actually requires (register standing in for stream) — a disclosed, reasoned application of an existing Framework category to this world's own shape, not a proposed change to the category itself."

These are consistent with each other and with para 97. The substitution is now named and justified rather than silent, which is what N4 asked for. §0's justification (strand-singularity leaves no streams to test) is sound on Doc_01 §6's own finding.

There is no contradiction between §0 licensing register-as-proxy and 5.7 saying it did not use the register proxy: 5.7 declines because *no* plurality — of stream, register, voice or period — is attested at all, so the proxy question never arises. 8.2's decline still cites "single-register," which is now legitimate because §0 has licensed and explained that proxy; Round 2 had already cleared 8.2 on any reading.

### Is 5.7's new reasoning a fair reading of the passage?

**Yes — it is fair, well grounded, and appropriately hedged.** I read `luther_works-v2-selected_jacobs-spaeth1916.txt` 7140–7232 rather than only the cited window.

The quotation verifies verbatim at 7221–7224: "I permit other men to follow the other opinion, which is laid down in the decree _Firmiter_[50]; only let them not press us to accept their opinions as articles of faith, as I said above."

The document's reading — that this is Luther "conceding latitude to a pre-existing Catholic position he is declining to fight over, not a demonstrated split between streams or voices *within* this world's own reconstructed ecology" — holds against the text on three grounds:

1. The "other opinion" is expressly identified as an external one: the decree *Firmiter*, i.e. the received canon-law dogma Luther is arguing against throughout the section. The text does not say that anyone inside the Wittenberg reform holds it.
2. "Other men" is unspecified. Nothing in the passage attests that the toleration is extended to members of this world's own community, which is what an attested internal plurality would require.
3. The document's supporting point checks out and is the stronger half of its argument. At 7143–7149 the one group inside the world that *is* described is described as holding neither position: "as they do not understand, neither do they dispute, whether accidents are present or substance[47] but believe with a simple faith that Christ's body and blood are truly contained in whatever is there." The common people are undifferentiated, not a third party to a split. That actively cuts against PV rather than merely failing to support it.

The note also declines to overclaim — it records that "the case is closer than 8.2's and worth Doc_06 re-reading directly rather than trusting this pass's judgment alone." That is the right disposition for a judgment call at this stage.

I record the contrary reading so a later reader can weigh it: in 1520 Luther is still nominally inside the Western Church, so the boundary between "outside opinion" and "opinion held by people in this world" is not as clean as the note implies. But the note's claim is about what the passage *demonstrates*, and on that narrower question it is correct — the passage demonstrates a boundary of toleration, not an attested internal split.

See **R3-5** and **R3-6** for two smaller things inside this item.

## 5. N5 — deliberate deferral — **CONFIRMED DEFERRED, DISCLOSED, WITH REASONS**

N5 is disclosed in three separate places in §13, not dropped:

- the Round 2 review-outcome bullet states it in full, including the governing rule it sits against;
- the Round 2 fixes bullet states "**N5** — not fixed, per the review's own recommendation; logged here as a disclosed, deliberate deferral to the pre-disposition cleanup pass, not an oversight";
- the review-requirement item (e) hands the open decision forward to this round rather than closing it.

The Disagreement log records N5 as "explicitly deferred with reasons stated." This is honest handling, and it is what the project's "don't let gaps go quiet" discipline asks of a deferral.

### My independent judgment, as requested

**Not blocking for Revision 2. It should become blocking at disposition, and it needs an owner outside this document.**

*Why not blocking now.* Round 2's reasoning holds and I can confirm it empirically: the inline markers made this round fast and cheap. I located every Revision 2 fix by searching for its finding number, which is most of why this recheck cost what it did. The rule the markers sit against binds `World-Builds/` documents "once approved to proceed"; this one is DRAFT, Revision 2, disposition none claimed. No rule is currently breached, and stripping them mid-cycle would make the next targeted recheck materially more expensive for no gain in correctness.

*Why it cannot be deferred indefinitely.* Three things, and the first is new information this round:

1. **The deferral is accreting, not static.** Round 2 counted "roughly thirty" markers in Revision 1. My count of Revision 2 finds **38 bolded inline fix markers** across §§0–12, **52 total "Round 1"/"Round 2" mentions**, touching **19 of the 72 entries** plus §0, §10, §11 and §12. Revision 2 added its own layer — "corrected, Round 2 N2," "re-reasoned Round 2 N4," "corrected Round 2 N7," "corrected, Round 2 N8" — on top of Revision 1's. Each round makes the eventual strip larger and riskier, because by then some markers will be load-bearing prose wrapped around substantive content (5.7's PV note and §0's tag key are already in that shape) and separating the two will be a judgment call, not a deletion.
2. **The strip is still unowned.** It exists only inside §13 of the document it is about. Nothing outside Doc_03 records that Doc_03 must not be approved to proceed until the markers come out.
3. **This world has already had this failure once.** `witt_Source_Registry.md` is **APPROVED TO PROCEED, Revision 5** and its header carries five rounds of fix narration — what Round 1 corrected, what Round 4 found in Round 3's fix, what Round 5 caught — plus the inline correction note in row R30. That is the exact end-state N5 predicts, already realised in a sibling file in the same directory. It is evidence that "we'll clean it up before disposition" does not happen by itself here.

*What I recommend, without treating it as a new finding.* Keep the markers through the review cycle. Register the strip as a **named precondition on Doc_03's approval to proceed** somewhere that outlives this document's own §13 — see **R3-7**, which is the mechanism for that and is missing.

## 6. N6, N7, N8 — **ALL PASS**

**N6 — PASS.** §11 item 5 now reads "ten of seventy-two, corrected Round 2 N6 from 'seventy-one,' stale since 2.10 was added at Revision 1." The ten-entry [AS] list in that sentence matches my script's recomputation exactly (2.6, 2.7, 4.2, 4.4, 5.3, 6.1, 7.1, 7.5, 8.2, 8.4), and 72 is the count I independently derive. The only two remaining occurrences of "seventy-one" in the document are inside correction notes describing the superseded value, which is correct.

**N7 — PASS, verified by my own enumeration, not by reading the document's claim.** I enumerated every printed thesis number in `luther_works-v1-selected_jacobs-spaeth1915.txt` lines 1139–1602: 95 printed numbers, first `1.` at 1154, last `95.` at 1516.

| Duplicated number | Printed at | Standard number displaced |
|---|---|---|
| 13 | 1198, 1201 | 12 |
| 36 | 1249, 1285 | 26 |
| **53** | **1348, 1352** | **52** |
| 73 | 1419, 1422 | 72 |

Exactly four duplicates, and the numbers 12, 26, 52 and 72 are never printed — the mirror image of the same corruption, which confirms the four are real duplications rather than a parsing artefact. §0 Discipline 1 now names all four: "it prints '13.', '36.', '53.' and '73.' each twice." The previously omitted "53." — the number 1.1 and 9.3 actually cite and correct — is now included.

**N8 — PASS.** Entry 6.7's Voices line now reads: "it also occurs once at v1 12378, lowercase, in Schmauk's 1915 introduction (grep-located per §13's builder-grep sweep, not inside a declared direct-read range — corrected, Round 2 N8, to be marked the same way Ap 4729 was)." §13's v1 discovery row carries the matching flag: "**12378 grep-located ('Popedom,' builder-grep row below — corrected, Round 2 N8: previously cited with no range or grep-located flag)**." The locus is no longer undeclared.

I re-verified the underlying claim independently: `grep -o -i "popedom"` across all vendored files returns **seven** occurrences — six capitalised in `luther_table-talk_bell1886.txt`, one lowercase at v1 12378, which reads "The open and fearless opposition to the popedom at Rome, which," inside Schmauk's introduction to *The Papacy at Rome* (12218–12426). 6.7's "chiefly Bell's, six of seven" is exact. See **R3-6** for one imprecise word in the fix note.

---

# NEW SUBSTANTIAL FINDING

## R3-1 — N3 was fixed at the symptom; the same defect sits unfixed in the same sentence, and is larger

**What I checked.** Having verified the Neve fix, I checked the rest of §12's "Read in full this pass" list against the files, on the view that N3's root cause is not one bad range but an unaudited coverage list.

**What the document claims.** §12, first sentence:
> "Read in full this pass: SC (whole file); the Ninety-Five Theses and their footnotes; AC Article II and Articles IV–XXVIII and the abuses preamble...; the *Kurze Form* preface and Commandments summary; Wittenberg Sermons 1, 2, 5, 8; the four hymnal prefaces and hymns I, IV, V, XXVI; Luther's 1539 and 1545 prefaces; ***The Papacy at Rome* 12775–12974**."

**What I found in `luther_works-v1-selected_jacobs-spaeth1915.txt`:**

| Feature | Line |
|---|---|
| Work title, `TO THE PAPACY AT ROME` | 12694 |
| Subtitle, `AN ANSWER TO THE CELEBRATED ROMANIST AT LEIPZIG[1]` | 12696 |
| First internal heading, `THE STATEMENT OF THE CASE` | 12775 |
| Declared range ends here, mid-argument | 12974 |
| Argument continues, answering 12968–12974 directly | 12975 onward |
| Work's `FOOTNOTES` block | 14691 |

The treatise runs from **12694 to roughly 14690** — about **2,000 lines**. The range declared "read in full" is **200 lines**, roughly a tenth of it, and it does not end at a structural boundary: 12974 closes the Romanist's syllogism ("B. Inasmuch as all Christendom is one community on earth, it must have a head, which is the pope") and 12975 begins Luther's reply to it ("[Sidenote: The Futility of the Argument] This argument I have designated with the letters A and B..."). The range stops in the middle of an exchange.

The Registry is more careful than §12 here. Row **R8** records only: "Introduction 12218–12320 read." It makes no claim that the treatise's text was read in full, and §11 item 8 — the "read in part" carry-forward list — does not list the Papacy treatise at all. So §12's "read in full" is the only place this claim exists, and it is unsupported by the file and unsupported by the Registry.

**Why it matters.** Three ways, and the third is the finding.

First, magnitude: proportionally this overstates coverage further than the Neve item did. Neve's range covered a bit over half its introduction; this covers about a tenth of its treatise.

Second, function: §12 exists to say what may and may not be relied on, and its next sentence is "Saturation is claimed only for the sections read in full." A downstream builder reading §12 would conclude that *The Papacy at Rome* has been exhausted for candidate terms and needs no further reading. It has not been. The treatise is the world's most sustained argument on papal authority, bearing directly on 6.7, 6.6 and 6.1.

Third, and this is why it is graded substantial rather than cosmetic: **this is "no fix on a fix" and "find and fix the root cause, not the symptom" in the plain sense.** Round 2 told the document that its "read in full" list contained an item that was not read in full. Revision 2 corrected that one item, wrote a careful inline note explaining exactly why the range fell short, and did not check the other items on the same list — including the only other one that carries bare line numbers, sitting eight words away in the same sentence. The class of defect was diagnosed and the class was not swept. By parity of grading with N3, which Round 2 called substantial, so is this.

I record the mitigation, as Round 2 did for N3: **no citation in the document is unwarranted by it.** 6.7's v1 12786–12788 falls inside 12775–12974, and every other entry §13 routes to this range is covered. Nothing is misquoted and nothing is miscited. The defect is in the coverage statement, not in the evidence.

**Fix.** Move *The Papacy at Rome* 12775–12974 from §12's "read in full" list to its "read in part" list, described as what it is — the opening section of the treatise, covering the cited loci — and add it to §11 item 8's carry-forward so the unread remainder is named as an open item. Then audit the remaining items on the §12 "read in full" list against the files in one pass, rather than one finding at a time, and say in §13 that the list as a whole was checked. The three unranged items I did not test (the *Kurze Form* preface and Commandments summary, the four hymnal prefaces, Luther's 1539 and 1545 prefaces) should be included in that sweep.

---

# NEW COSMETIC FINDINGS

**R3-2 — §13 attributes N1's fix to a script that is not in the repository.** §13 states: "`verify_doc03.py` rewritten to actually compare Origin and Risk/Function tags (not just tier) between body and Appendix, and re-run clean on all 72 rows." No file named `verify_doc03.py` exists anywhere under `/home/user/cic-project`. **Mitigation first, because it is the main thing: the claimed result is true.** My own independently written cross-check reproduces it exactly — 72/72 on all three columns — so the document is not asserting a false result, and this is a different and much smaller thing than N1, which asserted a result that did not reproduce. What is missing is the artifact. N1's fix instruction was to "re-run `verify_doc03.py` and establish why it passed," and the answer given names an instrument a later reader cannot open, re-run, or inspect for the same blind spot that caused N1. Either commit the script where such things belong (`Build/Ministry/Operations/Audits/`) and cite it, or drop the filename and describe in §13 exactly what the check compared and how — which is what makes it re-runnable. The project's own rule that a review finding "can't be dismissed by self-certification" is the reason to prefer the first.

**R3-3 — §0 says Doc_01's Round 1 struck the Society of Jesus claim "as unsourced"; §8.4 records it as struck because a source, once read, said otherwise.** §0 writes: "that passage exists specifically because Doc_01's own Round 1 struck an earlier, similar claim ('no documented direct link') as unsourced." Doc_01 §8.4's own account is different in kind: the original draft was struck because it had been written "reading only this world's own Step 0 and the census," and "The Society of Jesus's own Step 0 (§2 A3), **now read**, states the relationship from the other side in direct terms." The claim was not unsourced; it was contradicted by a source that had not yet been read. The distinction matters slightly because N2's whole subject was Doc_03 characterising §8.4's findings imprecisely. One word: "as superseded" or "as contradicted by VI.11's own Step 0, once read."

**R3-4 — §0 labels its para 97 quotation "quoted here verbatim," and it drops a word.** Framework para 97, read directly from the .docx, reads "...of the world but **is** not universally representative across the whole reconstructed ecology." §0's quotation reads "...of the world but not universally representative across the whole reconstructed ecology," and the parenthesis asserts "para 97, quoted here verbatim." The sense is unchanged and the two words N4 and S12 were about ("streams," "periods") are both correctly present. But the document makes an explicit verbatim claim, and the project's own rule is that "a record marked 'quotes verified' is a claim to re-check, not a fact to trust." Restore "is," or drop the word "verbatim."

**R3-5 — 5.7's new bracketed gloss is correct but uncited, and its supporting locus is outside every declared read range.** The re-reasoned note renders the passage as "the decree *Firmiter* **[the 1215 Fourth Lateran dogma]**." Square brackets elsewhere in this document mark the edition's own insertions, and the edition's footnote [50] — the marker actually attached to *Firmiter* at v2 7223 — reads in full: "_Decretal. Greg. lib. I, tit. i, cap. I, section 3_." It does not mention Lateran or 1215. **The gloss is nevertheless sound and not supplied from general knowledge:** the same edition's footnote **[45]**, at v2 10562–10566 and anchored in this same treatise at v2 7026, reads "In the dogma of transubstantiation (Fourth Lateran Council, 1215) the Church taught that the substance of bread and wine was changed..." So Discipline 2 holds in substance. Two smaller things do not: the gloss is given with no locus, against Discipline 1's "every quoted phrase is given with the file and line(s) where it begins"; and both v2 10562 and v2 10577 fall outside every v2 range §13 declares. This is the N8 class of defect — a relied-upon locus outside the declared read record — reintroduced by the revision that fixed N8, which is the same root-cause pattern as R3-1. Cite the gloss to v2 10562 and either extend the v2 row or flag it, as 6.7 now does for v1 12378.

**R3-6 — 6.7 says v1 12378 is marked "the same way Ap 4729 was," and the two are marked in different ways.** Ap 4729 was handled by *extending a declared read range* (§13's Ap row now reads 4700–4730), and entry 6.8 cites it plainly with no flag. v1 12378 is handled by a *grep-located flag* with no range extension. Round 2's N8 offered both routes explicitly, so choosing the second is fine and the locus is now properly declared either way — it is only the claim of sameness that is inaccurate. Say "declared rather than left implicit, as Ap 4729 now is" or similar.

**R3-7 — this world has no `Open_Gaps_Tracking.md`, so N5's deferral and §11's nine open items live only inside the documents they concern.** `Open_Gaps_Tracking.md` exists for Alexandria, Syriac and Imperial-Juridical Christianity, opened at thread launch and described in Alexandria's own header as "the durable record; no real decision, review outcome, or open question lives only in the build thread's own conversation history." `World-Builds/Lutheran-Wittenberg/` has no such file, and there is no `world-build-docs/witt/`. The project rule is that "every known gap, open question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to live only in a conversation thread." At present the N5 deferral, the untested-neighbours gap, the unread Apology, the two unrowed [CT] contests and §11's Registry-maintenance proposals are all recorded only in Doc_03 itself. **I raise this as an observation, not as a Doc_03 defect** — creating it is the build thread's call, not this document's, and under the project's own default-actions table doc hygiene on another thread's content is flagged, not touched. But it is the mechanism that would own N5's strip, and its absence is why I judged above that the deferral needs an owner outside §13.

---

# Statistic re-run, and one small discrepancy

§13 states "26,073 words by `wc -w` after Revision 2's edits." `wc -w` on the current file returns **26,082**, a difference of nine. Too small to be a finding on its own, and I note it only because §13 offers the figure as re-runnable and Round 2 confirmed the previous revision's figure reproduced exactly. It most likely reflects a count taken before a final edit. Re-run it when the fixes above are made.

Other figures re-run and confirmed: 72 entries; 39/27/6 tier split; ten [AS] entries; three [PV] entries; two [CT] entries; seven "Popedom" occurrences, six of them Bell's; four duplicated thesis numbers.

---

# What a Round 4 check should and should not do

Smaller again. If the fixes above are made:

1. **R3-1** — re-read §12's "read in full" list against the files, all items at once, and confirm §11 item 8 carries the Papacy remainder forward. This is the only item of any weight.
2. **R3-2** — confirm `verify_doc03.py` exists where §13 says it does, or that §13 no longer names it.
3. **R3-3 – R3-6** — four single-phrase checks.
4. **Do not re-run** the 606-citation sweep, the 24-citation sample, the body-vs-Appendix cross-check, the thesis-number enumeration, or the Doc_01 §8.4/§8.5 comparison. All five came back clean this round, and the fixes above touch §0, §11, §12, §13 and entry 5.7's tag note only.
5. **N5** remains open by design. A Round 4 need not re-litigate it, but the document should not reach disposition while it is open and unowned (**R3-7**).

**Disposition: none claimed by this review.** Under the project's governance rule, no finding above may be closed by self-certification; each needs independent re-confirmation.
