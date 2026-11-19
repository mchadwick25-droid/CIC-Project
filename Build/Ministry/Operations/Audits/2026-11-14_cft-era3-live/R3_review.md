# Era 3 on the live tree (data release 42): review round 3

Reviewer: fresh Opus agent, full effort, independent of the drafting and of rounds 1 and 2. Round 3 of 3: a targeted recheck of `git diff 43b4bc34..HEAD` (commit `4effcef7`, "Era 3: review round 2 fixes") against the findings of `R2_review.md`. Text cleared in earlier rounds was not re-reviewed. The generated `cft-website` files were not reviewed.

**Verdict: approved to proceed. 0 blocking, 0 substantial, 3 minor.** The three minor points are one-line edits and need no further review round.

The validator passes: `node tools/validate-census.mjs --base census41.json cic-website/data/world-census.json` gives `559 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four known shortName warnings), exit 0.

The census diff since round 2 touches exactly five fields: the Nisibis story text, the Ladder legacy line, the Nubian source note, the Toledo IV teaser and Philoxenus's `dates`. Each matches what `R2_changes.md` and `Census_Text_Changes.md` say was built.

---

## Round 2 findings

| Finding | Status |
|---|---|
| N1 Toledo IV teaser | **Fixed.** "The bishops of Spain ... declare forced baptism wrong — and rule that ...". `Census_Text_Changes.md` now shows the clause through "rule that". |
| N2 Philoxenus dates line | **Fixed.** "bishop from 485; driven out 518 or 519" matches the card's datesNote: "Made bishop of Mabbug in 485, by Budge's date. Driven from Mabbug in the second year of the emperor Justin, the year 830 of the Greeks, which Budge reads as 518 to 519" (`Who-Profiles/era3/batch7/philoxenus-of-mabbug.card.json`, `dates`). The bar still ends at 523, Nau's end of his time as bishop, as the same note says. No new error. |
| N3 The Ladder | **Fixed.** "The Greeks held him in great value, Philippe Labbe says, and Elias of Crete wrote explanations of the Ladder." This is true to "apud Graecos in magno pretio habitum fuisse Climacum" (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` l.41362-41363, OCR normalized) and "Elias metropolita Cretensis, qui explanationes in Scalam scripsit" (l.41434-41435, OCR "seripsit"). It agrees with the John Climacus card: "Philippe Labbe says the Greeks held him in great value. ... Elias of Crete, he says, wrote explanations of the Ladder." |
| N4 Nisibis, Labourt on Sabrisho | **Fixed in fact.** See below. One clarity point from the new sentence (m2). |
| M1 Henana's death | **Fixed in fact; the sentence no longer parses well** (m1). |
| M2 "children" | **Fixed.** "a peine autant d'enfants" (Chronicle of Seert l.28711-28712). |
| M3 Julian's 543 | **Fixed** in the note; Longinus's "560s to 580s" agrees with his census line "consecrated after 566; with the Alodaei 580" and his card. The Open-Gaps 254 line misses one use of 543 (m3). |
| M4 Decision-Log quotation count | **Fixed.** The paragraph no longer gives a sum that fails; "Many", "13 readings", "One", "Fourteen" are each true as stated. |
| M5 Records lines | **Fixed.** "the coordinator had accepted each one before Mark's approval" is clear. The Open-Gaps 247 closure now names the Benedict line, and the census line reads "his order's tradition gives his death as 543" (`world-census.json` l.39246). |
| M6 Mark's words | **Checked as far as this review can.** The Decision-Log quotes Mark only as "Approve", on preview version 2, which is what the coordinator relayed. Nothing else is put in his mouth. [REVIEW-ROUNDS] is the known placeholder. |

### The new Nisibis sentences, checked

The text: "In the Chronicle the catholicos Sabrisho takes Henana's side. Labourt finds the same odd turn: Sabrisho's own synod of 596 spoke against the Henanians, yet he helped them against Gregory."

