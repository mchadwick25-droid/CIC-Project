# Source Readiness Dossier — Puritanism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.8
**Corpus-map slug:** `puritanism`
**Time window:** c. 1560–1660
**Region(s):** England, New England
**Dossier author / date:** library/source-research thread (Era VII session, one-world agent for VI.8), 2026-10-16
**Corpus-map / `cic/texts/` state as of:** 2026-10-16, branch `library/era-vii-2026-10`. No `cic/corpus-map/puritanism.yaml` bucket existed before this pass. The eleven staging files below are written and pass `corpus_map_merge.py --check`; the lead merges them. The English Reformation (VI.4) agent vendored its own files the same day, and the cross-links in section 2 point at those files by name.

## 1. Already assigned

Eleven files were vendored this pass and assigned in `cic/corpus-map/_staging/`. Nothing was assigned to this world before 2026-10-16.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Diary of Lady Margaret Hoby, 1599–1605 | hoby | tradition | assigned | 650 KB, diary c. 10,000 lines | `hoby_diary-1599-1605_meads1930.txt` |
| Historical Notices, Vol. I (Wallington's notebooks) | wallington | tradition | assigned | 600 KB | `wallington_historical-notices-v1_webb1869.txt` |
| The Diary of Richard Rogers (1587–90) | rogers-richard | tradition | assigned | 360 KB for both diaries | `knappen_two-elizabethan-puritan-diaries_1933.txt` |
| The Diary of Samuel Ward (1595–1632) | ward-samuel | tradition | assigned | same file | `knappen_two-elizabethan-puritan-diaries_1933.txt` |
| The Autobiography of Thomas Shepard | shepard | tradition | assigned | 190 KB | `shepard_autobiography_adams1832.txt` |
| Winthrop's Journal, Vol. I (1630–40) | winthrop | tradition | assigned | 830 KB | `winthrop_journal-v1_hosmer1908.txt` |
| A Golden Chaine, with the other treatises of the 1600 volume | perkins | tradition | assigned / provisional | 4.2 MB, second witness | `perkins_golden-chaine-and-treatises_legat1600.txt` |
| Seven Treatises (1610) | rogers-richard | tradition | assigned | 2.9 MB, second witness | `rogers-richard_seven-treatises_1610.txt` |
| An Admonition to the Parliament, the Exhortations, A Second Admonition, Certaine Articles (1572) | admonition-to-parliament | tradition | assigned | 540 KB | `admonition-to-parliament_puritan-manifestoes_frere-douglas1907.txt` |
| Minute Book of the Dedham Classis, 1582–89, with its letters | dedham-classis | tradition | assigned | 380 KB | `dedham-classis_minute-book_usher1905.txt` |
| Bancroft's narrative of the Presbyterian movement (in Usher's introduction) | bancroft | context | assigned | same file | `dedham-classis_minute-book_usher1905.txt` |
| Westminster Confession; Larger and Shorter Catechisms | westminster-assembly | tradition | assigned | 1.9 MB with proofs | `westminster-assembly_confession-catechisms-standards_nelson1877.txt` |
| Directory for Publick Worship, Form of Church-Government, Solemn League | westminster-assembly | tradition | provisional | same file | `westminster-assembly_confession-catechisms-standards_nelson1877.txt` |
| The Bruised Reed; The Soul's Conflict; shorter sermons | sibbes | tradition | assigned / provisional | 2.3 MB | `sibbes_complete-works-v1_grosart1862.txt` |
| Grosart's Memoir of Sibbes; Adams's notices of Shepard | sibbes; shepard | context | assigned / provisional | editorial matter | the two files above |

Cross-entry rows written in the same staging files: Hoby (VI.4, context, provisional); Perkins's Golden Chaine (VI.4, context, provisional); the Admonitions (VI.4, context, assigned); the Westminster Confession and Catechisms (VI.5 Scottish Kirk, tradition, assigned); the Scottish standards printed with them, the Sum of Saving Knowledge, the covenants and the directories (VI.5, tradition, assigned).

