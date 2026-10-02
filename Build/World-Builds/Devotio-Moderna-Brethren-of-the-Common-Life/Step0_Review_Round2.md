# Step 0 Review, Round 2 — Devotio Moderna / Brethren of the Common Life

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` at Revision 2, as it stands after the narration-stripping hygiene pass (commit 4b4ce830). Compared word-for-word against the pre-hygiene Revision 2 text (commit e3d87bb8).
**Checked against:** the Round 1 findings (commit acd9a888), the census entry in `cic-website/data/world-census.json`, `cic/texts/INTAKE.md`, `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, the Devotio Moderna corpus-map, the Constitution (V2.3 text, file `CiC_L1_Constitution_V2_2.docx`), and the vendored files in `cic/texts/`. Every quote was grepped by this reviewer. The document's own "checked" claims were not relied on.

## Verdict

**Targeted revision needed.** The Round 1 core fixes held. The census record, the date math, the letter count in B1, Groote's English voice in *Founders*, the authority framing, the geography and the authorship dispute are all fixed in substance, not just in wording. The floor and Tier 1 conclusions stand.

Three substantial problems remain:

1. The Groote "open question" did survive as a visible open question, as Round 1 asked. But it is no longer open. Mark ruled on the underlying rule on 2026-09-25. His ruling was merged before both the Revision 2 merge and the hygiene pass. The document now misstates the current rule.
2. The document's picture of what is vendored is out of date. It calls Zerbolt "not vendored" and an "unverified lead", but Zerbolt is now in the corpus.
3. Two attribution errors. One of them started in Round 1's own finding S4.

Two of the three come from events after Revision 2 was drafted, and the third comes from a Round 1 reviewer error. None is a failure of the revision loop itself. That matters for counting toward the three-round cap (see Disposition).

## Findings

### Substantial

**R2-S1. The S5 open question has been answered by Mark's own ruling. The document now misstates the governing rule.**