- "In the Chronicle ... takes Henana's side": "Mais le catholicos, bien loin de confirmer leur sentence, accueillit favorablement la lettre de Hnana" (`chronicle-of-seert_histoire-nestorienne-seconde-partie-po13-ara-fra_scher1919.txt` l.28666-28667, OCR "lottre do"). True.
- "Sabrisho's own synod of 596 spoke against the Henanians": "Sabriso' se prononça cependant contre eux dans le synode général qu'il tint au mois d'Yar de la sixième année de Chosrau (mai 596)" (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.12231-12233). True.
- "the same odd turn ... yet he helped them against Gregory": "Chose étrange et qui peint bien cette époque si troublée : Sabriso' seconda les Henaniens dans cette affaire. Il détestait Grégoire ... le catholicos entrava de mille manières l'action de son rival" (Labourt l.12273-12279). "Odd" is fair for "étrange"; "helped them against Gregory" is fair for "seconda ... dans cette affaire" and "entrava ... l'action de son rival". Scher's introduction agrees: "le catholicos Sabriso' le défendit, et voulut même déposer Grégoire" (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.16966-16968).
- The earlier sentence's "though the acts never name him" still stands with Labourt's "Les Pères du concile ne désignèrent pas nommément Henana" (l.12234-12235).

No new error of fact. Scher's note 2 on the Chronicle's chronology (l.28677-28683: Gregory's departure in 594/5 falls before Sabrisho was catholicos) is already covered by the caveat, "The chronology of the walkout is uncertain within a decade", which earlier rounds cleared.

---

## BLOCKING

None.

## SUBSTANTIAL

None.

## MINOR

### m1. The death sentence's two halves do not answer the same question (`the-church-of-the-east-under-persia`, documentedStories[1].text)

The text: "When Henana died is told two ways in Addai Scher's notes: under the catholicos Sabrisho, who died in 604, or still alive in 610."

The facts are right: "il mourut sous le patriarche Sabrjésus (596-604)" (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.21023-21024, OCR "Subrjésus") and "nous savons que Hnana vivait encore en 610 (Chronique de Séert)" (l.21734). But "When Henana died is told ... or still alive in 610" does not parse: "still alive" is not a when of his death. The passive "is told two ways", which round 2 asked to drop, also stays.

Fix: "Addai Scher's notes disagree on his death. One says he died under the catholicos Sabrisho, who died in 604; another says he was still alive in 610."

### m2. After the Labourt sentence, the walkout's "decision" has lost its referent (`the-church-of-the-east-under-persia`, documentedStories[1].text)

The text: "... yet he helped them against Gregory. Moved by Sabrisho's decision, about three hundred students walked out ..."

The inserted Labourt sentence now stands between the Chronicle's account and its walkout, so "Sabrisho's decision" reads as Labourt's last clause, or even as the synod of 596 against the Henanians. In the Chronicle the decision is his taking Henana's word over the metropolitan's: "Les étudiants furent fortement affectés de cette décision de Sabriso', qui avait repoussé la parole du métropolitain pour accepter celle de Hnana" (Chronicle of Seert l.28671-28672, OCR "fureiit", "atfectes", "repousse"). The return to the Chronicle is also unmarked.

Fix: "Moved, the Chronicle says, by Sabrisho's choice of Henana's word over Gregory's, about three hundred students walked out ..."

### m3. Open-Gaps 254 names two uses of Julian's 543 in the Nubian entry; there are three (`Open-Gaps.md`, entry 254, map-position item)

The text: "The Nubian Christianity entry's dates (543-652) and its first story's years (543-545) rest on the same modern year for Julian, which John of Ephesus does not give."

The entry's teaser also uses it: "The Nile in what is now Sudan, 543 to 652 CE — three Christian kingdoms ..." (`cic-website/data/world-census.json` l.40417). The Julian card: "John of Ephesus gives no year" (`Who-Profiles/era3/batch2/julian-missionary-to-the-nobadae.card.json` l.7).

Fix: "The Nubian Christianity entry's dates and teaser (543 to 652) and its first story's years (543-545) rest on ..."

---

## AI tells and generic voice

None in the changed lines. "Labourt finds the same odd turn" keeps Labourt's own "chose étrange" and reads as a person telling the story, not as a hedge. The Ladder and Philoxenus lines are plain and exact.
