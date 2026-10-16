# Source Readiness Dossier — The Huguenots

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.6
**Corpus-map slug:** `the-huguenots`
**Time window:** 1559–1685
**Region(s):** France (census region tag: Mediterranean)
**Dossier author / date:** Era VII library/source-research session, Huguenots world agent, 2026-10-16
**Corpus-map / `cic/texts/` state as of:** 2026-10-16, branch `library/era-vii-2026-10`, after this pass vendored ten files and wrote ten staging files. No `cic/corpus-map/the-huguenots.yaml` bucket existed before this pass; the staging files below are not yet merged (the lead merges).

## 1. Already assigned

Before this pass: nothing. No bucket, no staging row, no seed row and no registry note named this world.

After this pass, ten files are vendored in `cic/texts/` and staged in `cic/corpus-map/_staging/`, all for this world, pending merge:

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Synodicon in Gallia Reformata: the Confession of Faith (1559), the Discipline, and the acts of the national synods Paris 1559 to Loudun 1659, English (Quick 1692) | french-reformed-synods; quick (his own history, context) | tradition (context for Quick's history) | assigned | 4.1 MB, about 100,000 OCR lines, two volumes | `quick_synodicon-in-gallia-reformata_1692.txt` |
| The French Confession of Faith, 1559, French and English (Schaff 1877, extract) | french-reformed-synods | tradition | assigned | 86 KB | `schaff_gallican-confession-fra-eng_1877.txt` |
| Histoire des martyrs, Tome 3, Livres VIII–XII (Benoît/Lelièvre 1889), French | crespin | tradition | assigned | 5.3 MB, about 150,000 OCR lines | `crespin_histoire-des-martyrs-t3-fra_benoit-lelievre1889.txt` |
| Histoire ecclésiastique des églises réformées, Tome 1, Livres I–IV (Baum/Cunitz 1883), French | beza | tradition | assigned | 3.0 MB | `beza_histoire-ecclesiastique-t1-fra_baum-cunitz1883.txt` |
| Mémoires de Madame de Mornay, Tome 1 (de Witt 1868), French | mornay-charlotte | tradition | assigned | 800 KB | `mornay-charlotte_memoires-de-madame-de-mornay-t1-fra_de-witt1868.txt` |
| A Huguenot Family in the XVI Century (Crump 1926), English of the above | mornay-charlotte | tradition | assigned | 770 KB | `mornay-charlotte_huguenot-family-in-the-xvi-century_crump1926.txt` |
| Journal de Jean Migault (Weiss/Clouzot 1910), French | migault | tradition | assigned | 390 KB | `migault_journal-fra_weiss-clouzot1910.txt` |
| Jean Migault; or, The Trials of a French Protestant Family (Anderson 1852), English | migault | tradition | assigned | 180 KB | `migault_trials-of-a-french-protestant-family_anderson1852.txt` |
| Les Tragiques (Lalanne 1857), French | aubigne | tradition | assigned | 875 KB | `aubigne_les-tragiques-fra_lalanne1857.txt` |
| Memoirs of a Huguenot Family: James Fontaine's autobiography; the Edict of Nantes and the Edict of Revocation in English (Maury 1853) | fontaine-james; henry-iv-france and louis-xiv-france (the edicts, context) | tradition (context for the edicts) | assigned | 1.1 MB | `fontaine-james_memoirs-of-a-huguenot-family_maury1853.txt` |

Witness status, stated plainly per INTAKE §9. Primary and quotable once checked against the page image: the Schaff extract (French primary, English cross-check), both Mornay files (French primary), both Migault files (French primary; the English rests on an older printed text), Les Tragiques, Fontaine. Primary but letter-noisy: Quick (long s normalised, 91,894 occurrences; other misreads remain; the title page is unreadable). Second witness for exact wording: Crespin tome 3 and Bèze tome 1, because the OCR reads the reprinted old typography's long s as f throughout; both are readable and both are the only public-domain witnesses on a reachable host.

Each staging file also places the work in every other census world it serves (section 5 lists the placements that need a ruling): the Reformed Cities (VI.2) as context for the Confession, Crespin and Bèze; the Waldensian union (VI.10) as context for Crespin's Calabrian notices; the Church of the Desert (`church-of-the-desert-huguenots`, 1685–1787) as tradition, provisional, for the Confession, the Discipline, Migault, Fontaine, and as context for the Revocation and Quick's history.

## 2. Cross-link opportunities

Checked by grepping the `Title:`/`Creator:` lines of every vendored `.txt` and the `<DC.Title>` lines of the `.xml` files for Huguenot, Calvin, Geneva, Bèze, Coligny, Nantes, Navarre, Mornay, France and French, then opening each plausible hit.

- **Marot–Bèze Psalter, 1562** (`marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt`, assigned to the Reformed Cities VI.2 only). The census names the Psalter as this world's own primary practice. The vendored file is the complete 1562 Geneva printing "avec privilege du Roy". Tier: same time-place, named by the census, never opened for this world. Proposed row (tradition, assigned) in `crosslink_fragment.yaml`.
- **Calvin, Letters, Vol. IV (Bonnet 1858)** (`calvin_letters-vol4_bonnet1858.txt`, VI.2 only). Its own contents list names letters to the Prisoners of Paris, the Church of Paris, the King and Queen of Navarre and the Admiral de Coligny, 1559–1564. Tier: same time-place. Proposed row with `confidence: needs-ruling` on role (section 5).
- **Calvin, Letters, Vol. II** (`calvin_letters-vol2_bonnet1858.txt`). Letters "To the Faithful of France" (1547) and "To the Prisoners of Lyons" (1552–53, the martyrs Crespin records). Before the window; recorded here as named-never-opened for this world, no row proposed. A Doc_02 that treats the pre-1559 martyr churches as this world's prehistory may want it.
- **Bèze, Job Expounded (1589)** (`beza_job-expounded_legatt1589.txt`, VI.2). Bèze moderated the Synod of La Rochelle 1571 (Quick's own text, near line 5339), but this work is a Latin Job commentary in English with four mentions of France. Tier: same time-different-region. No row proposed.
- **Calvin, Geneva Catechism (Waterman 1815) and the Ordonnances ecclésiastiques (1576 revision, 1735 printing)** (VI.2). The Discipline of the French churches (in Quick) is their French cousin; neither file was opened for this world. Tier: named-never-opened. No row proposed; a Doc_02 comparing the Discipline with Geneva's order should read both.
- **Schaff, Second Helvetic Confession and Heidelberg Catechism (1919 extract)**. Does not contain the Gallican Confession (checked: the 1919 extract holds §55 and §69 only). Closed as a cross-link; the Confession was vendored separately from the 1877 printing.
- **van Braght, Martyrs' Mirror (Sohm 1886)** (VI.3). 258 hits on France/French/Paris, but these are Anabaptist martyrs; not this world. No row.
- Nothing else in the corpus (patristic, medieval, Jesuit, Orthodox, Methodist) touches this window and region.

## 3. Verified acquisition leads

All ten vendored items were verified on the host and are listed in section 1 with their identifiers; the seed rows in `seed_fragment.yaml` give the URL, the rights basis and the check. Verified on the host and NOT vendored this pass (reason in the right-hand column; every one is also a seed row with `status: not-yet-downloaded`):

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Histoire ecclésiastique, Tomes 2 and 3 | attr. Bèze; Baum, Cunitz, Reuss | none | 1883–89 | archive.org `histoireecclsi02bz`, `histoireecclsi03bz` | pd-us-by-date (no host status field) | metadata fetched, djvu.txt downloaded and sampled, 2026-10-16. Not vendored to hold the file count; tome 1 carries the 1559 synod. Same f-for-long-s OCR. |
| Histoire des martyrs, Tomes 1 and 2 | Crespin; Benoît, Lelièvre | none | 1885–87 | archive.org `histoiredesmarty01cres`, `histoiredesmarty02cres` (Google scans `histoiredesmart00benogoog`, `01benogoog` are worse) | pd-us-by-date | metadata fetched, djvu.txt downloaded, year-counted, 2026-10-16. Pre-1559 content; tome 1 holds the Mérindol/Cabrières material (VI.10). |
| Mémoires de Madame de Mornay, Tome 2 (letters, Notice) | Charlotte and Philippe de Mornay; de Witt | none | 1869 | archive.org `mmoiresdemadam02mornuoft` | pd-us-by-date, NOT_IN_COPYRIGHT | metadata fetched, title page read, 2026-10-16. Correspondence, left for a build thread to call for. |
| Tous les synodes nationaux des Églises réformées de France, 2 vols (the French acts and Discipline behind Quick) | Aymon (ed.) | none | 1710 | archive.org `touslessynodesna01gl`, `touslessynodesna02gl` | pd-us-by-date (no host status field) | metadata fetched, vol. 1 downloaded and sampled (readable, long s read as f), 2026-10-16. Not vendored: Quick carries the acts in English. |
| An edict of the French king ... (the Revocation in English, with the letter to the Elector of Brandenburg) | Louis XIV; anonymous | anonymous | 1686 | archive.org `edictoffrenchkin00unknuoft` | pd-us-by-date, NOT_IN_COPYRIGHT | metadata fetched, downloaded and sampled, 2026-10-16. OCR reads f for long s throughout; the clean 1853 rendering in the Fontaine file was vendored instead. |
| The history of the famous Edict of Nantes, 2 vols | Élie Benoist | anonymous | 1694 (London: John Dutton) | archive.org `historyoffamouse01beno`, `historyoffamouse02beno` | pd-us-by-date (no host status field) | metadata fetched for both, 2026-10-16; OCR not sampled. A refugee's narrative history, not the movement's own acts. |
| Cruel persecutions of the Protestants in the kingdom of France (reprint of an early English translation of Jean Claude's account) | Jean Claude; Narcisse Cyr (ed.) | anonymous, seventeenth-century | 1893 (Boston) | archive.org `cruelpersecution00clau` | pd-us-by-date; Library of Congress "unaware of any copyright restrictions" | metadata fetched, downloaded and sampled, 2026-10-16. Which English edition it reprints was not established. |
| The memoirs of a Protestant, condemned to the galleys of France | Jean Marteilhe | Oliver Goldsmith (1758) | 1895 reprint | archive.org `memoirsaprotest01martgoog` | pd-us-by-date, NOT_IN_COPYRIGHT | metadata fetched, 2026-10-16; OCR not sampled. Outside this window (1700–1713); belongs to the Church of the Desert. |
| A compendious history of the Reformation in France, 6 vols | Étienne Abel Laval | none | 1737–41 | archive.org `compendioushisto01lava` and siblings | pd-us-by-date (no host status field) | metadata fetched, 2026-10-16. An English narrative drawn from Bèze; not a translation; context only. |
| Histoire universelle, 10 vols (Société de l'histoire de France) | d'Aubigné; de Ruble, de Vaissière, Plattard | none | 1886– | archive.org `histoireunivers01aubi` and siblings | pd-us-by-date for the 1886–1909 volumes; the host notes a 1925 Plattard volume in the set, so each later volume must be date-checked | metadata fetched for vol. 1, 2026-10-16. Too large for this pass. |
| Mémoires et correspondance de Duplessis-Mornay, 12 vols | Philippe de Mornay | none | 1824–25 | archive.org `mmoiresetcorresp01morn` and siblings | pd-us-by-date (no host status field) | metadata fetched for t. 1, 2026-10-16. A build thread should name the volume it needs. |
| Du Plessis-Mornay in Elizabethan English: A treatise of the Church (1579, 1581), A worke concerning the trewnesse of Christian religion (1597), A discourse of life and death (1608), The mysterie of iniquitie (1612) | Philippe de Mornay | early English translators | 1579–1612 | archive.org `bim_early-english-books-1475-1640_a-treatise-of-the-church_mornay-philippe-de_1579` and the sibling bim items listed in the seed row | pd-us-by-date (microfilm collection, no status field) | metadata fetched for the 1579 item, 2026-10-16; OCR not sampled. The Quick item from the same microfilm series was letter-noisy. |
| The ecclesiasticall discipline of the Reformed churches in France | Reformed Churches of France | anonymous | 1662 | archive.org `bim_early-english-books-1641-1700_the-ecclesiasticall-disc_1662` | pd-us-by-date (microfilm collection) | metadata fetched, 2026-10-16; OCR not sampled. Quick already carries the Discipline. |
| Les Tragiques, from the author's manuscript | d'Aubigné; Charles Read (ed.) | none | 1872 | archive.org `lestragiquespubl00aubiuoft` | pd-us-by-date, NOT_IN_COPYRIGHT | downloaded and sampled, 2026-10-16. A second French witness; Lalanne 1857 vendored instead. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Public-domain English translation of Crespin's Histoire des martyrs | The census names Crespin as primary | archive.org search on title (martyrs AND France/French, 1550–1930, texts) returns Foxe editions, Mears's 1864 *Martyrs of France* (a nineteenth-century retelling), and a 1693 Dunton proposal to print a "French book of martyrs" (a prospectus, not the book). No translation exists on a reachable host. The census already says "available in full only in French". |
| Public-domain English translation of Bèze's Histoire ecclésiastique | The founding narrative | archive.org search on "reformed churches" AND "France", 1550–1930, English: only Laval's 1737 *Compendious History* (a derivative narrative, section 3) and seventeenth-century pamphlets. No translation exists. |
| Public-domain English translation of Les Tragiques | The Huguenot epic | archive.org creator search (Aubigné, English) returns only Merle d'Aubigné (a different author, nineteenth century), the 1679 and 1686 English of the *Confession de Sancy* (a satire, not Les Tragiques), and Françoise d'Aubigné's letters. No translation exists on a reachable host. |
| d'Aubigné, *Sa vie à ses enfants* in English | A first-person Huguenot life | Only hit is archive.org `saviesesenfants0000agri`, dated 1986, in copyright. Not checked for an older French printing this pass; the French is in the Mémoires editions, not searched. |
| Quick's Synodicon in a second, cleaner scan | The vendored scan is letter-noisy | archive.org title search returns one item only (the microfilm digitisation). EEBO/TCP at umich is blocked. Closed until another host is reachable. |
| Crump 1926 copyright | A 1926 British imprint | 1926 is inside the rolling 95-year rule as of 2026 (term ended 2021); the registry's pre-1931 rule applies regardless of place of publication. A 1947 Indian reprint (`dli.ministry.02967`) exists and was ignored. Cleared, not closed. |
| Migault, French 1910 second scan `journaldejeanmig00miga` | Same edition, University of Ottawa | Duplicate of the vendored Toronto scan; not needed. |
| Mornay, Google scans `mmoiresdemadame00goog`, `01goog` | Same edition as the vendored tome 1 | Sampled: Google boilerplate, accent and italic misreads; the Toronto scans are cleaner. `00goog` is tome 1 and `01goog` tome 2, not as their numbering suggests. |
| Schaff, Creeds of Christendom vol. III, 1919 printing (`creedschristend07schagoog`, `TheCreedsOfChristendomV3`) | A later printing of the vendored volume | The 1877 Princeton scan was chosen for its explicit copyright notice and NOT_IN_COPYRIGHT tag; the 1919 printings carry the same text. |
| Edict of Nantes, French text | The brief asked for the Edict in English; the French would sit beside it | archive.org holds many copies of *Edict du Roy sur la pacification des troubles de ce Royaume* dated 1644 (Google-derived `bub_gb_` items, no status field, OCR not sampled). Not vendored: the English in Fontaine serves the build; a French witness is a one-line search away. |
| Jurieu, Pastoral Letters (English, 1688–1699) | The refuge's voice to the churches under the cross | Microfilm bim items only, OCR unsampled, and the letters begin in 1686, outside this window. Recorded for the Church of the Desert. |
| Fontaine, *A tale of the Huguenots* (1838) | Earlier printing of the vendored memoir | Superseded by the 1853 edition, which the compiler enlarged and which adds the edicts. |
| Huguenot sources on blocked hosts (ccel.org, gallica, EEBO at umich) | Gallica holds the sixteenth-century printings of the Confession and Discipline | Blocked in this sandbox; nothing was looked for there. |

## 5. Open cross-world questions

- **Calvin's letters to the French churches (vol. IV, 1559–1564): what role?** The corpus-map README defines `context` as the outside view (critic, civil historian, opponent) and `antecedent` as a text the entry's own vendored sources demonstrably argue from. Calvin writing into Paris, Navarre and Coligny's circle is neither an opponent nor, yet, demonstrably argued from. Proposed `context`, `needs-ruling`. Whoever rules should also decide whether vol. II's 1547 and 1552–53 letters count as this world's prehistory.
- **The Reformed Cities (VI.2) vs the Huguenots (VI.6): where does Geneva's voice stop?** The Psalter, the Confession (drafted on Calvin's model), Crespin (a Genevan printer) and Bèze's Histoire (compiled in Geneva) all belong to both. This pass placed them as `tradition` here and `context` in VI.2 where VI.2 did not already hold them as `tradition`; the Psalter is `tradition` in both. The built VI.2 world should be told its Psalter and Bèze now serve a second world.
- **The Church of the Desert (`church-of-the-desert-huguenots`, 1685–1787): the same church after 1685.** The Confession and Discipline, Migault and Fontaine run across the 1685 line. Placed there as `tradition`, `provisional`. When that world gets its own dossier, the 1686 Revocation printing, Jurieu's Pastoral Letters, Marteilhe's galley memoir and the *Synodes du Désert* (archive.org `lessynodesduds01egli`–`03egli`, 1885, found in the Aymon search, not fetched) are its starting leads.
- **The Waldensian union (VI.10):** Crespin tome 3's Calabrian notices (1560–61) are placed as `context`, `provisional`; tome 1 (not vendored) holds Mérindol and Cabrières (1545). That world's own pass should decide whether a Genevan martyrologist is context or custody of its own martyrs' letters.
- **The Dutch refuge (VI.9, c. 1570–1650):** Migault's family reached Holland in 1688 and Crespin tome 3 carries the Netherlands martyrs of the 1560s with Guy de Brès as a named collaborator (the editors' notice). Neither falls inside VI.9's window; no rows proposed; named here so VI.9's pass sees them.
- **Author slug for the Histoire ecclésiastique.** The 1580 edition is anonymous; the file is slugged `beza` on the editors' and catalogue's attribution, to match the existing `beza` file. If the project prefers a corporate slug for an anonymous compilation, the staging file changes, not the vendored file.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "No question". The vendored Confession confirms it from the world's own text: article VI ("in this one sole and simple divine essence ... there are three persons: the Father, the Son, and the Holy Spirit") and article XIV ("Jesus Christ, being the wisdom of God and his eternal Son, has put on our flesh, so as to be God and man in one person"), read in `schaff_gallican-confession-fra-eng_1877.txt` at lines 672 and 1133.

**Sourcing (B1).** Strong and now in hand: the national church's complete self-governing record in English (Quick), its confession in French and English, its own founding narrative and martyrology in French, a woman's memoir and a schoolmaster's refugee journal each in French with public-domain English beside it, the Huguenot epic, and the two edicts that open and close the window. The thin spot is the French of the synod acts (Aymon 1710, a verified lead) and Du Plessis-Mornay's own theology (early English printings exist only as unsampled microfilm OCR). Two of the ten files are second witnesses for exact wording because of the OCR, not because of the edition.

**Ecology (B2).** Unusually balanced for this era: institutional (synods, Discipline), confessional, martyrological, personal and literary voices, male and female, noble and schoolmaster, across the whole 1559–1685 span. The risk is the reverse of thinness: Calvin and Geneva can swallow the French churches' own voice if a build quotes the Institutes where it should quote a synod or a consistory. The corpus map's placements guard that line.

**Uniqueness (B3).** Distinct from VI.2 (Geneva is the parent; this is the daughter church under a hostile crown, organised before any king allowed it) and from the Church of the Desert (the same body, after the Revocation, without legal existence). The 1685 boundary is clean in the sources: Migault and Fontaine straddle it, the synod acts end in 1659, Quick's history ends at 1685.

**Audiences (B4).** The "refugee" story and the persecuted-minority-with-a-constitution story both carry; the Psalter sung in secret and at the stake is the ordinary act the census already names.

**Scale (B5).** About 16.6 MB vendored (two large French volumes dominate); comparable to the Anabaptist and Tridentine worlds in bulk and wider in genre. A build would not run short of primary text.

**Recommendation: build.** The movement's own voice is now in the library in every register the census asked for, with the rights settled and the OCR caveats written down; the open questions in section 5 are placement questions, not sourcing gaps. This is a recommendation for Mark, not a decision.
