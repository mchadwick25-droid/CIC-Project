# Era 10, P2-E10b: trace of every new sentence

Companion to `CiC_Step0_Era10_P2E10b_Proposed.json`. Each new sentence in that file is listed here with the evidence it rests on. "E" and "item" numbers are the evidence lists in `CiC_Step0_Era10_Movements_V1_0.md`, under the candidate named. "repo" marks a relation that rests on census text (release 21), as the movements record's own Overlap lines do; these are flagged, since census text is counted apart from verified items.

## Notes for review

- **atlasIds.** IX.52 The Anglican Communion; IX.53 faith missions; IX.54 rescue missions; IX.55 the Christian homeschool movement; IX.56 the liturgical movement; IX.57 the Third Wave; IX.58 Promise Keepers. IX.50 stays reserved for G-15.
- **Section A not yet settled on a dated text** for IX.53, IX.54, IX.55 and IX.57. The ruling adds them (G-57, G-60, G-64, G-73), and their floorNote says plainly that no dated statement is cited yet. G-64 adds that Section A "must still be settled on a carrier's dated statement before the entry is built"; that condition is carried, not met.
- **Relations resting on census text.** Each new row's relationsSummary, and one sentence of three statusDescriptions, places the row against existing entries, as the record's Overlap lines do. They rest on release-21 census text, not on a verified item. They are marked "repo" below.
- **Fields left empty or absent.** `documentedStories` is `[]` on all seven rows: the record drafts no stories. `streams` is left off, as on 31 of the 49 era 10 rows: no item names a stream. `entry` is null (nothing built). `c2` is null (no c2 run). `modernCountries` is `[]` on IX.57 (its place label is "N. America", which carries no country on any row); IX.56 has no Belgium entry, because no Belgium ID is used anywhere in the census.
- **Region choices.** IX.54's region is "New York, then the U.S. and Canada" (the draft's "U.S., Canada" has no single gazetteer place; New York's IDs are VIII.19's). IX.56 drops the draft's "Germany": no verified item names a German carrier. IX.57 drops the draft's "UK": no verified item places the movement there.
- **Living evidence** is kept in `livingEvidence` and, per G-51(a), the same items sit in `sources[]` with the note "Evidence for the living mark only". IX.53's one dated item (2023) concerns Operation Mobilisation, which no item ties to the movement; the record says so and so does the row.
- **IX.58.** The Stand in the Gap figure is a crowd estimate (formation_confidence: Contested); the copy says "estimated".
- **Named lines placed:** Bible translation (Camp Wycliffe, in IX.53, G-56(a)); frontier missions and CPM (IX.24, G-58(b), G-59(a)); relief and development (IX.24, G-61(a)); mass evangelism (IX.24 and IX.33, G-34(a)); broadcasting (IX.33, G-65(a)); Word of Faith (IX.45, G-75(a)); Jesus music (IX.45) and praise and worship (IX.30, G-76(a)); the Toronto Blessing (IX.57, G-74(a)); the new monasticism (IX.28, G-67(b)).
- **Frontier missions** is held as an entry (G-79(c)), but G-58(b) makes it a named line in IX.24 now, and G-59(a) puts CPM beside it. The two lines are separate, so the frontier line can be dropped on its own if the review reads "held" as covering the line.
- **Not placed, with the reason:** Keswick (G-70(a): "nothing new"; VIII.4 is frozen). The UBS and Eugene Nida (G-56(a)) go to the cross-era Bible-translation thread, which has no census row. MacArthur and Grace to You (G-18(b)): no verified item; the record has only [S] (W22). IX.11's prosperity line already stands under G-54(a), so nothing is added there. The healing revival, the Oxford Group, the student movement and frontier missions get no rows.
- **IX.16, fields beyond the list.** Removing Iglesia ni Cristo also changes `dates` and `start` (1914 to 1926, the founding of La Luz del Mundo, from the row's own text), `region`, `placeLabel`, `modernCountries` (Philippines out; South Korea in, with VIII.21's IDs) and `floorNote`. `statusWord` still says "the row-split fork stays open": left as is, since splitting the other three bodies was not ruled. The row's `id` keeps "iglesia-ni-cristo-..." because ids are permanent.
- **Meta.** Applying the rows needs `meta.totalEntries` 301 to 308 and `statusCounts["Pre-Survey Candidate"]` 219 to 226 (`metaEdits`).


