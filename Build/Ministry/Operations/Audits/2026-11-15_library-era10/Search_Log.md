# Library search log: era 10 (1906 to about 2010), batch 1, 2026-11-15

The search record for the Library thread's first fill of the era 10 wants: rows 331-459 and council rows 31-46 of
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`, and the council leads named
on the era 10 scoping page. The vendored files, their rights bases and word counts, and the rows not filled are in
`Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 10 ... batch 1"). This file says where the batch
searched, how each rights call was made, what was refused, and what a profile writer must watch for.

Batch 1 took the major people first, then the conferences. It was worked by tradition and region: American
Protestants; Pentecostal and revival; Catholic Europe and German theology; the ecumenical and missionary
conferences with Asia and Latin America; the Eastern and Oriental churches; Africa and Oceania.

## The rights rule, as applied

Mark's rulings of 2026-11-15 (`Build/Ministry/Features/Source-Library/Decision-Log.md`: R1 to R11 in the entry "Era 10 rights rulings"; R12 in the entry for this batch):

- A printed imprint of 1930 or earlier, read on the title page in the OCR or on the page image. A reprint counts by
  its own date.
- R12 (Mark, 2026-11-15: "Copyright notice yes, preface with a check"): where the title page prints no year, a copyright notice of 1930 or earlier counts; a dated preface counts only
  when the library catalog date agrees. Each header says which was used. Nineteen files rest on it.
- R7: an American book of 1931-1963 whose copyright was not renewed counts as free, with the renewal search in the
  header. Two databases were searched for every candidate: the Stanford Copyright Renewal Database (its web search)
  and the NYPL `cce-renewals` data (a full copy, searched as text).
- R1: the Latin of the Acts of the Holy See printed by 1930 is held. Nothing was taken from vatican.va.
- R2, R3: owner-declared free texts are a class of their own; a non-commercial license is not held.
- R8: a lending-only scan is logged "located, not obtainable here".

## Calls made during the batch

| call | by | what |
|---|---|---|
| The Dictionary of African Christian Biography is CC BY-NC, not CC BY | Mark, through the coordinator, 2026-11-15 | The site's usage page (https://dacb.org/about/usage/) says: "DACB is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License ... Posting on websites containing advertising and all other commercial uses require the express written consent of the DACB." The footer's "CC BY 4.0" links to the by-nc license. R3 governs: cite and link. R2's line on the dictionary is superseded. |
| The Catholic Worker: "Original paper scans only" | Mark, through the coordinator, 2026-11-15 | The site's terms page (https://catholicworker.org/about/terms-of-use-and-privacy-policy/) says "Content from The Catholic Worker paper is not copyrighted", and also puts the site's content under "the Creative Commons Attribution Non-Commercial Share Alike 3.0 license" and says the texts "were digitized by hand by volunteers". Scans of the printed paper are taken on the first sentence; the site's transcriptions are cite and link. |
| A year printed on the title page only inside the work's title | Coordinator, 2026-11-15 (Mark may overrule) | Taken where the publisher and place on the title page are those of the first printing, nothing in the scan names a later printing, and the library catalog date agrees. Eleven files: the nine Edinburgh 1910 volumes, Lambeth 1930 (whose scanned copy also carries a library receipt stamp "NOV 25 1930"), and the Shanghai conference report of 1922. Each header says what the date rests on. |
| Acta Apostolicae Sedis, volumes 2, 18 and 20 | this thread, under R1 | The scans are third-party uploads on archive.org (one with a Public Domain Mark, two with no rights field). The title pages print 1910, 1926 and 1928. Held under R1. Nothing was fetched from vatican.va. |
| Maurin, Catholic Radicalism (1949) | this thread, under Mark's Catholic Worker ruling | An original scan of the Catholic Worker's own book. Its title-page verso prints: "The contents of this book are not copyrighted. The text may be reproduced by anyone in any desired form." No renewal in either database. |
| `cic/engine/texts_registry.py` accepts "Owner-declared free" | this thread | One line, so the registry check passes the class that `cic/texts/INTAKE.md` section 2 names. |

## Renewal searches (R7)

