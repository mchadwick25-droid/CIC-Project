# Opus check: era 10 Who scan after Mark's rulings of 2026-11-12

Checked: rows_all.md (scratchpad copy, read-only), the census `cic-website/data/world-census.json` (every string field of all 396 entries, plus edges and other top-level data), `cic/texts/`, `cic/corpus-map/`, and the Who scan audits for eras 1-7 and 9 (`Build/Ministry/Operations/Audits/2026-11-1*_who-scan-era*/Who_Scan_Era*.md`; no era 8 Who_Scan file exists, so Era8_Carry_Rows.md was not used). No paid calls. rows_all.md was not edited.

## Counts

| Task | Checked | CONFIRMED | CORRECTED | NOT SUPPORTED | Must move / flag |
|---|---|---|---|---|---|
| A. Newly scored rows | 5 | 4 (Ford, Lefebvre, Schutz, Antonios); 2 of the 4 also need a format fix | 1 (Gatu) | 0 | 0 |
| B. "Named in the census (no source held)" rows | 105 | 99 keep their place as LISTED | 12 status tags ("living" changed to "status unknown") | 0 | 2 must move to scored (Sun Myung Moon, Christianah Abiodun); 1 conditional (Ilia II); 1 group flag (Fellay group / Castro Mayer); 1 route defect (Yi Ki Poung) |
| C. Duplicates | 105 | 0 duplicates | - | - | 3 name hits, all different people |

The source not being held was re-confirmed for all four WANTED rows. Zero relevant hits in cic/texts or cic/corpus-map for "Desmond Ford", "Glacier View", "Investigative Judgment", "Marcel Lefebvre", "Archbishop Lefebvre", "Roger Schutz", or "Antonios" near "Eritrea" or "patriarch". The one "Brother Roger" hit is COKE 1793, a different man. The "Taiz" and "Antonios" hits are Latin or Greek patristic text. The only Lefebvre in the corpus-map is the 1907 Egyptologist.

## A. Newly scored rows

| Person | Verdict | Census entry id and field | Exact census words |
|---|---|---|---|
| Desmond Ford | CONFIRMED | seventh-day-adventist-church-twentieth-century, livingEvidence.evidence | "Census: Desmond Ford 'remained an Adventist member until his death in 2019': census statement; verification not recorded [S]" |
| Marcel Lefebvre | CONFIRMED (format fix needed) | the-post-vatican-ii-parish-world, documentedStories[1].text | "Lefebvre died in March 1991 unreconciled." and, for the age, "By 1988 he was eighty-two" |
| Roger Schutz | CONFIRMED | ecumenical-community-worlds-taize-and-iona, voices[1], longDescription, statusDescription, documentedStories[0].text, sources[0].work | voices[1]: "murdered on 16 August 2005"; story: "stabbed Brother Roger three times in the neck; he was ninety and died within minutes"; sources[0]: "Roger d. 2005 to Alois" |
| Antonios, patriarch of Eritrea | CONFIRMED (format fix needed) | modern-ethiopian-and-eritrean-christianity, sources[2].work and livingEvidence.evidence | sources[2]: "Patriarch Antonios deposed/house arrest 2006 (d. 2022)"; livingEvidence: "Patriarch Antonios held until his death (2022), per church factions and rights monitors" |
| John G. Gatu | CORRECTED | lausanne-era-global-evangelicalism, sources[12].work; the-ecumenical-movement-and-the-wcc, sources[5].work | "WCC, obituary of John G. Gatu"; "the WCC's obituary of John Gatu" |

**Does Gatu's obituary title count as the census stating his death?** Yes, narrowly. It sits in a text field of an era 10 entry (`sources[].work`, in two entries), and an obituary asserts death by definition. It gives no year, so the Dates cell must say the year is not stated. A "tribute" is different: Dobson's 2025 HSLDA tribute does not count (see B).

**Gatu: two further errors in the row.**
- The Ruling cell says "The entry text does not say what he did". That is wrong. lausanne-era-global-evangelicalism, relationsSummary: "In 1971 the Kenyan theologian John Gatu called for a moratorium on missionaries." The-ecumenical-movement-and-the-wcc, relationsSummary: "In 1971 the Kenyan theologian John Gatu first called for a moratorium on missionaries." The same entry's sources[5].note adds: "Gatu first made the call in 1971; where he made it is disputed."
- So his part in the movement is stated, his death is stated by the obituary title, and none of his own text is held. The row should become WANTED.