## IX.52 The Anglican Communion in the Twentieth Century

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2), on the Lambeth and Anglican Consultative Council records and two standard histories. | §3 Anglicanism E1-E5; B1; G-78(a) |
| statusDescription | Its window opens in 1906, where the Victorian Church of England entry ends. | §3 Anglicanism Overlap (repo: VIII.30 ends 1906); G-78(a) dates |
| sourcing | Rich: the records of the Lambeth Conference and the Anglican Consultative Council. | §3 Anglicanism B1; E1-E3 |
| sourcing | Two standard histories come from university presses, by Kevin Ward (2006) and William Sachs, ed. (2017). | §3 Anglicanism B1; E4, E5 |
| floorNote | No question. | §3 Anglicanism Section A |
| floorNote | In 1920 the bishops at Lambeth named the Nicene Creed as the sufficient statement of the Christian faith. | §3 Anglicanism E1 |
| relationsSummary | It carries on from the Victorian Church of England and the Oxford Movement, whose entries end in 1906. | §3 Anglicanism Overlap (repo: VIII.30, VIII.5); B3 |
| relationsSummary | Elsewhere in this era Anglicans appear inside other stories, such as the East African Revival and the Church of South India. | §3 Anglicanism Overlap (repo: IX.3, IX.32) |
| why | When Kevin Ward wrote his history in 2006, most Anglicans belonged to churches outside the West. | §3 Anglicanism E4 |
| why | Their bishops met in the Lambeth Conference. | §3 Anglicanism E1, E3, E9 |
| why | There they spoke on Christian unity, on limiting families and on sexuality. | §3 Anglicanism E1, E9, E3 |
| teaser | A worldwide family of churches whose bishops met at Lambeth, and whose members came to live mostly outside the West. | §3 Anglicanism E1, E4 |
| longDescription | The bishops of the Anglican churches met in the Lambeth Conference, in 1920, 1930, 1968 and 1998 among other years. | §3 Anglicanism E1, E9, E2, E3 |
| longDescription | In 1920 they sent out an Appeal to All Christian People. | §3 Anglicanism E1 |
| longDescription | It named the Scriptures, the Nicene Creed, the two sacraments and a shared ministry as the ground of a future unity. | §3 Anglicanism E1 |
| longDescription | In 1930 they voted 193 to 67, with 47 not voting, on limiting or avoiding parenthood. | §3 Anglicanism E9 |
| longDescription | Where a couple clearly felt a moral obligation to do so, they said, the method must be decided on Christian principles. | §3 Anglicanism E9 |
| longDescription | Lambeth proposed an Anglican Consultative Council in 1968, and it first met at Limuru, Kenya, in 1971. | §3 Anglicanism E2 |
| longDescription | Over the century most of the Communion came to live outside the West. | §3 Anglicanism E4 |
| longDescription | In 1998 the bishops passed a resolution on human sexuality. | §3 Anglicanism E3 |
| longDescription | In June 2008 the first Global Anglican Future Conference (GAFCON) met in Jerusalem and issued the Jerusalem Declaration. | §3 Anglicanism E6 |
| legacy | By 2006, Kevin Ward found, most of its members belonged to churches outside the West. | §3 Anglicanism E4 |
| legacy | Ward and William Sachs both tell its twentieth century as one Communion's story. | §3 Anglicanism E4, E5; Overlap |
| voices | The Lambeth Conference of 1920 — whose Appeal to All Christian People named the Nicene Creed as the sufficient statement of the Christian faith | §3 Anglicanism E1 |
| voices | The Lambeth Conference of 1930 — whose resolution on limiting parenthood was the only one that year with a recorded vote | §3 Anglicanism E9 |
| voices | The Anglican Consultative Council — proposed at Lambeth in 1968, and first meeting at Limuru, Kenya, in 1971 | §3 Anglicanism E2 |
| voices | The Global Anglican Future Conference — which met in Jerusalem in June 2008 and issued the Jerusalem Declaration | §3 Anglicanism E6 |

