# Era 3 on the live tree (data release 42): review round 2

Reviewer: fresh Opus agent, full effort, independent of the drafting and of round 1. A targeted recheck of branch `claude/cft-era3-live`: the round 1 findings, every participant line changed since `477c7d3b`, and the new release records. The branch moved to `43b4bc34` during the review ("Mark's ruling recorded"); that commit touches only the Decision-Log and Open-Gaps, and both were read at `43b4bc34`.

**Verdict: not yet approved to proceed. 0 blocking, 4 substantial, 6 minor.** Each substantial fix is a one-line text edit. A round 3 recheck need look only at those lines.

The validator passes: `node tools/validate-census.mjs --base census41.json cic-website/data/world-census.json` gives `559 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four shortName warnings of round 1). Every "Old" and "New" text in `Census_Text_Changes.md` was matched against release 41 and the branch census: all are present as given. Every quotation and rendering below was checked against the vendored file at the line given.

---

## Round 1 findings

| Finding | Status |
|---|---|
| B1 Victor of Vita and Fulgentius in the Non-Nicene lane | **Fixed.** Both are `toldWithin: null`, lane `4 Africa`, laneLabel "Africa". Their tree pages read "A person whose story no single tradition tells." The Homoian entry's `people` and `voices` are now identical to release 41: Victor is again a named row (voice 4, "a Nicene bishop and hostile witness"), and the Fulgentius link is gone from its Who. The card `tradition` field, which still names the Homoian entry, is not carried into the census. |
| B2 The Nisibis story | **Fixed at the root.** The governor and the catholicos Ishoyahb are gone, and each witness now carries what it holds. Two smaller points remain (N4, M1 below). |
| S1 Liberatus | **Fixed.** True to l.82406-82413 and to Garnier's note, which goes on to name Reparatus first among those deposed and exiled ("Horum primus depositus est ac in exsilium missus", l.82529-82530, OCR normalized). |
| S2 Philoxenus's dates line | **Partly fixed.** The death year is gone, but the new line makes a new error (N2). |
| S3 Julian and Longinus places | **Fixed.** "Constantinople · the land of the Nobadae", with no id. |
| S4 Voices against the cards | **Fixed** for the Julian and Benedict lines. One residue in the same entry (M3). |
| S5 Isidore at Toledo IV | **Partly fixed.** The story sentence is right; the teaser now has a grammar error (N1). |
| S6 The Ladder | **Partly fixed.** The double hedge is gone, but the new sentence misreads its held line (N3). |
| S7 The rendering rule | **Fixed.** `declaredRendering` and its 120-character reach are gone. The check keys each skip on entry id plus the exact quoted span (`renderings.has(rk)`), so it skips exactly the 14 listed spans and nothing near them. A listed span not met fails the run (`no longer stands in`), and a missing original file fails it too. The old comment is replaced. Run with the readings and renderings lists emptied, the check fails on 30 quotations: the 14 listed renderings and 16 scan faults, as the Decision-Log says. |
| S8 Records | **Fixed.** `Census_Text_Changes.md`, the Decision-Log entry and the Open-Gaps closures and entry 254 are on the branch. |
| M1 Maccurritae | **Fixed.** "thought them" for Mommsen's "videntur intellegi"; one name, John of Biclaro, throughout. |
| M2 Caesaria | **Fixed.** "The second greets her as a holy sister." |
| M3 Victor of Tunnuna sources | **Fixed.** "Note to section 91 of the Life of Antony"; "Introductory Note to Part I" stands at `anf03_tertullian.xml` l.465, and the "Victor of Tunis" line (l.1404) is inside it. |
| M4 Short dates lines | **Fixed.** Each new line rests on its card's datesNote (checked for Cassiodorus, Columbanus, John of Ephesus, Marius, Theodosius, Ferrandus, John of Biclaro, Dionysius). Philoxenus is N2. |
| M5 Places and regions | **Fixed.** Severinus "Noricum"; John Rufus "Antioch · Maiuma". `regions` is carried in Open-Gaps 254. |
| M6 Placings outside the list | **Fixed.** Constantius and Gennadius are named in the Decision-Log as the worker's calls. |
| M7 De-quotings | **Fixed.** |
| M8 Scan-reading drops | **Fixed.** A drop now requires the range's non-blank lines to equal `lines_held`. All three ranges were read: Perry l.24124-24128, McCrindle l.7193-7206 and Payne Smith l.13034-13042 hold exactly their declared lines and blank lines. |
| M9 Henana's death and the statutes | **Fixed**, with M1 below; the statutes' year is carried in Open-Gaps 254. |
| M10 Renderings | **Fixed.** "And yet I call God, who knows what is hidden, to witness that I have left out many deeds of my lord Germanus that were known and proved" renders "Et tamen Deum testor conscium secretorum me plura de domni mei Germani factis agnita et probata tacuisse" (`constantius-lyon_vita-germani_levison1920.txt` l.4577-4579) clause by clause. "We walk the middle way, then, with Christ as our guide" renders "nos ergo per medium Christo duce gradientes" (`faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt` l.11049-11050). |

---

## SUBSTANTIAL

### N1. The Toledo IV teaser now has a subject-verb error (`nicene-visigothic-iberia`, documentedStories[1].teaser)

The text: "The bishops of Spain, with Isidore of Seville's name first on their acts, declare forced baptism wrong — and rules that the Jews King Sisebut forced to the font twenty years earlier must remain Christians, on pain of the law."

The subject is now plural ("The bishops ... declare"), but the second verb kept the singular of the old subject ("A council ... rules"). A participant reads "the bishops ... rules". `Census_Text_Changes.md` shows the teaser cut off after "declare", so the error does not show there either.

Fix: "... declare forced baptism wrong — and rule that the Jews ...". Update the teaser's "New" line in `Census_Text_Changes.md` to show the whole sentence.

### N2. Philoxenus's dates line ends his time as bishop at his expulsion (`philoxenus-of-mabbug`, `dates`)

The text: "bishop 485 to 518 or 519".

The held line gives an expulsion, not the end of an episcopate: "in the second year of the reign of Justin, which was An. 830, he thrust out of Antioch Severus, and Xenaias from Mabug" (batch7 `records.json` l.478). The card's own datesNote says so, and then gives a different end: "Driven from Mabbug in the second year of the emperor Justin, the year 830 of the Greeks, which Budge reads as 518 to 519. ... François Nau gives 523 as the end of his time as bishop". His church did not hold that he stopped being bishop when he was driven out, and the map bar still ends at 523. The line now contradicts the card beside it.

Fix: "bishop from 485; driven out 518 or 519". This is the form round 1 offered ("bishop from 485; exiled 519"), with Budge's two years.

### N3. The Ladder sentence gives the Greeks' regard to the book; the held line gives it to the man (`chalcedonian-monasticism-judean-desert-and-gaza`, `legacy`)

The text: "The Greeks held it in great value, Philippe Labbe says, and Elias of Crete wrote explanations of it."

The Latin: "apud Graecos in magno pretio habitum fuisse Climacum, ut ex Athanasii quaestionibus, Elia Cretensi, Theodoro Studita, Philippo Solitario, Joanne Zonara, aliisque constat" (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` l.41362-41365, OCR normalized). "Climacum" is John, not the Ladder. The approved card has it right: "Philippe Labbe says the Greeks held him in great value." Elias "qui explanationes in Scalam scripsit" (l.41434-41435) is right as written.

