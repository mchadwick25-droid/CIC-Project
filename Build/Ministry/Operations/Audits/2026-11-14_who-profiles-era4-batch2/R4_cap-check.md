# R4 cap check: era 4 batch 2

## Scope

One targeted check, ordered in Mark's cap ruling (2026-11-14). It does not count toward the three-round cap. It covers four changed strings only:

1. Benjamin I of Alexandria, brief paragraph 2 and its audio: the Evetts sentence.
2. Gregory of Narek, brief paragraph 4 and its audio: the Stepanos of Taron sentence, and the tie of the next sentence to Stepanos.
3. Martin I of Rome, card `uncertain` item 8: his election and the Calliopas decree.
4. Timothy I of Baghdad, card `uncertain` item 9: why he is called "of Baghdad".

Reviewer: independent Opus, first sight of these files. I edited no profile file, made no git writes and made no web, paid or model calls. I used local reads, `engine.m1.gates.grade_text` and a JSON load only.

## Method

- I opened every cited line in the vendored file myself and read the passage around it, reading through OCR noise and Mansi's two-column interleaving.
- For each string I checked the witness, any quotation, pronoun reference, sentence length, fragments and AI tells, and read the rest of its paragraph or field.
- For 1 and 2 I ran `grade_text` on the whole brief from the repo root, counted words, and compared each audio file with its brief after removing "[calmly] " and "[warmly] ".
- For 3 and 4 I loaded each card with `json.load`.
- I ran `git diff HEAD` on all six files.

## 1. Benjamin I of Alexandria, brief paragraph 2: PASS, one MINOR

String: "B. Evetts, the History's translator, heads his life 622 to 661." (11 words.)

- Source: `severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt` l.3-6, title page: "Evetts, B. (Editor and translator)". l.42834: "BENJAMIN I, THE THIRTY- EIGHTH PATRIARCH. A. D. 622-661". The running heads repeat it (l.42707, 43121 and on, "A. D. 622-661" through OCR noise). "Translator" and "heads his life 622 to 661" both hold. An "A. D." heading is the editor's, so tying it to Evetts is right.
- "The History's": the sentence before names "the History of the Patriarchs of Alexandria", so the possessive is clear. It also removes the old "its", which could have meant Benjamin's church.
- Witness: named, with his role added. That meets the pattern ("Real witnesses named"). A role alone would not.
- "His": it can only mean Benjamin. Evetts does not head his own life.
- Writing: one idea and a natural date span. No AI tell.
- Gate: FK 8.23, Flesch 60.07, 405 words. PASS, though Flesch has almost no margin.
- Audio: equal to the brief once the tags are removed. One `[calmly]` and one `[warmly]`. PASS.

MINOR (not blocking, and not new): the next sentence, "He came from a rich family at Barshut...", follows a sentence whose subject is Evetts. Heard aloud, "He" briefly points back to Evetts. The sense is clear from Barshut and the monastery, and the source holds it (l.42842-42846, "a hamlet called Barshut"; "they were very rich"). Fix: move the Evetts sentence up one place, so that the paragraph reads "So says the History of the Patriarchs of Alexandria, a later Arabic history of Benjamin's own church. B. Evetts, the History's translator, heads his life 622 to 661. Benjamin I of Alexandria led the Egyptian church that refused the council of Chalcedon. He came from a rich family at Barshut ...". Make the same change in the audio. The words do not change, so the grade score and the word count stay the same. "Benjamin came" does not work as a fix: it drops Flesch to 59.65, which fails the gate.

## 2. Gregory of Narek, brief paragraph 4: PASS

String: "Stepanos of Taron, of Gregory's own century, wrote Armenian history." (10 words.)

