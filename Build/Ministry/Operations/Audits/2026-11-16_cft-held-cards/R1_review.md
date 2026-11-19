# R1 review: two Church Family Tree story cards against the held texts

Date: 2026-11-16. Round 1. Reviewer did not see the drafting.

Scope: `cic-website/data/world-census.json` and `cft-website/index.html`, diff against `origin/main`. When the review started the change was uncommitted. While it ran it was committed as `244943c4` on `claude/cft-held-cards` and pushed. The working tree is clean and the branch matches its remote.

Held texts used:
- AS = `cic/texts/acta-sanctorum_augusti-tomus-1-lat_1750.txt`. Line numbers are this file's own lines, not the host OCR lines in its header.
- PS = `cic/texts/john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` (Payne Smith, 1860).
- BR = `cic/texts/john-ephesus_lives-eastern-saints-po18_brooks1924.txt` (Brooks, PO 18).

Result: **2 BLOCKING, 14 NON-BLOCKING.** One of the NON-BLOCKING findings (N5) goes to Mark as an escalation note, because it touches the premise of his ruling.

---

## Card 1: "Dominic Sells His Books" (the-dominican-order, documentedStories[0])

Ruling 1 compliance: met. Jordan as source is gone. The saying is no longer credited to Jordan, and it is not in quotation marks. "Glossed in his own hand" is Stephen's own wording (`manu sua glossatos`, AS 108401). Mulchahey and the Tugwell/Jordan source entries are removed. No interpretive sentence remains.

