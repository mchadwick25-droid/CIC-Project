# Church Family Tree — Open Gaps

Append-only and numbered. A number never changes once merged. Cite an entry elsewhere by
subject and date, not by its number alone. Close an entry by appending a dated line under
it, never by deleting it.

1. **Repository is public (2026-11-06).** `mchadwick25-droid/CIC-Project` is public, so the
   code and the Library's structure are readable by anyone, although the license policy
   reserves all rights in them. Private, split or public-with-sensitive-material-moved is
   Mark's decision, with a real CI-minutes cost. Owner: Mark, in its own session.
2. **Lawyer's read of the license policy (2026-11-06).** Recommended before wide promotion,
   especially the AI training section. Owner: Mark.
3. **Two quotes from a CC BY-SA edition (2026-11-06).** Two link quotes come from Brandt's
   1890 Lactantius in a CC BY-SA 4.0 digital edition. Quoting the public-domain print instead
   is the lineage thread's call.
4. **Census `meta` license field (2026-11-06).** Not yet present; added with data release 2.
   - 2026-11-07: closed. `meta.license` names the Faithways Studio license policy and its address; it shipped with data release 3, the release that also carries the domain rule (release 2 was the place labels).
5. **Atlas drift on 23 movement entries (2026-11-06).** `atlas-v3.html` disagrees with the
   census on 23 `entry` blocks. Another thread's cleanup, filed in
   `Build/Ministry/Operations/Standing/CiC_Cross_System_Analysis_Tracking.md`. A gate on the
   standalone launch, not on the move.
6. **Two movement texts repeat corrected claims (2026-11-06).** `aquileian-christianity` and
   `roman-church-third-century`. Another thread's fix. A gate on the standalone launch.
   - 2026-11-07: `roman-church-third-century` fixed in the era 1 links pass: its `why` and
     `legacy` no longer tie "the gravely lapsed" to Callistus. `aquileian-christianity` (era 2)
     is still open.
   - 2026-11-07: `aquileian-christianity` fixed in the era 2 links pass. Its text no longer says
     Ambrose presided at the Council of Aquileia (381), in the description or in its voices; the
     Acts name Valerian of Aquileia first and show Ambrose leading the questioning. Closed.
7. **Domain transfer to Cloudflare (2026-11-06).** `churchfamilytree.com` can move from
   Namecheap to Cloudflare Registrar from about 17 November 2026, after the 60-day lock.
   Pointing its nameservers at Cloudflare can happen any time. Owner: Mark, with steps given.
   - 2026-11-06: nameservers now point at Cloudflare (`nadia` and `watson.ns.cloudflare.com`),
     confirmed at the .com registry. The registration transfer stays open until about 17 November.
8. **Registrant names (2026-11-06).** Whose name each of the four domains is registered in is
   unchecked. Mark: "update them eventually". Not a blocker.
   - 2026-11-06: `churchfamilytree.com` is registered with organization Faithways Studio, Inc.
     (Namecheap contacts). The three Cloudflare domains are still unchecked.
9. **Trade name and trademark screen (2026-11-06).** Register "Church Family Tree" as a
   Colorado trade name of Faithways Studio, and run a trademark screening search, before a
   mark is designed. Owner: Mark.
10. **Narration for new pages (2026-11-06).** The 8 movement pages added by
    mchadwick25-droid/CIC-Project#1517, and every entry added by the gap sweep, have no
    narration. A paid voice run: sample first, Mark's approval by ear, settings passed
    explicitly and printed. The 11 built worlds' recordings live with the world, not on the
    tree page; whether the tree page should carry them is open.
11. **Link colors not checked everywhere (2026-11-06).** mchadwick25-droid/CIC-Project#1521
    (link colors and legend switches) was not checked on the light theme, on phones or with
    a color-vision simulation. The build thread adds these checks to its Phase 2 phone test.
12. **The map's light theme is unfinished (2026-11-06).** Forced on with `data-theme="light"`,
    the map shows a grey ground and muddy river colors. Nothing on the site sets that attribute
    today, so visitors never see it. Found during the rivers check, the same before and after
    that change. The Phase 2 light-theme check (P2-K2) covers it.
13. **Rivers run dry where the census has no entry (2026-11-06).** Six rivers have years
    between their first and last recorded movement with no movement active. Lanes and years:
    1 (1666–1814, 1907–1911); 2 (1442–1516, 1651–1699, 1907–1914); 3 (313–324, 1907–1916);
    3.5 (452–1595, 1907–1944); 4 (1651–1703, 1707–1817); 80 (681–949, 1322–1516, 1651–1769,
    1816–1818, 1907–1912). Most begin just after an era boundary, which suggests end dates set
    to an era's close while the next entry starts later. Several are gaps in coverage, not in
    history. Mark ruled 2026-11-06: the map draws a dashed thread across each gap now (option B),
    and the census is filled later (option C). Owner of C: the Library and lineage thread, entry
    by entry, sourced and graded, with a numbered release. Each gap is checked as real or a
    coverage gap before any entry changes.
14. **New gap stories need place fields (2026-11-07).** Once PL1–PL3 ship, every gap story on the
    map carries `placeLabel` and `modernCountries`, and the validator requires them. The Shared
    Events workstream plans to add council stories placed like the gap stories
    (`../Shared-Events/Decision-Log.md`); its new entries will need both fields. Flagged to that
    thread, not changed here.
15. **Historical regions have no present-day country yet (2026-11-07).** 27 places in 45 entries
    show the place alone, by Mark's ruling: their Wikidata items name only dissolved states, or
    one country that understates them. A later pass finds every present-day country each region
    overlaps, from a gazetteer with boundaries, checked by an independent review, and ships as
    its own numbered release. The list is in
    `Build/Ministry/Operations/Audits/2026-11-07_place-labels/countries-by-place.json`
    (status "historical").
16. **New pages could meet old scripts for ten minutes after a deploy (2026-11-07).** Scripts and
    styles under `assets/` were cached for 600 seconds under unchanging file names, while pages were
    never cached, so a new page could run with an old script. Seen harmlessly after the
    place-labels follow-up.
    - 2026-11-07: fixed in P1c. Both sites' `_headers` now give `assets/` `max-age=0, must-revalidate`,
      so browsers check for a newer copy every time and get a short "not modified" answer when
      there is none.

