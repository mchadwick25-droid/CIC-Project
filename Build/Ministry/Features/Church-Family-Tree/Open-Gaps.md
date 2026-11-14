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
171. **What the Library's second wants batch filled (2026-11-10).** For the eras 8-9 rows held for
    sources (`CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`). Full list:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`.
    - Filled: ME-20 (Tolstoy 1885, 1894), ME-6 for the Dukhobors (their Living Book, 1909), RV-7
      (Bishop Ferencz 1875, 1907), AP7 (Mackenzie 1901, and Whitehouse 1873 shelved), AP15 (Dallet
      1874, the Korean Repository 1896, Underwood 1908), AP12 in part (Marsden's letters, 1913), AP11 to
      1808 (Adoratskii 1887), LA8-6 (Moreau 1797, Holly's report of 1874), LA8-8 (Claret 1863), LA8-9
      (Montalvo 1683, the Historia Bethlehemitica 1723).
    - The church's side only: LA8-10 (Juarros 1809, Garcia Pelaez 1852). The Cancuc and Cruzob texts
      themselves are still wanted.
    - Not found: AF-8, ME-4, ME-7, RV-9, AP10, AP13 and the Molokans. ME-21 is located but not
      fetched.
    - The Bell Part II ruling, as carried out: the row stays on the desert shelf as context, and on
      the Melitian shelf as tradition (Source-Library Decision-Log, 2026-11-10).
172. **What the Library's third wants batch filled (2026-11-10).** For the earliest named gaps in
    "Living traditions with no entry after a date" (2026-11-10). Each gap still needs a change order
    to add its row; the Library supplies the sources. Full list:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`.
    - Sources now held: Rome 604-1049 (Liber Pontificalis, Duchesne); the Frankish church 888-1049
      (Regino about 906, Flodoard 919-966); Benedictines after 604 (Cluny charters); Ireland after
      1169 (the Four Masters 1172-1378, Thurles 1850); Wales after 1282 (the Welsh Bible 1588 and the
      Prayer Book 1664); the Mozarabs after 1031 (the liturgy; Toledo deeds of the 12th-13th
      centuries); Lerins (its charters from the 11th century; Barralis 1613); Antioch after 312 and the
      Arabic Melkites (Paul of Aleppo, held); Jerusalem after 450 (Sophronius 634; the patriarchate's
      acts from 1670; Dositheus, held); Georgia 1245-1917 (Brosset part II, 1857); the Judean desert
      after 614 (Antiochus Strategos; George of Choziba, held).
    - Not found: the Syriac Orthodox Church 1300-1915.
    - Bears on "The Lerins entry says the abbey has stood since about 410" (2026-11-10): the
      cartulary and Barralis date the house's life after 450.
    - AP10 (Hermano Pule): Montero y Vidal 1895 summarises Apolinario's sworn declaration. ME-21
      (Rabinowitz): six full-view Google Books items need a browser download.
173. **Descent links the river origins want (2026-11-10).** From "Where each river leaves its parent"
    (Decision-Log, 2026-11-10). Each would let a census link, not a declared record, place a river.
    Each is a census change under the link evidence standard: sourced, reviewed, and given a data
    release. None is invented here.
    - A break link from the late-medieval Latin church to Lutheran Wittenberg. The census has only
      Wittenberg "argued against" the Tridentine church. Protestant & Evangelical already comes from
      Latin West through the Hussite "continued as" link to the Czech churches, so this changes no
      parent. It would make Luther's own break visible on the map.
    - A "gave rise to" link from the Cappadocian church at Caesarea to the Armenian conversion era.
      It would rest on Gregory the Illuminator's consecration at Caesarea, and must carry the
      Armenian church's own reading (an apostolic see, revived and not founded). Caucasus is
      declared from Greek East as Contested until then.
    - The start of Syriac East, Greek East and Africa, each declared from the origin trunk. A census
      link from a first-century trunk movement would place them by lineage, if a source supports one.
174. **The river record's declared reasons are not shown to visitors (2026-11-10).** Each declared
    river origin carries a reason, a confidence and a source, kept as data in the page. The map does
    not yet show them, for example in the Rivers key. Whether it should is a front-end question for
    Mark.
175. **Eras 8 and 9 rulings, Africa holds (2026-11-10).** P2-G89b (data release 33) carried out
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
176. **Eras 8 and 9 rulings, Latin America holds (2026-11-10).** From the same draft. Each hold
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
177. **Eras 8 and 9 rulings, Asia part 1 holds (2026-11-10).** India, China, Japan, Korea and the
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
178. **Eras 8 and 9 rulings, Asia part 2 holds (2026-11-10).** Southeast Asia, the Pacific and the
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
179. **Eras 8 and 9 rulings, Middle East and Caucasus holds (2026-11-10).** Slice ME-1.
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
180. **Eras 8 and 9 rulings, Eastern Europe and Russia holds (2026-11-10).** Slice ME-2.
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
181. **Eras 8 and 9 rulings, Catholic missions and the Society of Jesus holds (2026-11-10).** Slice
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
182. **Eras 8 and 9 rulings, Moravians, Arab evangelicals and Mennonites holds (2026-11-10).** Slice
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
183. **Missing modern-country IDs (2026-11-10).** A new row's modernCountries takes IDs from census
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
184. **VII.32's Russia and Ukraine (2026-11-10).** Ruling G89-49 a adds Russia (Q159) and Ukraine
    (Q212) to VII.32's row. The text is added. The countries cannot sit on the row's two-place label
    (Netherlands · Pennsylvania and beyond) under the validator's place-label rule, and changing the
    frozen label is not in the ruling. Waits for a place-label decision: a rule that allows more
    than two places, or a ruling to change the label. Owner: the place-label work.
185. **Two links with a candidate secondary quote (2026-11-10).** Widely Accepted needs a secondary
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
186. **New rows marked living with no dated source (2026-11-10).** Ten new entries are marked living
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
187. **VIII.52 runs to 1911, past era 9's end (2026-11-10).** Open. The sweep record flags it
    (section 10) and no gate question covers it.
188. **Two North Europe breaks stay open (2026-11-10).** The Scottish church after 1650 and the
    Swedenborgians after 1815 have no entry. The ruling left both open. For a North Europe pass,
    with the Toleration churches of Bohemia and Moravia in "Eras 8 and 9 rulings, Moravians, Arab
    evangelicals and Mennonites holds" (2026-11-10).
189. **Held items whose sources the Library now holds (2026-11-10).** The Library's batch 2 (PR
    #1579) vendored sources for ME-20, ME-6 (the Dukhobors), RV-7, AP7, AP15, AP12 (in part), AP11,
    LA8-6, LA8-8 and LA8-9. All stay held as ruled; their holds are in the region items "Eras 8 and
    9 rulings, Africa holds" to "Eras 8 and 9 rulings, Moravians, Arab evangelicals and Mennonites
    holds" (2026-11-10). A follow-up chunk enters them after this release. What the batch found:
    "What the Library's second wants batch filled" (2026-11-10).
190. **Years logged for other eras' owners (2026-11-10).** Holds that name an owner outside this
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
191. **The VOC lineage question put to Mark (2026-11-10).** G89-27 a names no successor for the
    Reformed church of the VOC world. The record marks the descent from it to the Protestant Church
    of the Moluccas as [S]. Aritonang ch. 9 describes Joseph Kam's work from 1815 as a
    rehabilitation of the same church, which reads as continuity, but VIII.26's own subject is
    mainly the new mission churches. The tree has no entry for the Moluccan church between 1815 and
    1861. No link is drafted. The question: should AP5 (protestant-churches-of-the-voc-world)
    continue as VIII.26?
    - Yes: a "continued as" link, at most Widely Accepted, with the 1815-1861 gap named.
    - No: AP5 stands without a successor and the gap stays open. The living mark waits for a dated
      record of the Protestant Church of the Moluccas.
192. **Small questions the eras 8 and 9 rulings leave open (2026-11-10).** None changes what
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
193. **What the Library's fourth wants batch filled (2026-11-10).** For the religious orders and the
    Maronites in "Living traditions with no entry after a date" (2026-11-10). Each gap still needs a
    change order to add its row; the Library supplies the sources. Full list:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`, batch 4.
    - Sources now held:
      - Athos after 1300: Meyer's typika and patriarchal acts, 1394 to the late 18th century;
        Dapontes, a Xeropotamou monk.
      - The Carthusians after 1534: Chauncy (1550); the statutes of 1681.
      - The Cistercians after 1300: Rance (1683); the Trappist constitutions (1894).
      - The Maronites after 1517: al-Duwayhi's history.
      - The canons regular after 1246: Barnwell (1295-96); the Premonstratensian statutes (1626).
      - The Order of Malta after 1291: the statutes of 1589.
      - The Carmelites after 1300: the general chapters, 1318-1593.
      - The Franciscans after 1517: the Annales for 1540-1553; the Capuchin constitutions (1638).
      - The Dominicans after 1300: the general chapters, 1304-1378 and 1601-1628.
      - The Jesuits after 1650: Thwaites 36-40; the Memoires de la Chine, 1717-1731, shelved on
        the Society of Jesus 1650-1814 entry, and the China letters also on Chinese Catholicism
        1650-1906. Thwaites also serves New France after 1650.
      - The Discalced Carmelites after 1622: Brother Lawrence; the Reforma, tome II (1655).
    - For the census owner: the Compiegne history (1836) sits on the ancien-regime shelf, which ends
      in 1815. A census story rests on that row, so it was left; the long-nineteenth-century shelf was
      added beside it.
194. **The held eras 8 and 9 items the Library's sources now carry (2026-11-10).** P2-G89c (data
    release 34) tested each item in "Held items whose sources the Library now holds" (2026-11-10)
    against its vendored source, and entered what the source carries. Audit:
    `Build/Ministry/Operations/Audits/2026-11-10_eras8-9-sourced/`.
    - **Entered:** RV-7, the Transylvanian Unitarian Church 1660-1906, a lane 8 row (Ferencz 1875
      and 1907; Rees 1818), continuing the anti-Trinitarian entry; AP11 to 1808, a line in the
      Russian church from Nikon to the Holy Synod (Adoratskii 1887); AP10, the Cofradia de San Jose,
      a line in Philippine Catholicism 1815-1906 (Montero y Vidal 1895, which prints the intendente's
      letter of 1841 and the parish priest's Relacion); AP15, the Protestant beginnings in Korea, a
      line in the Missionary Movement's Native Churches (Underwood 1908, for events to 1890; the
      Korean Repository 1896); AP12, the Anglican line only, in the Victorian Church of England
      (Marsden's letters, 1814-1837; three dates are his biographer's and are named so); LA8-6,
      Saint-Domingue before 1789 in Colonial Latin American Devotional Catholicism (Moreau 1797) and
      Holly's Haitian Episcopal church in the Black Church in America (the Spirit of Missions,
      December 1874); LA8-9, the Bethlemites, a line in Colonial Latin American Devotional
      Catholicism (Montalvo 1683; Garcia de la Concepcion 1723, the bull of 26 March 1687 read on
      the page image).
    - **Held, the source does not carry it:**
      - AP7, the Catholic St Thomas Christians 1815-1906. Mackenzie (1901) prints no Catholic
        document word for word: one clause of the 1861 rescript, and Roccos's signature. Waits for
        a Catholic source (Propaganda's acts on Malabar, Syro-Malabar writings, Chavara).
      - LA8-8, Cuba and Puerto Rico. Claret's Apuntes (1863) is a rule for governing a diocese; it
        says nothing of the church under the crown's patronage, of Puerto Rico's church or of 1898.
        Waits for a dated source on the Cuban church under Spain, 1815-1898.
      - AP11 after 1808, the line in the Russian church's synodal century. No later issue of
        Adoratskii is held. Waits for it, or Widmer (1976).
      - AP15, the Korean Catholic church after 1886. Korean Catholic Origins ends in 1886 and its
        status text keeps 1886-1904 for a later entry. Sources found for that entry: Father
        Coste's obituary in the Korean Repository (1896; the chapel of 1888, the seminary of 1891,
        the cathedral stone of 1892) and Underwood's count of over 42,000 Catholics in 1901.
      - AP12, the Catholic and Methodist lines and the Aboriginal missions. No source.
      - LA8-6, the Catholic concordat church after 1860 (no French Catholic source; the Concordat
        printing not found); Holly's emigration of 1861 (not in the 1874 issue); the Code Noir and
        Bois Caiman (not read or not found).
      - LA8-9 after 1723: the order's end in 1820 and its spread (Garcia's later books damaged).
      - AP10: the founding year 1832, the name Hermano Pule, and the bar from Spanish orders (not
        in Montero's pages). The Cofradia's own letters were seized in 1841; none is held.
      - AP15: the Nevius plan's rules and date, and the Ross New Testament's date (Underwood's
        "worked well" is a judgment of 1908, not used).
    - **Links RV-7 waits for:** English Unitarians after 1813, the Dutch Remonstrants after 1650,
      and the era 9 Hungarian Protestant row (each has no entry yet); a link from the Society of
      Jesus waits for a Catholic or Habsburg source on the seizures of 1693 and 1716, since only the
      Unitarians' own later account blames the Jesuits.
    - **Also closed:** "Two links with a candidate secondary quote" (2026-11-10): both quotes were
      re-checked word for word and both links are now Widely Accepted. "The VOC lineage question
      put to Mark" (2026-11-10): ruled yes by the coordinator; the VOC world's churches continue as
      Indonesian Christianity, Widely Accepted on Aritonang and Steenbrink, with 1815-1861 named as
      untold. The living mark there still waits for a dated record of the Protestant Church of the
      Moluccas.
    - This closes "Held items whose sources the Library now holds" (2026-11-10) for every item but
      those above.
195. **Two Section A questions for Mark: the Tolstoyans and the Dukhobors (2026-11-10).** The
    Library's texts now let each be assessed. Nothing is entered. The full assessment, with every
    quote at its lines: `Build/Ministry/Operations/Audits/2026-11-10_eras8-9-sourced/SectionA_ME6_ME20.md`.
    Owner: the coordinator, for Mark.
    - **ME-20, the Tolstoyans** (G89-48 a: "out of scope under A1 unless Mark chooses a lane 8
      entry"). Tolstoy's own words (1885, 1894) bear out the record's report in substance: Christ a
      teacher, "Son of God" a nature all men share, the bodily resurrection denied. No Tolstoyan
      community's own confession is in the Library.
    - **ME-6, the Dukhobors** (G89-46 a: "route the Dukhobors to Mark under A4 if they do not
      clear"). Their Living Book calls the Son "our God", equal to the Father, but reads his birth,
      death and rising as happening "in us" and refuses the sacraments in outward form. A1's plain
      denial is not met; A3 (a non-literal reading) and A4's one-commitment limit are the live
      questions. The Living Book is dated 1909 and its scan is unchecked, so none of it can enter a
      record yet. The Molokans' texts were not found.
196. **Small points P2-G89c leaves open (2026-11-10).** None changes what entered.
    - The Transylvanian Protestants' entry (1650-1815) still says "The Unitarians are a different
      church, told to 1650." It is now told to 1906. A frozen row; for a change order.
    - The anti-Trinitarian entry says the Polish Brethren were expelled in 1658. Rees dates the
      first decree to 1658 and the order to leave at once to 20 July 1660; Ferencz dates the ban to
      1659 and the last day to 10 July 1660. A frozen row; for a change order.
    - Underwood's Call of Korea (1908) stays `needs-ruling` on the Missionary Movement's shelf, which
      ends in 1906. Korean Protestantism in the Twentieth Century (1907-2010) covers its date of
      writing. For the Library thread.
    - Adoratskii's OCR keeps its errors in the quotes ("1115" for 1715, and others). The reviewer
      checked every date-bearing quote on the page images; two lines were not checked.
    - No country was added to any changed row: Korea, Australia, New Zealand, Haiti, Guatemala and
      China are not on the rows' place labels. Owner: the place-label work.
197. **Narration scope (Mark, 2026-11-10).** Mark, 2026-11-10, verbatim: "the counsels are stories i
    think" and "we need a minimum of a minute explanations on everything, then stories more, and
    longer ones on built worlds"; "this will be work next week". Coordinator note: the councils and
    other multi-tradition events are the Shared Events workstream (`Build/Ministry/Features/Shared-Events/`,
    charter 2026-10-17); major links would point to their event's story, the link note staying as
    evidence. Scheduled for the week after 2026-11-14. See also "Design idea: a brief that plays
    first, then an optional deeper story" (2026-11-10).
198. **What the Library's fifth wants batch filled (2026-11-10).** For ME-21 and the early modern mission
    and Eastern gaps in "Living traditions with no entry after a date" (2026-11-10). Full list:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`, batch 5.
    - ME-21 (Rabinowitz): the source the hold waits for is now held, opened raw. It includes the
      Documente of 1884 with the Hebrew originals, the letters of 1884, and the autobiography and
      sermons. The Hebrew letters are still wanted.
    - Now shelved on the new eras 8-9 entries: the St Thomas Christians (Paulinus 1794, Buchanan 1811,
      and held texts); Kongo after 1650 (Paiva Manso's documents after 1651, with the Count of Soyo's
      letters; Bentley 1900; held Capuchin accounts); Japan's hidden Christians (Marnas 1897);
      Chinese Catholics (Launay 1907, the Propaganda Collectanea).
    - New France after 1650: the Quebec bishops' mandements from 1659 and Marie de l'Incarnation's
      letters, on the ancien-regime church.
    - Ukrainian Orthodoxy after 1700: documents of the 1720s-1770s, `needs-ruling` on the Russian
      church's 1652-1815 entry.
    - Not found: a Chinese Catholic's own text, a Puthenkoor text of its own, Kongolese texts other
      than the Paiva Manso letters, hidden Christian prayers in print before 1931, and Ukrainian
      church print from 1918 to 1930.
    - Correction to "What the Library's fourth wants batch filled" (2026-11-10): al-Duwayhi was
      already held. The batch 4 file is a second scan of the same edition.