| # | Field / sentence | Evidence | Verdict |
|---|---|---|---|
| D1 | title (unchanged) | AS 108400-108401 | OK |
| D2 | when: "undated; told at the 1233 inquest" | Stephen gives no date (AS 108387-108407). The witnesses swore "sub anno Domini MCCXXXIII" (AS 106973). Annotation c gives August 1233 (AS 106986). | OK |
| D3 | tier "2" (unchanged) | n/a | OK |
| D4 | verification: "checked directly against the primary text" | The Latin testimony is held, AS 108387-108407 | OK |
| D5 | teaser, sentence 1: famine at Palencia, books glossed in his own hand, money to the poor | AS 108396-108403 | OK |
| D6 | teaser, sentence 2: the dead-skins saying | AS 108403-108404 (`Nolo studere super pelles mortuas, & homines moriantur fame`). It is in reported speech with no quotation marks, which is correct for an English rendering of the Latin. | OK |
| D7 | text: "sworn inquest held at Bologna for Dominic's canonization" | Notary's preface: "Relatio juridica", sworn witnesses, Bologna inquisitors, Gregory IX's authority (AS 106932-106975). The commentary calls it "Relatione juridica Bononiensi" (AS 66799) and the "testes Canonizationis" (AS 66810). | OK |
| D8 | text: "Brother Stephen of Spain, prior of the friars' province of Lombardy" | "Prior provincialis Ordinis Praedicatorum provinciae Lombardiae" (AS 108387-108388). The testimony itself does not say "of Spain". That comes from the Bollandist commentary, citing Bernard Gui's notes: "juxta notas Bernardi Guidonis natione Hispanus" (AS 66797-66798). | NON-BLOCKING (N1). Supported, but by the commentary, not the testimony. Acceptable as it stands. |
| D9 | text: "known Dominic … fifteen years and more" | AS 108389-108390 | OK |
| D10 | text: "first heard this story before he ever saw him, from great men worthy of belief" | "antequam haberet per visum notitiam … audivit multa bona de eo a magnis viris fide dignis" (AS 108392-108394; cleaner OCR at AS 66806-66807) | OK |
| D11 | text: "Dominic was then a canon of Osma, prior or subprior of its church, and was studying the Scriptures at Palencia." | Stephen does say this (AS 108394-108396). But the held text itself contests it. At the same inquest, John of Spain heard that Dominic sold his books while he "erat in saeculo", still a layman studying at Palencia (AS 107996-108001). The Acta Sanctorum editors, following Echard, judge that Stephen got the timing wrong ("irrepsisse … errorem", AS 66859-66885). Jordan's Libellus §7-8, also held, puts the sale before the bishop of Osma called Dominic to be a canon (AS 92447-92470). The card gives Stephen's version as plain narration, and the caveat does not flag the dispute. | **BLOCKING (B1).** A contested detail is presented as settled. Fix: frame it as what Stephen heard ("Stephen had heard that…"), and add to the caveat that another witness at the same inquest says Dominic was still a layman then, and that the Acta Sanctorum editors judge Stephen mistaken on this point. The other option is to drop the office detail. |
| D12 | text: "A terrible famine began to spread in that region, so that many poor people there were dying of hunger." | "incepit invalescere fames pessima in regione illa, ita quod multi pauperes ibi fame moriebantur" (AS 108396-108399; AS 66810-66811) | NON-BLOCKING (N2). "Invalescere" means "grow strong", not "spread". "Grew severe" would be closer. Minor. |
| D13 | text: "Moved by compassion and mercy, Dominic sold his books, which he had glossed in his own hand." | AS 108399-108401 | OK |
| D14 | text: "He gave the money, and the other things he had, to the poor." | AS 108402-108403 | OK |
| D15 | text: "He would not study on dead skins, he said, while men were dying of hunger." | AS 108403-108404. Reported speech, no quotation marks. | OK |
| D16 | text: "Some men of great standing followed his example, Stephen said, and from then on they began to preach with him." | "cujus exemplo quidam magnae auctoritatis similia fecerunt, & ex tunc cum eo praedicare coeperunt" (AS 66818-66820; AS 108405-108407) | OK |
| D17 | caveat: "Stephen testified under oath and was a friar of Dominic's own order." | "juratus" (AS 108388). Prior provincial of the Order of Preachers (AS 108387). | OK |
| D18 | caveat: "He tells what he had heard from others before he knew Dominic, and he gives no date." | AS 108392-108394. There is no date in AS 108387-108407. | OK |
| D19 | caveat: "The words are as Stephen reported them, in Latin." | The Latin is the notaries' sworn record (Prooemium notarii, AS 106950-106975). The held text does not show that Stephen spoke Latin. | NON-BLOCKING (N3). Suggest: "The words are as the Latin record of his testimony gives them." |
| D20 | sources[0] work: "Acts of the Canonisation Process … Bologna 1233, testimony of Brother Stephen of Spain" | AS 106932-106975 and 108383-108407. "Of Spain": see D8. | OK |
| D21 | sources[0] note: "Latin in Acta Sanctorum, Augusti tomus I (Venice, 1750)" | File header, lines 1 and 4 | OK |
| D22 | sources[0] note: "English in Francis Lehner … (1964)" | Not held, so it cannot be verified. This was carried over from the old card. It is a pointer to a translation, not a claim in the story. | NON-BLOCKING (N4) |
| D23 | Escalation note on ruling 1's premise | Ruling 1 says to remove "anything no held text says, including Jordan of Saxony as its source". But Jordan's Libellus is held in the same AS file (header, lines 1-2 and 9). §7 tells the book sale (AS 92447-92461). It has no saying and no glosses. It says the books were ones he badly needed ("quos sibi oppido necessarios possidebat"), that he sold his household goods too, and that his example moved other theologians and masters to give more alms. So the old card was wrong to credit the saying and the glosses to Jordan. It was not wrong that Jordan tells the story. The card as drafted follows the ruling. | NON-BLOCKING (N5). Not a card defect. Mark should know that his ruling's premise does not hold for the sale itself, before the card is approved to proceed. |

## Card 2: "John of Ephesus Baptises the Pagans of Asia — By Order" (syriac-orthodox-west-syriac-christianity, documentedStories[1])

Ruling 2 compliance: met. "Compelling", "fear of imperial law" and the Whitby "coercive character" source are gone. Also gone are the unsupported claims of a small sum, a white garment and burned idols, the 70,000 / 96-church figures, "spend his last years in Justin II's prisons" and "He saw no contradiction".

