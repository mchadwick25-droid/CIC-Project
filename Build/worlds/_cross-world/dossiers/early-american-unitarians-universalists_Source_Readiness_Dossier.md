# Source Readiness Dossier — Early American Unitarians & Universalists

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.27
**Corpus-map slug:** `early-american-unitarians-universalists`
**Time window:** 1770-1815
**Region(s):** New England, the mid-Atlantic, and London; census `regions`: North America, North Europe
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

21 works across 20 vendored files in `cic/corpus-map/early-american-unitarians-universalists.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| A Treatise on Atonement (1805) | ballou-hosea | tradition | assigned | whole work | `ballou-hosea_treatise-on-atonement_1805.txt` |
| American Unitarianism (1815) | belsham | tradition | assigned | Belsham's chapter and the letters of Freeman and Wells | `belsham_american-unitarianism-brief-history_1815.txt` |
| A Sermon delivered at the Ordination of the Rev. Jared Sparks (1819) | channing | transmission | assigned | whole work | `channing_sermon-at-the-ordination-of-jared-sparks-baltimore_1819.txt` |
| Divine Glory brought to View in the Final Salvation of All Men (1783) | chauncy | tradition | provisional | whole work | `chauncy_divine-glory-brought-to-view-in-the-final-salvation-of-all-men_1783.txt` |
| The Mystery hid from Ages and Generations (1784) | chauncy | tradition | assigned | whole work | `chauncy_mystery-hid-from-ages-and-generations_1784.txt` |
| The Salvation of All Men strictly examined (1790) | edwards-jonathan-jr | context | assigned | whole work | `edwards-jonathan-jr_salvation-of-all-men-strictly-examined_1790.txt` |
| Sermons on Particular Occasions (1814) | freeman-james | tradition | provisional | whole work | `freeman-james_sermons-on-particular-occasions_1814.txt` |
| Natural Religion, as distinguish'd from Revealed (1759) | gay-ebenezer | antecedent | provisional | whole work | `gay-ebenezer_natural-religion-as-distinguished-from-revealed-dudleian-lecture_1759.txt` |
| A Liturgy ... for the use of the First Episcopal Church in Boston (1785) | kings-chapel | tradition | assigned | preface and liturgy; the Psalter as scripture | `kings-chapel_liturgy-collected-principally-from-the-book-of-common-prayer_1785.txt` |
| A Sermon preached at the Opening of the Chapel in Essex-House (1774) | lindsey | tradition | provisional | whole work | `lindsey_sermon-at-the-opening-of-the-chapel-in-essex-street_1774.txt` |
| Seven Sermons (1749) | mayhew | antecedent | provisional | whole work | `mayhew_seven-sermons_1749.txt` |
| Letters, and Sketches of Sermons, vol. I (1812) | murray-john | tradition | assigned | whole volume | `murray-john_letters-and-sketches-of-sermons-v1_1812.txt` |
| Letters, and Sketches of Sermons, vol. II (1812) | murray-john | tradition | assigned | whole volume | `murray-john_letters-and-sketches-of-sermons-v2_1812.txt` |
| Letters, and Sketches of Sermons, vol. III (1813) | murray-john | tradition | assigned | whole volume | `murray-john_letters-and-sketches-of-sermons-v3_1813.txt` |
| Records of the Life of the Rev. John Murray (1816) | murray-john | tradition | assigned | the autobiographical records | `murray-john_records-of-the-life-written-by-himself_1816.txt` |
| Discourses relating to the Evidences of Revealed Religion (Philadelphia, 1796) | priestley | tradition | assigned | whole work | `priestley_discourses-on-the-evidences-of-revealed-religion-philadelphia_1796.txt` |
| Letters to the Members of the New Jerusalem Church (1791) | priestley | tradition | provisional | whole work | `priestley_letters-to-the-members-of-the-new-jerusalem-church_1791.txt` |
| Hymns composed by different authors, by order of the General Convention of Universalists (1808) | universalist-church | tradition | assigned | preface and hymns | `universalist-church_hymns-composed-by-order-of-the-general-convention_1808.txt` |
| The Universalist Profession of Belief (Winchester, 1803), as printed in The Winchester Centennial (1903) | universalist-church | tradition | provisional | the three articles of the Profession at the head of the volume | `universalist-church_winchester-centennial-with-the-profession-of-belief_1903.txt` |
| The Winchester Centennial, 1803-1903 (1903) | universalist-church | transmission | assigned | the historical sketch, addresses and sermons | `universalist-church_winchester-centennial-with-the-profession-of-belief_1903.txt` |
| The Universal Restoration (1788) | winchester-elhanan | tradition | assigned | whole work | `winchester-elhanan_universal-restoration-in-dialogues_1788.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| chauncy_seasonable-thoughts-on-the-state-of-religion-in-new-england_1743.txt | whole work | Chauncy's anti-revival manifesto, the start of the Boston liberal line that ends in his Universalism | antecedent / provisional |
| asbury_journal-v3_1821.txt | about line 5543 ("at Jonathan Winchester's, brother to the famous Universalist") | a Methodist bishop's passing witness to Winchester's reputation | context / provisional, low value |
| asbury_journal-v1_1821.txt, asbury_journal-v2_1821.txt | about v1 line 19033 and v2 lines 4587, 6117, 12917 (Universalists among the sects he meets) | outside view of Universalist presence in the 1780s-1800s | context / provisional, low value |

