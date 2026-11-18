# Targeted recheck 2: Gregory of Tours v3, Benedict of Nursia v3, and references.md

This is a recheck of changes only. I made no model calls and changed no repo file.

## 1. v3 against v2

**Gregory of Tours**
- **The blocking close is fixed.** It now reads "for his stands against Chilperic and Agilan, his is the only account we have."
  - It is true in the Library. Fredegar (krusch1888) has no Agilan and no Trinity decree. Fortunatus's poem to Chilperic concerns Berny, which the brief does not tell.
  - The earlier blocking finding is **cleared**.
- **"Learning was dying" is cut.** The lament now does that work alone, so the double beat is gone. Fine.
- **The tradition: "in the church of Merovingian Gaul."** The census supports it.
  - In cic-website/data/world-census.json, movement `merovingian-gallic-christianity` has the name "Merovingian Gallic Christianity", the informal name "The Church of Merovingian Gaul", the dates c. 480–620, and the region Gaul. Its `people` list includes `gregory-of-tours`.
  - Gregory became bishop in 573, inside that window. It is not overclaimed.
- **NON-BLOCKING (access).** "Merovingian" is a technical term the brief never introduces. The next sentence's "rival Frankish kings" glosses it only by implication. One way to fix it: "...in the church of Merovingian Gaul, ruled by Frankish kings of Clovis's line." Another is to let sentence 2 name them "the Merovingian kings".

**Benedict of Nursia**
- **"Loose living" is back inside Gregory's telling, and the Arian clause is dropped.** Both done. Fine.
- **The tradition: "and the early Benedictines of Italy begin with him."** The census supports it.
  - Movement `early-benedictine-italian-monasticism` has the name "Early Benedictine / Italian Monasticism", the informal name "The Early Benedictines", the dates c. 500–604, and the region Italy. Its `people` list includes `benedict-of-nursia`.
  - The census movement also lists Severinus of Noricum, who died in 482, and Eugippius. So the census tradition is wider than Benedict.
  - Still, "the early Benedictines ... begin with him" is literally true of Benedictines and does not claim the whole Italian monastic movement. It is not overclaimed. Fine.
- **NON-BLOCKING (rhythm).** Sentence 2 now runs about 41 words: "Gregory the Great tells of a young man ... who was sent to Rome to study and saw many of the students fall into loose living, so he left his books and his father's house." That is well past the pattern's ~25-word guide, and it chains "who ... and ... so". Split it at "study." and continue with "There he saw many of the students fall into loose living, so he left...". That keeps the detail inside his telling.
- **Opening craft.** "Around the year 500, Italy was ruled by Gothic kings" is now a bare setting line. It still opens as story, because the scene follows at once and Totila picks the Goths up later. Fine.

## 2. references.md

### Chapter numbers checked against the held files

| Citation | Held file and line | Status |
|---|---|---|
| Dialogues II.3 | gardner1911 l.3640, chapter "Three", the broken glass; twelve abbeys at l.3847, before chapter "Four" at l.3861 | Correct |
| Dialogues II.8 | chapter heading lost in OCR between "Five" (l.3909) and "Twelve" (l.4313); Cassino and Apollo at l.4163–4181 sit in the Florentius-to-Cassino chapter, which is II.8 in the standard numbering | Correct |
| Dialogues II.15 | l.4460 "Chapter Fifteen", Benedict's prophecy; the quote at l.4472 | Correct |
| Dialogues II.17 | l.4632 "Chapter Seventeen", "very Abbey to be now suppressed by the Lombards" | Correct |
| Dialogues II.31 | l.5210 "Chapter Thirty-one", Galla the Arian Goth under Totila | Correct (but now orphaned, see below) |
| Dialogues II.36 | quote at l.5567, just before "Chapter Thirty-seven" (l.5574) | Correct |
| Dialogues IV.30 | table of contents l.542; body l.7923ff | Correct |
| Dialogues II prologue, four disciples | l.3429 | Correct |
| Paul the Deacon III.1-2 | the quote is at Foulke l.5074, inside CHAPTER I (l.5059); CHAPTER II starts at l.5106 | **Wrong: should be III.1.** NON-BLOCKING |
| Miracles of Martin II.1 | arndt-krusch1885 l.46663–46665, LIBER II, c.1: "Sigiberto gloriosissimo rege duodecimo anno regnante", margin 573; Krusch confirms at l.391–392 | Correct |
| History I preface | Dalton l.339 | Correct |
| History I.38 | Dalton l.1286 | Correct |
| History V preface | Brehaut l.5139, "weary of relating ... the civil wars" | Correct |
| History V.31 (43) | Dalton l.10198 | Correct |
| History V.32 (44) | Dalton l.10362ff | Correct |
| History X.31 | Dalton l.22656ff | Correct |
| Rule ch.48 | Gasquet l.3109 | Correct |
| Rule ch.58 | Gasquet l.3535; quote at l.3595 | Correct |
| Rule ch.64 | Gasquet l.3896; quote at l.3960 | Correct |
| Rule ch.73 | Gasquet l.4267 | Correct |
| MGH Capitularia I no. 10 | Pertz l.2197, "KARLMANNI PRINCIPIS CAPITULARE", 742, with Boniface's letter "sexaginta vel septuaginta annos calcata" at l.2205–2206 | Correct |
| MGH Capitularia I no. 11 | Pertz l.2335, "CAPITULARE LIPTINENSE", 743 | Correct |
| Aachen 802 | Pertz l.7787ff | Correct |
| Fortunatus V.3 | l.10216, "Ad cives Turonicos de Gregorio episcopo", in Liber V | Consistent with V.3 (the poem number is not legible in the OCR) |

