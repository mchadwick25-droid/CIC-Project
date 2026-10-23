# Source Readiness Dossier — Chalcedonian Monasticism - Judean Desert and Gaza

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.5
**Corpus-map slug:** `chalcedonian-monasticism-judean-desert-and-gaza`
**Time window:** c. 450-614
**Region(s):** Palestine, Sinai
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of October 2026 (checked at `9675d7e3` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. Two files vendored on September 2026 under this entry were found this pass to hold other contents: the file named for Dorotheus's PG 88 is PG 87.3 (Moschus's Pratum and Sophronius) and the Cotelier file is tomus II (the Vita Euthymii only, no Vita Sabae). Both were renamed and corrected (decision log, October 2026). Other threads vendored Raabe's Peter the Iberian and PO 8 (the Plerophories), assigned here as context.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, October 2026).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Council of Chalcedon (451): Extracts from the Acts, Definition of Faith, Canons | council-of-chalcedon-451 | tradition | assigned | div1 11 — acts extracts, Definition 11.13, canons 11.18 (the; file 434,289 words | `npnf214_seven-ecumenical-councils.xml` |
| Vita Euthymii | cyril-scythopolis | context | provisional | confirmed present ('EUTHYMII VITA' header found); file file not present | `cyril-scythopolis_vita-sabae-euthymii-grc-lat_cotelier1681.txt` |
| Vita Sabae | cyril-scythopolis | tradition | provisional | confirmed present; ch. 83-90 not individually pinpointed - s; file file not present | `cyril-scythopolis_vita-sabae-euthymii-grc-lat_cotelier1681.txt` |
| Doctrinae Diversae | dorotheus-gaza | tradition | assigned | whole file; file file not present | `dorotheus-gaza_doctrinae-instructiones-grc-lat_migne-pg88.txt` |
| John Rufus, Plerophories (PO 8.1, 1912) | john-rufus | context | provisional | fascicle I from file line 224; Juvenal and the Jerusalem rev; file 365,127 words | `po08_john-rufus-plerophories-and-others-fra_1912.txt` |
| The Syriac Life of Peter the Iberian (Raabe, 1895) | life-of-peter-the-iberian | context | provisional | whole file; Juvenal and the Jerusalem revolt 2726-2806; file 64,362 words | `life-of-peter-the-iberian_petrus-der-iberer-deu_raabe1895.txt` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- John Moschus's Pratum Spirituale, now correctly identified in the renamed PG 87.3 file (raw lines ~3369-25000, ~120,000 words) and Cotelier's extra Moschus chapters (~46168-59653, ~37,000 words). Tier 1. Wired as tradition, second witness.
- Cyril of Scythopolis, Vita Euthymii (Cotelier tomus II, raw ~26790-45800). Re-rowed as tradition (it was context). The Vita Sabae row was withdrawn.
- Evagrius IV.33 (Barsanuphius, raw ~9257-9277), IV.7 (Zosimas, ~7976-8080) and Severus at Maiuma (~6990-7003): the only vendored English words about Barsanuphius. Context. Wired.
- Zachariah III.3-5 (the monks' revolt after Chalcedon, Peter the Iberian; Zachariah was a native of Gaza), raw ~2062-2750. Context (the rival side). Wired.
- npnf214 Constantinople II, the anathemas against Origen (12.9-12.10): the outcome of the New Laura's Origenist crisis. Context. Wired.
- Bernard 1896 PPTS vol. 1 extracts of the Breviarius, Theodosius and Antoninus; John of Ephesus PO 19 notices of Euthymius; Severus's letters: context, low. Not separately wired.

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Library of the Palestine Pilgrims' Text Society, vol. II (Eucherius, Breviarius, Theodosius, Procopius Buildings, Antoninus of Pia (`ppts-v2_eucherius-breviary-theodosius-procopius-antoninus_stewart1890-97.txt`) | Theodosius; Antoninus of Piacenza; Eucherius (attrib.); Procopius | Aubrey Stewart | 1896 | https://archive.org/details/p2libraryofpales01paleuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); the four parts' title pages read in the fetched text, October 2026 |
| Analecta Bollandiana 7 (1888): Antony of Choziba, Vita sancti Georgii Chozibitae (`antony-of-choziba_vita-georgii-chozibitae-analecta-bollandiana-7-grc_1888.txt`) | Antony of Choziba | C. Houze (ed., Greek) | 1888 | https://archive.org/details/sim_analecta-bollandiana_1888_7 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1888; no copyright field); the Life's heading located in the fetched text, October 2026 |
| Patrologia Graeca 88: Dorotheus of Gaza, Barsanuphius and John (questions), John Climacus, Agathias, Cosmas, John the Faster (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt`) | Dorotheus of Gaza; John Climacus; Agathias; and others | Migne (Greek with Latin) | 1860 | https://archive.org/details/pg-88 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (no copyright field; 1860 imprint); running heads 'S. DOROTHEI ABBATIS' and 'S. JOANNIS CLIMACI' and the Barsanuphius 'Interrogatio' section located in the fetched text, October 2026 |
| Vita Sabae and Vita Euthymii (`cyril-scythopolis_vita-euthymii-cotelier-monumenta-v2-grc-lat_1681.txt`) | Cyril of Scythopolis | Cotelier (ed.), Ecclesiae Graecae Monumenta | 1681 | https://archive.org/details/bub_gb_1Z5eE88JWfIC | pd-us-by-date | Claude (tech-readiness build thread): re-vendored from a stale, unmerged PR's own already-located acquisition; source and rights independently re-confirmed against archive.org directly for a representative sample of this batch |
| Doctrinae Diversae (`john-moschus_pratum-spirituale-sophronius-opera-grc-lat_migne-pg87-3.txt`) | Dorotheus of Gaza |  | 1860 | https://archive.org/details/bim_early-english-books-1641-1700_patrologiae-cursus-completus-_1860_88 | pd-us-by-date | Claude (tech-readiness build thread): re-vendored from a stale, unmerged PR's own already-located acquisition; source and rights independently re-confirmed against archive.org directly for a representative sample of this batch |
| Of the Buildings of Justinian (`procopius_buildings_stewart1888.txt`) | Procopius of Caesarea | Aubrey Stewart | 1888 | https://www.gutenberg.org/ebooks/65404 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 1888 imprint and PD statement read, October 2026 |
| Patrologia Orientalis II: Vie de Sévère par Zacharie le Scholastique; Vie de Sévère par Jean de Beith-Aphthonia (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt`) | Zacharias Scholasticus; John of Beth Aphthonia | M.-A. Kugener (Syriac text with French translation) | 1903 | https://archive.org/details/patrologiaorient02pariuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); 'VIE DE SEVERE, PAR ZACHARIE LE SCHOLASTIQUE' title line read in the fetched text, October 2026 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Cotelier tomus III (1686; archive.org bub_gb_PLhdE15tQTAC), which holds the Vita Sabae: Creative Commons Public Domain Mark, but the OCR reads Latin and Greek as Cyrillic and is unusable. Needs fresh OCR from the page images.
- Nau, Plerophories (Paris 1899; lesplrophories00joanuoft) and PO 2 Vie de Severe: the PO 8 and PO 2 volumes are the editions vendored.

**Gaps (no public-domain English, or no own voice):**

- No public-domain English of Barsanuphius and John, Cyril of Scythopolis, John Moschus or Dorotheus exists (Chryssavgis 2006-07, Price 1991, Wortley 1992, Wheeler 1977 are in copyright).
- Own voice in PD English is close to zero; in Latin and Greek it is substantial (Moschus ~157,000 words, the Vita Euthymii ~50,000, Dorotheus with the Barsanuphius questions), all second-witness OCR.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Barsanuphius and John, Letters (Chryssavgis; Sources Chretiennes 1997) | The census's chief voices | In copyright; archive.org copies are lending-only. The 1816 Venice Greek edition was not found. |
| fathers-of-the-church-a-new-translation-147-volumes | A bulk upload | An in-copyright series; never usable. |
| John Climacus, Holy Ladder of Perfection (1858) | English Ladder | Not confirmed on archive.org; Moore 1959 is in copyright. The Greek-Latin Ladder is in the PG 88 file. |
| Dorotheus in English (Wheeler 1977); 1646 Latin edition (bub_gb_RqgSJJiGwS8C) | Dorotheus in PD form | No pre-1931 English; the 1646 Latin edition was not verified further. |
| Hirschfeld, Hevelone-Harper, Rubenson | Census secondary sources | Scholarship, in copyright. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Sophronius's Synodical Letter (634) and the works printed with the Pratum: which entry holds him as tradition (the Heraclian sibling is likely)? needs-ruling.
- The anti-Chalcedonian Gaza voices (Zachariah, John Rufus, Raabe's Peter the Iberian, Severus) are wired as context only, never tradition.
- The 6th-century pilgrim texts (Theodosius, the Piacenza pilgrim) here or only in jerusalem-liturgical-pilgrimage-christianity?
- Sinai and Climacus: inside this entry's region or only its legacy? Climacus is wired provisional.

## 6. Build or atlas-only recommendation

**Recommendation: open question, leaning atlas only.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

Sourcing is the problem: every source the census lists is an in-copyright translation, and the vendorable own voice is in Latin and Greek second-witness OCR (Moschus, the Vita Euthymii, Dorotheus with the Barsanuphius answers). Building would mean authored modern renderings from Latin or Greek at scale: a methodology decision. If Mark allows Latin second witnesses to carry the voice the answer becomes build; otherwise atlas only. Ecology, uniqueness and audience are good.