Fix: "The Greeks held him in great value, Philippe Labbe says, and Elias of Crete wrote explanations of the Ladder."

A note for the card, not a finding on this branch: Labbe gives this point as the first of two heads to which he reduces what Antonius Magister "nonnulla de Climaco retulit" (l.41355-41362). "Labbe says" is true of the page, but it is Magister's point as Labbe sums it up. If the coordinator wants that told, it belongs with the card in Open-Gaps 254, not in this release.

### N4. The Nisibis story sets Labourt against the Chronicle on Sabrisho, where Labourt agrees with it (`the-church-of-the-east-under-persia`, documentedStories[1].text)

The text: "In the Chronicle the catholicos Sabrisho takes Henana's side, though Labourt reads Sabrisho's own synod as against the Henanians."

The clause on the synod is true: "Sabriso' se prononça cependant contre eux dans le synode général qu'il tint au mois d'Yar de la sixième année de Chosrau (mai 596)" (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.12231-12234). But "though" tells the reader that Labourt disputes the Chronicle's account, and he does not. Two pages on, he tells the Nisibis affair as the Chronicle does: "Chose étrange et qui peint bien cette époque si troublée : Sabriso' seconda les Henaniens dans cette affaire. Il détestait Grégoire ... le catholicos entrava de mille manières l'action de son rival" (l.12273-12279, OCR "af- faire", "11"). Labourt holds both: a synod against the party, and help to them against Gregory. Scher's introduction says the same: "le catholicos Sabriso' le défendit, et voulut même déposer Grégoire" (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.16966-16968). The witness that does contradict the Chronicle is Timothy I, as the Henana card says.

Fix: "In the Chronicle the catholicos Sabrisho takes Henana's side. Labourt finds the same odd turn: Sabrisho's own synod of 596 spoke against the Henanians, yet he helped them against Gregory."

---

## MINOR

### M1. Henana's death: "after 610" is firmer than Scher (`the-church-of-the-east-under-persia`, documentedStories[1].text)

The text: "When Henana died is told two ways in Addai Scher's notes: under the catholicos Sabrisho, who died in 604, or after 610."