## IX.53 The Faith-Mission Movement in the Twentieth Century

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §1 M5 Tier; G-57(a) |
| statusDescription | It is a movement carried by mission agencies across many churches, not a church itself. | §1 M5 E3 ('a fellowship of missions without denominational affiliation'); G-28 |
| statusDescription | Its window opens in 1917, when its agencies formed an association of their own. | §1 M5 E2, E3; G-57(a) |
| sourcing | Moderate: the association's records in the Wheaton College archives. | §1 M5 B1; E2, E12 |
| sourcing | Klaus Fiedler (1994) and William Svelmoe (2008) study it, inside wider histories by Joel Carpenter and Wilbert Shenk (1990) and Dana Robert (2009). | §1 M5 B1; E5, E8, E9, E10 |
| floorNote | Not yet assessed on a dated text. | §1 M5 Section A |
| floorNote | The movement has no confession of its own. | §1 M5 Section A; G-29(a) |
| floorNote | It is assessed through the dated statements of the agencies that carried it, and none is cited here yet. | §1 M5 Section A ('not staged and were not seen dated this run') |
| relationsSummary | It is one of two currents that came out of the Edinburgh conference of 1910; the other built the ecumenical movement. | §1 M5 E1 (repo: VIII.25 legacy); Overlap |
| relationsSummary | Its founders, the Wheaton archives record, no longer felt at one with that growing ecumenical movement. | §1 M5 E12 |
| why | In 1917 independent mission agencies formed a fellowship of their own, the Interdenominational Foreign Mission Association. | §1 M5 E2, E3 |
| why | Its members were popularly known as 'faith missions'. | §1 M5 E3 |
| why | Klaus Fiedler tells their history as one movement, from Hudson Taylor to present-day Africa. | §1 M5 E5 |
| teaser | Mission societies with no denominational tie formed a fellowship of their own in 1917, and were popularly known as faith missions. | §1 M5 E2, E3 |
| longDescription | In 1917 leaders of independent mission agencies met in March and again in September. | §1 M5 E2 |
| longDescription | From these meetings came the Interdenominational Foreign Mission Association, 'a fellowship of missions without denominational affiliation'. | §1 M5 E2, E3 |
| longDescription | Its archives describe founders who no longer felt at one with the growing ecumenical movement. | §1 M5 E12 |
| longDescription | Its member missions were popularly known as faith missions. | §1 M5 E3 |
| longDescription | Under the faith principle, a mission looked to prayer alone for its support. | §1 M5 E8 |
| longDescription | By 1965 the association counted forty-six missions. | §1 M5 E3 |
| longDescription | Wycliffe Bible Translators grew from the same culture. | §1 M5 E8 (Svelmoe places Wycliffe inside the faith-mission culture) |
| longDescription | Its training began at Camp Wycliffe, which W. Cameron Townsend and L. L. Legters founded in Arkansas in 1934. | §1 M1 E3 (Encyclopedia of Arkansas, verified); named line for Bible translation, G-56(a) |
| longDescription | Over time, William Svelmoe shows, the faith principle gave way to more open fundraising. | §1 M5 E8 |
| longDescription | Klaus Fiedler tells the whole story as one movement, from Hudson Taylor to present-day Africa. | §1 M5 E5 |
| legacy | Klaus Fiedler's history of 1994 carries the movement's story from Hudson Taylor into present-day Africa. | §1 M5 E5 |
| voices | The Interdenominational Foreign Mission Association — 'a fellowship of missions without denominational affiliation', organized in 1917 | §1 M5 E2, E3 |
| voices | Arthur F. Glasser — whose 1965 account in Christianity Today records the association's forty-six missions and their popular name | §1 M5 E3 |
| voices | W. Cameron Townsend and L. L. Legters — who founded Camp Wycliffe in Arkansas in 1934 to train Bible translators | §1 M1 E3 |

