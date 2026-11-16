# R2 recheck: two Church Family Tree story cards against the held texts

Date: 2026-11-16. Round 2, a targeted recheck of what changed since `R1_review.md`, as set out in `R1_changes.md`.

Scope: `git diff HEAD -- cic-website/data/world-census.json cft-website/index.html` on `claude/cft-held-cards` (uncommitted). Cards: the-dominican-order documentedStories[0], syriac-orthodox-west-syriac-christianity documentedStories[1].

Held texts, with line numbers from each file:
- AS = `cic/texts/acta-sanctorum_augusti-tomus-1-lat_1750.txt` (Latin OCR, long-s read as f)
- PS = `cic/texts/john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`
- BR = `cic/texts/john-ephesus_lives-eastern-saints-po18_brooks1924.txt`

Result: **0 BLOCKING, 8 NON-BLOCKING.** Both round 1 BLOCKING findings are resolved. The project lead's rulings, as he meant them, are carried out on both cards.

---

## Round 1 BLOCKING findings

| R1 | Status | Evidence |
|---|---|---|
| B1 (Dominic: "then a canon of Osma, prior or subprior" given as fact) | **Resolved** | The office detail is gone from the text. The layman-or-canon difference now sits only in the caveat. Both inquest witnesses are named and neither version is given as settled: John of Spain, "erat io feculo" (AS 107998); Stephen, "cum effet Prior vel Supprior eccJcGz Oxomenfis, cujaf erat Cmonicus" (AS 108395-108396). |
| B2 (Ephesus: "a communion the same emperor's laws declared illegal") | **Resolved** | Replaced by "Yet his own church suffered persecution in Justinian's time". PS 5569-5570: "in the height of the persecution in Justinian's time" (Cappadocian monks expelled from Gordison). |

## Imprisonment under Justin II

"he would later be imprisoned under Justin II for refusing Chalcedon": **supported.** Paul, "John (our author)", Stephen and Elisha were all held in one prison (PS 3414-3417). They answered that they would unite only if allowed to "excommunicate and eject ... the Synod of Chalcedon" (PS 3454-3462). The king is Justin, who framed a union edict and sent it to the bishops in prison (PS 3638-3643). He and Sophia receive the prisoners at PS 4250-4251, so this is Justin II. After a brief yielding they were "again delivered up to prison and to tortures even more severe" (PS 4238-4241). The sentence does not claim John never yielded, so it holds as written.

## Card 1: "Dominic Sells His Books"