- Source for the date: `stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt` l.802-804. Macler says Asolik lived "durant la seconde moitié du x° siècle et les premières années du xr°". At l.835-838 he says the history was written for the catholicos Sargis (992-1019), and at l.863-866 that the narrative ends in 1004-1005. The brief makes Gregory "a monk of tenth-century Armenia", and Ormanian's 1003 death is in the same brief. "Of Gregory's own century" holds. It also ends the old "of the same century", which came right after Serpos "writing at Venice in 1786".
- "Wrote Armenian history": the Gelzer-Burckhardt title, "Des Stephanos von Taron armenische Geschichte" (l.1), and Macler's "Histoire universelle" both support this.
- Next sentence: "He says teachers including Anania of Narek ruled that anyone baptized in the Chalcedonian faith be baptized again." "He" is the subject of the sentence before, Stepanos. The tie holds. Source: `stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt` l.6482-6483 ("Anania, der grofse Philosoph, welcher auch Mönch zu Narek war") and l.6507-6511 ("Diese alle ordneten ... an, dafs die auf das Bekenntnis von Chalkedon getauften noch ein zweites Mal getauft werden sollten"). Macler l.822-823 also has the reference to "Anania de Narek". It holds. The same lines say the ruling was made "auf den Befehl Ter Ananias hin", at the order of the catholicos Anania of Mokk. The brief leaves this out. That sentence is outside this check and is not wrong, so this is not a finding.
- Writing: 10 words, plain, and not a fragment. No AI tell.
- Gate: FK 8.09, Flesch 61.11, 405 words. PASS.
- Audio: equal to the brief once the tags are removed. One `[calmly]` and one `[warmly]`. PASS.

## 3. Martin I of Rome, `uncertain` 8: PASS

String: "His election. Foulke says it lacked the emperor's confirmation. Theodore Calliopas, the governor who arrested him, handed the clergy a decree. As Martin reports it, the decree said he had seized the see irregularly and without law." (2, 7, 12 and 16 words.)

- Foulke: `paul-the-deacon_history-of-the-langobards_foulke1907.txt` l.9938-9940, "Pope Martin I, whose appointment lacked the confirmation of the emperor and who was regarded by the latter as a usurper". This holds. Foulke writes "appointment" and the card writes "election". For a pope the two are the same event, and the card does not quote Foulke, so this is not a finding.
- Calliopas: Mansi calls him exarch throughout. l.82112-82113 has "Theodorus exarchus, qui cognomento Calliopa dicitur", and l.87156 has "a Calliopa exarcho". The card renders "exarchus" as "governor" elsewhere ("Olympius, the emperor's governor in Italy"; "Nor had he made him governor", from "illum feci exarchum", l.87840). "Governor" therefore keeps the card's one term for one thing (checklist 9). It holds.
- The arrest: l.87155-87157 has "inde a Calliopa exarcho vi abreptus, Constantinopolim missus est". The Book of the Popes, l.82112-82118, says Calliopas and Theodore the chamberlain "tollentes sanctissimum Martinum papam de ecclesia ... perduxerunt Constantinopolim". Martin's own letter, l.87375-87377, says "quando Calliopas cum Ravennati exercitu ... introivit civitatem". "Arrested him" holds.
- The decree: l.87342-87345 has "Quibus confestim introeuntibus, iussio a Calliopa porrecta", and the text runs on in the right-hand column at l.87424-87426: "est presbyteris & diaconibus, in qua humilitatis meae abiectio continebatur, quod irregulariter & sine lege episcopatum subripuissem". "Iussio" is a decree or order. "Porrecta est presbyteris & diaconibus" means it was handed to the clergy. "Irregulariter & sine lege" becomes "irregularly and without law", and "episcopatum subripuissem" becomes "seized the see". All of this holds.
- "As Martin reports it": the passage is in Martin's own first-person letter ("humilitatis meae"), and the clause is reported speech ("quod ... subripuissem"). "Reports" is more accurate than the earlier "quotes". It holds.
- "Him": the item is about Martin, and the only other people named before it are Foulke and the emperor, neither of whom could be the one arrested. "He" in the last sentence is Martin, who is named just before it. Both are clear.
- Writing: "His election." is the field's title opening, as in every other `uncertain` item. It is not a defect. There is no AI tell and no empty contrast.
- JSON: loads. PASS.

