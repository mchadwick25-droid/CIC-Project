# Source Readiness Dossier — The Waldensian-Reformed Union

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** VI.10
**Corpus-map slug:** `the-waldensian-reformed-union`
**Time window:** 1532–1655+ (the census reads "1532-1655+"; the vendored
sources run to 1664 (Léger) and 1689 (Boyer))
**Region(s):** the Alpine valleys of Piedmont (Savoy) and Dauphiné (France),
with the Provençal Vaudois to 1545
**Dossier author / date:** library/source-research thread, Era VII session,
world VI.10 agent, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch
`library/era-vii-2026-10`. No `cic/corpus-map/the-waldensian-reformed-union.yaml`
existed before this pass; the seven staging files below are written and pass
`corpus_map_merge.py --check` (24 assignments across 6 Atlas entries), not
yet merged.

**Second pass, October 2026.** Three more files vendored with three staging
files: the 1644 first printing of Gilles (wording witness beside the 1881
text), the 1618 Perrin scan, which turns out to hold Parts II and III (the
doctrine and discipline with the old Vaudois texts), and Crespin tome 1 for
Merindol and Cabrieres (1545). Lentolo was looked for again and not found:
archive.org has only his grammars, and Google Books could not be used this
session (zero API quota, a 429 on the web search after one query). The
vendored leads moved from sections 3 and 4 into section 1; section 6 revised.

## 1. Already assigned

Nothing was assigned to this world before this pass. The corpus held no
Waldensian text at all: a grep of every `Title:` and `Creator:` header line
in `cic/texts/` for Waldens, Vaudois, Valdes, Piedmont and Piemont found no
file. The seven files below were vendored this pass and staged.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The History of the Evangelical Churches of the Valleys of Piemont (1658), whole volume | morland | context | assigned | ~2.35M chars | `morland_history-evangelical-churches-piemont_1658.txt` |
| The valleys' own documents printed by Morland: the Angrogna confession of 12 September 1532, the ancient confessions, a brief Confession of the Reformed Churches of Piemont (Italian), the supplications of 1655, the depositions of the massacre | morland | tradition | assigned | part of the above | same file |
| Histoire ecclésiastique des Églises Vaudoises, tome I (1644; Pignerol 1881), chapters I–XXXVIII | gilles | tradition | assigned | ~756K chars, French | `gilles_histoire-ecclesiastique-eglises-vaudoises-v1-fra_1881.txt` |
| Histoire ecclésiastique des Églises Vaudoises, tome II, chapters XXXIX–LXII (to 1643) | gilles | tradition | assigned | ~829K chars, French | `gilles_histoire-ecclesiastique-eglises-vaudoises-v2-fra_1881.txt` |
| Histoire générale des Églises Évangéliques des Vallées de Piémont, livre I (1669): doctrine, discipline, confessions | leger | tradition | assigned | ~1.23M chars, French | `leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt` |
| Histoire générale, livre II: the persecutions to 1664 with the 1655 massacre and the lists of the killed | leger | tradition | assigned | ~1.90M chars, French | `leger_histoire-generale-eglises-vaudoises-livre2-fra_1669.txt` |
| Histoire des Vaudois (1619), Part I, with the 1532 articles | perrin | tradition | assigned | ~443K chars, French | `perrin_histoire-des-vaudois-fra_1619.txt` |
| History of the Old Waldenses and Old Albigenses with the doctrine and catechism (Perrin, English, 1624 translation reprinted 1847) | perrin | tradition | assigned | ~1.0M of ~1.9M chars | `perrin_history-ancient-christians-valleys-alps_1847.txt` |
| History of the Vaudois (Boyer, 1692, with additions from Arnaud), Part III of the same volume | boyer | context | assigned | ~0.6M chars of the same file | same file |
| Histoire ecclesiastique des Eglises Reformees des Valees de Piedmont, the first printing (Geneva 1644): the wording witness for the 1881 text | gilles | tradition | assigned | ~1.67M chars, French | `gilles_histoire-ecclesiastique-eglises-reformees-vallees-de-piemont-fra_1644.txt` (second pass) |
| Histoire des Vaudois (1618), Parts II and III: the Albigeois history, and the doctrine and discipline with the old Vaudois texts in parallel columns | perrin | tradition (Part III); context for the Albigenses entry (Part II) | assigned | ~0.48M chars, French and Vaudois | `perrin_histoire-des-vaudois-parties-2-3-fra_1618.txt` (second pass) |
| Histoire des martyrs, Tome 1 (1619 edition; 1885): 'Ceux de Merindol et Cabriere', the Provencal Vaudois and the massacre of 1545 | crespin | tradition | provisional | ~4.1M chars, French (the Merindol section is a small part) | `crespin_histoire-des-martyrs-t1-fra_benoit-lelievre1885.txt` (second pass) |

