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
    - 2026-11-08: the Cathar link is now on `balkan-bogomil-continuation` only; the one on
      `bogomils` is retired (Decision-Log, "Whole-set rulings"). The entries' overlap stays open.
    - 2026-11-08: closed. Split by date: `bogomils` covers c. 950–1054 and hands the rest to
      `balkan-bogomil-continuation` (Decision-Log, "The two Bogomil entries are split by date"; data release 21).
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
102. **The Philippine Independent Church has no entry (2026-11-08).** It broke from Rome in 1902 and
    still exists, but it sits inside `philippine-catholicism-gomburza-to-aglipay`. The era 9 pass
    drew no "broke with" link, since a body cannot break with an entry that contains it. Whether it
    needs its own entry is a portfolio question for Mark.
103. **Coptic and Ethiopian map gaps (2026-11-08).** No Coptic movement sits between
    `coptic-christianity-fatimid-to-mamluk` (to about 1300) and `coptic-revival-under-cyril-iv`
    (from 1854); the era 9 "continued as" link spans the gap at Dominant Modern Reconstruction, on
    modern lists of patriarchs. No Ethiopian movement sits between 1650 and 1855; not bridged.
    Portfolio layout, for Mark.
104. **Optina's continuesAs (2026-11-08).** `the-optina-elders-and-russian-ascetic-renewal` points
    its `continuesAs` at the whole Russian Church under Soviet rule, while
    `russian-church-synodal-century` has none of its own. The era 9 link follows the field at
    Inferential-Thin. A layout question for the census owner.
105. **Optina's émigré claim is stated as fact (2026-11-08).** The Optina summary and legacy say its
    spirituality "carried forward" into émigré theology in Paris; the link drawn for it is
    Inferential-Thin, and era 8 cut the same claim from the Paisian revival for want of a source
    ("Held for later link passes, from era 8", 2026-11-08). The era 9 part 2 cap was used before
    this was weighed. For P2-L11. The Dostoevsky visit of 1878 rests on repo-cited secondaries
    (Dunlop 1972, Stanton 1995) and stands.
106. **A floor question on the Universalists (2026-11-08).** The floor note and status line of
    `american-unitarianism-universalism-consolidations` call the Universalists "arguably
    floor-clean" and say much of it "would sit comfortably inside Nicene bounds". The vendored 1903
    Universalist centennial volume calls them Unitarian in their doctrine of God. The status line
    also prints an internal atlas code. For Mark.
107. **Well-known facts with no vendored source, era 9 part 2 (2026-11-08).** Added to the method
    question in "Well-known facts with no vendored source" (2026-11-07): the 1850 English hierarchy,
    the US immigrant church, Rerum Novarum, Mexico's Reform laws, Rome's slow recognition of the
    Latin American republics.
108. **Page recordings read old descriptions, era 9 part 2 (2026-11-08).** As in "Page recordings
    read the old descriptions" (2026-11-08): six recorded pages now play a description this pass
    rewrote: `the-optina-elders-and-russian-ascetic-renewal`, `jehovah-s-witnesses-bible-students`,
    `orthodoxy-after-1821-balkan-autocephalies`, `american-unitarianism-universalism-consolidations`,
    `ruthenian-greek-catholic-polotsk-to-galicia`, `ethiopian-christianity-tewodros-to-menelik`. A
    paid voice run, for Mark.
109. **Text owners' items from era 9 part 2 (2026-11-08).** Not changed in a links pass:
    - `alaskan-mission-herman-veniaminov` summary: "Tlingit alphabets" may overstate; the
      description and why name only the Aleut alphabet.
    - `oneida-community` dates the dissolution to 1880, 1881 or both in different fields.
    - Sentence fragments: `catholic-church-long-nineteenth-century`, `old-catholic-churches-union-of-utrecht`,
      `oneida-community` and `christadelphians` descriptions; the Unitarian-Universalist legacy.
    - The placeholder "-" as relations summary: `latter-day-saints-lds`,
      `jehovah-s-witnesses-bible-students`, `christadelphians`, `christian-science`,
      `oneida-community`, `spiritualism-new-thought`.
110. **Possible links that no text names, era 9 part 2 (2026-11-08).** Not drafted: the Urmia
    Assyrians' 1896 submission to the Russian church (Wigram 1929); John Thomas's years in the
    Stone-Campbell movement; Russell and the Adventists; Eddy and Quimby.
111. **"No Armenian Apostolic movement for 1650-1815" and "The Armenian line after the new
    movement" are closed (2026-11-08).** Mark ruled to add the movement. `armenian-apostolic-church-era-8`
    (VII.24a) now carries the Apostolic line from New Julfa to the Zartonk, and era 7's New Julfa
    link to the Mekhitarist movement is retired with a replacement. Audit:
    `Build/Ministry/Operations/Audits/2026-11-08_armenian-apostolic-era-8/`.
112. **The Armenian Apostolic movement's library bucket (2026-11-08).** `cic/corpus-map/` has no
    `armenian-apostolic-church-era-8.yaml`. The Apostolic works now under
    `armenian-christianity-era-8` (Ormanian, Chamich's Part VII, Zakaria and Abraham of Crete,
    Rycaut) belong with it, through their `_staging` files. Abraham of Crete's row also says he
    attended Nadir Shah's accession; in his own chapters 43-44 he left before it and heard of it
    afterward. For the Library thread.
113. **The new movement and the map's own list (2026-11-08).** Like the eight movements added since
    the map was built, `armenian-apostolic-church-era-8` has a tree page but no record in the map's
    embedded movement list, which `atlas-sync` only updates and never adds to. For the map's owner.

