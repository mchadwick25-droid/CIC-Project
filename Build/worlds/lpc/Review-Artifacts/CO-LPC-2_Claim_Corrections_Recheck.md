# CO-LPC-2 Claim Corrections: Targeted Recheck

**World:** `lpc`
**Scope:** Change order CO-LPC-2 (`lpc_Decision_Log.md`, 2026-10-24), the corrections to the 22 claims found false or overstated in Phase L2. Only the changed lines, the sites that repeat each claim, and the 22 new UNVERIFIED Claims Register rows were checked.
**Authority:** System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-2, one recheck of the claim corrections" (2026-10-24). This file is the one review that ruling covers.
**Reviewer model:** Opus 5.5 (`claude-opus-5-5`) for the whole run. No fallback to another model occurred.
**Date:** 2026-10-24
**Inputs:** the uncommitted `git diff` across 30 files; the false-claims evidence file from Phase L2; the cited `cic/texts/` lines, each read directly.

**Gates run:** `python -m engine.m10.cli regate lpc` gives PASS: 8 new or edited fields, no regression. `python -m engine.m10.cli claims lpc` gives PASS: 94 derived, 94 registered, 22 UNVERIFIED. `tools/check_live_commentary.py --surface records` reports 0 hits.

Severity: **P0/P1 block**. P2 does not block.

---

## Batch A

### 5c06ab34: Possidius's visibility (Doc_02 line 59)

Corrected. Possidius is a named co-sender of Ep. CLXXVI (`augustine_epistulae-124-184a-lat_goldbacher-csel44.txt` line 35938) and Ep. CLXXVII (address lines 36299–36301; his name is on 36301). The *Indiculus* is described in the Weiskotten notes (lines 3089, 5625) as printed in PL 46, which is not vendored. The correction is true at source and no wider than the evidence.

- **P2.** The cited line "36300" holds the start of the address, not the name. Proposed: "lines 35938 and 36299–36301".

### 40334bfa, 7ee09661, 09e32fac, 1b8bdab8, 12785a57: "formed by, or even aware of" (Doc_04, Doc_05 ×2, Doc_06, Doc_07)

Corrected at all five sites, and carried to Doc_06, lpclex012, the three Representative phase files, the World Profile (five sites), `lpc.term.bishop-of-bishops` and `lpc.gravity.conciliar-authority-theory`. A grep for "aware of", "knew of" and "reached ordinary" across `Build/worlds/lpc/` and `records/lpc/` finds no G5 leftover. The attendance clause matches ANF05 lines 56852–56855 ("together with the presbyters and deacons, and a considerable part of the congregation who were also present") and Hartel line 109 ("praesentibus etiam plebis maxima parte"). True at source. No finding.

### f9dafd30: each theory "at one locus" (Doc_04 Persistence)

The Doc_04 Persistence, Repetition, §4 table and §5 lines are corrected. So are Doc_05 line 305 and the gravity record. Epp. LXXI (to Stephen, ANF05 line 38405), LXXII (to Jubaianus, line 39018) and LXXV (to Magnus, line 40604) each state the freedom of each bishop's judgment, as cited. True at source.

- **P1. Four sites still state the one-locus claim.**
  1. `Doc_04_Gravity_Discovery.md` line 111 (Candidate 6 Repetition). Current: "Not confined to one locus the way Candidate 5 is — argued across two independent bishops' own extended treatments, decades apart." Proposed: "Not thin the way Candidate 5 is — argued at length in two independent bishops' own extended treatments, decades apart."
  2. `lpc_World_Profile.md` line 126. Current: "attested in both phases but at one locus each, a century apart". Proposed: "attested in both phases, each theory in one bishop's own voice, a century apart".
  3. `Representative/lpc_Rep_Phase2_Formation_Calibration.md` line 64. Current: "one attested locus per phase, a century apart". Proposed: "each theory in one bishop's own voice, a century apart".
  4. `Representative/lpc_Rep_Phase1_Ecology_Assessment.md` line 96. Same current text. Same proposed text.
- **P2.** Ep. LXXI is a synodal letter from Cyprian and the council, so "each in his own voice" (Doc_04 line 90) is loose for that one letter. Proposed, optional: "each in his own voice or his council's".

