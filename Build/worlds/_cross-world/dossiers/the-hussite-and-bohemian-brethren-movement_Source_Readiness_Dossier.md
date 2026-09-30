# Source Readiness Dossier — The Hussite and Bohemian Brethren Movement

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.6
**Corpus-map slug:** `the-hussite-and-bohemian-brethren-movement`
**Time window:** c. 1402–1517 (the census entry still reads 1415–1517; see §6)
**Region(s):** Bohemia (with Moravia for the Unity of the Brethren)
**Dossier author / date:** source-research thread, 2026-09-25; refreshed 2026-09-30 against `cic/texts/` and `cic/corpus-map/`
**Corpus-map / `cic/texts/` state as of:** 2026-09-30 — eight works are vendored and assigned. See §1.

## 1. Already assigned

**Eight works** are vendored and assigned to
`cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml`: two in
`tradition` role (Hus's own voice) and six in `context` role.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Letters of John Hus (Workman & Pope, 1904) | hus | tradition | assigned | ~673K chars | `hus_letters_workman-pope1904.txt` |
| De Ecclesia. The Church (Schaff, 1915) | hus | tradition | assigned | ~738K chars | `hus_de-ecclesia-the-church_schaff1915.txt` |
| *Historia Bohemica* (Piccolomini, 1592 Latin printing) | piccolomini | context | assigned | ~387K chars | `piccolomini_historia-bohemica-lat_1592.txt` |
| Church Constitution of the Bohemian and Moravian Brethren (*Ratio Disciplinae*, 1632/33; ed. Seifferth, 1866) | unity-of-the-brethren | context | assigned | ~343K chars | `unity-of-the-brethren_church-constitution_seifferth1866.txt` |
| The Life & Times of Master John Hus (Lützow, 1909) | lutzow | context | assigned | ~1.03M chars | `lutzow_life-and-times-of-hus_1909.txt` |
| The Hussite Wars (Lützow, 1914) | lutzow | context | assigned | ~990K chars | `lutzow_hussite-wars_1914.txt` |
| Bohemia: An Historical Sketch (Lützow, 1920) | lutzow | context | assigned | ~1.04M chars | `lutzow_bohemia-historical-sketch_1920.txt` |
| The Life and Times of John Huss, Vol. II (Gillett, 1871) | gillett | context | assigned | ~1.47M chars | `gillett_life-and-times-of-huss-v2_1871.txt` |

The two `tradition` works are Hus's own voice. No Unity of the Brethren
material from inside the window (1457–1517) is vendored: the *Ratio
Disciplinae* is a 1632/33 text and falls outside it. Piccolomini is a
contemporary hostile source; its scan carries systematic long-s errors
and interleaved marginal notes (see Doc_02).

## 2. Cross-link opportunities

- **Lollardy (V.5).** The link is direct textual borrowing, not a
  contested influence line. Schaff's translator introduction to the
  vendored *De Ecclesia* says Hus took whole paragraphs from Wyclif.
  Wyclif's own *Tractatus de Ecclesia* (`wyclif_de-ecclesia-lat_loserth1886.txt`)
  is vendored under Lollardy. Foxe's *Acts and Monuments*, Vol. III
  (`foxe_acts-and-monuments-v3_cattley-townsend1837.txt`) is assigned to
  Lollardy only; its own contents list carries Hus material (the
  Constance proceedings, Hus's letters, the Four Articles). It has not
  been checked for this world.
- **Lutheran Wittenberg (VI.1).** Luther's vendored works name the
  Bohemians and Hus directly (for example, the 1520 *Address to the
  Christian Nobility* in `luther_works-v2-selected_jacobs-spaeth1916.txt`).
  These are later (post-1517) witnesses to the tradition.
- **The Anabaptist Movements (VI.3).** No overlap identified.

## 3. Verified acquisition leads

The two originating leads, both now vendored:

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Letters of John Hus | Jan Hus | Herbert B. Workman & R. Martin Pope | 1904 | archive.org `lettersofjohnhus00husjuoft` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch, 2026-09-25, metadata and body text both checked |
| De Ecclesia. The Church | Jan Hus | David S. Schaff | 1915 | archive.org `deecclesiachurc00hussgoog` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch, 2026-09-25, metadata and body text checked |

**Scale (rough):** about 6.1 million characters in eight works. In
tradition-role terms it is one author in two genres (letters and a
systematic treatise), the same shape as a single-pillar world.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| *The Appeale of John Hus from the General Council's Excommunication* (London, 1662) | A short 17th-century English printing of a Hus text, archive.org `bim_early-english-books-1641-1700_the-appeale-of-_hus-jan_1662`, `NOT_IN_COPYRIGHT` | The OCR is unusable throughout. Not vendored. The vendored *Letters* already carry Hus's appeal language. |
| Unity of the Brethren primary material (a confession, a catechism, or the 1501 hymnbook) | The stricter branch the census names | A broad archive.org search (2026-09-25) found no period primary source. Still unresolved, not assumed absent. One named lead exists in the vendored Seifferth introduction: the Brethren's 1504 Confession to King Vladislav and their 1508 letters to Dr. Augustine are said to have been first printed in the *Fasciculus rerum expetendarum et fugiendarum* (Cologne, 1535). That volume is not fetched or vendored. |

## 5. Open cross-world questions

**Vs. Lollardy (V.5).** The census's Lollardy entry names a "contested
influence line to the English Reformation." That line does not run to
Hussitism. The Hussite link to Wyclif is direct textual borrowing (§2),
established by Schaff's introduction to the vendored *De Ecclesia*. The
two movements diverged sharply in outcome: Lollardy stayed underground,
while Hussitism won legal recognition in 1436. They are correctly two
separate candidates. A whole-of-tradition scholarly debate also exists
over how much Hus owed to Wyclif and how much to earlier Bohemian
reformers (Lützow's 1909 biography stresses the Bohemian forerunners).
Doc_01 for either world should carry both.

**Census hymnbook wording.** The claim that the Unity printed "what is
often called the first hymnbook in a European vernacular" by 1501
appears in the census entry's `why` and `longDescription` fields. It does
not appear in `relationsSummary`.

## 6. Step 0 scope notes

**Doctrinal floor:** the Step 0 check (`Build/worlds/hus/Step0_Movement_Scope_Confirmation.md`)
found no creedal question in Hus's own voice. Doc_01 extends that check
across all five commitments of Article 4 and across the movement's other strands.

**Scale honestly stated:** thin in named tradition voices (Hus alone) but
each of his two vendored works is substantial. The movement's
institutional and legal story (the 1436 Compactata) and the Unity's
in-window voice are covered only by context-role secondary works and one
hostile Latin chronicle.

**Census record still to update:** the V.6 entry's `dates` field still
reads "1415-1517"; the window is c. 1402–1517 (the entry's own
`statusDescription` already says the Prague formation runs 1402–14).
The corpus-map notes for the *Letters* ("his career at the university")
and several others need a hygiene pass in `cic/corpus-map/_staging/`.