Scher: "il mourut sous le patriarche Sabrjésus (596-604)" (Cause l.21023-21024) and "nous savons que Hnana vivait encore en 610 (Chronique de Séert)" (l.21734). "Still alive in 610" is what the card says. "After 610" claims he did not die in 610.

Fix: "Addai Scher's notes give his death two ways: under the catholicos Sabrisho, who died in 604, and elsewhere still alive in 610." This also drops the passive "is told two ways".

### M2. "Scarcely as many boys" (`the-church-of-the-east-under-persia`, documentedStories[1].text)

The text: "only twenty people, and scarcely as many boys, were left in the school". The Chronicle: "Il ne resta dans l'Ecole que vingt personnes et a peine autant d'enfants" (`chronicle-of-seert_histoire-nestorienne-seconde-partie-po13-ara-fra_scher1919.txt` l.28711-28712, OCR normalized). "Enfants" is children. "Boys" is likely for a school of clergy, but it is a reading.

Optional fix: "only twenty people, and scarcely as many children, were left in the school".

### M3. Julian's 543 stands in the source note of the entry whose voices line was corrected (`nubian-christianity`, sources[0].note)

The text: "The near-contemporary narrative of Nobadia's conversion (Julian 543, Longinus 569-80s) ...". This field was edited in this release (its Maccurritae clause). The Julian card's datesNote says: "John of Ephesus gives no year." S4 removed 543 from the voices line for this reason. The entry's `dates` "543-652" and the first story's `when` "543–545" rest on the same modern year.

Fix: drop "Julian 543, " from the note ("(Julian, then Longinus in the 560s to 580s)"), or carry the three uses of 543 in this entry by name in Open-Gaps 254 beside the map-years item.

### M4. The Decision-Log's quotation count does not add up as written

The text: "Of 36 quotations that first failed the check, none was a misquotation. 16 were faults in old scans ... One needed two held sources on the Victor of Tunnuna card ... The other 14 are the profiles' own English". 16 + 1 + 14 = 31. The 16 and 14 are right (see S7 above). "The other 14" makes the reader look for 5 more.

Fix: name the other five, presumably the quotation marks removed or replaced in the six profiles of the last sentence. For example: "Five more were quotation marks on words that were not quotations, or renderings with no mark; these were ...". Then "The other 14" can become "14".

### M5. Two records lines to tighten

- Decision-Log, "Decided": "The worker's recommendation on each of the preview's four questions stands as approved, as the coordinator had called them." "As the coordinator had called them" is unclear. Say what is meant, for example "as the coordinator set them out in the preview".
- Open-Gaps 247 closure lists the David, Gildas and Julian lines but not the Benedict line, which `Census_Text_Changes.md` and the Decision-Log both file under 247. Add it: "and the Benedict line of Early Benedictine / Italian Monasticism now gives 543, by his order's tradition."

### M6. The ruling text was filled in during this review

Commit `43b4bc34` replaced [RULING-TEXT], [RULING-Q1-TEXT], [RULING-Q2-TEXT] and [RULING-Q2] with Mark's approval of the preview ("Approve", version 2, questions 1 and 2). This review cannot check those words against what Mark said. The coordinator should confirm them before the PR is marked ready. [REVIEW-ROUNDS] remains a placeholder, as expected.

---

## Every changed line, checked

- **Profiles** (`git diff 477c7d3b..HEAD` on Who-Profiles and Council-Profiles: seven files). Moses of Khoren's "nouveau Platon" is Langlois's (l.24830). Victor of Vita's "nostrae civitatis" (of our city), brief and card. Caesaria. Victor of Tunnuna's two source titles. Constantius and Faustus renderings. All sound.
- **Census** (51 field differences from `477c7d3b`). Besides N1-N4 and M1-M3, all sound: the B1 lane fields, the Homoian people list, the Liberatus caveat and source note, the voices lines, the Maccurritae lines and edge, the places, and the dates lines.
- **Counts in the records.** 76 persons and 3 major councils are new against release 41. 5 persons are told within none (Boethius, Victor of Vita, Fulgentius, Procopius, Agathias), so 71 are told within. 71 new tradition-Who links and 10 council-Who links. 13 scan readings covering 16 failed quotations. 14 renderings.
- **Open-Gaps 254** carries what round 1 asked it to: audio, the SCAN map years, the Nobadae place id, `regions`, the Reccared rows, the statutes' year, the reading level of the two corrected stories, the A5 status word, and the tree-page 404 check.

## AI tells and generic voice

No assistant cadence, filler or stock hedging in any new line. The best of the new prose is plain and concrete: "The Chronicle of Seert tells it as a fight inside Nisibis." The weak spots are "is told two ways" (M1), the dangling "though" (N4) and the verb error in the teaser (N1). "In modern words" now stands beside exactly the 14 listed renderings, and in Ruricius it still appears three times in five paragraphs. That is honest, and round 1's note on it stands; it is not a finding.