| book | searched | result |
|---|---|---|
| Niebuhr, Moral Man and Immoral Society (Scribner, copyright 1932; a 1936 printing) | Stanford: "immoral society", "Moral man", "Niebuhr moral". NYPL data: "immoral society"; every row naming Reinhold Niebuhr | No renewal found. The NYPL data lists renewals of his other title of 1932, The Contribution of Religion to Social Work (R258326, 1960), and of his books of 1929, 1934, 1935, 1937, 1940, 1943 and later, and none for this one. The reviewer ran the NYPL search again with spelling variants: none. Held. |
| Houteff, The Shepherd's Rod, volume 2 (1932) | Stanford and NYPL: "Shepherd's rod", "Houteff" | Renewed: R244963, 2 November 1959, Florence M. Houteff (widow). Volume 1 (registered 4 December 1930) was renewed too (R220550, 1958). Volume 2 is not held. Volume 1 would be free by date, but the only scan is a revision of 1945 or later. |
| Maurin, Catholic Radicalism (1949) | Stanford and NYPL: "Catholic radicalism", "Maurin" | No renewal found. Held on the book's own notice. |

Keeble's Biography and Sermons (1931), the Cogdill-Woods Debate (1958), Ewart's Phenomenon of Pentecost (1947) and
Andreasen's Letters to the Churches (1959) were looked for as candidates. No scan of the first two was found; Ewart's
is a 1979 printing, lending-only; Andreasen's is a 1981 Australian reprint. No renewal search was run for them.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | 93 of the 94 files |
| lausanne.org | reachable | the Cape Town Commitment |
| dacb.org | reachable | read for its license; nothing taken |
| catholicworker.org | reachable | read for its terms; nothing taken |
| exhibits.stanford.edu/copyrightrenewals; the NYPL cce-renewals data on github.com | reachable | the renewal searches |
| archives.ifphc.org (Flower Pentecostal Heritage Center) | reachable | read for its terms only: "Photocopied materials and PDF files are for personal research only. Only after receiving express written permission from the Flower Pentecostal Heritage Center may items be republished in paper or digital formats." Its scans are served from pentecostalarchives.org, which was not opened. Wanted there: The Apostolic Faith (Los Angeles, 1906-1908). Held for Mark. |
| paperspast.natlib.govt.nz | refused (a bot check; tried twice, plainly) | Wanted there: Te Whetu Marama o te Kotahitanga, the Rātana movement's paper (from 1924), and its rights statement. |
| www.prlib.ru; dlib.rsl.ru | refused (connection reset; on a second plain try prlib.ru's search returned a security-check page) | Wanted there: Собрание определений и постановлений Священного Собора (Moscow, 1918) and the Деяния of 1918, in page scans. |
| www.gutenberg.org | refused (403) | Not needed. |
| HathiTrust | refuses automated clients itself (403), by the coordinator's check of 2026-11-15; no network setting opens it | Mark fetches HathiTrust items by hand |
| books.google downloads, gallica, MDZ, documentacatholicaomnia, anglicancommunion.org, the Adventist archives, mospat.ru | blocked or broken, by the earlier logs and the scoping page | not tried again |
| vatican.va | reachable | not used: its legal notes forbid collection. |

No refused host was worked around.

## Holdings check, before any search

The scoping page's check stands: the shelf held nothing for the era 10 names. One thing it left open is now checked:
Mirbt (1911) and Denzinger (1911) do carry the decree Lamentabili and the encyclical Pascendi in Latin (see the
"Held already" note in `CFT-Wants.md`).

## Searches, by group

Searchers were Sonnet subagents with one scratch directory each. Every pick was checked in this thread: the host
record, the title page or masthead (on the page image where the OCR was unclear), the byte count against the host's
listed size, and the end of the file. A second set of Sonnet readers mapped the parts and the wanted passages of each
file by line number.

**American Protestants.** Found by title and author on archive.org: Rauschenbusch's three books (printings of 1911,
1919 and 1917), Machen (1923), the Scofield Reference Bible (1917), Trumbull's life of Scofield (1920), God Hath
Spoken (1919), Riley (1924), both Niebuhr books, the four-volume Fundamentals of 1917, and the Scopes transcript
(four scans compared; one prints "Special Edition Copyright 1993" and was rejected). Fosdick's sermon: the first hit
was an undated pamphlet in a photocopy, not taken; the sermon was then found in The Christian Century of June 8, 1922.
The Baptist of June 10, 1922 also prints it (`baptist3192unse`, a bound volume of 12.7 MB), located and not taken.
Not found or not taken: see the wants list (Riley's Menace of Modernism, Larkin, the Watchman-Examiner).

**Pentecostal and revival.** The Apostolic Faith, Seymour's Doctrines and Discipline, Bartleman, Haywood, McAlister
and Ewart yielded nothing takeable (no scan, no printed year, or lending-only). Taken: Ramabai (1888), Dyer's Revival
in India (1907), Macnicol (1926), Barratt (1909), and the Korea Mission Field for April 1910 with Kil Sŏn-ju's
postcard. Dyer's Pandita Ramabai: The Story of Her Life (1900, `panditaramabais00dyergoog`) was found, but the
scan is cut off in chapter XII and was not taken. The bound 1910 volume of the Korea Mission Field garbles the postcard; the single-issue scan reads cleanly,
and its masthead date was read on the page image. Not taken: Gale's Korea in Transition (no mention of Kil), the
Korea Mission Field volumes for 1907-1909 (no first-hand words of his), Blair, Penn-Lewis, Houteff.

**Catholic Europe and German theology.** Taken: Tyrrell's four books, Loisy's two in French (1903, 1908) and one in English (1903),
The Programme of Modernism (1908), Acta Sanctae Sedis 40 (1907), Acta Apostolicae Sedis 2, 18 and 20, Barth in German
(1924) and English (1928), Beauduin in English (1926) and French (1919), Orate Fratres volumes 1 to 4 (55 issue
scans), Tillich (1926), Bultmann (1926) and a Mexican pamphlet of 1929. Held for Mark: Loisy's L'Évangile et l'Église
(1902, `lvangileetlglise00lois`): the scan is of a Columbia University preservation film whose target reads
"Reproductions may not be made without permission from Columbia University Library". Located and not taken: Virgil
Michel's thesis of 1918 (`criticalprincipl0000unse`). Not found: Barth's Römerbrief, Bonhoeffer's
Sanctorum Communio (1930), La piété de l'Église (1914), the Malines congress report of 1909, Mortalium animos in an
English of 1928-1930, Trifa, Cristea, the Primum Concilium Sinense, the Mexican bishops' pastoral of 1926.

**The conferences, Asia and Latin America.** Taken: Edinburgh 1910 in nine volumes (eight University of Michigan
scans and, for Commission V, a University of California scan, because the Michigan item numbered 0005 is a second
copy of Commission VI); Mott (1900, 1910, 1915); Oldham (1916, 1924); Lambeth 1908, 1920, 1930; Lausanne 1927;
Stockholm 1925; Jerusalem 1928 in eight volumes; Panama 1916 in three; Montevideo 1925 in two; the Shanghai conference
of 1922; Azariah and Whitehead (1930); Uchimura (1922); Kagawa (1925); two books of Sundar Singh (1924, 1925); Braga
in Portuguese and Spanish; Aglipay's catechism (1912). Not taken: Documentos interesantes of the Iglesia Filipina
Independiente (`ajh3760.0001.001.umich.edu`: no printed year, poor OCR); Uchimura's Shinkō nikki
(`shinkonikkitsuke0000uchi`: the OCR is unusable and the imprint unread); a Catholic critique of the Montevideo
congress (`congresoprotesta00fjcu`: an outside account). Not found: Nee, the True Jesus Church, Cheng Jingyi in
Chinese, Tilak, Yun Chi-ho, Mar Thoma prints, Korean and Indonesian church prints, Aglipay's Oficio Divino.

**Eastern and Oriental churches.** Taken: Bulgakov in Russian (1911, 1918), Fedotoff (1928), Spinka (1927), Emhardt
(1929), the Romanian law and statute of 1925. Not taken: Hyatt's Church of Abyssinia (1928; an outside account that
predates the events wanted). Located and not taken: the council's Деяния on archive.org are inside a reprint whose
title page reads "Москва 1994" (`deyaniya-svyashchennogo-sobora-pravoslavnoy-rossiyskoy-tserkvi-1917-1918-tom-1` and
its fellows); the journal Էջմիածին for 1918-1919 (`1918-12`), unchecked; Malayalam church monthlies of 1900-1911
(`1911_Malankara_Edavaka_Pathrika_Volume_20_Issue_01-03` and others) and Panjikaran, The Syrian Church in Malabar
(1912, `cu31924029361338`), unchecked. No date: Habib Girgis, أسرار الكنيسة السبعة (`AAlexandrina-102649`), a fourth
edition with no printed year. Not found, searched in the original scripts and in transliteration: the 1918 Definitions,
Tikhon's epistle as a separate print, the Declaration of 1927 in a Russian print, Svet nevechernii, the journal Put',
Balakian, Surma, Kyrion II, Khelaia, the encyclical of January 1920, the Pan-Orthodox acts of 1923, Serbian and
Bulgarian prints, Sheptytsky and Slipyj to 1930, al-Karma.

