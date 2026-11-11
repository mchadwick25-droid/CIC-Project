# R4 targeted recheck: length cuts restored (cap ruling)

This is a targeted recheck of the text restored after Mark's ruling that length follows scope. Only the sentences that differ between `<id>.pre-recheck.txt` and `<id>.txt` are checked, plus the two card JSON files that changed (origen, athanasius). Each `pre-recheck.txt` is byte-identical to the HEAD draft reviewed in R3. Length past 300 words is not a finding. Line numbers are file lines in /home/user/CIC-Project/cic/texts/.

Abbreviations: E = npnf201 (Eusebius); J = npnf203 (Jerome); A9 = anf09 (Origen, Commentary on John); N2 = npnf202 (Socrates, Sozomen); M = palladius_dialogue-life-of-chrysostom_moore1921.txt; NY = npnf205 (Gregory of Nyssa); B = npnf208 (Basil, letters); NZ = npnf207 (Gregory Nazianzen); L = anf07 (Lactantius).

## score.py (restored texts as delivered)
- origen.txt: 374 words, FK 8.6, FRE 62.3, no fails. In band.
- athanasius-of-alexandria.txt: 325 words, FK 8.4, FRE 63.3, no fails. In band.
- john-chrysostom.txt: 348 words, FK 8.8, FRE 60.0, no fails. In band, at the FRE floor.
- gregory-of-nyssa.txt: 309 words, FK 8.9, FRE 63.5, no fails. In band.
- gregory-of-nazianzus.txt: 307 words, FK 8.9, FRE 61.2, no fails. In band.
- constantine-the-great.txt: 312 words, FK 8.4, FRE 67.6, no fails. In band.

The fixes below were scored in memory with the same engine function (score_turn). Nothing was written to the drafts.
- origen with O1+O2 applied: 374 words, FK 8.6, FRE 62.5, no fails.
- john-chrysostom with C1 applied: 360 words, FK 8.5, FRE 61.5, no fails.
- gregory-of-nyssa with N1 applied: 346 words, FK 8.9, FRE 63.3, no fails.

## Quotations (character for character, tags stripped, line-wrap collapsed)
- Gregory of Nazianzus, new: "We seemed to have one soul, inhabiting two bodies." NZ 41521-41522 (`We seemed to` / `have one soul, inhabiting two bodies.`). MATCH, untrimmed. Context is Oration 43 §20, the Athens years ("a pursuit ... that of letters", NZ 41516-41517), so "Of their years together" is fair.
- No other restored sentence carries quotation marks. Origen's "come through a storm and been brought out of Egypt" is an unquoted paraphrase of A9 24726-24728 ("We emerged from the storm, we were brought out of Egypt"). That is acceptable.

---

## Origen — APPROVED WITH FIXES