- **The ruling.** Mark ruled on 2026-09-25 (PR #593, merged 17:45 UTC; entry in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`): "non english sources are treated as primary sources if they are primary sources to the world. language should not matter, only the sources credibility and truth."
- **INTAKE.md changed.** `cic/texts/INTAKE.md` now says "A clean public-domain original can be primary evidence." The phrase this document quotes as the current rule is gone from INTAKE.md: "second witnesses — never primary evidence for a Representative... this project's evidence language is English." That phrase exists only in the file's history before commit 077b84fe.
- **The Groote letters were re-assessed.** The follow-up commit cd63bbab re-assessed the Groote letters under the ruling. The corpus-map now says the "primary" label "now has real backing". The scan is not on the OCR ruling's list of garbled files.
- **Timing.** Revision 2 (15:55 UTC) came before the ruling, so its S5 handling was correct when it was drafted. The hygiene pass (4b4ce830, 18:09 UTC) came after the ruling. That pass also edited corpus-map files.

The hygiene pass kept the question open, as it was told to. But it also added two distortions:

- **A false quote.** It changed "Revision 1 also filed the Groote letters as 'PRIMARY content rather than a second witness'" into "The corpus-map currently files the Groote Latin letters as 'PRIMARY content rather than a second witness.'" That wording never appeared in the corpus-map. It is Revision 1's own paraphrase: `git log -S` traces it only to commit 0d4dc6b0. The corpus-map's pre-ruling wording was "vendored as PRIMARY content, the same treatment this corpus already gives comparable cases." So a paraphrase now appears as a quote of a canonical file, in the present tense, when that file said something different.
- **A present-tense claim about a retired rule.** It changed "Independent review found this conflicts" into "This conflicts with this project's own written rule." That states a retired rule as current.

One more problem with the cited precedent. The document leans on the 1606 Jesuit Constitutions and Nadal's 1595 *Adnotationes*. Both are now held as second witness under Mark's OCR ruling "a", because of scan quality. The precedent now points the other way.

**Fix:** Replace the open question in all five places it appears: the Status line, §3 B1, §4 item 2, §6, and the "Recommended next step". Replace it with a plain statement that Mark's 2026-09-25 library ruling governs. Under that ruling, the Acquoy Latin letters are primary evidence. Quote records hold the verified Latin. The spoken English is an Opus rendering, independently Opus-checked. *Founders*' English texts become a cross-check where they overlap. Cite the Decision Log entry.

Applying an existing ruling is not a new methodology change, so no fresh ruling is needed from Mark. This should not be left as a question for him. Round 1's instruction to "keep it open" was correct when given, but it has been overtaken.

**R2-S2. What the document says is vendored is out of date. Several binding statements are now false.**

Commit 79b68940 ("Vendor 40 confirmed PD sources across all six next-build worlds", 16:39 UTC) landed before the hygiene pass. The Devotio Moderna corpus-map now lists 11 files, not 3:

- Zerbolt, *The Spiritual Ascent* (Arthur 1908), `zerbolt_spiritual-ascent_arthur1908.txt`, with Kempis's Life of Zerbolt
- Kempis, *Chronicle of Mount St Agnes* (Arthur 1906)
- *The Little Garden of Roses and Valley of Lilies* (1867)
- Busch, *Chronicon Windeshemense* (Grube 1886, Latin)
- four Kempis *Opera Omnia* volumes (Pohl, Latin)
- the original three

The document still says the following:

- B2 says Zerbolt's *Spiritual Ascents* is "not vendored" and names the Arthur Zerbolt and Chronicle translations as an "Unverified lead... worth checking before Doc_02."
- §4 item 5 and the Tier paragraph list Zerbolt as a gap in what is vendored.
- B2, B1, §5 and the Section B conclusion describe a three-work base throughout.

The women's-side claim also needs care. "Zero vendored representation" should become "no vendored text in the Sisters' own voice." The *Chronicle* now records the Diepenveen Sisters' investiture in 1408 (line ~4282) and other sisters' houses, but it does so from the canons' side. The census's named voice, the Sisters' own collective lives, is still unvendored. Van Engen's *Basic Writings*, named by the census and in copyright, is also missing from B2's gap list.

**Fix:** Re-state B1, B2, the Section B conclusion, the Tier paragraph and §4 item 5 against the current corpus-map. The three-pillar framing and Tier 1 probably get stronger, not weaker. That is for the revision to state, not for this review to assume.

**R2-S3. Two attribution errors.**

- **(a) The Utrecht letter is not Groote's own writing.** B1 lists "an appendix letter to the Bishop of Utrecht" among "his own writing in public-domain English." It is not his. The *Founders* heading (line ~5095) reads "A Letter to the Bishop of Utrecht on behalf of Master Gerard Groote." The body speaks of Groote in the third person ("that Gerard Groote, a deacon of your Diocese"). Acquoy's introduction (line ~3787) names the author as an unnamed friend: "quidam Gerardi amicus, cujus nomen non ad nos pervenit." This error started in **Round 1's own S4**, and Revision 2 carried it forward faithfully. The reviewer is correcting its own earlier finding here. A1's separate description of the letter is accurate: "an appendix letter pleads for his suspended preaching license."
- **(b) *Founders* is Kempis's book, not Groote's.** A1 says "Groote's own *Founders* records 'many prelates of the Church were opposed to him...'" *Founders* is Kempis's work. The quoted passage (lines 2754–2758, Ch. IX per Acquoy's "Vita G. M. cap. 9") is Kempis's narration about Groote. The quote is verbatim. The attribution is wrong.

**Fix:** In B1, take the Utrecht letter out of the list of Groote's own writing. Describe it as a friend's letter on his behalf, preserved by Kempis. In A1, change "Groote's own *Founders*" to "Kempis's *Founders*".

### Moderate

- **R2-M1. A1 overstates what the Protestatio proves. Part of this was added by the hygiene pass.**
  - The hygiene pass added a new sentence: "the floor finding above rests on the positive Trinitarian/Christological evidence in §2 A1." That wording is not in pre-hygiene Revision 2.
  - The Protestatio (lines 4147–4185) is a general profession of Catholic orthodoxy: "that faith which is certain, pure, and Catholic, resting upon Jesus Christ Himself Who is the chief corner Stone"; Scripture and the Fathers; submission "to the judgement of the Holy Roman Church." It is real, positive orthodoxy evidence, but it has no Trinitarian or Christological content in the Article 4 sense.
  - The quoted fragment, "in regard to those things that are of faith, I have...", stops before any content at all.
  - "offered specifically to answer the movement against unorthodoxy" is garbled.
  - **Fix:** Describe the Protestatio accurately and quote its actual content. If A1 wants Article-4-specific positive evidence, cite and verify a passage that has it; Round 1 S12 pointed to *Imitation* Book IV. The floor conclusion itself is not at risk.