**Africa and Oceania.** Nothing first-hand was found in print to 1930 for the African-Initiated Churches people.
The searcher found entries in the Dictionary of African Christian Biography for most of the named people and none for
Engenas Lekganyane or André Matswa; the dictionary is cite and link (see the calls above).
Located and not taken: Lloyd, Dayspring in Uganda (1921, `dayspringinugand00lloyiala`) and Mullins, The Wonderful
Story of Uganda with Ham Mukasa's own account (1904, `wonderfulstoryug00mull`): both serve the era 9 Uganda entry
better than an era 10 row, and are left for the era 9 thread. Samuel Johnson's History of the Yorubas: two scans are
reprints of 1960 and 1973; a third (`the-history-of-the-yorubas-...-protectorate`) was not checked. Plaatje's Native
Life in South Africa (`dli.ernet.731`) prints no year. Māori and Pacific hymnals of 1896-1918 were located and not
checked.

## Intake

- Host additions were stripped by script and are counted in each header's Provenance note: Google's preamble, the
  Internet Archive's own notice, "Digitized by" page marks, and, in three Cornell scans, the scanning library's notice
  with its archive.org address. Library stamps, slips and film targets are left as the scans have them. Nothing else
  in any body was changed; the body of each file after its header is the stripped host text byte for byte.