**O1. BLOCKING: the restored Celsus sentence breaks the "it" in the Rufinus sentence.** In paragraph 3 the Celsus sentence now sits between On First Principles and "We read it mostly in Rufinus's Latin, and Jerome said Rufinus changed it." To the ear, "it" now points to the eight books against Celsus or to the True Discourse. That is misleading: the Rufinus problem belongs to On First Principles (the card's own uncertain[0] says so). The fact itself is sound: E 37104-37106, "a work of eight books in answer to that entitled True Discourse, which had been written against us by Celsus".
Replace:
> and that souls existed before birth. Eusebius also says he wrote eight books in answer to Celsus, who had attacked Christians in his True Discourse. We read it mostly in Rufinus's Latin, and Jerome said Rufinus changed it.

with:
> and that souls existed before birth. We read that book mostly in Rufinus's Latin, and Jerome said Rufinus changed it. Origen also wrote eight books in answer to Celsus, who had attacked Christians in a book called the True Discourse.

This also drops "Eusebius also says" (see O2). "A book called" keeps the ear from hearing "True Discourse" as a description.

**O2. STANDARD: the restorations push the brief toward a citation list.** Two of the three restored sentences open "Eusebius says" or "Eusebius also says". With them the brief has eight "X says" attributions, and paragraph 2 now runs "Jerome says ... Eusebius says ...". Neither the Hexapla nor the Celsus books is contested, lone or hostile. The pilot rule is to tell such points directly and keep the source in the notes (REVISE.md, "Witnesses"). Jerome stays on the Hebrew sentence, because "against the habit of his time and his people" is his judgment (J 40555-40557). The Celsus sentence is fixed in O1.
Replace:
> Eusebius says he then set the Hebrew text beside the Greek translations in the work called the Hexapla.

with:
> He then set the Hebrew text beside the Greek translations, in a work called the Hexapla.

Support: E 34715-34717 ("placed them opposite each other, with the Hebrew text itself. He thus left us the copies of the so-called Hexapla"), and the Greek versions at E 34717-34719 and J 40557-40560.

**O3. STANDARD: the card's Hexapla "about" now misreads Jerome and no longer says what the work is.** The new text reads: "Eusebius says Origen left us copies of it; Jerome says its extra translations came from Origen's library". Jerome actually wrote "a fifth, sixth, and seventh translation, which we also have from his library, he sought out with great diligence" (J 40562-40563). So Origen searched these translations out, and Jerome's own copies came from Origen's library. "Came from Origen's library" reads as though Origen took them from his own shelves. The card also has to stand alone, and this line no longer tells a reader what the Hexapla was. The Eusebius half is supported (E 34716-34717).
Replace the `"about"` value with:
> "the Hebrew text set beside the Greek translations; Eusebius says Origen left us copies of it, and Jerome says Origen searched out three more translations, which Jerome himself had from Origen's library"

Other restored items, checked:
- "Jerome says he was so devoted ... learned Hebrew, against the habit of his time and his people." J 40555-40557: "so assiduous in the study of Holy Scriptures, that contrary to the spirit of his time, and of his people, he learned the Hebrew language". Supported and named correctly. Eusebius agrees at E 34428-34429.
- "He later wrote that he had come through a storm and been brought out of Egypt." A9 24724-24728, in the preface to Book VI of the Commentary on John: "the storm in Alexandria ... We emerged from the storm, we were brought out of Egypt". Supported. It is placed after the move to Caesarea, it names no enemy, and it reads naturally after "In the year 231 Origen left Alexandria for Caesarea."
- Voice: no restored sentence runs past 28 words, and there are no AI tells.

Check lines: fidelity, one BLOCKING (O1). Witnesses, one STANDARD (O2). Card, one STANDARD (O3). Contested points unchanged. Score in band before and after the fixes.

---

## Athanasius of Alexandria — APPROVED

No findings.
- "Socrates gives another account too: some affirm the emperor did it for the unity of the church, since Athanasius refused any communion with Arius and his followers." N2 5367-5371: "Now some affirm that the emperor came to this decision with a view to the establishment of unity in the church, since Athanasius was inexorable in his refusal to hold any communion with Arius and his adherents." Supported, attributed to Socrates correctly, and told as a report ("some affirm"). It is an unquoted paraphrase that stays close to the source wording, which is acceptable. The sentence is 27 words, under the limit.
- The grain-ship sentence, now split off, is unchanged in substance (N2 5360-5366).
- Card legacy_remembered[1]: "the bishops at Tyre deposed him, and the reasons for his exile to Trier were reported two ways, as Socrates's telling shows." This is accurate and not misleading. An optional, non-blocking wording that says who said what: "Disputed in his own time: the bishops at Tyre deposed him, and Socrates reports two reasons for his exile to Trier, a charge about the grain ships and, as some said, the unity of the church."

Check lines: fidelity clean. Witnesses named correctly. Voice clean. Score in band.

---

## John Chrysostom — APPROVED WITH FIXES

**C1. BLOCKING: "feeding the poor through a famine" overstates Palladius.** Palladius writes that John "resided at Cucusus for a year, 'feeding great numbers of the poor of Armenia,' where a great famine occurred at the time; not with corn, so much as with words" (M 6290-6293). The brief drops his qualifier, so it reads as famine relief with food. Palladius says the feeding was more with words than with grain. "A year" is correct (see the chronology below).
Replace:
> Palladius says he spent a year there feeding the poor through a famine, until his enemies had him moved on.

with:
> Palladius says he spent a year there while a great famine struck Armenia, and that John fed the poor more with words than with grain. Then his enemies had him moved on.

"Moved on" stands for Palladius's transfer to Arabissus (M 6293-6295, "the fratricides, who transferred him to Arabissus").

**Chronology check (the specific watch item).** It holds.
- 404, to Cucusus: Sozomen, "conveyed him to Cucusus, a city of Armenia, which the emperor by letter had appointed" (N2 44067-44069).
- One year at Cucusus, then Arabissus: Palladius (M 6290-6295). The three years in M 704-706 (Sept 404 to June 407) cover the whole exile, so the notes rightly refused "three years at Cucusus".
- The harsher order to Pityus "on the shore of the Black Sea": Palladius, "a rescript, more severe than the last" (M 6392-6397). Sozomen agrees: "a remoter place of banishment, and soldiers were sent to conduct him to Pityus" (N2 44494-44496).
- 407 and the death on the road: Socrates has him die "in Comana on the Euxine, on the 14th of September" in the consulate the endnote reckons as 407 (N2 18609-18613). This agrees with "toward Pityus ... He died on the road". The June 407 date for the order rests on the contents list at M 706, a date only, and is consistent with Socrates.
- "In Armenia" follows Sozomen. Moore's footnote ("on the edge of Cilicia", M 6206) is rightly not used.

Other restored items, checked:
- "Socrates notes the irony: the bishops condemned John under a canon first framed at Antioch against Athanasius, and so approved Athanasius's own deposition." N2 18476-18487: "framed in the council convened against Athanasius at Antioch ... the bishops would not listen to his defence, but immediately condemned him, without considering that by using this canon they were sanctioning the deposition of Athanasius himself". Socrates himself makes the remark, so "notes the irony" is fair. It also sits in the right order: the Herodias clash with Eudoxia (N2 18455-18457), then the second council, then "Chrysostom was silenced" (N2 18490). Supported.
- "In 404 an imperial decree sent John to Cucusus in Armenia." N2 44067-44069. Supported.
- "In 407 a harsher order sent him toward Pityus on the Black Sea." M 6392-6397 and N2 44494-44496. Supported. "Toward" is right, because he never arrived.
- Voice: all restored sentences are under 28 words. The joins read naturally.

Check lines: fidelity, one BLOCKING (C1). Chronology holds. Witnesses named correctly (Socrates, Sozomen by content, Palladius). Score in band, and FRE rises to 61.5 with the fix.

---

## Gregory of Nyssa — APPROVED WITH FIXES

**N1. STANDARD: the ordination charge rests on the translators' prolegomena, while Basil, an ancient witness in the Library, carries it and tells it differently.**

The restored clause reads "Arian bishops charged him with irregularities in his ordination". It is drawn from NY 763-764 ("A charge of uncanonical irregularity in his ordination is brought up against him by certain Arian Bishops"). That is a modern summary, and it is not wrong in outline. But Basil, writing at the time, frames the case differently:
- B 39549-39552 (Letter 225, to Demosthenes, written "as from the synod of bishops"): the imperial vicar, "moved by the reproaches of Philochares, ordered my brother and fellow-minister Gregory to be haled before your judgment seat."
- B 39563-39574: money ("If there is any question of the wasteful expenditure of money...") and order. "If there is any other point of canonical order ... if there has been a failure in any point of canonical order, the responsibility lies with the consecrators and not with him who is forcibly compelled to undertake the ministry."
- B 40849-40857 (Letter 237): the Vicar "is certainly a friend of heretics", "has summoned a synod of wicked men in mid-winter in Galatia", and "has ordered the removal of my brother on the accusation of one man".
- The editor's note at B 39527-39528 ("alleged irregularities in Gregory's consecration") agrees that this is the ordination question.

So the contemporary witness puts the charge before an imperial official and gives Basil's answer. The brief instead names "Arian bishops" as the accusers on the prolegomena's word alone. The brief does tell it as a charge, not as fact, which is good. But it rests a story point on a modern source when an ancient one exists, and it simplifies who brought the case. Basil's answer also ties the point back to "over his protest", the sentence just before. None of the other witnesses tried (Gregory Nazianzen's letters in NZ, Theodoret, Socrates, Sozomen) carries the ordination charge in the Library files I searched. Basil does.