17. **"UK, today in United Kingdom" (2026-11-07).** Four entries label a place "UK" (African
    diaspora and reverse-mission churches; the emerging church; the narrative kingdom renewal; the
    charismatic renewal). The place line drops a country only when the label uses the country's
    own name, so these read "UK, today in United Kingdom" on the tree pages and the map. The label
    must stay inside the region text, so the fix belongs in the places rule (a place that is itself
    a country), not in one-off edits. Flagged to Mark; not changed yet.
    - 2026-11-07: fixed (Mark: "yes, fix the UK rule"). The place line now leaves out a country
      when a shown place is that country, by name as before, or by gazetteer ID: the place has
      the country's own ID and maps to that one country alone. Seven entries changed, and no
      others: the four "UK" entries, "Aotearoa New Zealand" (New Zealand), and two "Swiss
      lands" entries (Switzerland). "Ruthenia" carries Ukraine's ID in the place record but
      maps to Ukraine and Belarus, so it keeps both. The single-country condition is there for
      that case.

18. **Irenaeus has no movement of his own (2026-11-07).** Against Heresies is the strongest text
    against the Valentinians, but no census movement holds Irenaeus. In the era 1 links pass it
    stands only as a witness inside the household-church link to the Valentinians. Whether
    Irenaeus (or Lyon) gets an entry is a census decision for a later pass (P2-G).
19. **Montanism's end date (2026-11-07).** `montanism-the-new-prophecy` reads "c. 165-400s",
    but its own legacy runs to Justinian, and its new links cite Procopius, Secret History XI,
    and Justinian's Novel 45 for the sixth century. The census entry's owner should reconcile
    the dates.
20. **Raw movement IDs in four later movements' text (2026-11-07).** The relations summaries of
    `palestinian-ascetic-monasticism-early`, `aquileian-christianity` and
    `gallic-nicene-episcopate`, and the relations summary and legacy of
    `roman-church-gregorian`, print movement IDs to readers. They are for the era 2 and era 3
    links passes. Era 1 is clean.
    - 2026-11-07: the three era-2 movements are fixed in the era 2 links pass; their text now
      gives plain names. `roman-church-gregorian` (era 3) is still open.
    - 2026-11-07: `roman-church-gregorian` fixed in the era 3 links pass; its relations summary
      and legacy now give plain names. Closed.
21. **Who compiled the Philocalia (2026-11-07).** The project's records disagree. The Alexandria
    world's source record gives it `attribution_status: attributed`
    (`records/alx/source/alx.source.origen-philocalia.md`). The Cappadocian records say who
    compiled it is contested (`records/cappadocian/force/cappadocian.force.family-archive-transmission.md`).
    The vendored NPNF 7 text has Gregory of Nazianzus sending "works edited by himself and S. Basil"
    (`cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml`, lines 47442-47443). A cross-world
    ruling for Mark. Until then the era 1 text follows the more cautious reading ("tradition
    credits").
    - 2026-11-07: closed (Mark: "go with the reliable credits and forget the cappadocian record
      on this"). The tree credits Basil and Gregory of Nazianzus as its compilers, on the word of
      the NPNF 7 and NPNF 8 editors, beside Gregory's Letter 115. The records are not changed.
      Decision-Log, "The Philocalia's compilers", 2026-11-07.

22. **No entry for the church of Alexandria, 4th-5th century (2026-11-07).** The census holds the
    Alexandrian catechetical school (era 1) but not the see of Athanasius and Cyril. The Aksumite
    conversion-era and Cyrilline Egyptian texts call themselves its children, and no link can carry
    that without bending the school's entry. A census-structure decision for Mark. The sources are
    gathered in the era 2 links audit (Drafting_Record, escalations, group A).
23. **Two Egyptian Miaphysite entries from the same year (2026-11-07).**
    `cyrilline-miaphysite-egyptian-tradition` (from 451, era 2) and
    `cyrilline-miaphysite-egyptian-christianity` (451-642, era 3) describe the same church from the
    same year. A sourced "continued as" link joins them for now. Merge or split is Mark's call.
    - 2026-11-07: met again in the era 3 pass. Era 3's links attach to the era-3 entry only.
24. **Well-known facts with no vendored source (2026-11-07).** Some era-2 sentences state standard
    facts that are not relationships and have no vendored or repo-cited source: Ezana's conversion
    and his coins, Coptic as the language of worship, the twentieth-century Ethiopian patriarch. They
    stand as written, with the texts that would source them on the era 2 wanted list. Whether the
    "qualify" rule reaches facts like these is a method question for Mark.
    - 2026-11-07: era 3 has more of the same, also left standing: the Ladder read every Lent,
      Dorotheus as standard reading, Mar Saba and Saint Catherine's still inhabited (the Judean
      and Gaza monks); Monte Cassino's later destructions, including the bombing of 1944 (the
      Benedictines); the Arian buildings still standing in Ravenna (the Gothic churches).
    - 2026-11-08: the era 4 pass meets the same question in the late Anglo-Saxon (the tenth-century
      monastic reform, Alfred, Ælfric and Wulfstan), Scandinavian, Cluniac (the Cistercian break) and
      Byzantine texts (Stephen the Younger, Tephrike, the 1965 revocation). Held as written, wants listed
      in `Build/Ministry/Operations/Audits/2026-11-07_links-era-4/README.md`. Still Mark's call.
25. **Which entry owns an emperor's act against the Nicenes, 337-378 (2026-11-07).** Constantius II's
    exile of Hilary sits under the imperial church; Valens's deposition of Gregory of Nyssa sits under
    the Homoian church. Each link stands on its sources, but one rule should cover both. A mapping
    ruling for Mark.
26. **The two early Persian entries overlap (2026-11-07).** `persian-church-of-the-east-early`
    (300-451) and `the-church-of-the-east-under-persia` (424-651) share 27 years. Date structure is
    Mark's call; the "continued as" link between them stands on the synod of 424.
27. **Ambrose's Milan and the imperial church overlap (2026-11-07).** The imperial entry tells
    Ambrose's stand against the emperors as one of its own episodes, and the standalone Ambrose entry
    now links to it ("argued against"). Whether the standalone entry stays separate is Mark's call.
