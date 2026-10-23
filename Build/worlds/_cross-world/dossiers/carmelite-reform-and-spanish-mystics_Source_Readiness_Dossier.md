# Source Readiness Dossier — The Carmelite Reform and the Spanish Mystics

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** VI.29
**Corpus-map slug:** `carmelite-reform-and-spanish-mystics`
**Time window:** 1562-1622 (St Joseph's, Avila, founded 1562; Teresa
canonised 12 March 1622 by Gregory XV, per the 1622 relation listed in §3)
**Region(s):** Castile, then Catholic Europe
**Dossier author / date:** library/source-research thread, Era VII session,
world VI.29 agent, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch
`library/era-vii-2026-10`. The corpus held no Teresa or John of the Cross
text before this pass. Five staging files are written and pass
`corpus_map_merge.py --check`; the generated bucket files had already been
merged once by another process from an earlier draft of these staging files,
so they are stale and need one full re-merge (see §5).

## 1. Already assigned

Nothing was assigned to this world before this pass. A grep of every
`Title:` and `Creator:` header line in `cic/texts/` for Teresa, John of the
Cross, Carmel, Discalced and the Spanish mystics found only the Discalced
Carmelite mission narratives of the 1650s (Sebastiani, Vincenzo Maria), filed
under the St Thomas Christians. The five files below were vendored this
pass and staged. All are English; all are public domain by date.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Life of St. Teresa of Jesus, written by herself (Lewis, 3rd ed. 1904, with Zimmerman's introduction) | teresa-of-avila | tradition | assigned | ~210,000 words | `teresa-of-avila_life_lewis1904.txt` |
| The Interior Castle, or The Mansions (Stanbrook translation, Zimmerman, 2nd ed. 1912) | teresa-of-avila | tradition | assigned | ~93,000 words | `teresa-of-avila_interior-castle_stanbrook1912.txt` |
| The Book of the Foundations (Lewis, 1913), the foundations narrative | teresa-of-avila | tradition | assigned | ~200,000 words in the whole volume | `teresa-of-avila_book-of-foundations_lewis1913.txt` |
| Teresa's paper on the visitation of nunneries, the Carmelite Rule, the rule of the nuns and the Constitutions for the sisters (same volume) | teresa-of-avila | tradition | assigned | the closing part of the same file | same file |
| The Dark Night of the Soul, Spiritual Canticle and Living Flame of Love (Lewis, 2nd ed. 1891), with the Instructions and Precautions, eighteen letters, a censure and the Spiritual Maxims | john-of-the-cross | tradition | assigned | ~192,000 words | `john-of-the-cross_dark-night-canticle-living-flame_lewis1891.txt` |
| The Life of Saint John of the Cross (Burns and Oates, 1873), compiled from the Life by Fra Joseph of Jesus and Mary | john-of-the-cross (compiler unnamed on the title page) | context | assigned | ~82,000 words | `john-of-the-cross_life_lewis1873.txt` |

The same files carry further rows for sibling entries, all `context` and
`provisional` unless stated: `the-tridentine-church` (Life, Interior
Castle, Foundations), `the-society-of-jesus` (Life, Foundations),
`the-carmelites` (Life, Foundations, the 1873 Life of John),
`colonial-latin-american-devotional-catholicism` (Foundations, the brother
back from the Indies; `needs-ruling`) and `quietist-controversy-molinos-guyon`
(John, `antecedent`, `needs-ruling`). See §2 and §5.

**Witness quality, stated plainly.** All five files read cleanly at five
sample points each. The Lewis 1904 Life has garbled front matter and a few
mis-read chapter headings (locate chapters by the contents table). The
Interior Castle and the 1873 Life of John carry "Digitized by Google" lines
and Google front matter, left in place. The 1891 John volume and the 1913
Foundations are clean. Each is ready to quote once each quote is checked
against the page image. These are nineteenth and early twentieth century
translations: the voice is Lewis's and Stanbrook's English, not Teresa's or
John's Spanish. Zimmerman's introductions and notes are the editor's voice and
must not be quoted as the saints'.

**Scale.** About 780,000 words in five files (4.2 MB). Four files are the
two protagonists speaking in their own words (Teresa, 500,000 words; John,
190,000); one is a later Carmelite narrative.

## 2. Cross-link opportunities

Checked: every `Title:`/`Creator:` header in `cic/texts/`, then a word search
of the vendored corpus for Teresa, John of the Cross, Carmel, Discalced,
Inquisition and the Council of Trent. Most hits are advertisements inside
other books (the Burns and Oates catalogue in `dositheus_*` and `bacci_*`)
and are not links. The real ones:

- **Gregory XIII's constitution for the Discalced Carmelites** in
  `bullarium-romanum_magnum-bullarium-tomus2-pius-iv-to-innocent-ix-lat_cherubini.txt`
  (assigned to `the-tridentine-church`): the papal act setting the Discalced
  apart from the mitigated friars, with the compiler's note naming "Teresia
  Hispana" as foundress. Loci: note at lines 125190-125230, constitution
  from line 125228, running-head year 1580 at lines 125411 and 125674. A
  proposed `context`, `assigned` row is in the crosslink fragment. Tier:
  same time-place. The strongest find of the pass. Not read to the end; the
  year in one running head reads 1590 in the OCR, so check the page image.
  More Carmelite material in the same volume (lines 113540-113667, on the
  order's property) is not read.
- **Council of Trent, Session XXV, Decree on Regulars and Nuns** in
  `council-of-trent_canons-and-decrees_waterworth1848.txt`: Teresa's
  Foundations argues from it by name (the Council allowed convents to hold
  revenues, lines 7135-7140 and 11413 of the Lewis 1913 file; a hermit group
  swept into the orders, line 10025), and Zimmerman cites the enclosure
  decree. That meets the `antecedent` rule. Proposed `antecedent`,
  `provisional` row in the crosslink fragment. Tier: same time-place.
- **The Spiritual Exercises** (`ignatius-loyola_spiritual-exercises_mullan1914.txt`,
  and the Spanish `ignatius-loyola_exercitia-spiritualia-et-directoria-lat-spa_1919.txt`):
  the Jesuit prayer discipline that shaped Teresa's confessors. No vendored
  Teresa text names the Exercises, so the proposed row is `context`,
  `needs-ruling`. Tier: same time-place.
- **Francis Borgia's letters** (`borgia_sanctus-franciscus-borgia-v4-lat_1910.txt`):
  an editor's quotation at line 25830 has Teresa, then at Salamanca, seeing a
  soul rise to heaven, and the index lists "Teresia (Teresa), Sta., Salmanticae"
  (line 42211). Teresa's Life, in Zimmerman's note at line 1850, says she told
  everything to Francis de Borja. A named link in both directions, but only a
  quotation, so no row proposed. Polanco's Chronicon vol. IV has only an
  editor's note at line 26392 (Teresa lodged in the convent of Santa Isabel when
  she came to found a Carmelite house). Tier: same time-place, named.
- **Borromeo, Instructions to religious persons** (`borromeo_ammaestramenti-alle-persone-religiose-ita_1902.txt`,
  already under `the-tridentine-church` and `tridentine-parish-renewal-borromean-milan`):
  the parallel Milanese reform of nuns and religious in the same decades.
  Tier: same time-different-region. A comparison text, not a link.
- **Bellarmine, The Mind's Ascent to God** (`bellarmine_minds-ascent-to-god_1925.txt`):
  a Jesuit ascent treatise of the same age, set against John's. Tier: same
  time-different-register. Not named by either side, so no row.
- **Sebastiani and Vincenzo Maria** (`sebastiani_*`, `vincenzo-maria_viaggio-indie-orientali-ita_1672.txt`,
  Discalced Carmelites on the Malabar coast, 1656-1658): the same order a
  generation after the window. Already staged under the St Thomas entries.
  Tier: out-of-window. Whether they continue this world is a question for §5.
- **The Philippine entries** (VI.19, VII.29): searched for Teresa, John of the
  Cross and Discalced Carmelites across the vendored corpus; the Blair and
  Robertson volumes have no hit, and the "Juan de la Cruz" of the 1593 Manila
  doctrina was sent to Bataan in 1588, so is another friar. No Carmelite text
  names the Philippines. No link.

## 3. Verified acquisition leads

Every row was read on the host page (archive.org metadata and the title page
in the OCR) on October 2026. All are public domain by date. Not vendored this
pass: size discipline, or a duplicate of what is vendored. Most are in the
seed fragment as `not-yet-downloaded`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Ascent of Mount Carmel (The Works of St. John of the Cross) | John of the Cross | David Lewis, rev. Benedict Zimmerman | 1906 | https://archive.org/details/TheAscentOfMountCarmel | public domain by date; host Public Domain Mark 1.0 | metadata and title page, nihil obstat "Die 22 Feb. 1906", October 2026. ~0.8 MB. Not in the 1891 volume. |
| The Way of Perfection | Teresa of Avila | Benedictines of Stanbrook, ed. Zimmerman | 1919 reprint of 1911 | https://archive.org/details/thewayofperfecti00tereuoft | public domain by date; host NOT_IN_COPYRIGHT | metadata and title page (imprimatur 29 January 1911, reimprimatur 21 March 1919), October 2026. ~0.6 MB. |
| The Letters of Saint Teresa, a complete edition, vol. II | Teresa of Avila | Benedictines of Stanbrook | 1921 | https://archive.org/details/lettersofstteres0002unse (also letterst02tere) | public domain by date | metadata and title page (imprimatur 24 February 1921), October 2026. ~0.6 MB. |
| The Letters of Saint Teresa, a complete edition, vol. III | Teresa of Avila | Benedictines of Stanbrook | 1922 (title page MCMXXII; host date 1921) | https://archive.org/details/lettersofsaintte03tere | public domain by date; host NOT_IN_COPYRIGHT | metadata and title page, letters from 201 (December 1577), October 2026. ~0.6 MB. Volume I not located; the set is "Letters" 1919-24 in the task. |
| Obras de Santa Teresa de Jesus, tomo I Libro de la vida, and tomos II-VI (Relaciones; Camino de perfeccion; Moradas, Conceptos, Exclamaciones; Fundaciones, 1918; Constituciones, Poesias) | Teresa of Avila | none (Spanish); ed. Silverio de Santa Teresa, C.D., Burgos, El Monte Carmelo | 1915-1918 | https://archive.org/details/obrasdesantatere01tere (to ...06tere) | public domain by date | metadata and title pages of tomos I-VI, October 2026. 1.3-1.7 MB each. |
| Obras de San Juan de la Cruz, tomos I-V (Preliminares; Subida y Noche oscura; Canticos; Llama de amor viva; Procesos de beatificacion y canonizacion I) | John of the Cross | none (Spanish); ed. Silverio de Santa Teresa, O.C.D., Burgos | 1929 | https://archive.org/details/obrasdesanjuande02john (to ...01, 03, 04, 05) | public domain by date (published 1929) | metadata and title pages, October 2026. 1.3-1.9 MB each. Tomo V holds sworn testimony about John. |
| Obras del Mistico Doctor San Juan de la Cruz, edicion critica, tomo primero (and tomos II, III) | John of the Cross | none (Spanish); ed. Gerardo de San Juan de la Cruz, Toledo, with an epilogue by Menendez y Pelayo | 1912 | https://archive.org/details/obrasedicincr01john | public domain by date | metadata and title page, October 2026. ~1.7 MB. The alternative to Silverio 1929. |
| Vida de Santa Teresa de Jesus | Francisco de Ribera, S.J. | none (Spanish); Barcelona, Gustavo Gili editor | 1908 | https://archive.org/details/vidadesantatere00ribegoog | public domain by date; host NOT_IN_COPYRIGHT | metadata and title page, October 2026. 2.3 MB. The earliest full Life, by a Jesuit. No PD English found (§4). |
| Regla primitiva, y constituciones de los religiosos descalzos de la orden de la bienaventurada virgen del monte Carmelo ... de la congregacion de Espana | host attribution: San Alberto de Jerusalen | none (Spanish) | 1736 | https://archive.org/details/regla_202106 | public domain by date; host Public Domain Mark 1.0 | host record read (title, 1736, 0.55 MB); title page not read, October 2026. A later printing of the friars' Constitutions, not the 1581 text. |
| Sermon predicado en el religiosissimo convento de las monjas Carmelitas Descalzas de Sevilla ... a la Canonizacion de la Gloriosa Madre Santa Teresa de Iesus | Fr. Juan Salvador, Order of Our Lady of Carmel | none (Spanish) | 1622 | https://archive.org/details/A11207207 | public domain by date; host Public Domain Mark 1.0 (Biblioteca de la Universidad de Sevilla) | metadata and title page ("siete de Otubre de 1622"), October 2026. ~70 KB. |
| Breue relacion de las ceremonias hechas en la canonizacion de los SS. Isidro Labrador, Ignacio de Loyola, Francisco Xauier, Teresa de Iesus y Phelippe Neri ... Gregorio Papa XV en 12 dias del mes de Marzo, ano de 1622 | printer Juan Rene (host attribution) | none (Spanish) | 1622 | https://archive.org/details/breuerelaciondelasceremoniashechasenlacanonizaciondelos-ss.-isidro-labrador-igna | public domain by date; host Public Domain Mark 1.0 | metadata and title page (rough OCR), October 2026. ~12 KB. |

Spanish and English pairs: the English volumes are vendored first and the
Spanish originals are leads, because the brief caps the vendored set. Teresa's
Life, Interior Castle, Foundations and Way of Perfection, and John's Dark
Night, Canticle and Living Flame, all have a Spanish edition in the table
above. Per `INTAKE.md` a clean public-domain Spanish original can be primary
evidence; the Silverio sets are the editions a build would quote from.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| "The lyf of the Mother Teresa of Jesus ..." 1611, item `bim_early-english-books-1475-1640_the-lyf-of-the-mother-te_ribera-francisco-de_1611` | Host credits Francisco de Ribera; an English print of 1611, public domain by date | The text is Teresa's own Life in the first person ("I"), not Ribera's Life, so the host attribution is wrong. The microfilm OCR is garbled (8,969 long-s glyphs and many misread words) and the book duplicates the vendored Lewis Life. Not vendored. It opens with a censure dated at San Felipe, Madrid, 1 September 1587 and signed in the OCR "Fre Lywerof Lyons" (possibly Fray Luis de Leon; unverified). |
| Ribera's Life of Teresa in English | The task asks for a public-domain English beside each Spanish text | Archive.org searches by creator and title found only the Spanish (1908), an Italian of 1615 (`bub_gb_JHloiSXIJscC`) and the misattributed 1611 print above. No English translation found. Gap recorded. |
| Yepes, Life of John of the Cross (1618) and Yepes's Life of Teresa | Named in the task | No item under Yepes's name for John was found. The Yepes items on the host are Italian translations of the Life of Teresa (1622, `bub_gb_ALlpWswliYEC`; 1623, `bub_gb_bGuQgDYF9PUC`; 1628, `wotb_6743798`; 1730, 1747). No Spanish original or English found. The English Life of John vendored this pass is compiled from Fra Joseph of Jesus and Mary instead. |
| Sister Agnes Mason's Foundations, Cambridge 1909 (`sainttheresahist00tereuoft`) | Clean OCR, NOT_IN_COPYRIGHT | A second translation of the same book. The Lewis 1913 volume was vendored instead because it also carries the Rule and the Constitutions. A lead if a second English voice is wanted. |
| Luis de Leon's 1588 edition of Teresa | Named in the task | Searches by title and creator found no 1588 edition. Rousselot's *Los misticos espanoles* (1907, `losmsticosespao00rousgoog`) is scholarship, not a source. Closed. |
| The 1622 canonisation bull (Gregory XV, "Omnipotens") | The world's end date | The Cherubini note cites it as "Greg. XV. conft. 20 Omnipotens". The vendored Bullarium volume ends at Innocent IX. Other Bullarium sets are on the host (for example Cherubini 1655, `bub_gb_mI9alFkq1gAC`, and the Turin series 1857-72) but I did not identify the volume holding the bull. An open lead. The sermon and the ceremonial relation in §3 are the nearest items found. |
| Jeronimo Gracian on the reform | Named in Teresa's Foundations as her Superior | His own works on the host (`A13303807` Mystica Theologia 1609; `A1150271` Leviathan enganoso 1614; `A1090422`, `A1090423` 1609) are not about the reform. Andres del Marmol's Life of Gracian (1619, `bub_gb_CdA8v993QSoC`, 0.75 MB) has an unreadable OCR (Cyrillic-like glyphs on the title page). No Gracian *Peregrinacion* or *Dialogos* found. Gap recorded. |
| Teresa's Life, 1904 Lewis, other copies (`lifeofstteresaof00tere`, `lifeofsteresaofj00tere` 1870, `lifesteresajesu00teregoog` 1870) | Same text | Duplicates of the vendored translation. Not needed. |
| Complete Works of St. John of the Cross, Lewis 1864 (`TheCompleteWorksOfSaintJohnOfTheV1`, `...V2`) | The task names Lewis 1864/1889/1906 | Same translator as the vendored 1891 and the Ascent lead; 1891 was the volume chosen. Available as a second edition if a build wants it. |
| Constitutions of the Discalced nuns, 1787 (`wotb_6743800`) | Spanish text of the nuns' Constitutions | A late Madrid printing (Imprenta de Joseph Doblado, confirmed by Pius VI in 1786), not Teresa's text. The Teresa Constitutions are in the Lewis 1913 volume in English and in Silverio tomo VI in Spanish. Closed. |
| Luis de Granada (*Sinner's Guide* 1886, `sinnersguide00luis_1`, Library of Congress, translator not read), Luis de Leon (*Nombres de Cristo*, 1917 Madrid, `delosnombresdecr01leon`; *Perfecta casada*), Francisco de Osuna (*Abecedario espiritual*, Seville 1528, `ARes54407`, gothic OCR garbled) | The task lists them as leads only | Not Carmelites. Found on the host and recorded; not run down to title pages. Left for a wider Spanish-mystics pass. |
| Teresa's Life, Dalton translation of 1851 | Another PD English translation | Same text; Lewis is the standard. Closed. |
| A Philippine or mission text naming the Carmelite reform | The task asks to check | None found (see §2). |

## 5. Open cross-world questions

- **Stale generated buckets.** The five buckets that list this world's
  files (`carmelite-reform-and-spanish-mystics`, `the-carmelites`,
  `the-society-of-jesus`, `the-tridentine-church`,
  `colonial-latin-american-devotional-catholicism`) were merged once, by
  another process, from an earlier draft that included
  `teresa-of-avila_book-of-foundations_mason1909.txt`, which does not exist.
  One full `corpus_map_merge.py` run prunes it. This dossier did not touch
  the generated files.
- **The Carmelites (IV.23, c. 1206-1300).** Teresa and the 1873 Life of John
  describe the mitigated order and the primitive Rule from the sixteenth
  century. Staged as `context`, `provisional`. Whether the two worlds share
  one Rule text (the Carmelite Rule is printed in the Lewis 1913 volume) is
  for a ruling.
- **The Tridentine Church (VI.22) and the Society of Jesus (VI.11).** The
  Teresa texts are staged as `context`, `provisional` on both. A build must
  decide whether a woman's mystical prose is voice for the Tridentine Church
  or context, and whether the Jesuit directors in her Life belong to VI.11 as
  outside testimony. Not decided here.
- **The Gregory XIII constitution and Trent Session XXV** are proposed as
  cross-link rows (§2). Both live in buckets belonging to other worlds.
- **Quietist Controversy (VII.14, listed Within Another World).** John is
  staged as `antecedent`, `needs-ruling` because that entry has no vendored
  source arguing from him yet.
- **Colonial Latin American Devotional Catholicism (VII.17).** One row
  (Lorenzo de Cepeda's return from the Indies, Foundations, contents line 13901) is
  `needs-ruling` and outside that entry's window.
- **Sebastiani and Vincenzo Maria (Malabar, 1656-58).** Discalced Carmelites
  a generation after 1622. Whether the world ends at 1622 or its order
  continues into those missions is a question for the census owner.
- **Roles for the 1873 Life of John.** Placed `context`, not `tradition`:
  a seventeenth-century Carmelite biography in a Victorian English
  compilation is neither the reform's voice nor an outsider's. A ruling may
  prefer `transmission` or a new role.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census floorNote reads "No question (intra-Catholic
reform, Inquisition-shadowed - the shadow is part of its story)". Nothing
seen this pass says otherwise. Zimmerman's introduction records Teresa's
Life held at the Holy Office and denounced to the Inquisition in 1574, and
the Life of John tells the Toledo imprisonment, both inside the world's own
story. A Doc_01 should disclose that the voices are Carmelite insiders and
that the library holds them in nineteenth-century English.

**Sourcing (B1) and ecology (B2).** Rich on the two protagonists, as the
census says: three of Teresa's major works in English (Life, Interior
Castle, Foundations with the Rule and Constitutions) and John's three
commentaries with his letters and maxims, about 780,000 words. The ecology
is lopsided toward the founders' own prose and Carmelite hagiography. The
honest gaps: no Gracian; no public-domain English for Ribera or Yepes; no
independent outside witness in English beyond the Gregory XIII constitution,
the Inquisition material in Zimmerman's apparatus, and the Trent and Jesuit
sources already in the corpus; the Spanish originals are leads, not in hand.

**Uniqueness (B3).** The Carmelites (IV.23) share the order but not the
century or the voice. The Tridentine Church (VI.22) and the Society of Jesus
(VI.11) share the frame but speak as institutions; this world is a woman's
reform from inside and a friar's poems from a prison. The Borromean Milan
entry (VI.12) is a parallel diocesan reform. Overlap is mapped in §2 and §5,
none of it disqualifying.

**Scale (B5).** Five files, 4.2 MB, 780,000 words. Smaller than the
Waldensian world, but denser in first-person voice.

**Recommendation: build.** The world's two named voices are vendored whole,
the floor is clear, the window is distinct from its siblings, and the
census's own note that this is "viable, secondary" is a statement about
priority, not about sources. The cost is that every voice is an English
translation of the Spanish, with the Silverio editions named as the next
acquisition, and that the outside witnesses (Gracian, Ribera, the
canonisation record) are thin. That is a normal Era VII condition, not a
reason to hold. This is a recommendation for Mark, not a decision.