- **NON-BLOCKING.** Dialogues IV.30's "Arian" and all of II.31 (Galla) now support nothing in the brief, because the Arian clause is gone. Keep IV.30 for "Gothic kings", and drop II.31 or say what it supports.

### Plain claims traced to "What the brief draws on"

Every plain claim in both briefs traces to the list, except these. All are NON-BLOCKING.
- **The tradition labels in both briefs.** Neither "in the church of Merovingian Gaul" nor "the early Benedictines of Italy begin with him" has a line. Add a census line, or a Sources line naming the Library's tradition entry.
- **Benedict: "Nearly all we know of his life comes from Gregory's Dialogues."** It is widely accepted, and the census longDescription says the same, but it has no line.
- **Benedict: "written ... about fifty years after Benedict died".** This rests on Gardner's 593 against the traditional 543. Both sit under What is uncertain, which is acceptable for "about".
- **Benedict: "Gregory wrote to show what God did through a saint".** It has no line.
- **Gregory: "Two centuries later" (Paul the Deacon).** It has no line for the date.
- **Gregory: "Much of what is known ... comes from those books".** It traces only to the Brehaut item under What is uncertain, which is acceptable.

### Modern scholars

Everyone taken out of the briefs now sits under Sources and under What is uncertain:
- Gregory: Brehaut and Dalton.
- Benedict: Gardner and Gasquet.

### What is uncertain, checked for accuracy

- **Brehaut.** Accurate (Brehaut l.68–72).
- **Fortunatus and Berny.** Accurate. Dalton l.27121–27123 says the council "is celebrated by Fortunatus in a poem addressed to Chilperic, and containing a panegyric of Fredegund (Carm. ix. 1). He says nothing of the affair mentioned by Gregory."
- **"Who Eusebius was." BLOCKING (references only).** The item says Gregory's History "never says which Eusebius". That is literally true of the History, but it misstates the evidence. Gregory himself settles it elsewhere.
  - In Glory of the Confessors 3 (arndt-krusch1885 l.56917) he writes: "Eusebius vero Vercellensis episcopus magnum huic Helario adiutorium contra hereses fuit."
  - Dalton's own note cites this passage (l.26989–26990: "Miracles wrought by the power of Hilary and Eusebius are described by Gregory in G. M., chs. 2 and 3").
  - As written, the item presents as open a point that Gregory's own words close.
  - Fix: state that Gregory, in Glory of the Confessors 2–3, pairs Hilary of Poitiers with "Eusebius of Vercelli", Hilary's great helper against heresy. Cite it in What the brief draws on, and drop the item from What is uncertain or recast it.
- **Gardner's and Gasquet's dates.** Accurate in substance:
  - Gardner l.12628–12630 gives born about 480 and leaving Rome "probably a few years before 500", with the date "disputed".
  - Gardner l.1025 dates the Dialogues to 593.
  - Gardner l.12778 and Gasquet l.202–203 give 543 as the tradition.
  - NON-BLOCKING: Gasquet says "in the year 480" (l.172–173), not "about". The item should read "Gardner gives about 480, Gasquet 480". Gardner also calls the leaving date disputed, which is worth keeping.
- **"The Collations." NON-BLOCKING, an inconsistency.** The brief states the Cassian identification plainly, and rightly so. Cassian's own Institutes announce his "Conferences of the Fathers" (npnf211 l.15528), and NPNF reads Rule ch.73 that way (l.16050–16057). Listing it under What is uncertain contradicts the brief. Move it to What the brief draws on, citing Cassian's Institutes and the NPNF note.
- **Gasquet on what the Rule did.** Accurate (l.398–402 and l.580–581).
- **Estinnes.** Accurate in substance. Pertz l.2355–2366 records that Hefele and Hahn hold the synod was held by Carloman and Pippin together, and that the editor argues against it. NON-BLOCKING: "disputed by the editors" is loose. It is historians (Hefele, Hahn) against the MGH editor.

## 3. Readability (engine.m1.profile_readability --report)

| Brief | Words | Grade | Grade, names out | Reading ease, names out | Words a sentence | Joining words per 100 | Short sentences | Result |
|---|---|---|---|---|---|---|---|---|
| Gregory v3 | 393 | 9.4 | 8.2 | 75.2 | 21.8 | 1.3 | 6% | pass |
| Benedict v3 | 422 | 9.4 | 7.6 | 78.1 | 21.1 | 0.7 | 5% | pass |

At about 165 words a minute, Gregory runs about 2:23 and Benedict about 2:33. There is no hard cap. NON-BLOCKING.

## Verdict

- **Gregory of Tours v3 brief: CLEARS.** The earlier blocking finding is fixed. The only open note is NON-BLOCKING: gloss "Merovingian".
- **Gregory of Tours references: DO NOT CLEAR.** One BLOCKING finding: the Eusebius item. Gregory's own Glory of the Confessors 3 names Eusebius of Vercelli as Hilary's helper, so the point is not open. Two NON-BLOCKING items: Paul the Deacon III.1-2 should be III.1, and add a trace for the tradition label.
- **Benedict of Nursia v3 brief: CLEARS.** One NON-BLOCKING item: split the 41-word sentence 2.
- **Benedict of Nursia references: CLEAR.** All are NON-BLOCKING:
  - Move the Collations out of What is uncertain.
  - Drop or repurpose the orphaned II.31 (Galla) and the "Arian" note on IV.30.
  - Give Gasquet's 480 as he wrote it.
  - Tighten the Estinnes wording.
  - Add a trace for the tradition label.
