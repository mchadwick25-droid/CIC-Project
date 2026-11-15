# R1 review: Library era 10, batch 2 (2026-11-15)

**Verdict: CHANGES REQUIRED. 4 blocking findings.** All four are small corrections of wording, line ranges or shelf notes. No rights line fails. No file needs to come out.

Reviewer: independent, read and grep only. No network, no validators, no page images. Branch `claude/library-era10-b2`, read at commit `0482b470`.

## Blocking findings

| # | file | what is wrong | evidence | what would fix it |
|---|---|---|---|---|
| B1 | `cic/corpus-map/_staging/put_n08-rus_1927.yaml`; `put_n22-rus_1930.yaml` (and the regenerated bucket `emigre-orthodoxy-and-the-paris-school.yaml`) | The shelf notes name signers who sign nothing in the number. | n08 note: "Signed pieces here by Bulgakov, Berdyaev". No piece in number 8 is signed by Bulgakov. He appears only as the author of a book under review (text line 15868, "Прот. Сергій Булгаковъ ДРУГЪ ЖЕНИХА", reviewed by Ilyin, signed at 16193). The header's own list has no Bulgakov piece. n22 note: "Signed pieces here by Florovsky, Berdyaev". No piece in number 22 is signed by Berdyaev. Line 4390 is a letter from Russia addressed to him ("Письмо изъ Россіи Н. А. Бердяеву"). The only signatures of the four names are Florovsky's at 6278 and 6412. The other 23 notes agree with the signatures in the text. | n08: "Signed pieces here by Berdyaev." n22: "Signed pieces here by Florovsky; a letter from Russia addressed to Berdyaev." Regenerate the bucket. |
| B2 | `cic/texts/vvedensky_tserkov-i-gosudarstvo-rus_1923.txt`, Content note | The header dates a document where the print gives no date, and the range stops 60 lines early. | Header: "The epistle of the Council of September 1917 at about lines 6949-6994". The legible text gives the epistle no date. It orders prayers "14 сентября" (line 6952); the sittings around it are of 18 and 30 August (lines 6895, 7083). The page that would carry a heading is garbled (lines 6947-6948). The epistle runs on to line 7056 ("...самоотвержения и любви Христовой"); the narrative resumes at 7057. | "An epistle of the Council to the people, with no date legible in the print (it orders prayers for 14 September), at about lines 6949-7056; its opening is garbled." The same words go to the REGISTRY and queue rows that copy the Content note. |
| B3 | `cic/texts/christian-east_v4-no2-may-1923.txt` and `christian-east_v4-no4-november-1923.txt`: Content notes, staging rows, and the two Russian buckets | Two shelf loci cut a document of Patriarch Tikhon short. | May 1923: header and locus say lines 4125-4147. The pastoral begins at 4125 and ends at 4200 ("To Thee belongs our life. To Thee goes forth our hope."); the next piece begins at 4203. The locus holds about a third of it. November 1923: header and locus say lines 1359-1612. The epistle ends at 1629. The signature (1624-1625), "Donskoi Monastery, Moscow" and the date "July 15th, 1923" (1629) lie outside the locus, though the header cites that date. | May 1923: lines 4125-4200. November 1923: lines 1359-1629. Change the header, the staging row, the REGISTRY and queue copies, and regenerate the two buckets. |
| B4 | `Build/Ministry/Features/Source-Library/CFT-Wants.md` (batch 2, rows not filled); `Hand_Fetch_List.md` item 7 | Two finds are stated as fact that the batch's own list marks unconfirmed, and one "confirm" rests on search snippets. | CFT-Wants line 1101: "Te Whetu Marama is on Papers Past". Hand_Fetch_List item 7: "Papers Past landing URL, years digitised and rights statement: NOT CONFIRMED"; the only evidence is [S] and [P]. CFT-Wants line 1115: "The first is on Gallica". Hand_Fetch_List item 9 marks the Gallica URL [S]; the fetch was refused and the title page was not seen. Hand_Fetch_List item 7 also says "Te Ara and other pages confirm first issue 15 March 1924" under an [S] mark. | CFT-Wants: "is reported on Papers Past (not confirmed)"; "a Gallica record is reported for it (not opened)". Hand_Fetch_List item 7: "search results say" in place of "confirm". |

## Non-blocking findings

