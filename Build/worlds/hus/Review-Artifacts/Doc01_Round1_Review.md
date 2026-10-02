Simulated review — informational only, not an Article 31 substitute.

# Doc_01 World Identification, Boundaries and Orientation: Round 1 full review (hus)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** hus build-thread drafting worker (commits a1cefcb61 and 06551b798; commit trailers read "Claude Sonnet 5.5")
- **Round:** 1 (full review of the first draft)
- **Truncation check, method 1:** structural count. Headings §1 to §10 are all present and in order (lines 13, 25, 59, 72, 85, 110, 128, 150, 172, 188). The strand table has six lines with five cells each; the forces table has five lines with four cells each. The file has 190 lines and ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 06551b798. `wc -c` equals `git cat-file -s` (33,790 bytes), and `git hash-object` equals `git rev-parse HEAD:<path>` (5f098bc8…). The file has no uncommitted changes.
- **Date:** 2026-09-30
- **Document:** `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md`, as committed at HEAD 06551b798
- **Governing inputs used:** `Step0_Movement_Scope_Confirmation.md` (Approved to proceed) and its §4 items; `Step0_Review_Round3.md` finding R3-m1; Construction Framework V7.4 Part I (read from the docx); Constitution V2.3 Articles 4, 21, 22 and 29 (read from `CiC_L1_Constitution_V2_2.docx`, whose internal text is V2.3); `Build/worlds/rzg/Doc_01_World_Identification_Boundaries_Orientation.md` as the finished form.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear. Substantial revision required.** 0 P0, 8 P1, 12 P2.

The document is complete against Part I of the Framework, and most of it is well sourced. Of about 75 quotations checked at source, all but one match the vendored text, allowing for OCR spacing and line-break hyphens. R3-m1 is applied correctly. The Article 4 check extends Step 0's check as §4 item 1 requires, and its evidence is real. The live-commentary check is clean.

The eight P1 findings change claims, confidence ratings or the argument for scope. Two are factual errors against the world's own tradition voice: the claim that the cup was "not Hus's own concern", and the description of Letter VI. One leaves out in-window evidence that the Unity's majority gave up strict non-resistance. Two concern the one-world, three-strand argument: the alternatives are under-argued, one ground is misdescribed, and the finding's status is inconsistent. Two concern confidence tags and the verbatim floor check. One is a claim of violence against Germans and Jews in 1419 that the cited source does not make.

None of the eight is disqualifying. Each can be fixed inside this document without reopening Step 0.

## Scope 1: template completeness

Checked against Construction Framework V7.4 Part I and against the `rzg` Doc_01.

- Distinct World Criteria (four questions): §3, all four answered.
- Temporal, Geographic and Cultural Scope: §2, all answered, including internal and transitional developments.
- World Separation Criteria (six questions): §4, all six run against the three parts, with evidence on both sides.
- Strand Determination: §5, finding recorded with named evidence per strand, as the Framework requires.
- Preliminary Forces Identification: §6, with the four questions and a Layer 1 six-cell sketch. Article 22's honest-ending rule is applied: no internal fracture closes the world in 1517.
- World Continuity & Distinction: §7 covers inheritance, transmission and adjacent worlds. The Framework's three further questions are not answered in so many words (P2-10).
- Living Tradition Status: §1, marked triggered, not confirmed, and left to the project lead.
- Step 0 binding items: §4 item 1 in §8; items 2 to 4 carried in §9; item 5 (window) in §2; R3-m1 in §2 and §1.
- Forces Framework Step 1 integration: present and substantive in §6.

## Scope 2: quotations and loci, checked at source

Every quotation was searched with whitespace and line-break hyphens normalised, then read in context. The script and the full hit list are not kept in the repository. All of the following match.