| # | Field / sentence | Evidence | Verdict |
|---|---|---|---|
| J1 | title (unchanged): "… — By Order" | n/a | NON-BLOCKING (N6). Now that the compulsion claim is gone, "By Order" can still be read as forced baptism. It is defensible only as "by imperial commission" (PS 12034-12035: "built with my knowledge and at my command"). The title was outside the drafter's brief, so Mark should decide whether it stays. |
| J2 | when: "542 onward" | PS 217-218 (Payne Smith, from the extracts) | OK |
| J3 | tier "1" (unchanged) | n/a | OK |
| J4 | verification: "checked directly against the primary text" | Checked against English translations (PS, BR). The Syriac was not checked. | NON-BLOCKING (N7). Accurate in practice. "Against the primary text in translation" would be more exact. |
| J5 | teaser: persecuted Miaphysite bishop, Justinian's agent, "counted the churches he built" | PS 11915-11956; BR 39043-39046; PS 9006 | OK on content. NON-BLOCKING (N8): one 34-word sentence, past the ~25-word ceiling. |
| J6 | text: "chronicled the persecution of his own church by the Chalcedonian emperors accepted a commission from one of them" | Persecution in Part III under Justin II (PS 3400-3420). "The persecution in Justinian's time" (PS 5570). The commission (PS 11915-11917). | OK |
| J7 | text: "In Justinian's reign he was appointed teacher of the pagans in the four provinces of Asia, Caria, Phrygia and Lydia; … Payne Smith, dates the mission to 542." | PS 11915-11917 ("teacher of the heathen in Justinian's time in the four provinces"). PS 217-218 (542, from the extracts). | OK |
| J8 | text: "John reports the results himself." | PS III.36-37; BR ch. 47 (first person, "our meanness", BR 39043) | OK |
| J9 | text: Lives count of 80,000 converted, 98 churches, 12 monasteries, 7 churches from synagogues | BR 39043-39046 (ch. 47) | OK. NON-BLOCKING (N9): the Lives also gives a second count in ch. 43, the chapter this card cites, of "ninety-two churches and ten monasteries in four provinces" (BR 38066-38068). The card and caveat read as if the Lives had only one count. |
| J10 | text: Ecclesiastical History gives 99 new churches and 12 monasteries over the 35 years Deuterius worked with him | PS 8999-9007 (Payne Smith quotes II.44) | OK |
| J11 | text: "His deacons, he writes, uprooted altars, destroyed shrines and cut down trees." | BR 38032-38033 ("uproot altars and destroy shrines … and cut down trees in ardent religious zeal"). The four deacons "laboured … with us" (BR 37986-37989). | OK |
| J12 | text: Derira, near Tralles, temple levelled to its foundations, chief monastery built on the site | PS 11918-11937 | OK |
| J13 | text: "Justinian paid for it and for the other monasteries and churches." | PS 11954-11956 | OK |
| J14 | text: "Elsewhere he records with approval the later trials of pagans in Constantinople, some of whom were put to death." | Trials in Constantinople under Tiberius and Maurice (PS 11316-11330, 11625-11710). Executions (PS 11638-11644, 11690-11694). Approval: "the punishment which they deserved" (PS 11695-11697) and "the just reward of their deeds" (PS 11706). | OK. NON-BLOCKING (N10): most of those tried professed Christianity and practised heathen rites in secret (PS 11648-11650, 11702-11705). "Secret pagans" would be more exact than "pagans". |
| J15 | text: "He was, at the same time, a bishop of a communion the same emperor's laws declared illegal, …" | No held text says Justinian's laws declared the Miaphysite communion illegal. PS has only "the persecution in Justinian's time" (PS 5570) and Theodosius removed from his see (PS 2514). Payne Smith's preface says the reverse: John's party was "not being condemned by their opponents as heretics, and yet being separated from their communion" (PS 296-300). This sentence was carried over from the old card unchecked. | **BLOCKING (B2).** Unsupported, and the held text cuts against it. Fix: replace it with what the held texts give, e.g. "a bishop of a communion that suffered persecution in Justinian's time". |
| J16 | text (same sentence): "… and a man who would later be imprisoned under Justin II for refusing Chalcedon." | John ("our author") was imprisoned with Paul, Stephen and Elisha during Justin II's reign, under Patriarch John Scholasticus, for refusing the union (PS 3405-3420, 3895-3910) | OK. NON-BLOCKING (N11): the sentence runs to 31 words; split it when B2 is fixed. |
| J17 | text: "The tradition that built its identity on suffering imperial coercion for the sake of conscience also produced, in its most important historian, a zealous agent of an emperor's campaign against the old religion." | Interpretive. "Zealous" is fair (BR 38033; PS 11934-11937). "Built its identity on suffering … for conscience" and "most important historian" are judgments that the cited chapters do not show. | NON-BLOCKING (N12). Goes beyond the held texts, though it does not misstate them. It is also 33 words long. Consider trimming it to what the pages show. |
| J18 | text: "His own pages document both." | J6, J12-J16 | OK |
| J19 | caveat: "John of Ephesus is the sole source for his own mission" | A claim about other sources being absent, which the held texts cannot prove. Payne Smith says the Part II extracts give "almost the sole facts respecting our author" (PS 196-197). | NON-BLOCKING (N13). Hedged and not contradicted. |
| J20 | caveat: "and his two works give different round numbers" | 98, 99 and 7 are not round numbers. There are more than two counts: Lives ch. 43 (92/10, BR 38066-38068), Lives ch. 47 (BR 39043-39046), EH II.44 (PS 9006), and Payne Smith's 70,000 in four years from the Part II extracts (PS 219-221). | NON-BLOCKING (N14). Suggest: "and his works give different numbers". |
| J21 | caveat: "The date 542 is Payne Smith's, from extracts of the lost second part of John's history." | PS 186-197 (Part II survives only in extracts in Dionysius) and PS 208-218 | OK |
| J22 | sources[0]: EH Part III, III.36-37 and II.44, with III.27-34 on the trials; note on the mission, numbers and Derira | III.36 (PS 11893), III.37 (PS 11998). II.44 by position: II.41 marker at PS 8927, then "the two succeeding chapters", then Deuterius (PS 8993-8995). III.26 (PS 11014), III.28 (PS 11123), III.34 (PS 11660), III.35 (PS 11829). | OK |
| J23 | sources[1]: Lives ch. 43 (deacons) and ch. 47 (count), Brooks | Contents list (BR 39813, 39821). Ch. 43 (BR 37982-38084). Ch. 47 (BR 38839-39046). | OK |
| J24 | sources[2]: Harvey 1990 (unchanged) | Not held. No sentence depends on it alone. | NON-BLOCKING (folded into N7 and N13). Nothing to fix. |