- Orate Fratres: each volume file is put together from that volume's issue scans in order, with one marker line
  before each issue.
- The Cape Town Commitment: the text was taken from the page's content block by script. No word was changed.
- Line numbers in the headers are the vendored files' own line numbers.

## Cautions for profile writers

1. **Scofield Reference Bible.** The OCR runs the Bible text and Scofield's notes together by column. Check a note
   against the page image before quoting it.
2. **Bulgakov (both files) and Tillich.** Poor OCR. Do not quote without the page image. They are second witnesses
   until checked.
3. **Emhardt 1929.** The English of Metropolitan Sergius's letter is, by the book's own word, a translation made from
   a Paris Russian newspaper; the book gives that paper's date as July 22, 1927. Give the date of the declaration from
   another source, and say the English is Emhardt's printing. The answers of the Solovki bishops are quoted in parts
   only. No held file prints a full rejection of the declaration, so the "both sides" test for Sergius is half met.
4. **Fedotoff 1928.** His appendix paraphrases the documents of 1927. At one place the print or the OCR dates
   Tikhon's proclamation to 1919; the other places say 1918.
5. **Spinka 1927.** Tikhon's epistle is in English; Spinka says he cites it in full, and the print marks one
   omission with dots. Emhardt prints the same epistle and can check it. The book has nothing on 1927.
6. **Barth in English (1928).** The scan lacks the end of the last address. The English edition also moves one
   address to the end; the German file keeps the order of 1924.
7. **Barth, Bultmann, Tillich.** Free in the United States by date. Barth is protected in Europe until 2038 (R6).
8. **Loisy.** Two of the three files were printed in 1903, before the census entry's window opens in 1906. Their
   shelf rows are marked for a ruling. The French L'Évangile et l'Église of 1902 is not held.
9. **Tyrrell, Christianity at the Cross-Roads.** The OCR prints the preface date as "June 29, 1900". Check the page
   image before giving a date. The introduction is M. D. Petre's, not his.