The same files carry further rows for sibling entries: `waldensians-in-the-alps`
(Morland's, Léger's, Gilles's and Perrin's medieval material, `tradition`,
`provisional`), `the-waldensians` (`context`, `provisional` or `needs-ruling`,
see §5), `the-huguenots` (`context`, `provisional`), `the-reformed-cities-zurich-and-geneva`
(Gilles on the 1532 synod, `context`, `provisional`) and `cathars-albigensians`
(Perrin's Albigenses, `context`, `provisional`).

**Witness quality, stated plainly.** Gilles (1881 re-edition) and the 1847
English Perrin/Boyer volume have clean OCR and are ready to quote once each
quote is checked against the page image. Morland (1658), Léger (1669) and
the French Perrin (1619) are seventeenth-century printings whose OCR renders
the long s as the letter f throughout (not as the long-s glyph the quote
gate can normalise); they are second witnesses for exact wording until a
cleaner scan or a transcription is vendored. Léger Book II is the worst of
the three (garbled title page, marginalia and closing pages), though the
body reads.

The three second-pass files are second witnesses too. Gilles 1644 reads at
about 0.69 with every chapter heading lost, so a passage is found there by
phrase from the 1881 text; it exists to confirm first-printing wording, not
to quote from. Perrin 1618 reads at about 0.64, the parallel columns of the
Vaudois tongue and French interleaved by the OCR; the Vaudois texts need the
page image. Crespin tome 1 reads at about 0.71 (f for long s), like tome 3.
Perrin 1618 corrects the first pass: the scan is not another Part I but
Parts II and III, so the French of all three parts is now in the corpus.

**Scale.** About 9.4 million characters in seven files: roughly 4.4M in
French, 5.0M in English. Three insider pastor-historians (Perrin 1619,
Gilles 1644, Léger 1669), one sympathetic outsider (Morland 1658), one
later outsider narrative (Boyer 1692). Confessional and testimonial texts
are embedded in these, not separate.

## 2. Cross-link opportunities

Every vendored file whose body mentions Waldens, Vaudois, Valdes, Piedmont
or Piemont was listed and the hits read.

- **Calvin's Letters, vols. I, II and IV** (`calvin_letters-vol1_bonnet1858.txt`,
  `-vol2-`, `-vol4-`, assigned to `the-reformed-cities-zurich-and-geneva`).
  Vol. I: LXXXI to Farel (line 14004) on the Vaudois of Provence; CXXXI to
  Farel (line 20769) and CXXXVII to Bullinger on the 1545 massacre of
  Mérindol and Cabrières. Vol. II: CCLV to Wolfgang Musculus (line 11779) on
  the prohibition of the Vaudois conferences, with Bonnet's note at line 943.
  Vol. IV: DC to the Pastors of Zurich, 14 July 1561 (line 9512), a
  collection for the churches of Piedmont after the 1560–61 war. Tier: same
  time-place (Geneva's own side of the union). Rows proposed in
  `crosslink_fragment.yaml`. Note that vol. IV's DLXVII "To the Waldenses"
  (line 5506) is to the Bohemian Brethren, per Bonnet's footnote, and is not
  a Piedmont letter.
- **Van Braght, Martyrs' Mirror** (`van-braght_martyrs-mirror_sohm1886.txt`,
  lines 158808–158830): a Dutch magistrates' letter of the 1660s recalls the
  collections "in the year 1655, when the Vaudois ... were so miserably
  dispersed". One passage, a Dutch Mennonite witness to the international
  response. Tier: same time, different region. No row proposed; noted here
  for a build.