- **R2-M2. §0 still says "documented both-directions influence on two already-source-ready worlds."** The document corrects both claims in B1 and B3: "documented" is too strong for the Luther direction, and Wittenberg is Built & Live. So §0 contradicts the document's own later sections. §1's unqualified "touched a year of Luther's own schooling" is acceptable only because B1 qualifies it.
- **R2-M3. Round 1 S13 is not addressed.**
  - The Hussite Step 0 still says Mark selected the Hussites "specifically to bring Era 6 to a three-candidate set alongside Lollardy and Devotio Moderna."
  - This document says Mark's first instruction named Lollardy and the Hussites, and that Devotio was restored afterwards as the third.
  - Both documents claim to be the candidate "added to complete a three-candidate Era 6 batch," and both cannot be right.
  - No decision-log entry records the selection sequence.
  - Mark's quoted instruction, "add it back in to era 6 so that is 3 worlds for era 6", cannot be verified against any file in the repo.
  - **Fix:** Log the actual sequence in a decision log and make the two documents agree.
- **R2-M4. The narration strip is incomplete.**
  - Revision-history wording is still in the text: A3's heading "with a date correction"; "Corrected evidence:"; "Clears — on the corrected dates"; three "(… corrected)" tags in the Section A conclusion; B1's heading "corrected on several points"; B3's "with a correction to their status"; A3's "per §3 B5's own correction"; the Section B conclusion's "corrected" and "a corrected, more honest account"; §4 item 1 "corrected at Revision 2"; §4 item 2 "The letter count is corrected"; §4 item 4 "— corrected"; §0's "disclosed accurately rather than smoothed".
  - These describe the document's own history rather than stating facts. That falls under the same CLAUDE.md "live/canonical surfaces" rule the hygiene pass was enforcing.
- **R2-M5. The document points to a Round 1 review that is not in the tree.**
  - The Status line and §6 point to `Step0_Review_Round1.md` for "the full finding list."
  - That file is not on this branch or on `origin/main`. It exists only in commit acd9a888, on the unmerged branch `origin/source-research/step0-review-round1`. The same is true for all six worlds' Round 1 files.
  - The hygiene pass stripped the inline recap because "that record belongs in the sibling Step0_Review_Round1.md file." That file is missing, so the Round 1 audit trail is currently nowhere on main.
  - That branch also holds Round 1's fix to the Benham file header. `kempis_imitation-of-christ_benham1886.txt` still reads "Cassell & Company" here; the title page reads "John C. Nimmo."
  - **Fix:** Merge or restore the Round 1 review files. This is outside this document's own thread; flagged, not touched.
- **R2-M6. §4 item 2 gets the letter count wrong.** It says "14 of 66 surviving." B1 correctly says 64 of the 66 are attributable to Groote. Acquoy (lines 896–899) says the 19th and 20th letters are by William of Salvarvilla. It should read "14 of the 64 attributable to Groote in the codex." The corpus-map's Groote staging entry still has Round 1's S3 error ("fourteen letters", "Gerard Groote's own surviving letters"). It also carries inline "Correction (2026-09-25)" narration inside a canonical file. Both are flagged for the corpus-map owner, not touched here.

### Minor

- **"Rests" and "evidently rested" disagree.** B2's "the earlier Tier 1 census finding … rests in part" was hardened from Revision 2's "evidently rested." The Section B conclusion still says "evidently," so the two sections now disagree.
- **Benham's position on Gersen is overstated.** Benham is firm that Kempis did not write the book: "the erroneous notion that he was its author" (line 520, verbatim). But he reports the Gersen case as the view of "the advocates of the Gersen authorship" and closes with "Whoever the author may be" (line ~661). "Argues instead for … Gersen" goes a little beyond what he says.
- **The Xavier anchor is Coleridge's, not Xavier's.** It is Coleridge's (1872) editorial narration (line 3509) and a footnote citing Alcazar (lines 4532–4536), not Xavier's own letters. "Xavier's *Letters* Vol. 1 … records" should name the editor.
- **Dangling boilerplate.** "figures below are raw word counts from vendored .txt" is left over, and no figures follow it.
- **Punctuation in a census quote.** The `relationsSummary` quote uses an em dash where the census has " - ". Round 1 flagged this as minor, and it is still unfixed.