## IX.54 The Rescue Mission Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §1 M12 Tier; G-60(a) |
| statusDescription | Its window opens in 1906, when mission leaders in New York formed a federation of gospel missions. | §1 M12 E3; G-60(a) |
| statusDescription | Its first missions are older, from 1872, and are told here as its beginning. | §1 M12 E2; G-60(a) reach-back disclosed |
| sourcing | Moderate: one academic study, Norris Magnuson's Salvation in the Slums (1977). | §1 M12 B1; E7 |
| sourcing | The network's own history, a 1972 history in Christianity Today and the Billy Graham Center Archives add to it. | §1 M12 B1; E3, E6, E2 |
| floorNote | Not yet assessed on a dated text. | §1 M12 Section A |
| floorNote | Its network keeps a statement of faith, but the text and its first date are not cited here. | §1 M12 E9; Section A |
| relationsSummary | The Salvation Army did the same kind of work, but as a church body. | §1 M12 Overlap (repo: VIII.6) |
| relationsSummary | Norris Magnuson places the rescue missions among the revivalist welfare movements of 1865 to 1920. | §1 M12 E7 |
| why | In 1872 Jerry McAuley opened a mission on Water Street in New York. | §1 M12 E2 |
| why | Others followed, and in 1906 mission leaders in New York formed a federation of gospel missions. | §1 M12 E2, E3 |
| why | A historian places them among the revivalist welfare movements of 1865 to 1920. | §1 M12 E7 |
| teaser | City gospel missions, from New York's Water Street in 1872 to a union of missions in 1913. | §1 M12 E2, E3 |
| longDescription | In 1872 Jerry McAuley opened a mission on Water Street in New York. | §1 M12 E2 |
| longDescription | Others followed. | §1 M12 E2 |
| longDescription | In 1877 Colonel George Clarke and his wife Sarah opened the Pacific Garden Mission in Chicago, apparently without ties to McAuley. | §1 M12 E6, E2, E4 |
| longDescription | It aimed to be 'a harbor for wrecked and ruined lives'. | §1 M12 E4 |
| longDescription | In 1906 mission leaders in New York formed a National Federation of Gospel Missions. | §1 M12 E3 |
| longDescription | On 17 September 1913 a wider body followed, the International Union of Gospel Missions, with about fifty missions. | §1 M12 E3, E6 |
| longDescription | The historian Norris Magnuson counts the rescue missions among the revivalist welfare movements of 1865 to 1920. | §1 M12 E7 |
| longDescription | Their welfare work, he argues, came from a commitment to evangelism and personal holiness. | §1 M12 E7 |
| longDescription | By 1972 the union counted some 350 members. | §1 M12 E6 |
| longDescription | In 2000 it became the Association of Gospel Rescue Missions. | §1 M12 E3 |
| legacy | The union, renamed the Association of Gospel Rescue Missions in 2000, was still the movement's network in 2010. | §1 M12 E3 (AGRM from 2000; renamed Citygate Network only in 2018) |
| voices | Jerry McAuley — whose mission on Water Street, New York, opened in 1872 | §1 M12 E2 |
| voices | Colonel George Clarke and Sarah Clarke — who opened the Pacific Garden Mission in Chicago in 1877 | §1 M12 E2, E4, E6 |
| voices | Sidney Whittemore — who led the International Union of Gospel Missions at its founding in 1913 | §1 M12 E3 |

## IX.55 The Christian Homeschool Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §2 M13 Tier; G-64(a) |
| statusDescription | Its window opens in March 1983, when the Home School Legal Defense Association was launched. | §2 M13 item 10; G-64(a) |
| statusDescription | The Christian day schools and a book of 1975 came before it and are told here as background. | §2 M13 items 1, 3, 5; G-64(a) disclosed prelude |
| statusDescription | It covers only the Christian root of homeschooling that Mitchell Stevens names, not the movement as a whole. | §2 M13 item 1; Section A |
| sourcing | Moderate: three university-press studies, by Mitchell Stevens (2001), Milton Gaither (2008) and Alan Peshkin (1986), and the carriers' own texts. | §2 M13 B1; items 1, 2, 3, 5, 6, 10 |
| floorNote | Not yet assessed on a dated text. | §2 M13 Section A |
| floorNote | Its legal defense association calls itself a Christian organization, but no dated statement of faith is cited here. | §2 M13 item 11; Section A |
| relationsSummary | The school Alan Peshkin studied was a fundamentalist Baptist one, which ties this entry to Fundamentalism. | §2 M13 item 3; Overlap (repo: IX.33) |
| relationsSummary | Mitchell Stevens traces a second, liberal root of homeschooling, which is not Christian and stays outside this entry. | §2 M13 item 1; Overlap |
| why | Sociologist Mitchell Stevens found that homeschooling was not a scatter of private choices but an organized movement. | §2 M13 item 1 |
| why | He traced one of its two roots to the Christian day-school movement of the 1960s and 1970s. | §2 M13 item 1 |
| why | A legal defense association for homeschooling families followed in 1983. | §2 M13 items 6, 10 |
| teaser | In 1983 two homeschooling fathers, both lawyers, founded a legal defense association for families who taught their children at home. | §2 M13 items 6, 10 |
| longDescription | Sociologist Mitchell Stevens traces one root of homeschooling to the Christian day-school movement of the 1960s and 1970s. | §2 M13 item 1 |
| longDescription | Alan Peshkin spent eighteen months in one such school, a Baptist school in Illinois, in the late 1970s. | §2 M13 item 3 |
| longDescription | He called it a 'total world'. | §2 M13 item 3 |
| longDescription | Raymond and Dorothy Moore's Better Late Than Early (1975) argued that formal lessons should wait until a child was older. | §2 M13 item 5 |
| longDescription | Around 1982 James Dobson interviewed Raymond Moore about the book on the air. | §2 M13 item 10 |
| longDescription | Some families who heard the broadcast began to teach their children at home. | §2 M13 item 10 |
| longDescription | In March 1983 two homeschooling fathers, the lawyers Michael Farris and J. Michael Smith, launched the Home School Legal Defense Association with their wives. | §2 M13 items 10, 6 |
| longDescription | At the time, homeschooling was legal in only a handful of states. | §2 M13 item 6 |
| longDescription | A reviewer of Stevens's study summed the movement up as 'a woman's enterprise, in which men are usually junior partners'. | §2 M13 item 9 |
| legacy | By 2001 Mitchell Stevens could describe homeschooling as 'an elaborate social movement'. | §2 M13 item 1 |
| voices | Raymond and Dorothy Moore — whose Better Late Than Early (1975) argued that formal lessons should wait until a child was older | §2 M13 item 5 |
| voices | Michael Farris and J. Michael Smith — homeschooling fathers and lawyers who launched the Home School Legal Defense Association in March 1983 | §2 M13 items 6, 10 |
| voices | Mitchell Stevens — the sociologist whose Kingdom of Children (2001) traced homeschooling's Christian root | §2 M13 item 1 |