| # | Field / sentence | Evidence | Verdict |
|---|---|---|---|
| D1 | when: "undated; while he studied at Palencia" | Jordan "cum Paleatix ftudent..." (AS 92447); John "ftudebit Palentiz" (AS 107998-107999); Stephen "ftudebac apud Paiendam" (AS 108396). No year in any of them. | OK |
| D2 | teaser, s1: famine at Palencia, books sold, money to the poor | AS 92447-92459 | OK |
| D3 | teaser, s2: "One witness adds ... glossed in his own hand ... dead skins" | Stephen only: AS 108401-108404. Jordan (AS 92447-92463) and John (AS 107996-108004) have neither detail. | OK. 26 words, just past the ~25 ceiling (N1). |
| D4 | "Three early witnesses tell this story." | Jordan, John of Spain, Stephen | OK (see N2 on "again") |
| D5 | "Jordan of Saxony, in his Libellus on the beginnings of the order" | File header lines 1-2; prologue addressed to the brothers of the Order of Preachers by "Jordanis" (AS 92260-92262) | OK |
| D6 | "...while Dominic was studying at Palencia, a severe famine struck almost all of Spain." | "orta eft fames valida fere per univerfam ... Hifpaniam" (AS 92447-92450, garbled OCR but readable) | OK. 28 words (N1). |
| D7 | "Moved by the needs of the poor, Dominic sold his books, which he greatly needed, and all his household goods, and gave the money to the poor." | "pauperum neceflitate permotus" (AS 92450-92451); "Vendens ... libros, quos fibi oppido neceffarios poffidebat" (AS 92456-92457); "[cum omni fupellectile fua]" (AS 92457-92458); "dedit pauperibus" (AS 92459) | OK. The household-goods phrase is bracketed in the edition, but the editors' own summary and commentary give it as Jordan's: "libros & fupellectilem diftrahit" (AS 64175), "libros & omnem fuam fupellectilem ... vendidit" (AS 66780-66781). 27 words (N1). |
| D8 | "His example, Jordan says, moved other theologians and masters to give alms more freely." | "cujus pietatis exemplum ... aliorum theologorum ac magiftrorum animos provocavit ... eleemofynis ex tunc largioribus abundarent" (AS 92459-92463) | OK |
| D9 | "At the inquest held at Bologna ... two friars told the story again under oath." | John "juratus" (AS 107807-107808); Stephen "jurat us" (AS 108388). Inquest at Bologna (AS 106932-106975, per R1). | OK. On "again", see N2. |
| D10 | "Brother John of Spain had heard it from Dominic's fellow canons and from many other men worthy of belief." | "fe audivifle a concanonicis dicti F. Dominici, & a multis aliis viris fide dignis" (AS 107996-107997); "Frater Johannes Hifpanus facerdos de Ordine Praedicatorum" (AS 107807-107808) | OK |
| D11 | "In his telling, the famine was so bad that many of the poor were dying, and Dominic sold his books and everything he had to feed them." | "invaluit fames ... ita quod pauperes fame affligebantur, & multi moriebantur ... vendidit libros & omnia, quae habebat, & dedit pro cibo pauperum" (AS 107999-108004) | OK. 27 words (N1). |
| D12 | "Brother Stephen, prior of the friars' province of Lombardy, had heard it from great men worthy of belief before he ever saw Dominic." | AS 108387-108394 | OK |
| D13 | "He adds two details. The books were glossed in Dominic's own hand. And Dominic said he would not study on dead skins while men were dying of hunger." | "manu fua gloftitos" (AS 108401); "Nolo ftudere fuper pelles mortuas, & homines moriantur fame" (AS 108403-108404). Reported speech, no quotation marks. | OK |
| D14 | "Some men of great standing followed his example, Stephen said, and from then on they began to preach with him." | AS 108405-108407 (unchanged from R1) | OK |
| D15 | caveat: "All three witnesses belonged to Dominic's own order" | Jordan: prologue (AS 92260-92262) and "Frater Jordanus, Magifter Ordiois Prsdicato[rum]" (AS 102500). John: AS 107807. Stephen: AS 108387. | OK |
| D16 | caveat: "and the two at the inquest tell what they had heard from others" | AS 107996-107997; AS 108392-108394 | OK. Jordan's own source is left unstated (N3). |
| D17 | caveat: "John of Spain says Dominic was still a layman, while Stephen says he was already a canon of Osma." | John: "erat io feculo" (AS 107998). The AS editors read it the same way: "quando ipfe F. Dominicus erat in feculo" (AS 66862-66863). Stephen: AS 108395-108396. Both views are named and neither is settled. | OK on the ruling. "Layman" goes a little past the Latin (N4). |
| D18 | caveat: "None gives a year. The saying is as the inquest recorded it, in Latin." | No year in AS 92447-92463, 107996-108004 or 108387-108407. The Latin is the notaries' record (R1 N3). | OK |
| D19 | sources[0]: Jordan, Libellus §7. Note: famine and sale; Latin in AS; English in Tugwell, *Early Dominicans* (1982) | §7 marker at AS 92447. Tugwell is not held. | OK. See N5. |
| D20 | sources[1]: inquest, "testimonies of Brother John of Spain and Brother Stephen of Spain"; note: the sale, glossed books, saying | AS 107807ff, 108387ff. Stephen "of Spain" rests on the commentary (AS 66797-66798, R1 N1). | OK. The text now says "Brother Stephen" while the source line keeps "of Spain" (N6). |

No rendering of Latin is in quotation marks anywhere in the card.

## Card 2: "John of Ephesus Converts the Pagans of Asia for Justinian"

