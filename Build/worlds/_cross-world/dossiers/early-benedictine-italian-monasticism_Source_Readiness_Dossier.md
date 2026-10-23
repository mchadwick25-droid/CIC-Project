# Source Readiness Dossier — Early Benedictine / Italian Monasticism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.6
**Corpus-map slug:** `early-benedictine-italian-monasticism`
**Time window:** c. 500-604
**Region(s):** Italy
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of 2026-10-23 (checked at `469dd9b2` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. The staging for Gregory's Dialogues named this entry only in a note and assigned it to `roman-church-gregorian`. Cassian's Latin Institutes was vendored with no staging file; this pass added one.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, 2026-10-23).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Conferences of John Cassian | cassian | tradition | assigned | div2 4.4-4.6 — Conferences I-XXIV (three parts, one work); file 583,580 words | `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` |
| The Twelve Books on the Institutes of the Coenobia | cassian | tradition | assigned | div2 4.3 — The Institutes; file 583,580 words | `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` |
| Register of the Epistles of St. Gregory the Great (Books I-VIII selection) | gregory | context | assigned | div2 3.5 — Register of the Epistles, Books I-VIII; continued; file 483,662 words | `npnf212_leo-great-gregory-great.xml` |
| Register of the Epistles of St. Gregory the Great (Books IX-XIV selection) | gregory | context | assigned | div2 2.5-2.10 — Books IX-XIV; continuation of the Register b; file 322,488 words | `npnf213_gregory-great-ephraim-syrus-aphrahat.xml` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- Gregory's Dialogues Book II, the only Life of Benedict (raw lines ~3393-5700, ~18,800 words): wired as tradition, needs-ruling, the double placement the Gregorian dossier left open.
- Anonymus Valesianus (Theoderic's Italy) and Eugippius quoted in it, inside the Prosper/Chronica minora file (~39513-41490). Context, tier 2. Wired.
- Gregory's Register letters to abbots and abbesses (npnf212 ~35070, 35261, 36209, 39065, 45696; npnf213 ~5405, 9017, 9047): finding-aid row. Wired.
- Cassian's Latin Institutes (CSEL 17): newly staged, provisional.

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Rule of Saint Benedict (`benedict_rule-of-saint-benedict_gasquet1925.txt`) | Benedict of Nursia | Cardinal Gasquet | 1925 | https://archive.org/details/ruleofsaintbened0000bene | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Chatto and Windus 1925; no copyright field); the Prologue and chapters located in the fetched text, 2026-10-23 |
| The Rule of St. Benedict, Latin with English (Hunter Blair) (`benedict_rule-of-st-benedict-lat-eng_hunter-blair1907.txt`) | Benedict of Nursia | D. Oswald Hunter Blair | 1907 | https://archive.org/details/TheRuleOfStBenedict | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1907; CC Public Domain Mark 1.0), 2026-10-23 |
| Boethius, The Theological Tractates and The Consolation of Philosophy (Loeb) (`boethius_theological-tractates-consolation_stewart-rand1918.txt`) | Boethius | H. F. Stewart; E. K. Rand | 1918 | https://archive.org/details/theologicaltrac00testgoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Heinemann 1918), 2026-10-23 |
| Patrologia Latina 70 (Cassiodorus, Institutiones) (`cassiodorus_opera-institutiones-pl70-lat_migne1847.txt`) | Cassiodorus | J.-P. Migne (compiler) | 1866 | https://archive.org/details/patrologiaecursu70mign | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (date field 1800; Migne PL printed 1844-1866); the Institutiones located in the fetched text, 2026-10-23 |
| The Letters of Cassiodorus (Variae), condensed (`cassiodorus_variae-letters-hodgkin1886.txt`) | Cassiodorus | Thomas Hodgkin | 1886 | https://www.gutenberg.org/ebooks/18590 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched; PD statement and 1886 imprint read, 2026-10-23 |
| The Life of Saint Severinus (`eugippius_life-of-saint-severinus_robinson1914.txt`) | Eugippius | George W. Robinson | 1914 | https://archive.org/details/saintseverinus00eugiuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Harvard 1914), 2026-10-23 |
| The Book of the Popes (Liber Pontificalis), vol. I (`liber-pontificalis_book-of-the-popes-v1_loomis1916.txt`) | Liber Pontificalis (anonymous) | Louise Ropes Loomis | 1916 | https://archive.org/details/LiberPontificalisV1 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1916; CC Public Domain Mark 1.0), 2026-10-23 |
| History of the Langobards (`paul-the-deacon_history-of-the-langobards_foulke1907.txt`) | Paul the Deacon | William Dudley Foulke | 1907 | https://archive.org/details/historyoflangoba00pauluoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Penn 1907), 2026-10-23 |
| History of the Wars, Books V and VI: The Gothic War (`procopius_wars-5-6-gothic_dewing1919.txt`) | Procopius of Caesarea | H. B. Dewing | 1919 | https://www.gutenberg.org/ebooks/20298 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 1919 imprint and PD statement read, 2026-10-16 |
| Procopius, History of the Wars, Books VI.16-VII.35 (Loeb vol. IV) (`procopius_wars-6-16-7-35-gothic-grc-eng_dewing1924.txt`) | Procopius of Caesarea | H. B. Dewing | 1924 | https://archive.org/details/procopiuswitheng04procuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); the volume's own 'First printed 1924' leaf read in the fetched text, 2026-10-16 |
| Patrologia Latina 88 (Regula Magistri, Cresconius) (`regula-magistri-cresconius-pl88-lat_migne1862.txt`) | The Master (anonymous); Cresconius | J.-P. Migne (compiler) | 1862 | https://archive.org/details/patrologiaecur88mign | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (date field 1800; the title leaf reads 1862); the Regula Magistri located in the fetched text, 2026-10-23 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Wolfflin's Latin Rule (benedictiregula01wlgoog, Teubner 1895) and Butler's 1912 Latin Rule: redundant with the Hunter Blair Latin.
- Ennodius (MGH AA 7): not opened; low priority.

**Gaps (no public-domain English, or no own voice):**

- The Rule of the Master has no public-domain English.
- Cassiodorus's Institutiones: Latin only (Jones 1946 needs a renewal check; Mynors 1937 is non-US).

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Doyle's English Rule (Gutenberg 50040) | Complete Rule in English | The text prints Copyright 1948; needs a renewal check before use. |
| Rule of the Master, tr. Eberle (1977); RB 1980; Martyn 2004; Zimmerman 1959 | Modern English editions | In copyright (Zimmerman needs a renewal check). |
| Cassiodorus, Institutiones tr. Jones (1946) | Cassiodorus in English | Needs a renewal check. |
| Gregory of Tours | Benedict material | None. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Dialogues II (and I): tradition for this entry as well as for roman-church-gregorian? needs-ruling (E1 in the working notes).
- Cassian is tradition here; antecedent fits better now the Rule (ch. 73 commends him) is vendored.
- Cassiodorus and Vivarium: part of this entry or context only?

## 6. Build or atlas-only recommendation

**Recommendation: build.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

if the Dialogues placement is ruled. Own voice in public-domain English is about 35,000-40,000 words: the Rule (~20,500) and Dialogues II (~18,800). The Rule of the Master is Latin only. Rich surrounding ecology (the Register, Eugippius, the Liber Pontificalis, Paul the Deacon, Cassiodorus, Boethius); the overlap with the Gregorian entry is real but narrow (that world is episcopal, this one is the cloister).
