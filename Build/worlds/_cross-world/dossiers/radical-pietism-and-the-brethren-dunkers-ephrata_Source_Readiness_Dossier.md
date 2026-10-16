# Source Readiness Dossier — Radical Pietism & the Brethren (Dunkers, Ephrata)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.3
**Corpus-map slug:** `radical-pietism-and-the-brethren-dunkers-ephrata`
**Time window:** 1690s–1815
**Region(s):** Germany (Schwarzenau, Wittgenstein), then Pennsylvania (Germantown, Conestoga, Ephrata); census `regions`: North Europe
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-16
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass. Nothing Brethren or Ephrata was vendored before it.

## 1. Already assigned

Eighteen works across fourteen vendored files, all added this pass to `cic/corpus-map/radical-pietism-and-the-brethren-dunkers-ephrata.yaml`:

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Chronicon Ephratense (English translation, Hark 1889) | lamech-agrippa | tradition | assigned | whole volume; numbered chapters | `lamech-agrippa_chronicon-ephratense_hark1889.txt` |
| Chronicon Ephratense (German original, Ephrata 1786) | lamech-agrippa | tradition | assigned | whole volume; page numbers in running heads | `lamech-agrippa_chronicon-ephratense-deu_ephrata1786.txt` |
| Rights and Ordinances of the House of God (A Short and Plain View), English 1810 | mack-alexander | tradition | assigned | whole work; dialogue turns Son./Father. | `mack-alexander_rights-and-ordinances_1810.txt` |
| Ground Searching Questions (Grundforschende Fragen, 1713), English with German, 1860 | mack-alexander | tradition | assigned | the section headed Ground Searching Questions | `mack-alexander_writings-bilingual_columbiana1860.txt` |
| Memoir of Alexander Mack, Sen., by his son | mack-alexander | tradition | assigned | the section headed Memoir of Alexander Mack, Sen. | `mack-alexander_writings-bilingual_columbiana1860.txt` |
| Urständliche und Erfahrungs-volle Hohe Zeugnüsse (Beissel's theological letters, 1745) | beissel | tradition | assigned | whole volume | `beissel_urstandliche-hohe-zeugnusse-deu_ephrata1745.txt` |
| Mystische und sehr geheyme Sprüche (99 Mystical Proverbs, 1730), German with Miller's English | beissel | tradition | assigned | the numbered proverbs 1-99 | `beissel_mystical-proverbs-and-millers-letter-to-franklin_sachse1912.txt` |
| Peter Miller's letter to Benjamin Franklin (1771) | miller-peter | tradition | assigned | the letter prefixed to the proverbs | `beissel_mystical-proverbs-and-millers-letter-to-franklin_sachse1912.txt` |
| Conrad Beissel's Treatise on Music (preface to the Turtel-Taube, 1747), Sachse's English | beissel | tradition | assigned | the section headed as Beissel's treatise on music | `sachse_music-of-ephrata-cloister-beissel-treatise_1903.txt` |
| The Music of the Ephrata Cloister (Sachse's monograph) | sachse | context | assigned | the monograph chapters outside the treatise | `sachse_music-of-ephrata-cloister-beissel-treatise_1903.txt` |
| Theosophische Lectionen, Erster Theil (Ephrata, 1752) | ephrata-community | tradition | assigned | whole volume; numbered Lectionen | `ephrata-community_theosophische-lectionen-deu_1752.txt` |
| Das Gesäng der einsamen und verlassenen Turtel-Taube (Ephrata hymnal, 1747) | ephrata-community | tradition | assigned | whole volume; numbered hymns and stanzas | `ephrata-community_turtel-taube-hymnal-deu_1747.txt` |
| Das Kleine Davidische Psalterspiel der Kinder Zions (Germantown, 1744) | church-of-the-brethren | tradition | assigned | whole volume; numbered hymns | `church-of-the-brethren_kleine-davidische-psalterspiel-deu_saur1744.txt` |
| Hochmann von Hochenau, Confession of Faith (Detmold, 1702), German facsimile with literal English | hochmann | tradition | assigned | chapter VI, from printed page 83 | `brumbaugh_history-german-baptist-brethren_1899.txt` |
| Early Germantown Brethren records and Mack family documents as printed by Brumbaugh | brumbaugh | tradition | provisional | the Germantown chapters | `brumbaugh_history-german-baptist-brethren_1899.txt` |
| Christopher Sauer's pamphlet and letter against Conrad Beissel (1739), English | sauer-christopher | tradition | assigned | pp. 76-96 of the journal volume | `sauer-christopher_quarrel-with-beissel-1739_pennypacker1888.txt` |
| Materials towards a History of the American Baptists, vol. I: Pennsylvania (1770) | edwards-morgan | context | assigned | the sections on the Tunkers and on Ephrata | `edwards-morgan_materials-history-of-baptists-pennsylvania_1770.txt` |
| A History of New Sweden: the visit to the Ephrata Cloister, 20 August 1753 | acrelius | context | assigned | one titled section | `acrelius_history-of-new-sweden_reynolds1874.txt` |

Every vendored file carries its rights basis, section labelling, credit line and republication note in `cic/texts/REGISTRY.yaml`. Seven of the fourteen are German Fraktur scans (the 1786 Chronicon, the Zeugnüsse, the Lectionen, both hymnals, and the German halves of the 1860 Mack and 1899 Brumbaugh volumes): usable for locating passages, but every quotation must be re-read against the page image before a record claims it verified.

## 2. Cross-link opportunities

- **German Pietism (VII.2).** Hochmann's 1702 confession (in Brumbaugh) is linked to `german-pietism-spener-francke-halle` as `context`, provisional: Hochmann was formed at Halle under Francke before he separated. Brumbaugh's chapter on Spener, Francke and Arnold is narrative, not source.
- **The Moravian Church (VII.4).** The Chronicon's chapters on the 1741–42 Pennsylvania synods and Zinzendorf's visit are linked to `the-moravian-church-at-herrnhut` as `context`, provisional: an Ephrata eyewitness of the Moravians as rivals.
- **The Baptists (VII.16).** Morgan Edwards's 1770 survey is linked to `the-baptists` as `tradition`, assigned: a Philadelphia Baptist's inside record of his association, and the Brethren seen from a neighbouring communion.
- **Not linked, named for a later pass.** Acrelius's whole volume is the own-voice record of the Swedish Lutheran church on the Delaware, a community the census does not list. The Kleine Davidische Psalterspiel was also used by Pennsylvania Mennonites (no Era VIII Mennonite entry in the census; the Anabaptist world closes at 1650).

CORPUS-USE tier check: no previously vendored file names Mack, Beissel, Hochmann, Ephrata, Schwarzenau or the Dunkers (title and author scan of `WORKS.yaml`, `AUTHOR-IDS.yaml` and the registry). Nothing earlier in the corpus reaches this world.

## 3. Verified acquisition leads

Verified against the host and not vendored this pass (size, lower priority, or garbled OCR):

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Zionitischer Weyrauchs Hügel oder Myrrhen Berg (the first Ephrata hymnal, 692 hymns, printed by Sauer) | Ephrata community (Beissel and others) | n/a (German) | 1739 | archive.org/details/zionitischerweyr00unkn | pd-us-by-date; John Carter Brown item, no rights field | archive.org metadata API and `_djvu.txt` download, 2026-10-16; 1.66 MB, two-column OCR sometimes interleaved. Not vendored this pass for size; the 1747 Turtel-Taube carries the Ephrata hymn voice |
| Die erste Liebe der Gemeinen Jesu Christi (5th ed.) | Gottfried Arnold | n/a (German) | 1732 | archive.org/details/11348025bsb | pd-us-by-date; Bayerische Staatsbibliothek item | metadata and download, 2026-10-16; 4.9 MB, usable Fraktur OCR. Antecedent for this world and for German Pietism; held for a decision on size (the 1700 edition `bub_gb_0PxVAAAAcAAJ` is garbled). No English translation of this work exists |
| Paradisisches Wunder-Spiel (the last Ephrata hymnal, Beissel's own) | Conrad Beissel | n/a (German) | 1766 | archive.org/details/paradisischeswun00beis | pd-us-by-date | metadata API, 2026-10-16; `_djvu.txt` 1.9 MB present; not downloaded |
| The German Sectarians of Pennsylvania, 2 vols (1708–1742; 1742–1800) | J. F. Sachse | n/a | 1899–1900 | archive.org/details/germansectarians01sach and germansectarians02sach | pd-us-by-date | metadata and download, 2026-10-16; clean OCR; scholarship with translated documents and the Ephrata imprint bibliography. Not vendored: narrative is Sachse's own and "legendary" by his own label; mine for quoted documents only |
| The German Pietists of Provincial Pennsylvania 1694–1708 | J. F. Sachse | n/a | 1895 | archive.org/details/germanpietistsof00sach | pd-us-by-date; `possible-copyright-status: NOT_IN_COPYRIGHT` | metadata and download, 2026-10-16; pre-history (Kelpius, the Wissahickon hermits); scholarship |
| The Religious Poetry of Alexander Mack, Jr. (German with English) | Alexander Mack Jr.; ed. and tr. S. B. Heckman | Heckman | 1912 | archive.org/details/religiouspoetryo00mack | pd-us-by-date; Library of Congress statement | metadata and download, 2026-10-16; clean OCR, 326 KB. Second-generation Germantown voice; a strong candidate for the next pass |
| The Works of Jacob Behmen, the Teutonic Theosopher (4 vols, Law edition) | Jakob Böhme; ed. William Law | 18th-century English | 1764 | archive.org/details/worksofjacobbehm01bohm (to 04bohm) | pd-us-by-date | metadata API, 2026-10-16; existence and open status confirmed; not downloaded (about 10 MB; antecedent only) |
| Christosophia oder Der Weg zu Christo (Ephrata press, Böhme) | Jakob Böhme | n/a (German) | 1811 | archive.org/details/spohn1104 | pd-us-by-date | metadata API, 2026-10-16; the Ephrata press at the window's end |
| Letters of Christopher Marshall to Peter Miller, of Ephrata (PMHB 28) | Christopher Marshall | n/a | 1904 | archive.org/details/jstor-20086122 | pd-us-by-date; JSTOR Early Journal Content | metadata API, 2026-10-16; 15 KB; an outsider's letters to Miller |
| Brethren Digital Archives collection, Elizabethtown College (further Ephrata and Brethren imprints 1785–1815, e.g. `spohn2521` Die Ernsthafte Christenpflicht, 1785; `spohn1077` Georg Adam Martin, Christliche Bibliothek, 1792) | various | n/a (German) | 1785–1815 | archive.org collection `brethrendigitalarchives` | pd-us-by-date | collection seen in search, 2026-10-16; items not individually verified; the natural starting point for the window's last decades |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Conrad Beissel, A Dissertation on Man's Fall (Ephrata, 1765, English) | Beissel's only English-language imprint | Not on archive.org under title or `creator:(beissel)`; not reproduced in Sachse vol. 2 (text searched); HathiTrust catalogue returned a JavaScript challenge from this environment. Not found on any reachable host |
| Beissel, Mystische und sehr geheyme Sprüche (Philadelphia: Franklin, 1730), separate print | Earliest Beissel print | No separate scan on archive.org; the 1912 Sachse facsimile with Miller's English is vendored instead |
| Hochmann von Hochenau, Glaubensbekenntnis (1702), separate print | Own-voice confession | No separate print on archive.org; vendored inside Brumbaugh (German facsimile, garbled OCR, with literal English) |
| H. Renkewitz, Hochmann von Hochenau (1969; English 1994) | Carries Hochmann documents | 1969 non-US publication and 1994 translation: in copyright |
| D. F. Durnbaugh (ed.), The Complete Writings of Alexander Mack (1991) | Standard modern English | 1991: in copyright |
| Christopher Sauer Bible (Germantown, 1743) and its preface | Sauer's own voice | Not on archive.org for 1743 (only a 1743 New Testament and the 1763 second-edition Bible surfaced, neither verified); Sauer's voice is covered by the 1739 pamphlet in Pennypacker's English |
| Project Gutenberg | A possible English Chronicon or Brumbaugh | "Ephrata" returns only a novel; "Brethren Brumbaugh" returns nothing |
| Gottfried Arnold, Die erste Liebe, 1700 edition (`bub_gb_0PxVAAAAcAAJ`) | Closest to the 1696 first edition | OCR garbled beyond use; the 1732 fifth edition (§3) is the usable scan |
| archive.org `dasgesngdereinsa00unkn` (John Carter Brown Turtel-Taube) | Second copy of the 1747 hymnal | Its `_djvu.txt` is a 15 KB stub; the Princeton copy was vendored |

## 5. Open cross-world questions

- **Where Gottfried Arnold belongs.** Die erste Liebe (1696) and the Unparteiische Kirchen- und Ketzer-Historie (1699–1700) are the radical-Pietist primitivist texts Mack, Hochmann and Beissel all read, and Zinzendorf after them. They are also German Pietism's own literature. Whether Arnold is vendored under this world, under VII.2, or once for both (the corpus map allows all three) is a placement question for the project lead; nothing here decides it. The Ketzer-Historie exists in five open sets on archive.org, all with garbled OCR and PDFs over 170 MB.
- **A Swedish-Lutheran-on-the-Delaware world.** Acrelius's History of New Sweden is that community's own record; the census has no entry for it. Named here so the text is not re-found.
- **Böhme and the Philadelphians.** The 1764 Law edition of Böhme and the Ephrata press's 1811 Christosophia point to a Behmenist current that runs under this world, the Moravians and the English Philadelphian Society. No census entry owns it.
- **Pennsylvania Mennonites.** The Kleine Davidische Psalterspiel served Mennonite congregations too; the Anabaptist world (VI.3) closes at 1650 and no Era VIII Mennonite entry exists.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build.** The own voice is deep and distinctive: Mack's two treatises and his son's memoir, Beissel's letters and proverbs, the Solitary's Lectionen, two hymnals, the community's own chronicle in German and English, and the printer's quarrel from Sauer's side; plus two independent contemporary outside witnesses (Edwards 1770, Acrelius 1753). The floor (Step 0 A1) is clear: Trinitarian, believer's-baptism Pietists. The one weakness is language: the Ephrata voice is German and none of it has a public-domain English translation except the Chronicon and the 1730 proverbs, so Representative renderings would be the Library's own, made from Fraktur scans that need page-image checks. A Step 0 should also settle the strand question (Germantown Brethren versus Ephrata, a real split in 1728) that the census entry names as "a real uniqueness test".