| # | Field / sentence | Evidence | Verdict |
|---|---|---|---|
| J1 | title | Appointed "teacher of the heathen in Justinian's time" (PS 11915-11916). "Converted many thousands from the error of idol worship" (PS 11919-11920). Funded "by king Justinian" (PS 11955-11956). Justinian of the monastery: "built with my knowledge and at my command" (PS 12040-12041; the king is Justinian, PS 12019). Lives: "eighty thousand were converted" (BR 39043). | OK. "By Order" is gone. The title claims nothing beyond the held chapters: "Converts" is John's own claim, and the card frames it as his. |
| J2 | text: two sentences where one stood (542 date; Lives count) | PS 11915-11917; PS 217-218; BR 39040-39046 | OK, wording unchanged |
| J3 | text: "...the later trials in Constantinople of people accused of secret pagan worship, some of whom were put to death." | Trials and death sentences (PS 11638-11645, 11688-11692). Approval: "the punishment which they deserved" (PS 11692). Secret heathen rites under a Christian profession (PS 11648-11650, 11702-11705, per R1). | OK. 25 words. |
| J4 | text: "Yet his own church suffered persecution in Justinian's time, and he would later be imprisoned under Justin II for refusing Chalcedon." | PS 5569-5570; imprisonment as above | OK |
| J5 | text: "His own pages record both: the persecution his church suffered, and the campaign he led for an emperor against the old religion." | Persecution (PS 5569-5570, 3414-3462); campaign (PS 11915-11956; BR 38030-38033, 39040-39046) | OK. The interpretive sentence of R1 N12 is gone. |
| J6 | caveat: "the only held source for his own mission, and his counts differ from one chapter to another" | BR 38066-38068 (ch. 43), BR 39043-39046 (ch. 47), PS 9006 (II.44) | OK on substance. "Held" is internal jargon on a public page (N7). |
| J7 | teaser (unchanged) | n/a | Still one 34-word sentence (R1 N8, not addressed) (N8). |
| J8 | sources[0] work: "...with III.27–34 on the trials of pagans" (unchanged) | n/a | Minor mismatch with the new text's "people accused of secret pagan worship". Folded into N8. |

## index.html against the census

The added and removed lines in `cft-website/index.html` are identical to those in `world-census.json`, once `\uXXXX` escapes are decoded and indentation is stripped (checked with `diff`). Every field of both cards in the census, including all source entries, appears verbatim in `index.html`. `git status` shows only these two files modified, plus the untracked audit folder. Only these two cards changed: 23 lines in each file.

## NON-BLOCKING findings

- **N1 (Dominic, length).** Four sentences run 26-28 words: the second teaser sentence and the text's sentences 2, 3 and 7. Splitting each in two would bring them under the ~25-word ceiling.
- **N2 (Dominic, "again").** "Two friars told the story again" suggests Jordan's telling came first. The held file does not date the Libellus against the August 1233 inquest. Dropping "again" removes the implication.
- **N3 (Dominic, caveat).** The caveat says the two inquest witnesses report hearsay but is silent on Jordan, who names no source for this episode (AS 92447-92463). A reader may infer Jordan saw it himself. Suggest: "None of the three says he saw it himself."
- **N4 (Dominic, "layman").** "In feculo" (AS 107998) means "in the world", not yet in religious life. It does not say whether he was a cleric. "Was still a layman" adds that. Suggest: "John of Spain says Dominic had not yet entered religious life". This is a plain English rendering, with no quotation marks.
- **N5 (Dominic, Tugwell).** The Tugwell *Early Dominicans* pointer is back, now as a translation pointer on the Jordan source. It is not held and cannot be checked here. It carries no claim in the story, like the Lehner pointer (R1 N4).
- **N6 (Dominic, "of Spain").** The text now calls him "Brother Stephen", but sources[1] still says "Brother Stephen of Spain". That name is supported only by the commentary (AS 66797-66798). Make them consistent one way or the other.
- **N7 (Ephesus, caveat jargon).** "The only held source" uses the project's internal term on a participant-facing page. Suggest: "John of Ephesus is our only source for his own mission".
- **N8 (Ephesus, carry-overs).** The teaser is still one 34-word sentence (R1 N8). The sources[0] label "on the trials of pagans" no longer matches the text's wording.

## Summary

No BLOCKING findings. B1 and B2 are resolved. The Justin II imprisonment sentence is supported (PS 3414-3461, 3638-3643, 4238-4251). Dominic follows the ruling as meant: Jordan §7 is the source for the famine and the sale, Stephen carries the glosses and the saying, John of Spain is the second witness to the sale, and the layman-or-canon difference is only in the caveat with both witnesses named. The Ephesus title no longer says "By Order" and claims nothing the held chapters do not say. index.html matches the census, and nothing else changed.