10. **Medievalism.** Two voices in one book. The English of Mercier's pastoral is not complete; the French in the
    appendix is.
11. **The Programme of Modernism.** Its authors are unnamed. The book does not say who made the English of Pascendi.
    The Latin in Acta Sanctae Sedis 40 is the text to quote from, and this English of 1908 can check a rendering of ours.
12. **Acta Sanctae Sedis 40.** The OCR garbles the decree's date line. Fair to poor OCR.
13. **Latin without an old English.** Mortalium animos (1928), Sacrorum antistitum (1910), the homily to the Chinese
    bishops and Ab ipsis (1926), and Iniquis afflictisque (1926) are held in Latin only. No English of theirs printed
    by 1930 was found. A rendering of ours needs the second independent rendering of R11.
14. **Edinburgh 1910.** The editors' note in volumes 1 to 8 says it was "necessary to abbreviate the speeches" in
    the discussions and that the speakers did not revise them. Cheng
    Jingyi's name is printed "Chang Ching-Yi" in volume 8. Commission V's title page reads oddly in the OCR; check the
    page image before citing its title.
15. **Lambeth 1920.** The Appeal to All Christian People is printed twice with small differences of wording. Quote
    the Resolution 9 text. In all three Lambeth volumes only the Resolutions bind the Conference; the committee
    reports say so.
16. **Lambeth 1930, Resolution 15.** A page break cuts across it in the OCR.
17. **Jerusalem 1928, volume 1.** Only the Council's statement was adopted by vote; the volume says the Council is not
    responsible for the other papers.
18. **Shanghai 1922.** The editors arranged the matter by commission and shortened manuscripts.
19. **Christ in the Indian Villages.** Joint authorship; the book does not say which chapters are Azariah's.
20. **Uchimura.** A 1922 printing of a book whose preface is dated 1895.
21. **Kil Sŏn-ju.** His only held words are one postcard in English, printed in April 1910. The print calls him
    "Kil Moksa" and "Pastor Kil" and signs the postcard "Kil Sun Chu" (garbled in the OCR). The writer says only that
    Mr. McCune gave him a translation; it does not say who translated.
22. **Ramabai.** Her own held book is of 1887-1888, before Mukti. Her "A Testimony" is held only as quoted by
    Macnicol (1926). Dyer's Revival in India is a compilation of letters, many unsigned.
23. **The Fundamentals.** The preface of the 1917 edition says twelve volumes were planned in 1909 and that this
    edition prints their articles "with the exception of a very few". It does not date the first issues. Cite an
    essay by its author. Volumes 3 and 4 carry their 1917 copyright line on the page image only.
24. **Niebuhr, Moral Man and Immoral Society.** A 1936 printing. Held as not renewed (R7); the header carries the
    search.
25. **The Scopes transcript.** A court record with many voices. The host notes text cut off at the inner margin on
    some pages.
26. **The Christian Century, June 8, 1922.** One whole issue; only the sermon is Fosdick's.
27. **Orate Fratres.** Many writers; editorials are unsigned. The marker lines "[[ archive.org item ... ]]" are ours,
    not the print's. Two issues in volume 4 lack a masthead date in the OCR.
28. **Beauduin in English.** The OCR misreads the copyright line as 1916; the title page and imprimatur are of 1926. Virgil Michel's translation; the translator's note does not print the French title.
    "Notre piété pendant l'Avent" is a different work.
29. **Maurin, Catholic Radicalism.** Dorothy Day's introduction is hers, not his. The essays carry no issue dates.
30. **The Catholic Worker, June 1969.** Newspaper columns run together in the OCR. Dorothy Day was living when it was
    printed; people named in the issue may be living now.
31. **The Cape Town Commitment.** Quote word for word only, with an acknowledgement to The Lausanne Movement. No
    modern rendering.
32. **The Padilla pamphlet.** No author is named. Whether Luis Padilla is among the companions of row 424 was not
    checked.
33. **The Romanian law of 1925.** Article numbers are unreliable in the OCR.
34. **Aglipay's catechism.** The title and imprint come from the library record; the OCR of the title page is damaged.