114. **Four whole-set rulings for Mark, eras 1 to 9 (2026-11-08).** The whole-set review held
    them; each is a reading of a method rule. (a) A link resting only on one 19th- or early-20th-century
    account is Dominant Modern Reconstruction in 10 links and Inferential-Thin in 4. (b) What
    `verified-direct` means, and whether a vendored secondary source may carry file, lines and quote;
    six secondary-only links are marked A and verified-direct with nothing behind them. (c) A bishop
    deposed by a ruler with no council named is major in era 3, minor in era 8. (d) The Bogomil-to-Cathar
    link is drawn from both Bogomil entries (see "The Bogomil entries overlap", 2026-11-08). Audit:
    `Build/Ministry/Operations/Audits/2026-11-08_links-whole-set-review/`.
    - 2026-11-08: closed. Mark ruled on all four, as five rulings (Decision-Log, "Whole-set
      rulings"); applied in data release 19. Audit: `Build/Ministry/Operations/Audits/2026-11-08_whole-set-rulings/`.
115. **Census owner's items from the whole-set review (2026-11-08).** Movement fields, not links:
    - Six `continuesAs` fields name a successor the links type as "influenced" or "gave rise to"
      (Carolingian to the Gregorian papacy, Cyrillo-Methodian to Kievan Rus', Athonite to the
      Palamite synthesis, the Czech churches to Herrnhut, Paisius to Optina, Edinburgh 1910 to the
      WCC). 21 "continued as" links start at a movement with no `continuesAs`.
      `armenian-christianity-after-avarayr` points past the movement between it and the Bagratids.
    - `the-old-believers` summary says they "grew out of Muscovite Christianity"; the restored
      link runs from the Russian church before Nikon's reforms.
    - The Anomoean summary says the council of 381 "formally cursed" that party; the links say
      "condemned".
    - House punctuation in link notes: single and double quote marks both in use, and the full
      stop both inside and outside the closing mark.
116. **No entry for the Malankara church, 1665-1912 (2026-11-08).** The era 7 St Thomas Christians
    link into era 9 is now "gave rise to": the era 9 entry also holds the Northeast India hill
    churches. No movement carries the larger body between the Coonan Cross and 1912. A census
    question for Mark.
117. **The era 6 open questions are ruled (2026-11-08).** Mark ruled on all seven (Decision-Log,
    "Rulings on the era 6 open questions", 2026-11-08). Carried out in
    `Build/Ministry/Operations/Audits/2026-11-08_era-6-rulings/`, data release 18. This closes:
    - "The Church of the East's 'Hakkari' name" (2026-11-08): renamed "…and the Northern Remnant";
      the informal name, region, place label and the 1552 schism's status line follow.
    - "No link type for church jurisdiction" and "No link type for an authority's acts on another
      body's own order" (both 2026-11-08): drawn as "in contact with", with an outcome where the
      link's own sources show the act. Two links re-typed from "influenced", four authority links added
      (among them Leo X's division of the Franciscans and the papal acts on the Observants), and
      outcomes set on three existing "in contact with" links.
    - "The Council of Basel sits under the papacy" (2026-11-08): stays as it is.
    - "The inquisition-record sects and the Free Spirit overlap" (2026-11-08): split by evidence.
      `latin-papal-church-avignon-to-lateran-v--inquisition-record-sects-adamites-and-kin` is
      retired into the papal church's link to the Free Spirit, which now carries the 1367 case.
    - "Well-known facts with no vendored source" (2026-11-07) and its era 5 and era 6 additions
      (2026-11-08): plain facts stand with their wanted text listed; 18 guarded facts were sourced
      or restated as reported, Breslau among them.
    - "Page recordings read the old descriptions" (2026-11-08) and its era 6 and era 7 entries:
      each recording now carries a fingerprint of its text, and a page whose text changed hides its
      player. 143 recordings were stale when the fingerprints were written. The paid re-voicing
      batch runs once, after the era 9 links pass (see the next entry).
118. **One paid re-voicing batch after era 9 (2026-11-08).** Per ruling 7: every recording whose
    fingerprint no longer matches its page is re-voiced in one batch after the P2-L9 merge. Sample
    first, Mark's approval by ear, every setting passed and printed. Until then those pages show no
    Listen player. For Mark, when era 9 merges.
119. **The Carthusians after 1300 go to the new-entries batch (2026-11-08).** Per ruling 4, a later
    Carthusian movement, split by era as the Waldensians were, is made in the agreed-entries release
    (P2-G3). It is already candidate 23 in the gap sweep
    (`Build/Ministry/Operations/Audits/2026-11-08_tree-gap-sweep/`). Until then the English mystics
    text states the Carthusian copying of The Cloud and the Scale with no link.
120. **Wanted texts from the era 6 rulings (2026-11-08).** Leo X's Ite vos (1517) in a vendored
    edition; Martin V's bulls on the Observants and the full Constance decree; a source for the
    Allied bombing of Monte Cassino (1944); Lea, Inquisition of the Middle Ages, vol. II, p. 549
    (Capistrano at Breslau). The full list is in the audit README.
121. **"One paid re-voicing batch after era 9" (2026-11-08) is closed.** All 155 stale tree
    recordings were re-voiced (3 in the sample, 152 in the run); none is stale now. Decision-Log,
    "Tree pages re-voiced after era 9", 2026-11-08.
122. **Seven links wait for a modern study (2026-11-08).** Graded Inferential-Thin because no modern
    study is cited in the repo for their reading (Decision-Log, "Dominant links on two or three old
    accounts"). Any of them can go back to Dominant Modern Reconstruction once its study is read and
    cited. The list, with the study each needs: `Build/Ministry/Operations/Audits/2026-11-08_old-account-links/README.md`.
123. **The Bogomils page needs re-voicing (2026-11-08).** Its description changed in data release 21,
    so its recording no longer matches and the Listen button is hidden. It joins the next paid
    re-voicing batch: sample first, approved by ear, every setting passed and printed.
124. **IX.16 still describes Iglesia ni Cristo after the split (2026-11-08).** Data release 21 adds
    `iglesia-ni-cristo` (IX.51) under G-14, but the era 10 edits carry no IX.16 text that takes
    Iglesia ni Cristo out. Its name, shortName ("Iglesia ni Cristo"), teaser, why, longDescription,
    floorNote, legacy, voices and first source still name it, and its statusDescription still calls
    the split "a real, open question, not yet acted on". The three-body text is drafted and reviewed
    in P2-E10b. IX.16's id stays as published.
125. **Iglesia ni Cristo row: fields not in the draft (2026-11-08).** D-E1 drafted no `placeLabel`,
    `modernCountries`, `regions`, `sources`, `longDescription`, `teaser`, `voices`, `legacy` or
    `documentedStories`. Release 21 takes each from IX.16's own copy: its Philippines place and
    country, "Greater Asia", its Iglesia ni Cristo source and "CHC vol. 9", its two Iglesia ni Cristo
    voices, D-E1's `why` as the description, its legacy sentences on the successions and counts, and
    a teaser cut from its teaser's words. The row still needs one link toward Philippine Catholicism
    (VIII.39), for P2-L10. For review in P2-E10b.
126. **IX.31's old page and its place on the map (2026-11-08).** IX.31 is retired with no redirect
    (G-8 (a)). The page generator does not remove pages, so `cft-website/tree/deconstruction-and-ex-vangelical-communities.html`
    still serves the old entry, and the map's embedded list still draws it (`atlas-sync` never
    removes). What the old address serves (the old page, a short "retired" page, or nothing) is
    for Mark.
127. **Recordings made stale by the era 10 census pass (data release 22) (2026-11-08).** No paid run was made. Tree pages:
    36 era 10 recordings no longer match their text, so their pages and map cards hide the Listen
    player; Iglesia ni Cristo has none; IX.31's recording is left with no movement. Documented
    stories: 25 more recordings no longer match their text. Two now sit under the wrong story,
    because the map plays a story's recording by its position, without a fingerprint check:
    IX.16's first story ("Two Thousand Couples and a Tax Trial") would play the recording of the
    removed "The Apostle Pleads Guilty", and New Calvinism's first ("The Sunday After") the
    removed "The Year Mars Hill Came Apart". These two must be dealt with before the release
    reaches the live site. Re-voicing is a paid batch: sample first, Mark's approval by ear.
128. **The `kind` field on the era 10 rows, IX.57 included (2026-11-08).** P2-E10b carries the
    question of whether the field fits the new rows, in `_meta.kind` of the proposal. P2-E10c
    rules on the field. Owner: the P2-E10c thread.
129. **Pueblo and the arena in IX.58 (2026-11-08).** "From Boulder" was dropped as untraced. Pueblo and
    the arena are traced to E2's article only as the Movements review (Round 1, M-12) read it.
    The item text for E2 in `CiC_Step0_Era10_Movements_V1_0.md` should record them from the
    article itself. Owner: the Movements record's thread.
130. **IX.53, faith missions, held (2026-11-08).** The row is held out of data release 22: no
    carrier's statement of faith was found, so Section A cannot be assessed. The line named in
    G-56(a), Wycliffe in IX.53, is held with it. Two items are wanted: a carrier's dated
    statement of faith, and the Round 1 fixes (M5 E4) carried in the held note. The hold waits on
    Mark: hold the row, or build it under G-57(a) with a "not yet assessed" floorNote
    (Round 2, S2-2). If built, `totalEntries` is 308 and Pre-Survey Candidate 226.
131. **A dated copy of the Vineyard statement of faith (2026-11-08).** The IX.57 floorNote dates
    the board's adoption to November 1994 from copies published by others (bible.ca,
    religionfacts). The Vineyard publisher's own dated copy is wanted; the 2002 and 2009 captures
    are the leads.
132. **An earlier date for the IX.54 statement of faith (2026-11-08).** The only copy seen is
    Citygate Network's live page, undated, earliest capture 2025. The 2012 capture of
    agrm.org/agrm/Statement_of_Faith.asp, contents unseen, is the lead for an earlier date.
133. **The wrong-story playback in entry 127 is closed by the map's fingerprint check (2026-11-08).**
    The map now plays a documented-story recording only when the SHA-256 fingerprint of the story
    text it shows matches the manifest's `hash`, using the same fingerprint as the generator
    (commit "Map: play a documented-story recording only when its fingerprint matches the story
    text shown"). The two shifted recordings in entry 127 are hidden, not misplayed. Still open:
    264 story recordings and 36 tree recordings no longer match their text and stay hidden until
    re-voiced. About 242 of the story recordings were already mismatched before this work, and the
    live site, which lacks this check, may still be playing them under changed text until this
    reaches `live`. Re-voicing is a paid batch: sample first, Mark's approval by ear. Owner: Mark,
    with the narration thread.
134. **The gap sweep is ruled (2026-11-09).** Mark ruled on the P2-G1 list (Decision-Log, "The gap
    sweep ruled (P2-G1)", 2026-11-09). The entries are built in P2-G2 and P2-G3. This settles:
    - "No entry for the church of Alexandria, 4th-5th century" and "Two Egyptian Miaphysite entries
      from the same year" (both 2026-11-07): I.14 is retired into II.1, which starts with
      Athanasius (328) and runs across the era line.
    - "Irenaeus has no movement of his own" and "Augustine has no movement of his own" (both
      2026-11-07): each gets a person entry, Irenaeus told within the household churches, Augustine
      within `latin-pastoral-congregational-christianity`, whose text is corrected to match its Doc_01.
    - "Which entry owns an emperor's act against the Nicenes, 337-378" (2026-11-07): each link stays
      on its own sources; the method page states the convention.
    - "The two early Persian entries overlap" (2026-11-07): `persian-church-of-the-east-early` ends
      at the synod of 424, where the evidence marks the change.
    - "Ambrose's Milan and the imperial church overlap" (2026-11-07): both stay; Ambrose also gets a
      person mark.
    - "Caucasian Albania's end date" (2026-11-07): the span follows the vendored histories
      (Brosset 1876, Ormanian 1912), and the Bagratid "absorbs … after 705" goes. The entry's owner
      sets the years from them.
    - "No link type for communion" (2026-11-07): no new type before launch; the method page says
      how communion is drawn.
    - "Two 'continues as' fields name entries the evidence only influenced" (2026-11-08): both are
      cleared.
    - "Links the sources support but no text names" (2026-11-08): the Alcuin link is drawn; the
      Salzburg and Cluny links wait for a reading.
    - "Long-gap links to modern churches" (2026-11-08): not drawn; the gap shows as a dashed thread.
    - "No movement for the Bulgarian church of the Second Empire" (2026-11-08): stays inside
      `serbian-and-bulgarian-medieval-monasticism`.
    - "No medieval English or Scandinavian successor entry", "No Melkite entry between 1009 and
      1724" and "No Syriac Orthodox movement after 1300" (all 2026-11-08): held as named gaps until
      the Library holds a voice for each period (see the next entry).
    - "Dominant Modern Reconstruction on old secondary works" (2026-11-08): settled by the earlier
      "Whole-set rulings" and "Dominant links on two or three old accounts" (2026-11-08), which
      stand.
    - "No Carthusian movement after 1300" (2026-11-08): a later Carthusian movement is made in
      P2-G3, per the era 6 rulings (2026-11-08).
135. **Gaps held for sources (2026-11-09).** Under principle 3 of the sweep ruling, each of these is a
    real census gap with no voice in the Library for its period. Each shows as a dashed thread and
    is built when its texts are vendored. For the source-research thread:
    - the medieval English church, 1066 to about 1330 (wanted: Anselm, Eadmer, Becket's letters,
      the chroniclers);
    - the medieval Scandinavian church after 1104;
    - the Melkites, 1009 to 1724;
    - the Syriac Orthodox church after 1300 (the Chronicon of Bar Hebraeus, vol. 3, carries a
      continued list of maphrians dated 1317 to 1369; vol. 2 is not vendored);
    - the Scottish church after 1650 (Library texts stop at 1654 and Rutherford's letters at 1661);
    - the Swedenborgian New Church after 1815 (wanted: the Boston New Jerusalem Magazine, the
      General Convention's liturgies);
    - the Old Believers after 1815, with the Belokrinitsa hierarchy (1846).
136. **What P2-G2 leaves for P2-G3 (2026-11-09).** Data release 24 retired I.14 into II.1 and made
    Tertullian a person entry (Decision-Log, "The gap sweep ruled (P2-G1)", 2026-11-09). Left open:
    - II.1's dates and text still run from 451. Extending it to 328, with Athanasius, is P2-G3's
      content work. I.14's own content (its three documented stories, from Ephesus 431 on, its voices
      line for Cyril, its places to visit) left the census with it. It stands in release 23 for
      P2-G3 to draw on. Its recordings are in `Archive/Superseded-Site-Pages/retired-tree-audio/`.
    - The "gave rise to" link from the desert monks, re-made on II.1 as
      `desert-monasticism--cyrilline-miaphysite-egyptian-christianity--2`, is true while II.1 starts
      in 451. Once II.1 starts in 328, the church of Alexandria is older than the desert monks. P2-G3
      re-checks the link beside the "influenced" link on the same pair.
    - The Library row for Theophilus of Alexandria (`npnf214_seven-ecumenical-councils`) says he falls
      in the gap between the catechetical school (to 400) and II.1 (from 451). Once II.1 starts in
      328, the row may move to II.1. Owner: the Library thread.
    - The people rows hold only person entries so far: Tertullian, in the Latin Apologists' row.
      P2-G3 adds the named voices. The Latin Apologists' first voices line is Tertullian himself, so
      that row must not list him twice.
    - Four links name Tertullian in their notes but do not touch his entry:
      `greek-apologists-second-century--latin-apologists`,
      `post-apostolic-house-church--marcion-marcionism`,
      `post-apostolic-house-church--valentinian-and-other-gnostic-christianities` and
      `greek-apologists-second-century--valentinian-and-other-gnostic-christianities`. `concerns` is
      left off them. Whether each is about him is P2-G3's reading.
    - Tertullian's entry is still called "Tertullian's Voice", which reads as a label now that the
      page is headed "About This Person". The ID stays. Renaming the display name is P2-G3's call.
    - A named voice backed by `source` must quote the person's own words. The validator checks that
      the quote is verbatim, but not whose words it is. When P2-G3 fills the rows, a reviewer confirms
      the speaker of each quote.
137. **176 story recordings wait for the ElevenLabs quota to reset (2026-11-09).** The paid run Mark
    approved re-voiced 85 of 261 stale story recordings (51,653 credits) and stopped when the
    account's 121,000-credit quota was used up. Mark ruled: "wait for the quota reset", with no
    top-up and no overage. When the quota resets, run the same command with the same settings (voice
    onegjDE2z0mQtp1g0HK7, model eleven_v4, mp3_44100_64; approved run "Era 10 re-voice, full story
    batch (Mark approved sample 2026-11-09)"). It skips what is current and makes the 176 left
    (252,306 characters). Until then the map's fingerprint check keeps them hidden. The tree's own 36
    stale recordings use other voices and get their own sample first. Owner: this thread, at the
    reset.
138. **Three areas the era 10 global sweep did not reach (2026-11-09).** After Round 1 and its
    supplementary pass, the era 10 global completeness sweep
    (`Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_GlobalSweep_V1_0.md`,
    section 2, "Not swept") still has not swept three areas, in any river:
    - the Hispanic Caribbean's Protestants (Puerto Rico, the Dominican Republic);
    - the Armenian Evangelical churches of the Near East (their union of 1924 is [S]);
    - the migrant churches of the Gulf.
    Each needs its own pass under the sweep's rules before the gate can say the era is global.
    Owner: the sweep thread.
139. **Lines the global sweep's ruling placed but no verified item yet carries (2026-11-09).** The
    era 10 global sweep gate ruled these lines in. P2-E10h (data release 25) held each one, because
    its evidence is still [S], snippet-only or V-s. Each enters when its item is opened and verified.
    Owner: the source-research thread. The record is
    `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10h_Proposed.json`,
    `notes`.
    - **Africa:**
      - Shembe, Legio Maria (with its open A1 question), Chilembwe and Toko (C12);
      - Milingo and Sant'Egidio in IX.59;
      - the TRC faith-community hearings in IX.60's legacy (G-81 a);
      - the Church of Pentecost in IX.11 (G-84 a);
      - the Sudanese Presbyterian church and the Dinka hymns in IX.61;
      - a dated item for the expulsion order of 27 February 1964.
    - **Latin America:** the SIL line in IX.63. Its role is contested, and it needs the SIL's own
      account beside Stoll's (G-142 a).
    - **Asia:**
      - Minjung theology, the March First Movement and the growth decades in IX.64;
      - Timor-Leste in IX.37 (G-115 a);
      - the Japanese Orthodox Church after 1906 (G-121 a);
      - the Uniting Church in Australia and Hillsong (G-116 a);
      - El Shaddai's founder and founding date. Its line in IX.66 names neither until Wiegele is
        opened at the page that dates it.
    - **Eastern Europe and the Middle East:**
      - Ukrainian autocephaly in IX.69 (G-130 b);
      - the Chaldean Church in IX.19 (G-131 a);
      - the Christian Peace Conference in IX.46;
      - Mukachevo in IX.21 (G-129 a);
      - the deported Catholics and Lutherans cross-reference in IX.69 (G-148 a).
    - **Waiting for a row:** the lines that go into GS-A2 (G-104 a, G-117 a, G-147 a) and E4 (G-148 a)
      wait for those rows, which are "enter once". The Pará story moves out of IX.11 only when LA-2
      enters (G-91 a, G-132 b).
140. **Open points left by P2-E10h (2026-11-09).**
    - **IX.44 lists Peru as its only modern country.** The validator allows a country only if its
      place is on the place label, so the United States cannot be added without changing the label
      ("N. America · Peru and beyond"). Owner: Mark's call, through the next census pass on IX.44.
    - **Map self-reference in older rows.** "This map …" sentences remain in IX.4, IX.7, IX.11, IX.44,
      IX.46, IX.19 and IX.22. The live-commentary check does not flag them, and the same wording
      runs across many rows outside this release. Whether participant copy may name "the map" is a
      fleet-level style call. Owner: Mark.
    - **IX.11 calls the Lausanne critiques "within the same Pentecostal family".** Lausanne is a
      wider evangelical network. Owner: a later IX.11 pass.
    - **The new rows have no lineage links.** Their parents sit in frozen eras 8 and 9. The
      candidates are:
      - VIII.31 → IX.69
      - VIII.28 → IX.71 and IX.72
      - VIII.12 → IX.72
      - VIII.48 → IX.62
      - IX.62 → IX.8
      - VIII.43 → IX.59
      Owner: P2-L10.
    - **On the map, a lane's first dot sits at the lane's own place, and its river curves in from the
      parent lane over the next stretch.** The new 4.5 lane shows this at 1906: "Catholics in
      Africa" sits a little above where its river arrives. Every lane born from a parent is drawn
      this way. Owner: Mark's call on whether to change it.
141. **IX.48, American Orthodoxy, lists no modern country (2026-11-10).** Its place label reads
    "North America", not "N. America", so the change order of 2026-11-10 (modern countries from each
    row's own text, Mark's option c) did not reach it. Its country list stays empty, as the "N.
    America" rows' lists were before. Whether the same rule applies to rows labeled "North America"
    is Mark's call. Found by the Round 1 review of the N. America countries proposal (M-4).
142. **Breaks in the timeline: churches that drop out between entries (2026-11-10).** Found by a scan
    of data release 25 for years where a tradition has no entry. Mark ruled to log them, not sweep
    them now (option c). He also asked that each be checked as unique, not a story another entry
    already tells, as the Jesuits' worldwide work is one movement. Each break below was checked
    against every row whose dates overlap it, by name, place and text. None is carried by another
    entry. Each is a real gap in a frozen era, so filling it is a change order and needs its sources
    found first.
    - **Ethiopian church, 1650 to 1855.** VI.25 ends at Fasilides (1650) and VIII.49 starts at
      Tewodros (1855). The Gondar period and the Zemene Mesafint have no entry. VIII.13 names
      Ethiopia only for Cyril IV's mission there in the 1850s. Tied to the next item: the Ethiopian
      church took its bishop from the Coptic patriarch.
    - **Coptic church, 1517 to 1854.** No entry carries the Copts before Cyril IV (VIII.13). VI.18
      names a Coptic patriarch only in passing.
    - **Church of the East, 1650 to 1815.** VI.30 (the schism of 1552) ends in 1650 and VIII.40 starts
      in 1815. This is the Syriac East river's only break.
    - **St Thomas Christians of India, 1665 to 1815.** VI.18 ends after the Coonan Cross (1653). The
      Halle and Moravian rows (VII.2, VII.4) and VIII.7 name India for Protestant missions only, not
      this church.
    - **Armenian church, 1441 to 1517.** V.21 ends with Etchmiadzin's restoration (1441) and VI.28
      starts at the era line (1517). This is likely an era-boundary slip, not a missing story. Its
      fix may be a date change on one of the two rows.
    - **Georgian church, 1245 to 1660.** IV.15 ends in 1245, and nothing names the Georgian church
      again until VII.20 at 1660 (which is the Church of England's "Georgian" era, not Georgia).
      The Georgian church has no entry after 1245.
    - **Catholic missions in China, 1650 to 1793, and the Chinese Rites controversy.** VI.11 (the
      Society of Jesus) and VI.13c (Ming China) both end in 1650. VII.19 tells the Jesuits'
      suppression of 1773 only as a European story. VIII.21 names Beijing only as where Yi Sung-hun
      was baptized (1784). Tied to the Jesuits, so it may be best told as the Society of Jesus's
      era 7 continuation, not as a separate Chinese row.
    - **Japan's hidden Christians, 1650 to 1865.** VI.13b ends in 1650 and VIII.45 starts at their
      discovery in 1865. They kept the faith without priests, so this is their own story, not the
      Jesuits'.
    - **Maronite church, 1517 to 1900.** V.22 ends at 1517. VII.23 names the Maronites only as an
      earlier union with Rome, so they have no entry for four centuries.
    - **Greek Catholics of Galicia, 1906 to 1946 (Sheptytsky's church).** VIII.38 ends in 1906 and
      IX.21 starts in 1946. IX.70 says these churches are "a separate line", and none carries them
      between the wars.
    Also thin, though not empty: Latin America, 1492 to 1900, has three entries for four centuries
    (VI.13d, VII.17, VIII.48). The 48 era 10 rows with no link from an earlier entry wait for P2-L10.
    Owner: the eras 8 and 9 sweep (P2-G89), or a later timeline pass, once Mark rules on the scope.
143. **What grade a "member of" link takes on the council's own record alone (2026-11-10).** The
    World Council of Churches' own pages give 1948 as the year both the Ecumenical Patriarchate and
    the Church of Greece joined. A "member of" link from the Greek church (part 2 of P2-L10) would
    rest on that record alone. Under the method brief, Widely Accepted needs a secondary work as
    well, so with no study cited the link would be Inferential-Thin. That is a thin grade for a
    council's own membership roll. Whether a council's own dated membership record may carry
    Widely Accepted alone is a method question for Mark, to rule before part 2 drafts its
    "member of" links. Found by the part 1 revision and the Round 2 review.
144. **The 1904-07 revival entry calls the three revivals "unconnected" (2026-11-10).** The entry
    `the-1904-07-revival-family-wales-mukti-india-pyo` says, in its longDescription, why and
    legacy, that the Welsh, Mukti and Pyongyang revivals were unconnected and that none descended
    from another. Helen S. Dyer's life of Pandita Ramabai (1913 edition) says news of the Welsh
    revival led to a new prayer circle at Mukti in January 1905, and that news from the Welsh
    missions in the Assam hills encouraged it. The fix runs through three fields, so under the
    link method it is left for the entry's owner, not rewritten in P2-L10. The claim that none of
    the three came from Azusa Street still holds. Found by the part 1 drafters (group D) and
    confirmed by Round 1.
145. **Five tree-page recordings read old descriptions after P2-L10 part 1 (2026-11-10).** Data
    release 27 rewrote the longDescription of five movements with tree recordings:
    - `global-south-pentecostal-christianity`
    - `hebrew-roots-and-torah-observance-movements`
    - `ratana-church-and-pacific-adjustment-movements`
    - `the-chinese-church-indigenous-and-suffering`
    - `the-ecumenical-movement-and-the-wcc`

    Their recordings in `cft-website/audio/tree/` still read the old text. Re-voicing them is a paid
    run. It joins the tree's other stale recordings, which get their own sample for Mark first (see
    "176 story recordings wait for the ElevenLabs quota to reset", 2026-11-09). Owner: this thread,
    on Mark's approval.
146. **Open-Gaps 143 is settled (2026-11-10).** Mark ruled that a "member of" link may be Widely
    Accepted on the council's or member church's own dated membership record alone. See the
    Decision-Log, "A 'member of' link may be Widely Accepted on the membership record alone".

147. **The Sayfo entry says Syriac history "had gone quiet after about 1300" (2026-11-10).** The
    entry for the Syriac churches from 1915 (atlasId IX.19) says, in its relationsSummary and legacy,
    that Syriac recorded history "had gone quiet after about 1300". It also says Syriac
    communities experienced that silence "as erasure", and uses map wording ("named honestly
    here"; "On this map the entry does one more thing").
    - The Church of the East wing the entry covers has its own entries (V.17, VI.30, VIII.40) and an
      existing "continued as" link, so the first claim does not hold for it. It holds only for the
      Syriac Orthodox side, which Open-Gaps 135 already lists as a held gap after 1300.
    - No source supports the claim about what communities experienced.
    - The fix spans two fields, so under the link method it is left for the entry's owner, not
      rewritten in P2-L10. Found by the part 2 drafters (group G).
148. **Joint declarations between churches, and no entry for Rome after 1962 (2026-11-10).** The
    part 2 drafters of P2-L10 (group G) read two joint declarations online, on vatican.va:
    - Paul VI and Athenagoras I, 7 December 1965;
    - John Paul II and Mar Dinkha IV, the Common Christological Declaration of 1994.

    Each shows contact between two churches directly, in both churches' own names. Two things stop
    a link:
    - **A method question for Mark.** Under the method, Widely Accepted needs a study as well, so
      a link resting on a joint declaration alone could not reach it. Mark ruled that a membership
      roll alone may carry a "member of" link. Should a joint declaration alone carry an "in
      contact with" link the same way?
    - **No endpoint.** The census has no entry for the Roman Catholic Church after 1962. The Pius X
      entry ends at the Council, and the post-Vatican II parish entry is not the papacy.

    Both claims are confirmed and recorded as no-entry in
    `Build/Ministry/Operations/Audits/2026-11-10_links-era-10-part-2/Drafting_Record.json`. Owner:
    Mark (the method question), then the census owner (whether a post-conciliar Catholic entry is
    needed).
    - 2026-11-10: two part 2 links use the post-Vatican II parish entry for acts of Rome after 1962,
      with flags on each saying why it fits the entry's own scope (the parish, the liturgy):
      `the-tridentine-church--the-post-vatican-ii-parish-world` (Summorum Pontificum, 2007, Art. 5
      §1 on parishes) and `the-post-vatican-ii-parish-world--latin-american-catholicism-twentieth-century`
      (Paul VI's Bogotá homily, 1968). If a post-conciliar Catholic entry is made, both are re-checked.

149. **Era 10 after P2-L10: what is still unlinked, and two more stale recordings (2026-11-10).**
    - **Nine era 10 movements have no link of any kind:** IX.7, IX.30, IX.51, IX.54, IX.58,
      IX.60, IX.61, IX.70 and IX.73. For each, either its text names no relationship to a census
      movement that a source opened in the run supports, or the relationship waits for a ruling or
      a text (dispositions in the two P2-L10 drafting records). 28 of the 71 era 10 movements have
      no "gave rise to" or "continued as" link coming in, down from 48. Many of their parents fall
      in the timeline breaks of Open-Gaps 142, so they come with that work. Owner: the next link
      pass after sources are found.
    - **Two more tree recordings read old descriptions.** Data release 28 rewrote the
      longDescription of `ecumenical-community-worlds-taize-and-iona` and
      `oneness-pentecostalism`. These join the five of Open-Gaps 145 for a paid re-voice, on
      Mark's approval after a sample.
150. **What P2-G3 settles (2026-11-10).** Data release 29 carries the agreed entries (audit:
    `Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/`). It closes these parts of "What
    P2-G2 leaves for P2-G3" (2026-11-09): II.1 now runs from 328 with Athanasius; the desert monks'
    "gave rise to" link is retired for the "influenced" link on the same pair; Tertullian's display
    name is "Tertullian"; the four links naming him are read (one concerns him); every tradition has
    its people row, with each quote's speaker confirmed by the reviewer. From "The gap sweep is
    ruled" (2026-11-09) it builds the seven new movements, the Mennonite and Melkite successors, the
    later Carthusian movement (1300 to 1534) and the person entries. The Theophilus row stays with
    the Library thread ("Library shelf moves the release points to", 2026-11-10).
151. **The people the later-worlds count found, held for a follow-up (2026-11-10).** Mark's answer
    D a. As written, the rule passes 125 people, most from eras 1 and 2, and the count is noisy:
    namesakes (Jerome Lalemant counts for Jerome) and the editions' own notes and indexes count as
    mentions. Before any of them gets an entry: check each alias for namesakes, leave out editorial
    matter, re-run, and put the clean list to Mark. Result and scripts:
    `Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/counts/`. Owner: a P2-G3 follow-up.
152. **Library shelf moves the release points to (2026-11-10).** For the Library thread; the corpus
    map was not edited:
    - the Theophilus row (`npnf214_seven-ecumenical-councils`) may move to II.1, now that II.1 starts
      in 328;
    - Bell 1924, Part II (the Melitian papyri) sits on `desert-monasticism`'s shelf and belongs on a
      new `melitian-schism` shelf;
    - the nine new movements have no shelves yet;
    - Busch's Chronicon Windeshemense is on the Devotio Moderna shelf as context; ruling 51 makes it
      the houses' own voice (role tradition);
    - Love's Mirror is shelved on the mystics and lay-piety entries; it is the later Carthusians' own
      voice;
    - Simeon of Beth Arsham's letter and Life are shelved as context on Aksum and the Church of the
      East, while ruling 15 tells him within the Syriac Orthodox church.
153. **Places with no source ID (2026-11-10).** No census entry has a gazetteer ID for these places,
    so the new entries leave them out of `modernCountries` rather than type an ID from memory:
    Quebec (New France lists no country), Cagliari, Delaware and New Jersey, London, Bruges, Deventer
    and Mount St Agnes (Thomas à Kempis lists none), Antwerp, Worms and Vilvoorde, Maiuma and Gaza,
    Upper Hungary and Indiana. Owner: the place-label work (PL2's method: looked up, never from
    memory).
154. **The Martyrs Mirror file is a modern printing (2026-11-10).**
    `cic/texts/van-braght_martyrs-mirror_sohm1886.txt` is a 2012 Herald Press printing with a 1938
    copyright notice; its front matter is not public domain. Release 29 quotes only van Braght's own
    text from it, in Sohm's 1886 translation. Owner: the Library thread (a suggested task is queued).
155. **Open points left by P2-G3 (2026-11-10).**
    - The later Carthusian entry ends in 1534; with 1534 onward a named gap, the reviewer suggested
      1539, when the English houses closed (in the Library). Left at 1534.
    - The desert monks' "influenced" link on II.1 rests on 457 evidence, after the monks' entry ends
      (c. 430), as the published link already did. For P2-L11.
    - No entry holds the church of Alexandria before 328 (Peter, Achillas, Alexander).
    - Two-way checks for the home texts: the person links are named on the person pages, not yet in
      their home movements' text (for example, the Methodist revival's text does not name Luther).
    - Nestorius's working years run past his home entry's end (430); his page says so.
    - For entry owners: `carthusian-life` says the order kept its shape "ever since", now that it
      has a successor; Ambrose's home text says he was consecrated "within the week", where the
      source says eight days.
156. **Recordings for the new pages wait for the one batch (2026-11-10).** Mark ruled (2026-11-10)
    that all tree recording waits for one batch after P2-L10 and P2-G3 have both merged. Release 29
    adds 31 new tree pages (38,112 characters), 3 pages whose text changed (3,898) and 6 stories
    (3,508): 45,518 characters in all. No sample was prepared and no paid call made. Owner: this
    thread, at the batch.
157. **What P2-V settles (2026-11-10).** Data release 30 carries the written definition of "living"
    and the check of every living flag (Decision-Log, "What 'living' means: P2-V applied as data
    release 30", same date; audit `Build/Ministry/Operations/Audits/2026-11-10_living/`). Ruling 15's
    condition before the leaf appears is met; the drawn marks are P2-K1. Flags: 192 true before, 264
    after (of the 127 true in eras 1 to 9: 117 kept, 9 graded, 1 dropped; 73 added; era 10 as
    ruled at its gate).
158. **Living traditions with no entry after a date: the named gaps (2026-11-10).** Under principle 3
    of the gap sweep ruling, each is told only to the year shown, and the gap is named on its living
    flag (`decisions_final.json`, field `namedGap`). Filling any of them adds a row to a frozen
    era, so each is a change order with its sources found first. Some overlap "Breaks in the
    timeline" (2026-11-10). 79 gaps:
    the Church of Antioch after 312; the Church of Jerusalem after 450; the island monastery of
    Lérins between about 450 and today; the Georgian church from 1245 to 1917; Judean desert and
    Sinai monasticism from 614 to today; the Irish church from 1169 to today; the Syriac Orthodox
    Church between 1300 and 1915; the Welsh church from 1282 to today; the Latin church in the
    Frankish lands from 888 to about 1049; Benedictine monasticism after 604; the Roman Church from
    604 to about 1049; Arabic-speaking Chalcedonian Christians between 1009 and 1724; the Mozarabic
    community from 1031 to today; the Latin church from 888 to about 1049; the St Thomas Christians
    from 1665 to 1836; Athonite monasticism after 1300, apart from the hesychast entries; the
    Carthusians after 1534; the Cistercians after 1300; the Maronites after 1517; the canons regular
    after 1246; the Order of Malta after 1291; the Carmelites after 1300, apart from the reform of
    1562-1622; the Franciscans after 1517; the Dominicans after 1300; the Kongo church after 1650;
    the Lutheran churches after 1906; the Unitarian church of Transylvania after 1650; the Reformed
    churches after 1906; the Mennonites and Amish after 1890; the Nordic Lutheran churches after
    1650, apart from the Haugean and Laestadian entries; the Hutterites after 1785; the Waldensian
    church after 1655; the Jesuits after 1650; the Schwenkfelders after 1650; Japanese Christians
    between 1650 and 1865; the French Reformed churches after 1787; English and Welsh Catholicism
    after 1650; the Church of Scotland after 1650; the Discalced Carmelites after 1622; Chinese
    Catholics between 1650 and 1906; the Remonstrants after 1650; the church in New France after
    1650; Ukrainian Orthodoxy between 1700 and today; the Delaware Swedish congregations after 1786;
    English Dissent after 1815; the Old Believers after 1815; French Protestantism after 1787; the
    Brethren after 1815; Armenian Catholics and the Mekhitarists after 1815; the Moravian Church
    after 1815; New England's Congregational churches after about 1760; the Welsh chapel tradition
    after 1815; the Shakers after 1815; English Unitarianism after 1813; the New Church after 1815;
    Sunday school and Bible institutes after c. 1900; Korean Catholicism after 1886; the Pacific
    island and South Indian mission churches after 1906; the Haitian Catholic Church after 1860; the
    Inner Mission and Diakonie after 1880; the Old Catholic Churches after 1906; Methodism after
    1906; Baptists after 1906; the Quakers after 1906; the Melkite Church after 1911; Confessional
    Lutheranism after 1906; Malagasy churches after 1895; Unitarianism and Universalism after 1906
    (the entry's 1961 merger is told only inside it); the Plymouth Brethren after 1906; the
    Latter-day Saints after 1906; Dutch Neo-Calvinism after 1906; the Holiness denominations after
    1906; Laestadianism after 1906; the Christadelphians after 1906; Spiritualism and New Thought
    after 1906; Russian evangelicals after 1906, apart from the Soviet-era Baptists told only to
    1991; the Salvation Army after 1906; Jehovah's Witnesses after 1906; Christian Science after
    1906.
159. **Present-day families the tree does not reach (2026-11-10).** The backward check
    (`research/backward_check.json`) traced 58 present-day families. 24 reach about 2010 through a
    living entry; 29 stop earlier (the gaps above); 5 have no entry at all: the Greek Orthodox
    Patriarchate of Alexandria, the Church of Cyprus, the Polish Orthodox Church, the Orthodox
    Church of the Czech Lands and Slovakia, and the Macedonian Orthodox Church. Eastern Catholic
    churches the tree never names: the Syriac, Coptic, Ethiopian and Eritrean, Hungarian, Slovak,
    Italo-Albanian, Bulgarian, Greek and Croatian Greek Catholic churches. For a later completeness
    pass; adding any is a change order.
160. **The Lérins entry says the abbey has stood since about 410 (2026-11-10).** The abbey's own
    history page speaks of a "reopening", which suggests a break in the community. No dated source
    in hand settles when or for how long. The living flag stands with no descent grade. For the
    entry's owner: the "stood since about 410" line, once a source is found.
161. **Link grades that reflect sources, not a break in the church (2026-11-10).** On some lines (the
    Coptic and the Latin American among them), a "continued as" link is graded low because the tree
    lacks entries or sources for a period, not because the church broke. P2-V's descent grades no
    longer copy those link grades. For P2-L11: re-check them.
162. **Living marks that wait for a dated source (2026-11-10).** Four living flags have no dated item
    after 2010: Kongo Christianity to 1650, the Anti-Trinitarian currents (the Transylvanian church),
    the Schwenkfelders and the New France mission. They stay living, graded none, as the era 10 gate
    ruled for the same case. Wanted: a dated own-voice item for each. Also weak: about 30 own-voice
    items are rotating home pages, and every CR mark could reach CD with a verified independent
    source. For the source-research thread.
163. **Open questions the check left, and one line for another owner (2026-11-10).** Each verdict
    below was applied under the rule; the question is recorded here, not decided:
    - Post-Apostolic Household-Church Christianity: Is a period before the churches divided an
    episode of one living tradition, or only a root they all claim?
    - Alexandrian Catechetical / Christian-Platonist Tradition: Does the later catechetical teaching
    of the Coptic Orthodox Church of Alexandria count as descent, or only as a claim of heritage?
    - The Church of Antioch in the Third Century: Which of the patriarchates of Antioch should the
    tree name as the carrier of the third-century church?
    - The Anatolian Church in the Third Century: Is this the Greek church of Anatolia in one period,
    which the Orthodox churches carry, or a circle of writers?
    - Cappadocian Christianity: Did the Greek Orthodox community of Cappadocia end in the population
    exchange of 1923 to 1924? If a dated source shows it did, this local church is ended under the
    local-church rule.
    - The Church of Aquileia: Is this the local church of Aquileia, which present dioceses might
    carry, or the work of one writer?
    - The Church of Caucasian Albania: The entry says the Udi people of Azerbaijan are generally
    seen as descended from its Christians; does a documented Udi church community today count as
    descent?
    - British and Welsh Christianity: The entry says no separately continuing British church exists;
    does the Church in Wales count as the same tradition?
    - Nicene Visigothic Iberia: Does the Visigothic church count as alive through the Mozarabic rite
    alone, or through the whole Catholic Church in Spain?
    - The Latin Church of Outremer: The Latin Patriarchate of Jerusalem was revived in 1847, but the
    entry treats that as a later see, not a continuation of this church.
    - Canons Regular / Victorine School: The Victorine school itself ended with its abbey; the entry
    names the canons regular family, which continues.
    - Military-Religious Orders (Templars, Hospitallers): The entry names two orders; the Templars
    were suppressed, while the Hospitallers continue as the Order of Malta. I treated the entry as
    living through the Hospitallers.
    - The Humiliati: The entry says some houses of Humiliati nuns lived on; it gives no date for
    their end.
    - The Beguines: The entry's own text names no last member; the end rests on two dated reports of
    the death of the last traditional beguine in 2013.
    - Rhineland Mysticism & the Friends of God: The entry does not state an end for the circle; it
    describes only how the writings spread.
    - The English Mystics and Devout: The entry does not state an end for the circle; it describes
    only the later fate of the writings.
    - Lollardy: The entry gives no final date or merger for the Lollard households; their end as a
    community is inferred from the entry's closing date.
    - Mission-Born Christianities (Kirishitan Japan; Kongo; China; New Spain/Andes): This is a label
    entry for four churches, so it is living only through its four regional entries.
    - Anti-Trinitarian Currents (Servetus; Polish Brethren/Socinians; Transylvanian Unitarians): The
    Polish Brethren wing of this entry did not continue; only the Transylvanian church is alive.
    - The Czech Churches' Last Century (Utraquists and Unitas): The entry is flagged not living, but
    its Unity of the Brethren wing continues through the Moravian Church; the Utraquist wing ended.
    - Mission-Born Christianity in New France: The Huron Christians who reached Quebec in 1650 may
    be the ancestors of today's Wendake community, but no source in hand shows it.
    - The Kyiv-Mohyla Orthodox Revival: Two Orthodox bodies in Ukraine both claim this Kyiv
    heritage, so the present body is disputed.
    - The Swedish Lutherans of New Sweden: Does a congregation that changed church body and language
    still carry the Swedish Lutheran tradition, or does the tradition end with the pastors'
    departure in 1786?
    - English Old Dissent — Presbyterians and Congregationalists: Only the United Reformed Church
    was fetched; the Congregational Federation and the Unitarian half rest on the entry's own text
    and the English Unitarianism entry.
    - The Church of the Desert: The fetched page does not say that the Eglise protestante unie de
    France continues the Reformed Church of France; that link rests on the entry's own text.
    - Armenian Christianity — the Mekhitarists and the Catholic Patriarchate: Only the Armenian
    Catholic Church could be fetched with a dated item; the Mekhitarists rest on the entry's own
    text.
    - The Hesychast Revival - Paisius & the Philokalia: The carrier is the Romanian church entry
    because Neamt lies in Romania; the Russian line has no entry holding present-day evidence.
    - The Sunday School & Bible-Institute Movement: The entry itself asks whether this is a
    tradition or a set of methods inside other traditions; I answered on the Bible-institute and
    Sunday-school bodies it names.
    - The Reveil & Inner-Mission Awakening: The census flag is false, but the tradition the entry
    names is alive; the flag looks like a mismatch for the gate.
    - Catholic Apostolic Church (Irvingites): The entry names the New Apostolic Church as a
    breakaway daughter; if that church counts as the same tradition this entry would be living.
    - Spiritualism / New Thought: The census flag is false because the entry sits outside the
    Christian frame, but the living flag asks only whether the tradition is alive; I answered that
    question.
    - The Student Volunteer Movement & Edinburgh 1910: The Edinburgh 1910 strand continues through
    the International Missionary Council's merger into the World Council of Churches; if that counts
    as the same entry, it would be living through that ecumenical entry.
    For the method page's owner: "What is still to come" still says the tenth era is not yet
    linked, though P2-L10 has linked it.
164. **The later-worlds people at Mark's gate (2026-11-10).** P2-G3b re-ran the count held by
    "The people the later-worlds count found, held for a follow-up" (2026-11-10) with namesakes
    checked, editorial matter masked and every counted passage read in context and reviewed (audit:
    `Build/Ministry/Operations/Audits/2026-11-10_later-worlds-people/`). 32 people pass the clean
    count; 14 are recommended for entries and 18 held, with three questions (founders, words
    written for or with a person, two traditions resting on one book). The list is the artifact
    https://claude.ai/artifact/AGVVFoi57c6gNtDtVoyADC. No census change until Mark picks. Owner:
    P2-G3b.
165. **Shelf and data defects the clean count found (2026-11-10).** For the Library thread and the
    census owner; nothing was edited:
    - `cic/corpus-map/montanism-the-new-prophecy.yaml` holds Hippolytus's Refutation, an opponent's
      book, as the tradition's own voice.
    - The 1453-1650 Ottoman parish-millet shelf holds Nikodemos's Synaxaristes (about 1805).
    - `john-ephesus_lives-eastern-saints-po17_brooks1923.txt` is described on the Palaiologan shelf
      as Petit's Florence documents; the file opens as John of Ephesus's Lives.
    - The Brosset file on the Georgian Golden Age shelf holds only Brosset's introduction, charters,
      notes and index.
    - Many rows give "whole file" for a volume that binds several works (anf05's Hippolytus with
      Cyprian, Langlois's Moses of Khoren with Koriun and Elishe, PO fascicules with synaxaries), so
      a whole-file count reads works the shelf did not mean.
    - The people rows' `year` is an active or accession year, not a death; the later-worlds count
      used it as the last year, which let Theodoret and Eunomius pass on traditions that began in
      their lifetimes.
    - Ephrem appears in the alias list as "Ephraim the Syrian", unmatched to the shipped entry.
166. **The later-worlds people held, with their reasons (2026-11-10).** Mark ruled "take every
    recommendation" on the P2-G3b list (Decision-Log, "The later-worlds people ruled (P2-G3b)").
    Each person below passes the clean count and is held; a change of rule or a new text in the
    Library could bring them in. Owner: P2-P / the Library thread, as noted.
    - **Founders (question A):** Priscillian (Priscillianist Asceticism; no work of his held),
      Valentinus (the Valentinians), Mani (Manichaeism), Novatian (Novatianism; own works held),
      Hilarion of Gaza (opens Early Palestinian Ascetic Monasticism), Apollinaris of Laodicea
      (Apollinarian Christianity; own fragments held), Valdes (the Waldensians), Francis of Assisi
      (the Franciscan movement; his own writings are not on the shelf), Zwingli (the Reformed
      Cities; own works held). Each is told within that movement's entry.
    - **Own words (question B):** Johannes Tauler. His sermons survive as his hearers' notes.
    - **One witness (question C):** Constantius II (both later traditions rest on Nikodemos's
      Synaxaristes); Basilides (Rome and Montanism rest on the same Hippolytus passages, and his
      death date is unknown).
    - **No words of their own in the Library:** Paul of Samosata (the council's letter and
      Malchion's half of the debate only), Mesrop Mashtots (Koriun's Life of him, no work of
      his), Maximilla (her sayings come through opponents), Kaleb (a prayer reported by others),
      Heraclius (the Ekthesis is not held), Bonaventure (one quoted sentence in an editor's note).
      Wanted texts for the Library thread: Paul of Samosata's fragments, a Mesrop text, the
      Ekthesis, Bonaventure's Itinerarium and Life of Francis, Francis's own writings.
    - **Pamphilus of Caesarea**, held after Mark's ruling by the correction in the Decision-Log
      ("The later-worlds people ruled (P2-G3b)"): the Library holds only Rufinus's preface and
      epilogue to the Apology for Origen, and the fragments on Acts are of disputed authorship.
      Wanted for the Library thread: the Apology for Origen, Book I, in Rufinus's Latin (PG 17) or
      an English translation. He comes in when the text does.
167. **Open points left by data release 31 (2026-11-10).** Audit:
    `Build/Ministry/Operations/Audits/2026-11-10_later-worlds-people/build/`.
    - The link `latin-papal-church-gregorian--latin-papal-church-avignon-to-lateran-v` rests on
      the Dictatus Papae as Gregory VII's. Mirbt's heading reports Sackur's view that Cardinal
      Deusdedit wrote it. Its note should say the authorship is disputed. Owner: P2-L11.
    - Lactantius lists no modern country: the census has no place ID for Nicomedia, Trier or Gaul.
      Paula lists Rome only (no Bethlehem ID). Owner: the place-label work.
    - Thirteen new tree pages (11,077 characters) join the one recording batch. Owner: this thread,
      at the batch.
    - Wanted for the Library thread, from the drafts: a Patrick chronology study; Justinian's Novel
      131 and the acts of 553; Cuthbert's letter on Bede's death; a source for Grotius's
      imprisonment; Mirbt's Dictatus heading in a clean scan.
168. **What the Library's first wants batch filled (2026-11-10).** For the wanted texts named in
    "The later-worlds people held, with their reasons" (2026-11-10). Full list:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`.
    - Filled: Pamphilus's Apology for Origen, Book I (Lommatzsch 1846; Migne PG 17 as a second
      witness); Priscillian's Wurzburg tractates (CSEL 18); Francis's writings (Robinson 1906, and the
      Latin Opuscula of 1904); Bonaventure's Legenda maior (Salter 1904) and three Latin works
      (Quaracchi 1911).
    - Already held, now shelved: Heraclius's Ecthesis, in Mansi X, read into the Lateran Council of 649.
    - Still owed by Mark's questions: Pamphilus (B, a book written jointly), Francis and Priscillian (A,
      founders). Bonaventure and Heraclius now pass answer C.
    - No own text survives, or none in the public domain was found: Mani, Kaleb, Valdes, Mesrop,
      Paul of Samosata, Basilides, Valentinus, Maximilla, Hilarion, Tauler.
169. **Shelf defects fixed, and two left for a cross-world ruling (2026-11-10).** These were in
    "Shelf and data defects the clean count found" (2026-11-10) and "Library shelf moves the
    release points to" (2026-11-10).
    - Fixed: Hippolytus's Refutation is now context on the Montanist and Ebionite shelves;
      Nikodemos's Synaxaristes is off the 1453-1650 shelf; the PO17 loci are split by line; the
      Brosset file is relabelled as the Introduction volume; Busch is tradition for the Devotio
      Moderna; Love's Mirror is on the Carthusian shelf; Bell Part II is on the Melitian shelf.
    - Open, for the coordinator: whether Bell Part II leaves the built `desert` shelf, and whether
      the Pedalion (1800) leaves the 1453-1650 shelf.
    - Not the Library's: the people rows' `year` and the Ephrem alias (census owner); the Theophilus
      row (a census question).
    - Queued: the general loci pass for multi-work volumes, and the Georgian chronicle text volumes.
170. **The held people the Library's first batch brings in (2026-11-10).** PR #1577 filled the wants
    ("What the Library's first wants batch filled", 2026-11-10) in "The later-worlds people held, with their reasons" (2026-11-10) for Pamphilus, Bonaventure
    and Heraclius, who now have entries (Decision-Log, "Three held people come in once the Library
    holds their words"). Francis and Priscillian's own words are now held too; they stay held as
    founders. The rest of that list stands: the Library found no own text for Mani, Kaleb or Valdes,
    and none survives for the others (`Build/Ministry/Features/Source-Library/CFT-Wants.md`).
    Wanted, from the drafts: an English rendering of the Apology, a clean text of the Ecthesis, a
    primary source for Heraclius's letter disowning it, and a source for Bonaventure's birth year.
171. **Eras 8 and 9 rulings, Africa holds (2026-11-10).** P2-G89b (data release 33) carried out
    Mark's rulings on the eras 8-9 global sweep. Each hold below gives what is held, its G89
    question and what it waits for. Drafts:
    `Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/drafts/`.
    - **AF-8, West Africa before the mission societies** (G89-12 a). Nothing was opened for Quaque,
      Capitein or Rebecca Protten; the only lead for Capitein is a 2001 translation, not public
      domain. Waits for a pre-1930 source for Quaque (SPG) and the Freetown settlers' churches,
      opened raw.
    - **AF-9, the Swedish mission in Eritrea from 1866 and Onesimos Nesib's Oromo Bible (1899)**
      (G89-13 a). Only [S] in the record; no source was read. Waits for a pre-1930 Swedish
      Evangelical Mission report or a life of Onesimos Nesib, and a source for 1866.
    - **AF-7, Ge'ez-rite Catholics (de Jacobis from 1839, Ghebre Mikael, Halai and Akkele Guzay)**
      (G89-11 a). The article read does not name the rite, the date 1839 or Ghebre Mikael. Waits for
      Crummey (1972) or a pre-1930 life of de Jacobis, opened raw.
    - **AF-7, Coptic Catholics (the patriarchate named in 1824, filled in 1895)** (G89-11 a). [S] in
      the record; only Butcher's account of 1741 was read. Waits for a source for 1824 and 1895.
    - **AF-4, the synod resolution of 1857, the Dutch Reformed Mission Church (1881) and the link to
      the church struggle against apartheid** (G89-5 a). Not in McCarter (1869). Waits for the Acta
      Synodi of 1857 in Dutch and a pre-1930 history that prints the resolution and the founding.
    - **AF-3, the years from about 1720 to 1879** (G89-9 a). Merolla (1692), Zucchelli (1715) and
      Proyart (1814) are in the Library but were not read; Cavazzi's passage on Njinga's return was
      not found in the OCR. Waits for a read of those texts for 1680-1760 and a source for
      1720-1879.
    - **AF-1, the Zemene Mesafint (its start in 1769 and its character)** (G89-7 a). No item read
      describes it; the row's sentence rests on the record's own account. Waits for Guidi's annals
      of Iyasu II and Iyo'as, or Weld Blundell's Royal Chronicle of Abyssinia (1922), opened raw.
    - **Wanted:** Guidi, Annales (CSCO, 1903-05; lending-only copies on archive.org); Weld Blundell
      (Cambridge, 1922; not found on archive.org by title); the Arabic History of the Patriarchs for
      the Ottoman patriarchs; Vansleb, Histoire de l'Eglise d'Alexandrie (1677); the archons'
      letters and waqf deeds, and Magdi Guirguis on the Jawhari brothers; Kongolese letters to Rome
      and Lisbon, and the Capuchin manuscripts of Antonio de Teruel and Bernardo da Gallo; the Acta
      Synodi of 1857 and a pre-1930 history of the Dutch Reformed Mission Church; Ntsikana's hymn in
      Xhosa from a pre-1930 printing; a modern study of James Bruce as a witness to Ethiopia in the
      1770s. The dated present-day statements wanted for the living marks are in "New rows marked
      living with no dated source" (2026-11-10).
172. **Eras 8 and 9 rulings, Latin America holds (2026-11-10).** From the same draft. Each hold
    gives its G89 question and what it waits for.
    - **LA8-6, Haiti before 1804 and after 1860 (the concordat church; Holly's Episcopal mission)**
      (G89-18 a). Two studies were seen only as catalog records; no primary was opened and no
      Library file covers Haiti. Waits for the Code Noir (1685), a French account of the concordat
      church and James Theodore Holly's own writings. Then Holly enters as a line in VIII.46 or
      VIII.1, and Saint-Domingue as a line in VII.17 or VII.19.
    - **LA8-8, Cuba and Puerto Rico under Spain, 1815-1898 (a line in VIII.48)** (G89-20 a). Nothing
      was opened; the record's items are all [S]. Waits for a source on the church under the
      patronato in the two colonies. Claret's Autobiografia is a lead, but its first printing may be
      after 1930.
    - **LA8-9, the Bethlemites in Guatemala, 1650s-1820 (a line in VII.17)** (G89-21 a). Nothing was
      opened; the record's items are all [S]. Waits for a pre-1930 source on Pedro de San Jose de
      Betancur and the order of 1687.
    - **LA8-10, the Virgin of Cancuc (1712) and the Talking Cross (1850-1901)** (G89-22 a). No
      primary was opened and no Maya-language source is in the Library. The Talking Cross raises a
      real Section A question that no dated statement answers. Waits for Francisco Ximenez's
      chronicle for Cancuc, a dated Cruzob text and a Section A ruling on the Cross.
    - **LA8-1, the revival of 1860-61 and Morant Bay (1865), as lines in the Caribbean row** (G89-14
      a). Both are [S]. Phillippo (1843) and Bleby (1868) cannot speak to 1860-65, and Underhill
      (1862) holds no account of the revival. Waits for a pre-1930 source on both. The row's
      sourcing line says plainly that they are not yet told.
    - **LA8-3, the Juazeiro line (Padre Cicero; the miracle of 1889) in VIII.48** (G89-15 a). The
      record's items are Della Cava's study (a catalog record, in copyright) and [S] notes. Waits
      for a pre-1930 source on Juazeiro or a reading of Della Cava, Miracle at Joaseiro. The
      Tomochic line enters now.
    - **LA8-7, Brazil's German Lutherans from 1824, as a line in VIII.41** (G89-19 a). The record's
      item is [S]; no Library file covers it. Waits for a pre-1930 source on the Lutheran colonists
      in Brazil. Then VIII.41 gains Brazil in its text and regions.
    - **LA8-7, Kalley (1855), Simonton (1859), the Waldensians in Uruguay (1857) and Gardiner
      (1851), in IX.63's pre-1916 line** (G89-19 a). All [S]; only Thomson (1818-21) was read, so
      only he enters. Waits for Kalley's and Simonton's journals and a source for the Waldensian
      colonies and Gardiner's mission.
    - **Wanted:** Phillippo (1843), Bleby (1868), Hinton (1849), Wallbridge (1848), Euclides da
      Cunha (1905), Vieira (1686), Antonil (1711) and Thomson (1827), read raw online and ready to
      vendor (the Library holds nothing yet for the region between 1815 and 1906); a pre-1930 source
      for the revival of 1860-61 and Morant Bay; a modern study for the Baptist link (Turner 1982;
      Dayfoot 1999) to lift it above Inferential-Thin; the Conselheiro's own sermons and notebooks
      and a dated statement of the community's faith, for the Section A question Euclides raises;
      Hernandez y Davalos, Coleccion de documentos (1877-82), and Morelos's Sentimientos de la
      Nacion (1813), not found on archive.org; Levine, Vale of Tears (1992), and Della Cava if a
      lawful copy can be reached.
173. **Eras 8 and 9 rulings, Asia part 1 holds (2026-11-10).** India, China, Japan, Korea and the
    Peking mission.
    - **AP7, the Catholic St Thomas Christians and the Chaldean Syrian body at Thrissur, 1815-1906,
      then AP1 extended to 1906 and a link to VIII.40** (G89-29 c, then a). The record rests on two
      pre-1930 Protestant studies (Richards 1908; Rae 1892, passage not located). The Chaldean
      bishops of 1861 and 1874, the vicariates of 1887 and Chavara are [S]. Waits for one Catholic
      or Malayalam source for the Catholic half in era 9, for example Chavara's own writings or
      Syro-Malabar sources.
    - **AP11, the Russian Ecclesiastical Mission in Peking and the Albazinians, 1685/1715-1906, then
      a line in VIII.31** (G89-36 b). No source was opened; Widmer (1976) was not found on
      archive.org. Waits for Widmer or a pre-1930 work on the mission and the Albazinians.
    - **AP15, Korea 1884/1886-1906 (Protestant beginnings; the Catholic years after toleration),
      then lines at the end of VIII.21 and in VIII.7** (G89-34 b). No source was opened. Waits for
      dated primary sources for the Protestant congregations (the Ross translation, the Nevius plan)
      and for the Catholic church after 1886.
    - **Wanted:** Paremmakkal Thoma Kathanar, Varthamanappusthakam (c. 1790; no pre-1930 printing
      found); the Malayalam originals of the Malankara history (Whitehouse App. D) and the Angamaly
      document of 1787 (App. E); a fuller read of Raulin 1745 and Sebastiani 1666 and 1672, in the
      Library, for AP1's window; Huang Bolu, Zhengjiao fengbao (1883), for the 1692 edict and the
      1723 memorial; Tenchi hajimari no koto, the hidden Christians' own text; Urakawa Wasaburo,
      Kirishitan no fukkatsu (1927-28), and a Japanese source for the village communities; Eric
      Widmer (Harvard, 1976). The missing China ID is in "Missing modern-country IDs" (2026-11-10).
174. **Eras 8 and 9 rulings, Asia part 2 holds (2026-11-10).** Southeast Asia, the Pacific and the
    VOC world.
    - **AP10, the Cofradia de San Jose (Hermano Pule), 1832-1841, then a line in VIII.39** (G89-33
      b). Only Ileto (1979) was verified, and the Blair and Robertson volumes searched do not carry
      the 1841 papers. No sentence can be drafted from it. Waits for a dated primary, such as the
      1841 papers.
    - **AP12, Christianity in colonial Australia and New Zealand, 1788-1906, as lines in VIII.29,
      VIII.30 and VIII.34** (G89-35 c). Breward (2001) and Suttor (1965) were not opened. Waits for
      primary sources for Australasia.
    - **AP13, Maori Christianity, Pai Marire and Ringatu, 1862-1906** (G89-30 c). Section A cannot
      be assessed. The only passage read is Cowan (1922), a hostile settler history. IX.26 starts in
      1925, so a line there would sit before its own row's dates. Waits for a Maori-language or
      Maori-authored source first: Te Ua's Ua Rongopai and the Ringatu Pukapuka.
    - **AP14, the Pacific Christian kingdoms, 1797-1906** (G89-37 a). Carried: the Pacific wing
      stays in VIII.7. Nothing is drafted. Splitting a Pacific row out would be a change order on a
      frozen row, which the ruling declined. Waits for nothing in this sweep; a reader of the
      Pacific wing may ask for a split later.
    - **AP9, the Karen Baptist movement in Burma, 1828-1906, as a line in VIII.27** (G89-31 a). The
      ruling asks for one modern study first. The only one found is an MA thesis (Opehtoo 2014) that
      rests on Mason and Harris, so it does not check the missionary memoir. Waits for a published
      modern history of the Karen Baptists and Karen-language sources.
    - **Wanted:** the Vietnamese text of Philiphe Binh, Sach so sang chep cac viec (1822; no
      pre-1930 printing found); Alexandre de Rhodes, Cathechismus (1651), the teaching and not only
      the title page; a Vietnamese Catholic source for 1833-1906; Valentijn, Oud en Nieuw
      Oost-Indien (1724-26), the Leijdecker Bible of 1733 and Ambon church records; the Dutch
      proclamations of 1658 and 1715 against Catholics in Ceylon and a Dutch Reformed account of the
      Ceylon church; Sebastiao do Rego's life of Joseph Vaz (1745) and Tamil and Sinhala Catholic
      texts. The dated present-day records wanted are in "New rows marked living with no dated
      source" (2026-11-10). The missing IDs and the VOC lineage question have their own items.
175. **Eras 8 and 9 rulings, Middle East and Caucasus holds (2026-11-10).** Slice ME-1.
    - **ME-2, the Maronite Church from Duwayhi to the Hindiyya affair (era 8 row)** (G89-39 a).
      Enters once the acts of the 1736 synod of Mount Lebanon are opened. Mansi vol. 38 is not on
      archive.org (most other volumes are). Without it the row would rest on Labourt and Volney
      alone. Waits for Mansi vol. 38, Collectio Lacensis vol. 2 (1876) or another public-domain
      edition of the acts.
    - **ME-4, the Orthodox Patriarchate of Antioch, 1815-1906 (era 9 row)** (G89-42 a). The only
      text read is Fortescue, a hostile Catholic witness. The first Arab patriarch, Meletios Doumani
      (1899), is in no text read. Waits for an Orthodox source after 1815.
    - **ME-7, the Syriac Orthodox Church and the Syriac Catholic split, c. 1650-1906** (G89-47 a).
      Both texts in hand are outsiders (Badger, Anglican; Fortescue, Catholic). The record asks for
      one own-voice or in-region item first. Waits for a Syriac or Arabic chronicle of the
      patriarchate after 1369, or Parry (1895).
    - **ME-16, the Holy Places and the Latin Patriarchate of Jerusalem (1847)** (G89-48 a). Held as
      a gate note: a cross-church story, not a movement by the four marks. It may become a line in
      the Orthodox and Catholic nineteenth-century rows. Waits for a decision on where the line sits
      and a second, non-Catholic study beside Fortescue.
    - **ME-21, the Hebrew Christians of Kishinev (Joseph Rabinowitz, 1884)** (G89-48 a). Snippet
      only. Waits for a pre-1930 source on Rabinowitz and the Kishinev congregation, opened raw.
    - **ME-18, the Volga missions and Il'minskii's schools** (G89-48 a). Only the Siberian part has
      a source read (Mouravieff). Waits for a source on the Volga and Kazan missions and
      Il'minskii's schools. The Beijing mission goes to the Asia slice.
    - **ME-19, the Assyrian evangelical church, as a half of the Urmia line** (G89-48 a). Only the
      Russian mission half has a source read (Wigram). Waits for Wigram on the Urmia Protestants or
      a mission history such as Anderson (1872).
    - **Wanted:** Mansi vol. 38; a clean Duwayhi, Tarikh al-ta'ifa al-maruniyya (the Library copy
      has damaged OCR and serves only as a locator); Brosset, Histoire de la Georgie, modern volumes
      (1856-58), and Grdzelidze, George and Vischer, Witness through Troubled Times (2006), for the
      Exarchate before any era 9 row (G89-44 b); a source on the Serbian church at Karlovci and
      Montenegro after 1815 (ME-17); a second source on the year the Urmia Assyrians joined the
      Russian Orthodox mission (1896 in Wigram; 1898 in the sweep's [S] note). The Maronite years
      1517-1650 are in "Years logged for other eras' owners" (2026-11-10).
176. **Eras 8 and 9 rulings, Eastern Europe and Russia holds (2026-11-10).** Slice ME-2.
    - **ME-6, the Dukhobors and the Molokans** (G89-46 a). The record holds each body for Section A.
      Pinkerton (1814) reports that the Dukhobors rejected the outward church, the sacraments and
      the icons; Conybeare's chapter on the Molokans' confession was not read. Waits for a dated
      confession of each body (Conybeare Part II, ch. II is in the Library), then an era 9 row for
      what clears.
    - **ME-20, the Tolstoyans, 1880s-1906** (G89-48 a). A defined movement, but Section A is a floor
      question: Tolstoy denied Christ's divinity on the record's unopened report. Waits for a dated
      text of Tolstoy's before 1906. If it bears out the report, the movement is out of scope under
      A1 unless Mark chooses a lane 8 entry.
    - **ME-9, Hungarian and Transylvanian Protestantism, 1815-1906 (era 9 row)** (G89-45 a). The
      only era 9 item read is one sentence of the Catholic Encyclopedia. Waits for a source from the
      churches' own side after 1815, in Hungarian or by a Hungarian Reformed or Lutheran author.
    - **ME-9, era 8 detail: Debrecen and Sarospatak, the Lutheran Slovaks and Germans of Upper
      Hungary, the galley-slaves' own narratives** (G89-45 a). [S] in the record; Bauhofer was read
      for the laws and the galleys only. Waits for a Hungarian-language source or the narrative of a
      galley pastor such as Balint Kocsi Csergo.
    - **ME-8, era 9 remainder: Blaj and the Transylvanian School, the metropolitanate of 1853, the
      national revival** (G89-41 a). The row drafted rests on one church argument of 1893. The scan
      prints 1855 for the metropolitanate; the record has 1853 as [S]. Waits for a second Romanian
      study (Iorga, or Bunea's other works) with the date of the bull.
    - **ME-8, era 8 remainder, 1751-1815: Sofronie, the Supplex Libellus Valachorum, Orthodox
      resistance after Visarion** (G89-41 a). Nothing read tells the later eighteenth century. Waits
      for Bunea's or Iorga's later volumes, or Nilles for the later documents.
    - **ME-8, the Carpathian Ruthenian union after 1652 and its line in VIII.38** (G89-41 a). The
      line in VII.28 is drafted from Nilles's petition of 1652. Nothing opened tells the church for
      1815-1906; the Mukachevo see date is [S]. Nilles's index gives 1771 for the first bishop of
      Munkacs, not read in context. Waits for a nineteenth-century source and Nilles's Munkacs
      entries re-read.
    - **ME-10, the Commonwealth church 1650-1772 and the Lithuanian book-smugglers of 1864-1904**
      (G89-40 a). The record recommends an era 9 row only. Theiner vol. 4 (in the Library) was not
      read. Waits for a Polish or Lithuanian source for each, and Theiner vol. 4 for the
      Commonwealth church.
    - **ME-5, own-voice texts: the Belaya Krinitsa statute, the encyclical of 1862, the decree of
      1905** (G89-38 a). The row enters on Conybeare (1814) and the earlier entry's own-voice texts.
      No Old Believer document of 1846 or 1905 was opened. Waits for Smirnov, Ivanovskii or Subbotin
      on the Austrian hierarchy (Russian; no scan found), or the texts themselves.
    - **Wanted:** a scan of Nilles's Symbolae with the Latin and Romanian text of the union act less
      damaged; Polish pastoral letters of 1815-1906; a Hungarian-language source and a galley
      pastor's narrative; Tolstoy's dated writings before 1906 and each Dukhobor and Molokan
      confession. The dated record for the Reformed Church in Hungary and the Lutheran churches is
      in "New rows marked living with no dated source" (2026-11-10). The two gaps after 1906 are in
      "Years logged for other eras' owners" (2026-11-10).
177. **Eras 8 and 9 rulings, Catholic missions and the Society of Jesus holds (2026-11-10).** Slice
    RV-A.
    - **RV-3, the Catholics of Bosnia, Albania and Bulgaria, 1815-1878 (era 9 part)** (G89-51 a).
      Two items were read, Evans (1877), an outside witness critical of all the clergy, and Lins in
      the Catholic Encyclopedia (1908), a Catholic study. They are not enough alone. The article
      prints the name as "Solkolski". Waits for one more verified source: a Bosnian Franciscan
      chronicle in Croatian or a non-Catholic study. The era 9 row, or a second segment, then
      enters.
    - **RV-3, the Bulgarian union of 1860-61, a line here or in VIII.28** (G89-51 a). An era 9
      event, so it cannot sit in the era 8 row. The record names Lins (petition of 30 December 1860;
      vicar apostolic consecrated 21 January 1861; he went to Odessa in June 1861; most went over to
      the Exarchate). Waits for the era 9 part of RV-3, or the owner of VIII.28, and a non-Catholic
      or Bulgarian source for the other side.
    - **RV-3, Albanian and Bulgarian Catholics, 1650-1815 (era 8 part)** (G89-51 a). The items read
      (Fermendzin 1892) concern Bosnia and Slavonia only. The row says so and lists no Albanian or
      Bulgarian country. Waits for the Albanian council of 1703 (Concilium Albanum) and a source on
      the Bulgarian Catholics before 1815.
    - **RV-1, the dates of the expulsions (1759-67), the Malabar and Madurai rites, the Pragmatic
      Sanction of 1767** (G89-1 b). All [S]. The text says the four kings expelled the Society but
      gives no year. Waits for the Pragmatic Sanction or Dobrizhoffer (1784).
    - **RV-1, the Society's years in Russia, 1773-1800** (G89-1 b). The row says the priests lived
      "many years" in Russia, as the bull of 1814 does. No text read gives houses, numbers or dates
      before the tsar's dispatch of 1800. Waits for a Polotsk source.
    - **The AF-6 line in VIII.29, the parts not drafted** (G89-2 a, G89-10 a). [S] in the record:
      the Spiritans under Libermann, the Society of African Missions of Lyon, Comboni's institutes,
      Laval in Mauritius, Ohrwalder, de Jacobis, the Lazarist work in China and Ethiopia, and the
      later work of the restored Jesuits. The Lazarists, the Holy Spirit Society and the Jesuits
      appear only as names in Launay (1893). No source was read for Catholic missions in Oceania
      before 1906. Waits for a read source for each: Hastings (1994), Laval and Ohrwalder, a
      Lazarist history.
    - **Propaganda in VIII.29, any act beyond 1845 and the press of 1867** (G89-2 a). The Library
      holds only volume I of the Collectanea (to 1866). Waits for volume II (1867-1906), if the
      source thread vendors it.
    - **The link from RV-1 to AP3, Japan's hidden Christians** (G89-1 b). The ruling links them, but
      no text read shows the Society in contact with the hidden communities between 1650 and 1814.
      Their tie to the order runs through VI.11 and Kirishitan Japan, already linked. A link would
      claim a contact the sources do not show. Waits for a text showing a Jesuit tie in the window,
      or Mark's leave to rest on the existing VI.11 to VI.13b line.
    - **Wanted:** Dobrizhoffer, Historia de Abiponibus (1784); the Pragmatic Sanction of Charles III
      (1767); a Polotsk source; a modern history of the Society's suppression and a Jesuit letter or
      house history from Paraguay or Russia (the sources read for RV-1 are Roman or outsiders'); a
      Guarani-language or Guarani-written source for the reductions after 1743; a Bosnian Franciscan
      chronicle in Croatian (Fojnica or Sutjeska), the Concilium Albanum (1703) and a non-Catholic
      study; the Collectanea vol. II; Hastings, The Church in Africa 1450-1950 (1994), opened, to
      grade the link from VIII.29 to IX.59 on the secondary it names. The IDs removed from RV-1 and
      RV-3 are in "Missing modern-country IDs" (2026-11-10); the Jesuit and China link is in "Two
      links with a candidate secondary quote" (2026-11-10).
178. **Eras 8 and 9 rulings, Moravians, Arab evangelicals and Mennonites holds (2026-11-10).** Slice
    RV-B.
    - **RV-7, the Transylvanian Unitarians after the Polish exile, 1660-1906** (G89-53 a). A Section
      A lane 8 question with thin sources; the only verified item is Rees's 1818 introduction to the
      Racovian Catechism, a Unitarian study. Waits for a Transylvanian Unitarian source for
      1660-1906, in Hungarian or Latin. Then a lane 8 row or a line closing VI.14.
    - **RV-9, Kosmas the Aitolian (1714-1779)** (G89-55 a). Not a movement by the four marks on
      present evidence. Nothing in the Library; archive.org holds only modern studies. Waits for a
      pre-1930 text on Kosmas, read raw or vendored. Then a line in VII.18.
    - **RV-8, the Toleration churches of Bohemia and Moravia, 1781-1906** (G89-54 a). The hidden
      Unity before 1722 and the Patent of 1781 are told in VII.4. The Lutheran and Reformed
      congregations of 1781-1906 lie outside this sweep's North Europe scope. Waits for a North
      Europe pass.
    - **RV-6, the AME Church and South Africa's Ethiopian Church (1896); Daniel Coker (1820); a link
      from VIII.1 to IX.4** (G89-52 a). Both items are [S]; no verified source was read. Waits for a
      pre-1930 text on the AME union of 1896 and on Coker's voyage of 1820.
    - **VII.32's end date (1890) checked against 1906** (G89-49 a). The end rests on an 1890 manual;
      Wiebe (1900) tells the Russian years only to 1876. The end is not moved. Waits for an inside
      Mennonite source dated 1891-1906.
    - **RV-5, other Moravian fields: Greenland, Nicaragua (the Moskito Coast), Ladakh, Alaska,
      Australia** (G89-4 a). The record names five lines and only those are drawn; the others are
      [S]. Hamilton covers some. Waits for a decision to widen the lines, then a read of the
      matching chapters of Hamilton (1901).
    - **RV-4, the Egypt synod date and the Evangelical Church of Egypt's later history** (G89-50 a).
      The synod date is [S]; no sentence uses it. Waits for a dated Egypt church source after 1863
      and an Arabic own voice, for example Bustani, for Syria.
    - **Wanted:** an Arabic text from the evangelical churches themselves, and Rufus Anderson,
      History of the Missions of the American Board to the Oriental Churches (1872), listed but not
      opened; a Coptic voice on 1867, and Guirguis and van Doorn-Harder (2011) to test the
      Watson-only links; J. Taylor Hamilton (1901) as a vendoring candidate, since every RV-5 quote
      rests on the online copy and nothing Moravian after 1815 is in `cic/texts/`; P. M. Friesen,
      Die Alt-Evangelische Mennonitische Bruderschaft in Russland (1911), and the charter of 1800; a
      Liberian or Black American own voice (a published letter or church minute) so that Lott Cary
      can be a people row, with Taylor (1837) as a vendoring candidate; Cranz and La Trobe (1780),
      already in the Library, for a Greenland line. The dated record for the Arab evangelical
      churches is in "New rows marked living with no dated source" (2026-11-10).
179. **Missing modern-country IDs (2026-11-10).** A new row's modernCountries takes IDs from census
    rows only, and each country's place must be on the row's place label. No census row carries the
    countries and places below, so they are left out. Owner: the place-label work.
    - **Africa:** kongo-christianity-after-1650 (Angola, DR Congo);
      the-dutch-reformed-church-at-the-cape (South Africa); southern-african-mission-churches (South
      Africa, Lesotho). All three lists are empty.
    - **Latin America:** caribbean-churches-of-slavery-and-emancipation (Jamaica, Guyana). The list
      is empty, though Jamaica is on its label. Jamaica Q766 is copied in only if a row that enters
      carries it.
    - **Asia:** chinese-catholicism-1650-1906 (China). VI.13c and IX.65 are empty too; adding a
      China ID to the census place data lets all three be filled. vietnamese-catholicism-to-1815 and
      vietnamese-catholicism-1815-1906 (Vietnam; no ID in the repo). catholics-of-dutch-ceylon (Sri
      Lanka Q854, Jaffna Q215277, Puttalam Q3088741, found in
      `Build/Ministry/Operations/Audits/2026-11-07_place-labels/countries-by-place.json`, not on a
      census row). protestant-churches-of-the-voc-world has Java only; Ambon and the Moluccas have
      no ID.
    - **Eastern Europe:** hungarian-and-transylvanian-protestantism-1650-1815 (Hungary, Slovakia);
      polish-and-lithuanian-catholicism-under-the-partitions (Lithuania); old-believers-after-1815
      (Romania, for the Danube settlements; the place has no census ID and is not on the label).
    - **Roman Catholic worlds:** society-of-jesus-1650-1814 (Paraguay);
      catholics-of-the-ottoman-balkans (Bosnia, Slavonia). The reviewer re-checked four IDs on
      Wikidata on 2026-11-10: Paraguay Q733, Bosnia and Herzegovina Q225, Croatia Q224 and Slavonia
      Q681964. They are ready to add once the rule allows IDs from outside the census.
    - **Moravians and Arab evangelicals:** moravian-church-after-1815 (Jamaica Q766, South Africa
      Q258 with Genadendal Q1501295, Suriname, Tanzania, Germany with Saxony Q183 / Q1202, Canada
      Q16); arab-evangelical-churches (Syria Q858, which is also not on its label); VIII.7
      (Liberia). Jamaica and South Africa were looked up in the place-label audit, not the census.
      Suriname, Tanzania and Liberia have no ID in the census or the audit.
180. **VII.32's Russia and Ukraine (2026-11-10).** Ruling G89-49 a adds Russia (Q159) and Ukraine
    (Q212) to VII.32's row. The text is added. The countries cannot sit on the row's two-place label
    (Netherlands · Pennsylvania and beyond) under the validator's place-label rule, and changing the
    frozen label is not in the ruling. Waits for a place-label decision: a rule that allows more
    than two places, or a ruling to change the label. Owner: the place-label work.
181. **Two links with a candidate secondary quote (2026-11-10).** Widely Accepted needs a secondary
    quote. Each candidate below was added after the slice reviews closed and the coordinator ruled
    it out of this release, so both links enter at Inferential-Thin. For the follow-up chunk, under
    a fresh review.
    - **chinese-catholicism-1650-1906 to society-of-jesus-1650-1814.** Candidate: The Catholic
      Encyclopedia, vol. 3 (New York: Robert Appleton Company, 1908), article "China", the Jesuits
      at the court of Peking. Quote: "The Jesuits, as astronomers or interpreters were in high
      favour at Court". Public domain. File: `raw/cathen3.txt`. URL:
      https://archive.org/download/catholicencyclop0003char/catholicencyclop0003char_djvu.txt
      (accessed 2026-11-10).
    - **southern-african-mission-churches to the-moravian-church-at-herrnhut.** Candidate: J. Taylor
      Hamilton, A History of the Missions of the Moravian Church during the Eighteenth and
      Nineteenth Centuries (Bethlehem, Pa.: Times Publishing Co., 1901), Chapter I, Schmidt at the
      Cape. Quote: "Whilst Schmidt was laboring to overcome the prejudices of whites and reach
      heathen hearts at the southern end of the continent". Public domain. File:
      `raw/hamilton1901.txt`. URL:
      https://archive.org/download/historyofmission00hami/historyofmission00hami_djvu.txt (accessed
      2026-11-10).
182. **New rows marked living with no dated source (2026-11-10).** Ten new entries are marked living
    with livingEvidence graded "none (no dated item after 2010 found)". Each wants a dated
    present-day source to grade CD or CR. Owner: P2-V's follow-up.
    - kongo-christianity-after-1650: a dated statement of the Catholic Church in northern Angola and
      the lower Congo, for example the diocese of M'banza-Kongo.
    - the-dutch-reformed-church-at-the-cape: a dated statement of the Dutch Reformed Church (NG
      Kerk).
    - southern-african-mission-churches: a dated statement of the Moravian, Presbyterian, Methodist
      and Lesotho Evangelical churches.
    - caribbean-churches-of-slavery-and-emancipation: a dated own-voice item after 2010, for example
      the Jamaica Baptist Union or the Methodist Church in the Caribbean and the Americas.
    - vietnamese-catholicism-1815-1906: a dated statement of the Catholic Bishops' Conference of
      Vietnam.
    - catholics-of-dutch-ceylon: a dated statement of the Catholic Bishops' Conference of Sri Lanka.
    - protestant-churches-of-the-voc-world: a dated record of the Protestant Church of the Moluccas,
      and a source for its descent from the Company's church.
    - hungarian-and-transylvanian-protestantism-1650-1815: a dated record for the Reformed Church in
      Hungary and the Lutheran churches; the mark now rests on the record's word alone.
    - catholics-of-the-ottoman-balkans: a dated present-day source on the Catholic Church in Bosnia
      and Croatia.
    - arab-evangelical-churches: a dated item from the National Evangelical Synod of Syria and
      Lebanon or the Evangelical Church of Egypt.
183. **VIII.52 runs to 1911, past era 9's end (2026-11-10).** Open. The sweep record flags it
    (section 10) and no gate question covers it.
184. **Two North Europe breaks stay open (2026-11-10).** The Scottish church after 1650 and the
    Swedenborgians after 1815 have no entry. The ruling left both open. For a North Europe pass,
    with the Toleration churches of Bohemia and Moravia in "Eras 8 and 9 rulings, Moravians, Arab
    evangelicals and Mennonites holds" (2026-11-10).
185. **Held items whose sources the Library now holds (2026-11-10).** The Library's batch 2 (PR
    #1579) vendored sources for ME-20, ME-6 (the Dukhobors), RV-7, AP7, AP15, AP12 (in part), AP11,
    LA8-6, LA8-8 and LA8-9. All stay held as ruled; their holds are in the region items "Eras 8 and
    9 rulings, Africa holds" to "Eras 8 and 9 rulings, Moravians, Arab evangelicals and Mennonites
    holds" (2026-11-10). A follow-up chunk enters them after this release. List:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`.
186. **Years logged for other eras' owners (2026-11-10).** Holds that name an owner outside this
    sweep. Nothing is drafted for them.
    - **The Coptic church, c. 1300-1517 (the Mamluk years)**, between
      coptic-christianity-fatimid-to-mamluk and the-coptic-church-under-the-ottomans (G89-8 a). AF-2
      starts at 1517 by Mark's leave. Owner: the era 6 owner. See "Coptic and Ethiopian map gaps"
      (2026-11-08); AF-1 and AF-2 close the rest of that break.
    - **The Maronite years 1517-1650 (the Maronite College in Rome, 1584; the councils of 1596 and
      1616)** (G89-39 a). Owner: the era 7 owner, as a separate change order.
    - **The Romanian Greek Catholic Church, 1906-1948**, between ME-8's era 9 row and IX.73 (G89-41
      a). The continued-as link crosses years no row tells. Owner: the era 10 owner.
    - **Polish Catholicism, 1906-1918**, between ME-10 and IX.70 (G89-40 a). Same crossing. Owner:
      the era 10 owner.
    - **The Bulgarian union of 1860-61 as a line in VIII.28** (G89-51 a). Owner: the owner of
      VIII.28, or the era 9 part of RV-3.
187. **The VOC lineage question put to Mark (2026-11-10).** G89-27 a names no successor for the
    Reformed church of the VOC world. The record marks the descent from it to the Protestant Church
    of the Moluccas as [S]. Aritonang ch. 9 describes Joseph Kam's work from 1815 as a
    rehabilitation of the same church, which reads as continuity, but VIII.26's own subject is
    mainly the new mission churches. The tree has no entry for the Moluccan church between 1815 and
    1861. No link is drafted. The question: should AP5 (protestant-churches-of-the-voc-world)
    continue as VIII.26?
    - Yes: a "continued as" link, at most Widely Accepted, with the 1815-1861 gap named.
    - No: AP5 stands without a successor and the gap stays open. The living mark waits for a dated
      record of the Protestant Church of the Moluccas.
188. **Small questions the eras 8 and 9 rulings leave open (2026-11-10).** None changes what
    entered. Each is a choice the ruling did not name. Owner: the coordinator, for Mark where
    marked.
    - VII.2 (Danish-Halle mission) keeps its dates, 1675-1750, as the ruling names no date change.
      Its new line on Indian ordinations reaches 1813. For Mark: move the end, or keep it.
    - VII.17 (New Spain and Peru) now has the place label "Peru · Brazil and beyond", because a
      label holds two places and each country needs its place on it. Its short name still reads
      "New Spain & Peru". For Mark: another label or short name.
    - The Caribbean churches row carries no `kind`, like the Black Church in America row. A
      "cross-church movement" kind would fit it only loosely. For Mark.
    - Two open-access modern studies (Aritonang and Steenbrink 2008; Dutton 2017) carry sentences
      in the Asia rows, as the sweep record cites them. Their archive.org records state no license,
      so their sources carry none. The Library thread may record the licenses.
    - Frozen paragraphs that changed rows carry unchanged still score below the reading target,
      for example VIII.7, VIII.27, VII.2, VII.19, VIII.29, VIII.31, VIII.32 and VII.23's teaser.
      The ruling did not name them. They wait for a readability pass on frozen text.
