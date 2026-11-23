# Search names batch 1: review, round 1 (Opus, 2026-11-23)

Scope: the 29 rows in `cic-website/data/search-names.json`. All 29 bases are tree bases. Each was re-read by script against `cic-website/data/world-census.json` → `movements[id = entry]` → dotted field. All 29 entries exist, all 29 fields resolve, and all 29 basis texts appear word for word. Each sentence was then read in its field for what it supports. Mark's ruling (2026-11-23) that a living heir's present name is kind "other name" is taken as given.

## Verdict per row

| # | Name | Entry | Kind | Verdict |
|---|---|---|---|---|
| 1 | Nestorian | the-church-of-the-east-under-persia | opponents | OK. "a name its opponents gave it." |
| 2 | Nestorian | persian-church-of-the-east-early | opponents | OK. "came from this church's rivals, not from itself." |
| 3 | Nestorian | the-church-of-the-east-on-the-silk-road | opponents | OK. "given to it by opponents rather than chosen by itself." |
| 4 | Nestorian | church-of-the-east-under-the-mongols | opponents | OK. "the church that Latin Europe called Nestorian": an outsider gave the name. |
| 5 | Jacobite | syriac-orthodox-west-syriac-christianity | opponents | OK. "outsiders attached ... it never called itself that." |
| 6 | Montanist | montanism-the-new-prophecy | opponents | OK. "their opponents' label." |
| 7–9 | Assyrian Church of the East | persian-early, under-persia, timur-to-hakkari | other name | OK. Each legacy line names it as a living heir. |
| 10–12 | Chaldean Catholic Church | same three | other name | OK. |
| 13 | Ancient Church of the East | persian-church-of-the-east-early | other name | OK. |
| 14–17 | Ethiopian Orthodox Tewahedo Church | four Ethiopian entries | other name | OK. Each legacy line says the same institution continues as it. |
| 18 | Eritrean Orthodox Tewahedo Church | aksumite-christianity-conversion-era | other name | OK. |
| 19 | Coptic Orthodox Church | alexandria-catechetical | other name | OK. The line attributes it as "main living heir". |
| 20 | Coptic Orthodox Church | cyrilline-miaphysite-egyptian-christianity | other name | OK. "Its line of patriarchs runs without a break to the Coptic Orthodox pope." |
| 21 | Greek Orthodox Patriarchate of Antioch | antiochene-church-third-century | other name | **Finding A** |
| 22 | Greek Orthodox Patriarchate of Jerusalem | jerusalem-liturgical-pilgrimage-christianity | other name | **Finding C** |
| 23–24 | Roman Catholic Church | latin-papal-church-gregorian, -avignon-to-lateran-v | other name | OK. |
| 25 | Church of Jesus Christ of Latter-day Saints | latter-day-saints-lds | other name | **Finding C** |
| 26 | Copts | coptic-christianity-under-early-islam | other name | OK. The sentence uses "the Copts" for this entry's community. |
| 27 | Copts | coptic-revival-under-cyril-iv | other name | OK. |
| 28 | Asia Minor | country: Turkey | older name | **Finding B** |
| 29 | Axum | aksumite-christianity | spelling | OK. The same sentence uses "Axum" for the city and "Aksumite" for its kingdom. |

Country spelling: the census spells it "Turkey" (`modernCountries[].country`, Q43). Row 28 matches. There is no Abyssinia row in the file. It is held in `Wanted.md`, so it was not reviewed here.

## Findings, by severity

**A. (Medium: misleading.) Row 21, Greek Orthodox Patriarchate of Antioch → antiochene-church-third-century.** The quoted sentence is word for word. But the next sentence in the same field says, "The Melkite Greek Catholic Church also has a patriarch of Antioch, so the line is disputed." The entry's `livingEvidence.descentConfidence` is **Contested**. The row has no way to carry that rating, so it presents a contested heir as a settled other name. Mark's ruling covers the kind for a living heir. It does not settle which heir a contested line belongs to. Fix: take the row out of the file and hold it in `Wanted.md` for Mark's ruling on contested heirs. Do not add a Melkite row to balance it, because that would stack a second claim on the first.

**B. (Medium: unsupported kind.) Row 28, Asia Minor → Turkey, "older name".** The basis says "Asia Minor, in today's Turkey". That places a region inside the country. It does not say Asia Minor was ever the name of Turkey. It was not, since Asia Minor is the Anatolian peninsula and Turkey also includes Thrace. So the sentence supports "in", not "formerly called". The census already records Asia Minor as a place (`modernCountries` place "Asia Minor", Q12824780, country Turkey). Fix: hold the row for Mark's ruling on a kind for "region within a country". Or drop it if place search already covers the census's own place names.

**C. (Low: the basis does not support the row by itself.) Rows 22 and 25.** Each basis is a source credit cut from inside a citation string in `livingEvidence.evidence`. Row 22's is "Greek Orthodox Patriarchate of Jerusalem (8 November 2026)". Row 25's is "The Church of Jesus Christ of Latter-day Saints Newsroom (31 December 2025)". On their own, these words name a publisher. They do not say the entry is that body. Fix: for row 22, quote the `livingEvidence.basis` sentence, "The church of Jerusalem is alive today as the Greek Orthodox Patriarchate, whose own news page carries entries dated November 2026." Keep the evidence credit only for the words "of Jerusalem". For row 25, quote the full citation through ": own-voice; verified." That shows the name is the church's own. Pair it with the basis sentence "The church publishes its own figures, last updated on 31 December 2025."

No other findings.