## IX.56 The Liturgical Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §2 M11 liturgical Tier; G-68(a) |
| statusDescription | Its window closes in 1962, where historians close the Catholic movement, at the Second Vatican Council. | §2 M11 liturgical item 6 (chapter 'the Roman Catholic Liturgical Movement 1900-62'); G-68(a) |
| statusDescription | The parish after the Council is told in its own entry. | §2 M11 liturgical Overlap (repo: IX.23); G-68(a) |
| sourcing | Rich: its own journal from 1926 and its English handbooks of 1935 and 1937. | §2 M11 liturgical B1; items 3, 4 |
| sourcing | Two academic histories, by Keith Pecklers (1998) and by John Fenwick and Bryan Spinks (1995), tell its story. | §2 M11 liturgical B1; items 5, 6 |
| floorNote | No question. | §2 M11 liturgical Section A |
| floorNote | Its carriers were Catholic Benedictine houses and Anglican parishes, in churches that confess the Nicene Creed. | §2 M11 liturgical Section A; items 1, 3, 4 |
| relationsSummary | It ran through Benedictine abbeys, journals and parishes rather than through the Vatican. | §2 M11 liturgical Overlap; items 3, 4 |
| relationsSummary | The entry on the Catholic Church before the Council names it once, and the entry on the parish after the Council receives its outcome. | §2 M11 liturgical item 8 (repo: IX.47); Overlap (repo: IX.23) |
| why | Historians date the popular liturgical movement from an address at Malines, Belgium, in 1909. | §2 M11 liturgical item 1 |
| why | It reached America through Saint John's Abbey in Collegeville, where the journal Orate Fratres was founded in 1926. | §2 M11 liturgical item 3 |
| why | In England, Gabriel Hebert's books gave the Parish Communion movement its handbook. | §2 M11 liturgical item 4 |
| teaser | From a 1909 address in Malines, a movement for the renewal of worship reached Catholic abbeys and Anglican parishes. | §2 M11 liturgical items 1, 3, 4 |
| longDescription | In 1909 Dom Lambert Beauduin spoke at the National Congress of Catholic Action in Malines, Belgium. | §2 M11 liturgical item 1 |
| longDescription | Historians date the popular liturgical movement from that address. | §2 M11 liturgical item 1 |
| longDescription | In 1926 Virgil Michel of Saint John's Abbey in Minnesota founded the journal Orate Fratres, the movement's voice. | §2 M11 liturgical item 3 |
| longDescription | He also set up the Liturgical Press. | §2 M11 liturgical item 3 |
| longDescription | Keith Pecklers has shown how closely its American leaders tied worship to social justice in the 1930s and 1940s. | §2 M11 liturgical item 5 |
| longDescription | In England, Gabriel Hebert published Liturgy and Society in 1935. | §2 M11 liturgical item 4 |
| longDescription | The Church Times later called it 'the Bible of the Parish Communion Movement'. | §2 M11 liturgical item 4 |
| longDescription | Hebert's collection The Parish Communion (1937) set out a practice that changed the pattern of Sunday-morning worship. | §2 M11 liturgical item 4 |
| legacy | John Fenwick and Bryan Spinks tell its story across Catholic, Anglican, Eastern and North American churches, and close the Catholic part in 1962. | §2 M11 liturgical item 6 |
| voices | Dom Lambert Beauduin — whose address at Malines in 1909 historians take as the movement's start | §2 M11 liturgical item 1 |
| voices | Virgil Michel — who founded the journal Orate Fratres at Saint John's Abbey in 1926 | §2 M11 liturgical item 3 |
| voices | Gabriel Hebert — whose Liturgy and Society (1935) was called 'the Bible of the Parish Communion Movement' | §2 M11 liturgical item 4 |