28. **Augustine has no movement of his own (2026-11-07).** Era 2's links from Ambrose, Jerome, Hilary,
    the Donatists, the Pelagians and the Gallic monks point at
    `latin-pastoral-congregational-christianity`, whose own text says it is congregational life, "not
    the councils and not the controversies". Whether that is his home, or he needs an entry, is a
    cross-era mapping decision for Mark (P2-G).
29. **The Homoian and Gothic Homoian entries overlap (2026-11-07).** `homoian-arian-christianity`
    (4th-6th c.) and `gothic-and-vandal-homoian-christianity` (451-c. 680) cover the same kingdoms;
    the first's last third repeats the second. The link between them is "gave rise to", which does
    not depend on a period split. For the entry owner.
30. **Era-2 text outside the links pass (2026-11-07).** Found in the era 2 pass, left for each entry's
    owner because none is a relationship claim in the four fields the pass edits:
    - `imperial-juridical-christianity` `why` dates Constantine's toleration to 312; its description
      says 313.
    - `armenian-christianity-conversion-era` calls the Armenian Bible "the Queen of Translations";
      no vendored or repo-cited source carries the epithet.
    - `aquileian-christianity` teaser: Rufinus is "the only reason anyone knows" the creeds differed
      (the same overstatement this pass removed from the description). A documented story there is
      marked "primary text not yet read", though the text is vendored.
    - `hieronymian-ascetic-literary` voices: a pope "wrote back" to Eustochium; Innocent wrote to John
      of Jerusalem.
    - `gallic-monastic-ascetic-christianity` legacy: Lérins still a monastery, Martin patron of
      France with thousands of churches, both unsourced.
    - `anomoean-eunomian-christianity` and `apollinarian-christianity` legacies: unsourced claims
      that their texts are still used or quoted.
    - `cappadocian-nicene-pastoral-monastic-tradition` tile: its false "and named them" is gone, but
      the tile scores Reading Ease 56.6.
    - `danubian-latin-christianity` (era 1): check for the "last Homoian bishops" framing corrected
      here.