Rights. Nine files are public domain by date (1600 to 1908 imprints, read in each file's own OCR). The Hoby diary is a 1930 publication, public domain by date since 1 January 2026. The Knappen diaries are a 1933 US publication: no renewal was found in the Catalog of Copyright Entries renewal volumes for 1960, 1961 and 1962 (Project Gutenberg transcriptions #11821 to #11826, searched for Knappen, 'Elizabethan Puritan' and 'American Society of Church History'), and the archive.org item's rights field records a HathiTrust copyright review finding public domain. The NYPL `cce-renewals` repository could not be reached from this session (GitHub access to that repository is not enabled), so the Gutenberg transcriptions of the same catalog were used; the search terms and volumes are in the file header.

OCR. Nine files are clean at all five sample points. Two are second witnesses under Mark's OCR ruling of 2026-09-25: Perkins (1600 print) and Rogers (1610 print), both with systematic long-s misreads. They locate passages; a quotation from either must be verified against the page images first. No cleaner public-domain scan of either exists on archive.org (the EEBO microfilm items are worse).

Scale. The eleven files total about 15 MB. The census names four primary genres (diaries, conversion narratives, practical divinity, church-order records); each is now represented by at least one clean file, which is why the intake runs to eleven files rather than the usual six to eight.

## 2. Cross-link opportunities

Checked by grepping every `Title:` and `Creator:` header line and then the full text of the vendored corpus for this world's own figures and controversies (Cartwright, Perkins, Puritan, Sibbes, Baxter, Winthrop, Shepard, Westminster Assembly, Admonition, Marprelate). Proposed rows are in `crosslink_fragment.yaml` for the lead to add to the existing staging files.

- **Hooker, Of the Laws of Ecclesiastical Polity, Books I–V** (`hooker_laws-of-ecclesiastical-polity-books-1-5_keble1850.txt`, vendored for VI.4). The Preface is addressed to the Puritans and answers the Cartwright line; Walton's Life names Cartwright. Role context, assigned. Tier: same time and place.
- **Barlow, The Summe and Substance of the Hampton Court Conference, 1604** (`barlow-william_summe-and-substance-hampton-court-conference_1804.txt`, VI.4). The only official record of the Puritan ministers' hearing before James I, by a hostile dean. Context, assigned. Same time and place.
- **The Book of Common Prayer, 1559** (`church-of-england_liturgical-services-elizabeth-1559_clay1847.txt`, VI.4). The book the Admonition's View of Popish Abuses attacks clause by clause. Context, provisional. Same time and place.
- **Visitation Articles and Injunctions, Vol. III, 1559–1575** (`church-of-england_visitation-articles-injunctions-v3-1559-1575_frere-kennedy1910.txt`, VI.4). Parker's Advertisements of 1566 and the surplice enforcement that produced the first 'puritans'. Context, provisional. Same time and place.
- **The Two Books of Homilies** (`church-of-england_two-books-of-homilies_griffiths1859.txt`, VI.4). The Certaine Articles defend the charge that reading homilies is 'as evill as playing on a stage'. Context, provisional.
- **Foxe, Acts and Monuments, Vol. VIII** (`foxe_acts-and-monuments-v8_cattley-townsend1837.txt`, VI.4). Lady Hoby's diary records the Book of Martyrs read aloud to her household (file line 9984). Context, provisional; the antecedent question is in section 5. Same time and place.
- **Beza, Job Expounded, 1589** (`beza_job-expounded_legatt1589.txt`, Reformed cities). Beza in English from the same Cambridge printer who issued Perkins in 1600. Context, provisional. Same time and place.

Checked and not linked (named, never opened for this purpose): Calvin's Letters, Vol. IV (`calvin_letters-vol4_bonnet1858.txt`) has letters to Knox and Cecil of 1559–61, which belong to the Scottish and English settlements rather than to the Puritan movement; the Frankfort letters of 1555 to the English exiles are in Vol. III, which is not vendored. Wesley's Journal, Vol. I, names Perkins and the Puritans twice, and Asbury's Journal names Baxter, Shepard and Perkins as reading; these are the Methodist Revival's own reception of Puritan devotional books (section 5), not rows for this world. McGlothlin's Baptist Confessions names Perkins once; out of scope. The Martyrs' Mirror mentions the Puritans in passing; out of scope.

## 3. Verified acquisition leads

Each lead below was opened on archive.org (metadata API) on 2026-10-16; where the OCR was downloaded, it was sampled at five points.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Chronicles of the First Planters of the Colony of Massachusetts Bay, 1623–1636 | Alexander Young (compiler): Higginson, Dudley, Clap, Cotton, Mather, Shepard and others | — | 1846 | `archive.org/details/chroniclesoffirs00younuoft` | pd-us-by-date; NOT_IN_COPYRIGHT on the item | metadata and OCR read, contents list verified (24 documents), 2026-10-16. The strongest unvendored lead for the New England half. |
| Winthrop's Journal, Vol. II (1641–49) | John Winthrop | J. K. Hosmer (ed.) | 1908 | `archive.org/details/winthropsjournal02wint` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata read, 2026-10-16 |
| Historical Notices, Vol. II | Nehemiah Wallington | R. Webb (ed.) | 1869 | `archive.org/details/historicalnotice02walluoft` | pd-us-by-date; NOT_IN_COPYRIGHT | OCR downloaded and sampled, 2026-10-16; mostly copied news from 1642 |
| The Works of Anne Bradstreet in Prose and Verse | Anne Bradstreet | J. H. Ellis (ed.) | 1867 | `archive.org/details/worksofannebrads00brad` | pd-us-by-date; NOT_IN_COPYRIGHT | OCR downloaded and sampled, 2026-10-16; the reprinted 1678 text carries long-s misreads, the editorial matter is clean |
| The Cambridge Platform (1648) with the 1680 Confession | Cambridge Synod; Boston Synod | — | 1850 | `archive.org/details/cambridgeplatfor00cong` | pd-us-by-date; NOT_IN_COPYRIGHT | OCR downloaded and sampled, clean, 2026-10-16 |
| The Marprelate Tracts, 1588, 1589 | Martin Marprelate (pseud.) | William Pierce (ed.) | 1911 | `archive.org/details/marprelatetracts0000will` | pd-us-by-date (1911 London); no rights field on the item | OCR downloaded and sampled, 2026-10-16; text pages readable, several blank versos OCR'd as mirrored garbage |
| Reliquiae Baxterianae | Richard Baxter | Matthew Sylvester (ed.) | 1696 | `archive.org/details/reliquiaebaxteri00baxt` | pd-us-by-date; NOT_IN_COPYRIGHT | OCR downloaded and sampled, 2026-10-16; long-s misreads throughout (second-witness quality). Window straddles this world and English Old Dissent. |
| The Complete Works of Richard Sibbes, Vols. II–VII | Richard Sibbes | A. B. Grosart (ed.) | 1862–64 | `archive.org/details/completeworksofr02sibb` and sister items | pd-us-by-date; NOT_IN_COPYRIGHT in the search listing | search listing only, 2026-10-16 |
| The Works of Thomas Shepard, 3 vols. (Sincere Convert, Sound Believer, Parable of the Ten Virgins) | Thomas Shepard | J. A. Albro (ed.) | 1853 | `archive.org/details/worksofthomasshe01shep` | pd-us-by-date (Boston 1853); no rights field seen | search listing only, 2026-10-16 |
| The Autobiography of Thomas Shepard, duplicate scans | Thomas Shepard | N. Adams (ed.) | 1832 | `autobiographyoft00shep2`, `autobiographyth00adamgoog` | pd-us-by-date; NOT_IN_COPYRIGHT | search listing, 2026-10-16; same edition as the vendored copy |
| History of Plymouth Plantation, 1620–1647 | William Bradford | W. C. Ford (ed.) | 1912 | `archive.org/details/historyofplymout02brad` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata read, 2026-10-16; Separatist context, not this world's voice |
| The Workes of William Perkins, Vol. 1 (1626 folio) | William Perkins | — | 1626 | `archive.org/details/WilliamPerkinsWorksVol1` | Creative Commons public domain mark on the item (uploader DigitalPuritan) | metadata read, 2026-10-16; OCR not sampled, expected to be of the same garbled kind as the 1600 volume |
| John Cotton's treatises (The Way of the Churches of Christ in New-England 1645, The Keyes of the Kingdom 1644, Singing of Psalmes 1647, and others) | John Cotton | — | 1640s | `archive.org/details/vvayofchurchesof00cott` and sister items | pd-us-by-date; no rights field seen | search listing only, 2026-10-16; early prints, OCR unknown |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Lewis Bayly, The Practice of Pietie (1623, 14th ed.), `bim_early-english-books-1475-1640_the-practice-of-pietie-_bayly-lewis-bp-of-ban_1623` | Census-named devotional best-seller | Only EEBO microfilm items exist on archive.org (1623, 1632, 1635, 1642 and later). The 1623 OCR was downloaded (after two server errors) and is garbled at every sample point, with the long s kept as U+017F and column fragments interleaved. Not a quoting text. A later clean printing (18th century or Victorian) was not found in the search; look again for one before a build needs Bayly. |
| Dod and Cleaver, A Godlie Forme of Householde Government | Census-named | Only EEBO microfilm items (`bim_..._cleaver-robert_1598`, `_1600`, `_1614`); given the Bayly result the OCR is expected unusable. Not downloaded. Lead kept in the seed file with that caveat. |
| Perkins, A Golden Chaine, EEBO microfilm items 1591–1631 | Alternative scans of the same work | All `bim_early-english-books` microfilm items; the Princeton 1600 scan (vendored) is the better of a poor set. |
| Knappen, Two Elizabethan Puritan Diaries, items `twoelizabethanpu0000knap` and `twoelizabethanpu0000rich` | Same edition | Lending-restricted (`inlibrary`, `printdisabled`); the unrestricted Princeton copy was used instead. |
| Lady Hoby, The Private Life of an Elizabethan Lady, ed. Joanna Moody (1998), `privatelifeofeli0000hoby` | Modern edition of the same diary | 1998, in copyright, lending-restricted. |
| Shepard, God's Plot, ed. Michael McGiffert (1972), `godsplotparadoxe0000shep` | The census's own named edition of the autobiography and journal | In copyright, lending-restricted. The 1832 Adams edition carries the same autobiography text. |
| Shepard's Cambridge congregation's conversion relations (The Confessions, ed. Selement and Woolley, 1981; McGiffert's 1972 selection) | Census-named lay conversion narratives 'as delivered for church admission' | Both editions are in copyright (1972, 1981); the manuscript relations were first printed in them, so no public-domain text of the lay confessions exists. This is the one census-named source with no public-domain path. |
| Winthrop's Journal, Google scans `winthropsjourna00hosmgoog` to `06hosmgoog` | NOT_IN_COPYRIGHT copies of the Hosmer edition | None carries a volume field; the copy opened (`winthropsjourna01hosmgoog`) turned out to be Vol. II, not Vol. I. The BLC scan `winthropsjournal01wint` is Vol. I and was vendored. |
| Westminster standards: 1658 Humble Advice (`humbleadviceofas1658west`), 1675 Glasgow (`confessionoffait1675west`), 1860 Nelson (`confessionoffait00westuoft`), Macpherson 1881 (`westminsterconfe01macp`, `westminsterconf00unknuoft`, `peopleseditionof00macp`) | All public domain | OCR sampled on each: the 17th-century printings carry long-s misreads, the 1860 OCR is rougher than the 1877, and Macpherson's handbooks set the confession in italics the OCR mangles. Superseded by the 1877 Nelson printing. |
| Dedham classis, Google scan `presbyterianmov00pregoog` | NOT_IN_COPYRIGHT | Poorer OCR than the Robarts scan of the same edition; superseded. |
| Puritan Manifestoes, 1954 and 1972 reprints (`bwb_T5-AGA-708`, `puritanmanifesto0000frer`) | Same text | Lending-restricted; the 1907 original was used. |
| Thomas Cartwright's own works | Census names Cartwright | Only Latin commentaries (1632, 1647) and EEBO microfilm items of the Confutation of the Rhemists (1618) appear on archive.org; no English edition of his Replies to Whitgift was found. His position is represented through the Second Admonition, Hooker's Preface and Bancroft's narrative. |
| Baxter, The Saints' Everlasting Rest, 19th-century printings (`saintseverlastin1838baxt` and others) | Clean public-domain OCR | They are the Fawcett abridgement (1758), not Baxter's text; the 1650s originals exist only as EEBO microfilm items. Baxter is in any case a boundary case for this world (section 5). |
| Samuel Ward's diary in a separate edition | Census-named | Exists only in Knappen 1933 (vendored). |
| Nehemiah Wallington's other notebooks (Seaver's 1985 study; the Folger and British Library manuscripts) | More of the same voice | Not printed in any public-domain edition; Webb 1869 is the only one. |

## 5. Open cross-world questions

- **Boundary with the English Reformation and Elizabethan Settlement (VI.4).** Perkins, Sibbes, Rogers, Hoby and Ward all lived and died inside the Church of England. The staging files place them as this world's `tradition` and give VI.4 `context` rows for Hoby and Perkins. Whether the moderate conforming Puritans should also be `tradition` for VI.4 is for the lead and Mark, not decided here.
- **Westminster and the Scottish Kirk (VI.5).** The Confession and Catechisms are assigned `tradition` to both worlds, and the Scottish-only parts of the 1877 printing (Sum of Saving Knowledge, National Covenant) to VI.5 only. If a VI.5 agent vendors its own printing of the standards, the two files become two Expressions of one Work and need a WORKS.yaml entry.
- **Foxe as antecedent.** Hoby's diary shows the Book of Martyrs read in a godly household. Under the README's 'argues from' rule that is use, not argument; the cross-link row is `context`, provisional, and the antecedent question is left open.
- **Baxter and English Old Dissent (VIII).** Reliquiae Baxterianae (1696) covers 1615 to the 1680s. It is a lead here, not vendored; which world owns Baxter's voice is a portfolio question.
- **The Methodist Revival (VIII) as reader of Puritan books.** Wesley's Journal names Perkins; Asbury's names Baxter, Shepard and Perkins; Wesley's Christian Library abridged Sibbes and others. These are reception facts for the Methodist world's own Doc_02, recorded here so they are not lost; no rows were written.
- **The Baptists (VIII) and the Separatists.** Bradford's Plymouth history and Cotton's church-way treatises sit on the line between this world and the Separatist and Baptist entries; left as leads.

## 6. Step 0 scope notes and recommendation

Floor (A1). The census floorNote is 'No question'. Nothing found this pass raises one: every vendored source is Trinitarian and Chalcedonian, and the Westminster Confession states both in its own words.

Sourcing (B1). Rich, and now in hand. Eleven public-domain files cover the four primary genres the census names: diaries (Hoby, Rogers, Ward, Wallington), a conversion narrative (Shepard), practical divinity (Perkins, Rogers, Sibbes), and the church-order record (the Admonitions, the Dedham minutes, Westminster), with Winthrop for New England. Nine files are clean; two are second witnesses. The one census-named source with no public-domain path is the lay conversion relations of Shepard's congregation.

Ecology (B2). Unusually balanced for this era: women's and artisans' voices beside the divines, a hostile witness (Bancroft, and the VI.4 cross-links to Hooker and Hampton Court), and the movement's own minutes. Author gravity is spread, not concentrated in one figure.

Uniqueness (B3). The overlap with VI.4 is real but legible: the same establishment documents serve VI.4 as `tradition` and this world as `context`, and the Puritan diaries and manifestoes have no counterpart in VI.4. The Westminster standards are shared with VI.5 by design.

Audiences (B4). The evangelical and Reformed descendants of this world are among the project's largest likely audiences; the diary genre is also the most direct bridge to a participant's own practice of self-examination.

Scale (B5). The window is a century and two continents, but the vendored set is about 15 MB and the leads are few and specific; a build can start from what is here.

**Recommendation: build.** The floor is clear, the native genre is vendored in clean public-domain editions, and the cross-world boundaries are named rather than tangled. This is a recommendation for Mark, not a decision; the VI.4 boundary question in section 5 is the one item that needs his ruling before Doc_01.