### a187ea83: rite wording "not attested" (Doc_05 line 165 construction note)

The two spoken exchanges are now named, and both are at source: the interrogation at ANF05 line 38062, the renunciation at `npnf108_augustine-exposition-psalms.xml` line 17698 (Psalm LXXXI §18). The correction still leaves the note false, in two ways.

- **P1. Order and gestures are attested in this build, and the note says they are not.** `lpcctx001_the-making-of-a-catechumen.md` verifies the signing and salt at entry and the creed taught before the Lord's Prayer, handed over and given back (Augustine's phase; the salt is *Confessions* I.11, `npnf101_augustine-confessions-letters.xml` line 4431). `lpcctx003_what-the-water-seals.md` verifies the anointing and the imposition of hands (Cyprian's phase; ANF05 lines 38074, 38620). Doc_05's own rendered passage at §3.2 supplies an order ("we teach you the creed before you are given the water ... and you say it back"). The new tail "each attested in its own phase only" is also wider than the evidence. Augustine confirms the question about the Church was still put at baptism in his day (*On Baptism* V.20.28, `npnf104_augustine-anti-manichaean-anti-donatist.xml` line 13058). Only the exact wording is single-phase.
  Proposed replacement for the text from "**beyond two fixed spoken exchanges" to "each attested in its own phase only.":
  > **beyond what this build's context chunks verify, the full order, gestures and setting of the rites at Carthage or at Hippo are not attested in anything this build has verified** (Doc_02 §5, §9 items 2 and 9), and nothing beyond those chunks is supplied. The chunks verify the signing and salt at entry and the creed handed over and given back, from Augustine's phase (`lpcctx001_the-making-of-a-catechumen.md`); the interrogation Cyprian quotes (*Ep.* LXIX §2, `cic:anf05_hippolytus-cyprian-caius-novatian.xml:line38062`) and the renunciation Augustine re-performs (*Exposition on Psalm* 81 §18, `cic:npnf108_augustine-exposition-psalms.xml:line17698`), each quoted word for word in one phase only (`lpcctx002_the-questions-at-the-water.md`); and the anointing and laying on of hands after baptism, from Cyprian's phase (`lpcctx003_what-the-water-seals.md`). Augustine also confirms that the question about the Church was still put at baptism in his day (*On Baptism* V.20.28, `cic:npnf104_augustine-anti-manichaean-anti-donatist.xml:line13058`).

### 6c30b049, 56dcc3b1: presbyters "almost exclusively" faction, ordinary work "essentially unattested" (Doc_07 line 126)

Corrected. Ep. XXXV leaves Cyprian's own portion for needy strangers "with Rogatianus, our fellow-presbyter" (ANF05 lines 32152–32153). Ep. IV has "the presbyters also, who there offer with the confessors" (line 28984). Both are set in persecution. True at source.

- **P2.** The sentence after the new glimpses ("That is a real distortion in the institutional picture") now points back to the loyal presbyters, not to the faction picture. Proposed: "The faction picture is a real distortion in the institutional picture." The World Profile already uses this wording.
- **P2.** `Doc_05_Ecological_Reconstruction.md` line 69 (lens table) still says "in Cyprian's phase presbyters appear mostly as a faction". Proposed: "appear most visibly as a faction", which matches Doc_05 §5.4 and Doc_07.

---

## Batch B

### 77d40657: grace "no evidence ... in Cyprian's phase ... not a gap in the search" (gravity record)

The record is corrected, and the corrected wording is true. *Testimonies* III.4 is in Native Registry row 5: "That we must boast in nothing, since nothing is our own" (ANF05 line 53424; Latin, Hartel `cyprian_testimoniorum-...` line 3300). Augustine quotes those words against the Pelagians in *Against Two Letters of the Pelagians* IV.25–26 (`npnf105_augustine-anti-pelagian-writings.xml` lines 18057–18106) and *On the Predestination of the Saints* 7 (line 20912). The quotation in the record matches word for word.

- **P1. The same claim still stands at nine other sites.**
  1. `Doc_04_Gravity_Discovery.md` line 131 (Explanatory). Current: "— no Pelagian-anthropology-equivalent material is identified anywhere in Cyprian's own corpus, since the Pelagian controversy postdates Cyprian by over a century." Proposed: "— no Cyprian-phase text is organized around the question, since the Pelagian controversy postdates Cyprian by over a century. Cyprian states the theme only in passing (*Testimonies* III.4, "That we must boast in nothing, since nothing is our own", `cic:anf05_hippolytus-cyprian-caius-novatian.xml:line53424`), and Augustine later quoted it against the Pelagians (`cic:npnf105_augustine-anti-pelagian-writings.xml:line18057`)."
  2. Doc_04 line 132 (Persistence). Current: "(no Cyprian-phase evidence identified in this world's own Native corpus)". Proposed: "(no Cyprian-phase text organizes formation around it; Cyprian states the theme only in passing, *Testimonies* III.4)".
  3. Doc_04 line 169. Current: "— no Cyprian-phase evidence is identified —". Proposed: "— no Cyprian-phase text organizes formation around it —".
  4. `Doc_05_Ecological_Reconstruction.md` line 209. Current: "and no Pelagian-anthropology-equivalent exists anywhere in Cyprian's corpus, because the controversy postdates him by over a century. That is a real temporal boundary, not a gap in the search." Proposed: "Cyprian states the theme in passing (*Testimonies* III.4), and Augustine later quoted him against the Pelagians, but nothing in Cyprian's phase organizes formation around it. The controversy postdates him by over a century."
  5. `Lexicon-Chunks/lpclex007_grace.md` line 63. Current: "No Pelagian-anthropology-equivalent material exists anywhere in Cyprian's corpus, because the controversy postdates him by over a century — a real temporal boundary, not a gap in the search." Proposed: "Cyprian states the theme in passing (*Testimonies* III.4: "That we must boast in nothing, since nothing is our own"), and Augustine later quoted those words against the Pelagians. But nothing in Cyprian's phase organizes formation around it, because the controversy postdates him by over a century."
  6. `records/lpc/term/lpc.term.grace.md` line 88 (`senses.evidential`). Current: "This term belongs to Augustine's own phase; no Pelagian-anthropology-equivalent material exists anywhere in Cyprian's corpus, since the controversy postdates him by over a century." Proposed: "This term belongs to Augustine's own phase. Cyprian states the theme in passing (Testimonies III.4), and Augustine later quoted him against the Pelagians, but the controversy postdates Cyprian by over a century."
  7. `lpc_World_Profile.md` line 140. Current: "no Cyprian-phase evidence exists in this world's Native corpus, since". Proposed: "no Cyprian-phase text organizes formation around it (Cyprian states the theme only in passing, *Testimonies* III.4), since".
  8. `Representative/lpc_Rep_Phase2_Formation_Calibration.md` line 58. Current: "no Cyprian-phase evidence exists in this world's Native corpus". Proposed: "no Cyprian-phase text organizes formation around it; Cyprian states the theme only in passing, *Testimonies* III.4".
  9. `Representative/lpc_Rep_Phase3_Voice_Construction.md` line 55. Current: "with no Cyprian-phase evidence in this world's own Native corpus." Proposed: "with no Cyprian-phase text organizing formation around it; Cyprian states the theme only in passing (*Testimonies* III.4)."
- **P2.** `lpc.force.transmission-asymmetric-span-133-year-silence` description: "Grace and human incapacity shapes only the second." reads as a grammar slip. Proposed: "The concern with grace and human incapacity shapes only the second."

### 48fee228: "Nowhere ... does Augustine answer directly whether Constantine corrupted what we were" (spoken witness)

The fix is carried to the witness's `text`, `positions`, `tensions` and sources, to `lpc.witness.blamed-for-the-worlds-troubles`, to `lpc.limit.the-outsiders-own-view` and to `lpc.source.augustine-answer-to-petilian`. I read §§202–205 in full (`npnf104_augustine-anti-manichaean-anti-donatist.xml` lines 17610–17726, NPNF Book II ch. 93). Each statement checks:
- Petilian's charge, "what have you to do with the kings of this world, in whom Christianity has never found anything save envy towards her?", is at §202.
- "commit no sin if they make a right use of that friendship" is at §203, with "if any are elated by it, they yet sin far less grievously than you".
- "certainly no foe to the name of Christian, but rather rendered glorious by it ... deciding most justly on behalf of His unity" is at §205.
- "Petilian's own side had asked Constantine to judge ... and he ruled against them" holds. In §205: "even when you yourselves appealed to him"; "on your ancestors making their petition, Constantine had given an episcopal judgment both at Rome and at Arles ... from the other you appealed to him"; "Constantine ordered that the basilicas should be taken from you".

"His unity" glossed as "the unity of Christ" follows the antecedent ("the hope which he maintained in Christ"). The quotations are word for word. The new text keeps the world's voice ("our bishop", "us"), discloses Augustine's partiality, and has no AI tells. FK 8.3 / FRE 66.8 (`text`), 8.6 / 64.6 (`positions[0]`), 5.1 / 82.1 (`tensions[0]`).

- **P1. The Source Registry and Doc_02 still license only §51 of this work.** The witness's new locus has no Registry licence. Row 14 says "this row licenses that one locus only". Row 280 says "The one locus of the work this world relies on, Book II, chapter 51 (section 118), is licensed at row 14". Doc_02 line 29 says "Registry row 14 draws on it for one specific claim". The source record now says Confidence A covers two passages.
  - Row 14, Source/Licence cell. Replace "; this row licenses that one locus only." with: "; and **Book II, chapter 93 (sections 202–205)**, where Petilian charges that Christianity "has never found anything save envy" in the kings of this world and Augustine answers that Constantine was "certainly no foe to the name of Christian, but rather rendered glorious by it," grounding `lpc.witness.constantine-did-not-corrupt`; this row licenses those two loci only." Add to its Verification cell: "**Book II, chapter 93 (sections 202–205) directly verified** against the same file, lines 17610–17726."
  - Row 280. Replace "that row 14 carries on one locus only" with "that row 14 carries on two loci only". Replace "The one locus of the work this world relies on, Book II, chapter 51 (section 118), is licensed at row 14 on its own footing" with "The two loci of the work this world relies on, Book II, chapter 51 (section 118) and chapter 93 (sections 202–205), are licensed at row 14 on their own footing". Replace "its structure and one locus were checked" with "its structure and two loci were checked".
  - Doc_02 line 29. Replace "Registry row 14 draws on it for one specific claim: Book II, chapter 51 (section 118), where Augustine answers Petilian by naming the chair of the Roman Church, in which Peter sat, and which Anastasius fills to-day, grounds `lpc.witness.apostolic-succession-of-bishops`; the quoted sentence is verified at source." with "Registry row 14 draws on it for two specific claims. Book II, chapter 51 (section 118), where Augustine answers Petilian by naming the chair of the Roman Church, in which Peter sat, and which Anastasius fills to-day, grounds `lpc.witness.apostolic-succession-of-bishops`. Book II, chapter 93 (sections 202–205), where Augustine answers Petilian's charge against friendship with kings by calling Constantine "certainly no foe to the name of Christian", grounds `lpc.witness.constantine-did-not-corrupt`. Both are verified at source."
- **P2.** In the witness record, `retrieve_when` item 2 says "needs the one sub-question of the four that our own record does answer". Two sub-questions are now answered, one by this record and one by the Demetrianus witness. Proposed: "needs the Constantine sub-question of the four, which our own record answers".

### 8c8ff86b: presbyters "almost exclusively as faction" (World Profile line 224)

Corrected. Ep. XXXVII is addressed "to Rogatianus and Numidicus, his fellow-presbyters", and has "I sent you as my substitutes to discharge the necessities of our brethren, with funds" (ANF05 lines 32247–32258). In Ep. XXXIV Numidicus "should be appointed in the number of Carthaginian presbyters" (line 32099). "Enrolled" is more exact than "ordained", and right. No finding.

### 7a0e9082: "relief work leaves no documents" (lpcstory002)

Corrected. Pontius, *Life* 9–10 (ANF05 lines 27939–27992), is the one account of the plague relief. Ep. XXXV and the ransom letter record other relief. No finding.

### a5bad882: "a pastoral problem the treatises never name" (lpcstory003)

Corrected. *On the Mortality* 17 (ANF05 lines 47068–47071) consoles one who "had been prepared for confession ... [and is] deprived of martyrdom, in that I am anticipated by death". "Touch only from the other side" is fair.

- **P2.** The new text repeats itself: "a man who survived the fire and did not want to. He did not want to be alive." Proposed: "Numidicus is the reverse case: he survived the fire, and he had not wanted to. Ordination is Cyprian's answer to that: here is why you were left behind."

### 31abcdcc: 2B-4 "the only force ... carries formation logic across the 133-year silence", "attested twice" (Doc_08)

Corrected at Doc_08 lines 191, 278 and 302, the Force Index (lines 30, 34, 91), Doc_09 line 119, World Profile lines 184, 366 and 768, and both force records. The new instance is true at source (npnf105 lines 18019–18106, 20912). Possidius quotes *De Mortalitate* at Weiskotten lines 3877–3878.

- **P1. Two World Profile sites still say "twice" or name only two instances.**
  1. `lpc_World_Profile.md` line 428. Current: "Continuity across the gap is textual, not successive — established by the force above and by Possidius quoting Cyprian's *De Mortalitate*." Proposed: "Continuity across the gap is textual, not successive — carried most fully by the force above, and also by Possidius quoting Cyprian's *De Mortalitate* and by Augustine's anti-Pelagian citations of Cyprian on grace (2A-4)."
  2. `lpc_World_Profile.md` line 652. Current: "attested twice: Augustine engaging Cyprian's conciliar acts, and Possidius quoting Cyprian's *De Mortalitate*." Proposed: "attested more than once: Augustine engaging Cyprian's conciliar acts, Possidius quoting Cyprian's *De Mortalitate*, and Augustine's anti-Pelagian works citing Cyprian on grace."
- **P1. The new clause "the only one that engages Cyprian's conciliar acts" is a new exclusivity claim, and the world's own record contradicts it.** Force 2A-3 (the Donatist schism) is the Donatists' appeal to those same acts (Doc_08 lines 135 and 298; `lpc.force.donatist-schism` "appeal to Cyprian's conciliar acts"). What only 2B-4 does is have this world itself read and answer them. Proposed at each site:
  1. Doc_08 line 191: "and the only one that engages Cyprian's conciliar acts" becomes "and the only one in which this world itself reads and answers Cyprian's conciliar acts".
  2. Doc_08 line 302: the same replacement.
  3. `lpc_Force_Index.md` line 91: the same replacement.
  4. `lpc_World_Profile.md` line 366: the same replacement.
  5. `records/lpc/force/lpc.force.augustine-engagement-cyprian-conciliar-acts.md`: "It is also the only one that takes up Cyprian's council acts." becomes "It is also the only one in which this world itself reads and answers Cyprian's council acts."
- **P2.** At Doc_08 line 191, "This force is the instance the matrix carries as a crossing, not the whole of it" now sits beside a second crossing in the matrix (2A-4). Proposed: "This force is the crossing 3B-2 records; 2A-4 carries a second strand, and the Possidius instance is not a force."
- **P2.** The `lpc.force.augustine-engagement-cyprian-conciliar-acts` line "This placement was checked, not simply inherited." is build narration in a canonical record, and this change edited it. Proposed: delete the sentence.
- **Spoken-field question.** "Cyprian's book on dying" in the 3B-2 record, for *De Mortalitate*, is acceptable. It is plain and accurate, since the treatise is about how a Christian faces death, and it does not mislead. Naming the work by title is not required in a `description` field.

### 75d73052: "the sole textual ground" (lpc.term.bishop-of-bishops)

Corrected to "the principal textual ground of the Cyprianic pole". "Principal" rather than "sole" is right, because Epp. LXXI, LXXII and LXXV restate the formula. lpclex012 has 0 hits for "load-bearing" and "evidentiary weight". No finding.

### 94dc0428: "No text authored by a woman survives" (lpc.limit.womens-own-voice)

The Therasia evidence checks out. NPNF Letters XXV, XXX and XCIV (lines 24531, 25665, 39400) and Goldbacher (`augustine_epistulae-1-123-lat_goldbacher-csel34.txt` lines 3976, 4252, 6719, 33368) name "Paulinus and Therasia". The letters are largely in Paulinus's first person.

- **P1. The new wording is wider than the old and wider than the evidence.** "No text in a woman's own voice survives" is false against a Native text. The *Passion of Montanus and Lucius* 8 (Native, Registry rows 269 and 270) gives Quartillosia's own first-person account of her vision: "quae in hunc modum quod uidit exposuit. Vidi, inquit, filium meum..." (`cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` lines 5771–5783; also `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` line 7655). Men wrote the text, but the voice is hers. The defensible claim is about authorship. Proposed `why_sources_cannot_answer` tail:
  > No text a woman wrote herself survives anywhere in this world''s own Native corpus, in either phase. The nearest are letters Paulinus of Nola sent to Augustine in his own and his wife Therasia''s names (Letters XXV, XXX and XCIV), which he writes largely in his own first person, and a few women''s words that men set down, such as Quartillosia''s account of her vision in the Passion of Montanus and Lucius (ch. 8).
- **Outside this change order; it should be logged in `Open_Gaps_Tracking.md`.** The same record's spoken `statement` ("Women appear throughout our own record and never narrate it ... None of them is audible") and Doc_09 §5 item 4 run against Quartillosia's narration. This is not a CO-LPC-2 correction and does not count toward this verdict. It is a participant-facing absolute that needs its own check.

### c7aafc6f: Possidius "the sole source" for Phase Two's story (lpc.figure.possidius)

Corrected, and consistent with the story record's Prosper locus.

- **P2.** Prosper also records that Augustine was still answering Julian's books at the end, "in ipso dierum suorum fine respondens" (`prosper_chronica-minora-1-lat_mommsen1892.txt` lines 54206–54212), so "corroborates only the death, its date and the siege" is slightly narrow. Proposed: "(Prosper's Chronicon corroborates the death, its date and the siege, and adds that he was still answering Julian, but says nothing of the sickroom)".