**Format fixes.**
- **Antonios:** the row has 13 cells, not 12. The grep note ("grep \"Antonios.{0,20}Eritrea\" over cic/texts: no hit ...") sits in its own cell between Source wanted and Check. It belongs in Evidence.
- **Lefebvre:** the Confidence cell (cell 10) is empty.

## Table of rows that are CORRECTED, NOT SUPPORTED, or must move (paste-ready)

### A1. John G. Gatu (CORRECTED: LISTED to WANTED)

```
| John G. Gatu | death stated by a census source title only, year not given (lausanne-era-global-evangelicalism, sources: "WCC, obituary of John G. Gatu"; the-ecumenical-movement-and-the-wcc, sources: "the WCC's obituary of John Gatu") | Lausanne-Era Global Evangelicalism; The Ecumenical Movement and the WCC | WANTED | Not held | No held line. Greps over cic/texts: "Gatu" as a whole word hits only Greek and Latin files (OCR noise); "Moratorium" hits only one Luther volume, an unrelated use. | Should be WHO (voice), thin: the census says "In 1971 the Kenyan theologian John Gatu called for a moratorium on missionaries" (lausanne-era-global-evangelicalism, relationsSummary; the-ecumenical-movement-and-the-wcc says "first called"), and that at Lausanne in 1974 a broad moratorium "appeared to be rejected by most leaders". Where he made the call is disputed (the-ecumenical-movement-and-the-wcc, sources note). Nothing of his own is held. His death rests on a source title (an obituary), with no year: counted as stated under Mark's ruling of 2026-11-12, flagged for the coordinator. | Gatu's 1971 moratorium call in his own words [not named in the census; to locate]; Christianity Today, "What's Behind the Idea of a Missionary Moratorium?" (November 1974); the WCC obituary of John G. Gatu (census SOURCES) | judgment call | Inferential-Thin (no held line; census only) | found in text (relationsSummary of lausanne-era-global-evangelicalism and of the-ecumenical-movement-and-the-wcc) | no |
```

### A2. Antonios (CONFIRMED; format fix only, the grep note moves into Evidence)

```
| Antonios, patriarch of Eritrea | deposed 2006, under house arrest; died 2022 (census SOURCES; death stated in the census entry only) | Modern Ethiopian & Eritrean Christianity | WANTED | Would be: Life told by another | None held. Grep "Antonios.{0,20}Eritrea" over cic/texts: no hit ("Eritrea" alone appears only in Kebra Nagast, Castanhoso and Eusebius, earlier works). | Story-type: a patriarch deposed and confined by the state (census WHY). No own voice named. | Eritrean church records of the 1993 autocephaly and the 2006 deposition; Binns (2017) (census SOURCES) [suggested; to confirm] | clear | Documented (census entry only) | named voice (modern-ethiopian-and-eritrean-christianity, voice 4) | no: a recent head under pressure |
```

### A3. Lefebvre (CONFIRMED; fill the blank Confidence cell)

In cell 10, replace the empty cell with `Inferential-Thin (no held line; census only)`. This matches the Schutz row, which is the same case. The rest of the row stands.

### B1. Sun Myung Moon (MUST MOVE: LISTED to scored WANTED)

The row says the census "does not state" his death. That is wrong. iglesia-ni-cristo-the-way-international-unificat, livingEvidence.evidence: "Unification Church: Moon d. 2012". This fits the entry's legacy line, "The Unification Church was still led by its founder" (the 2010 frame).

```
| Sun Myung Moon | died 2012 (death stated in the census entry only: iglesia-ni-cristo-the-way-international-unificat, livingEvidence, "Unification Church: Moon d. 2012") | The Way International; Unification Church; La Luz del Mundo | WANTED | Would be: Own work | No held line. Grep of cic/texts for "Sun Myung": no hit. | Should be WHO: founded the Unification Church in Seoul on 1 May 1954; the Divine Principle (1966) is its foundational text (census voice); a federal jury convicted him in 1982 of filing false tax returns (census legacy). Nothing of his is held. Death stated in the census entry only (Mark's ruling of 2026-11-12, recent deaths). | The Divine Principle (1966) [named in the census; not held] | clear | Inferential-Thin (no held line; census only) | named voice (iglesia-ni-cristo-the-way-international-unificat, voices[1]) | judgment call |
```