Replace:
> Arian bishops charged him with irregularities in his ordination, and in 376 he was banished, until Valens died in 378.

with:
> Later an imperial official, whom Basil calls a friend of heretics, had Gregory summoned on charges about church money and his ordination. Basil answered that if any church rule had been broken, the blame lay with those who ordained him, not with a man forced to serve. In 376 Gregory was banished, until Valens died in 378.

Notes entry to add: B 39549-39552, B 39563-39574, B 40849-40857; banishment 376 at NY 784-785 as before. "Charges about church money and his ordination" is told directly. Basil names money outright and raises the ordination point conditionally, and the NY 763-764 and B 39527-39528 summaries state the ordination charge plainly. The sentences run 22, 26 and 10 words.

Check lines: fidelity. The clause as restored is not false, but it is witnessed only by the prolegomena (STANDARD, N1). The charge is told as a charge. Score in band, 63.3 with the fix.

---

## Gregory of Nazianzus — APPROVED

No findings.
- "Egyptian bishops objected, citing a rule from Nicaea against moving a bishop from one see to another". NZ 23175-23178: "the Egyptian Bishops ... determined ... to oust Gregory from the Patriarchal Throne on the ground of a Nicene canon forbidding translations". Told directly from the introduction, which states it plainly, and framed as the bishops' citation, not as a ruling. That is acceptable. The introduction's remark that the canon "had virtually been rescinded by the act of the Council" is not needed, because the brief has already said the council made him archbishop. Sozomen corroborates the Egyptian objection (N2 40817-40818) but does not name the canon. The sentence is 26 words.
- The new quotation MATCHES (above). Its lead-in, "Of their years together he wrote:", follows the Athens sentence naturally.

Check lines: fidelity clean. Quote MATCH. Voice clean. Score in band.

---

## Constantine the Great — APPROVED

No findings.
- "The same decree ordered the places where Christians met to be given back." L, Lactantius chap. XLVIII: "the places appropriated for their religious assemblies ... do restore them to the Christians" and "All those places are, by your intervention, to be immediately restored to the Christians". Supported. "The same decree" follows the Milan sentence already accepted in R3.

Check lines: fidelity clean. Voice clean. Score in band.

---

## Verdicts
- Origen: APPROVED WITH FIXES (O1 BLOCKING, O2 STANDARD, O3 STANDARD card).
- Athanasius of Alexandria: APPROVED (one optional card wording).
- John Chrysostom: APPROVED WITH FIXES (C1 BLOCKING).
- Gregory of Nyssa: APPROVED WITH FIXES (N1 STANDARD).
- Gregory of Nazianzus: APPROVED.
- Constantine the Great: APPROVED.

Every fix is given as exact replacement text and was scored in band. The fixes can be applied without another review round.
