# Card check 2: The Roman Church in the Third Century

Checked: `roman-church-third-century.card.json` and `Card_Edits.md` (with its "Changes after the grade fixes"), against `Card.existing.json`, the final brief `roman-church-third-century.brief.txt`, `Outline.md`, `Review.md`, `Fresh_Read.md`, the grade-fix files and the earlier `Card_Check.md`, with CLAUDE.md ("Trust and source fidelity"), Kit Part 1, `kinds/tradition.md` and the role. The checker did not write the card.

**Verdict: PASS.**

## The earlier check's corrections

All twelve FIX items in `Card_Check.md` are applied word for word, and nothing else moved with them:

1. `legacy`: "... against the Arians, who held that the Son of God was a creature." Ath 28469 re-read.
2. `documentedStories[0].text`: "to manage the church’s cemetery, and on Zephyrinus’ death he became bishop." H 13802-13806 and 13816-13819 re-read. The Appian Way is only the editor's note at 13805-13806.
3. `documentedStories[0].text`: "he said he forgave all their sins, sins of sensual pleasure among them; he let women of rank count a companion, slave or free, as a husband;". H 13873-13875 and 13934-13938 re-read.
4. The "pastoral policy" sentence is gone.
5. "Hippolytus was eventually exiled to Sardinia, in 235;". LibCat 66805-66808 re-read: Pontianus and "Yppolitus presbyter" were deported to Sardinia, with no mines and no death.
6. The catacomb sentence is gone from `documentedStories[0].caveat`.
7. `documentedStories[0].sources[1].note` is as given.
8. "had spent his time as bishop repairing the breach". E 41758 ("eleven years") and LibCat 66908-66911 re-read.
9. "underground burial galleries where". H 41184-41186 ("in the cemetery") re-read.
10. "He was himself arrested within the month." is gone.
11. `voices[5]` is as given. LibCat 66915-66917 re-read.
12. The sentence on "second- and third-century religious movements" is gone from both `why` and `legacy`.

## Against the final brief

- **Check 2 (nothing else moved).** A field-by-field diff against `Card.existing.json` shows changes only in `why`, `sourcing`, `teaser`, `voices`, `legacy` and `documentedStories` (both stories' `text`, story 0's `caveat` and both `sources`/`modernWorks`), plus the new `uncertain`, `sources` and `quotationOriginals`. Each change is listed in `Card_Edits.md`. `floorNote`, `relationsSummary`, `people`, both stories' `title`, `when`, `tier`, `verification` and `teaser`, and story 1's `caveat` are word for word.
- **Edit 13 (why).** The brief now says only "Callistus, who had been a slave". The mines are Leave out (Outline, Cut first 24). So the edit is justified.
- **Edit 14 (Hartel note).** CyL 6748 with 6776 ("circumuentos se esse / adfirmarunt", with the apparatus between them), CyL 6831-6832 ("circumuenti sumus") and H 32980-32981 ("they affirmed that they had been deceived") were re-read. Each one matches the brief's "saying they had been deceived".
- **Check 1 (items sent to the card).** Outline Cut first 24 (the cemetery) is in the Hippolytus `sources` note. Cut first 27 (Natalius's welts) is in `uncertain`, and the visions and angels it names agree with the brief's "A writer of his day says ...". Cut first 20, 22, 23, 25, 26, 28, 29 and 31 are in the `sources` notes as listed. Every other grade-fix cut is Leave out. No modern opinion, date or identification enters the new wording. Brent and Moss stand only in `modernWorks`, and each note says what the work covers.
- **Check 3.** The card has no `briefReferences`.
- **Check 4.** The final brief quotes three spans, and the card has one `quotationOriginals` entry for each. Each `modern` matches the brief word for word. I re-read each `printed`/`englishPrinted` and found it verbatim at its lines:
  - Q1: H 13856-13857.
  - Q2: CyL 1129-1133 and H 28856-28860.
  - Q3: CyL 6825-6828 and H 33011-33016.

  Both files are in `sources`. Q1 has no held Greek, so its English stands alone, as its `uncertain` says. The card names no audit, review or ruling, and it uses American spelling.
- **Check 5.** No quote is under six words, so none is "checked at card" and none carries `secondReading`.
- **Census run.** I made a scratch census copy outside the repository, with the card merged into the entry and the final brief as `longDescription`. `node tools/validate-census.mjs <copy>` gives 629 movements, 736 edges, 10 eras, 0 errors and 4 warnings. All four warnings are short names on other entries. The real census was not edited.
- **Check 7.** This is a tradition entry and there is no new census entry, so there is nothing to check.

## Noted, no change

- `documentedStories[0].teaser` ("written by the man who set himself up against him") is unchanged from the starting card. Read plainly, it says he opposed Callistus, which H 13627-13633 supports ("withstood him"). It does not name him as a rival bishop, so it stays.
- `teaser` ("Rome between 200 and 260") spans the tradition's own years, and the census runs to 268. The legacy's 260s material comes in at that date. The teaser does not contradict the brief, which ends at 251.
- The claims `Card_Edits.md` still lists as not found stay in place, as the role says. These are "grave sin after baptism", "two questions", "That is the answer the Western church kept", "Hippolytus wrote his Refutation to discredit Callistus", "Rome venerates both as saints", Xistus "seized while presiding", Damasus's inscription and Lawrence "four days later".
- The items `Card_Check.md` noted and held still stand. Stephen and Aurelian are for the connections pass. The finding-aid studies (Duchesne, Harnack and the rest) are for the researcher to name before release.