## IX.57 The Third Wave & the Vineyard

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §3 Third Wave Tier; G-73(b) |
| statusDescription | Its window opens in 1982, when the Signs and Wonders course began at Fuller Seminary. | §3 Third Wave E1; G-73(b) |
| statusDescription | The entry on the charismatic renewal and the Jesus movement closes where this one begins. | §3 Third Wave Overlap (repo: IX.45) |
| sourcing | Rich: Fuller Seminary's archive of the course, its founders' books, Fuller's own study of it and four academic studies. | §3 Third Wave B1; E1, E4-E9 |
| floorNote | Not yet assessed on a verified dated text. | §3 Third Wave Section A |
| floorNote | The Vineyard churches' statement of faith has not yet been checked against its publisher's own text. | §3 Third Wave E10 [S]; Section A |
| relationsSummary | It follows the charismatic renewal and the Jesus movement, whose entry closes where this one begins, in 1982. | §3 Third Wave Overlap (repo: IX.45) |
| relationsSummary | The Toronto Blessing of 1994 grew inside one of its churches. | §3 Toronto Blessing E2, E3; G-74(a) |
| why | In 1982 John Wimber began teaching 'Signs and Wonders' at Fuller Seminary. | §3 Third Wave E1 |
| why | C. Peter Wagner called the stream 'the Third Wave'. | §3 Third Wave E3 |
| why | Its people sought the gifts of the Spirit without taking on Pentecostal or charismatic theology or worship styles. | §3 Third Wave E3 |
| teaser | A seminary course called 'Signs and Wonders', and a stream of churches that sought the Spirit's gifts without becoming Pentecostal. | §3 Third Wave E1, E3 |
| longDescription | In 1982 John Wimber and C. Peter Wagner began teaching MC510, 'Signs and Wonders', at Fuller Theological Seminary in Pasadena. | §3 Third Wave E1 |
| longDescription | The course ran until 1985 and drew controversy. | §3 Third Wave E1, E5 |
| longDescription | Fuller's faculty dropped it in early 1986 and published its own study, Ministry and the Miraculous, in 1987. | §3 Third Wave E5 |
| longDescription | Wagner called the stream 'the Third Wave'. | §3 Third Wave E3 |
| longDescription | Its people believed in the power and gifts of the Holy Spirit without adopting Pentecostal or charismatic theology or worship styles. | §3 Third Wave E3 |
| longDescription | Wimber set out his method in Power Evangelism in 1985. | §3 Third Wave E4 |
| longDescription | In 1994 a revival called the Toronto Blessing began at the Toronto Airport Vineyard. | §3 Toronto Blessing E2 (year and name, verified); named line, G-74(a) |
| longDescription | The Vineyard association cut its ties with that church in December 1995. | §3 Toronto Blessing E3 |
| longDescription | Margaret Poloma published a study of the revival in 1997. | §3 Toronto Blessing E4 |
| longDescription | Jon Bialecki has since studied 'the Third Wave' by name, and the Vineyard as 'an American charismatic movement'. | §3 Third Wave E8, E9 |
| legacy | Donald Miller studied the Vineyard in 1997 beside two other new church networks, and Jon Bialecki's ethnography of it followed in 2017. | §3 Third Wave E7, E9 |
| voices | John Wimber — who taught the Signs and Wonders course at Fuller and wrote Power Evangelism (1985) | §3 Third Wave E1, E4 |
| voices | C. Peter Wagner — who taught the course with Wimber and coined the name 'Third Wave' | §3 Third Wave E1, E3 |
| voices | Ministry and the Miraculous (1987) — Fuller Seminary's own study of the course it had dropped | §3 Third Wave E5 |