### B2. Christianah Abiodun (MUST MOVE: LISTED to scored WANTED)

The row says she "died 1994 (common knowledge)". The census states it. african-initiated-churches-harrist-aladura-zioni, documentedStories[1].text: "She led her branch for sixty-five years, was called Captain Abiodun, and died in 1994". The row's "in cic/texts" is also wrong: a grep for "Abiodun" in cic/texts returns 0 files.

```
| Christianah Abiodun (Captain Abiodun) | died 1994 (death stated in the census entry only: african-initiated-churches-harrist-aladura-zioni, story, "She led her branch for sixty-five years, was called Captain Abiodun, and died in 1994") | African-Initiated Churches (Aladura) | WANTED | Would be: Own work + life told by another | No held line. Grep of cic/texts for "Abiodun": no hit. | Should be WHO: by the census story the Cherubim and Seraphim began in her trance (her account of the vision of June 1925); in 1929 she and Orimolade fell out, and her followers formed the Cherubim and Seraphim Society under her. The movement's histories name her co-founder. Her own account is named in the census sources but not held. Death stated in the census entry only (Mark's ruling of 2026-11-12, recent deaths). | Christianah Abiodun Emmanuel, account of the vision of June 1925 and the founding of the Cherubim and Seraphim, in the Society's own publications; J. D. Y. Peel, Aladura (1968) [named in the census; not held] | clear | Inferential-Thin (no held line; census only) | found in text (african-initiated-churches-harrist-aladura-zioni, story 2) | judgment call |
```

### B3. Ilia II (CONDITIONAL: needs a coordinator or Mark call on scope)

The era 10 entry (the-georgian-orthodox-church-restored) does not state his death. It says he "still held the office in 2010" and cites a patriarchate news item of 21 May 2026.

The census does state his death in an **era 5** entry. the-georgian-golden-age, livingEvidence.evidence: "Georgian Orthodox Church confirms Locum Tenens, establishes funeral commission for Patriarch Ilia II, Georgia Today (18 March 2026): independent; verified."

The ruling as written covers "any text field of the era 10 entries". Under that letter, the row stays LISTED. If the census counts as a whole, he moves to scored.

If the row stays LISTED, the Ruling cell's "Living or unknown" should read "status unknown: treated as living". The death statement sits in the era 5 entry only.

If the row moves, the Dates cell would read: `died by March 2026 (death stated in the census, era 5 entry only: the-georgian-golden-age, livingEvidence, "establishes funeral commission for Patriarch Ilia II", Georgia Today, 18 March 2026); Catholicos-Patriarch from 1977`

### B4. Group flag: Bernard Fellay; Tissier de Mallerais; Williamson; de Galarreta; Antônio de Castro Mayer

The group row does not need to move. One member is flagged.

The census story names six excommunicated men: Lefebvre, Castro Mayer and the four new bishops. It says "Benedict XVI lifted the excommunications of the four surviving bishops" (2009). Lefebvre's death is stated. Castro Mayer's is not: the text can be read as implying he did not survive, but it does not say so.

All five stay "status unknown: treated as living". Castro Mayer is the one assisting bishop, not one of the four consecrated, so consider splitting him out to keep the group uniform.

No other pair or group row has one member's death stated and another's not. Rows checked: the Joaquín pair, the Winters, LaHaye and Jenkins, the Moores, the Stahls and Camacho, Ghiuș and Boghiu, Farris and Smith, McCartney and Wardell, Pelvetsky and Melnyk, the Ranaghans, Stanley, Kennedy and Dixon, the Jackson, Taylor and Booth group, Read and Anderson, Driscoll and Nicholas, Abblé and the others, and the Hebrew Roots trio.

### B5. Route defect: Yi Ki Poung

The census does not name him: 0 hits for any spelling. He is in a held source. UNDER (underwood_call-of-korea_1908.txt) 6487: "One of the seven men ordained, Yi Ki Poung, was set aside as missionary to the island of Quelpart". 6494: "Sixteen years ago, he stoned me on the streets of Pyeng Yang".