- **Unity of the Brethren, Church Constitution** (`unity-of-the-brethren_church-constitution_seifferth1866.txt`,
  lines 203–206, 4094–4128, 8021): the Brethren's own account of taking
  ordination from the Waldenses in the 1460s. Serves the medieval Waldensian
  entries, not this one. Tier: out-of-window. No row proposed here; flagged
  for `waldensians-in-the-alps`.
- **Zwingli, Latin Works vol. III** (`zwingli_latin-works-correspondence-vol3_heller1929.txt`,
  lines 11293–11325): Zwingli on the Waldensian view of the Eucharist, with
  the editor's note that Luther called the Bohemian Brethren Waldenses. A
  passing reference, not a link. No row.
- Jesuit Latin volumes (Lainez, Nadal, Polanco, Borgia) carry a few mentions
  each of "Valdenses" or Piedmont in the 1560s; not opened beyond the hit
  lines. Out of scope for this pass; a build that wants the Catholic
  mission's view of the valleys in the 1560s should look there.

## 3. Verified acquisition leads

All seven vendored editions were verified on the Internet Archive item
(metadata fetched, full text fetched and sampled at five points, title page
read in the OCR) on October 2026. Rows for each are in `seed_fragment.yaml`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The History of the Evangelical Churches of the Valleys of Piemont | Samuel Morland | none (English) | 1658 | `archive.org/details/historyofevangel00morl` | pd-us-by-date; item carries no rights field, no access restriction; Princeton copy | direct fetch, metadata and OCR title page, October 2026. VENDORED. |
| Histoire ecclésiastique des Églises Vaudoises, tomes I–II | Pierre Gilles | none (French) | 1881 (of 1644) | `histoireecclesia01gill`, `histoireecclesia02gill` | pd-us-by-date; no rights field; Princeton copies | direct fetch of both, October 2026. VENDORED. |
| Histoire générale des Églises Évangéliques des Vallées de Piémont, livres I–II | Jean Léger | none (French) | 1669 | `bub_gb_kzsAtn028N8C` (Book I), `bub_gb_Yf_DYoc9lb0C` (Book II) | pd-us-by-date; Public Domain Mark on both; National Library of Naples | direct fetch of both, October 2026; the two scans are the two Books of one printing. VENDORED. |
| Histoire des Vaudois (Part I) | Jean Paul Perrin | none (French) | 1619 | `bub_gb_i-OELQwHc4IC` | pd-us-by-date; Public Domain Mark | direct fetch, October 2026; body ends with Part I. VENDORED. |
| History of the Ancient Christians inhabiting the Valleys of the Alps | Perrin; Boyer (Part III) | the 1624 translation, reprinted | 1847 | `historyancientc00boyegoog` | pd-us-by-date; NOT_IN_COPYRIGHT; NYPL copy | direct fetch, October 2026. VENDORED. |
| Histoire ecclésiastique des Églises Réformées ... autrefois appelées Églises Vaudoises (the 1655 Geneva printing, Jaques Remondet) | Pierre Gilles | none | 1655 | `bub_gb_3bpEABVwNjwC` | pd-us-by-date; Public Domain Mark; National Central Library of Rome | direct fetch and five-point sample in the second pass, October 2026: about 0.68, no better than the 1644 scan, which was vendored instead (section 1). Stays a lead only as a second scan. |
| Luthers fore-runners (the 1624 English Perrin, all three parts) | Perrin | catalogued as Samuel Lennard (not read off the OCR) | 1624 | `bim_early-english-books-1475-1640_luthers-fore-runners-_perrin-jean-paul_1624` | pd-us-by-date; no rights field | direct fetch and sample, October 2026. Not vendored: 16,302 long-s glyphs and many broken words; the 1847 reprint is clean. |
| The History of the Vaudois | Pierre Boyer | none | 1692 | `bim_early-english-books-1641-1700_the-history-of-the-vaudo_boyer-pierre_1692_0` | pd-us-by-date; no rights field | metadata only, October 2026. Not vendored: the 1847 volume carries it. |
| An Account of the late persecution of the Protestants in the vallys of Piemont ... 1686 | anonymous | none | 1688 | `accountoflateper00unse` | pd-us-by-date; no rights field; Princeton copy | metadata only, October 2026. After the main window. |
| History of the Waldenses of Italy, from their origin to the Reformation | Emilio Comba | Teofilo E. Comba | 1889 | `historyofwaldens00comb` (also `cu31924029440512`) | pd-us-by-date; no rights field | direct fetch and sample, October 2026. Secondary; no Chanforan text in it. |
| The Israel of the Alps, 2 vols. | Alexis Muston | John Montgomery | 1875 (1866 first ed. `israelalpsacomp01mustgoog`; 1852 Hazlitt tr. `israelalpsahist00mustgoog`) | `israelofalpscomp01must`, `israelofalpscomp02must` | pd-us-by-date; no rights field | direct fetch and sample, October 2026. Secondary. |
| Waldensian researches during a second visit to the Vaudois of Piemont | W. S. Gilly | none | 1831 (1824 Narrative: `narrativeofexcur00gill`) | `waldensianresear00gill` | pd-us-by-date; no rights field | direct fetch and sample, October 2026. Secondary, out of window. |
| The Olivetan Bible (French, 1535) | Pierre Robert Olivétan | — | 1535 | `olivetan`; `bible_olivetan_1535` (stated as from e-rara.ch) | Public Domain Mark on both | metadata only, October 2026; file lists not checked for a text derivative. Out of scale for the corpus; only the preface and dedication would serve a build. |
| Some remarks upon the ecclesiastical history of the ancient churches of Piedmont | Pierre Allix | none | 1690 (Oxford 1821 reprint `someremarksupone00alliuoft`, NOT_IN_COPYRIGHT) | `someremarksupone00alli_0` (1690) | pd-us-by-date | metadata only, October 2026. Antiquity polemic; serves the medieval entries, if anything. |
| A history of the Vaudois church from its origin | Antoine Monastier | — | 1846 (French 1847 `histoiredelglis01monagoog`) | `historyofvaudois00monauoft` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata only, October 2026. Secondary. |