Sibling spec in this batch: `priestley_letters-to-the-members-of-the-new-jerusalem-church_1791.txt` (in `specs/swedenborgian-new-church.yaml`) carries a provisional `tradition` row for this world.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Universalist's Hymn Book | Elhanan Winchester | none | 1794 | https://archive.org/details/universalistshym00winc | pd-us-by-date | metadata API, djvu 0.44 MB, OCR 0.66 (title leaf missing from the scan; imprint London 1794 per host), 23 October 2026 |
| Psalms, Hymns and Spiritual Songs, designed for the use of the Church Universal | First Universal Church in Boston (Murray's society) | none | 1792 per host; a dealer's slip in the scan says Boston 1802; imprint not legible | https://archive.org/details/psalmshymnsspiri00univ | pd-us-by-date | metadata API, djvu 0.37 MB, OCR 0.66, 23 October 2026 |
| The Benevolence of the Deity | Charles Chauncy | none | 1784 | https://archive.org/details/benevolenceofdei00chau | pd-us-by-date | metadata API, 23 October 2026 |
| Five Dissertations on the Scripture Account of the Fall | Charles Chauncy | none | 1785 | https://archive.org/details/fivedissertation00chau | pd-us-by-date | metadata API, 23 October 2026 |
| Two Sermons on the Nature, Extent and Perfection of the Divine Goodness | Jonathan Mayhew | none | 1763 | https://archive.org/details/twosermonsonnatu00mayh | pd-us-by-date | metadata API, 23 October 2026 |
| Christian Sobriety | Jonathan Mayhew | none | 1763 | https://archive.org/details/christiansobriet00mayh_0 | pd-us-by-date | search hit, 23 October 2026 |
| Review of American Unitarianism | Jedidiah Morse | none | 1815 | https://archive.org/details/reviewofamerican00mors | pd-us-by-date | metadata API, djvu 0.14 MB, 23 October 2026 |
| Remarks on the Rev. Dr. Worcester's Letter to Mr. Channing | William Ellery Channing | none | 1815 | https://archive.org/details/remarksonrevdrwo00chan | pd-us-by-date | metadata API, 23 October 2026 |
| A Letter to the Rev. William E. Channing | Samuel Worcester | none | 1815 | https://archive.org/details/lettertorevwilli00worc | pd-us-by-date | search hit, 23 October 2026 |
| Memoirs of Dr. Joseph Priestley, written by himself, with a continuation | Joseph Priestley and others | none | 1806 (Northumberland) | https://www.gutenberg.org/ebooks/75111 | public domain in the USA per Gutenberg | Gutenberg page and text head, 23 October 2026 |
| A Series of Letters in Defence of Divine Revelation | Hosea Ballou | none | 1820s edition | https://www.gutenberg.org/ebooks/8225 | public domain in the USA per Gutenberg | Gutenberg page and text head, 23 October 2026 |
| Union: or, a Treatise of the Consanguinity and Affinity between Christ and his Church | James Relly | none | 1759 | https://archive.org/details/bim_eighteenth-century_union-or-a-treatise-of_relly-james_1759 | pd-us-by-date | metadata API, djvu 0.03 MB (not downloaded), 23 October 2026 |
| The Life of Rev. John Murray (later edition) | John Murray | none | 1833 | https://archive.org/details/lifeofrevjohnmur00murr | pd-us-by-date | metadata API, 23 October 2026 |

Relly's Union is the book Murray learned his Universalism from. It is the clearest `antecedent` for the Murray strand, but the microfilm OCR was not measured.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Chauncy, Salvation for All Men (1782) | brief names it | only 1975 and 1977 reprints on the host, both access-restricted (lending only) |
| mysteryhidfromag0000chau and two others (1969 reprints) | Chauncy's Mystery | access-restricted reprints; the 1784 first edition is vendored |
| mysteryhidfromag00chau_0, bim_..._the-mystery-hid-from-age_chauncy-charles_1784 | 1784 Mystery | duplicate copies |
| Articles of Faith and Plan of Church Government (Philadelphia Universalist convention, 1790) | the Universalists' first confession and polity | microfilm OCR garbled (0.40) |
| Lindsey, The Apology on resigning the vicarage of Catterick (1782 edition) | Lindsey's own account of his break | microfilm OCR 0.57; a Google scan of the 1818 edition (apologytheophil00lindgoog) was not checked |
| The Universalist Register (host-dated 1803) | statistics | OCR garbled (0.23), and the host date looks wrong for a register series |
| recordsoflifeofr00murrrich, Murray Records 1827/1831 editions | Murray's life | duplicate or later |
| hymnscomposedbyd00univ (1810) | Universalist hymnal | second printing of the vendored 1808 |
| atreatiseonaton04ballgoog (1812), treatiseonatonema00ball (1811) and later | Ballou's Treatise | later editions; the 1805 first is vendored |
| universalrestora1831winc and later Winchester editions | cleaner OCR | later reprints; the 1788 first edition is vendored |
| winchestercenten00unse | centennial volume | duplicate |
| The Profession of Belief, 1803, in a contemporary printing | census source | not found |
| Records of Murray's Gloucester congregation from 1779 | census source | not found as a printed or OCR'd item |

## 5. Open cross-world questions

- Lindsey's Essex Street chapel (1774) and Priestley's English writings: do they belong to this world, to `english-old-dissent`, or both? Lindsey left the Church of England rather than coming out of Old Dissent. Rows are in the spec as provisional here and `needs-ruling` for english-old-dissent.
- The King's Chapel liturgy is a revised Book of Common Prayer from a colonial Church of England parish: should `restoration-georgian-church-of-england` take a transmission row? It is in the spec as provisional.
- Chauncy appears in two worlds: as the awakening's opponent (`the-evangelical-awakening-in-new-england`, Seasonable Thoughts already vendored) and as a Universalist here. Is one author file per world right, or should the Seasonable Thoughts take a row here too?
- Channing 1819 and Ballou 1805 both straddle this world and `american-unitarianism-universalism-consolidations`; where should the line fall?
- Winchester came from the Philadelphia Baptists; a `the-baptists` context row is in the spec as provisional.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build**, with the two threads kept distinct as the census asks. The Universalist thread has a strong own voice inside the window: Murray's autobiography and three volumes of his letters, Winchester's dialogues, Ballou's Treatise and the Convention's hymnal, with an orthodox reply for contrast. The Unitarian thread is thinner in America before 1815: the King's Chapel liturgy, one volume of Freeman's sermons, Belsham's pamphlet with the Boston letters, and Priestley's Philadelphia discourses. It leans on London (Lindsey) and on antecedents (Mayhew, Gay). The floor question can be argued from the world's own documents: the 1785 liturgy for the Unitarian thread, and for the Universalists both the 1803 Profession (in its 1903 reprint) and Ballou's denial of the Trinity, which shows the census's "may not touch the creed at all" needs care. The world is distinct from its 1819-1906 sibling, but its edges with English dissent and the New England awakening need rulings.

