# Source Readiness Dossier — The Reformed Cities: Zurich & Geneva

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.2
**Corpus-map slug:** `the-reformed-cities-zurich-and-geneva`
**Time window:** 1519–1650
**Region(s):** Swiss lands, then Europe
**Dossier author / date:** source-research thread, 2026-09-15; updated 2026-09-25
**Corpus-map / `cic/texts/` state as of:** 2026-09-25 — no longer a cold
start, and this §1's own prior "None" was already stale by the date it was
written: a same-day 2026-09-15 vendoring pass had assigned 10 works across
8 files to `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`
before this dossier was ever read against current `main`. A 2026-09-25
pass added 6 more works across 6 more files, closing 4 of this dossier's
own remaining §3 leads (2 genuinely new works — Zwingli's Latin Works Vol.
III and the Genesis Commentary — plus additional volumes of two others).
Current total: 16 works across 14 files. See §1 below for current state,
and §3 for exactly what remains open.

## 1. Already assigned

**Updated 2026-09-25 — no longer a cold start.** 16 works, across 14
vendored files, assigned to `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`:

| work | author | role | confidence | source file |
|---|---|---|---|---|
| The Second Helvetic Confession (1566) | bullinger | tradition | assigned | `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` |
| The Heidelberg Catechism (1563) | ursinus-olevianus | tradition | assigned | `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` |
| Institutes of the Christian Religion, Book I | calvin | tradition | assigned | `calvin_institutes-christian-religion-vol1_beveridge1845.txt` |
| Institutes of the Christian Religion, Books II–III | calvin | tradition | assigned | `calvin_institutes-christian-religion-vol2_beveridge1845.txt` |
| Institutes of the Christian Religion, Book IV | calvin | tradition | assigned | `calvin_institutes-christian-religion-vol3_beveridge1845.txt` |
| The Catechism of the Church of Geneva | calvin | tradition | assigned | `calvin_geneva-catechism_waterman1815.txt` |
| Mutual Consent in Regard to the Sacraments (the Consensus Tigurinus, 1549/1554) | calvin-zurich-pastors | tradition | assigned | `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt` |
| Selected Works (letter to Erasmus, disputation acts, the 1527 *Refutation of the Tricks of the Baptists*, other shorter writings) | zwingli | tradition | assigned | `zwingli_selected-works_jackson1901.txt` |
| The Sixty-Seven Articles of Zwingli (1523) | zwingli | tradition | assigned | `zwingli_selected-works_jackson1901.txt` |
| The Latin Works and the Correspondence of Zwingli, Vol. I | zwingli | tradition | assigned | `zwingli_latin-works-correspondence-vol1_jackson1912.txt` |
| Commentaries on the First Book of Moses, Called Genesis, Vol. I | calvin | tradition | assigned | `calvin_commentaries-genesis-vol1_king1847.txt` |
| Commentaries on the First Book of Moses, Called Genesis, Vol. II | calvin | tradition | assigned | `calvin_commentaries-genesis-vol2_king1847.txt` |
| Letters of John Calvin, Vol. I | calvin | tradition | assigned | `calvin_letters-vol1_bonnet1858.txt` |
| Letters of John Calvin, Vol. II | calvin | tradition | assigned | `calvin_letters-vol2_bonnet1858.txt` |
| Letters of John Calvin, Vol. IV | calvin | tradition | assigned | `calvin_letters-vol4_bonnet1858.txt` |
| The Latin Works of Zwingli, Vol. III ("Of True and False Religion") | zwingli | tradition | assigned | `zwingli_latin-works-correspondence-vol3_heller1929.txt` |