31. **A Gallic source record is out of date (2026-11-07).**
    `records/gallic/source/gallic.source.augustine-letters-221-226-absence.md` says Prosper's and
    Hilary's letters to Augustine are not vendored. The Latin is, in CSEL 57
    (`cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, from line 16888). For the
    Gallic world record's owner.
32. **Era 1's link notes were never scored for reading level (2026-11-07).** The era 2 pass scored
    every new and rewritten link note (all at Reading Ease 60 or more). Era 1 scored only movement
    paragraphs: 100 of the 120 notes on main before era 2 score below 60. For P2-L11, or a pass of
    its own.
33. **"Direct heir of Desert Monasticism" (2026-11-07).** `chalcedonian-monasticism-judean-desert-and-gaza`
    (era 3) claims it, but the documented chain runs from the desert to the early Palestinian monks
    to the Chalcedonian houses, and its last step is only Inferential-Thin. For the era 3 pass.
    - 2026-11-07: fixed in the era 3 pass. The relations summary now says the movement drew on
      Desert Monasticism, and a new "influenced" link from the desert carries it. Closed.
34. **No link type for communion (2026-11-07).** None of the six types means "in communion with".
    Era 3 meets it twice: Aksum with Alexandria, and the Egyptian with the Syriac Orthodox
    church. Both are held as "in contact with" at the grade their evidence reaches (the Aksum one
    Inferential-Thin, since no letter from those years survives). A new type would change the
    method. Mark's call.
    - 2026-11-08: era 4 meets the same gap as jurisdiction: the Church of the East's catholicos sent
      the St Thomas Christians their bishops. Held as "in contact with" (Widely Accepted). One ruling
      should cover communion and jurisdiction together.
35. **Caucasian Albania's end date (2026-11-07).** `church-of-caucasian-albania` ends at 705, and
    `bagratid-armenian-christianity` says it "absorbs" the catholicosate after 705. The vendored
    histories (Brosset 1876, Ormanian 1912) show the see living on inside the Armenian church,
    with a catholicos installed in 1701/2, until it was abolished in the early nineteenth century.
    The era 3 pass took the year 705 out of the Albanian prose. The dates belong to the entry's
    owner, for Mark's ruling.
    - 2026-11-08: the era 4 pass also left the Bagratid summary's "absorbs the story of Caucasian
      Albania's catholicosate after 705" as written, for the same ruling.
36. **The Armenian "continues as" chain skips a movement (2026-11-07).**
    `armenian-christianity-after-avarayr` continues as `bagratid-armenian-christianity`, skipping
    `armenian-christianity-before-the-bagratids` (c. 554-884), which has no "continues as" of its
    own. The era 3 "continued as" links run through the pre-Bagratid movement. The two data fields
    need the matching fix. For the entry owner.
37. **Sebeos on the Albanian catholicos (2026-11-07).** Sebeos (ch. 33, in Macler's French) puts
    "le catholicos de Géorgie et d'Albanie" on Chalcedon's side at Khusro II's court, c. 614. If the
    Albanian head is meant, the entry's Oriental Orthodox stream is not the whole story. Needs a
    reader of Thomson's English Sebeos (1999), which is not vendored.
38. **No "continued as" link from the Irish monasteries to medieval Ireland (2026-11-07).** The
    census splits Ireland at 664, but neither era-3 text names the continuation. For the era 4 pass.
    - 2026-11-08: fixed in the era 4 pass. A "continued as" link (Documented) rests on Bede IV.4 and
      V.15 and Adomnán's line of abbots. The medieval Irish text is still a one-line stub: it names
      the continuation only by starting at 664, where the earlier entry ends. Closed.
39. **Whitby in the Anglo-Saxon text (2026-11-07).** The era 3 pass added the Whitby link (the
    Anglo-Saxon church "argued against" the Irish, Bede III.25). `anglo-saxon-christianity` also
    names Whitby; the era 4 pass should count that link as named there.
    - 2026-11-08: done in the era 4 pass. Era 3's Whitby link is counted as named in the Anglo-Saxon
      text, and era 4 kept it as published. Closed.
40. **An era-2 link note uses internal wording (2026-11-07).** The note of
    `palestinian-ascetic-monasticism-early--chalcedonian-monasticism-judean-desert-and-gaza` says
    "No text we hold ties the later monks to the earlier". The era 3 review proposed "No source
    from the time ties the later monks to the earlier, so this rests on place and sequence alone."
    The link is era 2's, so era 3 left it. For P2-L11.
41. **No medieval English or Scandinavian successor entry (2026-11-08).** Late Anglo-Saxon ends at
    1066 and Scandinavian conversion at 1104, and no entry carries either church on. The Scandinavian
    "continued as" link therefore runs to the Reformation kingdoms (1527). It rests on the see of
    Skara at both ends and states Denmark's break of 1536-37, graded Inferential-Thin. Whether it
    should stand until a medieval entry exists is a census-structure call. Mark's call.
42. **Two "continues as" fields name entries the evidence only influenced (2026-11-08).**
    `carolingian-reform-christianity` continues as `latin-papal-church-gregorian` (160 years apart,
    Cluny between), and `cyrillo-methodian-slavic-christianity` continues as `kievan-rus-christianity`
    (what passed was books and letters, not a community). The era 4 links are typed "influenced".
    Should the fields be cleared? For Mark or the entry owner.
43. **Links the sources support but no text names (2026-11-08).** Alcuin's *Against Elipandus*
    (vendored, PL 100-101) would carry a Documented Carolingian "argued against" Mozarabic link.
    Lützow (1910) names the Salzburg clergy who opposed Methodius; Férotin (1912) names Cluny's monks
    in the replacing of the Mozarabic rite. Each needs new prose first. Mark's call.
44. **The Bogomil entries overlap (2026-11-08).** `bogomils` runs from the tenth century on, and
    `balkan-bogomil-continuation` covers 1054-1300. Basil's burning (c. 1100) and the Cathar link fall
    in both. The Cathar link sits on `bogomils`, whose text names it three times. Mark's call.
45. **No Melkite entry between 1009 and 1724 (2026-11-08).** The Melkite legacy says the communion
    continues, and the only later entry is the 1724 split, so its "gave rise to" link spans seven
    centuries (the note says so). Mark's call.
46. **The Abbasid Church of the East is a stub (2026-11-08).** `church-of-the-east-under-the-abbasids`
    has empty relations summary, description and legacy; the era 4 pass rewrote only its `why`. For
    the entry owner.
47. **The Georgian Golden Age says "silent since 622" (2026-11-08).** `the-georgian-golden-age` (era 5)
    calls its tradition silent since 622, against the revival entry's monasteries and Iviron, now
    joined by a "continued as" link. For the era 5 entry owner.
48. **Dominant Modern Reconstruction on old secondary works (2026-11-08).** Twelve era 4 links carry
    this grade, several on nineteenth- and early twentieth-century works (Rački 1869, Evans 1877,
    Mouravieff 1838, Lützow 1910, Brosset 1849). Some of those works retell a medieval narrative
    rather than reconstruct anything. Both reviewers held that the grade understates rather than
    overstates, and that dropping to Inferential-Thin would call standard facts thin. A method
    ruling: what the grade means when it rests on old works, or vendor the medieval texts. Mark's call.
49. **Two source rules applied in era 4 (2026-11-08).** (a) A retelling centuries later (Herberstein
    1549, the Kyiv Synopsis 1674, the Malabar chronicle after 1580) is not a primary for ninth- or
    tenth-century events; it is listed as a secondary. (b) A canon's own text carried in a later
    collection (Theodosius, 853-858, in Assemani's printing) counts as a primary, at Widely Accepted
    when it reaches us only in translation. Both reviewers agreed. They change no method rule, but
    later eras should apply them the same way; P2-L11 should check earlier eras against them.
50. **Era-4 text outside the links pass (2026-11-08).** Left for each entry's owner:
    - The Silk Road description ends on a sentence fragment.
    - The Kievan description's "Envoys…" sentence has no main verb.
    - The Cluniac summary describes Peter the Venerable, after the entry's 909-1109 window.
    - Dates the vendored texts give differently: Alopen's arrival (636, not 635); the Kollam plates
      (Mingana, about 824, not 849); Lund's archbishopric (Anjou, 1103, not 1104).
    - The late Anglo-Saxon `why` and description state the tenth-century refounding outright (see
      "Well-known facts with no vendored source", 2026-11-07).
51. **Cistercians and Cluny (2026-11-08).** The era 5 pass removed every Cluny claim from
    `cistercian-monasticism`: its own text has the founders leave Molesme, and no vendored text ties
    Cîteaux to Cluny. The era 4 `cluniac-reform-monasticism` text still says the Cistercians reacted
    against Cluny. For the era 4 owner.
52. **Well-known facts with no vendored source, era 5 (2026-11-08).** Added to the method question in
    "Well-known facts with no vendored source" (2026-11-07). Era 5 sentences left standing as written,
    each with its wanted text on the era 5 list: the Carmelites' move west, Molesme, the Lavra's
    founding in 963; Lateran IV's dress rule for Jews and Muslims, the Council of Troyes and the
    Templar rule (1129), the Protestant orders of St John, Rhodes and Malta, the reach of William of
    Tyre's history; Dante placing Joachim in paradise, the crown's annexation of Languedoc, the
    Waldensian name; the memory of 1204 in the Orthodox churches, John Paul II's words in 2001 (the
    drafter doubts "apology" is the exact word), the contested Kyiv Lavra and Kyiv's political weight.
    Two of these (Troyes, the orders of St John) touch bodies with no movement of their own.
53. **No movement for the Bulgarian church of the Second Empire (2026-11-08).** The Tarnovo synod of
    1211 against the Bogomils cannot be linked. A census-structure question for Mark, low urgency.
54. **Long-gap links to modern churches (2026-11-08).** The Georgian golden age and the Serbian and
    Bulgarian monasteries are not linked to their modern entries (the Georgian church restored in
    1917; the modern Balkan churches, era 9), with centuries and other entries between. Whether such
    links should exist is a mapping ruling for Mark.
55. **No link type for church jurisdiction (2026-11-08).** A patriarch appointing another church's head
    bishop is drawn as "influenced" (Caesarea to Armenia, Constantinople to Kyiv) or as "in contact
    with" (Alexandria and Aksum; the Coptic patriarch and Ethiopia). A method question for Mark.
56. **No Syriac Orthodox movement after 1300 (2026-11-08).** `syriac-renaissance` has nothing to
    continue as. Portfolio structure, for Mark, low urgency.
57. **The Abbasid Church of the East has no continuesAs (2026-11-08).**
    `church-of-the-east-under-the-abbasids` (era 4) has `continuesAs` null, though the era 5 pass
    added its "continued as" link to `church-of-the-east-under-the-mongols`. A data fix for the era 4
    owner.
58. **Humiliati sources (2026-11-08).** Innocent III's letters of 1201 (Tiraboschi) and the decree Ad
    abolendam of 1184 (Mansi 22, or Friedberg) are not vendored. They would settle the approval year,
    now "around 1200", and the three qualified sentences on 1184.
59. **The Franciscan order and the Observants, held for P2-L6 (2026-11-08).** Eugenius IV's 1438
    letter making Bernardino of Siena vicar of the Observant houses (Bullarium Franciscanum, new
    series I, no. 385, lines 34646-34653) documents `franciscan-order-era-6` gave rise to
    `observant-reform-and-popular-preaching`. Drafted in the era 5 pass, dropped there because both
    ends are era 6. The era 5 Franciscan text is carried by
    `the-franciscan-movement--observant-reform-and-popular-preaching` (influenced).
60. **Two more out-of-era link notes use "we hold" (2026-11-08).** Besides the one in "An era-2 link
    note uses internal wording" (2026-11-07): `desert-monasticism--iconophile-byzantine-monasticism`
    and `antiochene-church-third-century--antiochene-exegetical-christianity-chrysostom-ce`. Era 5
    cleared every case touching its own movements. For P2-L11.
61. **Page recordings read the old descriptions (2026-11-08).** The tree pages play a recording of
    each movement's description, and the link passes rewrite descriptions. In era 5, 16 recorded
    pages now play text that no longer matches the page: `cistercian-monasticism`,
    `canons-regular-victorine-school`, `athonite-and-comnenian-byzantine-monasticism`,
    `the-beguines`, `the-waldensians`, `zagwe-and-early-solomonic-ethiopian-christianity`,
    `maronite-christianity`, `military-religious-orders-templars-hospitallers`,
    `cathars-albigensians`, `free-spirit-heresy`, `serbian-and-bulgarian-medieval-monasticism`,
    `byzantine-church-after-1054`, `latin-papal-church-gregorian`, `armenian-cilicia`,
    `latin-church-of-outremer`, `the-humiliati`. Eras 1 to 3 likely have the same drift. The
    recording manifest stores no hash of the text it was made from, so nothing catches it. Fixing it
    is a paid voice run: sample first, Mark's approval by ear, settings passed and printed. For Mark.
62. **"Silent since 622" is fixed (2026-11-08).** The era 5 pass removed the claim from
    `the-georgian-golden-age`; its summary now says it carries on from the Tao-Klarjeti revival.
    This closes "The Georgian Golden Age says 'silent since 622'" (2026-11-08).
63. **The Franciscan order and the Observants is drawn (2026-11-08).** The era 6 pass drew
    `franciscan-order-era-6--observant-reform-and-popular-preaching` (gave rise to, Documented) from
    Eugenius IV's 1438 letter. This closes "The Franciscan order and the Observants, held for P2-L6"
    (2026-11-08). The era 5 link from the Franciscan movement to the Observants (influenced) stands
    beside it: it carries the founder's Rule across 1300, the new one the Observant houses as houses
    of the order.
64. **Well-known facts with no vendored source, era 6 (2026-11-08).** Added to the method question in
    "Well-known facts with no vendored source" (2026-11-07). Era 6 follows the era 5 practice: plain
    facts that are not links between movements stand. Restored after review: the Mamluk campaigns in
    the Kesrwan around 1305 (`maronite-christianity-era-6`); the Ewostathians' Sabbath and the
    council of 1450 (`the-ethiopian-monastic-flowering`); the St Thomas Christians' privileges from
    Hindu rulers and their headman (`st-thomas-christians-1300-1517`); Julian's day in the Church of
    England's calendar (`the-english-mystics-and-devout`). Left standing: John of Capistrano's
    preaching and the persecution of the Jews of Breslau in 1453
    (`observant-reform-and-popular-preaching`); Rome sending friars against the Bosnian Church;
    Margery Kempe's life facts and Julian's cell rebuilt after wartime bombing; the Devotio houses
    closing in the Reformation; the 1317 Dongola inscription; Leo X's Ite vos (1517). Wanted texts
    for each are in the era 6 audit README. For Mark.
65. **The Church of the East's "Hakkari" name (2026-11-08).** `church-of-the-east-timur-to-hakkari`
    is titled "... and the Hakkari Remnant". Its corrected fields put the late-fifteenth-century
    patriarchs at Gazarta and Mosul on the upper Tigris (the 1490-1504 history; Wigram 1929), with
    survivors in the Hakkari mountains. The teaser now says so. Whether to rename the movement, and
    the era 7 summary of `church-of-the-east-schism-of-1552` that leans on the title, is Mark's call.
66. **No link type for an authority's acts on another body's own order (2026-11-08).** Leo X's Ite
    vos (1517) divided the Franciscan order; Martin V, Eugenius IV and the councils set the
    Observants' government. These are neither "argued against" nor "gave rise to". Five such
    sentences were left unlinked as not-a-claim. Close to "No link type for church jurisdiction"
    (2026-11-08). A method question for Mark.
67. **The Council of Basel sits under the papacy (2026-11-08).** The Compacts of Basel link
    (`latin-papal-church-avignon-to-lateran-v--the-hussite-and-bohemian-brethren-movement--2`) runs
    from the papal church, because the census has no movement for the conciliar movement. If the
    councils are ever told apart from the papacy, the link's "from" changes (a retired ID and a new
    one). For Mark, low urgency.
68. **No Carthusian movement after 1300 (2026-11-08).** `carthusian-life` ends in 1300, so the
    documented Carthusian copying of The Cloud of Unknowing and Hilton's Scale cannot be drawn as a
    link. The English mystics text states the copying without a link. Extending the entry or adding a
    later one is portfolio structure, for Mark.
69. **The inquisition-record sects and the Free Spirit overlap (2026-11-08).**
    `inquisition-record-sects-adamites-and-kin` (1350-1500) and `free-spirit-heresy` (1250-1400)
    both cover the German Free Spirit trials and rest on the same Vienne decree. No lineage link fits
    the overlap. Whether to split them by evidence (Adamites in one, Free Spirit in the other) is
    for the census owner and Mark.
70. **Held for later link passes, from era 6 (2026-11-08).** Each joins two movements outside era 6:
    - `czech-churches-last-century` to `the-moravian-church-at-herrnhut` (continued as): the Hussite
      text's "renewed as the Moravian Church" rests on it. Eras 7-8.
    - `the-hesychast-revival-paisius-and-the-philokalia` to `the-optina-elders-and-russian-ascetic-renewal`. Eras 8-9.
    - The later steps of the Church of the East (to the Chaldean and Assyrian lines), the Armenian
      catholicosate of Cilicia (to Antelias), the Maronites and the St Thomas Christians (to the
      Malankara and Mar Thoma churches). Eras 7-10.
    - `the-waldensian-reformed-union` legacy still names the union with the Italian Methodists and
      the church in Argentina and Uruguay, which eras 5 and 6 removed for want of a source. Era 7.
    - `the-old-believers` summary says it "grew out of" Muscovite Christianity; the only link is an
      Inferential-Thin "influenced" (Conybeare 1921). Era 8.
71. **The Maronites' unbroken communion with Rome (2026-11-08).** The Maronite tradition holds it was
    never out of communion with Rome; Eugenius IV's bull of 1445 receives the Maronites of Cyprus
    into union. `maronite-christianity-era-6` now states both. Whether a `contested_claim` record is
    wanted is a world-build matter, for the Maronite world's owner.
72. **"Entry" in status descriptions (2026-11-08).** Thirteen era-6 `statusDescription` fields, and
    about 80 across all eras, say "entry", which is build wording in public text. The link passes do
    not edit status fields. For P2-L11 or the census owner.
73. **Page recordings read the old descriptions, era 6 (2026-11-08).** As in "Page recordings read
    the old descriptions" (2026-11-08): the era 6 pass rewrote the long description of all 23 era-6
    movements, and each has a recording in `cft-website/audio/tree/`. All 23 now play text that no
    longer matches the page. A paid voice run, for Mark.
74. **"Continues as" with no graded link (2026-11-08).** 36 movements carry `continuesAs` with no
    matching "continued as" link: 4 in eras 3 to 5 (Armenia after Avarayr, the Carolingian reform,
    the Cyrillo-Methodian mission, Athonite monasticism; see "Two continues as fields name entries
    the evidence only influenced" and "The Armenian continues as chain skips a movement"), 30 in eras
    7 to 9 and 2 in era 10. The map's card now marks each "continued as · not yet graded", and names
    the checked link where the pair has one of another kind. The era 7 to 9 passes and P2-L11 close
    them; era 10 waits for P2-L10.
75. **The tree's own pages have no light theme (2026-11-08).** The movement pages and the about,
    method, data, privacy and support pages are dark only; a browser set to light shows them dark.
    Seen while checking P2-M and P2-D. P2-K2's light-theme check covers it, with the map's
    ("The map's light theme is unfinished", 2026-11-06).
76. **Outcome test, adoption by vote (2026-11-08, for Mark).** Does a church body adopting another
    side's confession, catechism or worship order by its own vote count as "a rule ... changed by an
    authority" (major) or as "a text taken up" (minor)? Era-7 review round 1 (R1-05) ruled it a text
    taken up, and the era 7 pass dropped four outcomes: `lutheran-wittenberg-and-its-congregations--scandinavian-reformation-kingdoms`
    (Uppsala 1593), `the-reformed-cities-zurich-and-geneva--the-scottish-reformation-and-kirk` (General
    Assembly 1562), `the-reformed-cities-zurich-and-geneva--the-huguenots` (Paris synod 1559) and
    `the-reformed-cities-zurich-and-geneva--dutch-further-reformation-and-refuge-culture` (Emden 1571).
    Two more links of the class carry none in era 7's view: `hieronymian-ascetic-literary--the-tridentine-church`
    (Trent's Vulgate decree) and `the-kyiv-mohyla-orthodox-revival--orthodoxy-under-the-ottomans-parish-millet-and-n`
    (the patriarchs' 1643 decree on Mohyla's Confession). Main (era 6, PR #1544; the P2-ML major-links
    pass) already publishes an outcome on `hieronymian-ascetic-literary--the-tridentine-church`, so the
    class stands one with an outcome and five without until Mark rules. Main's outcome is left in place
    because it is not the era 7 pass's to change; Mark's ruling settles all six alike.
77. **Sentence fragments in era-7 prose (2026-11-08).** Fragments left by an earlier sentence split
    (e.g. "Asking the government to allow their view.") remain in long descriptions and legacies the
    era 7 pass did not otherwise rewrite: the Dutch Further Reformation, Remonstrants, Waldensian union,
    Czech churches, Zurich and Geneva (two), English Reformation (two), Scottish Kirk, Huguenots
    (legacy), recusants (long description and legacy), Puritanism (two), Jesuits, Ottoman Orthodoxy,
    Philippines, Kyiv-Mohyla (two), Carmelite reform (two) and the Tridentine church (legacy). Not
    relationship claims. For the census owner, or P2-L11.
78. **Long link notes, era 7 (2026-11-08).** Some notes the era 7 pass did not otherwise touch run past
    three sentences: `the-anabaptist-movements--the-baptists` and `puritanism--the-baptists` (five
    each), `scandinavian-conversion-christianity--scandinavian-reformation-kingdoms` (four). Trim when
    next touched. For P2-L11.
79. **The validator does not check secondary quotes (2026-11-08).** `tools/validate-census.mjs` checks
    quotes only on primary sources. Secondary sources may carry a file, lines and quote (137 now
    do), and those go unchecked. Every era-7 secondary quote was checked by hand in revision 1 and
    review round 2. The validator should check them too. For the validator's owner (P2-ML).
80. **Wanted texts that would lift three era-7 links (2026-11-08).** John Thornton, The Kongolese
    Saint Anthony (1998), read at a locus (`kongo-christianity-afonso-to-1650--the-antonian-movement-in-kongo`
    is Inferential-Thin until then); Stephen Turnbull (1998) or Christal Whelan (1996), read at a
    locus (`kirishitan-japan--japanese-christianity-hidden-emergence-meiji`); Kenneth Mills, Cambridge
    History of Christianity vol. 6 ch. 27 (`new-spain-and-andes-mission-born-christianity--colonial-latin-american-devotional-catholicism`);
    and the English royal proclamation against the Family of Love, dated 1580 only by Fuller's 1845
    editor. Full list: the era 7 audit README.
81. **A label movement with no links of its own (2026-11-08).** `mission-born-christianities-kirishitan-japan-kon`
    is a label over four regional movements. The era 7 pass drew every relationship it names on the
    regional movement instead, so the label stands alone in the tree. The review agreed. Whether a
    label should show as joined is a display question, for Mark. The only other label is
    `progressive-christianity` (era 10).
82. **Page recordings read the old descriptions, era 7 (2026-11-08).** As in "Page recordings read the
    old descriptions" (2026-11-08): the era 7 pass rewrote the long description of four era-7
    movements (the Anabaptists, the Family of Love, the St Thomas Christians under Portuguese pressure,
    the Carmelite reform), and each has a recording in `cft-website/audio/tree/`. All four now play
    text that no longer matches the page. A paid voice run, for Mark.
83. **"Held for later link passes, from era 6" (2026-11-08), era 7's part closed.** The era 7 pass drew
    `czech-churches-last-century--the-moravian-church-at-herrnhut` and removed the Waldensian union's
    Italian Methodist and Argentina-Uruguay clause for want of a source. The 1552 Chaldean line's union
    with Rome in the nineteenth century joins two era-9 movements and is held for P2-L9.
    For "'Continues as' with no graded link" (2026-11-08): eight of the nine era-7 `continuesAs`
    fields now have a matching "continued as" link. The ninth, `czech-churches-last-century` to
    `the-moravian-church-at-herrnhut`, is drawn as "gave rise to": the Renewed Unity's own history
    shows named people and a bishop passing on, not the same community carried forward.
84. **"Outcome test, adoption by vote" (2026-11-08) is closed.** Mark ruled adoption by vote minor
    (Decision-Log, "Major links: a church body adopting another's text by vote is minor",
    2026-11-08). The four era-7 outcomes stay dropped, and the Vulgate outcome on
    `hieronymian-ascetic-literary--the-tridentine-church` is removed. P2-L11 checks eras 1 to 6 for
    other outcomes of the class.
85. **No Armenian Apostolic movement for 1650-1815 (2026-11-08).** The Armenian lane runs from New
    Julfa through `armenian-christianity-era-8`, which covers the Mekhitarists and the Armenian
    Catholic patriarchate, into the Zartonk. That entry's own text treats the Apostolic Church as the
    other, larger body, so the era 8 pass drew no "continued as" link along the Armenian line. Options:
    add an era-8 Apostolic movement (the drafter's recommendation), widen this one, or accept the
    lane as it stands. Portfolio structure, for Mark. Ruled the same day (Mark: "add an era-8
    Armenian Apostolic movement"); built in its own pull request after the era 8 pass.
86. **No movement owns English Unitarianism (2026-11-08).** Essex Street Chapel (1774) and the
    English Unitarian precedent have no census movement; the corpus map marks it as needing a ruling.
    If it is ruled part of `english-old-dissent`, a Documented "influenced" link from Old Dissent to
    `early-american-unitarians-universalists` is ready to draft. The Swedenborgian summary is a bare
    dash, and its own sources record an exchange with Priestley's Unitarians (1791-92); the same
    ruling decides where that goes. For Mark.
87. **No link type for a transfer of jurisdiction (2026-11-08).** The move of the Kyiv metropolis
    under Moscow (1686) is drawn as "in contact with", with an outcome, because none of the six types
    names a change of jurisdiction. Adding a type is a method change, for Mark.
88. **The Society of Jesus ends in 1650 (2026-11-08).** `the-society-of-jesus` (era 7) runs
    1540-1650, but era 8 links to it for Pascal's letters (1656) and the suppression (1773). Each of
    those links carries a note of the mismatch. Extend the entry or add a later Jesuit movement: for
    the era 7 owner and Mark.
89. **Build wording in other eras' public text, found in era 8 (2026-11-08).** Link notes:
    `desert-monasticism--iconophile-byzantine-monasticism` ("no text we hold"),
    `palestinian-ascetic-monasticism-early--chalcedonian-monasticism-judean-desert-and-gaza`
    ("No text we hold"), `antiochene-church-third-century--antiochene-exegetical-christianity-chrysostom-ce`
    ("No source we hold"). Fields: `the-franciscan-movement` statusDescription ("sources here"),
    `greek-apologists-second-century` sourcing. Adds to "Two more out-of-era link notes use 'we
    hold'" (2026-11-08). For P2-L11.
90. **Page recordings read the old descriptions, era 8 (2026-11-08).** As in "Page recordings read
    the old descriptions" (2026-11-08): the era 8 pass rewrote the long description of
    `english-old-dissent`, `the-baptists`, `the-evangelical-awakening-in-new-england` and
    `the-moravian-church-at-herrnhut`, and each has a recording. A paid voice run, for Mark.
91. **Held for later link passes, from era 8 (2026-11-08).**
    - `the-methodist-revival` summary names Pentecostalism "through Holiness": eras 9-10.
    - The era-9 Optina movement still carries the Dostoevsky and emigre claims the era 8 pass cut
      from the Paisian revival for want of a source. Era 9.
    - `new-spain-and-andes-mission-born-christianity` has no `continuesAs`, though era 8 drew its
      "continued as" link to `colonial-latin-american-devotional-catholicism`. A data fix, era 7.
    - The era-7 Dutch and Czech movements state as fact the ties to German Pietism and the Moravians
      that era 8 qualified. Era 7.
    - `philippine-catholicism-era-8` is named "Era-8 Segment", which is build wording in public text.
      For the census owner.
92. **The rest of "Held for later link passes, from era 6" (2026-11-08) closed by era 8.** Era 7
    drew the Czech-to-Moravian link (see "'Held for later link passes, from era 6', era 7's part
    closed"). Era 8 draws `the-hesychast-revival-paisius-and-the-philokalia--the-optina-elders-and-russian-ascetic-renewal`
    (gave rise to, Documented). The Old Believers' "grew out of Muscovite Christianity" now has a
    link, era 7's `russian-church-stoglav-to-nikon--the-old-believers`, but it is "influenced"; see
    "Era 7 and era 8 typed three links differently" below. "'Continues as' with no graded link"
    (2026-11-08) now stands at 18 movements. Three are era 8's: the Paisian revival (its Optina link
    is "gave rise to"), `the-baptists`, and `armenian-christianity-era-8`, which the Armenian
    Apostolic movement re-routes.
93. **Well-known facts with no vendored source, era 8 (2026-11-08).** Added to the method question
    in "Well-known facts with no vendored source" (2026-11-07). Left as written in era 8: the Valaam
    mission to Alaska in 1794 and Herman's part in it, and the Moravian communion of 13 August 1727
    and the "choirs". The era 8 pass qualified or removed every relationship claim that lacked a
    source; these are events, not relationships.
94. **Era 7 and era 8 typed three links differently (2026-11-08).** Era 7 published first, so its
    versions stand; era 8's drafts are kept in its audit (`Final.json`, `merge_notes`). Czech
    churches to the Moravians: era 7 "gave rise to", era 8 "continued as" (Contested). Anabaptists
    and Baptists: era 7 "influenced" (Contested), era 8 "in contact with" (Documented, Smyth's
    application to the Waterlanders). The Russian church before Nikon to the Old Believers: era 7
    "influenced", era 8 "gave rise to" (Documented); the Old Believers' summary says "grew out of".
    For P2-L11.
95. **The Armenian line after the new movement (2026-11-08).** Era 7 drew
    `armenian-christianity-new-julfa--armenian-christianity-era-8` (continued as) on the line of
    Apostolic catholicoi. Once the Armenian Apostolic movement is added, that evidence belongs to it:
    the follow-up retires the link with a replacement to the new movement.
96. **Well-known facts with no vendored source, era 9 part 1 (2026-11-08).** Added to the method
    question in "Well-known facts with no vendored source" (2026-11-07). Left standing as written: the
    Primitive Methodists and AME Zion, the 1844 Methodist split, Keswick, Spurgeon's Tabernacle, the
    slavery cause of the 1845 Baptist split, Landmarkism, the 1832 Stone-Campbell union, the
    Victorian Church of England's Gorham case, Essays and Reviews and first Lambeth Conference, the
    New Apostolic Church's size, Newman's 2019 canonization, the Quaker Nobel Prize of 1947.
97. **Page recordings read old descriptions, era 9 part 1 (2026-11-08).** As in "Page recordings
    read the old descriptions" (2026-11-08): four recorded pages now play a description this pass
    rewrote: `the-haugean-awakening`, `the-reveil-and-inner-mission-awakening`,
    `confessional-lutheran-revival-emigrations`, `russian-evangelicals-stundists`. A paid voice run,
    for Mark.
98. **Era 7's St Thomas link into the Northeast India churches (2026-11-08).** Era 7 published
    `st-thomas-christians-under-portuguese-pressure-d--northeast-india-revivals-and-the-mar-thoma-refor`
    (continued as, Widely Accepted), resting on Malankara documents. Its era-7 text no longer names
    Northeast India. The era-9 movement joins two different bodies: the Mar Thoma reform, which does
    descend from the St Thomas Christians, and the northeast hill churches, which came from Welsh and
    American missions. Whether "continued as" fits the whole movement is for P2-L11.
99. **Text owners' items from era 9 part 1 (2026-11-08).** Not changed, because no vendored text
    settles them or another entry owns them:
    - `the-chinese-church-indigenous-and-suffering` (era 10) says its churches "owed nothing to the
      foreign missions"; era 9 now draws a "gave rise to" link from the mission churches to it.
    - `the-student-volunteer-movement-and-edinburgh-191` has `continuesAs` pointing to the ecumenical
      entry; its link is "gave rise to", and it did not itself become that body.
    - `the-sunday-school-and-bible-institute-movement` legacy: "graded" lessons of the 1870s; the 1872
      series was uniform.
    - `russian-evangelicals-stundists` story: the place of the 1884 Baptist meeting ("in the
      Caucasus") is unchecked.
    - `victorian-church-of-england` has no source list at all.
    - `the-baptists` (era 8) legacy: Carey's society "opened the era of Protestant foreign missions";
      Carey's own Enquiry (vendored, lines 798-799) gives the Moravians first place.
    - `dispensational-prophecy-culture` (era 10) says it "grew out of" Brethren teaching; the era 9
      link is "influenced".
100. **Two possible links that no text names, era 9 part 1 (2026-11-08).** Kuyper's 1891 edition of
    Voetius's catechism lectures (a possible Dutch Further Reformation influence on Dutch
    neo-Calvinism) and Conybeare tracing Stundism to Spener's Pietism (lines 14615-14621). Not
    drafted: no movement text names them.
101. **Era 8 and era 9 drew the same Methodist link (2026-11-08).** Era 8 published
    `the-methodist-revival--nineteenth-century-methodism` (continued as, Widely Accepted) before era 9
    part 1 merged, so it stands and era 9's draft was set aside. Era 9's draft was Documented: the
    1862 reprint of the Methodist Conference minutes says the yearly minutes had come out in an
    unbroken series from 1765 (era 9 part 1 drafting record). A possible upgrade, for P2-L11.
102. **"No Armenian Apostolic movement for 1650-1815" and "The Armenian line after the new
    movement" are closed (2026-11-08).** Mark ruled to add the movement. `armenian-apostolic-church-era-8`
    (VII.24a) now carries the Apostolic line from New Julfa to the Zartonk, and era 7's New Julfa
    link to the Mekhitarist movement is retired with a replacement. Audit:
    `Build/Ministry/Operations/Audits/2026-11-08_armenian-apostolic-era-8/`.
103. **The Armenian Apostolic movement's library bucket (2026-11-08).** `cic/corpus-map/` has no
    `armenian-apostolic-church-era-8.yaml`. The Apostolic works now under
    `armenian-christianity-era-8` (Ormanian, Chamich's Part VII, Zakaria and Abraham of Crete,
    Rycaut) belong with it, through their `_staging` files. Abraham of Crete's row also says he
    attended Nadir Shah's accession; in his own chapters 43-44 he left before it and heard of it
    afterward. For the Library thread.
104. **The new movement and the map's own list (2026-11-08).** Like the eight movements added since
    the map was built, `armenian-apostolic-church-era-8` has a tree page but no record in the map's
    embedded movement list, which `atlas-sync` only updates and never adds to. For the map's owner.