**No public-domain English exists for Gilles or Léger.** Neither work was
ever translated in full; the archive.org creator and title searches returned
only the French. Morland (1658) and Perrin/Boyer (1847) are the English
witnesses to the same events. Recorded as a gap, not a failure to search.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Lentolo's manuscript history (1560s; printed by Teofilo Gay, Torre Pellice, 1906) | The census names it; the earliest insider history | archive.org creator search "Lentolo" returns only his Italian grammars (`bub_gb_WwGIhoUhIB8C`, `bub_gb_3M-FVYVYAlIC`); title searches on "persecutioni"/"persecuzioni" with "valli"/"valdesi" and creator "Gay, Teofilo" return nothing. Not found on any reachable host. A 1906 Italian printing would be public domain by date if located. Second pass, October 2026: a creator search for Lentolo, Lentulo and Lentolus on archive.org again found only the grammars and a 1575 English printing of the Italian grammar; the Google Books API answered with a zero daily quota and the Google Books web search with a 429 after one query, so that host was not searched. Still not found. |
| Perrin 1618 Geneva printing `bub_gb_x_0dyBHt4kcC` | A second scan of the French Perrin, perhaps holding Parts II to III | Second pass, October 2026: fetched and read. It is Parts II and III, not Part I, and was vendored (section 1). Removed from this list. |
| Morland, second scan `the-history-of-the-churches-of-piemont` (opensource upload) | A second OCR of the same 1658 book | Fetched and compared: no contributor, fewer chapter headings survive, and the closing pages are garbage. The Princeton scan is the better witness and was vendored. |
| Gilles 1881, Google/Harvard one-volume scan `histoireecclsia00gillgoog` | Marked NOT_IN_COPYRIGHT | Fetched: 666K chars against 1.55M for the two Princeton volumes, and the 30% sample is garbled. Not a complete witness; the Princeton pair was vendored. |
| The Synod of Chanforan articles (1532) as a separate printing | The union's founding act | No separate printing found. The articles are in hand four times inside vendored files: Perrin 1619 French (articles I–XVII around line 12113), Perrin 1847 English (Part I, around lines 5232–5698), Morland 1658 English (the Angrogna confession heading above line 7942), and Gilles tome I (the synod chapters around line 2447). The census is right that they survive only in later copies. |
| The Waldensian Confession of 1655 as a separate printing | The community's own creed after the massacre | No separate printing found. Morland prints confessions of the Reformed Churches of Piemont in Italian (headings at lines 9438, 9686, 10820); Léger Book I ends with "la dernière Confession de leur Foy" (introduced at line 14685). Which printed text is the 1655 confession was not settled this pass; a build verifies it against the page images. |
| The Olivetan Bible text | The union's deliverable | Two Public Domain Mark items exist (§3). Not vendored: a whole Bible is out of scale; only the preface and Calvin's Latin preface would serve. Open as a narrow lead, not closed as absent. |
| Milton's sonnet | Named in the census | Not a source for this world (a response from outside); not searched. |
| EEBO pamphlets of 1689–1699 (the Vaudois march, the exiled Vaudois, the Duke of Savoy's 1694 proclamation) | Contemporary English on the Glorious Return | Seen in the title search; not fetched. After the window; the 1847 Boyer/Arnaud text covers 1689. Listed here so a later "Glorious Return" pass starts from the identifiers: `bim_early-english-books-1641-1700_a-journal-of-all-that-ha_1689`, `bim_early-english-books-1641-1700_the-present-state-of-the_1691`, `bim_early-english-books-1641-1700_the-case-of-the-exiled-v_wake-william-abp_1699`. |
| Cappel, La doctrine des Vaudois (1618) `ladoctrinedesvau00capp` | A 1618 French statement of Waldensian doctrine | Seen in the title search; not fetched. Jacques Cappel was a Sedan professor, so this is a Huguenot apologetic, not the valleys' voice. Open for a later pass. |
| Cameron, The Reformation of the Heretics (1984); Audisio, The Waldensian Dissent (1999) | The census's secondary works | In copyright; not searched. |

## 5. Open cross-world questions

- **The "ancient" documents and the medieval entries.** Morland (1658) and
  Léger (1669) print the valleys' manuscripts (the Nobla Leyczon, the
  treatises, the confessions) and date them to the twelfth century. Modern
  scholarship dates most of the manuscripts to the fifteenth and early
  sixteenth centuries. The rows for `waldensians-in-the-alps` (1300–1517)
  are `provisional` on that basis; the rows for `the-waldensians` (c. 1173
  onward) are `needs-ruling` because the twelfth-century claim is the
  contested point itself. Léger's backdating is also part of this world's
  own story (the census says so). Whoever builds any of the three
  Waldensian entries should settle, once, which world reads these texts as
  voice and which as context.
