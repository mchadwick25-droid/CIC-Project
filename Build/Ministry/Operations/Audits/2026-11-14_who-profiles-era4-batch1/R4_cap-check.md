# R4 cap check: era 4 batch 1

## Scope

One targeted check, ordered in Mark's cap ruling (2026-11-14). It does not count toward the three-round cap. It covers three changed card strings only:

1. Boniface of Mainz, card `keyWorks` item 1 `about`: the Saxons sentence.
2. Nennius, card `dates`: the Duchesne sentence.
3. Adomnán of Iona, card `uncertain` item 5: the "lover of peace" sentence.

Reviewer: independent Opus, first sight of these files. I edited no profile file, made no git writes and made no web, paid or model calls. I used local reads and a JSON load only.

## Method

- I opened every cited line in the vendored file myself and read the whole passage around it: all of Kylie's letter 46 (and Torhthelm's reply, letter 47), both of Duchesne's uses of "pseudo-Nennius", and Bede V.15 in Giles. OCR noise was read through.
- For each string I checked pronoun reference, witness, any quotation word for word, sentence length (word count), fragments and AI tells.
- I read the rest of each of the three fields, to see that the changed string sits well in it and that nothing around it reads broken.
- Each card was loaded with Python's `json.load`.

## 1. Boniface of Mainz, `keyWorks` 1 `about`: PASS

String: 'He asks them to pray that God would turn the hearts of the pagan Saxons. The Saxons themselves say, he writes, "We are of one blood and one bone."' (15, 12 words.)

- Source: `boniface_english-correspondence_kylie1911.txt` l.7487-7525, letter 46, "Boniface urges all the English to pray for the conversion of the Saxons ... About 737."
- Who "them" are: the letter is addressed to "all God-fearing Catholics, sprung from the English race" (l.7494-7495). The field's title, "Letter to all the English on the Saxons", supplies the referent. Holds.
- Who writes: "Boniface, or Wynfrith" (l.7496). "He" is Boniface. Holds.
- The prayer: l.7518-7521, "you should seek to obtain that our Lord and God Jesus Christ ... may turn to the Catholic faith the hearts of the pagan Saxons". Holds.
- The quotation: l.7522-7523, "Have pity on them because even they themselves are wont to say “¢ We are of one blood and one bone,”’". The words inside the marks are verbatim; "“¢" and "”’" are OCR. The comma becomes a full stop at the end of the card's sentence, a normal change. Holds.
- "The Saxons themselves say": "they themselves" follows "them" in "Have pity on them", and "them" is the pagan Saxons of the clause before. "Are wont to say" is a habit, which the plain present "say" carries. Torhthelm's reply calls the Saxons "our people" (l.7571), which agrees with this reading. Holds.
- Witness: Kylie, named in item 0 and in this item's "dated about 737 by Kylie" (l.7487-7488). "He writes" keeps the words Boniface's.
- Rest of the field: Torhthelm "answered with a gift and a promise of prayers" agrees with l.7572-7579 ("a gift, small indeed"; "you are constantly remembered in holy masses and in daily prayers"). The field reads in order.
- Writing: short sentences, no AI tell, no empty contrast, no fragment beyond the field's own title-continuation opening. Not a finding.

## 2. Nennius, `dates`: PASS

String: "Louis Duchesne, who calls the writer pseudo-Nennius, places him in the ninth century." (14 words.)

- Source: `liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt` l.27343-27344, "l'Historia Britonum du pseudo-Nennius (ixe siècle)". The other use, l.52070-52071, lists in a manuscript "Marci anachoretae Historia Britonum (Pseudo-Nennius)", which confirms the name is Duchesne's habit and not a slip.
- "Calls the writer pseudo-Nennius": holds. "Places him in the ninth century": Duchesne's "(ixe siècle)" sits on the work under that author's name, so dating the writer to it says no more than the line. Holds.
- Witness: Duchesne, named in the sentence.
- Rest of the field: it sets the book's own dates (858, 976, 547 years after 447), Williams ab Ithel's 674 and then Duchesne, each with its witness, and ends on the absent birth and death. The Duchesne sentence fits that sequence.
- Writing: one idea, no hedge filler, no AI tell. Not a finding.

## 3. Adomnán of Iona, `uncertain` 5: PASS

String: "So, Bede adds, this lover of peace did not have to quarrel more seriously with those who would not follow him." (21 words.)

- Source: `bede_ecclesiastical-history-english-people_giles1903.txt` l.13581-13592, V.15: "he departed this life before the next year came round, the Divine goodness so ordaining it, that as he was a great lover of peace and unity, he should be taken away to everlasting life before he should be obliged, on the return of the time of Easter, to quarrel still more seriously with those that would not follow him in the truth."
- True to the source: Bede gives the early death as God's way of sparing him that quarrel. "So" carries "so ordaining it, that". "More seriously" keeps "still more seriously". "Lover of peace" is cut from "lover of peace and unity", and "in the truth" is dropped. Neither cut changes the sense, and the sentence is not set as a quotation. Holds.
- Witness: "Bede adds" ties it to Bede, as the sentence before does ("Bede says God so ordered it ..."). "Bede adds" is fair, since the second sentence gives the purpose the first leaves out.
- Rest of the field: "Bede, who held to the Roman reckoning, tells his change of mind as a turn to the truth" agrees with l.13560-13571. The Ceolfrid sentence that follows is outside this check and was left as it stands. The four sentences read in order.
- Writing: 21 words, under the limit, no colon reveal, no tail. Not a finding.

## JSON

`boniface-of-mainz.card.json`, `nennius.card.json` and `adomnan-of-iona.card.json` each load with `json.load`. PASS.

## Findings

None. No BLOCKING or MINOR finding.

## Verdict

CLEAR.

- The Boniface sentence is true to letter 46. "Them" are the English, Boniface writes, and the quotation is verbatim (l.7518-7525).
- The Nennius sentence names Duchesne, his term and his date as he gives them (l.27343-27344, 52070-52071).
- The Adomnán sentence keeps Bede's reason for the early death with Bede, and says no more than V.15 does (l.13587-13592).
- All three meet the writing bar, and all three cards are valid JSON.