| # | file | finding |
|---|---|---|
| N1 | `zankov_eastern-orthodox-church_lowrie1929.txt` | The OCR prints the title-page year as "1939" (line 115). The header says 1929 was read on the page image. I could not check the image. Mott's foreword is dated September 1929 (line 277) and no year after 1929 stands anywhere else in the file. A second eye on the image would close it. |
| N2 | `put_n02-rus_1926.txt`, `put_n17-rus_1929.txt` | The masthead year is garbled ("192©", line 42) or misread ("1939", line 57). The Rights lines say so and rest on the neighbouring numbers and on dates inside the number (n17: "23. III. 1929" at 3874; "1929. V. 30" at 5423). Disclosed and sound. The basis table counts both under "the year on the masthead"; a footnote there would be exact. |
| N3 | `jabavu_black-problem-2e_1921.txt` | The Rights line says "printed 1921" and rests on a foreword of December 1920 with a catalogue date of 1920. The author's preface is dated January 1921 (line 283), so the catalogue date is the first edition's. Every date is public domain and all three are given. The call is logged for the coordinator. |
| N4 | `velimirovic_religion-and-nationality-in-serbia_1915.txt` | The Rights line says no year is legible "in the OCR". It does not say the page image was read. R12 speaks of a title page that prints no year. The dated note (line 115) and the catalogue date carry it either way. |
| N5 | `wanger_imfundiso-yebandhla-elikatolike-zul_1912.txt` | "Printed 1912" is the title page (line 93). The leaf of 1915 (lines 99-112) shows this copy was issued in or after 1915. Disclosed in the header; public domain either way. |
| N6 | `gollock_sons-of-africa_1928.txt`, Content note; caution 7 | "The Kibangu section crediting Dr Lerrigo": the Kibangu section is lines 7089-7175 and does not name him. The credit stands at lines 7386 and 7466, in the chapter's closing discussion, outside the shelf locus (6616-7180). "For study groups" is not in the print in those words; the preface names the Missionary Education Movement (line 319). |
| N7 | `international-review-of-missions_v12_1923.txt` | The section "Religious Unrest" begins at line 11465, not 11456. Nine lines off; the end (11610) is right. |
| N8 | Shelf rows: `jabavu`, `mikhail`, `manassa-yuhanna` | The same case is handled two ways. Each is the tradition's own writer after the entry's window closes, with no later entry to hold him. Jabavu (1920-21) is context on the southern African entry (to 1906). Mikhail (1911) and Manassa Yuhanna (1924) are tradition on the Coptic entry (to 1906). The shelf principle does not decide this case. One rule is wanted; it is the coordinator's call. The Zulu hymnal of 1911 and Tucker (1908) as tradition are defensible: the hymn words and the events fall inside the windows, and the notes say so. |
| N9 | Shelf notes: three Loisy rows; Ramabai; two Sundar Singh rows | "The decree Lamentabili of 1907 answers this book and its fellow", "before Mukti" and "the entry tells of his visit to the Maramon Convention in 1918" state things the text files cannot carry. The census entries support the first and the third. They explain the role, so I leave them; a strict reading of "describe the text only" would trim them. |
| N10 | Headers: `manassa-yuhanna`, `catholic-sabha`, `khrimian`, `tucker` | "Were looked for and not found", "were not examined", "volume I was not taken" tell what the builder did. They mark real limits, but they are process words in a header. |
| N11 | `CFT-Wants.md`, batch 2 summary | "Languages held beside English (32 files)" reads as 32 files not in English. The table has 32 English files and 39 others (rus 28, fra 2, zul 2, mal 2, mri 1, ara 1, hye 1, deu 1, ell 1). |
| N12 | `Search_Log.md`, calls table | "3,330 such lines were stripped". The 25 Путь headers add up to 3,332. |
| N13 | `Search_Log.md` | "Thirty-two more issues of The Christian East to 1930 are on the host and were not taken" gives no reason. Lototsky and Евразийский временник are "located and not examined" with no reason. The Mizo and Khasi identifiers are said to be "kept in the wants table"; they are in `searcher-logs/oriental_LOG.md`, not in `CFT-Wants.md`. |
| N14 | `Search_Log.md` (Oceania); `te-karere` | The log says the letter is "about Rātana's petition on the Treaty". The legible text speaks of Rātana raising the Treaty again ("nga tikanga whakaara a Ratana i te Tiriti", line 198) and of a covenant. "Petition" is not in what can be read. The header does not use the word. |
| N15 | `CFT-Wants.md` line 1103 | "The three 'Catholic Worker' pamphlets of 1944-1947". The Search_Log dates two of them (1947) and gives no date for the third. |
| N16 | `Hand_Fetch_List.md` item 14 | "Fails the 1930 test" is concluded for an item marked [S], not opened. |
| N17 | Scan artefacts, noted only | Library stamps and slips: `american-zulu` line 135 ("JAN 20 1993"); `smith` line 29 ("NOV. 1941"); `wanger` line 185 ("APR 28 1977"); `mikhail` lines 5885-5928 (due dates 1979-1991); `naayem` lines 124-125 (deposit stamp); `gollock` line 8457 (catalogue card, "1861-1940"). None is a sign of a later printing. |