So the Route "Named in the census (no source held)" and the Source tag "census text" are both wrong. The Route should be a held-source route, and the Source tag `found in text (UNDER 6487, 6494)`. The held line does not state his death (the book is from 1908).

### B6. Status tag corrections ("living" with no sign of living in the census)

Each of these is tagged "living: Listed only until death". In each case the census gives no sign the person is alive: no dated act after 2010 and no present-tense statement. Change the tag to `status unknown: treated as living`.

| Row | Person | Latest dated act in the census |
|---|---|---|
| 141 | Edir Macedo | founding of IURD, 1977 (voice only) |
| 146 | Matthew Ashimolowo | KICC 1992; Charity Commission story, no later date |
| 147 | Sunday Adelaja | 2009 charges |
| 151 | Eduardo Manalo | "Succession to Eduardo Manalo (2009)" |
| 204 | Kevin Ranaghan; Dorothy Ranaghan | Catholic Pentecostals (1969) |
| 209 | Gustavo Gutiérrez | Teología de la liberación (1971) |
| 210 | Leonardo Boff | Ecclesiogenesis (1977) |
| 211 | Yosyp Terelya | Chronicle samizdat from 1984 |
| 212 | Antonii Pelvetsky; Mykhailo Melnyk | consecrated bishops in Kyiv, February 1946. The "living" tag is unsupported, and these two are the clearest case: see the observation below. |
| 218 | Enrique Dussel | CEHILA founded under him, 1973 |
| 219 | Sigitas Tamkevičius | Chronicle 1972-1989 |
| 237 | John Bell | Wild Goose material, no date |

"Living" is correctly kept for Leo XIV, who has a "video message to a conference on China (5 November 2026)", and for Naasón Joaquín García, for whom the census gives a "2022 California guilty plea and sentencing".

### Cases checked and left as LISTED, status unknown

None of these states a death:
- **David Koresh:** the census gives the fire's death toll (76) and "Koresh's own account of the seven seals was left unfinished". It never names him among the dead. The row stands.
- **James Dobson:** "Michael Farris, 'A Tribute to Dr. James Dobson', HSLDA (21 August 2025)". A tribute is not a death notice. The row stands.
- **Shenouda III:** "Shenouda III's books (1971-2012)" is the span of his books, not of his life. The row stands.
- **Georgi Vins:** "Lidia Vins, whose husband had died in the camps" is about his father. The row stands.
- **Chuck Smith:** he speaks at someone else's funeral (1993). The row stands.

The other 89 rows were grepped across the whole census (death words within 200 characters of the name) and across cic/texts. No death statement was found.

### Observation (not a ruling question; for the coordinator)

The scan scores people who died before 1990 as "d. before 1990; death not in a held source (Widely Accepted)" (for example Pius X, Kimbangu and Lenshina). Some of the 105 LISTED rows look, by this checker's common knowledge only, like pre-1990 deaths. Under that same convention they would be scored, not listed:
- Minnie Abrams (d. 1912)
- Yi Ki Poung (d. 1942)
- Fernando Stahl (d. 1950)
- Mykhailo Melnyk (d. 1955)
- Antonii Pelvetsky (d. 1957)
- Norman Binsted (d. 1961)
- Joseph Naayem (d. 1964)
- A. M. Burton (d. 1966)
- Ana Stahl (d. 1968)
- Suzuki Masahisa (d. 1969)
- Isabelo de los Reyes Jr. (d. 1971)
- Roy Allan Anderson (d. 1985)

These dates are not from a held source or the census, so verify them before acting. Mark's ruling (2) covers deaths in 1990 or later, so it does not settle these.

## C. Duplicates

None. A first-column match across rows_all.md and the era 1-7 and 9 Who scans found three name hits, all different people:
- "Macedo" is Antonio de Macedo Costa (era 9) and Macedonius (era 2), not Edir Macedo.
- "Isabelo de los Reyes" in era 9 is the father, paired with Aglipay. The era 10 row is the son, Isabelo de los Reyes Jr.

Brother Alois appears in the Schutz row's Ruling text only, not as a scored row.
