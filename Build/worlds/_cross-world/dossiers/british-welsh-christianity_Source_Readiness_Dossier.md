# Source Readiness Dossier — British and Welsh Christianity

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.17
**Corpus-map slug:** `british-welsh-christianity`
**Time window:** c. 451-768
**Region(s):** Wales, W. Britain, Cornwall, Brittany
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of October 2026 (checked at `9675d7e3` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. No corpus-map bucket and no staging row existed before this pass. Constantius of Lyon's Vita Germani (Levison 1920) was vendored earlier with no staging at all; it is now staged here as context.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, October 2026).

None. No bucket file and no staging row named this entry before this pass.

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- Bede I.17-22 (Germanus, Gildas), II.2 (Augustine's Oak and the monks of Bangor), V.18, V.23. Context, tier 2. Wired.
- Constantius, Vita Germani: the British missions (raw ~2665, ~2993, ~3475). Context, provisional, pre-window. Newly staged.
- Gregory of Tours on the Bretons: IV.4 (Macliav), IV.20, V.21 (Winnoch). Context, tier 2. Wired.
- Gregory the Great's Responsa to Augustine, question IX (npnf213 ~7524, ~7908); Gennadius LVII (Fastidius); Prosper's entry for 429 (Agricola, Germanus). Context, tiers 3-4. Wired.
- Not wired: Faustus of Riez (British-born; prolegomena), Pelagius ('a British monk', npnf105), Duchesne III.

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Annales Cambriae (`annales-cambriae-rolls-series-20-lat_williams-ab-ithel1860.txt`) | anonymous Welsh annalists | John Williams ab Ithel (ed.) | 1860 | https://archive.org/details/annalescambri20will | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Rolls Series 1860; no copyright field); the 768 entry located in the fetched text, October 2026 |
| Lives of the Cambro British Saints (`rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt`) | anonymous Welsh hagiographers | W. J. Rees (ed. and tr.) | 1853 | https://archive.org/details/livesofthecambro00reesuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; 1853), October 2026 |
| Die Bussordnungen der abendlaendischen Kirche (the Latin penitentials) (`wasserschleben_die-bussordnungen-der-abendlaendischen-kirche-lat-deu_1851.txt`) | Vinnian; Columbanus; Cummean; Gildas; anonymous | F. W. H. Wasserschleben (ed.) | 1851 | https://archive.org/details/diebussordnungen00wass | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Graeger 1851; no copyright field); the Gildas and Vinnian penitentials located in the fetched text, October 2026 |
| Gildas, De excidio Britanniae (with fragments, penitential and Lorica) (`gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt`) | Gildas | Hugh Williams | 1899 | https://archive.org/details/gildaedeexcidiob00gilduoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Cymmrodorion 1899); sections 1-110 and Caradoc's Life located in the fetched text, October 2026 |
| History of the Britons (Historia Brittonum), tr. J. A. Giles (`nennius_history-of-the-britons-giles.txt`) | Nennius (attrib.) | J. A. Giles | undated (translator d. 1884) | https://www.gutenberg.org/ebooks/1972 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched; PD statement read, October 2026 |
| Libri Sancti Patricii (Latin) (`patrick_libri-sancti-patricii-lat_white1918.txt`) | Patrick | Newport J. D. White (ed.) | 1918 | https://archive.org/details/librisanctipatr00patr | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (SPCK 1918; no copyright field), October 2026 |
| St. Patrick, His Writings and Life (with Muirchu's Life) (`patrick_writings-and-life-with-muirchu-eng_white1920.txt`) | Patrick; Muirchu | Newport J. D. White | 1920 | https://archive.org/details/StPatrick1920 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1920; CC Public Domain Mark 1.0); the Confession and Letter located in the fetched text, October 2026 |
| The Life of St. Samson of Dol (`samson-of-dol_life-of-st-samson_taylor1925.txt`) | anonymous | Thomas Taylor | 1925 | https://archive.org/details/lifeofstsamsonof00sams | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (SPCK 1925; no copyright field); title page read, October 2026 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Wade-Evans, Life of St David (MN5136ucmf_5, 1923); Evans and Rhys, Book of Llan Dav (textofbookofllan00evan, 1893); MGH Chronica minora III (Latin Gildas and Historia Brittonum): verified, not vendored.

**Gaps (no public-domain English, or no own voice):**

- One substantial own-voice author, Gildas (~20,000 words in English, complete in the Williams edition), plus Patrick (shared, ~10,000), Samson (~30,000 words; date Contested). Annales Cambriae is Latin; the lives of David, Illtud and Cadoc are 11th-12th century.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Gutenberg 1949 (Gildas, tr. Giles) | An English Gildas | Truncated at section 26 (checked against the text, ll. 754-800); superseded by Williams 1899. |
| Giles, Six Old English Chronicles (gri_33125001291513, 1848) | Gildas and Nennius in English | Redundant; may share the Gildas truncation (unverified). |
| Stevenson 1838; Fawtier 1912; Loth 1914; Wade-Evans 1944; Rees 1840; Skene; Morris-Jones 1912; Haigh 1861 | Latin and Welsh texts | Superseded, not found, non-US 1944, scholarship, secular verse or too late. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Patrick overlaps the Irish entry (one edition, two rows?).
- Gildas in Irish tradition (Columbanus cites him; the Irish catalogue names him; his penitential sits with the Irish ones): antecedent for the Irish entry?
- Brittany against Merovingian Gaul (Samson at Dol and at Paris).
- Pelagius, Fastidius and Germanus (before 451): antecedents here, or wholly pelagianism's?
- The Bede overlap with anglo-saxon-christianity belongs in PAIRS.yaml.
- The 768 end rests on 9th-10th-century compilations (Annales Cambriae, the Historia Brittonum prologue): confidence tag.

## 6. Build or atlas-only recommendation

**Recommendation: build (thin), or pair with the Irish entry.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

The choice between the two is Mark's. One substantial own voice (Gildas, complete in English), Patrick shared, Samson of contested date; heavy overlap with the Irish entry. Distinct per the census.