## What held up

- **Rights lines.** All 71 state a basis the rule allows. I recounted the basis table: 65 by a printed year, 3 by a copyright notice (R12), 2 by a dated preface or foreword (R12), 1 by the calendar leaf. It agrees.
- **Later printings.** No "reprint", "impression" or later-edition notice that postdates the claimed year. "Second Edition" (Jabavu; The Soul of Serbia, same year 1916), "troisième édition" (Loisy 1904) and "second music edition" (Zulu hymnal, by its preface of 1911) are the printings the headers name. No reproduction-permission notice. Bell's "permission" lines (50, 119-180) are his own dedication and acknowledgements of 1924.
- **Host marks.** No "Digitized by", "Google", "archive.org", "Руниверс" or "Библиотек" below line 12 in any file.
- **No Rights line, header, REGISTRY row or queue row names Mark, a ruling or the coordinator.**
- **Counts.** 71 files. 4,273,101 words in the bodies (my recount, whitespace-split, header excluded). The 71 CFT-Wants rows name 71 files that exist; each row's word count and basis string match the file. 71 REGISTRY entries, 71 queue rows, 71 new staging files.
- **Cautions.** The 34 cautions each match a header (with the two soft spots at N6).
- **Batch 1's twelve rows.** All twelve are settled as the Search_Log table says, and each role fits the shelf principle.

## Files checked in depth (33)

`international-review-of-missions_v11_1922`, `_v12_1923`, `_v17_1928`; `gollock_sons-of-africa_1928`; `marty_etudes-sur-l-islam-en-cote-d-ivoire-fra_1922`; `tucker_eighteen-years-in-uganda-and-east-africa-v2_1908`; `jabavu_black-problem-2e_1921`; `wanger_imfundiso-yebandhla-elikatolike-zul_1912`; `te-karere_v24-mri_1930`; `naayem_shall-this-nation-die_1921`; `mikhail_copts-and-moslems-under-british-control_1911`; `manassa-yuhanna_tarikh-al-kanisa-al-qibtiyya-ara_1924`; `khrimian_amboghjakan-yerker-hye_1929`; `malankara-sabha-tharaka_v6-no12-mal_1910`; `catholic-sabha_v2-nos5-6-mal_1922`; `bell_documents-on-christian-unity-1920-24_1924`; `vvedensky_tserkov-i-gosudarstvo-rus_1923`; `valentinov_chernaia-kniga-rus_1925`; `nikolaevskii-sobor_ko-dniu-dvadtsatipiatiletiia-patriarkha-tikhona-rus_1922`; `velimirovic_christianity-and-war_1915`; `ecumenical-patriarchate_mavri-vivlos-ell_1920`; `loisy_evangile-et-l-eglise-3e-ed-fra_1904`; `christian-east_v8-no4-winter-1927`, `_v4-no2-may-1923`, `_v4-no4-november-1923`; `put_n02`, `put_n05`, `put_n08`, `put_n09`, `put_n17` (every listed start and end line opened); in part: `christian-east_v11-no2-summer-1930` and `_v3-no3-october-1922` (the Meletios loci), `zankov_eastern-orthodox-church_lowrie1929` (title leaf and forewords).