### d730e7a3: Duval, "this Registry's entire material-evidence layer" (record and Registry row 60)

Corrected at both sites. Registry rows 63 and 82 are type M and licensed for row 38. No finding.

### 8fdddf7d: Granfield, "which no other row addresses at this level" (record and Registry row 113)

Corrected at both sites. Row 186 (Norton, 250–600) and row 101 (Bobertz) read as described. No finding.

### 68a02b2a: subsellia tag "registered nowhere else" (Doc_08 line 474)

Corrected. OG-22 carries Doc_07 Round 2 NEW-L4. `L0_Docs03-05-06-07_Recheck_2026-10-23.md` line 108 reads "In OG-22". No finding.

---

## Claims Register: the 22 UNVERIFIED rows

Each row was checked at source per `Claims_Register_Template.md`. The completed rows are at `/tmp/claude-0/-home-user-CIC-Project/9b5d8278-a95d-517b-9c50-6f34185a4ec1/scratchpad/claims_C_done.md`: 7 columns, with `id`, `file` and `claim` unchanged, and every cited path exists.

- **Completed: 20.** 4 VERIFIED (6a216d81, 258ed6f3, 45ebd3b9, 54a194ae) and 16 JUDGEMENT. The fourteen "formed by" rows rest on one named reading: a search of Doc_02 plus the 256 preface. That shows presence and nothing about formation.
- **Left UNVERIFIED: 2, because each is false or overstated at source.**
  - 7cc4ac26 (Doc_05 construction note): see a187ea83 above.
  - d3480c4b (`lpc.limit.womens-own-voice`): see 94dc0428 above.

  When these two are reworded, their ids change and the new rows need checking.

## No new error

Every changed sentence was read in full. No sentence is broken. The new process narration is the one P2 at the 2B-4 record (a sentence the change edited, not one it added). The new claims are the ones raised above: "the only one that engages Cyprian's conciliar acts" and "each attested in its own phase only" (both P1), and "corroborates only" (P2). Every quotation added in a spoken field is word for word.

---

## Counts

- Claims checked: 22. Fully corrected and true with no blocking finding: 16. Carrying a P1: 6 (f9dafd30, a187ea83, 77d40657, 48fee228, 31abcdcc with two P1s, 94dc0428).
- **P0: 0. P1: 7.** P2: 10.
- Claims Register rows completed: 20 of 22.
- Gates: regate PASS; claims PASS.

VERDICT: Substantial revision required