- **Workman–Pope, *Letters*:** the 1402 appointment (line 1440) and the chapel's Czech-preaching condition (1456); the note giving 1401 as Hus's first year of preaching (5440, note to Letter XVII); "intense nationalism … written in Czech" (3687, the note that introduces Letter XI); "the great schism" (1901); "Isti sunt sancti" (4558); the two Waldensians from Dresden and "the summer of 1414" (8804–8807); "monstrous article" (10938).
- **Hus's own letters:** XVII (5308), XX (5659–5660), XXI (5848), XXXIV (7591) and XXXIX (8332). Each quotation sits under the letter number the document gives.
- **Schaff, *De Ecclesia*:** p. 18 (line 3333), p. 34 (3973–3975) and p. 70 (5429–5433), with the running heads confirming each page. From the introduction: "three votes …" (593), the two hundred books burned in 1410 (586), "appropriated paragraph after paragraph" (1515), "did a man owe more to mortal teacher", the schism dates 1377–1415 (1916) and 1378–1417 (10132), and Loserth's revision after Flajšhans (1676–1679).
- **Gillett, Vol. II:** the Athanasian creed passage is on pp. 53–54 (2672–2713; the running head "63" is OCR for 53); the decree of 15 June 1415, ch. III (3850); the Four Articles, pp. 441–44; "scarcely differing" (17350); "pertained rather to moral conduct" (17527); the more than forty thousand at the Tábor assemblies (17657); no musical instruments, "undistinguished by garb", "brother and sister" (17703–17711).
- **Lützow, *Hussite Wars*:** "openly seceding" and "the moderate Utraquists always endeavoured" (3574–3575); "widely spread at Tabor" (5321); the Loquis burning (5308–5313); the Adamites (312–314, 5336); Nedoma, 1891 (5361); "Modern writers generally" (6325); Queen Sophia at the sermons (941).
- **Lützow, *Bohemia*:** the Rokycan passages (9505–9510); the Goll note (9416–9420); the Waldensian note (10066–10071); Kunwald near Žamberk (10096); "on insufficient evidence" (10100); the Great and Small parties (10111); Chelčický on bloodshed (10012) and the Real Presence (10041); 30 July 1419 (6525); the three town halls (10757–10761); the enactments of 1508 (11854).
- **Lützow, *Life and Times*:** Kybal (194); the forerunners (1270 onward); Tábor captured in 1452 (15477).
- **Seifferth:** the Barony of Lititz (164); 1467 (192–201); the 1504 Confession and the 1508 letters (289–292); the Preface's "genuine offspring of the holy martyr Huss" on p. 95 (4150–4152) and its "law of Christ" sentence (4157–4160); two hundred congregations (4131–4133); the signature "The Seniors and Ministers" (4299); the Apostles' creed (6275); the Trinity absolution (6403); the title page naming Seifferth "Bishop of the Brethren's Church".
- **Piccolomini:** the chapter heading *De perfida secta Hus[sitarum]* (3619); the German masters going to Leipzig (3677); the codices of Dionysius and Cyprian (3889); "Martyrum honores" (4087).
- **Luther:** the Wace–Buchheim safe-conduct passage (6960–6965), with the ellipsis dropping only "without attempting self-justification, and own one thing to the Bohemians, namely"; the same passage in Jacobs–Spaeth vol. 2 (4309); the Bacon–Allen hymn note (2771–2772).
- **Foxe:** the testimonial of Nicholas, bishop of Nazareth and inquisitor, "a faithful and a catholic man" (34383).
- **Nicene terms:** "begotten", "consubstantial", "giver of life", "third day" and "maker of heaven" do not occur in Hus's two works in the credal sense. "Begotten" occurs once in the *Letters*, about a son born to a woman. "One substance" occurs once in *De Ecclesia*, quoting Gregory on the church. The document's claim holds.
- **Census:** the V.6 fields quoted (`living`, `continuesAs`, `dates: "1415-1517"`, the Herrnhut and 1501 hymnbook claims, and "we are all Hussites without knowing it" in `legacy`) match. The Luther remark occurs in none of the nine vendored Luther files. The document's carrying of it as the census's own claim is correct.
- **Constitution V2.3:** Article 21's definition, Article 22's "situated against the forces" and "no internal fracture is attested" (519), and Article 29's "touches a tradition that continues into the present" (591) are verbatim. The Step 0 header's quotation of the five Article 4 commitments (lines 161–165) is verbatim.

The one quotation that does not match is at P2-1.

## Scope 3: the Article 4 check

Every locus in §8 is real and says what the document says it says. Hus's own voice gives positive evidence on all five commitments, and the trial evidence is strong corroboration: Gillett, pp. 53–54, has Hus repeat the Athanasian article on the Trinity. The Taborite claims are also true at source. Gillett calls the Taborite articles moral, not credal (17527). Lützow reports Loquis burned over his views on Communion (5308–5313). Lützow calls the Adamites unconnected with Hussitism (5336). Nothing vendored shows a Taborite denial of a commitment. The Unity limit is stated honestly.

The defects are in how the check is written and scored (P1-7), not in its evidence.

## Scope 4: confidence tags

The five-level vocabulary is used throughout, and "Not Attested" is never used as a sixth level. The tags on the main contested questions are right:

- Hus–Wyclif: Widely Accepted for *De Ecclesia*'s textual dependence, Contested as an account of the movement.
- The Waldensian ordination of 1467: Contested.
- The Tábor–Unity link: Contested.
- The chalice's origin: Contested.
- The Unity's two hundred congregations: Inferential/Thin.

Three other tags are too strong (P1-6).

## Scope 5: decisions reserved to the project lead

- Living Tradition Status: correctly left open and assigned to the project lead.
- Representative identity: correctly not decided. §9 item 3 keeps it for a packaged choice.
- One world or two: correctly put to the project lead in §9 with three options and a recommendation.
- The three-strand call: stated inconsistently (P1-4).
- Nothing is attributed to the project lead.

## Scope 6: readability and live-file hygiene

- **Readability.** Scored with the engine's own grader (`engine.m7.turn_readability.score_turn`, markdown symbols stripped). Whole document: FK 9.2, inside the band; FRE 51.6, below the floor of 60. §1: FK 10.6, FRE 47.1. §2: FK 10.2, FRE 50.4. §5: FRE 44.0. §8 and §9 are inside the target. Thirty sentences run past 35 words, mostly the catalogue sentences in §2 and the Governed-by line. For comparison, the `rzg` Doc_01 scores FK 15.3 and FRE 26.7. See P2-11.
- **Hygiene.** `python tools/check_live_commentary.py --surface worlds` exits 0. Its only line for this file is PROTECTED (the §9 heading). No change history, review discussion or revision narration was found by reading. Status and Disposition state the draft status plainly.

## Findings

**P1-1. §3, candidate gravity 2 (line 64): "it was not Hus's own concern (§8), so it must not be attributed to him."**
- The vendored *Letters* contradict this. Letter LXXI to Gallus (Hawlik), from Constance (line 11980 onward), has Hus write: "do not oppose the sacrament of the Lord's cup, which was instituted of Christ". It also says: "prepare to suffer for the eating of the bread and the communion of the cup". Workman's note before Letter XLIII (8815–8818) says Hus "soon committed himself decisively to the opinions of Jakoubek". The index lists "Defence of the cup 242-6".
- Step 0 A1 kept the qualifier: he "committed to it only late, from prison." This document drops it and turns the point into a rule for later documents.
- The cross-reference is also wrong. §8 does not discuss the cup.
- Fix: the cup was not Hus's cause while he was in Prague. He took it up from prison in 1415 and defended it to the end. It became the movement's emblem through Jakoubek. Point to Step 0 A1 and the Letters.

**P1-2. §7 (line 132): "Letter VI, to the English Wycliffite Richard Wyche, was read out in the Bethlehem Chapel."**
- Letter VI is Hus's reply to Wyche. What reached the Bethlehem was Wyche's letter to Hus. Workman's contents line (389) reads "Hus's delight with Wyche's letter; He read it in the Bethlehem". In the letter itself (2679–2697), Hus tells a crowd of "nearly ten thousand" about Wyche's letter, and the people ask him to translate it into Czech.
- Fix: correct the sentence to say this.