In these files every cited range was opened. Apart from B2, B3, N6 and N7 the passages stand where the headers say and are what the headers say. Title, Creator and Publisher lines match the print, or carry the "host record" caveat where the print cannot be read (Manassa Yuhanna, Khrimian's years and office, both Malayalam monthlies, the Greek title, Bell's initials, Christianity and War's author). No office, date or "first" beyond B2 was found supplied from outside the print. Each file ends where its header says.

## Checks I could not make

- **Page images.** Fourteen headers say a year or imprint was "read on the page image": `armenian-church` (the OCR does carry "First Published in 1908", line 102), `catholic-sabha`, `ecumenical-patriarchate`, `loisy` (OCR carries 1904, line 89), `malankara-sabha-tharaka`, `manassa-yuhanna`, `te-karere`, `velimirovic_christianity-and-war` (OCR carries 1915, line 42), `velimirovic_serbia-in-light-and-darkness`, `vvedensky`, `wigram`, `zankov_eastern-orthodox-church`, and the Faith Press imprint on `christian-east` winter 1927. For these I checked that nothing in the text contradicts the year. Nothing does, except the OCR's "1939" in Zankov (N1).
- **The Malayalam years.** The OCR supports them indirectly: "ചിങ്ങ 1008" for 1098 on the calendar leaf of the Catholic Sabha (line 107), and Malayalam-era '85 through the subscription list of the Sabha Tharaka (1085 = 1910).
- **Vvedensky's printer** ("Мосполиграф ... Красный пролетарий") is not in the OCR. The header does not say it was read on the image.
- **Catalogue dates** used for R12 (Jabavu; Velimirović, Religion and Nationality).
- **Whether each archive.org item is open or lending-only.** Six sources have identifiers of the lending pipeline's pattern (`documentsonchris0000gkbe`, `sonsofafrica0000goll_g2r2`, `eighteenyearsinu0000tuck`, `easternorthodoxc0000tsan_r7h2`, `1922catholicsabh0000mala`, `bwb_C0-AYK-159`). The headers say the text was fetched directly with a matching byte count, which a locked item does not allow. I could not confirm it without the network.
- **Byte counts**, and the count of stripped host lines per file.
- **Arabic, Armenian, Greek, Malayalam and Māori passages** were matched by place and by proper names, not read through.

## Rights lines, all 71 files

"Line" is the vendored file's own line. "Image" means the header says the year was read on the page image.

| file | basis | found in text at line | later-printing hits |
|---|---|---|---|
| american-zulu-mission_amagama-okuhlabelela-zul_1911 | copyright notice 1911 (R12) | yes, 168; "Published March 10, 1911" at 175 | "Second music edition" (123), of 1911 by the preface; hymn copyright acknowledgements 239-263; stamp 1993 (135). None blocking. |
| armenian-church_divine-liturgy_1908 | title page (image) | "First Published in 1908" at 102 | none |
| austin_baqubah-refugee-camp_1920 | title page | yes, 39 | none |
| bell_documents-on-christian-unity-1920-24_1924 | title page | yes, 38; preface "Easter 1924" at 265 | "By permission" (50) and 119-180 are the editor's own |
| catholic-sabha_v2-nos5-6-mal_1922 | calendar leaf, both eras (image) | not as "1922"; ME 1098 garbled as "1008" at 107 and 4104 | none; "1999" at 4104 is OCR garble |
| christian-east_v1-no3-september-1920 | cover date | yes, 12 | none |
| christian-east_v10-no1-spring-1929 | cover date | yes, 12 | none |
| christian-east_v11-no1-spring-1930 | cover date | yes, 15 | none |
| christian-east_v11-no2-summer-1930 | cover date | yes, 169 | none |
| christian-east_v2-no2-july-1921 | cover date | yes, 15 | none |
| christian-east_v3-no2-july-1922 | cover date | yes, 12 | none |
| christian-east_v3-no3-october-1922 | cover date | yes, 12 | none |
| christian-east_v4-no1-march-1923 | cover date | yes, 113 | none |
| christian-east_v4-no2-may-1923 | cover date | yes, 12 | none |
| christian-east_v4-no3-august-1923 | cover date | yes, 12 | none |
| christian-east_v4-no4-november-1923 | cover date | yes, 12 | none |
| christian-east_v8-no4-winter-1927 | cover date | yes, 87 | none |
| ecumenical-patriarchate_mavri-vivlos-ell_1920 | title page (image) | yes, 29 and 59, in garbled title leaves | none |
| gollock_sons-of-africa_1928 | copyright notice 1928 (R12) | yes, 98; preface "May 1928" at 326 | catalogue card at 8457 (scan) |
| international-review-of-missions_v11_1922 | volume title leaf | yes, 24 | none |
| international-review-of-missions_v12_1923 | volume title leaf | yes, 24 | none |
| international-review-of-missions_v17_1928 | volume title leaf | yes, 24 | none |
| jabavu_black-problem-2e_1921 | dated foreword, catalogue agreeing (R12) | foreword "12th December, 1920" at 118; preface "January, 1921" at 283 | "Second Edition" (37, 245), the edition held. See N3. |
| khrimian_amboghjakan-yerker-hye_1929 | title page | yes, 28 and 203 | none |
| loisy_evangile-et-l-eglise-3e-ed-fra_1904 | title page (image) | yes, 89 | "Troisième édition" (81), the edition held |
| malankara-sabha-tharaka_v6-no12-mal_1910 | cover imprint (image) | no; a garbled Malayalam-era date at 26 | none |
| manassa-yuhanna_tarikh-al-kanisa-al-qibtiyya-ara_1924 | title page (image) | garbled at 148 ("۱۹۲١") | none; "©" hits at 204-259 are OCR noise |
| marty_etudes-sur-l-islam-en-cote-d-ivoire-fra_1922 | title page | yes, 72 | none |
| mikhail_copts-and-moslems-under-british-control_1911 | title page | yes, 61; "London. 1911." at 126 | due-date slips 1979-1991 at 5885-5928 (scan) |
| naayem_shall-this-nation-die_1921 | copyright notice 1921 (R12) | yes, 116 | deposit stamp at 124-125 (scan) |
| nikolaevskii-sobor_ko-dniu-...-tikhona-rus_1922 | title page | yes, 26 and 228 | none |
| panjikaran_syrian-church-in-malabar_1912 | title page | yes, 63 | none |
| put_n01-rus_1925 | masthead | yes, 43 | none |
| put_n02-rus_1926 | masthead, garbled; neighbours | "192©" at 42 | none. See N2. |
| put_n03-rus_1926 | masthead | yes, 43 | none |
| put_n04-rus_1926 | masthead | yes, 42 | none |
| put_n05-rus_1926 | masthead | yes, 49 | none |
| put_n06-rus_1927 | masthead | yes, 47 | none |
| put_n07-rus_1927 | masthead | yes, 49 | none |
| put_n08-rus_1927 | masthead | yes, 48 | none |
| put_n09-rus_1928 | masthead | yes, 48 | none |
| put_n10-rus_1928 | masthead | yes, 55 | none |
| put_n11-rus_1928 | masthead | yes, 58 | none |
| put_n12-rus_1928 | masthead | yes, 52 | none |
| put_n13-rus_1928 | masthead | yes, 54 | none |
| put_n14-rus_1928 | masthead | yes, 52 ("192 8") | none |
| put_n15-rus_1929 | masthead | yes, 53 | none |
| put_n16-rus_1929 | masthead | yes, 56 | none |
| put_n17-rus_1929 | masthead, misread; neighbours and inner dates | OCR "1939" at 57; "23. III. 1929" at 3874 | none. See N2. |
| put_n18-rus_1929 | masthead | yes, 57 | none |
| put_n19-rus_1929 | masthead | yes, 58 | none |
| put_n20-rus_1930 | masthead | yes, 54 | none |
| put_n21-rus_1930 | masthead | yes, 56 | none |
| put_n22-rus_1930 | masthead | yes, 56 | none |
| put_n23-rus_1930 | masthead | yes, 60 | none |
| put_n24-rus_1930 | masthead | yes, 56 | none |
| put_n25-rus_1930 | masthead | yes, 57 | none |
| smith_christian-mission-in-africa-le-zoute-1926_1926 | title page | yes, 68 | library stamp "NOV. 1941" at 29 (scan) |
| te-karere_v24-mri_1930 | mastheads of the numbers | yes, 16 and 239; a November number at 9021 | none |
| tucker_eighteen-years-in-uganda-and-east-africa-v2_1908 | title page | yes, 187 | none |
| valentinov_chernaia-kniga-rus_1925 | title page | yes, 20 | none |
| velimirovic_agony-of-the-church_1917 | title page | yes, 42 | none |
| velimirovic_christianity-and-war_1915 | printed cover (image) | yes, 42 | none |
| velimirovic_religion-and-nationality-in-serbia_1915 | dated prefatory note, catalogue agreeing (R12) | "June 15, 1915" at 115; no year on the title leaf in the OCR | publisher's list at the foot names other books' impressions (907-929). See N4. |
| velimirovic_serbia-in-light-and-darkness_1916 | title page (image) | preface dates "April, 1916" at 145, "Easter, 1916" at 304 | none |
| velimirovic_soul-of-serbia_1916 | title page | yes, 63 | "Second Edition" (58), same year |
| vvedensky_tserkov-i-gosudarstvo-rus_1923 | title page (image) | preface "22 января 1923 года" at 349 | none |
| wanger_imfundiso-yebandhla-elikatolike-zul_1912 | title page | yes, 93 | leaf of 29 April 1915 at 99-112 (named in the header); stamp 1977 at 185 (scan). See N5. |
| wigram_our-smallest-ally_1920 | title page (image) | not on the title leaf; Austin's letter "February 6, 1920" at 204 | none |
| zankov_eastern-orthodox-church_lowrie1929 | title page (image) | OCR reads "1939" at 115; foreword "September 1929" at 277 | none. See N1. |
| zankov_orthodoxe-christentum-des-ostens-deu_1928 | title page | yes, 51 | none |
