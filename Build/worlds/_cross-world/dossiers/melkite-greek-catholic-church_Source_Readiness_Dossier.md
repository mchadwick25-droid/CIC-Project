# Source Readiness Dossier — The Melkite Greek Catholic Split

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.23
**Corpus-map slug:** `melkite-greek-catholic-church`
**Time window:** 1724-1815
**Region(s):** Damascus, Aleppo, Mount Lebanon; census `regions`: Middle East
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

8 works across 4 vendored files in `cic/corpus-map/melkite-greek-catholic-church.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Histoire des patriarcats melkites, t. II-III (1910-1911) | charon | transmission | provisional | whole work | `charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt` |
| Histoire des patriarcats melkites, t. III: the hierarchy chapters with documents of 1724-1760 | charon | context | assigned | tome III's chapter on the history of the hierarchy (for example the signature lists from about raw scan lin... | `charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt` |
| Congregations of Propaganda and papal acts on the Melkites, 1716-1815 (Mansi 46) | mansi | context | assigned | the particular congregations of 1729 on Cyril VI's election (from about raw scan line 2512), the congregati... | `mansi_sacrorum-conciliorum-collectio-tomus-46-synodi-melchitarum-lat_petit1911.txt` |
| Melkite synods and documents after 1815 (Mansi 46) | melkite-church | transmission | provisional | from the synod of 1831 at the Annunciation monastery, Zuq Mikhail (about raw scan line 90763), to the synod... | `mansi_sacrorum-conciliorum-collectio-tomus-46-synodi-melchitarum-lat_petit1911.txt` |
| Melkite synods and episcopal documents, 1716-1815 (Mansi 46) | melkite-church | tradition | assigned | the synods of Saint Saviour of 1730, 1736, 1751 and 1756 (from about raw scan line 19050), the synods of 17... | `mansi_sacrorum-conciliorum-collectio-tomus-46-synodi-melchitarum-lat_petit1911.txt` |
| The Travels of Macarius (Paul of Aleppo), vol. 1 | paul-of-aleppo | antecedent | provisional | the Aleppo and Syrian opening books and every passage on the Antiochian patriarchate | `paul-of-aleppo_travels-of-macarius-v1_belfour1836.txt` |
| Travels through Syria and Egypt, vol. 2 (Volney, 1788): the Greek Catholic convents, Mar Hanna al-Shuwayr and its press | volney | context | assigned | the passage on the Greek Catholic convents in the Druze country and Mar Hanna (about raw scan lines 6670-72... | `volney_travels-through-syria-and-egypt-v2_1788.txt` |
| Travels through Syria and Egypt, vol. 2 (Volney, 1788): the pashaliks and the Christians of Aleppo, Damascus and the coast | volney | context | provisional | the chapters on the pashaliks | `volney_travels-through-syria-and-egypt-v2_1788.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| `propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt` | the entries 'pro Graeco-Melchitis', from about file line 33436: a constitution of Benedict XIV with the Italian instruction for the Melkite nation on rites, fasts and customs; further Melkite entries through the volume | Rome's rulings on the Melkites in the window; the file mentions Melkites about 40 times | context / assigned |
| `paul-of-aleppo_travels-of-macarius-v1_belfour1836.txt` (proposed in the Ottoman spec) | the Aleppo and Antioch passages | The Antiochian church before the split, from its own patriarch's household | antecedent / provisional (cross-row already in that spec) |