199. **What the Library's sixth wants batch filled (2026-11-11).** For the Europe 1650-1815 gaps in
    "Living traditions with no entry after a date" (2026-11-10). Full list:
    `Build/Ministry/Features/Source-Library/CFT-Wants.md`, batch 6.
    - Own-voice texts now held: the Transylvanian Unitarians (Keresztény Magvető 1861, the 1889
      marriage law, Főtanács minutes 1909-1913); the Waldensians (Arnaud's Glorieuse rentrée, French and
      English); the Schwenkfelders (the 1879 register, Schultz's chronicle in Seipt); the Remonstrants
      (Limborch, the Brotherhood's register and gedenkboek); the Church of Scotland (the Acts 1638-1842,
      Wodrow III, Boston's memoir); English Catholics (Milner 1818); the French Reformed (the 1872 synod,
      Vincent); the Delaware Swedes (Holy Trinity's records to 1810, Clay).
    - Outsiders or histories only: the Hutterites after 1785 (Wolkan 1918); the Nordic state churches
      (Cornelius, Helweg).
    - Most of these have no entry after their first window, so the texts wait unshelved for one.
    - Held for Mark: the Schwenkfelder sacrament rules (a licence on the upload).
    - Not found: an insider Hutterite print before 1931; the 1762 Schwenkfelder hymnal; the Church Law
      of 1686, Pontoppidan, Kingo, Brorson; Kirk's Biographies.
    - Shelf ruling on Marsden (P2-G89c): see the Source-Library Decision-Log, 2026-11-11. The Victorian
      Church of England entry quotes two letters of 1814, before its window; this is for the census owner.
200. **What the 2026-11-11 recording batch leaves for later (2026-11-11).** The batch recorded every
    tradition brief and documented story whose text had changed or had no recording. That settles
    "176 story recordings wait for the ElevenLabs quota to reset" (2026-11-09). Still open:
    - **Person briefs.** All 39 are rewritten to the person-brief standard (Decision-Log,
      "Person briefs: 60 to 120 seconds, personal and theological", 2026-11-11), then recorded
      together in David Baker's voice (`fxnZk29PIJ3WKEC9MDEo`).
      - The tree planner leaves out person rows until then. The exclusion comes out, and a
        required `--person-voice-id` comes in, with that work.
      - Tertullian's existing brief plays in Daniel on the live site until it is replaced.
    - **Councils and new stories.** They have no census text yet (Shared Events, see "Narration
      scope", 2026-11-10). They get their own sample and run once written.
    - **8 movements with no `longDescription`.** No brief is recorded until text is written:
      armenian-christianity-before-the-bagratids, medieval-irish-christianity,
      medieval-welsh-christianity, church-of-the-east-under-the-abbasids,
      kongo-christianity-afonso-to-1650, kirishitan-japan, china-mission-born-christianity,
      new-spain-and-andes-mission-born-christianity.
    - **The 62 gap stories** (`cic-website/audio/stories/`) store no text fingerprint, so a
      changed text does not show which recording is stale.
    - **Orphan manifest keys.** One tree key (`deconstruction-and-ex-vangelical-communities`) and
      12 story keys belong to retired or built rows. They cost nothing and play nowhere.
    Owner: the recording thread.
201. **What the people layer leaves open (2026-11-11).** P2-P builds Mark's Who design (Decision-Log,
    "The people layer: Who beside every tradition and river (P2-P)", 2026-11-11). Still open:
    - **Card data for everyone else.** Only the 10 pilot people carry a `card`. The other 29 person
      entries, and the named voices, show what exists until their cards are written to the pilot's
      standard. Owner: the person-brief rewrites.
    - **A named voice's own Library works.** A voice whose words sit on a Library shelf (`held`)
      shows no works on its card. The map holds the row's ID but not the work's title. Voices quoted
      from a source show that source's work. Owner: P2-P follow-up; a choice between mirroring the
      title into the map's data and loading the shelf at run time.
    - **The Basil link.** `desert-monasticism--iconophile-byzantine-monasticism` concerns Basil of
      Caesarea, who is told within neither end. The map draws it between the two traditions, and
      Basil's card lists it under "Links on the map". Owner: the census owner, whether `concerns`
      should stay on that link.
    - **Voices joined to entries by name.** Rows that name a person entry as a plain voice (for
      example Athanasius in the rows of the Aksumite church and the Coptic church) are joined to the
      entry on the map by name and date. They are not joined in the census. Owner: the census owner,
      whether those rows should point to the entry.
    - **Voices of built worlds.** The map leaves a built world's `voices` lines out, so a person
      named only by a built world (24 rows, for example the post-apostolic house church's) shows
      "Also named by …" on their card, without that world's own line. Owner: P2-P follow-up.
    - **A tradition that names no one** has no profile pill, and its card's Who button reads "Who ·
      no one named". Mark sees this in the screenshots.
202. **One man spelled two ways in the people rows (2026-11-11).** Sulpicius Severus is "Sulpitius
    Severus" in the rows of `gallic-nicene-episcopate` (year 403) and
    `gallic-monastic-ascetic-christianity` (year 397), and "Sulpicius Severus" in the row of
    `priscillianist-asceticism` (year 403). The census's links and sources spell him "Sulpicius".
    The Who stacks join people by name, so he shows as two people, with two cards. Owner: the
    census owner (one spelling, and whether the years should agree).
203. **The Who sweep (2026-11-11).** Mark set the test for a Who (Decision-Log, "Who a Who is: the
    record stands on its own", 2026-11-11). Until every person is sorted against it, Who shows
    only the 39 person entries.
    - The work: a read-only sweep after Friday 2026-11-13. It sorts every person in the census
      into Who, story or wanted. That covers the 39 person entries and the named voices in every
      tradition's `people` list. Each call rests on the body of work the Library holds: their own,
      recorded by hearers or disciples, produced with their circle, or carried by a following. Mark
      sees the result, with any exceptions or missing categories.
    - Waiting on it: the named-voice items in "What the people layer leaves open" (2026-11-11) and
      "One man spelled two ways in the people rows" (2026-11-11).
    - Lifting the display rule (`WHO_ENTRIES_ONLY` on the map and the tree pages) follows Mark's
      call on the result.
    - Owner: the coordinator.
204. **The era 1 Who scan's wanted sources (2026-11-11).** Four people would be a Who if the Library
    held one named source. Owner: the Library thread.
    - Melito of Sardis: *Peri Pascha* (Perler, Sources Chrétiennes 123, or Bonner 1940). Only
      fragments are held, in `anf08`.
    - Ptolemy the Valentinian: Epiphanius, Panarion 33, which holds the Letter to Flora (Holl, GCS
      25, 1915). The Library's Epiphanius files start at heresy 34.
    - Paul of Samosata: his fragments in Loofs, *Paulus von Samosata* (1924). The Loofs 1905 file in
      the Library is *Nestoriana*, not this.
    - Mani: his followers' own texts, the Cologne Mani Codex (Koenen and Römer 1988), the Kephalaia
      or the Manichaean Psalm-Book. Augustine and the Acts of Archelaus are one witness for his
      life.
    - Mark's rule: a source counts only if it can carry a life, not only writing (the coordinator's
      routine call, open to Mark).
    - Source: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era1/`.
205. **Pamphilus's Apology for Origen: is an English text held in `npnf203`? (2026-11-11).** The
    Opus check of the era 1 Who scan reported an English Apology in `npnf203`, section vi.v. The
    Decision-Log ("The later-worlds people ruled (P2-G3b)", 2026-11-10) and "The later-worlds people
    held, with their reasons" (2026-11-10) say that file holds only Rufinus's preface and epilogue.
    The scan did not rely on it. Open: open `npnf203` at vi.v and say which is true. Owner: the
    Library thread.

206. **The era 2 Who scan's wanted sources (2026-11-11).** Two people would be a Who if the Library
    held one named source. Owner: the Library thread.
    - Gregory the Illuminator: Agathangelos, *History of the Armenians* (Thomson, 1976). Only later
      retellings are held (Moses of Khoren, Chamich).
    - Ezana of Aksum: his Ge'ez inscriptions (Littmann, *Deutsche Aksum-Expedition* IV, 1913, or RIE
      270–271).
    - Mesrop Mashtots left this list: the check found Koriun's Life held in French (Langlois, tome
      2), so he is WHO as a judgment call.
    - Source: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/`.
207. **Jovinian's live profile comes down (2026-11-11).** Mark: "Take it down". Jovinian is LISTED:
    his book is lost and four points of doctrine survive in opponents. The profile comes down in a
    later release; no site change is made by the scan. Owner: the coordinator, for the release.
208. **Councils as tradition-like entries with their own icon and title; participants on their Who
    click (2026-11-11).** Mark: "counsels are treated like a tradition with a different icon and
    title. but people who are a part of it should be on the who click". Making councils a census
    entry kind is later work for the map and data, and a change order on frozen eras. The era 2
    scan lists 13 councils with their participants. Also named in era 2 text and not yet
    tabulated: Gangra (c.340), Rome (377), Paris (c.360), the Donatist council that condemned
    Tyconius (c.380), Saragossa (c.380), Toledo (400), Constantinople (383), the African councils
    of 418 and the Persian synod of 424. Owner: the coordinator.
209. **Pliny the Younger: open judgment call (2026-11-11).** A governor's report, not a historian's
    work, so not decided under the OUTSIDE WITNESS label. The letter (Ep. 10.96 and Trajan's reply)
    is held only inside McGiffert's note 891 to Eusebius III.33 (`npnf201`, lines 19451–19533). If
    he is WHO, an edition of Pliny, Book 10, is the source wanted. Owner: Mark's call, then the
    Library thread.
210. **Other open points from the era 2 scan (2026-11-11).** Owners as noted.
    - Recorders under Mark's ruling, era 1: Pontius the Deacon is rescored WHO in the era 1
      addendum. Philip (Bardaisan's pupil) and Hegesippus may fall under the same ruling and are
      not yet retested. Owner: the coordinator.
    - Better sources than the ones held: the Pachomian Lives (Greek), Antony's letters, Possidius's
      Indiculus (PL 46), Libanius's orations and letters, Porphyry's fragments, an edition of
      Josephus checked against a critical text. Owner: the Library thread.
    - Shapers named in no era 2 census text and so not scored: Ossius, Alexander of Alexandria,
      Liberius, Marcellus of Ancyra, Eusebius of Nicomedia, Eutyches, Dioscorus, Moses the Robber.
      Owner: the coordinator.
    - Reccared (589) and Euthymius the Great (377–473) fall in era 3 by date and go to that scan.
    - OUTSIDE WITNESS is a standing label; each later era scan applies it. Owner: the coordinator.
    - Source: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/`.
211. **Origen's brief ends on a dispute (2026-11-11).** Mark's "dispute in place" ruling (see
    "The Who profile pattern", 2026-11-11) moves a contested point to where it arises. Origen's live
    brief closes on the 553 council ("though how far it went is still argued"). It needs a small
    change order and a cap ruling for its recheck. Not made. Owner: the coordinator.
212. **Pattern findings in the eight live person texts (2026-11-11).** An Opus read of the eight
    early-church briefs and cards against `Who_Profile_Pattern.md` found no fabrication. It found
    the items below. Each changes reviewed text, so each needs a change order. Nothing was changed.
    Owner: the coordinator.
    - **Common names, in Mark's name-of-place form.** The live "the church historian Socrates" and
      similar forms predate "Socrates of Constantinople". Bare shared names still at first mention:
      Zachariah (Constantine card, "of Mitylene" in the source title), Rufinus (Origen brief and
      card, Nazianzus card), Gallus (Origen card, "the emperor Gallus"), Porphyry (Methodius card),
      Palladius without his place (Chrysostom brief), "Gregory" as the subject in the Nazianzus and
      Nyssa briefs, and "Gregory's" in the Nyssa card. Bare unique names with no context: Jerome,
      Theodoret, Photius, Lactantius, Licinius, Decius and Valerian.
    - **Contested claims told as settled, or sides unnamed.** Nazianzus card: "With Basil he
      gathered the Philocalia" is stated flatly, while the Origen brief says "are thought to have
      gathered" and Letter 115 does not name Basil. Methodius brief: the narrator settles the
      Decius dating ("cannot be right"); the card words it better. Nyssa brief and card: the
      restoration question names no holder of either side. Origen: "though how far it went is still
      argued" and "are thought to have gathered" name no witness.
    - **Unattributed modern judgments.** Athanasius brief, "From hiding he wrote more than half of
      his surviving works" (the NPNF editor's count). Ephrem card, "Most writers date his death to
      373, and some to 378". Nazianzus card, "It seems he did not". Nyssa card, "It seems to rest on
      two passages", and "None of his writings speaks of her as his wife" (an absolute).
    - **Archaic quotes that are hard to hear.** Chrysostom, "Wouldest thou do honor…". Nyssa, "the
      advance has no check". Nazianzus, the closing quote. Any re-rendering is Opus-authored.
    - **Beat lines and contrasts.** Athanasius, "But the price was high" and "not joined to God".
      Ephrem, "It worked". Methodius, "Little else is certain". Chrysostom, "Socrates notes the
      irony:". Verbless card labels ("Honored beyond Syria.", "Honored as a martyr.").
213. **No vendored place for Apollinaris (2026-11-11).** The Origen card's "Apollinaris" cannot
    take a name-of-place identifier, because no vendored source gives one. The pattern leaves the
    name as the sources have it. Open: whether the Library thread can name a source. Owner: the
    Library thread.
214. **The era 3 Who scan's wanted sources (2026-11-11).** Eight people would be a Who if the Library
    held one named source. Owner: the Library thread.
    - Iakob Tsurtaveli: *The Martyrdom of Shushanik* (Lang, *Lives and Legends of the Georgian
      Saints*, 1956; Georgian ed. Abuladze). It would also lift Shushanik from LISTED to STORY.
    - Vachagan III of Albania and Movses Daskhurantsi: Movses Daskhurantsi, *History of the Caucasian
      Albanians* (Dowsett, 1961, or Patkanian, 1861), with the Canons of Aghuen. One source serves
      both rows.
    - Sabas: Cyril of Scythopolis, *Vita Sabae* (Cotelier, *Ecclesiae Graecae Monumenta* III; Schwartz
      1939). Only Severus-passage extracts are held, in the Kugener PO2 file (l.24694–25324).
    - John Malalas: *Chronographia* (Dindorf 1831, or Migne PG 97). A short extract is held in the
      Kugener PO2 file (l.25347–25421).
    - Theophylact Simocatta: *Historiae* (de Boor 1887, or Migne PG 113). Photius's English epitome
      is held (`photius_library-v1_freese1920`, l.4812–5400); the work is not.
    - al-Tabari: *Tarikh al-rusul wa'l-muluk* (de Goeje 1879–1901; Zotenberg's French 1867–74). Era
      4 by date.
    - Ibn Ishaq: *Sirat Rasul Allah* as edited by Ibn Hisham (Wüstenfeld 1858–60). Era 4 by date.
    - Source: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/`.
215. **Open points from the era 3 scan (2026-11-11).** Owners as noted.
    - Thirteen rows carried to era 4 were scored in the era 4 scan (2026-11-11): Muirchu, Adomnán,
      Jonas of Bobbio, Aidan, Colmán, Cogitosus, Braulio, Ildefonsus, John of Nikiu, Maximus the
      Confessor, Sophronius, Antony of Choziba, al-Baladhuri. Mennas (Benjamin I's brother),
      al-Tabari and Ibn Ishaq moved there too, which brings era 3 to 100 people (WHO 64, STORY 18,
      LISTED 12, WANTED 6). Barsanuphius and John of Gaza are one paired WHO row (Mark's pairing
      ruling). Brigid of Kildare's WHO row rests on Cogitosus, who is WHO in era 4 (a recorder with a
      thin own life), so her route stands. Owner: the coordinator.
    - Marcellinus Comes is WHO as a recorder with a thin own-life; the profile marks that. Owner:
      the coordinator.
    - Source gaps: the full acts of Constantinople 553 (Mansi 9; only English extracts are held in
      `npnf214`), Mansi 8, Justinian's edicts against the Three Chapters (c.543/545 and 551), the
      acts of Dvin II and III and the Council of Aghuen (only Ormanian's summaries are held),
      Columbanus's Rules and other letters, Thomson's *Elishe*, Lang 1956, and the Armenian Book of
      Letters. The Library has Heraclius's Ekthesis in Latin (Mansi 10, l.100125–100714) but not in
      Greek. Owner: the Library thread.
    - Misleading file names: the Cogitosus Life of Brigid sits inside
      `john-biclaro-leander-pl72-lat_migne1878.txt`; the Kugener PO2 file holds Vita Sabae extracts,
      a Malalas extract and the 536 acts; two near-identical John of Ephesus HE III files have line
      numbers about 1,850 apart. Owner: the Library thread.
    - Timothy Aelurus's own refutation is held only in Classical Armenian, with no translation.
      Owner: the Library thread.
    - Armenian Christianity before the Bagratids (c.554–884) names nobody in its census text
      fields, and its sourcing line is stale. Owner: the coordinator.
    - LISTED rows that could be argued as STORY: Proterius, Sahak of Rshtunik, Elias of Jerusalem.
      Owner: the coordinator.
    - Source: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/`.

216. **Open points from the era 4 scan (2026-11-11).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/`.
    - Vladimir the Great and Olga of Kyiv are LISTED "for now" (Mark: "Listed for now"). They rest on
      Mouravieff's 1838 retelling and the 1762 Kyiv Synopsis. Rescore both together when the
      Primary Chronicle (Cross and Sherbowitz-Wetzor 1953) is held. Owner: the Library thread, then
      the coordinator.
    - Heraclius (live person entry) is recorded STORY (Mark: "Story, keep live"). His live profile
      stays until stories are built, then moves over. Owner: the coordinator.
    - John of Damascus is WANTED (Mark: "Wanted"). The Life by John of Jerusalem is wanted (Greek,
      Migne PG 94; the citation is the checker's recollection and needs confirming). Owner: the
      Library thread.
    - 43 WANTED rows, most of them unheld in the Library: the Lives of Cyril and Methodius, the
      Primary Chronicle and the Kyiv Paterik, Ilarion's Sermon, Theodore the Studite, Stephen the
      Younger, Nikephoros (Ignatius's Life), Keroularios (Psellos's oration), Eulogius and Alvarus
      (the Cordoban martyrs), Ardo's Life of Benedict of Aniane, the Cluny abbots' Lives, the
      Old English reformers (Alfred, Dunstan, Æthelwold, Oswald, Ælfric, Wulfstan), Anskar and
      Rimbert, the Lives of Grigol Khandzteli and John the Iberian, al-Tabari, Ibn Ishaq and Ibn
      Hayyan. Owner: the Library thread.
    - Library material the scan found: the Serpos Armenian history (1786, t1 to t3) and the Kyiv
      Synopsis (1762) are held, as late retellings. Misleading names: the "toledo-iii" file holds the
      whole Hispana; the "capitulatio-de-partibus-saxoniae" file holds MGH Capitularia I; the
      chronicle-of-seert po5 file opens with Evetts's History of the Patriarchs; the po11 and po1
      synaxaire files hold the Coptic Lives of Isaac and Yusab. Two OCR columns run together in
      Ildefonsus's De viris illustribus (l.17040-17101). Owner: the Library thread.
    - The coordinator's calls (Mark may overrule): pairs split as drafted; all seven Coptic
      patriarchs WHO with Major "no"; Dhuoda WHO; Alopen WHO with the thin life flagged. Owner: the
      coordinator.
    - One supplement scan after all eras for shapers the Library holds but no census text names:
      Wilfrid, Cuthbert of Lindisfarne, Cedd, Chad, Fursey, Elipandus of Toledo, Felix of Urgell and
      the Lismore saints (Senán, Findian, Brendan, Ciarán, Findchua; sixth century, never scored in
      era 3). Owner: the coordinator.
    - Adam of Bremen and Nestor the chronicler go to the era 5 scan; Hugh of Cluny (abbot 1049 to
      1109) is LISTED here and falls across the era boundary. Owner: the coordinator.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

217. **Map Who build slice: caps, major mark, placement (2026-11-11).** Owner: the map build slice.
    Mark's ruling is in `Decision-Log.md`, "Map Who: how many names, which names, and where they sit"
    (2026-11-11).
    - Change the caps from 6 names for a tradition and 4 for a river in an era to 4 and 5.
    - Add a "major" mark to each Who in the data, proposed at writing time and confirmed by Mark in
      each batch. Pick by major, order by date; a "more" click shows everyone, in date order.
    - "More" sits under a tradition's names and next to the river's Who button. Each river name
      sits at the dates the person was active, to the right of the river.
    - Everything else on the map fades while a Who is open.
    - The live build moves a stack to the river's left when the right side is tight. Resolve that
      against Mark's "to the right of the river", with the fade as the likely answer, and bring Mark
      any case where the right side has no room.

218. **Name-clarity recordings held for about two months (2026-11-11).** Mark: "ok put these on hold
    for a couple of months until we have more credits, this is not a major concern". Every recorded
    text held back by the name-clarity pass (PR #1597, release 38; list in
    `Build/Ministry/Operations/Audits/Name_Clarity_Pass_Held_Back_2026-11-11.md`) stays as it is,
    text and audio: the 8 Jon person briefs and the 69 tradition and story recordings. The text of
    those fields is not edited until then. Re-record them together in one approved, capped run when
    credits allow. Owner: the coordinator.

219. **Open points from the era 5 scan (2026-11-11).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era5/`.
    - Innocent III (live person entry) is WANTED (Mark: "Wanted, keep live"). His live profile stays
      until the Gesta Innocentii III (tr. Powell, 2004; the edition is the checker's recollection
      and needs confirming) is held; then rescore him. Owner: the Library thread, then the
      coordinator.
    - 43 WANTED rows, most of them unheld in the Library. People and their named sources: Innocent
      III (Gesta), Sava of Serbia and Domentijan and Teodosije (the Lives of Sava, ed. Danicic),
      Bernard of Clairvaux, Robert of Molesme, Stephen Harding, Aelred, Walter Daniel and William of
      St Thierry (Matarasso, The Cistercian World, and Waddell, Narrative and Legislative Texts from
      Early Citeaux), Bruno of Cologne, Hugh of Lincoln and Adam of Eynsham (the Magna Vita), Norbert
      of Xanten, Hadewijch, Marie d'Oignies and Jacques de Vitry (the Life, Lettres and Historia
      Orientalis), Marguerite Porete, Clare of Assisi, Brother Leo (Scripta Leonis), Thomas of
      Celano, Agnes of Prague, Dominic, Jordan of Saxony, Diana d'Andalo, Gerard de Frachet, Humbert
      of Romans (the Legenda), Thomas Aquinas, Joachim of Fiore, Salimbene, Valdes of Lyon, Rainerius
      Sacconi, William of Tyre, Anselm of Canterbury, Thomas Becket, Hugh de Payens, Adam of Bremen,
      Anna Komnene (OUTSIDE WITNESS), Basil the Physician, George the Hagiorite, Gregory
      Pakourianos, Nestor the chronicler (the Primary Chronicle), Cyril III ibn Laqlaq and Marco Polo
      (OUTSIDE WITNESS). Edition names from memory are tagged "[suggested; to confirm]" in the
      audit. Owner: the Library thread (see 220).
    - Missing outside witnesses, recorded as wanted sources with no rows (coordinator's call): Ibn
      al-Athir, Usama ibn Munqidh, Ibn Jubayr, Rashid al-Din (the full history, not the held
      geography excerpt) and Benjamin of Tudela. None is named in an era 5 census text. Owner: the
      Library thread.
    - Library material the scan found: Denzinger holds canon extracts of Lateran I to IV, Verona
      1184 and Lyon II; the Athos Urkunden (Meyer 1894) hold Sava's Typikon and Athanasios's;
      Brosset's translation of the Georgian royal chronicle holds the Lives of David and Tamar;
      Ehrle's Archiv bd1 and bd2 hold the Anagni protocol and the Historia tribulationum on Gerard of
      Borgo San Donnino. Misleading names: Gratian (the emperor), Mechthild of Magdeburg and
      "von Helfeda", Euthymius the Hagiorite. Owner: the Library thread.
    - Census text to check by change order: the Beguines sources note says Mechthild finished the
      Flowing Light at Helfta; the held edition (Morel 1869, MECH 417-422) sets her apart from the
      Helfta Mechthild and has no line for it. Conflicting dates inside the sources: Innocent IV's
      confirming bull is 1247 in the census and 1248 in the held text; Richard of St Victor dies
      1162 on the census people list and 1173 in a held note. Owner: the coordinator.
    - Moves by date of work, to the era 4 supplement: Symeon the New Theologian, Yahya ibn Said,
      John of Rila. To the era 6 scan: Bernard Gui (he stays on the Waldensian people list and is
      scored once, in era 6), Eckhart, Tauler, Suso, Angelo Clareno, Belibaste, Jacques de Molay,
      John of Brunn, Guiard of Cressonessart, Euthymius of Tarnovo. Owner: the coordinator.
    - Supplement-scan leads (held, named in no census text): John of Parma, Peter Olivi, Elias of
      Cortona, Elizabeth of Thuringia, Berengar, Abelard, Gregory IV Dgh'a, Constable Sempad (a
      lay chronicler like Anna Komnene; the OUTSIDE WITNESS label would cover both) and Maron (era 2
      by date, no earlier row). Owner: the coordinator.
    - The coordinator's calls (Mark may overrule): Sava WANTED; Brother Leo WANTED; Dionysius bar
      Salibi, Mari ibn Sulayman and Abu Salih WHO, flagged; the pairs and the Alberic and Stephen
      Harding split; Humbert of Romans WANTED; Toros Roslin LISTED. Owner: the coordinator.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

220. **Library timing: one combined WANTED list after all scans (2026-11-11).** Mark: "After all
    scans". The Library thread gets one combined WANTED list after eras 6 to 10 are scanned, ordered
    by era with major figures first. Until then the WANTED sources in 216 and 219 are recorded, not
    acquired. Ruling in `Decision-Log.md`, "The era 5 Who scan" (2026-11-11). Owner: the coordinator.

221. **Open points from the era 6 scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/`. The census was not changed.
    - WANTED sources the Library does not hold, for the combined list (220): Margery Kempe's Book
      (the EETS text, Meech and Allen 1940 [suggested; to confirm]); Henry Pomerius's Life of
      Ruusbroec; Raymond of Capua's Legenda maior of Catherine of Siena; the Life of Capistrano by
      Nicholas of Fara or Christopher of Varese (GLASS 23228-23229 names the latter); the Lives of
      Euthymius of Tarnovo, Teodosij of Trnovo, Stephen of Perm, Joseph of Volotsk, Kirill of
      Beloozero, and Zosima and Savvatii; Jakoubek's tracts on the chalice; Zara Yaqob's Mashafa
      Berhan; the Gadla Ewostatewos (the check recalls Turaev's CSCO Acta S. Eustathii, 1905, not
      Conti Rossini [recollection; to confirm]); Getatchew Haile's Acts of Estifanos. Owner: the
      Library thread.
    - Outside witnesses with no rows: Rashid al-Din (only a geography extract is held), Ibn Battuta,
      Ibn Khaldun, Abu'l-Fida and al-Qalqashandi are named in no era 6 census text and none is held
      in own text. Wanted sources, no rows (the era 5 call). Owner: the Library thread.
    - Library correction: the Baluze file the corpus-map calls "the Latin Lives" of the Avignon
      popes holds the Collectio actorum veterum (letters and bulls); no Avignon pope has a held
      Life. Owner: the Library thread.
    - Moves by date of work, to an era 5 supplement: Peter Olivi (all his work is before 1298), Ban
      Kulin (c.1180-1204) and Nikephoros the Monk. Owner: the coordinator.
    - Supplement-scan leads (held, named in no census text): Jan Rokycana, Lukáš of Prague,
      Matthias of Kunvald, Aeneas Sylvius Piccolomini, Peter Payne, Andrew of Perugia, Pascal of
      Vittoria, Thomas of Metsoph, Hethum II, Maba Seyon, Giyorgis of Sagla and others listed under
      "Not scored" in the audit. Gerson and Marsilius are scored in era 6, so the supplement scan
      skips them. Owner: the coordinator.
    - Leads for the events scan (not scored): the Avignon papacy, the suppression of the Templars,
      the Western Schism, the Hussite wars and the Compacts of Basel, the Wycliffite Bible, the fall
      of Constantinople, Timur's campaigns, the Malabar letter of 1504, the Black Death. Owner: the
      events scan.
    - Era 5 file line corrected: Doukas, Sphrantzes, Chalkokondyles and Syropoulos are era 6 by date
      of work, not era 7. Owner: the coordinator.
    - Tekle Haymanot is kept in era 6 although the only held date is 1270 and the date of the Gadla
      is not in a held line; confirm when the Gadla is dated. Owner: the Library thread.
    - The coordinator's calls (Mark may overrule): the thin-life writers LISTED; Kempe WANTED;
      Savonarola and Colette WHO, Capistrano WANTED; Kantakouzenos WHO; two rows for Barlaam and
      Akindynos; Ruusbroec shared; Gerson and Marsilius WHO; Zara Yaqob WANTED; Tekle Haymanot in
      era 6. Owner: the coordinator.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

222. **Open points from the councils scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/`.
    - Map build (with 217): cross-church links for the Lausanne Congress, the World Council of
      Churches founding, the Synod of Barmen and the 1872 Bulgarian council, which each link one
      census entry now. Map entries for the major councils the census does not name as gatherings,
      with links to the listed traditions: the Councils of Rome and Carthage 251, the Council of
      Arles, the Council of Clermont, the Marburg Colloquy, the Diet of Augsburg of 1555, the
      Quinisext Council and the Council of Dvin. Owner: the map build slice.
    - Wanted records for the 46 major councils (named from memory; to confirm): the Reichstagsakten
      for the Diet of Worms; the Marburg colloquy record; the Edinburgh 1910 reports; the Chicago
      Statement and the Lausanne papers; the Barmen Declaration and synod records; Amsterdam 1948
      and New Delhi 1961 reports; the Vatican II documents (Vatican copyright); the acts of the
      Council of Constantinople of 1872 (the census says the acta are verified, the Library holds
      none: reconcile); the acts of the Council of Dvin (607-609); Mansi tomus 12-13 (Nicaea II),
      15-17 (the Photian councils) and 9 (Constantinople II). Owner: the Library thread.
    - The list of all councils holds 46 WANTED rows: see the audit for each council and its named
      source. The 1844 and 1845 church conferences, the Moscow Council of 1917-18, CELAM Rio 1955
      and Medellin 1968, and the Cape Town and Manila congresses are all not held. Owner: the
      Library thread.
    - Doc-hygiene, not touched: the content note in the Beza Histoire ecclesiastique tome 1 file
      says tomes 2 and 3 are not vendored, but both are in cic/texts. Owner: the Library thread.
    - Mark's rulings (2026-11-12): the Quinisext Council and the Council of Dvin are major councils;
      one word, councils, for every gathering. The coordinator's calls (Mark may overrule): the four
      other promotions, the story-list placement of Keswick and Westphalia, and the map-build
      items above. Owner: the coordinator.

223. **Open points from the era 7 scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era7/`. The census was not changed.
    - WANTED sources the Library does not hold, for the combined list (220): Katharina Schütz Zell's
      1524 Entschuldigung and 1558 hymn book; Marie Dentière's Epistre tres utile (1539);
      Gracián's Peregrinación de Anastasio or Diálogos; Fucan's Myōtei mondō and Ha Daiusu (Elison,
      Deus Destroyed); Xu Guangqi's memorials and prefaces; Guaman Poma's Nueva corónica; Las
      Casas's Historia de las Indias; Sahagún's Florentine Codex; the acts of the Polotsk process
      for Kuntsevych. All named from the workers' memory [suggested; to confirm]. Owner: the
      Library thread.
    - Sources that would strengthen rows that are now WHO: Camerarius's 1566 Life of Melanchthon;
      Samuel Clarke's Lives of Perkins; Valignano's Sumario (1583); Rutsky's collected letters; de
      Nobili's Tamil and Latin works; Argula von Grumbach's 1523 letter and pamphlets; Angela
      Merici's Rule and Counsels; Kuntsevych-type early lives. Owner: the Library thread.
    - Outside witnesses with no rows: no Ottoman, Jewish or secular-humanist historian of
      1517–1650 is held. Wanted sources, no rows: Kâtib Çelebi, Evliya Çelebi, Peçevi, Mustafa Ali,
      Selaniki; Joseph ha-Kohen, Samuel Usque, Gedaliah ibn Yahya, David Gans, Ibn Verga; de
      Thou, Guicciardini, Machiavelli, Bodin, Montaigne, Vasari; Leo Africanus; Busbecq. Owner: the
      Library thread.
    - Works after 1650 handed to the era 8 scan: van Braght, Lubieniecki, Leger, Morland, Louis XIV,
      Fontaine, Migault, Brandt, Challoner, Dodd, Zakaria of Kanaker, Ludolf, the Archdeacon Thomas
      of the Coonan Cross (suggested WANTED there), and eight later Eastern travellers and
      chroniclers. Baxter stays in era 7 with a flag. Owner: the coordinator (told to the era 8
      worker 2026-11-12).
    - Jean Ingoro and Jean Tingoro (Japan): possibly one man; the Pagès narrative volume that
      indexes Tingoro as a jifiaque is not held, and Ingoro's source note is OCR-garbled and needs a
      page-image check. Owner: the Library thread.
    - Library corrections: the OCR spells Katharina Schütz Zell "Zclin" (SCHULTZ 1446); Ursulines
      do appear in the Library; the Parsons file is Gertrude Parsons's Life of Colette, not Robert
      Persons; `APOL` is two works (Melanchthon's Apology and Smotryc'kyj's Apologia) across the
      workers' file keys. Owner: the Library thread.
    - Leads for the councils list (not scored): the Council of Trent; the Diet of Worms and the
      Diet of Augsburg 1530; the Colloquy of Marburg; the Synod of Dort; the Westminster Assembly;
      the Hampton Court Conference; the Synod of Diamper 1599; the Union and Synod of Brest
      1595–1596; the Stoglav 1551; the Lucaris synods; the Diet of Torda 1568; the Schleitheim
      assembly 1527; the Jesuit general congregations. Full list with Library files in the audit.
      Owner: the councils scan.
    - Dutch Further Reformation has no WHO yet (Teellinck and Voetius LISTED, Schurman STORY); a
      life source is wanted. Owner: the Library thread.
    - The coordinator's calls (Mark may overrule): Melanchthon, Perkins, Valignano, Rutsky, Argula
      von Grumbach and Angela Merici moved from WANTED to WHO; de Nobili WHO witness-only; Neri,
      Ivan IV, Winthrop and Dávid WHO; Hermogenes STORY; Cocks LISTED; Herberstein unlabelled.
      Owner: the coordinator.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

224. **Open points from the era 9 scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era9/`. The census was not changed.
    255 rows: WHO 34, STORY 11, LISTED 49, WANTED 161. The Library holds almost nothing of
    1815–1906. Approved to proceed (coordinator, under Mark's full-auto instruction of 2026-11-12).
    - WANTED sources the Library does not hold, for the combined list (220), major first, then the
      rest. Nothing is queued now (coordinator call). Titles tagged "[suggested; to confirm]" were named
      from the workers' memory. Owner: the Library thread.
      Major-marked rows (50):
      - Barton W. Stone: Biography of Elder Barton Warren Stone, written by himself (1847)
        [suggested; to confirm]; the Christian Messenger. Not held (greps: "Biography of Elder",
        "Christian Messenger")
      - Alexander Campbell: The Millennial Harbinger (1830-); the Christian Baptist (1823-30); the
        Campbell-Rice debate; Richardson, Memoirs of Alexander Campbell (1868-70) [all suggested;
        to confirm]
      - Charles G. Finney: Lectures on Revivals of Religion (1835); Memoirs of Charles G. Finney
        (1876) [both suggested; to confirm]
      - Phoebe Palmer: The Way of Holiness (1843); Wheatley, Life and Letters of Mrs. Phoebe
        Palmer (1876) [both suggested; to confirm]
      - Dwight L. Moody: A Life of D. L. Moody by his son (1900) [suggested; to confirm]; his
        sermons
      - Charles Haddon Spurgeon: The Metropolitan Tabernacle Pulpit (sermons); Autobiography
        compiled by his wife and secretary (1897-1900) [both suggested; to confirm]. Greps
        "Spurgeon" (none his own), "Metropolitan Tabernacle" (none)
      - Elias Hicks: Journal of the Life and Religious Labours of Elias Hicks (1832) [suggested;
        to confirm]; the Orthodox side's account
      - Joseph John Gurney: Memoirs of Joseph John Gurney (1854); his Observations on the
        Distinguishing Views and Practices of the Society of Friends (1824) [both suggested; to
        confirm]
      - William Knibb: Hinton, Memoir of William Knibb (1847); Phillippo, Jamaica: Its Past and
        Present State (1843) [both suggested; to confirm]
      - William Miller: His own Views of the Prophecies and a life told by a disciple (Bliss,
        Memoirs of William Miller) [suggested; to confirm]
      - Ellen G. White: Her Life Sketches / Spiritual Gifts and a life told by another [suggested;
        to confirm]
      - Joseph Smith: His own History and Doctrine and Covenants, with a life told by another
        [suggested; to confirm]
      - Brigham Young: The Journal of Discourses and his life told by another [suggested; to
        confirm]
      - Charles Taze Russell: Zion's Watch Tower and Studies in the Scriptures [suggested; to
        confirm]
      - Mary Baker Eddy: Science and Health and her own memoir Retrospection and Introspection
        [suggested; to confirm]
      - John Thomas: Elpis Israel and Eureka [suggested; to confirm]
      - Edward Irving: His collected writings and a life told by another [suggested; to confirm]
      - John Humphrey Noyes: His own writings and the community's periodical [suggested; to
        confirm]
      - Margaret and Kate Fox (pair): Their own confession and a life told by another [suggested;
        to confirm]
      - John Nelson Darby: His Collected Writings and Letters [suggested; to confirm]
      - Anthony Norris Groves: His journals and the memoir by his widow [suggested; to confirm]
      - George Mueller (Muller): His Narrative of the Lord's Dealings [suggested; to confirm]
      - Theodore Parker: His sermons and a life told by a friend [suggested; to confirm]
      - Hong Xiuquan: The kingdom's own printed edicts and a missionary's record of his visions
        [suggested; to confirm]
      - Antonio Conselheiro: Os Sertoes (3rd ed. 1905), plus his own sermon notebooks and a second
        witness [suggested; to confirm]
      - Euclides da Cunha: Os Sertoes, 3rd edition (1905) [suggested; to confirm]
      - John Henry Newman: Apologia pro Vita Sua (1864) [suggested; to confirm]; Tract 90 (named
        in the census voice line)
      - John Keble: The 1833 Assize Sermon (census) and a life of Keble [suggested; to confirm:
        Coleridge, Memoir of Keble, 1869]
      - Edward Bouverie Pusey: Liddon, Life of Edward Bouverie Pusey (1893-97) [suggested; to
        confirm]; his own tracts
      - William and Catherine Booth (pair): Catherine Booth's 1859 argument on women's ministry
        (census); William Booth, In Darkest England and the Way Out (1890) [suggested; to confirm]
      - Johann Hinrich Wichern: Wichern's own memorandum on the Inner Mission [suggested; to
        confirm: the 1849 Denkschrift]
      - Abraham Kuyper: His writings (census sources note: "Kuyper's writings"); a life [to
        identify]
      - Herman Bavinck: Reformed Dogmatics (census: "still in use")
      - Ignaz von Döllinger: Friedrich, Ignaz von Döllinger (1899-1901) (named in MIRBT 30949);
        his Briefe und Erklärungen über die Vaticanischen Decrete (named in MIRBT 31054-31055)
      - C. F. W. Walther: Der Lutheraner and the Missouri Synod founding documents of 1847 (census
        sources note)
      - Ambrose of Optina: His letters to laypeople and an early life [suggested; to confirm]
      - Nikolai (Kasatkin) of Japan: Nikolai's diaries or a life [suggested; to confirm]
      - Mkrtich Khrimian (Hayrik): Khrimian's writings and a life [suggested; to confirm]
      - Joseph Audo (Chaldean patriarch): Collectio Lacensis, acts of Vatican I [suggested; to
        confirm]; his pastoral letters
      - Cyril IV, Coptic patriarch: A Coptic church history of the 1800s (census note:
        "institutional and biographical") [suggested; to confirm]
      - Ioann Veniaminov (Saint Innocent): Veniaminov's journals and Aleut translations (census
        sources note)
      - Samuel Ajayi Crowther: Crowther's own Journals and a life, e.g. Page, Samuel Crowther
        (1908) [suggested; to confirm]; Crowther, Journal of an Expedition up the Niger (1855)
        [suggested; to confirm]
      - J. Hudson Taylor: Hudson Taylor, A Retrospect (1894) or Mrs Howard Taylor's life
        [suggested; to confirm]
      - Xi Shengmo (Pastor Hsi): A life, e.g. Mrs Howard Taylor, Pastor Hsi (1900) [suggested; to
        confirm]
      - Ludwig Ingwer Nommensen: A life of Nommensen, or Batak church records [suggested; to
        confirm]
      - Kiai Sadrach: Dutch mission reports and a modern life [suggested; to confirm]
      - David Jones and David Griffiths (pair): London Missionary Society papers or Ellis, History
        of Madagascar (1838) [suggested; to confirm]
      - Johann Ludwig Krapf: Krapf, Travels, Researches and Missionary Labours (1860) [suggested;
        to confirm]
      - Charles Lwanga: Martyr accounts [suggested; to confirm]
      - Tiyo Soga: Chalmers, Tiyo Soga: A Page of South African Mission Work (1877) [suggested; to
        confirm]
      Other WANTED rows (111):
      - Walter Scott: Baxter, Life of Elder Walter Scott (1874) [suggested; to confirm]
      - "Raccoon" John Smith: Williams, Life of Elder John Smith (1870) [suggested; to confirm]
      - Peter Cartwright: Autobiography of Peter Cartwright, the Backwoods Preacher (1856)
        [suggested; to confirm]. Greps "Peter Cartwright" (one list line), "Autobiography of Peter
        Cartwright" (none)
      - Daniel Coker: A Dialogue Between a Virginian and an African Minister (1810); Journal of
        Daniel Coker (1820) [both suggested; to confirm]
      - Zilpha Elaw: Memoirs of the Life, Religious Experience, Ministerial Travels and Labours of
        Mrs. Elaw (1846) [suggested; to confirm]
      - Julia Foote: A Brand Plucked from the Fire (1879) [suggested; to confirm]
      - Amanda Berry Smith: An Autobiography: The Story of the Lord's Dealings with Mrs. Amanda
        Smith (1893) [suggested; to confirm]
      - Hannah Whitall Smith: The Christian's Secret of a Happy Life (1875); her later
        autobiography The Unselfishness of God (1903) [both suggested; to confirm]
      - John S. Inskip: A Life of John S. Inskip (1885) [suggested; to confirm]
      - Robert P. Wilder: Wilder's own account of the 1886 Mount Hermon conference and his campus
        tours (title to be found)
      - Hugh Bourne and William Clowes (pair): Bourne's History of the Primitive Methodists
        (1823); Clowes's Journals (1844) [both suggested; to confirm]
      - Jabez Bunting: T. P. Bunting, Life of Jabez Bunting (1859) [suggested; to confirm];
        Conference minutes after 1798
      - James Varick: Christopher Rush, A Short Account of the Rise and Progress of the African M.
        E. Church (1843) [suggested; to confirm]
      - William Taylor: Story of My Life (1895) [suggested; to confirm]
      - James Robinson Graves: Old Landmarkism: What Is It? (1880); a life such as Hailey, J. R.
        Graves: Life, Times and Teachings (1929) [both suggested; to confirm]
      - William Bullein Johnson: Proceedings of the 1845 Augusta convention; Johnson's The Gospel
        Developed (1846) [suggested; to confirm]. The founding meeting is WANTED on the councils
        list
      - John Clifford: Baptist Union records of 1887-88; Marchant, Dr. John Clifford (1924) [both
        suggested; to confirm]
      - John Wilbur: Journal of the Life of John Wilbur (1859) [suggested; to confirm]
      - Lucretia Mott: Hallowell, James and Lucretia Mott: Life and Letters (1884) [suggested; to
        confirm]
      - Levi Coffin: Reminiscences of Levi Coffin (1876) [suggested; to confirm]
      - Samuel Sharpe: Bleby, Death Struggles of Slavery (1853) [suggested; to confirm]
      - John Smith of Demerara: The 1823-24 Demerara trial papers; Wallbridge, The Demerara Martyr
        (1848) [both suggested; to confirm]
      - Henry Bleby: Death Struggles of Slavery (1853) [suggested; to confirm]
      - Hiram Edson: His own manuscript account of the morning after 1844 [suggested; to confirm]
      - Joseph Bates: His Autobiography [suggested; to confirm]
      - Emma Hale Smith: Her 1835 hymnbook and a life told by another [suggested; to confirm]
      - Eliza R. Snow: Her poetry volumes and her own journal or a life [suggested; to confirm]
      - Emmeline B. Wells: The Woman's Exponent (periodical) and a told life [suggested; to
        confirm]
      - Robert Roberts: His magazine run and a life told by another [suggested; to confirm]
      - Mary Campbell and Margaret Macdonald (pair): A contemporary account of the 1830
        prophecies, and a life told by another [suggested; to confirm]
      - John Bate Cardale: The church's liturgy and his own tracts [suggested; to confirm]
      - Henry Drummond (banker, patron): A life told by another, and the Albury conference record
        [suggested; to confirm]
      - Tirzah Miller: Her diaries, in a printed edition [suggested; to confirm]
      - Andrew Jackson Davis: His own major book and his autobiography [suggested; to confirm]
      - Emma Hardinge Britten: Her history of Spiritualism [suggested; to confirm]
      - Phineas Quimby: His own manuscripts, with an early life [suggested; to confirm]
      - Emma Curtis Hopkins: Her own lessons and a told life [suggested; to confirm]
      - Charles and Myrtle Fillmore (pair): The Unity periodical and Charles Fillmore's books
        [suggested; to confirm]
      - Benjamin Wills Newton: His own tracts and a neutral told life [suggested; to confirm]
      - J. G. Bellett: His memoir of the early circle [suggested; to confirm]
      - Ralph Waldo Emerson: The 1838 Address and a life told by another [suggested; to confirm]
      - Dorothea Dix: A life told by another [suggested; to confirm]
      - Feng Yunshan: Taiping texts and a missionary's record [suggested; to confirm]
      - Yang Xiuqing: The kingdom's proclamations and a witness outside it [suggested; to confirm]
      - Hong Rengan: His own program and a missionary's record [suggested; to confirm]
      - Issachar Jacox Roberts: His own letters or a life told by another [suggested; to confirm]
      - Richard Hurrell Froude: His posthumously published papers (census), Remains [suggested; to
        confirm]
      - Priscilla Lydia Sellon: The Devonport sisterhood's own records (census sources note: "the
        sisterhoods' archives"); a contemporary life [to identify]
      - Theodor and Friederike Fliedner (pair): Their own accounts of Kaiserswerth [exact title to
        identify]
      - Adolphe Monod: The deathbed addresses taken down and published (census); sermons [to
        identify]
      - Guillaume Groen van Prinsterer: His own history and political writings [to identify;
        suggested: Ongeloof en Revolutie, 1847]
      - Hendrik de Cock: The Afscheiding's own acts of 1834 (census sources note) and a life [to
        identify]
      - Paul Petter Waldenström: His articles in Pietisten (from 1872, CORN 26595) and his books
        [to identify]
      - Charles Simeon: Carus, Memoirs of the Life of the Rev. Charles Simeon (1847) [suggested;
        to confirm]
      - Anthony Ashley Cooper, Lord Shaftesbury: A life of the seventh earl [to identify;
        suggested: Hodder, 1886]
      - Samuel Wilberforce: A life of the bishop [to identify; suggested: Ashwell and R. G.
        Wilberforce, 1880-82]
      - Frederick Denison Maurice: His Theological Essays and a life told through his letters
        [suggested; to confirm]
      - John William Colenso: His Pentateuch and Joshua critical examination [suggested; to
        confirm]
      - Charles Longley: The 1867 Lambeth Conference documents (census sources note)
      - Wilhelm Löhe: His writings and the Neuendettelsau records [to identify]
      - Bernadette Soubirous: Her own depositions of 1858, or an early life such as Lasserre,
        Notre-Dame de Lourdes (1869) [suggested; to confirm]
      - Nicholas Wiseman: His own Pastoral from the Flaminian Gate (1850) and Recollections of the
        Last Four Popes (1858) [suggested; to confirm]; and a life such as Wilfrid Ward, Life and
        Times of Cardinal Wiseman (1897) [suggested; to confirm]
      - Andrey Sheptytsky, metropolitan of Lviv: His pastoral letters (1900-1914) and an early
        life, such as Korolevsky, Métropolite André Szeptyckyj (1964) [suggested; to confirm]
      - Gregorio Aglipay and Isabelo de los Reyes (pair): The church's founding texts and Reyes's
        writings (the census names "the Iglesia Filipina Independiente's own founding texts")
        [suggested; to confirm editions]
      - Apolinario de la Cruz: A second account independent of Montero y Vidal, e.g. the friar's
        Relación cited in MONT 1476-1484 (by Fr. Manuel, title line garbled) or the trial record
        [suggested; to confirm]
      - Niijima Jo (Joseph Hardy Neesima): His Life and Letters (Hardy, 1892) [suggested; to
        confirm]
      - Uchimura Kanzo: How I Became a Christian (1895) [suggested; to confirm] and the collected
        works
      - Fabre Geffrard, president of Haiti: The Concordat of 1860 and its acts [suggested; to
        confirm]
      - Benito Juarez: The Reform laws of 1855-1860 (Ley Juárez, Ley Lerdo, Reform decrees)
        [suggested; to confirm]
      - Gabriel Garcia Moreno: The decree of consecration (1873-1874) and an early life
        [suggested; to confirm]
      - Vital Maria Goncalves de Oliveira and Antonio de Macedo Costa (pair; Brazil, religious
        question): Their pastoral letters and the trial records of the 1870s [suggested; to
        confirm]
      - Philiphê Binh (Philiphê Bỉnh): His book in Vietnamese (a chronicle of the Vietnamese
        Church, 1822) [suggested; to confirm]
      - Minh Mang, emperor of Vietnam: The edict of 1833 in French or English translation, in a
        Paris Mission history [suggested; to confirm]
      - Peter Paul Massaad, Maronite patriarch: His pastoral letters and patriarchal acts, or a
        Maronite history of the period [suggested; to confirm]
      - Joseph Dolci, Maronite patriarch: The acts of the Maronite synod of 1818 [suggested; to
        confirm]
      - Elias Hoyek, Maronite patriarch: His letters or memoirs, or a Maronite history of
        1899-1906 [suggested; to confirm]
      - Macarius of Optina: His published letters and a life, Optina press [suggested; to confirm]
      - Ivan Kireevsky: Collected works of Ivan Kireevsky [suggested; to confirm]
      - Theophan the Recluse: His Russian Dobrotolyubie and letters [suggested; to confirm]
      - Makary (Glukharev): His writings and a life of the Altai mission founder [suggested; to
        confirm]
      - John of Kronstadt: John of Kronstadt's diary (named in the Optina census sources note)
      - Nerses Varzhapetian: Records of the National Assembly and Nerses's reports (census sources
        note) [suggested; to confirm titles]
      - Grigor Odian: The Armenian National Constitution of 1863 and Odian's writings [suggested;
        to confirm]
      - Theoklitos Pharmakidis: His writings on the declaration of 1833 [suggested; to confirm]
      - Konstantinos Oikonomos: His defence of the Patriarchate's authority [suggested; to
        confirm]
      - Antim I (first Bulgarian exarch): The firman of 1870 and the 1872 acta (census sources
        note); a life of Antim
      - Thomas Jones (Khasi missionary): Welsh mission records and a life [suggested; to confirm]
      - Edwin W. Clark: American Baptist Naga mission records [suggested; to confirm]
      - Herman of Alaska: Herman's Spruce Island record (census sources note)
      - Iakov Netsvetov: Records of the native clergy (census sources note)
      - Tewodros II: Royal chronicles (census sources note)
      - Abuna Salama III: Mission-era accounts by outsiders (census sources note)
      - Yohannes IV: Records of the Boru Meda settlement of 1878 (census sources note)
      - Menelik II: Royal chronicles (census sources note)
      - Empress Taytu Betul: Royal chronicles (census sources note)
      - Liang Fa: His tract (Quanshi liangyan, 1832) plus a life [suggested; to confirm]
      - Ta'unga: His own narrative, in a modern edition; rights unchecked [suggested; to confirm]
      - Joeli Bulu: His autobiography, translated 1871 [suggested; to confirm]
      - Rasalama: The martyr accounts, e.g. in Ellis, Three Visits (1858) [suggested; to confirm]
      - Rafaravavy: A narrative of her escape [suggested; to confirm]
      - Ranavalona I: Mission histories of the persecution [suggested; to confirm]
      - Ranavalona II: Same mission histories [suggested; to confirm]
      - Joseph Mukasa Balikuddembe: Martyr accounts, Anglican and Catholic [suggested; to confirm]
      - James Hannington: His journals and a life, e.g. Dawson (1887) [suggested; to confirm]
      - Mwanga II: Mission and court accounts [suggested; to confirm]
      - Ntsikana: Chalmers, Tiyo Soga (1877) and Ntsikana's hymn [suggested; to confirm]
      - Moshoeshoe (Moshesh): Casalis, The Basutos (1861) [suggested; to confirm]
      - J. Taylor Hamilton: Hamilton's history of the Moravian Church (1901 per census)
      - Pliny Fisk: Jessup, Fifty-three Years in Syria (1910) [suggested; to confirm] and a memoir
        of Fisk
      - Butrus el Bistany and Sheikh Nasif el Yazigy (pair): The Smith-Van Dyck Bible story in
        Jessup (1910), or Arabic sources [suggested; to confirm]
      - Asaad es Shidiak: Jessup (1910); a memoir of Shidiak (1830s) [suggested; to confirm]
    - Scope hold for Mark: Spiritualism / New Thought is "Outside Article 4 Scope" in
      `ATLAS-TARGETS.md`. Its 6 rows (10 people: the Fox sisters, A. J. Davis, Hardinge Britten,
      Quimby, Hopkins, the Fillmores) stay WANTED and are provisional until Mark rules whether such a
      movement belongs on the tree. Owner: Mark.
    - Carried forward to era 10 (no verdict): Oldham, Azariah, Cheng Jingyi, John R. Mott, Tikhon
      (Bellavin), Ormanian, Scher, Malech, Wigram, Nurikhan, Kivebulaya, Bramwell Booth's post-1912
      work, Pius X's 1907 syllabus, Charon's patriarchates volumes, Bonch-Bruevich. Owner: the
      coordinator.
    - Handed to the era 8 worker 2026-11-12 (scored once there): Absalom Jones, Asbury, McGready,
      McNemar, Thomas Campbell, Raikes and Stock, Liele and David George, Coke and Jesse Lee,
      Ballou and the Universalist hymnbook committee, Freeman, Wells, Belsham, Murray, Winchester,
      Hauge, Wilberforce, Theodore de Cock and the Utrecht persons of the 1700s, Georg Schmidt,
      Nikodemos the Hagiorite and the Philokalia circle, Kosmas Aitolos, Paisius Velichkovsky, Tikhon
      of Zadonsk, Balaam, Paisii Hilendarski, Prokopovich, Chamich, Assemani, Filippov and Denisov,
      the Compiègne Carmelites, the Szeptyckis, Moreau de Saint-Méry, Volney, Anne Dutton. Kept in
      era 9: Carey, Allen (1816), Hormizd, Marsden, Sheptytsky, Hoyek, Underwood, Simeon, Gregory V.
    - Outside witnesses with no rows: no secular, Jewish, Muslim, Asian or African historian of these
      churches is held for 1815–1906. Owner: the Library thread.
    - Library corrections: the Pusey volumes on Cyril are by P. E. Pusey, not E. B. Pusey; the
      Library header's note that Appenzeller's report sits at about KREPO 19633 is wrong (19644 is
      the editors' list); Dallet's Korean names are French spellings (Ni Seng-houn-i, Tieng,
      Hoang); Heykamp is printed as Archbishop of Utrecht at MIRBT 31197-31198, where the census
      says Deventer. Owner: the Library thread.
    - Leads for the councils list (not scored): see the audit; they include the Melkite election
      synod of 1902 (Mansi 46, l.114334), the Armenian National Assembly 1863, the Synod of
      Mulanthuruthy 1876, the Mavelicare assembly 1818, the AME conference 1816, the Utrecht and
      Old Catholic gatherings 1870–1892, the General Synod of the Reformed Church of France 1872,
      and the Albury and Powerscourt conferences. Owner: the councils scan.
    - The coordinator's calls (Mark may overrule): Laestadius and Rosenius WHO; Carey, Channing,
      Filaret (Drozdov), Holly, Leonid of Optina WHO; Dallet, Marnas, Badger, Whitehouse and
      Philipos WHO as recorders; Montero y Vidal and Pelesz LISTED; Pobedonostsev STORY.
      Owner: the coordinator.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

225. **Open points from the era 8 scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era8/`. The census was not changed.
    411 rows: WHO 137, STORY 51, LISTED 179, WANTED 44. Approved to proceed (coordinator, under
    Mark's full-auto instruction of 2026-11-12).
    - WANTED sources the Library does not hold, for the combined list (220), major first, then the
      rest. Nothing is queued now (coordinator call). Titles tagged "[suggested; to confirm]" were
      named from the workers' memory. Owner: the Library thread.
      Major-marked rows (7):
      - Robert Hindmarsh: Hindmarsh, Rise and Progress of the New Jerusalem Church (pub. 1861)
        (named in census sources)
      - Dona Beatriz Kimpa Vita: Bernardo da Gallo, Relatione (Capuchin relation on the
        interrogation, trial and burning, 1706) and Lorenzo da Lucca's relation, both named in the
        census; Brásio, Monumenta Missionaria Africana, for the Portuguese-side documents [s
      - António Vieira: Vieira, Maria Rosa Mystica (Lisbon, 1686), named in the census; a life-
        bearing source: André de Barros, Vida do apostolico padre Antonio Vieira (Lisbon, 1746) and
        the Cartas [suggested; to confirm].
      - Charles Maigrot: Maigrot's Mandate of 1693 (Fujian) in a contemporary printing; Launay,
        Histoire générale de la Société des Missions-Étrangères, vol. 1 (Paris, 1894), named in the
        census, for the life [suggested; to confirm the printing of the man
      - François Pallu and Pierre Lambert de la Motte: Pallu's and Lambert's own Relations and
        letters, and Launay, Histoire générale de la Société des Missions-Étrangères, vol. 1 (Paris:
        Téqui, 1894), named in the census; the Monita of the first vicars [suggested; to confirm the
        earl
      - Alexandre de Rhodes: Rhodes, Divers voyages et missions (Paris, 1653), his own life-telling
        [suggested; to confirm]; the Catechismus of 1651 (Propaganda) as the work.
      - Joseph Vaz: Sebastião do Rego, Vida do venerável padre Joseph Vaz (Lisbon, 1744) [suggested;
        to confirm]; the Sketch of the Rise and Progress of the Catholic Church in Ceylon (Colombo,
        1848), named in the census.
      The rest (37):
      - Samson Occom: Samson Occom, A Short Narrative of My Life (1768), as printed in W. DeLoss
        Love, Samson Occom and the Christian Indians of New England (1899) [suggested; to confirm]
      - Ann Griffiths: The 1806 Welsh memoir of Ann Griffiths and her letters, by John Hughes of
        Pontrobert [recollection; to confirm]
      - James Davenport: James Davenport, The Reverend Mr. James Davenport's Confession and
        Retractions (Boston, 1744) [suggested; to confirm]
      - Nathan Cole: Nathan Cole, Spiritual Travels, as printed in M. J. Crawford, "The Spiritual
        Travels of Nathan Cole," William and Mary Quarterly 33 (1976) [recollection; to confirm]
      - Lemuel Haynes: Timothy Mather Cooley, Sketches of the Life and Character of the Rev. Lemuel
        Haynes (New York, 1837) [suggested; to confirm]
      - Sarah Crosby: Zechariah Taft, Biographical Sketches of the Lives and Public Ministry of
        Various Holy Women (1825-1828) [suggested; to confirm]
      - Samuel Davies: The first volume of the same edition (Sermons on Important Subjects, 1792)
        with the funeral sermon and life [recollection; to confirm]
      - Anne Dutton: Dutton, A Brief Account of the Gracious Dealings of God with a Poor, Sinful,
        Unworthy Creature (1743) [suggested; to confirm]
      - Isaac Watts: Thomas Gibbons, Memoirs of the Rev. Isaac Watts (1780) [suggested; to confirm]
      - Philip Doddridge: Job Orton, Memoirs of the Life, Character and Writings of Philip Doddridge
        (1766) [suggested; to confirm]
      - Judith Sargent Murray: Judith Sargent Murray, The Gleaner (1798) [suggested; to confirm];
        her letter books [suggested; to confirm]
      - Hannah More: William Roberts, Memoirs of the Life and Correspondence of Mrs. Hannah More
        (1834) [suggested; to confirm]
      - Thomas Bray: Samuel Smith, The Life of the Rev. Thomas Bray (1746) [suggested; to confirm]
      - William Wilberforce: R. I. and S. Wilberforce, The Life of William Wilberforce (1838)
        [suggested; to confirm]
      - Jakob Ammann: Ammann's letters of 1693 and the Amish division sources, in Die Täufer in der
        Schweiz (Akten) [suggested; to confirm]
      - Johanna Eleonora Petersen: Lebens-Beschreibung der Frauen Johannä Eleonora Petersen (1718),
        the census's own source; Becker-Cantarino's English (Chicago 2005) is the modern edition
        [suggested; to confirm the early German print]
      - Gottfried Arnold: Unparteiische Kirchen- und Ketzer-Historie (1699-1700), the census's own
        source; the Frankfurt edition of 1729 [suggested; to confirm]
      - Rebecca Protten: Her letters and Lebenslauf from the Unity Archives (Herrnhut), as printed
        in a published edition [suggested; to confirm]. Sensbach, Rebecca's Revival (Harvard 2005)
        is a modern secondary book, not an early source
      - Lodovico Antonio Muratori: Gian Francesco Soli Muratori, Vita del proposto Lodovico Antonio
        Muratori (Venice, 1756) [suggested; to confirm]; Il cristianesimo felice (1743) is online at
        archive.org A118051 (the census link).
      - Armand-Jean de Rancé: A life of Rancé by Pierre Marsollier (1703) [suggested; to confirm],
        or Rancé's letters [suggested; to confirm].
      - Nicolas Fontaine and Pierre Thomas du Fossé: Nicolas Fontaine, Mémoires pour servir à
        l'histoire de Port-Royal (Cologne, 1738) [suggested; to confirm]; Mémoires de Pierre Thomas,
        sieur du Fossé (Utrecht, 1739) [suggested; to confirm].
      - Tikhon of Zadonsk: A life by a disciple: Ivan Chebotarev (the monk who served him), Life of
        Tikhon of Zadonsk (late 18th c.) [suggested; to confirm]; and his Of True Christianity
        [suggested; to confirm]
      - Herman of Alaska: The Valaam mission records and a Life: Little Russian Philokalia vol. 3,
        Saint Herman: Wonderworker of Alaska (Platina, 1971) [suggested; to confirm]; Hieromonk
        Gideon, journal of his 1804-07 voyage to Russian America [suggested;
      - Ioan Inocențiu Klein: Augustin Bunea, Episcopul Ioan Inocenţiu Klein (1728-1751) (Blaj,
        1900) (named by the census) and Nicolaus Nilles, Symbolae ad illustrandam historiam
        ecclesiae orientalis (Innsbruck, 1885), vol. 2 [suggested volume; to confirm]
      - James Bruce of Kinnaird: James Bruce, Travels to Discover the Source of the Nile, vols. 2
        and 3 (Edinburgh, 1790)
      - Ibrahim al-Jawhari: al-Jabarti, Aja'ib al-athar (Cairo chronicle, obituary of Ibrahim al-
        Jawhari) [suggested; to confirm]; Butcher, The Story of the Church of Egypt, vol. 2 (London,
        1897) as named in the census
      - Bernardo da Gallo: The same Capuchin relation as above.
      - Pedro IV of Kongo: The da Gallo and Lorenzo da Lucca relations; Zucchelli's Italian original
        of 1712 [suggested; to confirm] for the pre-1704 court.
      - Úrsula de Jesús: Úrsula de Jesús, The Souls of Purgatory: The Spiritual Diary of a
        Seventeenth-Century Afro-Peruvian Mystic, ed. and trans. Nancy van Deusen (UNM Press, 2004),
        named in the census. A 2004 translation: the Library must check rights,
      - Philiphê Bỉnh: Bỉnh's own notebook and writings (Sách sổ sang chép) [suggested; to confirm];
        George E. Dutton, A Vietnamese Moses (University of California Press, 2017), open access,
        named in the census, as a carrier of the life.
      - Philippus Baldaeus: Baldaeus, Naauwkeurige beschryvinge van Malabar en Choromandel ... en
        het machtige eyland Ceylon (Amsterdam, 1672) [suggested; to confirm].
      - James McGready: McGready, A Short Narrative of the Revival of Religion in Logan County
        (1801), or his Posthumous Works (1831-32) [suggested; to confirm]
      - Thomas Campbell: Campbell, Declaration and Address (1809), and Richardson, Memoirs of
        Alexander Campbell (1868), vol. 1, which carries Thomas's life [suggested; to confirm]
      - Robert Raikes: Gregory, Robert Raikes: Journalist and Philanthropist (1877); Raikes's
        letters in the Gentleman's Magazine 1784 [suggested; to confirm]
      - Hans Nielsen Hauge: Hauge's own Skrifter and the Testament; a life such as Bang, Hans
        Nielsen Hauge og hans Samtid (1874) [suggested; to confirm]
      - Kosmas Aitolos: Kosmas, Didachai (Teachings) and a Life, English in Vaporis, Father Kosmas,
        the Apostle of the Poor (1977) [suggested; to confirm]
      - Athanasios Parios: Athanasios Parios, Christianike Apologia (1798), and a modern life
        [suggested; to confirm]
    - Quesnel is LISTED until the Réflexions morales (1692-94) are vendored; then he is WHO
      (Melanchthon rule). Owner: the Library thread.
    - Census gaps for people scored here by date of work. The Polish Brethren in exile
      (Lubieniecki), the Waldensians after 1655 (Léger, Morland), the Remonstrant brotherhood
      (Brandt), the Jesuit Ethiopia mission (Lobo) and the Black churches of the new republic
      (Absalom Jones, with McGready, Campbell and Hauge on an era 9 shelf) have no era 8 census
      entry. Owner: the census owner.
    - Leads for the councils list (not scored): see the audit; they include the Moravian synods
      (Gotha 1740, Marienborn, Zeist 1746, Herrnhut 1789), the Pennsylvania synods of 1742, the
      Synod of Tonkin 1670, the Moscow council of 1654, Alba Iulia 1701 and 1728, Angamaly 1787, the
      National Synod of Loudun, the 1653 Coonan Cross assemblies, the Synod of Qarqafe 1806 and the
      Winchester convention of 1803. Owner: the councils scan.
    - Library label errors and odd editions found by the scan, listed in the audit under "Open-Gaps
      items to register": the Chronicon Ephratense header names Peter Miller as Agrippa; the header
      attributes Mack's memoir to his son but the text shows the 1860 editor; Steenoven's letter to
      Noailles is dated "1714" in the OCR; the Charon file holds tomes II and III only (tome I tells
      the 1724 split); the John Hughes dates on the Welsh history file look like a namesake's; Mary
      Dyer is a namesake trap; the Gomidas quotation in the census is in no held file; the census
      says Macrina is sister of King Teimuraz I but Brosset has her as sister of King David. Owner:
      the Library thread.
    - No Jewish, Muslim or Asian chronicler of 1650-1815 is held, and the Hungarian Protestant entry
      has no corpus-map file and no held source; its persons are LISTED. Owner: the Library thread.
    - The coordinator's calls (Mark may overrule): Hacob IV, Simeon of Erevan, Mar Thoma I, Mar
      Dionysius I and De Cock WHO by the two-witness rule, flagged "no own text held";
      Freylinghausen WHO and Reitz LISTED; Arnauld WHO, flagged; Quesnel LISTED; Volney the only
      OUTSIDE WITNESS, with Rycaut, Tournefort, Ludolf and Moreau de Saint-Méry plain; Carey, Allen,
      Yohannan Hormizd and Gregory V left to era 9. No person in the table is alive. Owner: the
      coordinator.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

226. **Open points from the era 10 scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era10/`. The census was not changed.
    134 rows: WHO 6, STORY 2, LISTED 6, WANTED 120. A further 124 rows of people are held for
    Mark. The Library holds almost nothing of 1906–c. 2010. Approved to proceed (coordinator,
    under Mark's full-auto instruction of 2026-11-12).
    - Held for Mark: 124 rows of living people, people of unknown status and people who died in 1990
      or later (Ford, Lefebvre, Schutz, Antonios and Gatu among them). No verdict until Mark rules
      on living people. The list in the audit is the worklist. Owner: Mark.
    - Four entries name no person (Anglican Communion, Church Struggle against Apartheid,
      Protestantism in Latin America, Ecumenical Movement and WCC); their Who view stays empty
      until the combined WANTED list feeds them (coordinator call). Owner: the Library thread.
    - Surma Khanim is WANTED under the women rule; her own 1920 book is the wanted source
      [suggested; to confirm]. Owner: the Library thread.
    - Census flags. The slug `iglesia-ni-cristo-the-way-international-unificat` is truncated: it
      carries "iglesia-ni-cristo" but holds The Way, the Unification Church and La Luz del Mundo,
      and Iglesia ni Cristo has its own entry. C. H. Mason (Church of God in Christ) is not named
      in the Black Church in the Twentieth Century entry. The census owns both.
      Also noted: the Branch Davidian entry is marked not living although its text says remnant
      groups outlasted 1993; "Bishops' Council of August 2000" and "Jubilee Council of August
      2000" are one council under two names. Owner: the census owner.
    - Rauschenbusch's three books and Machen's Christianity and Liberalism are the sources most
      likely to be public domain at once: a short first pass for the combined list (220). Owner:
      the Library thread.
    - E. Kolodziejczyk (1911), carried from era 9, is a source writer and is not scored. Apolo
      Kivebulaya, carried from era 9, is a WANTED row here. Sheptytsky stays in era 9 (WANTED).
      Owner: the Library thread.
    - WANTED sources the Library does not hold, for the combined list (220), major first, then the
      rest. Nothing is queued now (coordinator call). Titles tagged "[suggested; to confirm]" were
      named from the workers' memory. Owner: the Library thread.
      Major-marked rows (47):
      - Walter Rauschenbusch: Christianity and the Social Crisis (1907); Christianizing the
        Social Order (1912); A Theology for the Social Gospel (1917) (the census sources
        list; rights of the 1917 book to confirm)
      - J. Gresham Machen: Christianity and Liberalism (Macmillan, 1923); Ned B. Stonehouse,
        J. Gresham Machen: A Biographical Memoir (1954) (both from the census story sources;
        rights of the 1954 book to confirm)
      - Karl Barth: Der Römerbrief (1919; 2nd ed. 1922); the Barmen Declaration (1934)
        (census sources; rights to confirm)
      - Reinhold Niebuhr: Moral Man and Immoral Society (1932); The Nature and Destiny of
        Man (1941-43) (census sources)
      - Harry Emerson Fosdick: 'Shall the Fundamentalists Win?' (1922); his autobiography
        [suggested; to confirm]
      - Cyrus Ingerson Scofield: The Scofield Reference Bible (1909; 1917) (census sources;
        public domain by date); a life of Scofield that sets out the dispute [suggested; to
        confirm]
      - Martin Luther King Jr.: Eulogy for the Martyred Children (18 September 1963) (census
        story source); the SCLC papers (census sources)
      - W. B. Riley: A life or his sermons and the WCFA records [suggested; to confirm]
      - Óscar Romero: His homilies and his diary (census SOURCES: "Martyr records: Romero's
        homilies and diary") [suggested; to confirm the edition]
      - Peter Maurin: Maurin's Easy Essays (census SOURCES)
      - Stefan Wyszynski: Jasnogorskie Sluby Narodu Polskiego (Komancza, 1956) (census
        SOURCES)
      - Virgil Michel: Orate Fratres (later Worship), from November 1926; the New Catholic
        Encyclopedia entry 'Michel, Virgil' (census SOURCES)
      - Watchman Nee: The Spiritual Man (1928); the Little Flock literature and the Nee-to-
        Lee corpus [named in the census SOURCES; not held]
      - Dietrich Bonhoeffer: Discipleship (1937), Life Together (1939), Letters and Papers
        from Prison (1951, ed. Bethge) [named in census SOURCES; not held]
      - Martin Niemöller: Niemöller's Dahlem sermons and the Pfarrernotbund records [named
        in census SOURCES; not held]
      - J. H. Oldham: Oldham's writings and the Edinburgh 1910 reports [suggested; to
        confirm]
      - John R. Mott: Mott's writings and the Edinburgh 1910 reports [suggested; to confirm]
      - Wei Enbo: A True Jesus Church history and records (1917-) [named in the census
        SOURCES; not held]
      - William J. Seymour: William J. Seymour, The Doctrines and Discipline of the Azusa
        Street Apostolic Faith Mission (1915); The Apostolic Faith (Los Angeles, 1906-1908,
        13 issues) [both named in the census; rights status to confirm]
      - Tahupōtiki Wiremu Rātana: Te Whetu Marama (the movement's paper); the church's
        creed, prayers, hymns and service book; Rātana Pā records [named in the census;
        rights to confirm]
      - Janani Luwum: The Janani Luwum martyrdom record (1977; the Westminster Abbey martyrs
        record, 1998) [named in the census; rights to confirm]
      - Pandita Ramabai: Mukti Prayer-Bell (her mission press); her own books [named in
        census; rights to confirm]
      - Kil Sŏn-ju: Korean church histories (Kil Son-ju); William N. Blair's eyewitness
        account, with Bruce Hunt, The Korean Pentecost and the Sufferings Which Followed
        (1977) [named in census sources]
      - William Nagenda: Nagenda's addresses; the convention record (Kabale 1935-) [named in
        census]
      - Festo Kivengere: Festo Kivengere, I Love Idi Amin (1977) [rights to confirm]
      - William Wadé Harris: Harris's teaching via hearers' records (1926 Benoit interview
        notes); Harrist catechisms and liturgies [named in census sources]
      - Moses Orimolade: Cherubim and Seraphim founding records (Orimolade, 1925) [named in
        census sources]
      - Simon Kimbangu: The 1921 colonial military-court trial record; the EJCSK's
        catechetical and doctrinal publications [named in census sources]
      - R. E. McAlister: Record of the April 1913 Arroyo Seco baptismal sermon [suggested;
        to confirm]
      - Frank Ewart and Glenn Cook: Frank Ewart, The Phenomenon of Pentecost (1947) [rights
        to confirm]
      - G. T. Haywood: G. T. Haywood's writings and hymns [named in census]
      - Victor Houteff: Houteff, The Shepherd's Rod (vol. 1 1930, vol. 2 1932) [named in
        census; rights to confirm]
      - Felix Y. Manalo: Pasugo (from February 1939); the 1914 government registration
        [named in census sources]
      - Dorothy Day: The Long Loneliness (1952); Loaves and Fishes (1963); The Catholic
        Worker paper (1933-) (census SOURCES)
      - Josyf Slipyj: Slipyj's Gulag letters and memoirs (1945-63) (census SOURCES)
      - Dom Lambert Beauduin: The Malines address of 1909 [text not named in the census; to
        confirm]
      - Gabriel Hebert: A. G. Hebert, Liturgy and Society (1935); The Parish Communion
        (1937) (census SOURCES)
      - Maria Skobtsova: Her essays, Essential Writings (Orbis 2003), and a life of her,
        e.g. Plekon, Living Icons (2002) (both named in the census SOURCES); rights to be
        checked by the Library thread [suggested; to confirm]
      - Habib Girgis: His catechetical writings and Sunday-school magazine; Bishop Suriel,
        Habib Girgis (SVS Press, Coptic Studies 2, 2017) (census SOURCES); rights to be
        checked [suggested; to confirm]
      - Kyrion II: The March 1917 declaration and the council acts, and Kyrion II's
        correspondence with Moscow (census SOURCES); Mikheil Kartvelishvili's work on the
        1917 restoration (National Archives of Georgia) [suggested; to confirm]
      - Sergei Bulgakov: Bulgakov's corpus with the 1935-37 Sophia controversy file, both
        sides (census SOURCES); rights to be checked [suggested; to confirm]
      - Georges Florovsky: Ways of Russian Theology (1937) (census SOURCES); rights to be
        checked [suggested; to confirm]
      - Vladimir Lossky: Mystical Theology of the Eastern Church (1944) (census SOURCES);
        rights to be checked [suggested; to confirm]
      - Iosif Trifa: Oastea Domnului weekly (1923-) and Trifa's books (census SOURCES)
        [suggested; to confirm]
      - Grigoris Balakian: Armenian Golgotha (1922; ET 2009) (census SOURCES); rights to be
        checked [suggested; to confirm]
      - Tikhon: Tikhon's 1918 anathema and the acts of the Local Council, and a life
        [suggested; to confirm]
      - Metropolitan Sergius: The Declaration of 1927 AND the catacomb rejections, both
        sides (census SOURCES) [suggested; to confirm]
      Other rows (73):
      - Victor Paul Wierwille: Victor Paul Wierwille, Power for Abundant Living (1971) and
        Jesus Christ Is Not God (1975) [named in the census; copyright likely; rights to
        confirm]
      - Frank Bartleman: Frank Bartleman, Azusa Street (orig. How Pentecost Came to Los
        Angeles, 1925) [rights to confirm]
      - Joe Church: Joe Church, Quest for the Highest (1981) [rights to confirm]
      - Joseph Babalola: CAC records around Babalola's 1930 revival [named in census
        sources]
      - Engenas Lekganyane: Engenas Lekganyane founding record (1924/25); the ZCC's
        practice-borne record [named in census sources]
      - Alice Lenshina: Lumpa Church records; Andrew Roberts's chapter (1970) is a later
        retelling [named in census sources]
      - Eusebio Joaquín González: La Luz del Mundo Apostleship confession (founding 1926)
        [named in census sources]
      - William N. Blair: William N. Blair, eyewitness account (with Bruce Hunt, The Korean
        Pentecost, 1977) [named in census sources; rights to confirm]
      - Jessie Penn-Lewis: Penn-Lewis and Roberts, War on the Saints (1913) [named in census
        sources; rights to confirm]
      - Reuben Spartas Mukasa: Dictionary of African Christian Biography, 'Spartas, Reuben';
        his church's records [named in census sources]
      - Johane Masowe: The apostolics' own records [suggested; to confirm]
      - André Matswa: Matsouanist records [suggested; to confirm]
      - Ben and Lois Roden: Ben and Lois Roden's Branch publications [named in census
        sources]
      - Michael Joseph Savage: The 1936 Ratana-Savage meeting and alliance record [named in
        census sources]
      - Silas Eto: The movement's own records where published [suggested; to confirm]
      - Apolo Kivebulaya: His diary (Luganda), extracts translated in Anne Luck, African
        Saint (1963); Kevin Ward, "Apolo Kivebulaya", Dictionary of African Christian
        Biography (census sources of the era 9 entry) [rights to confirm]
      - Paul Tillich: Systematic Theology (1951-63) (census sources; in copyright)
      - Rudolf Bultmann: New Testament and Mythology (1941) (census sources; in copyright)
      - Clarence Larkin: Dispensational Truth (1918) (census sources; public domain by date)
      - Curtis Lee Laws: The naming article, Watchman-Examiner (1920) (census sources)
      - Marshall Keeble: Keeble's stenographed sermons and the Gospel Advocate meeting
        reports, 1914-1968; Richard T. Hughes, Reviving the Ancient Faith (1996) for the
        life (the last from the census sources; the first two suggested; to confirm)
      - M. L. Andreasen: M. L. Andreasen, Letters to the Churches (1959); Seventh-day
        Adventists Answer Questions on Doctrine (1957; annotated ed., Knight, 2003) (both
        from the census story sources; the letters circulated privately, so a copy may be
        hard)
      - Clarence Orvil Dodd: The Faith (Warren, Ohio, 1937-), C. O. Dodd, editor; Richard C.
        Nickels, A History of the Seventh Day Church of God (1977; rev. 1999) (both from the
        census story sources)
      - William Jennings Bryan: The World's Most Famous Court Trial: Tennessee Evolution
        Case (1925, the stenographic transcript, the census's primary source)
      - The four girls of Sixteenth Street Baptist Church: Martin Luther King Jr., Eulogy
        for the Martyred Children (18 September 1963); Sixteenth Street Baptist Church, its
        own history and memorial record; the trial records (1977, 2001, 2002) (all from the
        census story sources)
      - Jim Jones: Peoples Temple records and the Disciples yearbook entries; Kenneth
        Teegarden's account [suggested; to confirm]
      - Donald Grey Barnhouse: 'Are Seventh-day Adventists Christians?', Eternity (September
        1956) (census story source)
      - LeRoy Froom: Seventh-day Adventists Answer Questions on Doctrine (1957), signed by
        no author; Froom's own works [suggested; to confirm]
      - Walter Martin: His account of the conversations [suggested; to confirm]
      - B. C. Goodpasture: The Gospel Advocate editorial (December 1954) (census story
        source)
      - Roy Cogdill: The Cogdill-Woods Debate (1958); the Gospel Guardian (census story
        sources)
      - George Tyrrell: His published works that drew the 1907 condemnations [titles not
        named in the census; to confirm]; Lamentabili and Pascendi (1907) as the Roman side
        (census SOURCES)
      - Havryil Kostelnyk: Bociurkiw, The Ukrainian Greek Catholic Church and the Soviet
        State (1939-1950) (CIUS, 1996); the acts of the Lviv 'Sobor' and the NKGB/KGB files
        opened after 1991 (census SOURCES)
      - Paul VI: His Kampala homily (31 July 1969, French text on vatican.va); the Missal of
        1969-70; the RCIA (1972) (census SOURCES); the Joint Catholic-Orthodox Declaration,
        7 December 1965, with Athenagoras I
      - Alfred Loisy: His published work condemned in 1907 [titles not named in the census;
        to confirm]
      - Joseph Kiwanuka: The Dictionary of African Christian Biography entry 'Kiwanuka,
        Joseph'; Catholic-Hierarchy entry (census SOURCES); his own letters [not named; to
        confirm]
      - Joseph-Albert Malula: The Roman Missal for the Dioceses of Zaire (approved 1988);
        Vatican News report (February 2023) (census SOURCES)
      - Placide Tempels: Tempels, La philosophie bantoue, trans. A. Rubbens (Lovania, 1945);
        Fabian, Jamaa (1971) (census SOURCES)
      - Thomas Tian Gengxin: Ticozzi, 'The 70th anniversary of Church hierarchy in China (11
        April 1946)' (census SOURCES, a secondary account)
      - Boleslaw Kominek: Oredzie biskupow polskich do ich niemieckich braci (Rome, 18
        November 1965) (census SOURCES)
      - Franciszek Blachnicki: IPN Lublin brochure on Fr Franciszek Blachnicki (census
        SOURCES); his own Light-Life texts [not named; to confirm]
      - Rutilio Grande: Martyr records for Rutilio Grande (1977) (census SOURCES, "Martyr
        records")
      - Cristobal Magallanes and his 24 companions: John Paul II, homily for the
        canonization of Cristobal Magallanes and 24 companions (21 May 2000), vatican.va;
        Jean Meyer, La Cristiada, 3 vols (Siglo XXI, 1973-74) (census SOURCES)
      - Pius XII: Divino Afflante Spiritu (1943); Ad Apostolorum Principis (29 June 1958)
        (census SOURCES)
      - Pius XI: His address to the newly consecrated Chinese bishops (28 October 1926); the
        1928 encyclical Mortalium Animos, which ruled Catholics could not take part in the
        ecumenical movement (census, the-ecumenical-movement-and-the-wcc) [suggested; to
        confirm] [Acta...
      - A. Kagame: Abblé et al., Des prêtres noirs s'interrogent (Cerf, 1956) (census
        SOURCES)
      - Jaime de Barros Camara: The Rio conference documents of 1955 and the Encyclopedia of
        Religion entry 'CELAM' (census SOURCES)
      - Leonidas Proaño: Awiti, La trayectoria pastoral de Leonidas Proaño (Quito, 2023, a
        thesis); his own pastoral writings [not named; to confirm]
      - Michal Klepacz: His part in the message of 18 November 1965 [not named; to confirm]
      - Annibale Bugnini: His own account of the reform [not named in the census; to
        confirm]
      - John XXIII: His council documents and letters [not named in the census; to confirm]
      - Tewophilos: The church's own Derg-era martyrology; Binns, The Orthodox Church of
        Ethiopia: A History (I.B. Tauris, 2017) (census SOURCES) [suggested; to confirm]
      - Mar Shimun XXIII: Records of the Church of the East in exile (Chicago) and a life;
        the census SOURCES name the exile records, not a title [suggested; to confirm]
      - Alexy I: The Tomos of 10 April 1970 granting autocephaly to the Orthodox Church in
        America (census SOURCES: "The Orthodox Church in America's autocephaly record
        (1970)") [suggested; to confirm]
      - Alexander Schmemann: For the Life of the World (1963); The Journals 1973-1983 (SVS
        2000) (census SOURCES); rights to be checked [suggested; to confirm]
      - Kyrillos VI: Kyrillos VI papers (1959-71) (census SOURCES) [suggested; to confirm]
      - Traian Dorz: Traian Dorz's hymns and prison memoirs (census SOURCES) [suggested; to
        confirm]
      - Abune Basilios: The Tawahedo church's institutional record of the 1959 autocephaly
        (census SOURCES) [suggested; to confirm]
      - Abdul Masih II and Baselios Paulose I: Syriac Orthodox patriarch and the first
        Catholicos of Malankara: The 1912 consecration record; Malankara synodal records and
        the Jacobite patriarchate documents (census SOURCES) [suggested; to confirm]
      - Ambrosi: The 1922 protest memorandum and the trial record (census SOURCES)
        [suggested; to confirm]
      - Joseph of Petrograd: The catacomb and True-Orthodox rejections of the Declaration
        (census SOURCES) [suggested; to confirm]
      - Athenagoras I: the Joint Declaration of 7 December 1965: Joint Catholic-Orthodox
        Declaration, 7 December 1965 (vatican.va) (census SOURCES) [suggested; to confirm]
      - Miron Cristea: Romanian Patriarchate, 'Patriarch Miron Cristea' (patriarhia.ro)
        (census SOURCES) [suggested; to confirm]
      - Dimitrije: Novosti (Belgrade), a century since the Tomos for the unification of the
        Serbian church (census SOURCES) [suggested; to confirm]
      - Kiril of Plovdiv: Statement of the Bulgarian Orthodox Church on the restoration of
        the patriarchate, 10 May 1953 (census SOURCES) [suggested; to confirm]
      - Sandu Tudor: Sandu Tudor's writings and a life; the census names only a 2025 article
        (Stanciu) [suggested; to confirm]
      - Khoren I: Etchmiadzin records under Soviet rule (census SOURCES); a life of Khoren I
        [suggested; to confirm]
      - Surma Khanim: Her own 1920 account of the murder and of the church's customs
        (Assyrian Church Customs and the Murdering of Mar Shimun, 1920) [suggested; to
        confirm]
      - John Sung: John Sung's diaries as compiled by his family [named in census SOURCES;
        not held]
      - V. S. Azariah: Azariah's addresses and a life [suggested; to confirm]
      - Cheng Jingyi: Cheng's writings and a life [suggested; to confirm]
      - George W. Peters: Indonesia Revival: Focus on Timor (Zondervan, 1973) [named in
        census SOURCES; not held]
      - Ju Gi-cheol: A life of the pastor [suggested; to confirm]; the 2025 news report is a
        census source, not held

227. **Open points from Mark's rulings of 2026-11-12 (living people, recent deaths, Spiritualism, Syriac page).** Owners as noted.
    Source: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era10/` and
    `.../2026-11-12_who-scan-era9/`. The census was not changed. These are Mark's rulings, picked from
    options and relayed by the coordinator.
    - Era 10 after the rulings: 244 rows: WHO 6, STORY 2, LISTED 108, WANTED 128.
      101 of the LISTED rows are living people or people of unknown status, "Listed only until
      death". This replaces the "held for Mark" list in 226. Era 9 after the rulings: 249 rows:
      WHO 34, STORY 11, LISTED 49, WANTED 155. Owner: the coordinator.
    - Open-Gaps 226 is not edited. Its "Held for Mark" bullet is superseded by this entry. Eight
      people it did not list as WANTED are now WANTED sources for the combined list (220), because their
      deaths are stated in the census: Ford, Lefebvre, Schutz, Antonios, Gatu, Moon, Abiodun, Ilia II.
      Owner: the Library thread.
      - Desmond Ford: Desmond Ford, Daniel 8:14, the Day of Atonement, and the Investigative
        Judgment (1980); the Glacier View statements in Ministry (October 1980) (both from
        the census story sources)
      - Marcel Lefebvre: His Declaration of 1974 and the protocol, sermon and decree of 1988
        (census SOURCES: "Lefebvre's 1974 Declaration; SSPX (1970; 1988 consecrations...)")
      - Roger Schutz: The Rule of Taizé (1954; later editions as The Sources of Taizé) and
        Brother Roger's other writings [named in the census SOURCES; not held]
      - Antonios: Eritrean church records of the 1993 autocephaly and the 2006 deposition;
        Binns (2017) (census SOURCES) [suggested; to confirm]
      - John G. Gatu: Gatu's 1971 moratorium call in his own words [not named in the census;
        to locate]; Christianity Today, "What's Behind the Idea of a Missionary Moratorium?"
        (November 1974); the WCC obituary of John G. Gatu (census SOURCES)
      - Sun Myung Moon: The Divine Principle (1966) [named in the census; not held]
      - Christianah Abiodun: Christianah Abiodun Emmanuel, account of the vision of June
        1925 and the founding of the Cherubim and Seraphim, in the Society's own
        publications; J. D. Y. Peel, Aladura (1968) [named in the census; not held]
      - Ilia II: His sermons and the Patriarchate's record of his reign [suggested; to
        confirm]
    - Spiritualism and New Thought (Mark: "Remove them"): the 6 rows (10 people) are removed from the era 9
      audit. Strike their sources from the WANTED list of Open-Gaps 224 (not edited): the Fox sisters, A. J.
      Davis, Hardinge Britten, Quimby, Hopkins, the Fillmores; and the "Scope hold for Mark" bullet of 224 is
      answered. They can be added back if the scope widens. Owner: the Library thread.
    - Possible deaths before 1990, known only from common knowledge, left "status unknown": Abrams, Yi Ki
      Poung, Fernando and Ana Stahl, Melnyk, Pelvetsky, Binsted, Naayem, Burton, Suzuki Masahisa, Isabelo de
      los Reyes Jr., Anderson. Each can be scored once a source confirms the death. Owner: the Library
      thread.
    - Syriac (Edessa/Nisibis) world page faults (Mark: "In the clean-up": fix them with the other 11 built
      worlds, as one change order, alongside the about 560 bare names). Owner: the clean-up change order.
      - Ephrem's Who line reads "about 338–373" when he was born c. 306.
      - "Ephrem" and "Ephraim" are mixed.
      - "Jacob", "Simeon" and "Marutha (unknown)" are bare names in the Voices headings.
      - The "This world's own hedge" labels are jargon.
      - "Not X but Y" lines: "He prayed not for the army's destruction, but for its withdrawal";
        "not a philosopher's definition - it was praise".
      - Hyphens are used as dashes.
      - Mark's ruling of 2026-11-11 stands: the flood story stays a full story, and its date already reads
        "513 of the Greeks, around the year 201".
228. **Placing the approved Who profiles (2026-11-12).** The eight era 1 batch 1 profiles (Josephus,
    Ignatius of Antioch, Marcion of Pontus, Justin Martyr, Clement of Alexandria, Eusebius of Caesarea,
    Hermas, Valentinus) are approved to proceed and held in
    `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era1/batch1/`. None is in the census or on
    the site. Open: how the map Who build (the slice in 217) takes them in, where each card's fields live,
    and when the briefs are recorded in Jon's voice (a paid run, gated by sample and approval). Mark's ruling
    of 2026-11-12 makes the profile "Marcion of Pontus". The census uses that form twice and "Marcion of
    Sinope" once, and the one "of Sinope" follows the ruling when the profile is placed. Owner: the map
    build slice.


229. **Open points from the supplement Who scan (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/`. The census was not changed.
    Decision-Log, "The supplement Who scan" (2026-11-12).
    - 253 rows: WHO 108, STORY 36, LISTED 92, WANTED 17. Eras: 1 (18), 2 (22), 3 (49), 4 (21), 5 (12),
      6 (39), 7 (23), 8 (22), 9 (46), 10 (1). Owner: the coordinator.
    - 17 WANTED sources for the combined list (220). Each has no held text. Maron (Theodoret's
      Religious History on Maron; the Maronite tradition's own account); Abelard (the Historia
      calamitatum); Nehemiah Tile and Mangena Mokone (Sundkler, Bantu Prophets in South Africa, 1948;
      the church's founding records); Evan Roberts (War on the Saints, 1913; journalism); "Awstin"
      (the Western Mail revival supplements, 1904-05); W. T. Stead (The Revival in the West, 1905);
      Washington Gladden (Applied Christianity, 1886); Charles M. Sheldon (In His Steps, 1896);
      Charles A. Briggs (the heresy trial record, 1891-93); A. A. Hodge and B. B. Warfield
      ("Inspiration", Presbyterian Review, April 1881); David Lipscomb (the Gospel Advocate);
      Jerry McAuley (his own account of the Water Street Mission); George and Sarah Clarke (the Pacific
      Garden Mission); James Thomson (Letters on the Moral and Religious State of South America,
      1827); Adolf von Harnack (What Is Christianity?, 1900); Josiah Ositelu (the Church of the Lord
      (Aladura) constitutions). Edition names from memory are tagged "[suggested; to confirm]" in the
      audit. Also wanted, no row: Paulinus of Aquileia's own Contra Felicem (not held). Owner: the
      Library thread.
    - Change-order items on earlier audits (no earlier audit is edited; coordinator's call). (1) Era 6:
      Isidore of Kiev is LISTED; his letters (PG 159 337-339) and Migne's notice of his career (55512-55516)
      are held, so the row may be rescored WHO with a thin life. (2) Era 3: the note that groups Zoilus
      with the African Three Chapters bishops is wrong; Zoilus is the Alexandrian patriarch put in after
      the deposition of Apollinaris (MOMM2 18879-18881). (3) Era 5: the Verdict cell of Anna Komnene reads
      "WANTED (OUTSIDE WITNESS)" while its text says "without the label". (4) Era 7: the Josaphat Kuntsevych
      row says WANTED, yet Susza's life of Josaphat (SUSZJ) is held. Owner: the coordinator.
    - Rows the scan could not settle alone. Yared and Pantalewon (era 3, WHO) rest on late Lives and may
      fall under the later-retelling rule used for the early saints; the ruling named only the ten
      founders. Roger Clap (LISTED) could be STORY on the Hopper precedent. Findian: the early "Vinnian"
      sources are held but editors split between Clonard and Moville, so a Vinnian row on the Penitential
      is possible. Owner: the coordinator.
    - Boundary and placement: Hasan-Jalalean is era 8 by date and was not scored; Philo falls before
      era 1. Owner: the coordinator.
    - Library finds. Names are double-spaced in many OCR files, so single-space searches wrongly returned
      "not held" for John of Parma, Pascal of Vittoria, Joan of Arc and Andrew of Perugia. The check
      re-ran the 17 WANTED rows of this scan whitespace-tolerant (16 confirmed not held). Step one of the
      combined WANTED list is the same script over the WANTED rows of the ten era audits; any row found
      held becomes a change-order item by era and is dropped from the list. Owner: the coordinator, then
      the Library thread.
    - The "Major?" column is a proposal for each WHO; Mark confirms it in each batch.

230. **Open points from the combined wanted list (2026-11-12).** Owners as noted. Source:
    `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/`. The census was not changed.
    Decision-Log, "The combined wanted list" (2026-11-12). This entry answers the open points of 229.
    - The list holds 461 person sources (150 major), 27 outside-witness sources with no person row and 46
      council records. By era (sources / major): 1 (4 / 1), 2 (3 / 2), 3 (6 / 0), 4 (41 / 5), 5 (44 / 12),
      6 (14 / 4), 7 (9 / 0), 8 (43 / 8), 9 (168 / 63), 10 (129 / 55). Owner: the coordinator, then the
      Library thread.
    - Change-order items from the whitespace-tolerant re-run: Charles Simeon (era 9) is held after all,
      as Wesley's own entry of 20 December 1784 and the editor's life note in Wesley's Journal vol. 7
      (Curnock), with a line in Marsden's life. The era 9 row says "grepped Charles Simeon: none". The
      row is dropped from the list; rescore it (WHO flagged "no own text held" by the two-witness rule
      for heads, or LISTED as a later retelling). No other WANTED row proved held; the hits on the
      others are mentions, namesakes or sources the audit row already names. The finding is in
      `Rerun_Findings.md`. Owner: the coordinator.
    - Resolved from 229: Yared and Pantalewon are LISTED (later-retelling rule, Lives dated); Roger Clap
      is STORY; Vinnian has a separate LISTED row. The supplement audit now reads 254 rows: WHO 106,
      STORY 37, LISTED 94, WANTED 17. Owner: the coordinator.
    - Major marks for 175 rows (all of eras 1 to 5 and the conditional marks later) are proposals by a
      Sonnet pass, 35 yes; Mark confirms them or changes them. They are in `Major_Proposals.md`. Owner:
      the coordinator.
    - "Would move to" is taken from each audit row's own wording; 170 rows say nothing, so the cell
      reads "inferred" and gives the rule's default. The Library thread should treat those as a guess.
      Owner: the Library thread.
    - Source names are the audits', many from memory and tagged "[suggested; to confirm]"; confirm each
      edition before acquiring it. The re-run searched names as the audits spell them; a source named
      under another spelling may still be held. Owner: the Library thread.
231. **Era 1 Who batch 2: site list lines and name gaps (2026-11-12).** The eight batch 2 profiles are
    approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era1/batch2/`.
    None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-12_who-profiles-era1-batch2/`;
    Decision-Log, "Who profiles, era 1 batch 2" (2026-11-12).
    - List lines in `cft-website/index.html`, reported by the round 1 review and not changed: Hippolytus
      is listed under two names, "Hippolytus" and "Hippolytus of Rome"; Bardaisan of Edessa has no person
      line (his tradition lists only his pupil Philip); Tacitus appears only as a source row; Suetonius
      does not appear. Owner: the map Who build slice, with the placing in "Placing the approved Who
      profiles" (2026-11-12).
    - Name gaps, with no place in a vendored source: Paulinus, secretary to Ambrose of Milan (Rolfe gives
      only "his secretary"), and Germanus, the bishop who accused Dionysius of Alexandria (McGiffert says
      his see is not known). Both are left as the sources have them. Owner: the Library thread.
    - Three era 1 WHO rows from the supplement scan are in neither batch: Peter of Alexandria, Anatolius
      of Alexandria and Laodicea, and Polycrates of Ephesus. Owner: the coordinator.
232. **Pronunciation list: proposals awaiting Mark, and a paid test not yet approved (2026-11-12).** Mark's
    seven names are live in `Build/tools/tree-narration-pronunciations.json`; Decision-Log, "Pronunciation
    list for the audio script" (2026-11-12). The page is the "Pronunciation List" Artifact.
    - 97 more names are proposed under the Standard English rule: 53 sure, 33 likely, 11 unsure, by
      era on the page. A fresh Opus agent disagreed with 14 of them and the page marks those. None is
      applied. Owner: Mark, to approve, change or drop each; then the coordinator adds the approved rows.
    - Whether `[pause]` between paragraphs gives the half second Mark asked for on eleven_v4 is unknown.
      The docs list no pause tags for v4. Fallback: an ellipsis at the paragraph end. Owner: Mark, by ear.
    - The docs do not say whether pronunciation dictionaries work on v4. Not tested; the list uses respellings.
    - Paid test: six lines, 459 characters, about 223 credits at 0.485 per character. Not run. Needs Mark's
      named approval with a cap, through the coordinator. Owner: the coordinator.
    - The `audio/*.audio.txt` files in the era 1 batches are checked-in copies of the brief with tags and
      do not carry the respellings. The run builds its request from the census text. Owner: the coordinator.
233. **Who scan records cleaned: duplicates merged, change-order items closed (2026-11-12).** Decision-Log, "Who scan records cleaned" (2026-11-12). Records: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-dedupe/Removed_Rows.md` and the ten era audits plus the supplement.
    - Closed: the change-order items of Open-Gaps 229, "Who scan supplement" (2026-11-12), and 230, "combined wanted list" (2026-11-12): Isidore of Kyiv (now STORY), the Zoilus note, the Anna Komnene Verdict cell, Josaphat Kuntsevych (now LISTED) and Charles Simeon (now LISTED). Owner: the coordinator.
    - Pliny the Younger is Who, outside witness, not major (Mark, 2026-11-12). His profile goes in era 1 batch 3. Owner: the coordinator.
    - Still open: `Era8_Carry_Rows.md` in the era 7 folder repeats rows that era 8 re-scored; it was not changed. Owner: the coordinator.
234. **Lactantius, Div. inst. V.4.3: the Latin wanted back on the Tertullian link (2026-11-13).** Decision-Log, "Data release 40" (2026-11-13). The link `tertullian-s-voice--latin-apologists` cites the public-domain English of ANF 7 since release 40, because the held public-domain scan of the 1890 Brandt print (CSEL 19) lacks page 411.
    - Wanted: a public-domain scan of Brandt's 1890 CSEL 19 that holds page 411 (Div. inst. V.4.3). When it is vendored, add the Latin quote beside the English. Listed on the combined wanted list, Library-label corrections, row 19. Owner: the Library thread, through the coordinator.
235. **Era 1 Who batch 3: a Pliny edition wanted, and the batch 2 and Pliny items closed (2026-11-13).** The four batch 3 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era1/batch3/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era1-batch3/`; Decision-Log, "Who profiles, era 1 batch 3" (2026-11-13).
    - Wanted: a public-domain edition of Pliny the Younger's Letters, Book 10. The Library holds no Pliny file. The profile cites the full English of letters 96 and 97 inside McGiffert's note to Eusebius, Church History III.33 (npnf201), and says so on its card. The source is not on the combined wanted list. Owner: the Library thread, through the coordinator.
    - Closed: the three era 1 WHO rows from the supplement scan named in Open-Gaps, "Era 1 Who batch 2: site list lines and name gaps" (2026-11-12), and the Pliny profile named in Open-Gaps, "Who scan records cleaned" (2026-11-12). All four are now profiled.
    - Placing on the site, list lines, and where the outside-witness label renders go with the map Who build, as in "Placing the approved Who profiles" (2026-11-12). Owner: the map Who build slice.
236. **Era 2 Who batch 1: list lines, Library items, and the supplement rows (2026-11-13).** The nine batch 1 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch1/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch1/`; Decision-Log, "Who profiles, era 2 batch 1" (2026-11-13).
    - List lines in `cft-website/index.html`, reported by the round 1 review and not changed: Arius, Antony the Great, Frumentius and Hilarion of Gaza have no people-list line. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Aetius of Antioch's Syntagmation is held only in the Greek of PG 42 (Epiphanius, Panarion 76), whose vendoring header marks it unquotable until checked against the page image. The brief tells his argument in modern words and quotes none of it. Owner: the Library thread.
    - Not held, and noted on the cards: Antony's seven letters (the Library has only Jerome's notice of them) and the Greek Lives of Pachomius. The Pachomius and Antony profiles rest on Palladius, Sozomen, the Ethiopic Rules and Athanasius's Life. Owner: the Library thread, to weigh for the wanted list.
    - The supplement Who scan's twelve era 2 WHO rows (Ossius of Cordoba, Alexander of Alexandria, Eutyches, Moses the Black, Eusebius of Nicomedia, Liberius of Rome, Marcellus of Ancyra, Marius Mercator, Eznik of Kolb, Prosper of Aquitaine, Hilary of Arles, Germanus of Auxerre) are not in the era 2 scan sequence these batches follow. Owner: the coordinator.
237. **Era 2 Who batch 2: list lines, name gaps, Library items, and a scan date (2026-11-13).** The nine batch 2 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch2/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch2/`; Decision-Log, "Who profiles, era 2 batch 2" (2026-11-13).
    - List lines: Damasus of Rome, Priscillian and Macrina the Younger have no row in any census people list; they are named only in voices lines and entry text. Auxentius of Durostorum is listed only under the era 3 movement "Gothic, Vandal & Lombard Homoian Christianity". Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Name gaps, left as the sources have them: Maximinus (given only as an Arian bishop), and Evodius in the Priscillian account (given by role). Ithacius is "of Sossuba" in Roberts's English and Halm's Latin of Sulpicius Severus, where the census has "Ossonoba"; the card uses the vendored form. Owner: the Library thread.
    - Not held, and noted on the cards: Cyril of Jerusalem's Letter to Constantius (known here through Gifford and Sozomen), Jerome's continuation of the Chronicle (used as Gifford quotes it), Augustine's Against the Letter of Parmenian, and a usable text of Basil's Against Eunomius (the PG 29 file is Greek with a garbled Latin column). Priscillian's own treatises are held only in a Schepss scan marked poor, so the brief tells them in modern words and quotes none. No held line gives the Donatist council that condemned Tyconius. Owner: the Library thread, to weigh for the wanted list.
    - Scan correction: the era 2 scan's Priscillian row says his following lasted "to Braga 563"; the held acts date that council era 599, which is 561. The scan's birth years for Cyril, Apollinaris, Macrina and Eunomius rest on no held line. The audit is not edited. Owner: the coordinator.
238. **Era 2 Who batch 3: list lines, tradition names, Library items and two ids (2026-11-13).** The nine batch 3 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch3/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch3/`; Decision-Log, "Who profiles, era 2 batch 3" (2026-11-13).
    - List lines in `cft-website/index.html`, reported by the round 1 review and not changed: none of the nine has a people-list line. Didymus the Blind and Evagrius Ponticus appear only as voice entries in their traditions' source lists. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card tradition names that are not site tradition names: Epiphanius of Salamis "Palestinian / Cyprus" and Olympias of Constantinople "Constantinople", taken from the era 2 scan. Settle with the placing. Owner: the map Who build slice.
    - Two ids differ from the scan's bare names. `fabiola-of-rome`: Jerome's Letter 126 has a second Fabiola, whom Fremantle's edition says "must be carefully distinguished". `olympias-of-constantinople`: no held source writes that form, but Palladius's Dialogue calls her "the deaconess of Constantinople" and says "There are several ladies of that name". Owner: the coordinator, if a different form is wanted before placing.
    - Not held: an English Panarion (the Library holds heresies 34 to 80 in Greek and Latin only), Panarion heresies 1 to 33, and the Ancoratus; Paulinus of Nola's Letter 29, which W. K. Lowther Clarke names with Palladius as the chief source on Melania the Elder; Didymus's commentaries and Jerome's Latin of his On the Holy Spirit; and a Latin text of Ammianus Marcellinus (only Yonge's 1862 English, from an uncorrected scan). The Mingarelli edition of Didymus's On the Trinity is held, but its Greek column did not survive the scan. Owner: the Library thread, to weigh for the wanted list.
    - Martin of Tours: Alexander Roberts's English of Sulpicius, Chronicle II.50, has the Priscillian trial put off "as long as Martin survived". Halm's Latin says while Martin was at Trier, and the brief follows the Latin. Owner: the Library thread, to note against the npnf211 file.
239. **Era 2 Who batch 4: list lines, Library items, and scan corrections (2026-11-13).** The nine batch 4 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch4/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch4/`; Decision-Log, "Who profiles, era 2 batch 4" (2026-11-13).
    - List lines: Palladius of Helenopolis and Philostorgius have no people-list line in the census. Honoratus of Arles is named only in the voices line of "Gallic Monastic-Ascetic Christianity", and Paulinus of Milan only in the voices line of the Ambrose of Milan entry. Rufinus has two lines that disagree: "Rufinus of Aquileia" under "Hieronymian Ascetic-Literary Christianity" and "Rufinus of Concordia" under "The Church of Aquileia". Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Traditions on the cards, to settle with the placing: Palladius "Desert Monasticism" (the other choice is "Antiochene Exegetical Christianity (Chrysostom-centered)"); Philostorgius "Anomoean (Eunomian) Christianity"; Paulinus "Ambrosian Milan (standalone)", the census name. Owner: the map Who build slice.
    - Not held, and noted on the cards: Prosper of Aquitaine's book against Cassian and the letters of Prosper and Hilary to Augustine; Paulinus of Nola's letters to Sulpicius Severus; an English Life of Honoratus (the held sermon is Latin in a rough scan, so the brief quotes none of it); an English Letter to Demetrias; the Indiculus of Possidius; Augustine's Letter 105 and Against Cresconius; Bidez's 1913 edition of Philostorgius; and Butler's Greek Lausiac History. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections: the Paulinus of Milan row's Marius Mercator claim (see the Decision-Log entry), and the scan's years for Rufinus, Sulpicius, Pelagius, Philostorgius and Honoratus, which rest on no held line. The audit is not edited. Owner: the coordinator.
240. **Era 2 Who batch 5: list lines, card traditions, Library items, and scan corrections (2026-11-13).** The ten batch 5 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch5/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch5/`; Decision-Log, "Who profiles, era 2 batch 5" (2026-11-13).
    - List lines: Socrates of Constantinople is named only in the voices line of "Novatianism", and Sozomen is in no census list. Mesrop Mashtots is named only in the voices line of "Armenian Christianity (conversion era)", and Koriun only in a relation note. Alexander of Alexandria, Eusebius of Nicomedia and Ossius of Cordoba have no people-list line. Cyril of Alexandria, Leo of Rome and Theodoret of Cyrrhus each have one. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions that are not site tradition names, taken from the scans: Socrates "Constantinople" and Sozomen "Gaza / Constantinople". Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted on the cards: an English or Armenian Koriun (only Emine's French, in Langlois's edition), and any writing of Mesrop's own; Theodoret's Religious History, and the Chalcedon session where he anathematized Nestorius (held only as Blomfield Jackson quotes it); the letters of Acacius of Beroea and of Epiphanius, Cyril's archdeacon, behind the bribery charge; Sozomen's Greek before Book 5. Prosper's Chronicle is held only in Mommsen's Latin scan, so the Leo brief tells it in modern words. Owner: the Library thread, to weigh for the wanted list.
    - Scan and census corrections: no held line gives "about 405" for the Armenian alphabet, which the census also uses, or the scan's "about 362 to 440" for Mesrop (a note in Langlois gives 361 to 441). That Koriun wrote at Catholicos Joseph's request is Langlois's statement; Lazar of Pharp says King Vramshapuh asked, and the records tag it contested. Sozomen's "about 400 to 450" rests on no held line, and the held edition spells "Salaminius". Eusebius of Nicomedia's death "about 341 to 342" is a note in A. C. Zenos's edition of Socrates, and Constantine's baptism by him is Blomfield Jackson's note, not Theodoret's text. The audits are not edited. Owner: the coordinator.
241. **Era 2 Who batch 6: list lines, card traditions, Library items, and scan corrections (2026-11-13).** The nine batch 6 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch6/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch6/`; Decision-Log, "Who profiles, era 2 batch 6" (2026-11-13).
    - List lines: none of the nine has a row in any census people list. Prosper of Aquitaine is named in the entry text of "Gallic Monastic-Ascetic Christianity" (the "Massilians" label) and in two link notes. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions taken from the scans that name a record the person appears in, not a party he belonged to: Marcellus of Ancyra "Cappadocian Christianity" (the shelf of Epiphanius), Marius Mercator "Pelagianism" (he wrote against it), Prosper of Aquitaine "Gallic Monastic-Ascetic Christianity" (he wrote against its Marseilles teachers) and Eutyches "The Church of Alexandria and Miaphysite Egypt" (whose Syriac chronicle faults him). Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted on the cards: Prosper's book against Cassian, On the Ungrateful (one verse only, in a note) and any English Prosper; Marcellus of Ancyra's book against Asterius, Eusebius of Caesarea's books against him, and an English text of his letter (held only in the Greek of PG 42, a rough scan); Eutyches's letters in Greek; the full Life of Hilary of Arles (only Mansi's extract) and an English Hilary; the Refutation of Eznik of Kolb beyond part of book II in French; an English Life of Germanus (Levison's Latin only); an English Marius Mercator. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections: no held line gives the supplement scan's "c.405" for Moses the Black, "c.378-448" for Germanus of Auxerre (Levison reckons his years as bishop near 418 to 448, and calls them not certain), "352-366" for Liberius (editors' dates), or "c.401-449" for Hilary of Arles (a vendoring header; Richardson and Jackson disagree on his birth). Prosper's "Born 403 ... died 463" is Richardson's note. The Eznik row's "the date of his work is Contested" has no held sides: no held line dates the Refutation. The Moses row's "sit in thy cell" saying names only an Abba Moses of Scete. The audits are not edited. Owner: the coordinator.
    - Langlois's introduction to Eznik names the assembly "Aschdischad" (Ashtishat), where Elishe has Artashat and Lazar of Pharp no place. Owner: the Library thread, to note against the Langlois file.

242. **Era 3 Who batch 1: list lines, a card tradition, Library items, and scan corrections (2026-11-14).** The ten batch 1 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch1/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch1/`; Decision-Log, "Who profiles, era 3 batch 1" (2026-11-14).
    - List lines: Vardan Mamikonian, Euthymius the Great and Moses of Khoren have no row in any era 3 census people list. The other seven have one. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card tradition taken from the scan that names a record the person appears in, not his own church: Victor of Vita "Gothic, Vandal & Lombard Homoian Christianity", the church that persecuted his. Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted in the cards or `records.json` (the Chronicle of Seert is not noted in the batch): Carrière's study of the Abgar legend in Moses of Khoren (Paris 1895), which Harnack lists by title only, so no held line says what date it argues (on the want list by the coordinator's ruling, 2026-11-14); Lazar Parpetsi's Letter to Vahan, the main source for his own life (the coordinator's ruling, 2026-11-14); a translation of Timothy Aelurus's Armenian Refutation; Dioscorus of Alexandria's own letters; a readable Greek or an English text of Cyril of Scythopolis's Life of Euthymius (only Cotelier's 1681 Latin column is readable; the census cites Price's 1991 English); an English Victor of Vita better than the rough 1605 scan; the Chronicle of Seert's sections on Barsauma of Nisibis. Owner: the Library thread, to weigh for the wanted list.
    - Moses of Khoren's date: the scan tags it Contested, fifth century against eighth or ninth. No held work argues the later date; Langlois and the Mekhitarist preface take the fifth century, and Macler says almost nothing precise is known of him. The later date appears only in the Library's file header for the Italian edition and in the era 3 scan. The brief says the Library holds only one side; the Contested tag stays, as the coordinator ruled. Owner: the Library thread (Carrière, above).
    - Scan corrections. Years that rest on no held line: Timothy Aelurus "457-477" (Feltoe gives 457 and 460, Evetts's heading 458-480, and "d. 477" is a file header), Euthymius "377-473" (Cyril dates him by consulships and reigns), and Narsai "c.413". The census year 485 for Lazar is not a year of his life: it matches Neumann's end date for the History, "from 428 to 485" (preface to Elishe). Dioscorus's death in 454 is the editors' date (Feltoe; Nau for 4 September), where Evetts's heading gives 458. Barsauma's "fl. 457" sits against the 435 that Scher and Abbeloos–Lamy cite; it is now a contested claim. Both dates for Avarayr are modern: Ormanian's 26 May; Neumann's June 451 (preface) and 2 June (margin); and the 2 June of a note in Lazar's French; Lazar's text names only Pentecost. No held line says Vardan's speeches are Elishe's composition. Vakhtang I Gorgasali's 446-499 is Brosset's. Owner: the coordinator.
    - Scan rows that cite the wrong place: the Lazar lines for Vardan (the narrative is near l.38817-39137 and 40120-40490 of the Langlois volume, not 36587-36712); Langlois's translation of Elishe opens after his introduction (l.25692-26100), with chapter one at l.26255, where the scan gives "27333 on"; the scan does not cite the introduction, which is the source for Elishe's life; the Lazar row's "translator Ghesarian's introduction", which is signed "V. L.", Victor Langlois (l.35357). Barhadbeshabba is held twice, the History in Nau's PO 9 and the Cause of the Foundation of the Schools in Scher's PO 4; the scan cites him only through Connolly, and whether the two authors are one man Nau leaves open. Owner: the coordinator.
    - Rescored: Vakhtang I Gorgasali, WHO in the era 3 scan, is STORY (the coordinator, 2026-11-14, under Mark's era 3 ruling "Story unless own voice"); no words of his own are held. The audit is not edited. Owner: the coordinator.
243. **Library era 5: wanted sources not found, and two held for rights (2026-11-13).** The Library's era 5 batch vendored 71 files for the era 5 rows of the combined wanted list (Open-Gaps 220 and 222). Source: `Build/Ministry/Operations/Audits/2026-11-13_library-era5/Search_Log.md`; `Build/Ministry/Features/Source-Library/CFT-Wants.md`, era 5; Decision-Log, "Church Family Tree wants, era 5" (2026-11-13). The era 5 rows of `Wanted_Sources.md` now say HELD or NOT FOUND, with file and lines.
    - Not found in public-domain print, so the rows stay open: Walter Daniel's Life of Ailred (row 70); Teodosije's Life of Sava (row 92); a Life of Robert of Molesme (row 58); Clare's Latin Letters to Agnes, Testament and Process (row 61); Dominic's canonization process (row 62); Humbert's Legenda sancti Dominici (row 97); Waldo's Profession of 1180 as a separate text (row 65); the Old French and Latin Mirror of Simple Souls (row 75); Cyril III ibn Laqlaq's own record, the later Latin witness Renaudot being held (row 93); Nerses of Lambron's speech at Hromkla (council 18); the decree text of Lyon I (council 19; Matthew Paris's narrative is held). Owner: the Library thread.
    - Held for Mark, found but not vendored: Hadewijch's Dutch editions on dbnl.org, which gives no per-item licence (row 73), and Dawes's 1928 English Alexiad, a transcription whose notice limits it to non-commercial use (row 88). Owner: Mark, for the rights call.
    - Held, text not obtainable as text: the Latin Cronica of Salimbene (MGH SS 32) and the Latin Vita Norberti A (MGH SS 12) are page images on dmgh.de only. Owner: the Library thread, if a text host is found.
    - For the tree: the Mirror of Simple Souls is held as an anonymous work (the 1927 volume does not name Porete); Pakourianos's Typikon is held in the later Greek version its editor prints; the Speculum perfectionis, Joachim's Tractatus and Brother Leo's Scripta carry `needs-ruling` shelves for date or attribution. Owner: the coordinator.

244. **Era 3 Who batch 2: list lines, card traditions, Library items, and scan corrections (2026-11-14).** The ten batch 2 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch2/`; Decision-Log, "Who profiles, era 3 batch 2" (2026-11-14).
    - List lines: Joshua the Stylite and Zachariah Rhetor have no row in any era 3 census people or voices list. John Rufus, Brigid of Kildare, Caesaria of Arles and Julian appear only as named voices; the other four have a people row. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions taken from the scan that name a record the person appears in, not a party shown in his own words: Joshua the Stylite and Zachariah Rhetor "Syriac Orthodox (West Syriac) Christianity"; John Rufus "The Church of Alexandria and Miaphysite Egypt", though he worked in Palestine and at Antioch. Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted on the cards: any English of the Life of Caesarius of Arles, his Rules or his sermons, and the poems of Venantius Fortunatus that Krusch says hold up Caesaria as an example; an English Cogitosus; any English Ferrandus of Carthage; Severus of Antioch's works against Julian of Halicarnassus and the Philalethes in translation; a second early witness to Benedict of Nursia beside Gregory's Dialogues; a second witness to Julian's mission independent of John of Ephesus (Michael the Syrian and Bar Hebraeus retell John). Owner: the Library thread, to weigh for the wanted list.
    - Library headers that run ahead of the held lines: the Rule files give Benedict "c.480-c.547", where Gardner and Gasquet give 543 as the tradition; the PL 65 header gives the Life of Fulgentius to Ferrandus outright, where the held notes leave it contested; the Raabe header gives the Life of Peter the Iberian to John Rufus "traditionally", where Raabe says its author is unnamed; the Joshua header calls the attribution uncertain, where Wright does not doubt it. Owner: the Library thread, to correct the headers.
    - Scan corrections. Years that rest on no held line or on a header: Severus "c.459", Zachariah "c.465-after 536", Benedict "c.547", Ferrandus "d. c.546" (Victor of Tunnuna's entry under 546 says only that he was held in high regard), Julian "fl. c.543-c.545" and the census's 543 (John gives no year), and Brigid's 439, 518 and 521, which are Basnage's notice reprinted in Migne, not Migne's own note. The scan's "Stokes's index gives 800-835" for Cogitosus is in Stokes's Tripartite Life, not the Lismore file. Wrong leads: the Caesarius and Caesaria lines at Krusch l.34451-36150 are Krusch's introduction (the Life starts at l.36175), and PL 67 "Vita ~96068" is the Bollandist commentary; the Ferrandus "Epist. V on the Three Chapters" is Letter VI; Zachariah's Theodora passage for Severus is from Book IX of the chronicle, which Brooks gives to the later compiler. "Presided at Agde" is not shown by the held acts, which give only Caesarius's signature. The Joshua row's Dionysius of Tell-Mahre is Wright's attribution; Nau names the compiler Pseudo-Dionysius, writing in 775. Owner: the coordinator. The audits are not edited.
    - Rescored: Vahan Mamikonian and Kaleb of Aksum, WHO in the era 3 scan, are STORY (the coordinator, 2026-11-14, under Mark's era 3 ruling "Story unless own voice"); no words of their own are held. Ferrandus of Carthage and Benedict of Nursia took their places. The audit is not edited. Owner: the coordinator.

245. **Era 3 Who batch 3: list lines, card traditions, Library items, and scan corrections (2026-11-14).** The ten batch 3 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch3/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch3/`; Decision-Log, "Who profiles, era 3 batch 3" (2026-11-14).
    - List lines: Marcellinus Comes and Procopius of Caesarea have no row in any era 3 census people or voices list (the Marcellinus of the Luciferians entry is another man). Theodora and Samson of Dol appear only as named voices; the other six have a people row. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions are the scan's placings, except Cosmas Indicopleustes, whose card follows the census's Aksumite Christianity people row; J. W. McCrindle thinks he most probably belonged to the Church of the East. Settle with the placing. Owner: the map Who build slice.
    - A census year no held line carries: the Chalcedonian monasticism entry says Barsanuphius "was an Egyptian who had walled himself into a cell at the monastery of Seridos near Gaza around 520". Evagrius Scholasticus gives the Egyptian, the enclosed cell and Gaza (tr. Walford, Book IV ch. 33); no held line gives 520, and the batch 3 profile does not use it. Owner: the coordinator, for the census text.
    - Not held, and noted on the cards: the full Correspondence of Barsanuphius and John (only Dorotheus's questions are held, in Latin); Cyril of Scythopolis's whole Life of Sabas (Kugener prints its Severus passages only); the four books Cassiodorus says Marcellinus Comes wrote on Constantinople and Jerusalem; the Judicatum of Vigilius; Robert Fawtier's own argument on the date of the Life of Samson, which Taylor reports; a readable page of the Synaxaristes's year for Romanos, which the OCR garbles. Owner: the Library thread, to weigh for the wanted list.
    - Left in the source's form: Theodore the Studite's "Antony and Ephrem", beside whom he says Barsanuphius's image stood, are given no place in the source, so the profile does not add one. Owner: the coordinator, if a place is wanted.
    - Scan corrections. Years that rest on no held line or only on a Library file header: Theodora "c.497", Romanos "c.490-c.556" (the file header), Cyril "c.525-c.559" (the file header; Kugener gives about 523 and after 557), Samson "c.485-565" (Taylor infers a birth about 486), Barsanuphius and John "first half of 6th c.". Marcellinus's "fl. 518-548" should end at 534; Mommsen gives the years to 548 to another hand. Mar Aba's "540-552" is Chabot's reckoning; Abbeloos and Lamy give 538. Vigilius's "recants 554" rests on a letter dated 8 December, which Percival gives as 553. Wrong leads: Theodora's Zachariah lines are a footnote quoting Michael the Syrian (l.15923) and Book IX, which Brooks gives to the later compiler (l.13168); the Mar Aba "Seert 29321-29330" is another Aba, as the scan notes. Sources the scan missed: Kugener's extracts of the Life of Sabas, Braun's German Life of Mar Aba, Bar Hebraeus on Mar Aba's death, Nicephorus Callistus on Theodora's Cyprus, Liberatus's chapter 22 in PL 68, and the Synaxaristes life of Romanos. Dorotheus of Gaza falls after this batch: Migne heads Gallandi's notice "ANNO DOMINI DXCVI". Owner: the coordinator. The audits are not edited.

246. **Major councils, eras 1 and 2: people with no verdict, place ids, Library items, and scan corrections (2026-11-14).** The nine council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era1/` and `era2/`, written to `Council_Profile_Pattern.md`. None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217). Source: `Build/Ministry/Operations/Audits/2026-11-14_council-profiles-era1-2/`; Decision-Log, "Major councils, eras 1 and 2" (2026-11-14).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id: Eustathius of Antioch (Nicaea); Julius of Rome and Constans (Sardica); Acacius of Caesarea and Basil of Ancyra (Ariminum and Seleucia); Nectarius of Constantinople and Eleusius of Cyzicus (Constantinople 381); Flavius Marcellinus (Carthage 411); John of Antioch, Memnon of Ephesus, Theodosius II, Celestine of Rome and Candidian (Ephesus); Marcian, Anatolius of Constantinople, Paschasinus of Lilybaeum and Flavian of Constantinople (Chalcedon). Owner: the coordinator, for a Who scan verdict.
    - Place ids: no census row gives a place id for Arles, Serdica, Philippopolis, Ariminum, Seleucia, Ephesus or Chalcedon. The entries copy the nearest country row (France, Bulgaria, Italy, Turkey) and leave the place id out. Owner: the map build slice.
    - Not held, and noted in the entries or `records.json`: an English text of the Gesta of the Conference of Carthage (411) or of Augustine's Breviculus, so their content is told in paraphrase; an English text of the Eastern bishops' letter from Sardica (held in Latin, CSEL 65); an English Hilary, Against Constantius; Cyril of Alexandria's letter home from Ephesus, held only in Latin (Mansi tomus 4), so the opening scene is told without quotation marks; the acts of Dvin (506) in the Armenian Book of Letters; any account of Nicaea by Arius or his party; any text of the Pneumatomachians in their own words; the rescript rejecting the Donatist appeal of 411, which is not in the held Theodosian Code. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections for the major-councils table (`2026-11-12_major-events-scan/Councils_Scan.md`). Ephesus: the scan has the Church of the East refusing the council; the held witnesses disagree (Wigram: no corporate action at the time; Badger: cut off by its decree), so the entry marks it Affected, with a contested claim. Chalcedon: `the-church-of-the-east-under-persia` is added as Affected, since its own Synodicon carries Chalcedon's canons and Leo's Tome. Sardica: `roman-church-third-century` (census dates 200-268) is not used, being of the wrong era. Constantinople 381: Timothy of Alexandria is LISTED, as the supplement scan has him. Arles: the year 314, the opening on 1 August and the Milan hearing of 316 are Hefele's; no held ancient letter gives a year. Owner: the coordinator. The audit is not edited.