- **Three Waldensian entries on the Atlas.** `the-waldensians` (c. 1173
  onward, Lyon and the Alps), `waldensians-in-the-alps` (1300–1517) and this
  one (1532–1655+). The vendored histories all start at 1160 and run through
  all three windows. The staging files map each to all three, with
  `tradition` only for the window the author wrote in. The census's own
  split is sound; the library does not need to merge them.
- **The Huguenots (VI.6), no dossier yet.** Perrin was a pastor at Nyons in
  Dauphiné and dedicated his book to Lesdiguières; Gilles and Léger report
  the French king's edicts for the Dauphiné valleys (Pragela, Val Cluson)
  and the French part in 1655; Léger wrote from the Walloon church of Leiden.
  `context`/`provisional` rows are staged for `the-huguenots`. The Provençal
  Vaudois of Mérindol and Cabrières (1545) sit between this world and the
  Huguenots; the Calvin letters on them are proposed for this world only.
- **The Reformed Cities (VI.2, built).** Gilles tome I on the 1532 synod with
  Farel and Saunier, and the Calvin letters above, are the two sides of one
  event. One `context`/`provisional` row is staged for that world. Its build
  thread may want to read the Chanforan chapter.
- **Cathars/Albigensians (floor-question register).** Perrin's Part II treats
  the Albigenses as Waldenses, a claim the sources do not bear out. One
  `context`/`provisional` row is staged there so that entry can see a
  seventeenth-century Protestant reading of the crusade; nothing more is
  claimed.