The first 10 rows (8 files) were vendored 2026-09-15, same day as this
dossier's original draft, and closed 5 of this §3's own leads plus the
Consensus Tigurinus item this dossier's own §4 had flagged "genuinely
open" — that closure was real but never reflected back into this dossier
until now. The last 6 rows (6 files: the two-volume Genesis Commentary,
Zwingli's Latin Works Vol. III, and the two remaining Letters volumes)
were vendored 2026-09-25, closing 3 more of this §3's own leads. See §3
for the one lead (Letters Vol. III) that remains genuinely open, and §5
for the world's own separately-tracked Source Registry acquisition gaps
(Ecclesiastical Ordinances, the Genevan Psalter, Beza, Dentière), which
are a real, higher-priority gap than anything remaining in this §3.

## 2. Cross-link opportunities

None identified this pass. Worth a dedicated check once Lutheran
Wittenberg's own corpus-map is further built out — no direct figure
overlap, but Calvin's and Zwingli's own polemics against Anabaptism
(vendored in `zwingli_selected-works_jackson1901.txt`'s 1527 *Refutation of
the Tricks of the Baptists*) may cross-link against `the-anabaptist-movements`.

## 3. Verified acquisition leads

Of the 9 leads originally listed here, 5 were closed 2026-09-15, 3 more
closed 2026-09-25, and 1 remains genuinely open. The Allen translation is
redundant with an already-vendored edition of the same work and needs no
further action.

| title | author | translator/ed. | year | url | rights basis | status |
|---|---|---|---|---|---|---|
| Institutes of the Christian Religion | Calvin | John Allen | 1813/1816/1844 | archive.org `institutesofchri01calv` | pd-us-by-date | **No action needed** — redundant with the Beveridge 1845 edition below, already vendored; not worth double-vendoring the same work in a second translation absent a specific reason. |
| Institutes of the Christian Religion | Calvin | Henry Beveridge | 1845 | archive.org `institutesofchrbeve01calv` etc. | pd-us-by-date | **Vendored 2026-09-15** — 3 vols., `calvin_institutes-christian-religion-vol{1,2,3}_beveridge1845.txt`. |
| Biblical Commentaries (Calvin Translation Society series, ~22 vols.) | Calvin | Calvin Translation Society (Rev. John King for Genesis) | 19th c. | archive.org | pd-us-by-date | **Partially vendored 2026-09-25** — the Genesis commentary only (2 vols., `calvin_commentaries-genesis-vol{1,2}_king1847.txt`, archive.org `commentariesonfi0{1,2}calvuoft`, direct fetch this session, `NOT_IN_COPYRIGHT` confirmed on both). A deliberate partial acquisition, not the whole series — the remaining ~20 volumes (Psalms, the Gospel harmony, Paul's epistles, and others) were not researched this pass and remain a real, open opportunity. |
| Letters of John Calvin, 4 vols. | Calvin | Jules Bonnet | 1855–58 | archive.org `lettersofjohncal01calv` etc. | pd-us-by-date | **Partially vendored 2026-09-25** — Vols. I, II, and IV (`calvin_letters-vol{1,2,4}_bonnet1858.txt`, Philadelphia: Presbyterian Board of Publication, 1858, direct fetch this session, `NOT_IN_COPYRIGHT` confirmed on all three). **Vol. III genuinely could not be located** — checked this identifier family (no `lettersofjohncal03calv` exists), the parallel 1855-57 Edinburgh/Constable printing (which also skips a standalone vol. 3), and Project Gutenberg (which holds only Vols. I-II). Not substituted or fabricated; a real, open gap, possibly resolvable via a dedicated HathiTrust pass. |
| Geneva Catechism | Calvin | Elijah Waterman | 1815 | archive.org `catechismofchurc00calv` | pd-us-by-date | **Vendored 2026-09-15** — `calvin_geneva-catechism_waterman1815.txt`. |
| Latin Works and Correspondence of Huldreich Zwingli, Vol. 1 | Zwingli | Samuel Macauley Jackson | 1912 | archive.org `latinworkscorres01zwin` | pd-us-by-date | **Vendored 2026-09-15** — `zwingli_latin-works-correspondence-vol1_jackson1912.txt`. |
| Latin Works..., Vol. 3 (contains "Commentary on True and False Religion") | Zwingli | Jackson & Heller | 1929 | archive.org `latinworkscorres03zwin` | pd-us-by-date | **Vendored 2026-09-25** — `zwingli_latin-works-correspondence-vol3_heller1929.txt`. 1929 publication date directly confirmed against the volume's own title page and copyright notice, more than 95 years before this session (2026); qualifies under this project's own rolling PD-by-date rule independent of archive.org's own classifier (which has not yet tagged this specific item either way). Contains "De Vera et Falsa Religione" and the Antibolon, as this row originally described. |
| Selected Works of Huldreich Zwingli | Zwingli | Samuel Macauley Jackson | 1901 | archive.org `translationsrepr01pennuoft` | pd-us-by-date | **Vendored 2026-09-15** — `zwingli_selected-works_jackson1901.txt`. The table-of-contents question this row originally flagged is now closed: directly verified to contain the Sixty-Seven Articles in full (see §4). |
| Heidelberg Catechism + Second Helvetic Confession, full English text | — | Philip Schaff, *Creeds of Christendom*, Vol. III | 1877/1919 | archive.org, pre-1923 copies | pd-us-by-date | **Vendored 2026-09-15** — `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` (a bounded extract, not the whole volume — see REGISTRY.yaml's own note). |

## 4. Checked and closed

| candidate | why it looked promising | why it's open/closed |
|---|---|---|
| CCEL's standalone Second Helvetic Confession page | Direct text | No translator/edition attribution on that page — use Schaff's *Creeds* Vol. III instead as the citable, dated edition. Not closed, just redirected. |
| Consensus Tigurinus (1549) — Zurich/Geneva doctrinal agreement | The actual documented bridge between Zwingli's and Calvin's traditions (see §6) | **Closed 2026-09-15** (this dossier's own text had not been updated to reflect it until now). Beveridge's CTS *Tracts and Treatises* (Edinburgh, 1844) was located and vendored as `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt` — a bounded extract, pp. 195–244 of the printed volume, distinct from that same volume's separate "Second Defence of the Sacraments... Against Joachim Westphal" which is NOT part of the Consensus and was not vendored under this row. See that file's own corpus-map assignment for the exact boundary. |
| Zwingli's individual short works (67 Articles, *Of Baptism*) as standalone items | Would be directly citable | **Closed 2026-09-15.** Directly verified inside `zwingli_selected-works_jackson1901.txt`: the Sixty-Seven Articles are present in full (lines ~4485–4700, embedded in the Acts of the First Zurich Disputation). *Of Baptism* was not independently itemized this pass — the volume's remaining shorter works are assigned as one collective row per the corpus's own large-volume granularity rule, not individually verified item-by-item. |

## 5. Open cross-world questions

None found against the existing (pre-451 CE) built worlds. Against sibling Era VII/VI candidates researched this same pass: no figure overlap with Lutheran Wittenberg, the Jesuits, the Anabaptists, or Lollardy.

**Flagging for a dedicated future pass, not acted on this session:** this
world's own `Build/worlds/rzg/Source_Registry.md` (rows 13–17) tracks five
already-identified, real acquisition gaps that are a higher priority than
anything remaining in this dossier's own §3, since they are named directly
in this world's own Doc_01/Doc_02 build record rather than general-interest
leads:

- **G1 — Ecclesiastical Ordinances of 1541/1561.** No genuine PD English
  edition located as of the last check; Schaff's *History of the Christian
  Church* Vol. VIII is paraphrase only, not a direct translation, and a
  1977 archive.org item carries an unverified third-party PD mark not
  accepted at face value.
- **G2 — The Genevan Psalter** (Marot & Beza, complete 1562). Not yet
  actively searched for a PD source.
- **G3 — A PD substitute or excerpt for the Consistory Registers of
  Geneva.** The McDonald/Eerdmans 2000 translation is confirmed
  copyrighted and will never be vendored; the underlying subject matter
  (Geneva's own consistory discipline records) is squarely Native to this
  world and its absence is, per the Source Registry's own note, "the
  single largest disclosed gap in this world's own source ecology."
- **G4 — Theodore Beza's own works** (letters, the *Tabula
  praedestinationis*, his share of the Psalter). Not yet actively
  searched.
- **G5 — Marie Dentière** (the 1539 *Epistre très utile* and the 1561
  preface to Calvin's sermon on women's apparel). A genuine Article
  20 marginalized-voice case, not yet actively searched.

## 6. Step 0 scope notes (for whoever drafts Doc_01/the Step 0 confirmation)

**Doctrinal floor clears cleanly.** Mainstream Reformed theology (Zwingli, Bullinger, Calvin) affirms Nicene/Chalcedonian trinitarian and Christological orthodoxy without qualification — codified explicitly in the Second Helvetic Confession ch. III (Trinity) and ch. XI (Christ), and the Heidelberg Catechism, both now confirmed PD-sourced above. Note for Doc_01: Calvin's role in Servetus's 1553 execution for anti-Trinitarian teaching belongs to a **neighboring** census entry (the anti-Trinitarian current, VI.14) — cross-reference rather than re-litigate there.

**Zurich/Geneva continuity — a real internal complication worth flagging for Doc_01, not a disqualifier.** Zwingli dies in 1531 (Kappel), before Calvin's Geneva ministry begins in earnest (1536, consolidated 1541). **There is no direct Zwingli-Calvin link.** The actual documented bridge is Heinrich Bullinger (Zwingli's real successor at Zurich, 1531–1575) and the Consensus Tigurinus (1549) — a formal doctrinal agreement between Bullinger's Zurich and Calvin's Geneva on the Lord's Supper, whose own PD English text is now vendored (§4 above; `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt`). Doc_01 should state this plainly: this movement's coherence rests on Bullinger, not on personal contact between its two most famous figures — a disclosed A2-style continuity question, not smoothed over, the same discipline the Latin Apologists' Step 0 applies to its own authors' complications.