## IX.58 Promise Keepers & the Christian Men's Movement

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered Viable, secondary (Tier 2). | §3 Promise Keepers Tier; G-77(a) |
| statusDescription | Its window opens in 1990, when Promise Keepers began. | §3 Promise Keepers E2, E3; G-77(a) |
| statusDescription | The size of its 1997 gathering in Washington is a crowd estimate. | §3 Promise Keepers E2, E3; Trace note (formation_confidence: Contested) |
| sourcing | Moderate: a university-press study by John Bartkowski (2004), an encyclopedia entry, the movement's own book of 1994 and dated contemporary reporting. | §3 Promise Keepers B1; E1-E5 |
| floorNote | No question, on a reported text. | §3 Promise Keepers Section A |
| floorNote | In 1997 a newspaper reported its statement of faith. | §3 Promise Keepers E1 |
| floorNote | It named one God in three persons, the deity of Jesus, and salvation through his death. | §3 Promise Keepers E1 |
| relationsSummary | Megachurches and Lausanne-era evangelicals shared its evangelical setting but not its subject. | §3 Promise Keepers Overlap (repo: IX.30, IX.24) |
| relationsSummary | James Mathisen set it apart from the wider men's movement of the same decade. | §3 Promise Keepers E2; Overlap |
| why | In 1990 a college football coach and a friend started a ministry, and its first men called themselves Promise Keepers. | §3 Promise Keepers E2, E3 |
| why | Within six years it filled 22 stadiums with nearly 1.2 million men. | §3 Promise Keepers E2 |
| why | Each man made seven promises about friendship with other men, purity, marriage, and reaching across racial and denominational barriers. | §3 Promise Keepers E3, E4 |
| teaser | A football coach's 1990 idea that filled stadiums with men making seven promises, and reached Washington in 1997. | §3 Promise Keepers E2, E3, E4 |
| longDescription | On 20 March 1990, Bill McCartney, the University of Colorado football coach, drove with a friend from Boulder to Pueblo. | §3 Promise Keepers E2 (Round 1 review M-12 confirms the Pueblo drive) |
| longDescription | From that trip grew a group of about seventy men who called themselves Promise Keepers. | §3 Promise Keepers E2 |
| longDescription | In 1991, 4,200 men met at the university's basketball arena. | §3 Promise Keepers E2 (Round 1 review M-12) |
| longDescription | In 1996, 22 stadium rallies drew nearly 1.2 million men. | §3 Promise Keepers E2 |
| longDescription | Each man made seven promises, published in 1994 as Seven Promises of a Promise Keeper. | §3 Promise Keepers E4 |
| longDescription | They pledged purity, strong marriages, and friendship across racial and denominational barriers. | §3 Promise Keepers E3 |
| longDescription | On 4 October 1997 a crowd estimated at about a million men gathered in Washington, D.C., for Stand in the Gap. | §3 Promise Keepers E3 (crowd estimate; formation_confidence: Contested) |
| longDescription | In March 1998 the ministry began laying off 345 paid staff. | §3 Promise Keepers E2 |
| longDescription | Sociologist John Bartkowski later traced the rise and fall of this Christian men's movement. | §3 Promise Keepers E5 |
| legacy | In 2001 James Mathisen called it 'the decade's most unexpected and immediately successful movement within the American church'. | §3 Promise Keepers E2 |
| voices | Bill McCartney and Dave Wardell — who founded Promise Keepers in 1990 | §3 Promise Keepers E3 |
| voices | Seven Promises of a Promise Keeper (1994) — the book of the promises each man made | §3 Promise Keepers E4 |
| voices | James A. Mathisen — whose 2001 essay called it the decade's most unexpected and immediately successful movement within the American church | §3 Promise Keepers E2 |

## IX.24 Lausanne-Era Global Evangelicalism

| field | sentence | evidence |
|---|---|---|
| relationsSummary | At the same congress, Ralph and Roberta Winter prepared a paper on the peoples that existing missions did not reach. | §1 frontier missions E12 (Christianity Today, 21 January 1983, verified); G-58(b) |
| relationsSummary | In 1997 the Southern Baptist International Mission Board adopted the Church Planting Movement approach, which David Garrison set out in a 2004 book. | §1 M3 E2 (Massey 2012: IMB adoption in 1997), E1 (Garrison 2004 book, verified); G-59(a) |
| relationsSummary | Evangelical relief agencies shared its ground, some from before 1974: Tearfund grew out of the Evangelical Alliance in 1968. | §1 M7 E3 (Freeman 2019, verified), E4 (Shin 2022: World Vision and Tearfund as evangelical humanitarianism); G-61(a) |
| relationsSummary | Brian Stanley's history names its age after Billy Graham and John Stott, and Graham's evangelistic association was incorporated in 1950. | §1 M4 E3 (Stanley, The Age of Billy Graham and John Stott, verified), E1 (BGEA timeline: incorporated September 1950); G-34(a) |