## Round 1 findings: disposition check

| Round 1 | Fixed? | Note |
|---|---|---|
| S1 census record | Yes | `statusWord` / `statusDescription` quoted verbatim against the census; framed as a carry-forward check. |
| S2 date math | Yes | 1471 is 46 years before 1517; 1380 is not a founding date; the 1374 deed and "after his death in 1384" are verbatim from the census; "c. 1380" is in the header, and Benham has "about the year 1380" (line 493). |
| S3 letter count | Mostly | B1 is correct (66 / 64 / 14; 15 EPISTOLA matches = title plus I–XIV). §4 item 2 is still wrong (R2-M6). |
| S4 Groote's English voice | Mostly | Protestatio (line 4147), Resolutions (line 4223), excerpted letters (line ~2740) and the appendix (line 5093) are all present. But the appendix letter is not Groote's (R2-S3a, a Round 1 error). |
| S5 Latin primary/second witness | Overtaken | Kept visibly open, as instructed, but Mark has since ruled (R2-S1). |
| S6 authority framing | Yes | "forbidden to preach by an edict craftily obtained" and the census's "concubines" sentence are verbatim. The non sequitur is removed. Attribution slip at R2-S3b. |
| S7 geography | Yes | "Westphalia and Saxony" is verbatim (line 3799). |
| S8 authorship dispute | Yes | Slight overstatement (minor above). |
| S9 influence confidence | Partly | Fixed in B1 and B3, not in §0 (R2-M2). |
| S10 Wittenberg status | Partly | Fixed in B3, not in §0 (R2-M2). The "no corpus-map cross-reference" claim holds: the only Wittenberg matches are the word "devotional". |
| S11 gap disclosure | Was fixed, now stale | "Only one gap" is gone. The gap list has been overtaken by new vendoring (R2-S2). |
| S12 sampling vs. read | Yes | The header phrase "the opening pages and a mid-document sample" is verbatim. The positive-evidence claim is overstated (R2-M1). |
| S13 selection history | No | R2-M3. |

## Checked against the hygiene diff (e3d87bb8 → 4b4ce830)

No fact, date, citation or quote was dropped outright. Three substantive changes went beyond removing narration, and none was marked:

1. The S5 paragraph changed a Revision 1 paraphrase into a present-tense quote of the corpus-map (R2-S1).
2. A1 gained a new claim that the Protestatio is Trinitarian/Christological evidence (R2-M1).
3. B2 hardened "evidently rested" to "rests" (minor).

The B1 letter-count sentence was reworded into a new claim ("64 of his letters survive in the source codex"). That claim is accurate.

## Confirmed accurate

- The Article 4 five commitments are verbatim against the Constitution (Version 2.3 text), apart from straight versus curly quotes.
- The census `floorNote` ("No question"), the `voices` women's-side quote, the `legacy` field reference, and Wittenberg's "Built & Live" status (`Build/worlds/witt`).
- Society of Jesus is "Pre-Survey Candidate."
- The dossier path exists.
- The *Founders* quotes and line anchors are correct within a few lines.
- The Acquoy codex description (line ~889).
- The Benham "erroneous notion" quote.
- The Xavier line anchors.
- The census `relationsSummary` wording, apart from the dash.

## Disposition

Per `cic-build-cycle`: R2-S1 to R2-S3 are errors, not thoroughness points. They need one more targeted revision, which will be Round 3, the last before the cap requires escalation.

**For Mark, on the cap.** R2-S1 and R2-S2 come from events after Revision 2 was drafted: Mark's library ruling, and the 40-source vendoring pass. R2-S3a comes from this reviewer's own Round 1 S4. None shows the revision loop failing to close. Mark may want to treat them as refresh work rather than as a third substantial round against the drafter.

**The S5 question does not need a new ruling from Mark.** His 2026-09-25 library ruling already answers it, and cd63bbab has applied it to the Groote letters. Round 3 should apply the ruling and cite it, not keep asking.

The Round 3 recheck should be limited to R2-S1 to R2-S3 and R2-M1 to R2-M6.

**Outside this document (flagged, not touched):**
- The Round 1 review files and the Benham header fix are stranded on an unmerged branch (R2-M5).
- The corpus-map's Groote entry has "fourteen letters" and inline correction narration (R2-M6).
- The Hussite Step 0 has the conflicting selection account (R2-M3).