## index.html and the rest of the census

- I parsed both files at `origin/main` and at `HEAD` and compared the full structures. In the census, exactly 11 fields changed, all on these two cards: Ephesus caveat, verification, text, teaser and sources (4 entries to 3); Dominic caveat, verification, when, text, teaser and sources (3 entries to 1). Titles and tiers are unchanged. Nothing else in the census changed.
- In `cft-website/index.html` (`const DATA`), the same 11 fields changed and nothing else did. Both cards in `index.html` are identical to the census cards. The atlas-sync regeneration matches.

## Readability (both cards)

The Dominic card holds the target: short sentences, plain words, no AI tells. The Ephesus card has several sentences of 23-34 words: the teaser (N8), J6, J7, J9, J12, J15/J16 (N11) and J17 (N12). None is a blocking finding. N8, N11 and N12 are the ones worth splitting.

## Summary of BLOCKING findings

- **B1** (Dominic, text): "Dominic was then a canon of Osma, prior or subprior" is given as fact. The same held inquest (John of Spain, AS 107996-108001), Jordan §7-8 (AS 92447-92470) and the AS editors (AS 66859-66885) contest it.
- **B2** (Ephesus, text): "a communion the same emperor's laws declared illegal" has no held support, and Payne Smith's preface (PS 296-300) cuts against it.