- **Author slug `boyer`.** Part III of the 1847 volume is Boyer's work, not
  Perrin's, and the staging file carries an `authors_ruled` block
  (metadata-omission) with the volume's own preface as evidence. The lead
  should confirm the slug when merging.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census floorNote reads "No question." The vendored
confessions bear that out on their face: Morland's 1532 Angrogna articles and
the Italian confessions of the Reformed Churches of Piemont are Reformed
creeds (Trinity, incarnation, two sacraments). Nothing seen this pass raises
a creedal question. The one disclosure a Doc_01 should carry is historical,
not doctrinal: the medieval "ancient" documents are dated by this
community's own historians to a century they do not belong to.

**Sourcing (B1) and ecology (B2).** Moderate-to-rich, as the census says,
and now in hand. Three insider pastor-historians in French across the whole
window (1619, 1644, 1669), the union's founding articles in French and
English, the 1655 depositions and the diplomatic record in English, and a
later English narrative to 1689. The honest gaps: no public-domain English
for Gilles or Léger; the seventeenth-century printings are second witnesses
for wording until checked against page images; the ordinary believer's
voice survives only in Morland's depositions and Léger's lists of the dead;
Lentolo is not found; the Chanforan "decisions" exist only in later copies.
The second pass added the first printing of Gilles for wording checks, the
French of Perrin's doctrine and discipline (the valleys' own old texts as
the union's apologist printed them), and Crespin's record of the Provencal
Vaudois to 1545, which the region line names and no file carried before.
Lentolo was looked for again and is still not found.
The ecology is pastor-historian heavy, with a strong martyrological
register after 1655.

**Uniqueness (B3).** The union of a medieval dissent with the Reformed
churches, and the memory-keeping that followed, is a story no sibling world
tells. Overlap with the medieval Waldensian entries is in the sources, not
the window; overlap with the Huguenots is at the French edge of the
valleys. Both are mapped, neither disqualifies.

**Audiences (B4).** The Waldensian church of Italy is a living body that
keeps this memory; the 1655 massacre and the Protestant international
response are widely known. A real audience exists.

**Scale (B5).** About 15.7 million characters in ten files after the second
pass (9.4M in the first seven), comparable to a mid-size built world; most of
the primary voice is French, and Crespin tome 1 is mostly matter for the
Huguenot world's prehistory.

**Recommendation: build.** Unchanged by the second pass, which added wording
witnesses and the Provencal Vaudois rather than a new kind of source. The
world's own named primary works (Gilles,
Léger, Morland, the Chanforan articles) are vendored and verified; the floor
is clear; the window is distinct from its siblings; and the one real cost,
that the insider voice is French and the seventeenth-century OCR needs
page-image checking, is the ordinary Era VII condition this library already
works under. This is a recommendation for Mark, not a decision.