## 4. Timothy I of Baghdad, `uncertain` 9: PASS

String: 'Why he is called "of Baghdad". Chabot and Bar Hebraeus place his enthronement at Seleucia, and Amr ibn Matta at Madaina. Joseph Assemani says the patriarchs then lived at Baghdad, Timothy at the monastery of Kelilisho.' (6, 15 and 15 words.)

- On topic: the item sets the place where he was enthroned (Seleucia or Madaina, not Baghdad) against where Assemani says he lived (Baghdad). That is the grounds for the name, and the item claims nothing beyond it. No vendored witness explains the epithet itself, and the item does not invent an explanation.
- Chabot: `synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` l.40258, "fut élu et intronisé à Séleucie, après huit mois". It holds.
- Bar Hebraeus: `barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt` l.9611-9613, "Timotheum vero assumptum deduxerunt Seleuciam et catholicum proclamarunt". It holds.
- Amr ibn Matta: `amr-ibn-matta_de-patriarchis-nestorianorum-commentaria-pars-altera-ara-lat_gismondi1896-1897.txt` l.13016-13017, "eumque consecraverunt Modainae indutum pallio violaceo". Amr says "consecrated" and the card says "enthronement". These are the same act in this context. It holds.
- Assemani: `assemani_bibliotheca-orientalis-tomus3-pars2-de-syris-nestorianis-lat_1728.txt` l.42422-42428. It says patriarchs were elected at Baghdad and consecrated at Modaina, then "fixum Bagdadi domicilium nunc in coenobio Caliljesu ... Timotheus & Josue in Caliljesu manere". l.42421 adds that Timothy built that monastery. "The patriarchs then lived at Baghdad, Timothy at the monastery of Kelilisho" holds. Tomus 3 pars 1 also has Timothy's "coenobium illius Caliljesu" (l.114219). The spelling "Kelilisho" matches the card's `place` field.
- Writing: the title opening matches the other items. The closing clause leaves out its verb ("Timothy at ..."), which reads naturally. No AI tell.
- JSON: loads. PASS.

## Diffs (`git diff HEAD`)

- `benjamin-i-of-alexandria.brief.txt` and `audio/benjamin-i-of-alexandria.audio.txt`: one line each, "its translator" changed to "the History's translator". Nothing else.
- `gregory-of-narek.brief.txt` and `audio/gregory-of-narek.audio.txt`: one line each, "of the same century" changed to "of Gregory's own century". Nothing else.
- `martin-i-of-rome.card.json`: `uncertain` item 8 only. The old text was "... The decree Theodore Calliopas handed to the clergy, as Martin quotes it, said he had seized the see irregularly and without law."
- `timothy-i-of-baghdad.card.json`: `uncertain` item 9, where "His name." became 'Why he is called "of Baghdad".', and a newline was added at the end of the file. The newline does not change the content.

## Findings

- BLOCKING: none.
- MINOR: Benjamin, paragraph 2. "He came from a rich family at Barshut" follows the Evetts sentence. Fix: move the Evetts sentence to directly after "So says the History ... own church." in both the brief and the audio. The words stay the same, so the gate score and the 405-word count stay the same.

## Verdict

CLEAR.

- The Evetts sentence matches the title page and the l.42834 heading.
- "Of Gregory's own century" matches Macler's dating of Stepanos (l.802-804), and the Anania sentence is still Stepanos's (Gelzer-Burckhardt l.6482-6511).
- Calliopas is the exarch, which the card renders as governor. He took Martin, and Martin's own letter reports the decree's "irregulariter & sine lege ... subripuissem" (Mansi l.87342-87345, 87424-87426).
- The Timothy item now does what its heading says, and each of its four witnesses holds.
- Both briefs pass the gate at 405 words, both audio files match their briefs, and both cards are valid JSON.