**P1-3. The Unity's non-resistance is presented as a constant through 1517.**
- The claim appears in §1 (Core Identity, "refused the sword"), in §3 (gravity 6), in §4 ("Has a new gravity emerged? Yes") and in §5 (the table's "Personal discipline and pacifism").
- Lützow's *Bohemia* (10110–10124), vendored and cited elsewhere in this document, says the split into the "Great" and "Small" parties at the end of the fifteenth century was about exactly this. The "Small" party kept Chelčický's teaching, "which included doctrines such as non-resistance to evil-doers". It "soon became extinct". The "Great" party "reconciled itself with the world, and by partly abandoning its earliest principles secured the future existence of the 'Unity.'"
- §5 names the division but not its subject. That leaves the strongest separation ground in §4 and one strand marker in §5 overstated for the second half of the Unity's in-window life.
- Fix: state what the division was about and carry it into the gravity-6 candidate and the strand table.

**P1-4. The three-strand finding: the alternatives are under-argued, and the finding's status is inconsistent.**
- *Under-argued.* Option (b), Tábor as a phase of the Utraquist strand, gets one word in its favour: "simpler". Its real case is left out:
  - The document's own §1 says "Two bodies then developed: the Utraquist church … and from 1457 the Unity."
  - The census's continuation entry names two ("Utraquists and Unitas").
  - Tábor is a bounded phase of 1419–52, about a third of the window. Article 21 speaks of a pattern "within a single world", and §5 does not ask whether a time-bounded phase can be a strand.
  - The Taborite column rests on hostile or partisan witnesses. Lützow says Březová's "hatred of the Taborites was even intenser than his hatred of the adherents of the Church of Rome" (*Hussite Wars*, 5355–5357). Gillett's account of the Tábor assemblies is, in his words, "the Calixtine narrative" (17715).
  - Option (c)'s case is fairer, but it too leaves out the Unity's own claim to a separate identity, made against the "pseudo-Hussites, the Calixtines" (Seifferth 4089–4090).
- *Status.* §5 says, "The strand finding governs strand attribution in every later document." That treats the finding as settled. §9 item 1 puts the same finding (option a against b and c) to the project lead as "decisions, not made here." The Framework makes strand determination a Step 1 finding. Here, though, it is bound up with the one-world-or-two decision, and that decision is the project lead's.
- *Fix.* Give each option its strongest case. Mark the strand count as a recommendation pending the project lead's decision, as the `rzg` Doc_01 did before its confirmation was filed. Say that attribution in later documents waits on that decision.

**P1-5. Two grounds for "one world" are misstated.**
- §4 Finding (line 83) says "the census already treats V.6 and VI.24 as one movement with parts". It does not. The census holds them as two separate entries with different windows, eras and lanes, linked by `continuesAs`. That both entries include both bodies is a fact about portfolio structure. It is not ecological evidence, and under the build cycle's escalation rules it should be labelled portfolio-level.
- §4 (line 77) says "The cup, Scripture and the Czech language all continue in the Unity (the *Ratio*'s Preface)". The Finding repeats the point as "the cup and the Czech-language Scripture runs through all parts". The Preface names the law of Christ, but not the Unity's cup and not the Czech language. The cup appears only as the Calixtines' concession (4077) and later in the *Ratio*'s body (4881), as seventeenth-century practice. "Czech", "Bohemian language" and "mother tongue" occur nowhere in the volume.
- Doc_02 licenses the Preface only "for what the Unity later said about its own origins."
- Fix: restate both grounds at the strength the sources bear.

**P1-6. Three confidence tags are stronger than their grounds.**
- (a) §2 (line 53) tags the crusade count "Widely Accepted" because Lützow says "modern writers generally" count it this way. That is a remark of 1914 about the numbering of 1421 and 1427 only (6324–6326). "Cesarini's … campaign of 1431 is a fourth" is the drafter's extension. The census's own V.6 `teaser` says Bohemia "was crusaded against five times". The numbering varies. Tag it Contested and give both counts, or drop the count.
- (b) §5 (line 101) tags Lützow's view of the Adamites "Dominant Modern Reconstruction" while saying "later work is unchecked". That tag is a claim about modern scholarship, which this document has not consulted. Inferential/Thin or Contested fits the stated ground.
- (c) §4 (line 78) gives the Unity's household discipline "Dominant Modern Reconstruction, because our detailed evidence is from 1632/33". That ground argues for Inferential/Thin for the in-window period, not for the Dominant Modern Reconstruction tag.

**P1-7. §8, the Article 4 check: the five commitments are not quoted verbatim, and the result under-reports what is only partly evidenced.**
- Step 0's governing line requires the commitments "quoted verbatim wherever this document must characterize one". §8 characterises each in a paraphrased label that drops clauses:
  - 1 drops "maker of heaven and earth, of all that is, seen and unseen";
  - 3 drops "incarnate of the Holy Spirit";
  - 4 drops "bodily" and "on the third day".
- The Result says only commitments 2 and 5 are affirmed "in substance … not in the Nicene wording". On the evidence given, 3 ("incarnate of the Holy Spirit") and 4 ("bodily resurrection on the third day") are also shown only in part. "He rose again" and "born of the Virgin Mary" are real evidence, but not of those clauses.
- The floor still holds. This is about precision, not about the outcome.
- Fix: quote each commitment verbatim from the Constitution (lines 161–165 of the V2.3 text) above its evidence. State clause by clause what is shown. Correct the Result and the matching sentence in `Open_Gaps_Tracking.md` item 4.

**P1-8. §6, Cell 2B (line 125): "the recurring violence against Germans and Jews (1419 and the 1480s)".**
- The 1480s part is supported by Lützow's *Bohemia* (10757–10761).
- The 1419 part is not. The cited 1419 event (*Bohemia* 6525–6535) is the storming of the New Town hall, in which "the burgomaster and several of the town-councillors were thrown from the windows". Neither the passage nor the document's own §2 names Germans or Jews.
- A claim of violence against a named ethnic or religious group needs a source. Cite one or narrow the cell to what Lützow says.

**P2-1. §8 (line 162):** the quotation "the fourth person in the Trinity" sits next to Gillett, but those are Workman's words (*Letters* 10939–10940, "that he was the fourth person in the Trinity"). Gillett reads "the fourth person— now added— of the Holy Trinity" (2685–2686). Cite Workman for the phrase.

**P2-2. §8 (line 159):** "the Allpowerful" joins a scan line break, "All- / powerful" (5659–5660). The same edition prints "All-wise" (11095). Render it "All-powerful".

**P2-3. §2 (line 42):** "the Letters from Constance (XXXIX–LXXXII)". Letter XXXVII is dated "Constance, November 4, 1414" and precedes XXXIX. Give the range as XXXVII–LXXXII, or say which letters are meant.

**P2-4. §5 table and Unity bullet (lines 94, 102):** Lützow's "on insufficient evidence" is about Michael, curate of Žamberk, being "said to have been ordained by a Waldensian bishop" (*Bohemia* 10100–10101). Lützow gives no year. Say so rather than attaching the phrase to Seifferth's 1467 synod. The Contested tag stands.

**P2-5. §2 (line 54):** the two Rokycan quotations come from Lützow's *Bohemia* (9504–9510), but only the third, from *Hussite Wars*, names its work. Name *Bohemia* for the first two.

**P2-6. §3 (line 69):** "the peasant and the noble, the Czech speaker and the priest, all 'brother and sister'". Gillett has "The rich and the poor sat down together, and priest and layman were undistinguished by garb" (17708–17710), from "the Calixtine narrative". Keep to Gillett's categories.

**P2-7. §1 (line 17):** "a smaller, stricter body that later took the name *Unitas Fratrum*". Seifferth (172–174) says "At an early period of this association it assumed the name". Change "later" to match.

**P2-8. §2 (line 40) and §5, §8:** the identification of Gillett's *Diarium* with Lawrence of Březová's chronicle is the drafter's own. It is plausible, but it needs a confidence tag. Where Březová is used as Taborite evidence, name his anti-Taborite stance (see P1-4).

**P2-9. §5, links between strands (line 104):** the Unity's own Preface of 1633 praises Tábor, which "held out for many years, defending with the sword their purity of doctrine and their constancy in the faith" (Seifferth 4078–4084). This is the Unity's own later voice on the link. Carry it beside Goll.

**P2-10. §7:** the Framework's further continuity questions are not answered as such:
- what shared material functions differently here than in adjacent ecologies;
- where continuity masks change;
- where discontinuity masks continuity.
The material for an answer is already in §7. One short paragraph would do.

**P2-11. Readability:** FRE is 51.6 for the whole document and 44.0 for §5. Break up the catalogue sentences in §2 (lines 33, 57), the Living Tradition paragraph (line 23) and the §4 Finding (line 83). Each runs past 45 words.

**P2-12. §4 (line 76):** "following Chelčický's teaching that 'the absolute and unconditional sinfulness of bloodshed'" is not a sentence. Write "his teaching of 'the absolute …'" or rephrase.

## Not verified

- The identification of the *Diarium Belli Hussitici* with Lawrence of Březová's chronicle. The vendored text says only "the author was chancellor of New Prague".
- §7's "The Moravian setting later shelters Hutterites". No vendored source was checked.
- The present-day status of Lützow's and Nedoma's view of the Adamites, and of the crusade numbering. No modern scholarship is vendored. P1-6 rests on the grounds the document itself gives and on the census's own count.
- Gillett's footnote at 17680–17690 was read only far enough to confirm the *Diarium* citation and the "chancellor of New Prague" line, not in full.
- `Doc_02_Source_Ecology.md` §2 (the Seifferth mediation record) and `Open_Gaps_Tracking.md` were read only at the entries this document cites. They were not reviewed.
- The Framework's Step 1 entry in the Forces Framework V1.1 docx was not re-read. §6 was checked against Framework V7.4 Part I and Constitution Article 22.
- Hus's two works were not read end to end. Loci were checked by search and read in context, as in Step 0.

## Outside this scope, noted only

- `Doc_02_Source_Ecology.md`, `Source_Registry.md` and `Open_Gaps_Tracking.md` were drafted and committed (06551b798) before this document was reviewed or approved to proceed. The build cycle says a later document begins only after the earlier one reaches Approved to proceed. Any Doc_01 fix under P1-1, P1-3, P1-5 or P1-7 must be propagated to them. `Open_Gaps_Tracking.md` item 4 already repeats the §8 result that P1-7 asks to correct.
- The census V.6 `dates` field still reads "1415-1517", as §9 item 8 says. Its `teaser` also says "Bohemia, 1415 to 1517". Both belong to the project lead.
