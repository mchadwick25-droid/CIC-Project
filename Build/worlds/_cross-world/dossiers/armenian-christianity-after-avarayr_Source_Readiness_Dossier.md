# Source Readiness Dossier — Armenian Christianity after Avarayr

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.4
**Corpus-map slug:** `armenian-christianity-after-avarayr`
**Time window:** 451-554
**Region(s):** Armenia
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of 2026-10-23 (checked at `469dd9b2` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. The sibling `armenian-christianity-conversion-era` holds Moses of Khoren in Italian (1850) and the ANF 8 extract. Another thread vendored Ormanian's Church of Armenia (1912) and Timothy Aelurus's Refutation (an Armenian text), both now assigned here.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, 2026-10-23).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Church of Armenia (Ormanian; Gregory's English translation, 1912): chapters VII-X, the fifth and sixth centuries | ormanian | context | provisional | chapters VII-X (file lines 2101-2970), including the Council; file 81,364 words | `ormanian_church-of-armenia_gregory1912.txt` |
| Timothy Aelurus, Refutation of Chalcedon, Armenian text (1908) | timothy-aelurus | transmission | provisional | whole file; file 120,986 words | `timothy-aelurus_widerlegung-der-lehre-von-chalcedon-xcl_ter-mekerttschian-ter-minassiantz1908.txt` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- Joshua the Stylite XX-XXI (the Armenians destroy the Persian fire-temples, c. 491, file lines ~1060-1105). Context, tier 3. Wired.
- John of Ephesus HE Part III II.18-24 (the Armenian catholicos at Constantinople 571-573). Context, tier 4. Wired.
- Zachariah XII.7 (the catholicos at Dvin, ~16313-16319) and II.5 (Proclus's Tome to the Armenians, ~1367-2027). Context and antecedent (needs-ruling). Wired.
- Evagrius V.7 (the Persarmenian revolt of 572). Context, tier 4. Wired.
- PO 18's Armenian Synaxarion (Shushanik, ~5964-5966): transmission, provisional. Wired.
- Moses of Khoren Book III (to c. 440): antecedent, needs-ruling (the work's date, 5th or 8th century, is Contested). Wired.
- Duchesne III (~20912-20919) on an anti-Chalcedonian council, dated 491 by Duchesne and now to Dvin 505-06: scholarship; confidence tag needed.

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Rituale Armenorum (with the Old Armenian Lectionary) (`rituale-armenorum-lectionary_conybeare1905.txt`) | Armenian Church (anonymous) | F. C. Conybeare (ed.) | 1905 | https://archive.org/details/ritualearmenorum00cony | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Clarendon 1905; no copyright field); Appendix II located in the fetched text, 2026-10-23 |
| Collection des historiens anciens et modernes de l'Armenie, tome II (`langlois_collection-historiens-armenie-tome2-fra_1869.txt`) | Koriun; Moses of Khoren; Elishe; Lazar of Parp; Eznik | Victor Langlois (ed.); Emine; Ghesarian (French) | 1869 | https://archive.org/details/collectiondeshi02langgoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Firmin-Didot 1869); contents list read in the fetched text, 2026-10-23 |
| The History of Vartan and of the Battle of the Armenians (`eghishe_history-of-vartan-and-the-armenian-war_neumann1830.txt`) | Eghishe (Elishe) | Charles Friedrich Neumann | 1830 | https://archive.org/details/thehistoryofvartan | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1830; CC Public Domain Mark 1.0); title page read in the fetched text, 2026-10-23 |
| History of the Wars, Books I and II: The Persian War (`procopius_wars-1-2-persian_dewing1914.txt`) | Procopius of Caesarea | H. B. Dewing | 1914 | https://www.gutenberg.org/ebooks/16764 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 'First Printed 1914' and PD statement read, 2026-10-16 |
| Histoire d'Heraclius par l'eveque Sebeos (`sebeos_histoire-d-heraclius-fra_macler1904.txt`) | Sebeos | Frederic Macler (French) | 1904 | https://archive.org/details/HistoireDheracliusParLevequeSebeos | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (no date or copyright field); the OCR title page MDCCCCIV and Macler's name read in the fetched text, 2026-10-23 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Langlois tome I with Agathangelos and Faustus (archive.org chama-01-02-langlois-etal-1867-1869): antecedent material, shared with the conversion-era entry; verified, not vendored.

**Gaps (no public-domain English, or no own voice):**

- The Book of Letters has no public-domain translation (Garsoian 1999 is in copyright), so the Dvin council of 554, this entry's defining institutional act, has no primary voice in any edition we could vendor.
- Lazar of Parp and Koriun are French only (Langlois 1869); Elishe is in English (Neumann 1830).

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Thomson's Elishe (1982; historyofvardana0000eghi) and Lazar (1991) | Named in the census | In copyright; Neumann replaces Elishe. |
| Bedrosian's Lazar (GhazarParbetsisHistoryOfTheArmenians) | English Lazar | No date, rights or licence field on the host; not vendorable. |
| Norehad's Koriun (New York 1964; LifeOfMashtots) | English Koriun | US 1964, presumed in copyright. |
| Garsoian 1999, Sarkissian 1965 | Census secondary sources | Scholarship, in copyright. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Shushanik: which entry holds her Armenian synaxarion notice as tradition, and which as context (Georgia)?
- Proclus's Tome counts as an antecedent only once an Armenian own-source is shown to argue from it.
- Moses of Khoren's date is shared with the conversion-era entry and needs a confidence tag.
- The Dvin council of 505/506 brought Georgian and Albanian bishops: it serves three entries, and its primary source has no PD translation.
- The window closes in 554 but the best outside witnesses are later (572, 610). A scope question.

## 6. Build or atlas-only recommendation

**Recommendation: build.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

with a condition: carry the Dvin 554 gap as an honest_limit record, or extend the window. Own voice: Elishe (~50,000 words in English) and Lazar and Koriun in French. Good uniqueness and audience fit.