## IX.33 Fundamentalism

| field | sentence | evidence |
|---|---|---|
| relationsSummary | Radio evangelists such as Paul Rader and Charles Fuller, shut out of free network time, bought airtime instead. | §2 M8 item 5 (Hangen 2002, verified); G-65(a) |
| relationsSummary | In 1944 evangelical broadcasters formed the National Religious Broadcasters, at the invitation of the National Association of Evangelicals. | §2 M8 item 2 (Wheaton NRB records; NAE, verified); G-65(a) |
| relationsSummary | Billy Graham's crusades began with a Los Angeles campaign in 1949, extended from three weeks to more than eight. | §1 M4 E1 (BGEA timeline, verified as BGEA states it); G-34(a) |

## IX.45 Charismatic Renewal & the Jesus Movement

| field | sentence | evidence |
|---|---|---|
| relationsSummary | The Word of Faith movement grew in the same years: Kenneth Hagin's Rhema Bible Training Center dates from 1974. | §3 Word of Faith E1 (Harrison, 'Word of Faith Movement', Contemporary American Religion, verified), E3 (Coleman 2000: a Faith ministry within charismatic Christianity); G-75(a) |
| legacy | Calvary Chapel's Chuck Smith founded Maranatha! Music in 1971, and Larry Eskridge's history of the Jesus People gives Jesus music a chapter. | §3 contemporary worship E1 (Maranatha! Music 'About', verified), E3 (Eskridge 2013, verified); G-76(a) |

## IX.30 The Megachurch & Seeker Movement

| field | sentence | evidence |
|---|---|---|
| legacy | Lester Ruth and Lim Swee Hong later wrote a history of contemporary praise and worship, and of the ideas that reshaped the Protestant church. | §3 contemporary worship E4 (Ruth and Lim 2021, verified); G-76(a) |

## IX.28 The Emerging Church & Post-Evangelical Movement

| field | sentence | evidence |
|---|---|---|
| relationsSummary | The new monasticism began in the same years: in 2004 more than sixty people in Durham, North Carolina, drafted its twelve marks. | §2 new monasticism item 1 (Houston Catholic Worker, 1 October 2004, verified); G-67(b) |

## IX.16 The Way International; Unification Church; La Luz del Mundo

| field | sentence | evidence |
|---|---|---|
| statusDescription | Its window starts in 1926, the founding of the earliest body it covers. | IX.16 longDescription (release 21): La Luz del Mundo founded 6 April 1926 |
| statusDescription | Iglesia ni Cristo, once carried here, now has its own entry. | G-14(a), Decision-Log 2026-11-08; IX.51 in release 21 |
| relationsSummary | Iglesia ni Cristo, once grouped with them, now has its own entry. | G-14(a); IX.51 in release 21 |

## IX.51 Iglesia ni Cristo

| field | sentence | evidence |
|---|---|---|
| longDescription | Iglesia ni Cristo, 'the Church of Christ', was registered with the government of the Philippines on 27 July 1914. | V1.0 IX.16 per-body note (registered 27 Jul 1914, verified); IX.16/IX.51 sources ('the 1914 government registration'); IX.51 informalName |
| longDescription | It was registered under Felix Y. Manalo, and its own history presents him as God's messenger for the last days. | IX.16 voices (release 21: 'under whom Iglesia ni Cristo was registered in July 1914'); V1.0 (the Messenger claim per the church's own history pages, own voice, verified) |
| longDescription | It honored Jesus as Lord and Savior but taught that he was not God. | IX.51 floorNote (release 21); V2.0 IX.16 Section A ('messenger claim, non-trinitarian') |
| longDescription | From February 1939 its magazine Pasugo, in Tagalog and English, set out that teaching. | V1.0 (Pasugo from Feb 1939, verified); IX.16 sources ('Pasugo/God's Message (Feb 1939-, Tagalog and English)') |
| longDescription | It passed through two changes of leader, in 1963 and 2009. | IX.51 statusDescription and legacy (release 21); V1.0 (successions 1963, 2009 [S], carried) |
| longDescription | By its own counts it was, by 2010, the largest church founded in the Philippines. | IX.16 legacy and IX.51 why (release 21); V2.0 confidence note (the church's own counts) |
| longDescription | No independent count is cited here, and independent scholarship on the church is thin. | IX.51 why and sourcing (release 21); IX.16 Barker source note |
