# Source Readiness Dossier — The Methodist Revival

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.5
**Corpus-map slug:** `the-methodist-revival`
**Time window:** 1738–1815
**Region(s):** Britain, then America; census `region`: Britain, then America
**Dossier author / date:** first written by this world's own build thread (`meth`) from its Step 0 and Doc_02 research, 2026-10-02; refreshed and extended by Claude, Library thread, Era VIII source-research pass, 2026-10-23, at the project lead's direction that the two worlds with an existing Doc_02 (this one and the Old Believers) be brought to the same library standard as the rest of the era
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass. Before it the world had twelve works across seven vendored files (Curnock vol. I, Sermons vol. I, the Large Minutes, the 1780 Collection of Hymns, Asbury's Journal in three volumes); the Library pass added twenty-three files and two cross-link rows.

## 1. Already assigned

Forty-five works across thirty-two vendored files in `cic/corpus-map/the-methodist-revival.yaml`. The rows with author slugs `wesley-john`, `wesley-charles`, `asbury-francis`, `wesleyan-conference` and `curnock-nehemiah` are the meth build thread's, with per-row loci in `Build/worlds/meth/Source_Registry.md`; the rows with `wesley-j`, `wesley-c`, `whitefield` and the rest are the Library pass's.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Life, Experience, and Gospel Labors of the Rt. Rev. Richard Allen, written by himself | allen-richard | tradition | provisional | whole work | `allen-richard_life-experience-and-gospel-labors_1880.txt` |
| The Arminian Magazine, vol. I (1778): the lay narratives, letters and preachers' lives | arminian-magazine | tradition | assigned | the lives, letters and experience accounts in the twelve numbers | `arminian-magazine_vol-1_1778.txt` |
| The Arminian Magazine, vol. I (1778): the treatises on Universal Redemption | arminian-magazine | tradition | assigned | the treatise extracts opening each number | `arminian-magazine_vol-1_1778.txt` |
| The Works of James Arminius, Volume One (Nichols, revised, 1853) | arminius | antecedent | provisional | whole file | `arminius_works-v1_nichols1853.txt` |
| The Journal of the Rev. Francis Asbury, Vol. I (1771-1786) | asbury-francis | tradition | provisional | whole volume | `asbury_journal-v1_1821.txt` |
| The Journal of the Rev. Francis Asbury, Vol. II (1786-1800) | asbury-francis | tradition | provisional | whole volume | `asbury_journal-v2_1821.txt` |
| The Journal of the Rev. Francis Asbury, Vol. III (1800-1815) | asbury-francis | tradition | provisional | whole volume | `asbury_journal-v3_1821.txt` |
| Gnomon of the New Testament, vol. I (Matthew-Mark), English 1857 | bengel | antecedent | provisional | whole volume | `bengel_gnomon-of-the-new-testament-v1_fausset1857.txt` |
| Memoirs of Simon Episcopius (Calder, 1838) | calder | transmission | provisional | whole file | `calder_memoirs-of-simon-episcopius_1838.txt` |
| The Life of Mr. J. Cennick, written by himself (1745) | cennick | context | provisional | the narrative of his years with Wesley at Kingswood and with Whitefield at the Tabernacle | `cennick_life-of-mr-j-cennick_1745.txt` |
| Extracts of the Journals of the Rev. Dr. Coke's Five Visits to America (1793) | coke | tradition | assigned | whole work | `coke_extracts-of-journals-five-visits-to-america_1793.txt` |
| The Journal of the Rev. John Wesley, A.M. (Curnock edition), Vol. I -- Curnock's own Editorial Introduction | curnock-nehemiah | context | assigned | Curnock's editorial introduction, lines about 1745-1770 | `wesley-j_journal-v1_curnock1909.txt` |
| Mary Bosanquet Fletcher's journal and letters, as quoted in Moore's Life (1818) | fletcher-mary | tradition | assigned | the journal entries and letters quoted throughout; Moore's connecting narrative excluded | `fletcher-mary_life-compiled-from-her-journal_moore1818.txt` |
| The Life of Mrs. Mary Fletcher (Moore's compiling narrative, 1818) | fletcher-mary | context | assigned | Moore's own connecting narrative between the quotations | `fletcher-mary_life-compiled-from-her-journal_moore1818.txt` |
| Nicodemus, or a Treatise against the Fear of Man (1701), English | francke | antecedent | provisional | whole tract | `francke_nicodemus-against-fear-of-man_1801.txt` |
| Religious Experience and Journal of Mrs. Jarena Lee (1836) | lee-jarena | tradition | provisional | whole work | `lee-jarena_religious-experience-and-journal_1836.txt` |
| A Short History of the Methodists in the United States of America, 1766-1809 (Lee, 1810) | lee-jesse | tradition | assigned | whole work | `lee-jesse_short-history-of-the-methodists-in-the-united-states_1810.txt` |
| Minutes of the Methodist Conferences, vol. I, 1744-1798 | methodist-conference | tradition | assigned | whole volume | `methodist-conference_minutes-v1-1744-1798_1862.txt` |
| The Doctrines and Discipline of the Methodist Episcopal Church in America, with explanatory notes (1798) | methodist-episcopal-church | tradition | assigned | whole work; the Articles of Religion in their own section | `methodist-episcopal-church_doctrines-and-discipline_coke-asbury1798.txt` |
| The Lives of Early Methodist Preachers, vol. I: the preachers' own narratives | methodist-preachers | tradition | assigned | the lives, each headed with its author's name; Jackson's essay excluded | `methodist-preachers_lives-of-early-methodist-preachers-v1_jackson1865.txt` |
| A Collection of Hymns of the Children of God in all Ages (1754) | moravian-church | context | provisional | the hymns translated from the German Herrnhut books | `moravian-church_collection-of-hymns-children-of-god_1754.txt` |
| A Short Account of the Experience of Mrs. Hester Ann Rogers, with her diary extract and spiritual letters | rogers-hester-ann | tradition | assigned | whole work | `rogers-hester-ann_short-account-of-the-experience_1811.txt` |
| The Journal of the Rev. Charles Wesley, vol. I (1736-1740s) | wesley-c | tradition | assigned | the dated Journal entries; Jackson's introduction and notes excluded | `wesley-c_journal-v1_jackson1849.txt` |
| A Collection of Hymns, for the Use of the People Called Methodists - the hymns themselves | wesley-charles | tradition | provisional | the 525 numbered hymns after the Preface (line 258) | `wesley-c_hymns-methodists_1780.txt` |
| Sermons on Several Occasions, Vol. I (Sermon III, 'Awake, Thou That Sleepest') | wesley-charles | tradition | assigned | heading at line 1204; through line about 1669 | `wesley-j_sermons-v1_1771.txt` |
| A Plain Account of Christian Perfection (Wesley, 1766) | wesley-j | tradition | assigned | whole tract | `wesley-j_plain-account-of-christian-perfection_pine1766.txt` |
| A Plain Account of the People called Methodists (Wesley, 1748; 1749 printing) | wesley-j | tradition | assigned | whole tract | `wesley-j_plain-account-of-the-people-called-methodists_1749.txt` |
| Queries humbly proposed to Count Zinzendorf (1755) | wesley-j | tradition | assigned | whole pamphlet | `wesley-j_queries-humbly-proposed-to-count-zinzendorf_1755.txt` |
| The Character of a Methodist (Wesley, 1742) | wesley-j | tradition | assigned | whole tract | `wesley-j_character-of-a-methodist_farley1742.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. II (from September 1738) | wesley-j | tradition | assigned | the dated Journal entries; Curnock's notes excluded | `wesley-j_journal-v2_curnock1909.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. III (1742 onward) | wesley-j | tradition | assigned | the dated Journal entries | `wesley-j_journal-v3_curnock1909.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. IV (the 1750s) | wesley-j | tradition | assigned | the dated Journal entries | `wesley-j_journal-v4_curnock1909.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. V (the 1760s) | wesley-j | tradition | assigned | the dated Journal entries | `wesley-j_journal-v5_curnock1909.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. VI (the 1770s) | wesley-j | tradition | assigned | the dated Journal entries | `wesley-j_journal-v6_curnock1909.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. VII (the 1780s) | wesley-j | tradition | assigned | the dated Journal entries | `wesley-j_journal-v7_curnock1909.txt` |
| The Journal of the Rev. John Wesley, Standard Edition vol. VIII (1789-1791, appendices and index) | wesley-j | tradition | assigned | the dated Journal and diary entries | `wesley-j_journal-v8_curnock1909.txt` |
| A Collection of Hymns, for the Use of the People Called Methodists - Preface | wesley-john | tradition | assigned | lines 75-258 | `wesley-c_hymns-methodists_1780.txt` |
| Sermons on Several Occasions, Vol. I (Sermon I, 'Salvation by Faith') | wesley-john | tradition | assigned | heading at line 490; through line about 845 | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I (Sermon II, 'The Almost Christian') | wesley-john | tradition | assigned | heading at line 874; through line about 1203 | `wesley-j_sermons-v1_1771.txt` |
| Sermons on Several Occasions, Vol. I (Sermons IV-XVI) | wesley-john | tradition | provisional | individual sermon headings verified line by line | `wesley-j_sermons-v1_1771.txt` |
| The Journal of the Rev. John Wesley, A.M. (Curnock edition), Vol. I | wesley-john | tradition | assigned | Wesley's own account of 24 May 1738 and the volume | `wesley-j_journal-v1_curnock1909.txt` |
| Minutes of Several Conversations (the Large Minutes) - Sections I and II | wesleyan-conference | tradition | assigned | lines 359-387 | `wesley-j_large-minutes_1850.txt` |
| The Two First Parts of his Life, with his Journals (Whitefield, 1756 revision) | whitefield | tradition | assigned | whole work | `whitefield_two-first-parts-of-his-life-with-journals_1756.txt` |
| The Works of the Reverend George Whitefield, vol. I: letters 1734 onward (1771) | whitefield | tradition | assigned | the numbered letters | `whitefield_works-v1-letters-1734-1770_1771.txt` |
| The Works of the Reverend George Whitefield, vol. VI: sermons and tracts (1771) | whitefield | tradition | assigned | the numbered sermons | `whitefield_works-v6-sermons_1771.txt` |

What the census names and the table covers: Wesley's Journal complete in the Standard Edition (eight volumes), his Sermons vol. I, A Plain Account of Christian Perfection, the Character of a Methodist and the Plain Account of the People called Methodists (the class-meeting machinery explained by its organiser); the General Rules and connexional government in the Large Minutes and the annual Conference Minutes 1744–1798; the 1780 Collection of Hymns with Charles Wesley's Journal; the women's and ordinary voices the census names (Bosanquet Fletcher's journal and the 1771 letter, Rogers's Account, the Arminian Magazine's first year, the early preachers' own lives); Whitefield's Journals, letters and sermons; the American connexion in Asbury, Coke, the 1798 Discipline with the Articles of Religion, and Jesse Lee; and Richard Allen and Jarena Lee at the era's edge, both provisional.

What the census names and the table does not cover: the class papers, band and society records (archival, Manifest item G4); the Wesley–Crosby correspondence of 1761 as a separate text (it is in Wesley's letters, not vendored in a collected edition); the remaining Standard Sermons (vols. II–IV of the Sermons, Manifest item G2); the Primitive Methodist accounts, which the census itself puts outside the window.

## 2. Cross-link opportunities

The meth build thread found none in the corpus as it stood. The Library pass linked: the Moravian 1754 hymnal (the German repertoire the Wesleys translated from; provisional), Cennick's Life (the Kingswood schoolmaster who broke with Wesley in 1741; provisional), and Wesley's Queries to Zinzendorf (tradition here, context for the Moravians). From this world's side the Library pass linked Wesley's Journal vol. I into the Moravian world (Georgia and Spangenberg) and Asbury's Journal vol. I into the Quaker world. Whitefield's Journals and sermons are cross-linked provisional `context` into the New England Awakening (VII.6), which may want them as tradition.

## 3. Verified acquisition leads

Public-domain editions not yet vendored, confirmed against the host as marked.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Sermons on Several Occasions, vols. II–IV (the remaining Standard Sermons, Manifest G2) | John Wesley | — | 1771 and later printings | https://archive.org/details/sermonsonseveral01wesl (an 1831 collected printing, vol. I) | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata API, djvu 1.56 MB, 23 October 2026; the specific vols. II–IV identifiers are still to be found |
| The Works of the Rev. John Wesley (Jackson, 1829–31), vol. XII, letters | John Wesley | — | 1829 | https://archive.org/details/worksrevjohnwes20weslgoog | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata API, djvu 1.3 MB, 23 October 2026; the route to the Wesley–Crosby and Wesley–Bosanquet letters (G9) |
| The Works of the Rev. John Wesley (Pine, Bristol 1771–74), vols. 2–4 (the Journal) and vol. 15 | John Wesley | — | 1771–74 | https://www.gutenberg.org/ebooks/63452 (vol. 2); 63909 (vol. 3); 68320 (vol. 4); 77550 (vol. 15) | pd-us (Gutenberg) | Gutenberg pages, 23 October 2026; proofread texts of Wesley's own lifetime edition; the Journal duplicates Curnock, vol. 15 holds letters and tracts |
| The Journal of the Rev. Charles Wesley, vol. II | Charles Wesley, ed. Jackson | — | 1849 | https://archive.org/details/1c3be7b8-808c-4714-b80e-c270b971bda4 (vol. I; vol. II to be located) | pd-us-by-date | metadata API for vol. I, 23 October 2026 |
| The Works of the Reverend George Whitefield, vol. II (letters continued) | George Whitefield | — | 1771 | https://www.gutenberg.org/ebooks/71140 | pd-us (Gutenberg) | Gutenberg page, 23 October 2026 |
| Whitefield's separate Journal numbers of 1739–1740 (A Continuation of the Reverend Mr. Whitefield's Journal) | George Whitefield | — | 1739–40 | https://archive.org/details/continuationofre03whit ; continuationofre04whit ; continuationofre00whit | pd-us-by-date | search hits, 23 October 2026; the unabridged contemporary printings behind the 1756 revision |
| The Lives of Early Methodist Preachers, vols. II–VI | ed. Thomas Jackson | — | 1865–66 | https://archive.org/details/thelivesofearly01jackuoft (vol. I vendored) | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata API for vol. I, 23 October 2026; the later volumes' identifiers to be found |
| Minutes of the Methodist Conferences, vols. II onward (1799–) | Methodist Conference | — | 1862– | https://archive.org/details/minutesofmethodi00wesl (vol. I vendored) | pd-us-by-date | metadata API for vol. I, 23 October 2026 |
| A Plain Account of Christian Perfection, later printings (1770, 1777, 1785, 1789) | John Wesley | — | 1770–89 | https://archive.org/details/bim_eighteenth-century_a-plain-account-of-chris_wesley-john_1789 | pd-us-by-date | search hits, 23 October 2026; the 1789 printing is the last of Wesley's lifetime |
| The Character of a Methodist, later printings (1743, 1786, 1793, 1814) | John Wesley | — | 1743–1814 | https://archive.org/details/bim_eighteenth-century_the-character-of-a-metho_wesley-john_1743_0 | pd-us-by-date | search hits, 23 October 2026 |
| The Journal of the Rev. Francis Asbury (1852, Lane and Scott edition) | Francis Asbury | — | 1852 | https://archive.org/details/journalofrevfran03asbu | pd-us-by-date | found by the meth thread's search; the 1821 first edition is vendored instead |
| Wesley's Large Minutes, final 1789 edition | John Wesley | — | 1789 | not located | — | still an open lead, as the meth thread recorded; the 1850 reprint is vendored |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| "Journal of the Rev. Francis Asbury," identifier `journalofrevfran00asbu` | Reported as Volume I | The title page reads Vol. II; vendored as `asbury_journal-v2_1821.txt` (meth thread) |
| The class papers, band and circuit records (Manifest G4) | The census's lived organisational core | Manuscript, chiefly the Methodist Archives, Manchester; not on open hosts. The Plain Account of the People called Methodists (vendored) is the organiser's own description of the system the records belong to |
| The Wesley–Crosby correspondence (1761) as a text of its own | Named by the census | Not printed separately; the letters are in the collected editions (lead above, Jackson vol. XII) |
| Whitefield, A Short Account of God's Dealings (1740) as a separate printing | The research worker's lead | No separate item found on the host by title (23 October 2026); the text is the first part of the 1756 Two First Parts, vendored |

## 5. Open cross-world questions

- **The Moravian Church at Herrnhut (VII.4).** Carried over from the meth thread's dossier: Aldersgate took place at a Moravian-influenced society, Wesley's first Moravian contact was the Georgia voyage of 1735–36, and the relationship broke in 1740 over stillness. VII.4 now has a bucket of its own (Library pass) with Wesley's Georgia journal and his 1755 Queries linked into it from this world. How VII.4's Doc_01 characterises the relationship stays with that world's thread and the project lead, as the meth thread said (`Build/worlds/meth/Doc_01_World_Identification_Boundaries_Orientation.md` §7; `Open_Gaps_Tracking.md` item 2).
- **Whitefield's allocation (VII.5, VII.6, VII.10).** The meth thread's Doc_01 §9 escalated how Whitefield's post-1741 legacy is allocated across this world and its neighbours. His Journals, letters and sermons are now vendored under this world and cross-linked provisional `context` into VII.6; the Welsh world (VII.10) has its own Whitefield material in its leads. The allocation is the project lead's; the texts are placed so any ruling can be applied by changing roles, not by re-vendoring.
- **Two author-slug conventions in one bucket.** The meth thread's rows use `wesley-john`, `wesley-charles`, `asbury-francis`, `wesleyan-conference`; the Library's rows use the filename slugs `wesley-j`, `wesley-c`. Both validate. Reconciling them is a doc-hygiene change to another thread's rows and is flagged here for the meth thread, not made.
- **The AME edge (Allen, Jarena Lee).** Both are placed provisional in this bucket because their conversions and Methodist years fall inside the window and the AME founding of 1816 falls just outside it. If the portfolio adds a Black Church world for Era IX, these two files belong to it as tradition and stay here as context.
- **The British and American strands.** The meth thread's Doc_01 names the 1784 Christmas Conference as the hinge; Coke's journals, the 1798 Discipline and Jesse Lee's history now give the American strand its own voice in the bucket. Whether that is one world with two strands or two worlds is the project lead's call, as before.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Build**, as the meth thread's own Step 0 already found and the census tiers it (Strong, Tier 1). The Library pass changes the ground under the Doc_02 the meth thread wrote: every acquisition gap that document and the world's gaps ledger named as binding is now closed except the manuscript class and circuit records. Wesley's Journal is complete in the Standard Edition; Whitefield speaks in his own Journals, letters and sermons; the women the census names (Bosanquet Fletcher, Rogers) and the Arminian Magazine's lay narratives are in the bucket; the Conference Minutes run from 1744 to 1798 and the American Discipline carries the Articles of Religion; the early lay preachers tell their own lives. The world's own thread should revise Doc_02's gap statements against the refreshed §1 table before any Doc_03 work, and settle the slug question in §5.