Nothing else in `cic/texts/` names the Melkites of this period. The `melkite`-matching files are on the Chalcedonian Melkites of late antiquity and the early Middle Ages, a different subject.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| al-Lahut al-adabi bi-asrihi (Theologia moralis universa), vols. 1-5 | Paul-Gabriel Antoine | Yusuf Ajluni, Melkite Basilian monk of Mar Yuhanna al-Shuwayr (as the item's transcribed title page says) | 1795 (Rome, Propaganda press) | https://archive.org/details/TheologiaMoralisUuniversAr01 (and ...Ar02-Ar05) | PD by date (1795). The uploader's CC BY-NC-ND licence covers only the scan | metadata API, djvu 0.86 MB for vol. 1 (1.21 MB vol. 2), OCR 0.82, 23 October 2026. The only Arabic print by a Melkite found. It is a translation of a Latin manual, and the Arabic OCR has frequent letter errors |
| Oriens Christianus, tomus II (Antioch) | Michel Le Quien | none | 1740 | https://archive.org/details/A216171 (also bub_gb_86weAemI-e4C) | PD by date; the item carries a CC public-domain mark | metadata API, djvu 3.95 MB, OCR 0.70, 23 October 2026. Contemporary entries 'Cyrillus VI catholicus' and 'Sylvester schismaticus' (from a consul's letter of 1733), but only a page or two in a 4 MB volume |
| Nubdha tarikhiya fima jara li-ta'ifat al-Rum al-Kathulik mundh sanat 1837 | Maximos III Mazloum | none | 1907 | https://archive.org/details/nubdhahtrkhyahfm00maks | PD by date | metadata API, djvu 0.69 MB, 23 October 2026. Arabic, the Melkite patriarch's own voice, but from 1837 on, after the window |
| Documents inedits pour servir a l'histoire du patriarcat melkite d'Antioche, I: Maxime III | Thomas Mazloum | none | 1926 | https://archive.org/details/documentsinditsp0000larc | PD by date (1926) under the project's rule | metadata API, djvu 0.40 MB, 23 October 2026. After the window |
| al-Machriq, annual volumes (1898 onward) | ed. Louis Cheikho | none | 1901 and later | https://archive.org/details/AlMachriq04 | PD by date for volumes to 1930 | metadata API, djvu 3.91 MB (vol. 4), 23 October 2026. Arabic Jesuit review with articles on Arabic printing and Melkite history; would need an article-by-article search |
| Travels through Syria and Egypt, vol. I | C.-F. Volney | unnamed | 1788 | https://archive.org/details/travelsthroughsy01voln | PD by date | metadata API, djvu 0.59 MB, OCR 0.88, 23 October 2026. Egypt and Syrian geography; Mar Hanna only in passing |
| Benedicti XIV Bullarium, tomus I | Benedict XIV | none | 1746 | https://archive.org/details/A210104 | PD by date; CC public-domain mark | metadata API, djvu 2.8 MB, 23 October 2026. Should carry Benedict XIV's Melkite constitution of 1743 (not checked in the text); in any case Mansi 46 and the Propaganda Collectanea already print the Melkite acts |
| Bibliotheca juris orientalis canonici et civilis | J. S. Assemani | none | 1762-1766 | https://archive.org/details/bub_gb_wbJSwpYhwnQC | PD by date | metadata API, djvu 1.55 MB, 23 October 2026. Byzantine canon law; not on the split |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Charon, Histoire des patriarcats melkites, tome I | The narrative of 1724 | Never published; tomes II-III are vendored |
| Writings of Euthymius Saifi, Abdallah Zakher, Neophytos Nasri, Cyril VI Tanas | The voices the census names | No printed edition before 1930 found on archive.org under Latin, French, English or Arabic searches |
| Arabic books from the Aleppo (1706) or Shuwayr (from the 1730s) presses | The census's "Aleppo's Arabic Christian printing presses" | No scans found on archive.org; the hosts that might hold them (Gallica, HathiTrust) are blocked |
| Niebuhr, Reisebeschreibung / Travels through Arabia | An outside traveller in Syria | His Syrian pages are slight on the Melkites; not pursued |
| Juris pontificii de Propaganda Fide (de Martinis) | Papal acts for the Eastern rites | Not found on archive.org |

## 5. Open cross-world questions

- The Orthodox half of the Antioch split (Sylvester and his successors) is given by the census to Ottoman-era Orthodoxy (VII.18). Mansi 46 and Volney carry it only from the Catholic and outside sides. Is an Orthodox Antiochian witness needed there, and does one exist in public-domain print?
- The census names kin-shapes in the Union of Brest and the Maronite union. Would the Ruthenian eighteenth-century entry (VII.28) share the Propaganda Collectanea rows?
- No census entry carries the Melkites after 1815. Mansi 46's nineteenth-century synods and Charon tome II are placed as provisional transmission.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Open question, leaning Atlas only for now; this is advice, not a ruling.** The census's "moderate" sourcing is accurate for institutional records: Mansi 46 is a full documentary spine for the election, recognition, synods and Roman oversight, and Charon adds transcribed signatures. Almost none of it is the world's own voice in the sense a Representative needs. It is Latin and Italian synod acts, letters to Rome, and Rome's replies. No sermon, life, hymn or letter by Saifi, Cyril VI or Zakher in Arabic was found in public-domain print, and the one Arabic Melkite print found is a translated Latin manual. The census itself marks the entry "deferred, richer window later". The material here would support a strong outside-and-institutional portrait, but not a Representative speaking in the community's own Arabic idiom. A build should wait until Arabic sources (al-Machriq articles, Shuwayr imprints, a later Melkite world) are surveyed.

