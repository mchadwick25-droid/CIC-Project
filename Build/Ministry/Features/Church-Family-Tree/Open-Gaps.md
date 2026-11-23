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
   - 2026-11-21: Mark ruled no lawyer's read before the launch ("no lawyer, lets keep going"). Closed for launch.
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
    - 2026-11-14: carried unchanged. The eras 1-2 build (Decision-Log, "Eras 1 and 2 on the live tree") did not change the caps, the major mark or the placement of Who names. Mark's change of the same day removed the separate profile pill, so Who is the one control: one per river per era and one beside each tradition.

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
    - 2026-11-14: closed for the 20 era 1 profiles (batches 1 to 3): they are person entries in the census and on the site as text, with no audio player. Marcion is "Marcion of Pontus" throughout. Recording stays on hold (218). Data release 41.


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
    - 2026-11-14: list lines closed by data release 41. Every era 1 profile is a person entry in its tradition's Who (Hippolytus once, as Hippolytus of Rome; Bardaisan told within Bardaisan and the Bardaisanites; Tacitus and Suetonius in the Origin river). The name gaps (Paulinus, Germanus) are carried unchanged.
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
    - 2026-11-14: the placing is closed by data release 41. The Pliny the Younger edition wanted from the Library is carried.
236. **Era 2 Who batch 1: list lines, Library items, and the supplement rows (2026-11-13).** The nine batch 1 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch1/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch1/`; Decision-Log, "Who profiles, era 2 batch 1" (2026-11-13).
    - List lines in `cft-website/index.html`, reported by the round 1 review and not changed: Arius, Antony the Great, Frumentius and Hilarion of Gaza have no people-list line. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Aetius of Antioch's Syntagmation is held only in the Greek of PG 42 (Epiphanius, Panarion 76), whose vendoring header marks it unquotable until checked against the page image. The brief tells his argument in modern words and quotes none of it. Owner: the Library thread.
    - Not held, and noted on the cards: Antony's seven letters (the Library has only Jerome's notice of them) and the Greek Lives of Pachomius. The Pachomius and Antony profiles rest on Palladius, Sozomen, the Ethiopic Rules and Athanasius's Life. Owner: the Library thread, to weigh for the wanted list.
    - The supplement Who scan's twelve era 2 WHO rows (Ossius of Cordoba, Alexander of Alexandria, Eutyches, Moses the Black, Eusebius of Nicomedia, Liberius of Rome, Marcellus of Ancyra, Marius Mercator, Eznik of Kolb, Prosper of Aquitaine, Hilary of Arles, Germanus of Auxerre) are not in the era 2 scan sequence these batches follow. Owner: the coordinator.
    - 2026-11-14: list lines closed by data release 41 (all nine are person entries in a tradition's Who). Library items carried unchanged.
237. **Era 2 Who batch 2: list lines, name gaps, Library items, and a scan date (2026-11-13).** The nine batch 2 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch2/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch2/`; Decision-Log, "Who profiles, era 2 batch 2" (2026-11-13).
    - List lines: Damasus of Rome, Priscillian and Macrina the Younger have no row in any census people list; they are named only in voices lines and entry text. Auxentius of Durostorum is listed only under the era 3 movement "Gothic, Vandal & Lombard Homoian Christianity". Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Name gaps, left as the sources have them: Maximinus (given only as an Arian bishop), and Evodius in the Priscillian account (given by role). Ithacius is "of Sossuba" in Roberts's English and Halm's Latin of Sulpicius Severus, where the census has "Ossonoba"; the card uses the vendored form. Owner: the Library thread.
    - Not held, and noted on the cards: Cyril of Jerusalem's Letter to Constantius (known here through Gifford and Sozomen), Jerome's continuation of the Chronicle (used as Gifford quotes it), Augustine's Against the Letter of Parmenian, and a usable text of Basil's Against Eunomius (the PG 29 file is Greek with a garbled Latin column). Priscillian's own treatises are held only in a Schepss scan marked poor, so the brief tells them in modern words and quotes none. No held line gives the Donatist council that condemned Tyconius. Owner: the Library thread, to weigh for the wanted list.
    - Scan correction: the era 2 scan's Priscillian row says his following lasted "to Braga 563"; the held acts date that council era 599, which is 561. The scan's birth years for Cyril, Apollinaris, Macrina and Eunomius rest on no held line. The audit is not edited. Owner: the coordinator.
    - 2026-11-14: list lines closed by data release 41. Card traditions settled: Epiphanius of Salamis within Early Palestinian Ascetic Monasticism. Name gaps and Library items carried unchanged.
238. **Era 2 Who batch 3: list lines, tradition names, Library items and two ids (2026-11-13).** The nine batch 3 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch3/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch3/`; Decision-Log, "Who profiles, era 2 batch 3" (2026-11-13).
    - List lines in `cft-website/index.html`, reported by the round 1 review and not changed: none of the nine has a people-list line. Didymus the Blind and Evagrius Ponticus appear only as voice entries in their traditions' source lists. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card tradition names that are not site tradition names: Epiphanius of Salamis "Palestinian / Cyprus" and Olympias of Constantinople "Constantinople", taken from the era 2 scan. Settle with the placing. Owner: the map Who build slice.
    - Two ids differ from the scan's bare names. `fabiola-of-rome`: Jerome's Letter 126 has a second Fabiola, whom Fremantle's edition says "must be carefully distinguished". `olympias-of-constantinople`: no held source writes that form, but Palladius's Dialogue calls her "the deaconess of Constantinople" and says "There are several ladies of that name". Owner: the coordinator, if a different form is wanted before placing.
    - Not held: an English Panarion (the Library holds heresies 34 to 80 in Greek and Latin only), Panarion heresies 1 to 33, and the Ancoratus; Paulinus of Nola's Letter 29, which W. K. Lowther Clarke names with Palladius as the chief source on Melania the Elder; Didymus's commentaries and Jerome's Latin of his On the Holy Spirit; and a Latin text of Ammianus Marcellinus (only Yonge's 1862 English, from an uncorrected scan). The Mingarelli edition of Didymus's On the Trinity is held, but its Greek column did not survive the scan. Owner: the Library thread, to weigh for the wanted list.
    - Martin of Tours: Alexander Roberts's English of Sulpicius, Chronicle II.50, has the Priscillian trial put off "as long as Martin survived". Halm's Latin says while Martin was at Trier, and the brief follows the Latin. Owner: the Library thread, to note against the npnf211 file.
    - 2026-11-14: list lines closed by data release 41. Card traditions settled: Epiphanius within Early Palestinian Ascetic Monasticism; Olympias of Constantinople told within none, in the Greek East river. Library items and the two ids carried unchanged.
239. **Era 2 Who batch 4: list lines, Library items, and scan corrections (2026-11-13).** The nine batch 4 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch4/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch4/`; Decision-Log, "Who profiles, era 2 batch 4" (2026-11-13).
    - List lines: Palladius of Helenopolis and Philostorgius have no people-list line in the census. Honoratus of Arles is named only in the voices line of "Gallic Monastic-Ascetic Christianity", and Paulinus of Milan only in the voices line of the Ambrose of Milan entry. Rufinus has two lines that disagree: "Rufinus of Aquileia" under "Hieronymian Ascetic-Literary Christianity" and "Rufinus of Concordia" under "The Church of Aquileia". Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Traditions on the cards, to settle with the placing: Palladius "Desert Monasticism" (the other choice is "Antiochene Exegetical Christianity (Chrysostom-centered)"); Philostorgius "Anomoean (Eunomian) Christianity"; Paulinus "Ambrosian Milan (standalone)", the census name. Owner: the map Who build slice.
    - Not held, and noted on the cards: Prosper of Aquitaine's book against Cassian and the letters of Prosper and Hilary to Augustine; Paulinus of Nola's letters to Sulpicius Severus; an English Life of Honoratus (the held sermon is Latin in a rough scan, so the brief quotes none of it); an English Letter to Demetrias; the Indiculus of Possidius; Augustine's Letter 105 and Against Cresconius; Bidez's 1913 edition of Philostorgius; and Butler's Greek Lausiac History. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections: the Paulinus of Milan row's Marius Mercator claim (see the Decision-Log entry), and the scan's years for Rufinus, Sulpicius, Pelagius, Philostorgius and Honoratus, which rest on no held line. The audit is not edited. Owner: the coordinator.
    - 2026-11-14: list lines closed by data release 41 (Rufinus is one entry, told within The Church of Aquileia, and the voice row "Rufinus of Concordia" there became that link). Traditions settled as the card names them. Library items and scan corrections carried unchanged.
240. **Era 2 Who batch 5: list lines, card traditions, Library items, and scan corrections (2026-11-13).** The ten batch 5 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch5/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch5/`; Decision-Log, "Who profiles, era 2 batch 5" (2026-11-13).
    - List lines: Socrates of Constantinople is named only in the voices line of "Novatianism", and Sozomen is in no census list. Mesrop Mashtots is named only in the voices line of "Armenian Christianity (conversion era)", and Koriun only in a relation note. Alexander of Alexandria, Eusebius of Nicomedia and Ossius of Cordoba have no people-list line. Cyril of Alexandria, Leo of Rome and Theodoret of Cyrrhus each have one. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions that are not site tradition names, taken from the scans: Socrates "Constantinople" and Sozomen "Gaza / Constantinople". Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted on the cards: an English or Armenian Koriun (only Emine's French, in Langlois's edition), and any writing of Mesrop's own; Theodoret's Religious History, and the Chalcedon session where he anathematized Nestorius (held only as Blomfield Jackson quotes it); the letters of Acacius of Beroea and of Epiphanius, Cyril's archdeacon, behind the bribery charge; Sozomen's Greek before Book 5. Prosper's Chronicle is held only in Mommsen's Latin scan, so the Leo brief tells it in modern words. Owner: the Library thread, to weigh for the wanted list.
    - Scan and census corrections: no held line gives "about 405" for the Armenian alphabet, which the census also uses, or the scan's "about 362 to 440" for Mesrop (a note in Langlois gives 361 to 441). That Koriun wrote at Catholicos Joseph's request is Langlois's statement; Lazar of Pharp says King Vramshapuh asked, and the records tag it contested. Sozomen's "about 400 to 450" rests on no held line, and the held edition spells "Salaminius". Eusebius of Nicomedia's death "about 341 to 342" is a note in A. C. Zenos's edition of Socrates, and Constantine's baptism by him is Blomfield Jackson's note, not Theodoret's text. The audits are not edited. Owner: the coordinator.
    - 2026-11-14: list lines closed by data release 41. Card traditions settled: Socrates of Constantinople within Novatianism; Sozomen told within none, in the Greek East river. Library items and corrections carried unchanged.
241. **Era 2 Who batch 6: list lines, card traditions, Library items, and scan corrections (2026-11-13).** The nine batch 6 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch6/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch6/`; Decision-Log, "Who profiles, era 2 batch 6" (2026-11-13).
    - List lines: none of the nine has a row in any census people list. Prosper of Aquitaine is named in the entry text of "Gallic Monastic-Ascetic Christianity" (the "Massilians" label) and in two link notes. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions taken from the scans that name a record the person appears in, not a party he belonged to: Marcellus of Ancyra "Cappadocian Christianity" (the shelf of Epiphanius), Marius Mercator "Pelagianism" (he wrote against it), Prosper of Aquitaine "Gallic Monastic-Ascetic Christianity" (he wrote against its Marseilles teachers) and Eutyches "The Church of Alexandria and Miaphysite Egypt" (whose Syriac chronicle faults him). Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted on the cards: Prosper's book against Cassian, On the Ungrateful (one verse only, in a note) and any English Prosper; Marcellus of Ancyra's book against Asterius, Eusebius of Caesarea's books against him, and an English text of his letter (held only in the Greek of PG 42, a rough scan); Eutyches's letters in Greek; the full Life of Hilary of Arles (only Mansi's extract) and an English Hilary; the Refutation of Eznik of Kolb beyond part of book II in French; an English Life of Germanus (Levison's Latin only); an English Marius Mercator. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections: no held line gives the supplement scan's "c.405" for Moses the Black, "c.378-448" for Germanus of Auxerre (Levison reckons his years as bishop near 418 to 448, and calls them not certain), "352-366" for Liberius (editors' dates), or "c.401-449" for Hilary of Arles (a vendoring header; Richardson and Jackson disagree on his birth). Prosper's "Born 403 ... died 463" is Richardson's note. The Eznik row's "the date of his work is Contested" has no held sides: no held line dates the Refutation. The Moses row's "sit in thy cell" saying names only an Abba Moses of Scete. The audits are not edited. Owner: the coordinator.
    - Langlois's introduction to Eznik names the assembly "Aschdischad" (Ashtishat), where Elishe has Artashat and Lazar of Pharp no place. Owner: the Library thread, to note against the Langlois file.
    - 2026-11-14: list lines closed by data release 41. The four record-not-party cards (Marcellus, Marius Mercator, Prosper, Eutyches) stay as the profiles have them, told within the tradition whose record names them. Library items and corrections carried unchanged.

242. **Era 3 Who batch 1: list lines, a card tradition, Library items, and scan corrections (2026-11-14).** The ten batch 1 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch1/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch1/`; Decision-Log, "Who profiles, era 3 batch 1" (2026-11-14).
    - List lines: Vardan Mamikonian, Euthymius the Great and Moses of Khoren have no row in any era 3 census people list. The other seven have one. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card tradition taken from the scan that names a record the person appears in, not his own church: Victor of Vita "Gothic, Vandal & Lombard Homoian Christianity", the church that persecuted his. Settle with the placing. Owner: the map Who build slice.
    - Not held, and noted in the cards or `records.json` (the Chronicle of Seert is not noted in the batch): Carrière's study of the Abgar legend in Moses of Khoren (Paris 1895), which Harnack lists by title only, so no held line says what date it argues (on the want list by the coordinator's ruling, 2026-11-14); Lazar Parpetsi's Letter to Vahan, the main source for his own life (the coordinator's ruling, 2026-11-14); a translation of Timothy Aelurus's Armenian Refutation; Dioscorus of Alexandria's own letters; a readable Greek or an English text of Cyril of Scythopolis's Life of Euthymius (only Cotelier's 1681 Latin column is readable; the census cites Price's 1991 English); an English Victor of Vita better than the rough 1605 scan; the Chronicle of Seert's sections on Barsauma of Nisibis. Owner: the Library thread, to weigh for the wanted list.
    - Moses of Khoren's date: the scan tags it Contested, fifth century against eighth or ninth. No held work argues the later date; Langlois and the Mekhitarist preface take the fifth century, and Macler says almost nothing precise is known of him. The later date appears only in the Library's file header for the Italian edition and in the era 3 scan. The brief says the Library holds only one side; the Contested tag stays, as the coordinator ruled. Owner: the Library thread (Carrière, above).
    - Scan corrections. Years that rest on no held line: Timothy Aelurus "457-477" (Feltoe gives 457 and 460, Evetts's heading 458-480, and "d. 477" is a file header), Euthymius "377-473" (Cyril dates him by consulships and reigns), and Narsai "c.413". The census year 485 for Lazar is not a year of his life: it matches Neumann's end date for the History, "from 428 to 485" (preface to Elishe). Dioscorus's death in 454 is the editors' date (Feltoe; Nau for 4 September), where Evetts's heading gives 458. Barsauma's "fl. 457" sits against the 435 that Scher and Abbeloos–Lamy cite; it is now a contested claim. Both dates for Avarayr are modern: Ormanian's 26 May; Neumann's June 451 (preface) and 2 June (margin); and the 2 June of a note in Lazar's French; Lazar's text names only Pentecost. No held line says Vardan's speeches are Elishe's composition. Vakhtang I Gorgasali's 446-499 is Brosset's. Owner: the coordinator.
    - Scan rows that cite the wrong place: the Lazar lines for Vardan (the narrative is near l.38817-39137 and 40120-40490 of the Langlois volume, not 36587-36712); Langlois's translation of Elishe opens after his introduction (l.25692-26100), with chapter one at l.26255, where the scan gives "27333 on"; the scan does not cite the introduction, which is the source for Elishe's life; the Lazar row's "translator Ghesarian's introduction", which is signed "V. L.", Victor Langlois (l.35357). Barhadbeshabba is held twice, the History in Nau's PO 9 and the Cause of the Foundation of the Schools in Scher's PO 4; the scan cites him only through Connolly, and whether the two authors are one man Nau leaves open. Owner: the coordinator.
    - Rescored: Vakhtang I Gorgasali, WHO in the era 3 scan, is STORY (the coordinator, 2026-11-14, under Mark's era 3 ruling "Story unless own voice"); no words of his own are held. The audit is not edited. Owner: the coordinator.
    - 2026-11-14: list lines closed by data release 42 (all ten are person entries; the voice rows naming them became links). Card tradition settled: Victor of Vita is told within no tradition, in the Africa river, since the Homoian entry would set a Nicene bishop in the Non-Nicene river (Mark's approval of the preview, question 2). Library items and scan corrections carried unchanged.
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
    - 2026-11-14: list lines closed by data release 42. Card traditions settled as the cards name them: Joshua the Stylite and Zachariah Rhetor within Syriac Orthodox (West Syriac) Christianity, John Rufus within the Church of Alexandria and Miaphysite Egypt. Library items and scan corrections carried unchanged.

245. **Era 3 Who batch 3: list lines, card traditions, Library items, and scan corrections (2026-11-14).** The ten batch 3 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch3/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch3/`; Decision-Log, "Who profiles, era 3 batch 3" (2026-11-14).
    - List lines: Marcellinus Comes and Procopius of Caesarea have no row in any era 3 census people or voices list (the Marcellinus of the Luciferians entry is another man). Theodora and Samson of Dol appear only as named voices; the other six have a people row. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions are the scan's placings, except Cosmas Indicopleustes, whose card follows the census's Aksumite Christianity people row; J. W. McCrindle thinks he most probably belonged to the Church of the East. Settle with the placing. Owner: the map Who build slice.
    - A census year no held line carries: the Chalcedonian monasticism entry says Barsanuphius "was an Egyptian who had walled himself into a cell at the monastery of Seridos near Gaza around 520". Evagrius Scholasticus gives the Egyptian, the enclosed cell and Gaza (tr. Walford, Book IV ch. 33); no held line gives 520, and the batch 3 profile does not use it. Owner: the coordinator, for the census text.
    - Not held, and noted on the cards: the full Correspondence of Barsanuphius and John (only Dorotheus's questions are held, in Latin); Cyril of Scythopolis's whole Life of Sabas (Kugener prints its Severus passages only); the four books Cassiodorus says Marcellinus Comes wrote on Constantinople and Jerusalem; the Judicatum of Vigilius; Robert Fawtier's own argument on the date of the Life of Samson, which Taylor reports; a readable page of the Synaxaristes's year for Romanos, which the OCR garbles. Owner: the Library thread, to weigh for the wanted list.
    - Left in the source's form: Theodore the Studite's "Antony and Ephrem", beside whom he says Barsanuphius's image stood, are given no place in the source, so the profile does not add one. Owner: the coordinator, if a place is wanted.
    - Scan corrections. Years that rest on no held line or only on a Library file header: Theodora "c.497", Romanos "c.490-c.556" (the file header), Cyril "c.525-c.559" (the file header; Kugener gives about 523 and after 557), Samson "c.485-565" (Taylor infers a birth about 486), Barsanuphius and John "first half of 6th c.". Marcellinus's "fl. 518-548" should end at 534; Mommsen gives the years to 548 to another hand. Mar Aba's "540-552" is Chabot's reckoning; Abbeloos and Lamy give 538. Vigilius's "recants 554" rests on a letter dated 8 December, which Percival gives as 553. Wrong leads: Theodora's Zachariah lines are a footnote quoting Michael the Syrian (l.15923) and Book IX, which Brooks gives to the later compiler (l.13168); the Mar Aba "Seert 29321-29330" is another Aba, as the scan notes. Sources the scan missed: Kugener's extracts of the Life of Sabas, Braun's German Life of Mar Aba, Bar Hebraeus on Mar Aba's death, Nicephorus Callistus on Theodora's Cyprus, Liberatus's chapter 22 in PL 68, and the Synaxaristes life of Romanos. Dorotheus of Gaza falls after this batch: Migne heads Gallandi's notice "ANNO DOMINI DXCVI". Owner: the coordinator. The audits are not edited.
    - 2026-11-14: list lines closed by data release 42. Card traditions settled: Procopius of Caesarea told within no tradition, in the Greek East river; Samson of Dol within British and Welsh Christianity, since the census has no Breton movement; the others as their cards name them. Library items and scan corrections carried unchanged.

246. **Major councils, eras 1 and 2: people with no verdict, place ids, Library items, and scan corrections (2026-11-14).** The nine council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era1/` and `era2/`, written to `Council_Profile_Pattern.md`. None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217). Source: `Build/Ministry/Operations/Audits/2026-11-14_council-profiles-era1-2/`; Decision-Log, "Major councils, eras 1 and 2" (2026-11-14).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id: Eustathius of Antioch (Nicaea); Julius of Rome and Constans (Sardica); Acacius of Caesarea and Basil of Ancyra (Ariminum and Seleucia); Nectarius of Constantinople and Eleusius of Cyzicus (Constantinople 381); Flavius Marcellinus (Carthage 411); John of Antioch, Memnon of Ephesus, Theodosius II, Celestine of Rome and Candidian (Ephesus); Marcian, Anatolius of Constantinople, Paschasinus of Lilybaeum and Flavian of Constantinople (Chalcedon). Owner: the coordinator, for a Who scan verdict.
    - Place ids: no census row gives a place id for Arles, Serdica, Philippopolis, Ariminum, Seleucia, Ephesus or Chalcedon. The entries copy the nearest country row (France, Bulgaria, Italy, Turkey) and leave the place id out. Owner: the map build slice.
    - Not held, and noted in the entries or `records.json`: an English text of the Gesta of the Conference of Carthage (411) or of Augustine's Breviculus, so their content is told in paraphrase; an English text of the Eastern bishops' letter from Sardica (held in Latin, CSEL 65); an English Hilary, Against Constantius; Cyril of Alexandria's letter home from Ephesus, held only in Latin (Mansi tomus 4), so the opening scene is told without quotation marks; the acts of Dvin (506) in the Armenian Book of Letters; any account of Nicaea by Arius or his party; any text of the Pneumatomachians in their own words; the rescript rejecting the Donatist appeal of 411, which is not in the held Theodosian Code. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections for the major-councils table (`2026-11-12_major-events-scan/Councils_Scan.md`). Ephesus: the scan has the Church of the East refusing the council; the held witnesses disagree (Wigram: no corporate action at the time; Badger: cut off by its decree), so the entry marks it Affected, with a contested claim. Chalcedon: `the-church-of-the-east-under-persia` is added as Affected, since its own Synodicon carries Chalcedon's canons and Leo's Tome. Sardica: `roman-church-third-century` (census dates 200-268) is not used, being of the wrong era. Constantinople 381: Timothy of Alexandria is LISTED, as the supplement scan has him. Arles: the year 314, the opening on 1 August and the Milan hearing of 316 are Hefele's; no held ancient letter gives a year. Owner: the coordinator. The audit is not edited.
    - 2026-11-14: the nine councils are census entries and tree pages (data release 41). The 17 people with no Who scan verdict show as "Not yet assessed" with no id. Place ids are still missing for Arles, Ephesus and Chalcedon, so those entries carry no country row (see 249). Library items and scan corrections are carried unchanged.

247. **Era 3 Who batch 4: list lines, census text, Library items, and scan corrections (2026-11-14).** The ten batch 4 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch4/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch4/`; Decision-Log, "Who profiles, era 3 batch 4" (2026-11-14).
    - List lines: Cassiodorus and Agathias have no row in any era 3 census people or voices list. Jacob Baradaeus, Longinus and David of Wales appear only as named voices; Gildas, Theodosius I of Alexandria, Victor of Tunnuna, Radegund and John of Ephesus have a people row. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Census text no held line carries: the British and Welsh Christianity voices line says David "died around 589" and "became the patron saint of Wales"; no held file gives 589 (the annals give 601 and 588, Ussher 554, the Bollandists 544 or 550) or the patron-saint title. The same entry calls Gildas "the only substantial contemporary British voice from this period", which no held scholar says in those words; the batch 4 card does not use it. The Miaphysite Egypt voices line gives Theodosius "patriarch from 535", a year that rests on B. Evetts's heading and E. W. Brooks's notes. The Nubian Christianity voices line dates Longinus's Alodia mission "around 580", which is R. Payne Smith's reckoning of John of Ephesus's year 891, and the Julian line's "Nobadia" is in no held file (as batch 2 found). Owner: the coordinator, for the census text.
    - Not held, and noted on the cards: Garet's Vita of Cassiodorus (Patrologia Latina 69); Hugh Williams's general Introduction to Gildas, to which his notes refer for the dating argument; Theodosius of Alexandria's treatise against the Tritheites and his letter to the Alexandrians (Patrologia Graeca 86); Giraldus Cambrensis's Life of David; the epigrams of Agathias, including the one to the archangel on which Niebuhr rests his faith; any English translation of Agathias, of Victor of Tunnuna or of the Lives of Radegund. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections. Years that rest on no held line or only on a Library file header: Gildas "c.500-c.570" (Williams's estimate and the annals' 570), Jacob Baradaeus "c.500" (no held birth year; 578 is Brooks's conversion of Michael's 889), Agathias "c.532-c.580" (the file header; Niebuhr gives 536 or 537, and before 582), Cassiodorus "c.485-c.580" (the file headers; Hodgkin gives about 480 and 575), Radegund "c.520" (no held line; 587 is the editors' reckoning), John of Ephesus "588" (the file headers; Brooks gives probably 586), David of Wales "c.500-c.589" (no held line), Longinus "c.585" (no held line). The scan's "no work of his own is held" for Theodosius I is wrong: two letters are held in English in the Syriac chronicle under Zachariah's name, with sermon quotations in Cosmas and a fragment of his Tome in the Lateran acts. Agathias's "Vita" is B. G. Niebuhr's of 1828, not an ancient Life. The three "Radegund" poems are Fortunatus's by every held edition. Victor of Tunnuna's Balearic Islands are Mommsen's correction of the manuscripts. Wrong leads: Victor's four cited entries are about Reparatus (his own exile is at l.19194-19354); Theodosius's Zachariah lines (13160-13172) are the chapter on Severus, and his John of Ephesus lines are Payne Smith's footnote; Jacob's "Jacobites" lead is not in Lives ch. 50; the Longinus "officiated for Theodosius" line is Payne Smith's own bridge, and his letter is at l.15720-15838; David's Wasserschleben "~532" is the table of contents; Radegund's letter is at Dalton l.19821, not the chapter list at l.17533. Sources the scan missed: Cassiodorus's own Chronica (Mommsen), the Bollandists' commentary on David (Acta Sanctorum, March I), Michael the Syrian on John of Ephesus's last prison, Gregory of Tours's Glory of the Confessors on Radegund's funeral. Owner: the coordinator. The audits are not edited.
    - 2026-11-14: list lines closed by data release 42 (Agathias told within no tradition, in the Greek East river). Census text: the David and Gildas voices lines of British and Welsh Christianity are rewritten on held lines (David's death "in 588 or 601", no patron-saint title; Gildas's book "written in the 540s"), the Julian line of Nubian Christianity no longer gives 543 or "Nobadia", and the Benedict line of Early Benedictine / Italian Monasticism now gives 543, by his order's tradition. Theodosius's "patriarch from 535" (Evetts's heading, Brooks's notes) and Longinus's "around 580" (Payne Smith's reckoning) rest on held lines and stand. Library items and scan corrections carried unchanged. Source: Decision-Log, "Era 3 on the live tree" (2026-11-14).

248. **Era 3 Who batch 5: list lines, a card tradition, census text, Library items, and scan corrections (2026-11-14).** The ten batch 5 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch5/`; Decision-Log, "Who profiles, era 3 batch 5" (2026-11-14).
    - List lines: Evagrius Scholasticus and Baudonivia have no row in any census people or voices list; both are named only in entry text (Evagrius in the Chalcedonian monasticism and Miaphysite Egypt entries; the Evagrius of the desert monasticism rows is Evagrius Ponticus). Henana of Adiabene appears only as a named voice. The other seven have a people row. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card tradition: the scan places Evagrius Scholasticus in the Syriac Orthodox church. He writes for the side that held to Chalcedon, as adviser to Gregory, patriarch of Antioch, so his card reads "The Byzantine Imperial Church (Justinianic)", by the coordinator's call of 2026-11-14. The other cards are the scan's placings in the census's names. Settle with the placing. Owner: the map Who build slice.
    - Census text: the three Reccared people rows quote his short subscription at the Third Council of Toledo (collectio canonum 1808, l.36771), and two of them call it his profession of faith; the longer tomus is at l.36631-36744. The rows give 589, 586 and 586 for the same line. The Leander rows give 579; the line one of them cites, from his Rule for his sister Florentina, carries no year. Owner: the coordinator, for the census text.
    - Not held, and noted on the cards or records: William Reeves's annotated Adomnán and the Irish annals Huyshe cites (the Annales Cambriae are held, and their editor John Williams ab Ithel sets their years for Columba at 521, 562 and 595); the Life of Dositheus, and any English of Dorotheus of Gaza; any English of Venantius Fortunatus's hymns; O. M. Dalton's first volume, the Introduction his notes cite; Odo of Cluny's Life of Gregory of Tours; Henana's treatises on the Rogations and Golden Friday, which Addai Scher reports surviving and Patrologia Orientalis 7 prints; an English text of the acts of the Third Council of Toledo beyond Percival's excerpt; Boniface's letters to Nothelm, known only through the Register editors' quotation. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections. Years that rest on no held line or only on an editor's reckoning: Evagrius "c.536-c.594" (E. Walford's birth reckoning; no held line gives a death year); Gregory of Tours "538-594" (Arndt; Krusch gives 593); Columba "c.521-597" (Huyshe; Williams ab Ithel sets the Annales Cambriae at 521 and 595; Bede gives 565 for the voyage); Leander "c.534-600" (no birth line; the death is given as 595, 599, 600, 601 and 603 by different editors); Venantius Fortunatus "c.530-c.600" (W. D. Foulke's note and M. A. Luchi); Reccared "c.559-601" (no birth line; 586 and 601 are Isidore's eras 624 and 639); Henana "c.572-c.604" (572 is Scher's reckoning; no death year is held); Augustine of Canterbury "d.604/605" (his epitaph gives 26 May with no year); Baudonivia "fl. c.600-610" (Krusch's reasoning puts her book soon after 600). Wrong or loose leads: the Leander Notitia in PL 72 is William Cave's, which Migne reprints; the 800 pupils of Henana are in Mari ibn Sulayman, though Assemani credits Amr; the synods of 585, 596 and 605 never name Henana, and Chabot, Braun and Labourt infer it; Dorotheus of Gaza's "mid-6th c." stands against Migne's heading "ANNO DOMINI DXCVI" on Andrea Gallandi's notice. Owner: the coordinator. The audits are not edited.
    - 2026-11-14: list lines closed by data release 42. Card tradition settled: Evagrius Scholasticus within the Byzantine Imperial Church (Justinianic). The Reccared rows of the census text item are carried in 255. Library items and scan corrections carried unchanged.

249. **Eras 1 and 2 on the live tree: carried items (2026-11-14).** The 75 Who profiles and 9 major councils are in the census and on the site as text (data release 41). Source: Decision-Log, "Eras 1 and 2 on the live tree" (2026-11-14).
    - Recording: none of the 84 entries has audio. They join the held recordings of Open-Gaps 218 and wait for an approved, capped run. Owner: the coordinator.
    - Place ids: the census has no row to copy ids from for Arles, Ephesus, Chalcedon, Jerusalem, Gaza, Cyprus, Ancyra, Cordoba, Auxerre and many towns of these profiles, so those entries name the place with no "today in" country. No id is invented. Owner: the map build slice, with the Library thread.
    - Map position of people: `start` and `end` are the years the card names; where it names none, the year comes from the Who scan or the census record: Marcion 150 (the card's "middle of the second century"), Valentinus 140 (the census voice year), Ignatius 107 (Eusebius's Chronicle, in the brief), Polycrates 196 (the editor's reading), Anatolius 270 to 280 (the translator's conjectural dates), Frumentius 330 to 360, Koriun 431 (the card's one anchor, the canons of Ephesus), Eznik 451, Moses the Black 405 (the scan's suggestion), Didymus 350 and Tyconius 380 (census voice years). The card's own dates line says what the sources give. Owner: the coordinator, if a different year is wanted.
    - Dioscorus of Alexandria is a Who with no entry yet; the Chalcedon council lists him as "Profile to come". Owner: the coordinator, for a profile.
    - Council people: 17 people have no Who scan verdict ("Not yet assessed"); see 246. Owner: the coordinator.
    - Open-Gaps 217 (caps of 4 and 5, the major mark in the data, the "more" click, placement to the right of the river, the fade) is carried unbuilt. The batch major marks are in the Decision-Log, not the data. Owner: the map build slice.
    - The `audio/*.audio.txt` copies in the profile folders keep the earlier spellings (the spelling fix changed the briefs and cards, not the audio copies); the recording run builds from the census text. Owner: the coordinator.
    - `tools/check_tree_domains.mjs` reports 404 for the new tree pages until the site is deployed; check it again after the deploy. Owner: the coordinator.
    - 2026-11-14: Dioscorus of Alexandria closed by data release 42: he is a person entry, and the Chalcedon council's Who links to him. The other items are carried unchanged.

250. **Major councils, era 3: people with no verdict, place ids, Library items, and scan corrections (2026-11-14).** The three era 3 council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era3/`, written to `Council_Profile_Pattern.md`. None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217). Source: `Build/Ministry/Operations/Audits/2026-11-14_council-profiles-era3/`; Decision-Log, "Major councils, era 3" (2026-11-14).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id: Eutychius of Constantinople, Ibas of Edessa and Pelagius I of Rome (Constantinople 553); Masona of Mérida, Euphemius of Toledo, Eutropius, abbot of Servitanum, Queen Baddo and King Leovigild (Toledo 589); Abraham of Aghbatank, Movses II of Eghivart and Vertanes (Dvin). Primasius of Hadrumetum is WHO in the supplement scan but has no profile yet, so he shows with no id. Owner: the coordinator, for a Who scan verdict.
    - Place ids: no census row gives a place id for Toledo or Dvin. The entries copy the country rows for Spain and Armenia and leave the place id out. Owner: the map build slice.
    - Not held, and noted in the entries or `records.json`: the full acts of 553 (Mansi, tomus 9), so the profile rests on the English extracts in NPNF 14; an English text of the Toledo III acts; any Homoian text from Visigothic Spain; the acts of the council of Dvin and the letters of Abraham and Kyrion (the Armenian Book of Letters); Ukhtanes's History of the Schism of the Georgians and Kirakos, which Brosset cites for the council; the Judicatum of 548. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections. Councils scan, era 3: Constantinople 553 does not use `aquileian-christianity` (census c. 340-410), being of the wrong era; it adds `the-church-of-the-east-under-persia` (Affected, through Jérôme Labourt's reading of the synod of 585) and `syriac-orthodox-west-syriac-christianity` (Affected, through Michael the Syrian), and gives the Antiochene row (census c. 350-430) as Condemned, following the existing census edge. Dvin: the year is told as between 596 and 609 (Brosset 596, Ormanian 609; Stephen of Taron and Issaverdens set it under Maurice); the id keeps 609. Who scan era 3: Stephen of Taron is marked WANTED and not held, but his history is held in German (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt`). Census, `georgian-christianity` story "Kyrion Answers the Armenians": several of its claims rest on no held line (Movses of Tsurtavi, "from Jerusalem", Kyrion turning to Rome), and the editors of Gregory's Register do not name Kyrion as the Quiricus of XI.52. Owner: the coordinator. The audit is not edited.
    - 2026-11-14: the three councils are on the site by data release 42. Primasius of Hadrumetum now links to his entry from the Constantinople 553 Who. Toledo and Dvin show no "today in" country, since no census row gives their place ids (as Chalcedon in release 41). The people with no verdict, Library items and scan corrections are carried unchanged.

251. **Era 3 Who batch 6: list lines, a card tradition, census text, Library items, a batch 5 correction, and scan corrections (2026-11-14).** The ten batch 6 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch6/`; Decision-Log, "Who profiles, era 3 batch 6" (2026-11-14).
    - List lines: Columbanus, John Moschus and Isidore of Seville have a people row. Babai the Great appears only as a named voice and in entry text. John of Biclaro is named only in entry text (Nicene Visigothic Iberia; Nubian Christianity, as "John of Biclarum") and in the note of the edge from Nubian Christianity to Makurian Nubian Christianity. Faustus of Riez is named in the text of the Gallic monastic entry ("Faustus, later became bishop of Riez") and in the note on the link from it to Merovingian Gallic Christianity; the Faustus people row is Faustus of Milevis. Gennadius of Marseilles has no people row; entry text, link notes and era 2 person entries cite him as the writer of the Lives of Illustrious Men. Constantius of Lyon has no people row, but the Germanus of Auxerre entry and the Hilary of Arles card name him as the writer of the Life of Germanus. Severinus of Noricum and Ruricius of Limoges are named nowhere in the census. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card tradition: the supplement scan places Severinus of Noricum in "Early Benedictine / Italian Monasticism" and in "Gothic, Vandal & Lombard Homoian Christianity". He was Catholic, and the second placing comes only from the Rugians he lived among, by George W. Robinson's reading of Eugippius. His card reads "Early Benedictine / Italian Monasticism", by the coordinator's call of 2026-11-14. Constantius of Lyon keeps the scan's "British and Welsh Christianity", which matches the Germanus of Auxerre card, though he was a man of Lyon; Ruricius of Limoges's corpus-map row is still marked as needing a ruling on which Gallic entry holds him, and his card reads "Merovingian Gallic Christianity". Settle with the placing. Owner: the map Who build slice.
    - Census text: the Nubian Christianity entry says John of Biclarum records a rival, Chalcedonian conversion of Makuria. John writes only of the "Maccurritae", and Theodor Mommsen, his editor, suggests the Makkourai of Mauretania that Ptolemy names (mommsen1894, apparatus at the year 569); the Library file header reads them as Makuria. The edge `nubian-christianity--makurian-nubian-christianity` reads him the same way ("John of Biclarum says the Makurians took up the Christian faith in the third year of Justin II, about 569"), with confidence Widely Accepted. The Nicene Visigothic Iberia entry has Isidore of Seville preside at the Fourth Council of Toledo (voices[2]; documentedStories[1], teaser and text). The acts give him only the first signature (Hispana l.40882-40884); Ernest Brehaut says he probably presided, and Francisco Antonio Lorenzana's 1775 preface to the Breviarium Gothicum says he did (PL 86 l.474). The card and records keep it contested. The note on the link from Gallic Monastic-Ascetic to Merovingian Gallic Christianity calls Faustus "the first abbot of Lérins". It reads Richardson's "first abbot of the monastery at Lerins, and then made bishop" (npnf203 l.43684-43685) as an order of abbots. Honoratus was the first abbot ("Honoratus primus abbas Lirinensis", Engelbrecht's index, engelbrecht1891 l.28706), as the Gallic monastic entry itself says. Owner: the coordinator, for the census text.
    - Library: `cic/texts/constantius-lyon_vita-germani_levison1920.txt` is cut short. It ends mid-sentence at l.4580 ("Et ideo in scribendo succinctum"), without the rest of the epilogue, the EXPLICIT and the p.283 apparatus its header promises. No profile claim rests on the missing text. Re-extract from archive.org `passionesvitaequesanctorum5`. Owner: the Library thread.
    - Not held, and noted on the cards or records: an edition of Sidonius Apollinaris (his letter IX.9 is held only in Barralis's 1613 print, and his letters to Constantius of Lyon and Ruricius of Limoges only through Levison and Engelbrecht); Photius's notice of the Spiritual Meadow (Bibliotheca, codex 199) and any English of the Meadow; Thomas Hodgkin's work, which W. D. Foulke cites for Columbanus's years; Columbanus's book against the Arians; Redemptus's account of Isidore's death, known through Poschmann, Mommsen and Brehaut; Braulio's Praenotatio in Latin; John of Biclaro's rule; a Syriac or English text of Babai the Great's own books (the Book of the Union is held as passages in J. Labourt's French, the Life of George in Oskar Braun's German, which shortens the introduction and leaves out or sums up several passages (braun1915 l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947, 14995-14996)); the Lives of Isidore by Lucas Tudensis and Rodericus Cerratensis; Gennadius of Marseilles's works against the heresies and his letter to Gelasius; any English of Faustus of Riez, Ruricius of Limoges or Constantius of Lyon. Owner: the Library thread, to weigh for the wanted list.
    - Correction to batch 5: the Henana of Adiabene records said Babai the Great's De Unione was "not held". It is held in part, as Labourt quotes it in French (labourt1904 l.15764-15866). His Life of George of Izla is held in Braun's abridged German and in three French passages Chabot gives, two of them on Henana's doctrines. Only that absent_details note was changed, by the coordinator's call of 2026-11-14; the brief and card of batch 5 are unchanged, and the point that the charges rest on Babai alone still holds.
    - Scan corrections. Benjamin I of Alexandria (era 3 scan, "patriarch 622-661") falls in era 4 by the date-of-work rule and is left to the era 4 sequence; Ruricius of Limoges took his place, and Theopistus goes to the end of the era 3 list for a check on whether he can be written. Years that rest on no held line or only on an editor's note or file header: Columbanus "c.543-615" (Foulke, citing Hodgkin); John Moschus "c.550-619" (the file header; 620 is Papebroch's year for the return of his body, and Fabricius's from Bolland for his death); John of Biclaro "c.540-after 621" (the header, and Mariana's "post annum 621" as Gallandi reports it); Babai the Great "fl. c.569-628" (Budge's note; 552/3 is Addai Scher's birth reckoning, and no source has him abbot before 603/4); Isidore of Seville "c.560-636" (the header for the birth; the PL 80 chronicle under Maximus of Zaragoza's name gives 556, which Nicolás Antonio treats as Higuera's forgery); Severinus of Noricum "about 482" (Robinson's chronological table; Eugippius gives only 8 January); Faustus of Riez "c.405/410-c.490/495" (the header; Engelbrecht says only "not long before 410" and calls the death year uncertain); Gennadius of Marseilles "died 496" (notes by E. C. Richardson and Blomfield Jackson); Constantius of Lyon "fl. c.480" (Levison's date); Ruricius of Limoges "c.440 to c.507" (the header; 485 for his bishopric is Engelbrecht's reckoning). Wrong or loose leads: Columbanus's "Rules and other letters not held" is wrong, since PL 80 holds his Rule, Penitential, sermons, six letters and poems; Fredegar IV.36 copies Jonas and is not an independent witness; Babai's Thomas of Marga Book III lead is Rabban Babai of Gebilta, a different man, and "own books not held" is wrong; John Moschus's life rests mainly on the old notice Daniel Papebroch prints, with the Notitia from Fabricius in Harles's edition; Seville II's "619" converts the acts' era 657, and Pagi's held note in Mansi 10 argues for 618; Toledo IV gives Isidore the first signature but does not say he presided; John of Biclaro signs as John of Gerona at Barcelona II and under King Gundemar's decree, signatures Mommsen identifies as his; Faustus's "the semi-Pelagian reply" is told as fact, where August Engelbrecht, his editor, denies he was a semi-Pelagian; Gennadius's "I Gennadius" notice is the scan's own-life lead, where Richardson thinks a later hand added it; Constantius's "the only near-contemporary Life" is an unchecked "only"; the Ruricius who signs councils in 535 and 541 is his grandson, by Leo's index to Fortunatus. Owner: the coordinator. The audits are not edited.
    - 2026-11-14: list lines closed by data release 42. Card traditions settled: Severinus of Noricum within Early Benedictine / Italian Monasticism; Constantius of Lyon within British and Welsh Christianity; Ruricius of Limoges within Merovingian Gallic Christianity; Faustus of Riez within Gallic Monastic-Ascetic Christianity. Census text closed: the Nubian Christianity entry and its link to Makurian Nubian Christianity now say the Maccurritae may not be the Makurians, as Mommsen thought them a people of Mauretania; Isidore's name stands first among the Toledo IV signatures, with no "presided"; Faustus "was abbot of Lérins before he became bishop of Riez". Library items and scan corrections carried unchanged. Source: Decision-Log, "Era 3 on the live tree" (2026-11-14).
252. **Era 3 Who batch 7: list lines, two card traditions, Library items, and scan corrections (2026-11-14).** The eight batch 7 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch7/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch7/`; Decision-Log, "Who profiles, era 3 batch 7" (2026-11-14).
    - List lines: none of the eight has a census people or voices row. Boethius is named only in the text of the Gothic, Vandal & Lombard Homoian Christianity entry (his execution) and Primasius only in the Tyconius card's legacy (F. C. Burkitt). The Philoxenus in the census is the Roman presbyter of Julius of Rome, a different man. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions, to settle with the placing: Boethius reads "The Byzantine Imperial Church (Justinianic)", the supplement scan's first placing, though he died in 524, before Justinian's reign; the scan's other placing is Early Benedictine / Italian Monasticism, and the only census line that names him is in the Homoian entry. Fulgentius of Ruspe reads "Gothic, Vandal & Lombard Homoian Christianity", the movement of the Vandal kingdom he lived under, as the Victor of Vita card does; the census has no movement for the Catholic church of Vandal Africa, and Latin African Christianity under Byzantium begins in 533. Owner: the coordinator, with the map Who build slice.
    - Library: the content note of `cic/texts/fulgentius-ruspe_opera-contra-arianos-pl65-lat_migne1847.txt` says no public-domain English exists, but an English abridgement of the Life of Fulgentius from 1605 is held in `cic/texts/victor-of-vita_memorable-and-tragical-history-persecution-eng_1605.txt` (from l.8053); no English of his own works is held. Several file headers give years no held line supports, listed below. Owner: the Library thread.
    - Not held, and noted on the cards or records: Ennodius (his Paraenesis and Life of Epiphanius, which Thomas Hodgkin and Rudolf Peiper use); the Latin Variae of Cassiodorus in full and an English Anonymus Valesianus; Assemani's Bibliotheca Orientalis II, through which alone the anonymous Life of Philoxenus is known, and Vaschalde's letters of Philoxenus; the Life of John bar Aphthonia (British Museum Add. 12,174) and his record of the Constantinople debates; Kugener's introduction to the second Life of Severus; Mansi IX, through which alone Heinrich Kihn reports Primasius's refusal to attend the council of 553 and the synod of 541; the Annals of Ulster, Tigernach, Inisfallen and the Four Masters vol. I, and Plummer's Vitae Sanctorum Hiberniae, for Ciaran; the Bollandists' January volume for Fulgentius; any English of the letters and poems of Avitus or of the works of Fulgentius and Primasius. Owner: the Library thread, to weigh for the wanted list.
    - Scan corrections. Years that rest on no held line or only on a file header: Avitus of Vienne "c.450-518" (the header; Peiper puts his birth about 460 and his index dates his death after 525 or 526 and before 533, a lower bound his preface doubts); Philoxenus of Mabbug "c.440-523" (the header and François Nau; Budge says born in the third quarter of the fifth century); Fulgentius of Ruspe "suggested c.462-527" (the header; Baronius gives 529 and Chifflet 533, as Andrea Gallandi reports; the Life gives the day only); Eugippius "c.460-c.535" (the header only); John of Beth Aphthonia "d. 538" (the header, which merges the writer of the Life with the archimandrite John bar Aphthonia; only the archimandrite's death is dated, to the year 849 of the Greeks by a chronicle extract Kugener prints, and to 850 by Elias of Nisibis); Ciaran of Clonmacnois "not in a held line" (the Annales Cambriae give it, set at 544 by John Williams ab Ithel; John O'Donovan gives 549); Primasius "death not in a held line" (holds; Victor of Tunnuna tells his death inside his entry for 552, after Primasius signed in May 553). Owner: the coordinator. The audits are not edited.
    - Batch 8, the last seven supplement era 3 WHO rows: Dionysius Exiguus, Liberatus of Carthage, Brendan of Clonfert, Martin of Braga, Marius of Avenches, Barhadbeshabba 'Arbaya and John Climacus, with Theopistus set aside for a separate check. Owner: the coordinator.
    - 2026-11-14: list lines closed by data release 42. Card traditions settled: Boethius told within no tradition, in the Latin West river (he died in 524, before Justinian's reign, and no census tradition is the Catholic church of Ostrogothic Italy); Fulgentius of Ruspe told within no tradition, in the Africa river, with Victor of Vita (Mark's approval of the preview, question 2). Library items and scan corrections carried unchanged. Source: Decision-Log, "Era 3 on the live tree" (2026-11-14).

253. **Era 3 Who batch 8: list lines, card traditions, census text, Library items, a batch 1 records note, and scan corrections (2026-11-14).** The eight batch 8 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch8/`. None is in the census or on the site. With them, every era 3 Who row of both scans is written or moved. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch8/`; Decision-Log, "Who profiles, era 3 batch 8" (2026-11-14).
    - List lines: none of the eight has a people row. John Climacus is named in the relations summary of Chalcedonian Monasticism - Judean Desert & Gaza. Liberatus of Carthage is named in the Latin Africa caveat and sources, the Socrates of Constantinople card and the Flavian/Eutyches caveat. The census names both the author of the Cause of the Foundation of the Schools and the author of the Ecclesiastical History "Barhadbeshabba", in edge notes, sources and entry text, without telling them apart; the profile and batch 1's Narsai and Barsauma cards keep them apart, with Nau's view that they may be one man given as his. Dionysius Exiguus, Martin of Braga, Brendan of Clonfert, Marius of Avenches and Theopistus are named nowhere in the census. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions (the worker's calls, accepted by the coordinator on 2026-11-14): Dionysius Exiguus in "Early Benedictine / Italian Monasticism", for the scan's "The Byzantine Imperial Church (Justinianic)" and "Latin canon law"; Liberatus of Carthage in "Latin African Christianity under Byzantium" only; Martin of Braga in "Nicene Visigothic Iberia", since the census has no Suevic movement; Brendan of Clonfert in "Insular / Irish Monastic Christianity" only, dropping the scan's Medieval Welsh placing. Settle with the placing. Owner: the map Who build slice.
    - Census text: the Chalcedonian Monasticism - Judean Desert & Gaza entry says Orthodox monks still read the Ladder aloud every Lent; no held line says so. It also says the Ladder was written "just after this period", which rests only on the Library file header's years for John Climacus (c.579-649); the held witnesses place him in the later 500s or about 600 and dispute the years. The Latin Africa entry cites Liberatus's Breviarium, chapter 24, as "a second African account of Reparatus' deposition"; the Breviarium never names Reparatus, and chapter 24 speaks only of bishops rewarded, deposed, exiled or in hiding (PL 68 l.82406-82413); Reparatus is named in Jean Garnier's notes. The Church of the East under Persia entry, documentedStories[1], cites the Cause of the Foundation of the Schools for a sequence that ends in the students' walk-out from Nisibis; the Cause praises Henana as a living master and does not tell the walk-out, which comes from the Chronicle of Seert. Owner: the coordinator.
    - Batch 1 records: the Dioscorus of Alexandria `records.json` calls Theopistus's History "the only held account of the exile". The Arabic synaxary (Basset) and the Ethiopic synaxary (Budge) also tell of the exile. Batch 1 is not edited; the fix goes into the era 3 map build with Open-Gaps 249, by the coordinator's call of 2026-11-14. Owner: the map Who build slice.
    - Library: the header of `cic/texts/po09_barhadbeshabba-ecclesiastical-history-part2-and-others-fra_1913.txt` names the History's author "Barhadbeshabba 'Arbaya, bishop of Halwan", merging the two writers; Nau gives the History to a priest of the school and leaves the identity open (l.31556-31604). The PG 88 Greek of John Climacus and Daniel of Raithu is garbled OCR, so only the Latin columns are usable. Not held, and noted on the cards or records: the Irish annals for Brendan of Clonfert (Ulster, Tigernach, Chronicum Scotorum, the early Four Masters volumes), Adomnan's Latin, and the Navigatio Sancti Brendani; Bede's On the Reckoning of Time and Chronicle as texts (quoted only in the PL 67 testimonia); any English of Liberatus's Breviarium or of Martin of Braga's works; Martin's letters; Conon of Lausanne's Gesta and the Lausanne cartulary; the first part of Barhadbeshabba 'Arbaia's History, Mingana's Syriac of the Cause, and the other books Abdisho lists; the Syriac of the History of Dioscorus, Amélineau's Coptic panegyric of Macarius of Tkow, Crum's fragments and Assemani's Vatican catalogue; Le Maistre's French Life of John Climacus. Owner: the Library thread, to weigh against the wants register.
    - Names no held source gives: the see of Bishop Petronius, to whom Dionysius Exiguus wrote on Easter, and the see of Agricola, the bishop the monks of Agaune rose against in Marius of Avenches's Chronicle. Both are named on the cards without a see. Owner: the Library thread.
    - Scan corrections (supplement scan). Theopistus: "nothing about the man himself is held" is wrong; the History of Dioscorus is told in his own voice and calls him the deacon of Dioscorus, and "which Peter the Iberian reused" should read that Nau gives the reworking to a writer of Peter the Iberian's school after 512; the 454 is Nau's year, and the PO 13 note the row could be read with is Nau's own, not the Chronicle of Seert's. Barhadbeshabba: "life known only from the subscription" is a false absence (Scher's introduction, the Chronicle of Seert, Guidi's chronicle and Labourt are held); the 605 is J.-B. Chabot's year, and the signature carries no epithet. John Climacus: the "569" at PG 88 l.41415 is an OCR reading in Philippe Labbe's notice, whose own view is a conditional 560 to 565; "Daniel's Life held in epitome" should read held whole (PG 88 l.42036-42850, and in the Acta Sanctorum); the header's 579 to 649 rests on no held line. Dionysius Exiguus: the life note is William Cave's, reprinted by Migne, and 532 is Bede's year in the PL 67 testimonia. Marius of Avenches: "c.530-594" is Mommsen's reckoning; his Mâcon signature is held in Maassen. Martin of Braga: "c.515-579" is the file header's; Caspari, Krusch, Dalton and the Bollandists give 580 for his death. Liberatus: "not in a held line" is too strong; Pope Agapetus's letter of 535, by Otto Günther's date, names him. Owner: the coordinator. The audits are not edited.

254. **Era 4 Who batch 1: list lines, card traditions, census text, Library items, and scan corrections (2026-11-14).** The eight batch 1 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch1/`. None is in the census or on the site; Bede's live person entry is unchanged. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch1/`; Decision-Log, "Who profiles, era 4 batch 1" (2026-11-14).
    - List lines: Boniface ("Boniface", 716), Leoba (732), Adomnán (679), Alcuin of York (782) and Dhuoda (841) have people rows. Aidan is named in the voices of Insular / Irish Monastic Christianity and Anglo-Saxon Christianity, and Hild of Whitby in the voices of Anglo-Saxon Christianity, with no people row. Nennius has none: the Medieval Welsh Christianity people list is empty, and its sourcing names the Historia Brittonum "attributed to Nennius". A people row for him is wanted, with "attributed" in the line. The Insular row gives Adomnán the year 679, after that movement's own end of 664. The census row names "Leoba", where the profile and the census row's own source title keep Edward Kylie's "Lioba". Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Card traditions (the worker's calls): Aidan of Lindisfarne in "Anglo-Saxon Christianity; Insular / Irish Monastic Christianity"; Adomnán of Iona in "Medieval Irish Christianity; Insular / Irish Monastic Christianity", Medieval Irish first by his years as abbot; Boniface of Mainz in "Anglo-Saxon Christianity", which lists him and covers his life, and not in Carolingian Reform Christianity, which begins in 751 and does not list him. Settle with the placing. Owner: the map Who build slice.
    - Census text, the live Bede entry (no census change was made in this batch). The longDescription's "Bede had just finished translating the Gospel of John" is L. Cecil Jane's; the St. Gallen text of Cuthbert's letter, as Charles Plummer prints it, has him translate as far as John 6:9 (Plummer 1896 l.11307-11312, English l.5760-5766), and Plummer doubts even that (l.5806-5811). "He died on Ascension Day in 735, aged sixty-two" gives a disputed year as settled (Plummer 735; 734 in Saxon Chronicle manuscripts; 742 in Lumby and Mayor; l.5430-5545), and the age is Jane's (Giles l.15615). The card's "unsigned editor" of the Biographical Notice is L. Cecil Jane (Giles l.15583-15588), and the card carries null author and date keys. The "sell Christ" legacy line is right but comes from the Wycliffite tract The Grete Sentence of Curs Expouned in Thomas Arnold's Select English Works, volume 3 (l.16380-16382, 17672-17674); the card's sources list only the Lollard Apology. The card's key work On the Times is tied to the "De Temporibus" of History III.17 as settled, where Plummer notes Bede gives that name to his longer work too (l.2736-2738). The card's remembered line opens on "Rome honors him.", a sentence with no fact of its own. Owner: the coordinator, for a census fix.
    - Census text, other entries. Anglo-Saxon Christianity, the story "The Oak at Geismar": it says robbers who wanted his chests killed Boniface; every held witness says pagans (Royal Frankish Annals "a paganis interfectus", l.1668-1670; Kylie "a heathen band", l.1817). Carolingian Reform Christianity, the Dhuoda story (marked "from reference summaries"): the dead she names are Bernard's kin, not both families' (Bondurand, l.571-574, 1559-1567); "she quotes Scripture, Gregory, Augustine and the poets" is not borne out, since her book quotes no Gregory and Augustine appears only in Bondurand's comparison (l.1225); Nithard has Bernard send William on terms, to commend himself to Charles for Bernard's Burgundian holdings, not as a hostage (Nithard l.2300-2305); on "William rebelled to avenge him", the held texts differ, with Bondurand giving the wish for vengeance to the younger Bernard (l.1840-1843) and an eighteenth-century editor's note in PL 115 giving it to William (l.112842-112844). Carolingian Reform Christianity, the story on Verden and Alcuin's letter rests on Alcuin's letters of 796, which are not held. Owner: the coordinator, for a census fix.
    - Library: the header of `cic/texts/alcuin_opera-omnia-letters_migne-pl100-101_1863.txt` says it holds PL 100 and 101 with the letters; the file holds PL 101 only (title page l.218), without the letters. Wanted, and noted on the cards or records: Alcuin's letters (PL 100, Dümmler's MGH Epistolae IV, or an English), the anonymous Vita Alcuini and Einhard's Life of Charlemagne, known here only through Jean Mabillon; Willibald's Life of Boniface and the full correspondence (Tangl or Emerton), and the Annales Fuldenses; Bede's computus works, the Letter to Plegwin and his commentaries; the text of Adomnán's Law (Cáin Adomnáin), the acts of Birr, Stokes's Tripartite Life volume I and Reeves's Life of Columba; the anonymous Whitby Life of Gregory the Great; a Life of Aidan and the Acta Sanctorum volume for 31 August; Heinrich Zimmer's Nennius Vindicatus, Gunn's 1819 edition, La Borderie's study and Mommsen's critical Latin of the Historia Brittonum; Carol Neel's English of Dhuoda. Owner: the Library thread.
    - Scan corrections (era 4 scan). Bede: Cuthbert's letter on his death is held, in Latin and English, in Plummer 1896 (l.11212-11425; English l.5511-5960), against the scan's "not held", which the row for Cuthbert, Bede's pupil, repeats; the History of the Abbots, the Letter to Egbert and Bede's prose Life of Cuthbert are also held; the Biographical Notice is L. Cecil Jane's. Hild: "one source (Bede)" is wrong, since Stephen's Life of Wilfrid in Raine 1879 also puts the synod in her presence and copies Pope John's letter naming men sent by her to Rome against Wilfrid (l.5083, 9418-9428); the Wilfrid among her five bishops is the later Wilfrid of York, not Wilfrid of Ripon; 614 is reckoned from Bede's sixty-six years. Aidan: "single source" should read nearly so, since the anonymous Lindisfarne Life of Cuthbert reports his death; "mission from 635" is the Bollandists' year, not Bede's. Adomnán: De Locis Sanctis is held, in PL 88 with his Latin Life of Columba and the Canones Adamnani; one held line gives the content of his Law ("not to slay women", a Lebar Brecc note in Stokes); his years are Wentworth Huyshe's. Boniface: Carloman's capitulary of 742, the Royal Frankish Annals, the Continuation of Bede and Altfrid's Life of Liudger are held witnesses the row does not list. Alcuin: his presence at Frankfurt in 794 rests on the capitulary's canon 56, not only on an editor; the scan's l.23690-23728 is Froben's dissertation, not Enhueber's; Mabillon rejects 804 for his death and argues he lived past 810. Dhuoda and Nennius: "c.803-843", "active 796" and "c.829" are the Library file headers, not held lines. Owner: the coordinator.

    - 2026-11-14: list lines closed by data release 42. Card traditions settled as the worker's calls name them. Census text closed: the Ladder legacy line, the Liberatus caveat and source note, and the Nisibis story of the Church of the East, each now carried by the witness that holds it. The Dioscorus records note now names the Arabic and Ethiopic synaxaries. Library items and scan corrections carried unchanged. Source: Decision-Log, "Era 3 on the live tree" (2026-11-14).
    - 2026-11-14: closed by data release 43 (Decision-Log, "Era 4 on the live tree"). List lines: the eight are person entries, and the Boniface, Leoba, Alcuin and Dhuoda rows link to them. Card traditions settled as the worker's calls name them. Census text closed: Bede's live entry takes his profile, with its six differences; the Oak at Geismar names pagans and now rests on Kylie and the annals; the Dhuoda and Verden stories rest on held lines. Library items and scan corrections carried in 265.

255. **Era 3 on the live tree: carried items (2026-11-14).** The 76 era 3 Who profiles and 3 era 3 major councils are in the census and on the site as text (data release 42). Source: Decision-Log, "Era 3 on the live tree" (2026-11-14); reviews in `Build/Ministry/Operations/Audits/2026-11-14_cft-era3-live/`.
    - Recording: none of the 79 entries has audio. They join the held recordings of Open-Gaps 218 and wait for an approved, capped run. The `audio/*.audio.txt` copies keep the profile text from before this release's spelling and rendering changes; the recording run builds from the census text. Owner: the coordinator.
    - Map position of people whose sources give no year in our reckoning: Euthymius 377 to 473 and Romanos the Melodist 490 to 556 (the Who scan's years), Julian 543 to 545 (the scan), John of Beth Aphthonia 538 (the Library file header, which is the archimandrite's year). Barsanuphius and John 527 to 565 (Justinian's reign, as held on the Theodora and Victor of Tunnuna cards). Each card's dates line says what the sources give. The Nubian Christianity entry's dates (543-652), its teaser ("543 to 652 CE") and its first story's years (543-545) rest on the same modern year for Julian, which John of Ephesus does not give. Owner: the coordinator, if a different year is wanted.
    - Place ids: many towns of these profiles have no census row to copy an id from (Arles, Gaza, Seville, Toledo, Dvin, Ravenna and others), so they show the name with no "today in" country. "The land of the Nobadae" (Julian, Longinus) has no id; the census "Nile Sudan" row may be copied if the map slice judges it the same place. No id is invented. Owner: the map build slice, with the Library thread.
    - `regions` on each person entry is its home tradition's (or its river's, for one told within none), as in release 41; no page reads it, and it can miss where a person lived (Vigilius, John Rufus, Constantius of Lyon). Owner: the map build slice.
    - Census text not changed here: the Reccared rows of Gothic, Vandal & Lombard Homoian Christianity and Nicene Visigothic Iberia (Open-Gaps 248); the Statutes of the School of Nisibis dated "496 and 602" in the Church of the East's Nisibis story, where Ignazio Guidi dates new rules made under Henana to 590; and the two story texts this release corrected (Church of the East, Nisibis; Nicene Visigothic Iberia, Toledo IV), which were above the reading-level target before and still are. Owner: the coordinator.
    - Status words: a person told within no tradition carries the A5 status "Named within another tradition's story", as in release 41. Owner: the map build slice.
    - `tools/check_tree_domains.mjs` reports 404 for the new tree pages until the site is deployed; check it again after the deploy. Owner: the coordinator.
    - 2026-11-14: the Reccared rows, Guidi's 590 for the Nisibis rules and the reading level of the Nisibis and Toledo IV stories closed by data release 43. The other items are carried in 265.

256. **Era 4 Who batch 2: card traditions, census text, Library items, and scan corrections (2026-11-14).** The eight batch 2 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch2/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch2/`; Decision-Log, "Who profiles, era 4 batch 2" (2026-11-14).
    - Card traditions (the worker's calls, accepted by the coordinator): Maximus the Confessor in "The Byzantine Imperial Church (Heraclian & Iconoclast Eras); Latin African Christianity under Byzantium"; Martin I of Rome in the Heraclian entry only, since no era 4 census movement is Roman, against the scan's "Heraclian; Roman"; Benjamin I of Alexandria in "Coptic Christianity under Early Islam; The Church of Alexandria and Miaphysite Egypt", Coptic first because his return under 'Amr and most of his patriarchate fall after 642. If a Roman era 4 movement is added later, Martin would take it second. Settle with the placing. Owner: the map Who build slice.
    - List lines: Maximus the Confessor has people rows in the Heraclian entry and in Latin African Christianity under Byzantium, Photius in the Macedonian entry, and Dionysius of Tel Mahre in Syriac Orthodox Christianity under Islam. Martin I, Timothy I, Jacob of Edessa, Gregory of Narek and Benjamin I are named in voices only, with no people row. Owner: the map Who build slice, with the placing in "Placing the approved Who profiles" (2026-11-12).
    - Census text, the Heraclian entry (no census change was made in this batch). "Vindicated by a council twenty years after his death": the held definition of the council of 680-681 does not name Maximus; Macarius of Antioch's profession read there curses him, and the council anathematizes and deposes Macarius (NPNF 2.14 l.25749, 25997; Mansi 11 l.74364-74367). "In 653 he was arrested in Rome with Pope Martin": no held line puts Maximus's arrest in Rome with Martin. "The record of his first trial, written by a disciple who was present": no author line was found in the held Record. The story "Pope Martin Writes from the Crimea": the trial and stripping are told by the Commemoratio of one of his clergy, not by Martin's letters; the held account sets him on a terrace before a crowd reaching to the hippodrome, not "in the hippodrome" (Mansi 10 l.87877-87880, 87914-87916); the voyage took more than a year with a year on Naxos, not three months (Duchesne l.162997-163001); the bushel price merges two figures, three or four modii for one coin in letter XVII (Mansi 10 l.88468-88472) and one modius for four solidi in the Commemoratio (l.88255-88262); no prayer for the emperor is in letters XVI and XVII; and the Life is cited to Loomis's English, whose held volume ends before Martin. Owner: the coordinator, for a census fix.
    - Census text, other entries. The Macedonian entry: the 867 apse mosaic and Photius's homily at its unveiling were not found in any held file searched; "nearly three hundred books" is 279 in his own count (Freese l.1713). The Church of the East on the Silk Road: the voice line's debate with al-Mahdi rests on no held text of the disputation, only its title in 'Abdisho's list (Bar Hebraeus vol. 3 l.10402-10403; Budge l.17405-17406); "780 to 823" gives one of several held death years (Elias of Nisibis 823; Bar Hebraeus AH 204; Amr AH 205; Chabot's note 823 and his index 825). Syriac Orthodox Christianity under Islam: the story of Dionysius before the caliph (832, "Bashmuric", the reed houses, the officials dismissed) is in no held line; the held account of the journey is Bar Hebraeus's (vol. 1 l.21798-21822). Jacob of Edessa's 684 and 688 are in no held line; "the first grammar of Syriac" rests only on Assemani's report of Elias of Nisibis; "against the Greek" belongs in the held lines to his revision of Severus's homilies, not to the Old Testament; 708 is one of three held death years. Bagratid Armenian Christianity: no held source calls Gregory of Narek's book the Book of Lamentations, says it was read over the sick, or calls it raw (Ormanian: "florid and sublime"), and the 2015 Doctor of the Church declaration is later than every held source. Coptic Christianity under Early Islam: Benjamin's return is told one way only; Michael the Syrian's account that he promised the Arabs Alexandria (tome 2 l.33096-33128) and Renaudot's and Ludolf's view that the Copts helped the conquerors are not in the census. Owner: the coordinator, for a census fix.
    - Library: the header of `cic/texts/severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt` gives Benjamin I "r. 626-665", which no held line supports (Evetts heads his life 622 to 661). The PO 5 continuation of the History of the Patriarchs is held in a file named for the Chronicle of Seert. The header of the chronica-minora file names Guidi's part only, but the file also holds Brooks's texts, among them Jacob of Edessa's Chronicle (from l.14453). The header of the Pyrrhus disputation file gives "Carthage, 645"; the held lines say Africa, and 645 is Fabricius's year. Wanted, and noted on the cards or records: Michael the Syrian tome 3 (Chabot 1905, books XII to XXI); Assemani's Bibliotheca Orientalis tome 2; Wright's Two Epistles of Jacob of Edessa; Vööbus's Synodicon in the West Syrian Tradition; Timothy I's Apology before al-Mahdi (Mingana, Woodbrooke Studies 2) and his Letters (Braun, CSCO 1914); a text of Gregory of Narek's Book of Lamentations; any public-domain English of Maximus's works and trials, of Martin's letters and the Commemoratio, and of Photius's letters, homilies and Mystagogy. Owner: the Library thread.
    - Scan corrections (era 4 scan). The Photian councils (council row, l.224): Mansi 15, 16 and 17-18 are held, against the scan's "not held"; Mansi 16 holds the council of 869-870 with Nicetas's Life of Ignatius, and Mansi 17 the council of 879-880. This matters for the era 4 councils. Photius (l.47): his life is held, in Nicetas, in Symeon the Logothete and the chronicle continuing Theophanes (PG 109), in the Liber Pontificalis 2 and in Cornelius Will (1861), whose Latin holds part of his encyclical and dates his death to 891; Freese's list gives his terms as 858-867 and 878-886, not "877-?". Timothy I (l.54): Amr ibn Matta's lives and Elias of Nisibis are held witnesses the row does not list; a bishop Timothy of Beth Bagash in Braun's Synodicon is a further namesake. Dionysius of Tel Mahre (l.55): his death is held (Bar Hebraeus vol. 1 l.22468-22472), and his journey with al-Ma'mun is held in Bar Hebraeus (l.21798-21822); Michael's book XII is not held. Jacob of Edessa (l.56): his own words are held in the preface to his Chronicle in Michael tome 1 (l.56521-56590), in his gloss on Severus's sermon 77 in PO 16, and in his Chronicle in Brooks's Latin; his canons are held in part in Bar Hebraeus's Nomocanon (Mai, volume 10); Assemani gives a full chapter, XL, and Bar Hebraeus a full life. Maximus (l.46): "Carthage, 645" is the file header's; the Lateran acts hold a "Maximus monachus" signature though Binius's note says they do not name him. Martin I (l.50): two of his letters are printed in interleaved columns, so letter XVI's line on bread is l.88454-88458; the Breviary and Bede also hold him. Gregory of Narek (l.58): Serpos tome 3, Issaverdens's history and Armenian Ritual (two of Gregory's prayers), Stepanos of Taron in Macler's French and the German, Boré, Alishan, Nurikhan and Parisot's Aphrahat (two Latin quotations of Gregory) are held witnesses the row does not list. Benjamin I (era 3 scan, l.38): the PO 5 continuation, Michael the Syrian, Renaudot, both Synaxaria, Abu Salih and Assemani's Coptic catalogue (a homily on Cana, codex XVI) are held witnesses the row does not list. Owner: the coordinator.
    - 2026-11-14: closed by data release 43. Card traditions settled as named. List lines: Maximus, Photius and Dionysius link to their entries; the others are person entries in their home traditions. Census text closed: the Heraclian Maximus lines and the Martin story, the Macedonian 279 books and mosaic, the Silk Road Timothy voice line and story, the Dionysius story and Jacob of Edessa lines, the Narek lines and story, and Benjamin's return told with Michael the Syrian and Renaudot. Library items and scan corrections carried in 265.

257. **Era 4 Who batch 3: list lines, card traditions, two era 3 card readings, Library items, and scan corrections (2026-11-14).** The eight batch 3 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch3/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch3/`; Decision-Log, "Who profiles, era 4 batch 3" (2026-11-14).
    - List lines: Leoba has a people row in Anglo-Saxon Christianity (732). Muirchu is named in the voices of the Patrick of Ireland entry, Willibrord in the Anglo-Saxon long description, Theodore of Tarsus in the Bede entry's legacy, Wilfrid in the Insular / Irish Monastic, Columba and Anatolius entries, Cogitosus in the Brigid of Kildare entry and Tirechan in the Ciaran of Clonmacnois entry, all with no people row. Cuthbert of Lindisfarne is named nowhere in the census; its Cuthbert in the Bede entry is Bede's pupil. Owner: the map Who build slice.
    - Card traditions (the worker's calls, accepted by the coordinator on 2026-11-14): Muirchu and Tirechan in "Medieval Irish Christianity", since every held dating of their work is 664 or later; Cogitosus in "Medieval Irish Christianity; Insular / Irish Monastic Christianity", his date being disputed from Migne's 591 to Stokes's 800 to 835; Theodore, Willibrord, Leoba, Wilfrid and Cuthbert in "Anglo-Saxon Christianity" only. Leoba's last years may fall after 751, but no held line gives her death. Owner: the map Who build slice.
    - Name: the supplement scan's "Wilfrid of York" is written as Wilfrid of Ripon, id `wilfrid-of-ripon`, to agree with the approved Hild of Whitby texts, which keep "Wilfrid of York" for Hild's pupil, Wilfrid II (the coordinator's call, 2026-11-14).
    - Era 3 cards, two readings to check, not changed here (the coordinator's call, 2026-11-14: folded into the era 4 map build). The Brigid of Kildare card says Basnage "says that placing follows others", tying his "Cogitosum hic reponimus, aliorum vestigiis insistentes" (PL72 l.58442) to Migne's 591; Basnage wrote it for his own edition of Canisius, and the held lines do not show where he placed Cogitosus there. The Ciaran of Clonmacnois card dates Tirechan "after the plagues Stokes dates to 683", where Stokes's note reads "apparently" (STOKES l.3224) and Newport White gives no earlier than 664, possibly about 670, with Bury's 664 to 668 (WHITE l.1388-1390, 3596-3599). Owner: the era 4 map build, with the coordinator.
    - Library: `cic/texts/stokes_tripartite-life-of-patrick-v2-lat-muirchu-tirechan-confession_1887.txt` begins partway into Muirchu (l.213); Stokes's pages 269 to 271, with Muirchu's preface, table and name note, are missing, though the index points to them, and the header's "Muirchu from raw line ~360" and "Tirechan from ~2251" are wrong (Tirechan begins at l.2212). The Raine 1879 file is named for Byrhtferth's Life of Oswald, but Raine calls that Life anonymous (l.2425-2426), and the file also holds Stephen's, Fridegod's and Eadmer's Lives of Wilfrid. Wanted, and noted in the records: Rudolf of Fulda's Life of Leoba and any Acta Sanctorum September volume; Bede's verse Life of Cuthbert; an English of Stephen's Life of Wilfrid, of Bede's prose Life of Cuthbert and the Lindisfarne monk's Life, and of Cogitosus; Theofrid of Echternach's Life of Willibrord and Boniface's letter to Pope Stephen; Plummer's notes volume to Bede; Haddan and Stubbs; the acts of Adomnán's synod at Birr. White gives "Prof. Bury" and "Bishop Graves" no first names. Owner: the Library thread.
    - Scan corrections (era 4 scan). Theodore of Tarsus (l.32): Bruns's Hertford text is taken from Bede (BRUNS l.22374), not an independent witness; the Penitential of Theodore is held in Wasserschleben (1851), who holds that Theodore wrote no penitential himself; Stephen's, Fridegod's and Eadmer's Lives of Wilfrid add the 678 removal and the London confession. Willibrord (l.33): "c.658-739" rests on no held line (Alcuin gives the day and no year; the Roman Breviary gives 738, aged 81, and Kylie 739); his own calendar note is held in Duchesne's Liber pontificalis I; Boniface served under him in Kylie's introduction, not in a held letter. Leoba (l.34): "d. c.782" rests on no held line; "Boniface's last command" (BONI 1758) is Kylie's introduction, and no letter in his book tells of it; her verses are held in Kylie's English. Muirchu (l.35): "son of Cogitosus" rests on Bishop Graves's correction, which White reports; his preface is held only in White's English, since Stokes's pages are missing. Tirechan (l.36): "from the mouth or book of Bishop Ultan" (STOKES l.2212) is a heading in the Book of Armagh, not Tirechan's own sentence. Cogitosus (l.37): both of Stokes's index entries point to the page of Muirchu's preface, which is not held.
    - Scan corrections (supplement scan). Wilfrid (l.187): Stephen's (Eddius's) Life is held in Raine 1879, against the scan's "not held", and so are Fridegod's verse Life and Eadmer's Life; his petitions to Agatho and John VI are held in Stephen, and his subscription to Agatho's synodal letter in Mansi 11. Cuthbert of Lindisfarne (l.188): Bede's prose Life and the Lindisfarne monk's Life are held in Latin in Acta Sanctorum, March, volume 3, against the scan's "not held"; Bede's verse Life is not held; the year of consecration needs no "[suggested]", since Bede puts it in the year King Egfrid was killed, which his summary of years gives as 685. Owner: the coordinator.
    - 2026-11-14: closed by data release 43. List lines and card traditions settled as named. The Brigid (Basnage) and Ciarán (Tirechan's date) card readings are fixed in the census and the profile files. Library items and scan corrections carried in 265.

258. **Era 4 Who batch 4: card traditions, census text, Library items, era 3 card points, and scan corrections (2026-11-14).** The eight batch 4 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch4/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch4/`; Decision-Log, "Who profiles, era 4 batch 4" (2026-11-14).
    - Card traditions (the worker's calls, accepted by the coordinator): Humbert of Silva Candida in "The Latin Papal Church (Gregorian Reform to Innocent III); The Byzantine Imperial Church (Macedonian Era)", since both name him and the Latin Papal entry, his own church, begins in 1049; Beuno in "British and Welsh Christianity", against the scan's Medieval Welsh, which begins in 768, since the note in W. J. Rees's edition puts him in the sixth and seventh centuries with Clynog Fawr founded in 616; Jonas of Bobbio in "Insular / Irish Monastic Christianity", since Merovingian Gallic Christianity ends in 620, before his work of about 640. Owner: the map Who build slice.
    - Census text (no census change was made in this batch). The Latin Papal entry's voice line says Humbert "drafted the reform's sharpest arguments": the held lines show only his 1054 writings and his 1059 signature; his books against the simoniacs are not held. The Carolingian entry's voice line calls Hincmar a canon lawyer "who pressed the reform's claims even against kings": the held lines show him pressing church law against his nephew and before Pope Hadrian II, and, by his own letter, reproving King Charles for an unjust judgment; no held line shows more against kings. The Nicene Visigothic entry's line that Ildefonsus's devotion to the Virgin "shaped later Spanish piety" rests on no held line beyond Cixila's later Life. Owner: the coordinator, for a census fix.
    - Library. The header of `cic/texts/mirk_festial-enm_erbe1905.txt` gives Mirk "active about 1403", which no held line supports, and names British Museum MS. Cotton Claudius A. II, where the title page reads "EDITED FROM BODL. MS. GOUGH ECCL. TOP. 4" (l.110). The header and content note of `cic/texts/eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt` name Eulogius only, but the file also holds Prudentius of Troyes's works and Nicolás Antonio's notice of him (from l.79212). Wanted, and noted on the cards or records: Hincmar's treatises (Patrologia Latina 125-126) and Flodoard's History of the Church of Reims; Humbert's books against the simoniacs; the Acta Sanctorum Life of Attala (10 March), on which the editors rest Jonas's birth at Susa; any public-domain English of Will's 1054 texts, of the Toledo councils, and of the Lives of Ildefonsus and Julian. Owner: the Library thread.
    - Era 3 cards (outside this batch; not changed here). The Isidore of Seville card (era 3 batch 6) quotes Braulio's notice of Isidore's works without the held dispute over its authorship: a note printed with Nicolás Antonio's notice in PL 80 says Gregorius Mayansius denied it was Braulio's, and keeps it as his on the old manuscripts its writer had seen (l.52007-52061). The Columbanus card (era 3 batch 6) lists the Mansi 10 source with no date. Owner: the coordinator, for the era 3 map build.
    - Scan corrections (era 4 scan and supplement). Humbert (l.51): Cornelius Will's Acta et scripta (1861) is held, with the envoys' account, the sentence, the Dialogue and the reply to Nicetas, the edict of Keroularios's synod and Keroularios's letters to Peter of Antioch; the bull's 16 July is Will's reading, and Mirbt's 13 July is his heading. Hincmar (l.42): his canon-law and church-political work is held, against the scan's "not held": chapters for his priests, letters and his ordination in 845 (Mansi 15), the council of Douzy, the bishops' letter to Hadrian II, his own letter to Hadrian and the writings of both Hincmars (Mansi 16), his nephew's complaint to John VIII (Mansi 17-18), and his Life of Remigius (Krusch, MGH SRM 3); Mommsen (MGH AA 11) gives his death in 882; the annals' introduction the scan gives to Waitz is G. H. Pertz's. Prudentius (l.43): his own works are held in Patrologia Latina 115, among them his treatise against John Scotus Eriugena, his letter to Hincmar and Pardulus, the Tractoria and his verses for a Gospel book, with Nicolás Antonio's notice; who wrote the 861 notice is disputed (Pertz, Hincmar; Antonio, an unnamed annalist). Jonas (l.38): his Latin preface is held in Barralis 1613, his Life of John of Réomé in Krusch's MGH SRM 3, and the Acta Sanctorum for March, volume 3, gives his birth at Susa and a hedged succession as abbot of Bobbio. Braulio (l.44): his letters to and from King Chindaswinth and to Pope Honorius, and the Chronicle of 754 in Mommsen's edition, are held witnesses the row does not list. Ildefonsus (l.45): Julian's tribute, Cixila's and Cerratensis's later Lives and Antonio's notice (his reported birth in 607 and Agali as Saints Cosmas and Damian) are held. Julian (supplement l.191): Felix's notice of his death and Toledo XV's answer to the points Pope Benedict had raised are held; the header's c.642-690 rests on no held birth line. Beuno (l.70): no witness near his own time is held; every held account (the Welsh Life, the Latin Life of Winefred, Mirk's Festial, the Laws of Wales cited by Hugh Williams) is late. Owner: the coordinator.
    - 2026-11-14: closed by data release 43. Card traditions settled as named. Census text closed: the Humbert, Hincmar and Ildefonsus voice lines say only what held lines show. Era 3 cards: Isidore's card names the dispute over Braulio's notice, and the Columbanus Mansi 10 sources carry 1901. Library items and scan corrections carried in 265.
259. **Era 4 Who batch 5: list lines, card traditions, census text, Library items, and scan corrections (2026-11-14).** The eight batch 5 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch5/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch5/`; Decision-Log, "Who profiles, era 4 batch 5" (2026-11-14).
    - List lines: Alopen is named in the voices of The Church of the East on the Silk Road, Moses bar Kepha in those of Syriac Orthodox Christianity under Islam, and Athanasios the Athonite in those of The Byzantine Imperial Church (Macedonian Era) and Athonite & Comnenian Byzantine Monasticism. Sebeos is named in the Heraclius entry's voices and in the Council of Dvin and Caucasian Albania entries. John of Nikiu has a people row in The Church of Alexandria and Miaphysite Egypt entry. Sophronius is named in the Theodosius I of Alexandria and John Moschus entries. Thomas of Marga is cited, not named as a person, in the Babai the Great entry and a link. Antony of Choziba is named nowhere in the census. Owner: the map Who build slice.
    - Card traditions (the worker's calls, reported to the coordinator on 2026-11-14): Sophronius in "The Byzantine Imperial Church (Heraclian & Iconoclast Eras); Chalcedonian Monasticism - Judean Desert & Gaza", though neither names him; Athanasios in "The Byzantine Imperial Church (Macedonian Era); Athonite & Comnenian Byzantine Monasticism", the second an era 5 entry that begins with his Lavra in 963; Sebeos in "Armenian Christianity before the Bagratids" (c.554-884), since the scan's "Armenian Apostolic" is no census name and no era 4 Armenian entry covers the 660s; Antony of Choziba in "Chalcedonian Monasticism - Judean Desert & Gaza", whose window ends at 614, since no era 4 entry covers the Judean desert houses; Thomas of Marga in "The Church of the East on the Silk Road; The Church of the East under the Abbasids". Owner: the map Who build slice.
    - Census text to check, not changed here. Athonite & Comnenian Byzantine Monasticism, documented story on Athanasios's death: the abbot found alive under the dome, and "both of his Lives", rest on no held line; Philipp Meyer, from the Life, says all were pulled from the rubble dead (MEYER l.1415), and only one Life is known, through Agapios. The Church of the East on the Silk Road: "a Persian monk" (every held source says Syria, or Ta-ts'in), "rediscovered 1623-25" (held sources say 1625), and the edict's wording, which is Nicolini-Zani's, not held; the Tang huiyao is not held. The Church of Caucasian Albania cites "Sebeos, History, ch. 38-41" for the Khazar alliance; Macler's book III ends at chapter 38, and his note puts the one Khazar passage much earlier (MACLER04 l.3757-3760). The Church of Alexandria and Miaphysite Egypt (328-642) carries John of Nikiu's people row at 690, outside its window; his card reads "Coptic Christianity under Early Islam". Owner: the coordinator, for the census owner.
    - Sophronius card, first `uncertain` item: "No text of Sophronius's own time gives those words" should read "No held text", as records.json has it; noted by the R4 cap check and not changed after round 3. Owner: the era 4 map build.
    - Open-Gaps 50, "Era-4 text outside the links pass" (2026-11-08), reads Alopen's arrival as "636, not 635". The held stele translation (A. Wylie, in Malech 1910, l.13690), Henry Yule and Budge's Appendix B give 635; 636 comes from Assemani, the Abbeloos-Lamy note to Bar Hebraeus and Budge's introduction. Item 50 is not edited here (the coordinator's call, 2026-11-14). Owner: item 50's owner.
    - Library: Moses bar Kepha's On Paradise, in Masius's Latin, is held inside `cic/texts/nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt` (from l.37059), under another author's file name; the held text breaks off in part III. The Greek of Meyer's Athos edition and of the Choziba volume is badly garbled, and their headers mark it second witness only; Athanasios's and Antony's words are told from it in modern words and should be checked against the page images before any is quoted. The Choziba file header names C. Houze as editor; no line of the volume as held carries the name. Wanted: Assemani, Bibliotheca Orientalis II (the anonymous Life of Moses bar Kepha); Michael the Syrian, tome 3; Budge's Book of Governors, volume 1 (Syriac and introduction); the Acta Sanctorum for July (Athanasios); a modern study of Sebeos's authorship and the Armenian text; Connolly and Codrington's Two Commentaries on the Jacobite Liturgy (1913); the Tang huiyao. Owner: the Library thread.
    - Scan corrections (era 4 scan). Moses bar Kepha (l.57): one work is held, On Paradise in Migne PG 111, against "none of his works is held"; the life in the editors' note is theirs, from an anonymous Syriac life in Assemani's volume II, which is not held. Athanasios (l.48): Meyer knew the Life only in Agapios's Modern Greek version; the death by the falling dome is the Life's alone. Sophronius (l.49): the Miracles, his own poem and the Christmas sermon are held in PG 87.3. Sebeos (l.52): no held source names his see or argues against book III; Stephen of Taron's naming is held in German. Antony (l.53): the name Antony is in the Greek (AB7 l.35348). Alopen (l.59): every held source goes back to the stele; Wigram 1929 gives about 630. Thomas of Marga (l.61): Mari ibn Sulayman, in Gismondi's Latin, has him as metropolitan caring for his imprisoned brother, the patriarch Theodosius. John of Nikiu (l.68): his life is told in the History of the Patriarchs (Patrologia Orientalis 5), and Charles's 690 and 696 have no held source. Owner: the coordinator.
    - 2026-11-14: closed by data release 43. List lines and card traditions settled as named. Census text closed: the Athanasios story (one Life; the monks pulled out dead); the Silk Road stele story (Syria, 635, 1625, Wylie's wording, no Tang huiyao); the Albania source (Sebeos ch. 19, Macler's note); John of Nikiu's name row removed from the Miaphysite Egypt entry (Mark's pick, 2026-11-14). The Sophronius card reads "No source used here from Sophronius's own time". Item 50 is not edited; its 635/636 finding is carried into the stele story. Library items and scan corrections carried in 265.

260. **Era 4 Who batch 6: census text, Library items, and scan corrections (2026-11-14).** The eight batch 6 profiles (the Coptic patriarchs Agathon, John III of Samannud, Isaac, Simon I, Alexander II, Michael I and Joseph I of Alexandria, and Severus ibn al-Muqaffa) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch6/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch6/`; Decision-Log, "Who profiles, era 4 batch 6" (2026-11-14).
    - List lines: Coptic Christianity under Early Islam shows no people ("No one is shown"); Benjamin I and Severus are named in its voices, Yusab in its documented story and in the Syriac Orthodox under Islam and Makurian Nubian stories, and Michael I in the Makurian and Melitian schism entries. The other five are named in no census text. Owner: the era 4 map build.
    - Census text to check, not changed here. Makurian Nubian Christianity, "King Kyriakos Marches North for the Patriarch": the governor is "Abd al-Malik ibn Marwan" where the held History has "a son of Musa, son of Nasir" (PO 5 l.5840-5843; Evetts's note in Abu Salih l.13474); the forced marriage to a Christian woman, Michael sent south to meet the king, the realm "from the First Cataract to the joining of the Niles" and the Fayyum rest on no held line; "patriarch from 743" is the synaxarium editor's bracket, where Evetts heads 744. Coptic Christianity under Early Islam, "Two Patriarchs Ride with the Caliph's Army": the rebels' words, the safe-conducts, the years 831 and 832 and the end of the Bashmuric dialect rest on no held line (the History's life of Yusab, PO 10, is not held). Syriac Orthodox under Islam, the Dionysius story: the reed houses, the dismissed officials and the march to Fustat rest on no held line. Makurian Nubian Christianity, "Prince Georgios Goes to Baghdad": the parasol with a cross, al-Mu'tasim, the three-yearly tribute and 836 rest on no held line; Renaudot has an unnamed caliph and a gold cross in the prince's hand, Abu Salih has Ibrahim, brother of al-Ma'mun. Coptic Christianity under Early Islam, peopleNote: "whether he wrote it is disputed" is stronger than the held lines, which show a dispute over how much of the History is his and over his century (Evetts 1895 and 1904; Renaudot). Owner: the census owner, at the era 4 map build.
    - Library. `cic/texts/chronicle-of-seert_histoire-nestorienne-premiere-partie-fasc2-patrologia-orientalis-5-ara-fra_scher-dib1910.txt` holds Evetts's History of the Patriarchs, Agathon to Michael I, to l.10707, under the Chronicle of Seert's name. `cic/texts/john-ephesus_lives-eastern-saints-po17_brooks1923.txt` also holds Basset's Arabic Synaxarium for Baounah, Abib and Mesore (Simon I at 24 Abib, l.58407; Masis of Ousim at 11 Mesore, l.60599). `cic/texts/synaxaire-arabe-jacobite_po1-thout-babeh-synaxaire-ethiopien-fra_basset-guidi1907.txt` holds a cleaner copy of Evetts's life of Benjamin I (l.26645 ff.). Mina's Life of Isaac is held twice, in the PO 11 synaxarium file (l.21161 ff.) and bound into the Evetts PO 1 file (l.19006 ff.). Renaudot's year for Michael I's death is unreadable in the OCR (l.15533-15554). Wanted: the History's life of Yusab (Evetts, PO 10); Basset's Arabic Synaxarium for Hatour and Kiahk (PO 3), with the notices of Isaac and John III; Michael the Syrian, tome 3; Severus's Refutation of Eutychius (Chebli, PO 3) and History of the Councils (Leroy, PO 6), and the preface to the Book of the Councils the census cites. Owner: the Library thread.
    - Scan corrections (era 4 scan). Michael I (l.62): his life runs from PO 5 l.4414, not l.4979; its writer, John the deacon, names himself. John III (l.65): the governor demanded a hundred thousand denarii; drachmae appear only in John's answer. Simon I (l.63): his teacher was John, head of the monastery of Az-Zajaj, not John III; the men who kept mistresses were laymen, shut out by the bishops; his Arabic Synaxarium notice is held (PO 17 file, 24 Abib). Alexander II (l.64): the History gives twenty-four and a half years on the throne, not twenty-five. Isaac (l.71): Mina's Life is held in both files named above. Yusab (l.72): besides the Synaxarium, Renaudot's Latin retelling of the History's life, Budge's Ethiopic (23 Tekemt), Bar Hebraeus's quotation of Dionysius and Abu Salih are held. Agathon (l.66): his own first-person account of Benjamin's consecration of the church of Saint Macarius is held in Benjamin's life. Severus (l.67): Renaudot's notice and list of works, Budge's and Grébaut's Ethiopic synaxaria and Assemani's catalogue are held. Owner: the scan's next revision.
    - 2026-11-14: closed by data release 43. List lines: the eight are person entries in Coptic Christianity under Early Islam, whose peopleNote is gone. Census text closed: the Kyriakos, Georgios, Two Patriarchs and Dionysius stories rest on held lines. Library items and scan corrections carried in 265.
261. **Era 4 Who batch 7: list lines, card traditions, census text, Library items, and scan corrections (2026-11-14).** The seven batch 7 profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch7/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch7/`; Decision-Log, "Who profiles, era 4 batch 7" (2026-11-14).
    - List lines: Symeon the New Theologian is named in the voices of Athonite & Comnenian Byzantine Monasticism, and Niketas Stethatos in that entry's documented story. Paul the Deacon is cited in several era 3 entries and an edge, not as a person of an era 4 entry. Cedd and Chad, Elipandus and Felix, Paulus Emeritanus, and Pisentius and John are named nowhere in the census. Owner: the map Who build slice.
    - Card traditions (the worker's calls, confirmed by the coordinator on 2026-11-14): Symeon and Niketas in "The Byzantine Imperial Church (Macedonian Era); Athonite & Comnenian Byzantine Monasticism", since the scan's "Byzantine monastic and hesychast tradition" is no census name; Elipandus and Felix in "Mozarabic Christianity; Carolingian Reform Christianity", since the scan's Nicene Visigothic Iberia ends in 711; Paul the Deacon in "Carolingian Reform Christianity", since the scan's Early Benedictine Italian Monasticism (to 604) and Gothic, Vandal & Lombard Homoian Christianity (to 680) end before his birth and no era 4 entry covers Italy; Pisentius and John in "The Church of Alexandria and Miaphysite Egypt", the census name for the scan's id. Owner: the map Who build slice.
    - Pair length: the three paired profiles run to about 2:25-2:28 under the 2:30 cap (the coordinator's call), and the single non-majors to about 2:15; Mark kept these lengths on 2026-11-14 ("keep"), and later batches hold non-majors to 2:00 where a good story allows. Owner: the coordinator.
    - Census text to check, not changed here. Athonite & Comnenian Byzantine Monasticism, the story of Symeon's exile: "1009", "twenty-five years" as abbot, the trick question on the Trinity answered in verse, his teacher's conduct with young monks, and monks forbidden to follow him rest on no held line; its "a monk of no rank whom the hierarchy had never approved" conflicts with the held Life, in which the patriarch Sergius read and praised the hymns and later offered Symeon a metropolitan see (PG 152 l.20084-20109, 20281-20288); its peopleNote, that the Library holds no words of the people named, is out of date for Symeon and Niketas (Philokalia vol. 2). Mozarabic Christianity's peopleNote says the same, while Elipandus's own letters are held in PL 96; whether he belongs in that entry's people is the owner's call. Owner: the coordinator, for the census owner.
    - Library: Niketas's Life of Symeon is not held as a text, but François Combefis's long summary with Greek extracts is held in PG 152 (`calecas_opera-omnia-pg152-grc-lat_migne1866.txt`, l.19524-21260), in a file named for Manuel Calecas. Foulke's introduction to Paul the Deacon is missing its pages xx-xxi in the held file (the jump at l.616), on Paul's brother and the journey to France. Wanted: Symeon's works in PG 120 (Discourses, Hymns); Agobard of Lyon against Felix; Paulinus of Aquileia against Felix; Amélineau's Memphitic Life of Pisentius; the Anglo-Saxon Chronicle; Plummer's Bede, volume 2 (commentary); an English translation of the Lives of the Fathers of Mérida. Owner: the Library thread.
    - Scan corrections (supplement scan, era 4 table). Symeon (l.186): the Life by Niketas is not held, but Combefis's summary of it with extracts is, against "not held" with nothing in its place; the coordinator asked for this to be logged (2026-11-14). Pisentius and John (l.193): "d. c. 632" rests on the Library file header only; no held line gives his death year, and Budge gives none. Elipandus and Felix (l.190): Froben's "prope 50" years as bishop is very likely an OCR misreading of 30, and the 809 and 780 are Madrisi's, which Froben adopts. Paul the Deacon (l.194): "died after 791 (Foulke 865)" does not hold; Foulke l.865 is the death of Duke Arichis in 787, Foulke gives Paul's death day (13 April) with the year unknown, and 791 is Angilram's death. Paulus Emeritanus (l.192): "Levita Christi", his own word for his rank, is held (PL 80 l.9213), against "not in a held line (deacon of Merida)". Cedd and Chad (l.189): Giles's chapter heading "[a.d. 659]" for Cedd's death cannot stand beside Bede's own account of Whitby in 664; Plummer and the Bollandists give 664. Owner: the coordinator.
    - 2026-11-14: closed by data release 43. List lines and card traditions settled as named; the paired entries are one entry each. Census text closed: the Symeon story rests on Combefis's summary in PG 152; the Athonite peopleNote is made true; the Mozarabic peopleNote is gone. Library items and scan corrections carried in 265.
262. **Era 4 Who batch 8: list lines, census text, Library items, and scan corrections (2026-11-14).** The six batch 8 profiles (Eadburga of Thanet, Abbess Bugga, Yahya ibn Said of Antioch, Elias of Nisibis, Adam (Jingjing) and al-Baladhuri) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch8/`. None is in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch8/`; Decision-Log, "Who profiles, era 4 batch 8" (2026-11-14).
    - List lines: Adam is named in the voices of The Church of the East on the Silk Road, and Eadburga in Anglo-Saxon Christianity's Leoba story. al-Baladhuri is named in one census relation note, Nubian to Makurian Nubian Christianity. Bugga and Yahya are named in no census text; Elias appears only as a cited author on era 3 Who cards. al-Baladhuri's card reads "Outside the church"; the scan placed him with the Muslim chroniclers of the conquests, which is not a census movement. Owner: the era 4 map build.
    - Census text to check, not changed here. The Silk Road story says the stele was "composed in elegant Chinese by a priest named Adam — Jingjing"; the held lines join King-Tsing to Adam only through Henri Cordier's note in Yule (l.3000), and "elegant" rests on no held line. Owner: the census owner, at the era 4 map build.
    - Library. The header of `cic/texts/elias-of-nisibis_opus-chronologicum-lat_brooks-chabot-csco1910.txt` gives Elias 975-1046; no held line gives 1046 (Assemani and Mai: after 1049; Chabot: soon after 1049; Macler: about 1056). Elias's own preface and chapters on inheritance are held in `mai_scriptorum-veterum-nova-collectio-tomus10-ebedjesu-synodus-timothei-lat_mai1838.txt` (l.7395-7520, 8412 ff.). A second OCR of Patrologia Orientalis 18, with Yahya's avant-propos, is in `john-ephesus_lives-eastern-saints-po18_brooks1924.txt` (l.39862). Wanted: the rest of Yahya's history, after about 970; Elias's letter on Isho'yahb and his Sessions; J. Takakusu's T'oung Pao paper on King-tsing and the Satparamita; volume 2 of Hitti's al-Baladhuri. Owner: the Library thread.
    - Scan corrections (supplement scan). Elias (row l.197): the dates 975-1046 come from the Library header; the life on pp. 228-229 is a note Brooks marks as added by later hands; his own words on inheritance are held in Mai. Eadburga (l.195): "Abbess of Thanet" is in Kylie's headings and introduction, not in the letters; the Bollandists give a death day, 27 December, for their merged Eadburga-Bugga. Bugga (l.198): Bregwin's letter on her burial day is held in PL 96 (l.69812-69818); her mother's letter is Kylie's VIII, though the OCR heads it "VII". Owner: the scan's next revision.
    - Scan correction (era 4 scan). al-Baladhuri (l.69), "WHO (OUTSIDE WITNESS)", was taken by no batch 1 to 7; the coordinator added him to batch 8. Owner: the coordinator.
    - Two notes from the R4 cap check, not changed: in the al-Baladhuri brief, "He also gives the terms the Christians of Najran made with Muhammad" follows Khalid and can be heard as his ("Al-Baladhuri also gives" would fix it); the Adam card spells "King-Tsing" (Wylie) in one item and "King-tsing" (Cordier) in two. Owner: the next Who pass over era 4.
    - 2026-11-14: closed by data release 43. List lines: the six are person entries; al-Baladhuri is told within none, in the Syriac East & Asia river (Mark's pick, 2026-11-14). Census text closed: the stele story no longer says "elegant" or joins Jingjing to Adam beyond Cordier's note. The two R4 notes are fixed in the profile files. Library items and scan corrections carried in 265.
263. **Who re-score, eras 4 and 5: the rows still WANTED, and the calls for Mark (2026-11-14).** The era 4 and era 5 WANTED rows were re-scored after the Library's era 4 and era 5 batches. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-rescore-eras4-5/Rescore.md`; Decision-Log, "Who re-score, eras 4 and 5" (2026-11-14).
    - Still WANTED. Ibn Hayyan (era 4): no edition of al-Muqtabis before 1937 was found. Walter Daniel (era 5): his Life of Ailred was not found, and no work of his is held. Hadewijch (era 5): Mark allows only the 1875 dbnl edition, which is not vendored. Teodosije (era 5, split from Domentijan): his reworked Life of Sava (printed 1860) is not held, and by date of work he is probably era 6. Owner: the Library thread.
    - Calls for Mark. Þorgeir is STORY (alternative LISTED). Giorgi Merchule is WHO as a recorder (alternative LISTED). The Domentijan and Teodosije pair is split. Marco Polo has no OUTSIDE WITNESS label. Anna Komnene has no label either, unlike Procopius. Innocent III is STORY and keeps his live entry. Sergius-Tychicus is LISTED, but his letters quoted by Peter of Sicily could be ruled a second voice. Owner: Mark.
    - Major caps. Era 4 Greek East would hold nine majors and Latin West eleven, against five per river. Era 5 Latin West would hold fourteen. Which five each river shows is proposed in `Rescore.md`. Owner: Mark, through the coordinator.
    - Needs-ruling Lives still open after the re-score: Clement of Ohrid (the PG 126 Monitum disputes the author and date), Robert of Molesme, Norbert of Xanten, Agnes of Prague, Joachim of Fiore, Stephen Harding and Gregory Pakourianos. Where the held volume dates a Life (Stephen the Younger, Theodore the Studite, the Vita Euthymii, the Iviron Lives, Grigol Khandzteli), the date is given in the table. Owner: the batch that writes each profile.
    - Wanted, to strengthen rows that pass now: Innocent III's own works (De miseria, PL 217), which might make him WHO; Photius's Contra Manichaeos and Peter the Higumen, a second witness for the Paulician teaching; the Slavonic Lives of Constantine and Methodius in usable OCR. Owner: the Library thread.
264. **Era 6 Who batch 1: census differences, Library items, and scan corrections (2026-11-14).** The eight batch 1 profiles (John Wyclif, Thomas à Kempis, Richard Rolle, Julian of Norwich, Meister Eckhart, Johannes Tauler, Henry Suso and Geert Grote) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/`. Wyclif and Kempis are live census person entries and are not changed here; the other six are not in the census or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era6-batch1/`; Decision-Log, "Who profiles, era 6 batch 1" (2026-11-14).
    - Census text to check, the live Wyclif entry (not changed here). (1) "c. 1360-1384" and "From about 1360 he argued there against the friars": Vaughan says only that 1360 "has been mentioned"; Shirley calls the friar-controversy story a fact "only by courtesy and repetition" (VAUGHAN l.1260-1261; SHIRLEY l.806-812, 878-882). (2) "His 1845 editor says Balliol College chose him as its head": name Vaughan ("newly-elected warden of Baliol", l.1262-1266); Shirley and Forshall and Madden, from college deeds, have him master by April 1361 (SHIRLEY l.884-886; F&M l.957). (3) "In 1374 he went to Bruges ... The crown then gave him the parish of Lutterworth": "then" follows Vaughan (l.1996-2004); the patent roll gives April 1374, before Bruges (SHIRLEY l.2364-2377; F&M l.979-981). (4) "His opinions were condemned by the pope in 1377" and "In June 1377 the pope sent letters": the bulls order inquiry into what "should be found erroneous" (VAUGHAN l.2252-2262); the date is 30 May in Shirley (l.1728-1729) and 11 June in F&M (l.995-997). (5) "On 29 December 1384, as he gave out the bread at Mass, he was struck": Vaughan "is said to have been employed in administering the bread" (l.4761-4766); Shirley "hearing mass" (l.2748-2751); Walsingham, hostile, has him struck before a sermon against St Thomas (l.10997-11030). (6) "Jan Hus took paragraph after paragraph": David Schaff's phrase, resting on Loserth (SCHAFF l.1513-1516); say whose. (7) "As it met, an earthquake shook the city": supported by Vaughan (l.3810-3826); Knighton dates it 21 May (l.16925-16929), and Vaughan puts a second shock about 30 May (l.3872-3876). (8) The Bible: the 1850 editors' view is told as one side; Pollard disputes the Wyclif share (F&M l.2319-2320, 2407-2420; POLLARD l.841-848, 968-972). (9) The census gives no birth year; the held lines give 1324 as his biographers' year, which Shirley calls a vague conjecture (VAUGHAN l.576-577; F&M l.933-953; SHIRLEY l.654-660). Owner: the census owner.
    - Census text to check, the live Kempis entry (not changed here). (1) Dates "1406-1471": 1406 is his investiture; the death notice puts him in his ninety-second year in 1471, so birth about 1380, editors only (CHRON l.1189-1193, 3413-3416; BENHAM l.492-493). (2) "copied books in one small house all his life" and "he stayed in that small house until he died": he was exiled with the brothers to Lunenkerc in Frisia from 1429 and sent to Bethany for "a year and two months" (CHRON l.1903-1924, 2024-2026). (3) "When Thomas was twenty, Florentius sent him": that is the death notice (CHRON l.3419-3421); his own Chronicle has him come to Zwolle for the pardons and ask to stay (l.1103-1106). (4) Benham "argued that Thomas had only copied it": Benham says Thomas copied it, that his note began the mistake, and argues for John Gersen, abbot of Vercelli (BENHAM l.511-521, 628-633). (5) "Jean Gerson": Atkynson prints "Iohn Gerson, Chaunceler of Paris" (INGRAM l.1175-1182). (6) "the most copied Christian book after the Bible", repeated in the Devotio Moderna entry's why, legacy and sources: no held line calls it the most copied book; Neale has it "read more widely than any other in the Western Church", Benham "the most popular religious work in Christendom" (NEALE l.4717-4719; BENHAM l.663-664). (7) "Ignatius of Loyola kept it on his desk", also in that entry: held in Oliver Manare's reply to Lancicius, which says Ignatius usually kept no books on the table of his inner room but the New Testament and Thomas à Kempis (IGN-SCR1, `ignatius-loyola_scripta-de-sancto-ignatio-tomus01-lat-spa-ita_1904.txt`, l.24338-24347); the census should name Manare as its witness. The Manresa line on the "Gerconzito" and the Exercises' advice to read it are held too (IGN l.2604-2605, 25087-25092). (8) "his name means 'of Kempen'": Duthoit's view only (DUTHOIT l.564-570). (9) "for a time served as sub-prior": twice, named in 1429 and elected again in 1448 at sixty-seven (CHRON l.1923-1924, 2379-2382). (10) "fourteen of his own works": 14 files carry the `kempis_` prefix, two are the disputed Imitation and one is his edit of Brugman's Lydwine (LYD l.119-129). (11) "The question is still argued": held as contested between Neale (1857) and Benham (1886) against and Ingram (1893) and Pohl (1902) for; no held line is later. Owner: the census owner.
    - Census text to check, movement entries. Lollardy: "Around two hundred and fifty handwritten copies of the Wycliffite Bible still survive" is not in the Forshall and Madden preface by any search of "two hundred and fifty", "250" or "number of copies"; the profile does not use it. The English Mystics and Devout: Rolle's voice line ("whose Fire of Love helped make devotional writing in English popular") needs the Latin origin said; the Fire of Love was written in Latin (COMPER l.3065-3068) and reached English in Misyn's translation of 1435 (COMPER l.10383-10390); Julian's voice line, "the first woman known to have written a book in English", is in no held line; "lived for decades shut in a cell" rests on no held length of enclosure, only a recluse alive in 1413 and Blomefield's strict recluse in 1393 (HARFORD l.469-473; WARRACK l.414-415); the legacy lines on the May feast and the wartime rebuilding of the cell are not held. Rhineland Mysticism: the Tauler line, "survive 'as delivered' only through listeners' transcripts", drops Winkworth's hedge that the eighty-four Strasbourg sermons were probably published in his life with his corrections (WINK l.907-917, 7033-7036); the Suso voice line, "wrote the Life of the Servant ... together with his correspondent Elsbeth Stagel", should say the Life is told in the third person, that Stagel wrote it down secretly and that he added to it after her death (KNOX l.521-525, 545-558); the Suso story caveat, "Suso's prologue is the only account of the book's making", is not true of the Töss book, where Johannes Meier retells it from the prologue (STAGEL l.1905-1911); edges[319] quotes Grube's OCR "13G5" where Grube gives 1365; edges[320] says Eckhart "had taken back any errors put before the pope", where the bull says he revoked the twenty-six articles "in a heretical sense" (DENIFLE-II l.35785-35796, 35810-35819). Devotio Moderna, "Geert Grote Gives His House Away": "in 1372 or 1374" (no held line gives 1372; Grube has 1374, BUSCH l.310); "an illness and the influence of a Carthusian friend" (Kempis tells the prior's counsel, FOUNDERS l.2252-2310, and the illness separately, l.3527-3530; the link is the census's reading); "spent three years at the charterhouse" (Kempis says three years of study and prayer before he began to preach, l.2643-2644); "two rooms" and "a ban on receiving anyone who wanted the house as a convent" (not in Langenberg's summary of the deeds, LANG l.2062-2092; the deeds are not held); "forbidden to preach the year before for attacking the clergy's concubines" (no held line gives the year; the friend's letter says the clergy procured the ban "as we suppose", FOUNDERS l.5139-5142); "died of plague in 1384 at forty-three" (Kempis has the forty-fourth year nearly done, CHRON l.3787; Busch says he caught the plague, BUSCH l.15805-15818); "the later lives by Thomas à Kempis and Rudolf Dier" (Dier is named only in Acquoy's notes, GROOTE l.944, 3768; his Life is not held). Owner: the census owner.
    - Library defects. Header-only years: "John Wyclif (c. 1330-1384)" in the headers of the Vaughan, Lechler and Matthew files (l.2-3), and "(1340-1384)" in the Groote file (l.3); no text line gives 1330, and 1340 is Arthur's and Opzoomer's. `knighton_chronicon-v2-lat_lumby1895.txt` header says "canon of Leicester, fl. 1363"; the canonry rests on the manuscript title (l.1427-1428) and "fl. 1363" is unchecked. Print or OCR slips in Wyclif's files: Vaughan l.4765 (death year), l.1333 ("1870" for 1370), l.4391 (assembly "1381"); Shirley l.2743 ("1381" for 1384), l.1044. `kempis_chronicle-of-mount-st-agnes_arthur1906.txt` prints "1422 (1432)" at l.1981 and "June (July)" at l.2327 (translator's brackets; John's death depends on the first), and "1479" for the bishop's enthronement at l.3723 (a misprint). `busch_chronicon-windeshemense-lat_grube1886.txt` l.5413 reads "Kerapis" and "frator" at the one contemporary line naming Kempis as author; l.15929 gives Grube's margin date 1381 against the text's 1384. The Comper header gives 1914 where the preface is signed 1913. The Horstman header's title-page year is unreadable (Comper cites 1895). The Arnold, Select English Works volume 3 gives 1871 only in its header. The three Julian files' headers give "born 1343", Underhill's reckoning, not a witness; Harford's header year 1911 is host metadata. Eckhart: the Evans header 1924 has no body line; Evans l.477-532 carries errors (the Inquisition at Venice, excommunication, "born before 1200", the 13 February "last date"); the heading of Denifle's document I misprints 1327 as "1397" (l.35069). Tauler: the Winkworth year 1857 is the header's; her preface numbers sermons to 27 for a book of 25 (l.959-967). Suso: the Knox title-page OCR has lost "Francis Knox" (l.25-27); l.10712-10713 is a library catalogue card, not a witness; the Bihlmeyer file's dates are heavily OCR-damaged ("ISdd" for 1366, l.8965). Grote: DIEP l.467 prints "r383"; the Acquoy note at GROOTE l.3770-3779 is heavily garbled. Owner: the Library thread.
    - Library wanted. Kempis's Latin Life of Gerard (Pohl's volume 7), which would let Arthur's "Kempen" and "Ghent" be checked against the Latin; Rolle's English Psalter commentary, which the Horstman item's content note says it holds but searches find only as references (l.2751); Tauler's Middle High German sermons (none is vendored); Colledge and McGinn, on which the Rhineland entry's Eckhart story rests, are not held. Owner: the Library thread.
    - Scan corrections (era 6 scan). Wyclif: birth c.1330 is the header's; the held biographers' year is 1324 (Shirley doubts it); the death year is F&M l.1031, not Vaughan's garbled l.4765; "last illness at Mass" is Shirley's, and Vaughan says only that he is said to have been giving out the bread; Hereford's books are said to run to Baruch (F&M) or to Daniel (Pollard l.841). Kempis: Busch's naming sits inside the dream before the death of John Vos of Heusden in 1424 (BUSCH l.5345, 5410-5416); Benham's case for Gersen runs to l.633. Rolle: the day, 29 September, rests on Horstman alone (HORST l.134, 2161); COMPER 2129-2131 is the Office quoting him, and his own account of the three years is COMPER l.5493-5541; the disguise is HORST l.215-220, not 213-242; the Fire of Love has no held year. Julian: l.247 is Harford's summary, and the copyist's heading is HARFORD l.466-473; WARRACK l.342 gives only "over thirty years of age" (the 1342 reckoning is l.444-445), and the Blomefield 1442 title is WARRACK l.250-254; no held line shows her teaching at her cell; Margery Kempe's visit is in no held file. Eckhart: the dates and trial rest on Evans's summary, but the acts and the full bull are held in DENIFLE-II l.34495-35835; the bull has no excommunication of Eckhart (l.35785-35805); Evans's "13 Feb ... last date alive" is contradicted by the act of 22 February (l.35464-35467); his death in 1327 is Denifle l.34962 and Denzinger l.15220, not the header. Tauler: the day, 16 June 1361, is Winkworth's alone (l.7171-7172) and is Inferential-Thin, not Widely Accepted; the 1300 birth is the header's, against three held sides (1290, 1294, 1300). Suso: 1295 comes from a catalogue card and the header; the held witness is Bihlmeyer (l.4977-4985, 5017); the death is Bihlmeyer's 25 January 1366, against Knox, Evans and Grube at 1365; the burial place (church or cloister) is contested (BIHL l.8987-8991; KNOX l.86-87). Grote: 1340 is Arthur's and Opzoomer's, not a primary witness's; the lay rule is Dietrich Engelhusen's (LANG l.160-162); "living at Zwolle" reads "wonende toe GroUe" (DIEP l.441), a different town; the legacy line at BUSCH l.4810-4812 is John Vos's speech as Busch reports it. Owner: the scan's next revision.
265. **Era 4 on the live tree: carried items (2026-11-14).** The 61 era 4 Who profiles (64 people; three entries are pairs) are in the census and on the site as text (data release 43). Source: Decision-Log, "Era 4 on the live tree" (2026-11-14); reviews in `Build/Ministry/Operations/Audits/2026-11-14_cft-era4-live/`.
    - Map years where the sources give none (Mark's pick, "Keep and log", 2026-11-14). Cogitosus 591 to 835 (Migne's 591 to Stokes's index). Severus ibn al-Muqaffa 950 to 1000 (the scan's tenth century). Antony of Choziba 620 to 640 (the scan). Beuno 616 (the founding of Clynog Fawr in the note in Rees). Paulus Emeritanus 610 (Migne). Symeon the New Theologian 1000 (the Philokalia compilers). Also from one anchor each: Nennius 858 (the prologue), Sebeos 661 (the end of his history), Adam 781 (the stele), al-Baladhuri 892 (his death), Eadburga 717 to 740 (Kylie's dating of the letters), Muirchu 695 to 699, Tirechan 664 to 683. Each card's dates line says what the sources give. Owner: the coordinator, if a different year is wanted.
    - Recording: none of the 61 entries has audio. They join the held recordings of Open-Gaps 218 and wait for an approved, capped run. The `audio/*.audio.txt` copies keep the profile text from before this release's changes (Agathon, al-Baladhuri, Beuno, Brigid). Owner: the coordinator.
    - Place ids: many places of these profiles have no census row to copy an id from (Jarrow, Lindisfarne, Whitby, Mainz, Toledo, Baghdad, Reims and others), so they show the name with no "today in" country. No id is invented. Owner: the map build slice, with the Library thread.
    - Carried from 255: `regions` on each person entry is its home tradition's (al-Baladhuri's is Middle East); the A5 status for a person told within no tradition. Owner: the map build slice.
    - Martin I is told within the Heraclian entry only; if a Roman era 4 movement is added, Martin takes it second (Open-Gaps 256). Owner: the map Who build slice.
    - Census text not changed here, below the reading target before this release and touched only by a phrase: the why fields of the Macedonian, Syriac Orthodox under Islam and Coptic under Early Islam entries, the Heraclian longDescription and the Macedonian legacy. Bede's teaser, which is his approved card's knownFor (reading ease 59.1), was kept as approved (review round 2, M5). The Silk Road longDescription says "Luminous Religion" where Wylie's held English says "Illustrious". Owner: the coordinator.
    - Wanted, new: Willibald's Life of Boniface (its chapter 6 is the oldest account of the oak at Geismar); an English of the Record of Maximus's trial. Owner: the Library thread.
    - Library items and scan corrections of 254 and 256 to 262, and the 255 items not closed (recording, place ids, map years, regions, status words), are carried unchanged. Owner: the Library thread and the coordinator, as each entry names.
    - Open-Gaps 50's Alopen entry ("636, not 635") is not edited; the held stele gives 635 (Open-Gaps 259). Owner: item 50's owner.
    - `tools/check_tree_domains.mjs` reports 404 for the new tree pages until the site is deployed; check it again after the deploy. Owner: the coordinator.
    - Open-Gaps 217 (caps, major mark, placement) is carried. Owner: the map build slice.
266. **Major councils, era 4: people with no verdict, the missing Roman entry, a witness kind, Library items, and scan and census corrections (2026-11-14).** The six era 4 council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era4/`, written to `Council_Profile_Pattern.md`: the Lateran Council of 649, the Synod of Whitby (664), the Third Council of Constantinople (680-681), the Quinisext Council (691-692), the Second Council of Nicaea (787) and the Councils of Constantinople in the Photian affair (861-880). None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217). Source: `Build/Ministry/Operations/Audits/2026-11-14_council-profiles-era4/`; Decision-Log, "Major councils, era 4" (2026-11-14).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id. Lateran: Constans II, Stephen of Dor, Maurus of Ravenna, Amandus of Maastricht. Whitby: Oswy, Alfrid son of Oswy, Agilbert, Eanfleda, Tuda, Eata, Agatho the priest, James the Deacon, Romanus. Constantinople 680-681: Constantine IV, Agatho of Rome, Leo II, George I of Constantinople, Macarius of Antioch, Polychronius. Quinisext: Justinian II, Sergius I, Paul, Peter of Alexandria, Anastasius of Jerusalem and George of Antioch (the signers of 692), Basil of Gortyna, Zacharias the protospatharius, John of Porto, Boniface the counselor, John VII, Constantine. Nicaea: Constantine VI, Hadrian I, Basil of Ancyra, Constantine of Constantia, Sabbas of the Studium. Photian councils: Ignatius of Constantinople, Hadrian II, John VIII, Basil I, Michael III, Anastasius the Librarian, Radoald of Porto and Zacharias of Anagni. The era 4 scan's council row "Photius (WHO), Ignatius, Boris (LISTED)" (`Who_Scan_Era4.md` l.224) can be read as LISTED for Ignatius; it needs a ruling. Theophanes the Confessor, Theodore the Studite and Mark of Ephesus are WHO with no profile yet, so they show with no id. Owner: the coordinator, for a Who scan verdict.
    - No Roman entry for era 4. The census has no Roman or papal tradition between `roman-church-gregorian` (ends 604) and `latin-papal-church-gregorian` (begins c. 1049). Rome called the Lateran synod, sent envoys to 680-681, 787 and the Photian councils, and refused the Quinisext canons, but none of these can name a Roman tradition id; Rome's part is told in the entries' outcome and record. Owner: Mark, a portfolio question for the census.
    - Pattern gap: no witness kind fits a writer earlier than the meeting. Columbanus's Easter letters (PL 80) give the Irish Easter case some sixty years before Whitby; the entry files them as a later narrative with a note that they are not a witness to the synod. Owner: the coordinator, for the pattern.
    - Not held, and noted in the entries or `records.json`: the full acts of Nicaea II and their signatures (Mansi, tomus 12-13); the Caroline Books, Hadrian I's reply to Charlemagne and Ignatius the Deacon's Life of Tarasius; Hefele's volumes past 451; the Latin abridgment of the council of 861 in Cardinal Deusdedit's collection; Hergenröther's and Dvornik's studies of Photius, and Photius's letters and Mystagogy; Cummian's Easter letter, the Annals of Ulster and the Anglo-Saxon Chronicle; Bede's chronicle (his "erratic synod" reaches us only through Sirmond's preface in PG 99). None of the six profiles is thin for want of them. Owner: the Library thread, to weigh for the wanted list when the fill resumes.
    - Library headers. `paulus-emeritanus-braulio-sisebut-pl80-lat_migne1863.txt` does not say it holds Columbanus's letters (l.20270 ff.). `byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt` holds Stephen's, Fridegod's and Eadmer's Lives of Wilfrid, which its name hides. The content note of `mansi_sacrorum-conciliorum-collectio-tomus-11-lat_welter-facsimile1901.txt` says the volume ends with the life of Conon; it holds the whole Trullan record (l.88598-96798). Owner: the Library thread.
    - Scan corrections. Councils scan, era 4: the Lateran acts begin at Mansi 10 l.88609 (not "~96715"), its members were bishops and the Greek monks came by petition, and Maximus's presence is contested; Whitby's "The English, Irish and Welsh churches were brought onto the Roman Easter" overstates what Bede and Stephen show (Oswy's Northumbrian church), Stephen's Life is held, and Wilfrid (`wilfrid-of-ripon`) and Cedd (`cedd-and-chad`) are WHO; for Constantinople 680-681, `heraclius` and `maronite-christianity` do not mention the council, and the Maronites' later holding to one will is contested; for the Quinisext, `roman-church-gregorian` ends in 604 and the census names the council in four places, not two; for Nicaea, the census tells the council in seven entries and six edges, not about twenty; the Photian rows say Mansi 15-17 are not held, but they are, and Denzinger and the Pedalion hold the canons of 869-870 and 861. Who scan, era 4: Theophanes the Confessor is marked WANTED and not held, but his Chronographia is held; Hatfield is given as 17 October 680, after Giles's mistranslation, where Bede's Latin gives 17 September (Plummer l.24162-24163, 'sub die XV Kalendas Octobres'); the Tarasios row's l.38101 is Percival's citation, not the letter; the Photian council row (l.224) says Mansi 16 and 17 are not in the Library, but both are held (`mansi_sacrorum-conciliorum-collectio-tomus-16-lat_welter-facsimile1902.txt`, `mansi_sacrorum-conciliorum-collectio-tomus-17-18-lat_welter-facsimile1902.txt`). Owner: the coordinator. The audits are not edited.
    - Census text, to check. `byzantine-imperial-church-heraclian-iconoclast` says Constans II imposed the doctrine of one will; the Typos forbade all argument over one will or two (Mansi 10 l.103680-103687). `sophronius-of-jerusalem` cites the Lateran acts for Maximus's letter to Peter, which Mansi prints outside the acts (col. 690). `byzantine-imperial-church-macedonian` cites "conciliar records of 861/867", which do not survive, and says Bulgaria's choice is in the acts of 869-870; it came three days after the last session (the Book of the Popes; Anastasius's preface). The edge `latin-church-of-outremer--maronite-christianity` says William of Tyre's own text is not held; it is held (`william-tyre_historia-rerum-in-partibus-transmarinis-gestarum-v2-lat-fra_rhc1844.txt` l.26911-26979). `gregory-of-nyssa` says the second council of Nicaea called him "Father of Fathers"; no held extract of the acts has it. `carolingian-reform-christianity` does not tell the image dispute or Frankfurt's rejection. The Photius Who records label Mansi 17 l.53399-53432 the sixth session; it is the seventh (l.53309). Owner: the coordinator, for the census text and the map build.
267. **Era 6 Who batch 2: the river count, census text, names with no held time, Library items (2026-11-15).** The eight batch 2 profiles (Catherine of Siena, Bridget of Sweden, Bernardino of Siena, Angelo Clareno, William of Ockham, Gregory Palamas, Gregory of Sinai and Nicholas Cabasilas) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch2/`. None is a census person entry or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era6-batch2/`; Decision-Log, "Who profiles, era 6 batch 2" (2026-11-15).
    - Major caps. All eight are major. Greek East & Orthodoxy holds 3 era 6 majors (Palamas, Gregory of Sinai, Cabasilas). Latin West & Catholicism holds 13 against the 5 the map shows: batch 1's John Wyclif, Thomas à Kempis, Richard Rolle, Julian of Norwich, Meister Eckhart, Johannes Tauler, Henry Suso and Geert Grote, and this batch's Catherine of Siena, Bridget of Sweden, Bernardino of Siena, Angelo Clareno and William of Ockham. Which five the river shows is Mark's pick, as for eras 4 and 5 (Open-Gaps "Who re-score, eras 4 and 5", 2026-11-14). Owner: Mark, through the coordinator.
    - Census text to check (not changed here). Hesychasm & the Palamite Synthesis and the Byzantine entries say the synods "settled" or "ruled" the dispute, where Mansi heads the 1351 acts "Pseudo-synodus" and Combefis, after Gregoras, says no doctrine was debated in 1341 (MANSI26 l.12060, 19592-19597). "Palamas Among the Turks" tells a storm, where Gregoras has the ship becalmed and taken by pirates. The Hesychasm entry's "the layman" Cabasilas tells one side: Kantakouzenos calls him still a layman in 1353; Fabricius and Gass make him archbishop of Thessalonica; Martin Jugie (1926) finds no serious proof of the see (PO19 l.39892-39895). The Fraticelli and Franciscan Order entries give the History of the Seven Tribulations to Clareno as settled, where it is Ehrle's attribution, followed by Eubel and Oliger, and doubted by Affò, Richard and Tocco. The Observant Reform entry's held-up IHS tablet, and Benedetto's shorthand and dawn walks, have no held line. The Latin Papal Church story "Be a Man, Father, Arise!": the death year, the wording, the letter count, the September departure and the needle story differ from the held lines (Part A of the round 1 review). The Franciscan Order story: the galley "provided by" Louis, the "securely documented" date, the "four years" and the "rest of his life at Munich" are not held as told (Part C of the round 1 review). Owner: the census owner.
    - Names with no held time or role, kept under the common-name standard: Sigonius, Raynaldus's source for the Bologna story; Raynaldus himself; Richard, who doubts Clareno's authorship, has a year (1884, from Ehrle's note, EHRLE2 l.5856) but no first name or role; Nicolaus Minorita; and Müller, whom Carlini names only in a note beside Riezler, "e il MuLLER" [OCR] (CARL l.6278). Owner: the Library thread.
    - Ehrle's year list. Ehrle, after Papebroch, gives 1317, 1337 and 1348 as the years in which the Friday after Pentecost fell on 13 June (EHRLE1 l.27792-27795). A Julian Easter computation gives 1337 and 1348 but not 1317, so the 1317 may be a slip. The card keeps the list as printed. Owner: the scan's next revision.
    - Library wanted: Kallistos's Life of Gregory of Sinai; Raymond of Capua's full Legenda of Catherine; Bridget's Life by her confessors and Books VI to VIII of the Revelations; Ockham's Latin "flint" letter and his philosophical works; Palamas's letter from captivity and the full Triads; Maffeo Vegio's Life of Bernardino; Louis Petit's 1918 article on the Synodikon of Thessalonica, which Jugie cites. Owner: the Library thread.
268. **Major councils, era 5: people with no verdict, census parties with no entry, census text to check, Library items, and scan corrections (2026-11-15).** The three era 5 council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/`, written to `Council_Profile_Pattern.md`: the Council of Clermont (1095), the Fourth Lateran Council (1215) and the Second Council of Lyon (1274). None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217). Source: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era5/`; Decision-Log, "Major councils, era 5" (2026-11-15).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id. Clermont: Urban II, Adhémar of Le Puy, William of Orange, Raymond of Toulouse, Peter the Hermit, Hugh of Grenoble, Pontius of La Chaise-Dieu, Hugh of Lyon, Aldebert of Bourges, Baldric of Bourgueil, Guy of Vienne, Peter of Pamplona, Robert of Flanders. Henry IV and Gregory VII are left off the Clermont click: neither took part. Lateran IV: Almaric, Fulk of Toulouse, Honorius III, Dionysius O'Lonargan of Cashel, Conar O'Heney of Killaloe, Eghdon Mac Gilluir. Lyon: Gregory X, Jerome of Ascoli, Eudes Rigaud, Paul of Tripoli, John of Balastri, Germanos, Theophanes of Nicaea, John Bekkos, Joseph I, Euthymios of Vatopedi, Andronikos II, Clement IV, Martin IV. Dominic, Joachim of Fiore, Francis of Assisi and Thomas Aquinas are WHO with no census person entry, so they show with no id. Owner: the coordinator, for a Who scan verdict.
    - No Roman gap in era 5: `latin-papal-church-gregorian` (c. 1049-1300) covers Rome at all three councils. Parties at the councils with no census tradition at the date, the same kind of gap as era 4's missing Roman entry: the Irish church in 1215 (`medieval-irish-christianity` ends in 1169; the Four Masters and, in O'Donovan's notes, the Annals of Ulster tell of Irish bishops who died at Rome or on the way home); the Latin church of Constantinople under the Latin emperors (1204-1261), whose patriarch canon 5 ranks first after Rome; the Amalricians, condemned in canon 2; the Augustinian Hermits, the Friars of the Sack and the Apostolic Brethren, dealt with by Lyon's decree on the mendicant orders; the Tatar envoys at Lyon; La Chaise-Dieu, whose abbot made a concord at Clermont. `the-dominican-order` begins in 1216, a year after Dominic came to Lateran IV to ask for the order. Owner: Mark, a portfolio question for the census.
    - Pattern gap, again: no witness kind fits a writer earlier than the meeting. Joachim of Fiore's letter of 1200 and his Psalterium are the condemned party's own voice at Lateran IV; they are filed as later narrative with a note, as Columbanus was for Whitby (Open-Gaps 266, "Major councils, era 4", 2026-11-14). Owner: the coordinator, for the pattern.
    - Census text, to check. The edge `latin-papal-church-gregorian--latin-church-of-outremer` drops canon 2's condition at Clermont, "pro sola devotione, non pro honoris vel pecuniae adeptione" (Mirbt l.11226), and its "Latin clergy filled the new sees in the East" rests on two held cases (Dulaurier's notes, Matthew of Edessa l.15578-15584). `latin-papal-church-gregorian` (the Canon 68 story) gives "more than four hundred bishops and eight hundred abbots" and seventy-one constitutions; no held line gives 800 abbots or the number of canons, and canons 67-70 are not held; the held counts are Hethum's 422 bishops and 72 archbishops and al-Duwayhi's 411 bishops. `maronite-christianity`: "to settle its terms" has no held line; the pallium rests on al-Duwayhi alone (second witness); the bull Quia divinae sapientiae is not held; the patriarch's attendance is held in Jacques de Vitry (Historia l.10741-10747), so the edge `latin-papal-church-gregorian--maronite-christianity`, which says it rests on modern historians only, can name a held witness. `innocent-iii`: "summoned the Fourth Lateran Council in 1215"; the one held line on the summons dates the letters to 1213 (Pulkava, Emler's note, l.14999-15001). `byzantine-church-after-1054`: "needed help from the West" is the view of the modern Recueil editors (rhc-armeniens t2 l.54168-54172), while the held later witnesses (Pseudo-Brochard, Gennadios, the chronicle under Sphrantzes's name) say Michael VIII sought to ward off a Western attack; its sourcing names "Lyons 1274 acta", which are not held (three texts in extract only); the story "Michael VIII Punishes the Anti-Unionists" rests on Pachymeres and Michael's autobiography, neither held, says the church refused him a Christian burial where the held witnesses differ (Boulliau on Doukas l.32499-32501: no funeral pomp; Creyghton l.3090-3094: cast out unburied; Guillaume Adam l.63744-63748: the monks' oath), and its "with the exception of a compliant patriarch" sits against the Recueil note that Bekkos at first resisted (l.63805-63812). Owner: the coordinator, for the census text and the map build.
    - Not held, and noted in the entries or `records.json`: Mansi tomi 20, 22 and 24 (the acts of all three councils; one page of tomus 22, the Notitia, is reprinted in PL 214); Hefele's and Hefele-Leclercq's volumes V and VI; Fulcher of Chartres, Robert the Monk, Guibert of Nogent, the Gesta Francorum, Bernold of Constance and Urban II's letters (PL 151); canons 13 (in the acts) and 67-70 of Lateran IV, the summons Vineam Domini, Innocent III's council sermons, Roger of Wendover, Richard of San Germano and Peter of Vaux-de-Cernay; Pachymeres, Akropolites, Gregoras vol. 1, Bekkos's works (PG 141), the Lyon decrees Zelus fidei and Religionum diversitatem, and Salimbene's Latin chronicle for 1274. None of the three profiles is thin for want of them. Owner: the Library thread, to weigh for the wanted list when the fill resumes.
    - Library headers. `stephen-harding_charta-caritatis-and-exordium-in-pl166-lat_migne1894.txt` does not say it holds Albert of Aachen's and Baldric of Bourgueil's histories of the crusade (l.27607 ff., l.77237 ff.) or Walter of Thérouanne's Life of Charles the Good. `anselm-canterbury_opera-with-eadmer-historia-novorum-pl159-lat_migne1903.txt` does not name Hugh of Cluny's Life, letters and charters, among them the act made at Clermont (l.74872 ff.). The content notes of `liber-pontificalis_texte-introduction-commentaire-t2-lat-fra_duchesne1892.txt` (the life of Urban II, l.71346), `le-couteulx_annales-ordinis-cartusiensis-v1-lat_1887.txt` (Urban's letters for Hugh of Grenoble, l.13238-13319), `innocent-iii_opera-with-gesta-innocentii-pl214-lat_migne1853.txt` (the Notitia from Mansi XXII 687, l.956-1072), `acta-sanctorum_augusti-tomus-1-lat_1750.txt` (the Bollandist extracts and Bartholomew of Trent's Life of Dominic) and `acta-sanctorum_maii-tomus-6-lat_1739.txt` (Honorius III's letters and Joachim's letter of 1200, interleaved in two columns) leave those items out. `gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt` does not say it holds the annotations on vol. 1. `sphrantzes-cananus-anagnostes_chronicles-grc-lat_bekker1838.txt` holds the longer chronicle printed under Sphrantzes's name. Owner: the Library thread.
    - Scan corrections. Councils scan, era 5: Clermont is named in the census (the edge above), Albert of Aachen, Baldric and William of Tyre are held, Lambert of Saint-Omer's notice (Liber Pontificalis t1 l.47693-47697) gives 310 bishops, and the Beauvais record of 1114 (Mansi 21) holds further Clermont canons; the Mirbt range is l.11220-11233; `military-religious-orders-templars-hospitallers` has no held tie to Clermont, and `latin-papal-church-gregorian`, `cluniac-reform-monasticism` and `byzantine-church-after-1054` are missing. Lateran IV: `innocent-iii` is a person entry, not a tradition; Jacques de Vitry holds the Maronite patriarch's attendance; Mirbt's dates (11-30 November) are his; Denzinger also holds canons 4, 5 and 21, and canon 2's condemnation begins at l.13942. Lyon: `the-waldensians` is a place-name match with no held tie; the Denzinger range is l.14473-14646, the Mirbt decree l.13349-13427, the Glassberger narrative l.7150-7310 with l.7319-7332 and 7360-7367, and the opening at l.7157-7158 with the editors' 1 May at l.7205; Thomas Aquinas (WHO after the rescore) and Gregory X (not scored) are missing from the participants. The register's "Mansi 21 not held" (Lateran I and II) and Troyes "WANTED" are out of date: Mansi 21 is held. Who scan, era 5: the Lateran IV row's absences for Jeremiah al-Amshitti are corrected by Vitry; the Hugh of Cluny "no Life held" note is out of date (PL 159 l.64857). Owner: the coordinator. The audits are not edited.
269. **Era 4 Who batch 9: John of Damascus's census year, the river counting rule, the Kyiv pair's map era, re-score corrections, Library items (2026-11-15).** The seven batch 9 profiles (John of Damascus, Theodore the Studite, Cyril and Methodius, Antony and Theodosius of the Kyiv Caves, Anskar, Rimbert and Clement of Ohrid) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch9/`. John of Damascus is a live census person entry and is not changed here; the other six are not in the census or on the site. Batch 10 takes Stephen the Younger and Nikephoros I, split off from the re-score's batch 9 to hold the writing quality. Source: `Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch9/`; Decision-Log, "Who profiles, era 4 batch 9" (2026-11-15).
    - Census text to check, not changed here. John of Damascus's two person rows carry the year 730, and the Iconophile Byzantine Monasticism row sets it on a quotation from the Exposition of the Orthodox Faith (Salmond, `npnf209` l.36233-36234). In the held sources 730 is Le Quien's date for the second speech on the images (PG 94 l.32111-32115, where the scan reads "750", tied to Germanus's deposition); Fabricius dates the Dialectica, the first part of the work that holds the Exposition, after 743 (PG 94 l.942-943). Owner: the census owner, at era 4's completion release.
    - The river counting rule. By the census Who rows, Greek East & Orthodoxy era 4 held five majors and Latin West & Catholicism ten. John of Damascus, Theodore, and Cyril and Methodius make the Greek East eight, and Anskar makes the Latin West eleven. By era 4 card traditions the counts are nine and ten, since Humbert of Silva Candida's row sits in the Latin West at 1054 while his only era 4 card tradition is the Macedonian-era Byzantine church. The map shows five per river; which rule counts, and which five, is for the map build slice and Mark (Open-Gaps, "Map Who build slice: caps, major mark, placement", 2026-11-11). Owner: the map build slice.
    - Antony and Theodosius go on the map in era 5 and "Kievan Rus' Christianity, 1054-1240" (coordinator's call, 2026-11-15, by the active-year rule; Mark may overrule), with active year 1062, the move above ground in Nestor's Life. Their files stay in the era 4 batch. Their card's second tradition, "Kievan Rus' Christianity", covers Antony's settling after 1051 and, in the 1462 Paterik, his stay under Vladimir and Theodosius's tonsure in 1032. Owner: the release worker for era 4's completion release.
    - Clement of Ohrid's needs-ruling is closed by Mark's pick, "Keep as Who, dispute told (Recommended)" (relayed by the coordinator, 2026-11-15).
    - Re-score corrections (Rescore.md rows, not edited). John of Damascus: l.616-621 of the PG 94 file are Fabricius's words, not Le Quien's, and "post medium saeculi decimi" dates the Life's author; Anastasius's Latin makes John Mansur's grandson; the image speeches are held only in Greek and Latin. Theodore: "cum ipso vixit" (PG 99 l.3725) is the Sirmond preface's claim about the Sirmond Life, which Mai denies is Michael's; Naukratios wrote a letter, not a Life. Cyril and Methodius: the Salzburg account is at Ginzel l.13130-13722 and Industriae tuae at l.13878-13982; no held line names Methodius's jailer or calls him "of Sirmium", though an editor's note to the Salzburg account says John VIII restored his diocese in place of the old see of Sirmium (Ginzel l.13166-13173). Clement: the Monitum reports Miklosich and leaves the judgment to the reader rather than arguing it; Patrologia Graeca 111 (l.243-244, l.36942-36947) places the Life about the middle of the tenth century; the Life dates his burial, not his death; the Saint Panteleimon dedication is Nikodemos's, not the Life's. Antony and Theodosius: no held line gives Antony's death year, and the Paterik's base text begins only partway into its seventh discourse. Rimbert: the Turholt birthplace is an unsigned note in Waitz's edition. Owner: the re-score's next revision.
    - Library, wanted (the fill is paused until Mark's reset): an English of John of Damascus's speeches on the images; the acts of Nicaea II (Mansi tomi 12-13); the Life of Constantine (Cyril) in any language; the Slavonic Life of Methodius; any work of Clement of Ohrid, and the Short Life ascribed to Demetrios Chomatenos; a complete scan of the Life of Rimbert (the held Waitz scan ends in chapter 23, l.5422); Robinson's English has no Life of Rimbert. Owner: the Library thread.

270. **The map, direction B (data release 44): what the build leaves open (2026-11-14).** Source: Decision-Log, "The map, direction B: a quiet map and a Who list" (2026-11-14); the review rounds in `Build/Ministry/Operations/Audits/2026-11-14_map-direction-b/`.
    - The design worker's notes, as written. C7: "Phone bar words are 12px, the floor." C8: "A desktop opens with 40 traditions named where live named about 340 (the zoom-layer design). I explained this to Mark; he made no change." C9: "The stretch makes dates within an era unevenly spaced; cards keep the true dates." C11: "The era title does two jobs: on the simple overview a tap goes in; when zoomed in it opens the era card. The information mark and the strip always open the card." Owner: the map.
    - C10, not tested: real touch (pinch, flick), a screen reader on the new bar, list and era marks, speed on an older phone (the page is 7.9 MB), and audio. Tested since: overlaps with a Who open, 0 in all 29 river-eras on desktop and phone; keyboard focus and spoken labels in Chromium, by script. Owner: the map.
    - The Persecuted Church record (`persecuted-church-worlds-of-the-communist-era-in`) sits on the Eastern Catholic river (laneOrder 3.5), though its own lane field calls it a Greek East and Protestant span. The river shows no common name until this is settled. Mark approved "Greek and Latin · Eastern Catholic" on the understanding that, once Church & Empire left, the name is true for the whole river. A tradition there that spans Greek East and Protestant makes that not quite so. Settle the record's place and the river's common name together. Owner: the census owner, with Mark.
    - The stories' "How it connects" text shows builder notes to visitors. All 62 map stories carry a `relationsSummary`, shown under "How it connects". 58 of them show record slugs or builder lines, or both: 56 have slugs and 44 have builder phrasing. Examples: "anatolian-church-third-century (c. 240–312) is the same province's church" (plinys-two-ministrae); "whose record sits at tertullian-s-voice" (perpetua-and-felicity); "though that record never names Abitinae or Saturninus" (abitinian-martyrs). Under CLAUDE.md, process notes on a live surface are a defect. Its own job after release 44, at the coordinator's call (2026-11-14). Release 44 cut only the clauses that cited the removed river notes (scillitan-martyrs, elcho-island-revival, plinys-two-ministrae, simeon-on-the-pillar, juliana-and-corpus-christi). The removal check also found plinys-two-ministrae's first clause false ("Predates every Anatolian movement on the map by more than a century"; Montanism, from 165, and the Scattered Households of Asia Minor, from 70, are on the map). It was cut in release 44 at the coordinator's call (2026-11-15), which Mark may overrule. Owner: the map, with the census owner.
    - People's census dates. 69 of the 190 people have a bare range that reads as a lifespan but is often an office or active span (Martin Luther 1517-1546, Augustine 386-430, Gregory VII 1073-1085). Write the kind of span into each such `dates` string, checked against its sources. Four more lines read badly in the Who list: Olympias, Sozomen, Marius Mercator, Valentinus. Owner: the census owner.
    - The five imperial councils (Arles 314, Nicaea, Sardica, Constantinople I, Chalcedon) do not list Church and Empire in `council.rivers`. Owner: the census owner.
    - B5. Three movements across churches have no river link and always show: The Rescue Mission Movement, Promise Keepers & the Christian Men's Movement, and The Church Struggle against Apartheid. Owner: the census owner, if links are found.
    - The census `statusMeta` word for built worlds is "Open for conversation". The map shows "Conversations coming soon" while conversations are off; the census word is still the one other surfaces read. Owner: the census owner.
    - On a phone, a river-era taller than the screen leaves some of its names off screen until panned (27 of 107 shown names at the opening Who zoom); every name is also in the list. Owner: the map.
    - The Representative picture switch (A14, C5) is for when conversations return; the pictures were removed from the map and are in git history (the map before this release). Owner: the map, when Mark asks.
    - Open-Gaps 217 is met or replaced by A6 to A8: caps of 4 and 5, majors only, the major mark in the data, the list for "more", and names tied to their traditions.
    - Noticed by the round 3 targeted check, not changed: Braulio of Zaragoza's census date prints as "bishop c. twenty years; at councils 633-638"; Hebrew Roots' "c. 1990s-c. 2010" reads "about 1990s"; the tree pages print raw census dates ("1880s-c. 2010"), since the map's date formatter does not reach them; era 9's header leaves out the Global Revival river because 1904 Revivals is filed under era 10. Owner: the census owner, and the tree pages for the formatter.
    - Left open by the last targeted check (`Review_r3-fixcheck3.md`, 2026-11-15), all MINOR:
      - One connection's feedback key is 124 characters. `feedback.js` cuts keys at 120, so it still posts and stays unique, but no longer names its edge in full. Edge ids join two ids, so more long keys can come.
      - A failed Send in the feedback form, by keyboard, drops focus to the page body. Send still uses `disabled`.
      - At browser text sizes of 20-24px, the Who chip's label can shrink to its "×" on some wide screens. It is the coordinator's call under A20's one-row bar, and Mark may overrule it.
      - At 24px on phones under 369px wide, the Rivers and Key panels are wider than the screen, as before this release.
      - The Pliny story's "the same province's church" is loose: the third-century Anatolian record covers Pontus and Lycia.
      - A river whose only link is to a movement across churches would read "inside the river". No river does this today.
      Owner: the map.

271. **Major councils, era 6: people with no verdict, census parties with no tradition, census text to check, Library items, and scan corrections (2026-11-15).** The two era 6 council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/`, written to `Council_Profile_Pattern.md`: the Council of Constance (1414-1418) and the Council of Basel–Ferrara–Florence (1431-1445), one joined profile. Neither is in the census or on the site; councils go on the site with the map build (Open-Gaps 217, "Map Who build slice", 2026-11-11). Source: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era6/`; Decision-Log, "Major councils, era 6" (2026-11-15).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id. Constance: Francesco Zabarella, Jean de Brogny, Andrew, elect of Poznań, Carlo Malatesta, Giovanni Dominici, John of Chlum, Michael de Causis, the bishop of Lodi, Duke Ludwig, son of Clem of Bavaria, Frederick of Austria, Gregory, metropolitan of Kiev (Gregorius Semivlach in Harasiewicz), Richard, bishop of London, John of Heusden, Paulus Wladimiri, John Falkenberg, Jean Petit. Florence: John VIII Palaiologos, Joseph II of Constantinople, Julian Cesarini, Nicholas Albergati, Louis Aleman, Felix V, John of Ragusa, Antony of Heraclea, Dorotheos of Mitylene, Metrophanes of Cyzicus, Isaias of Stauropolis, the Georgian envoys (a bishop and a lay prince), Constantine, catholicos of the Armenians, the Armenian envoys Sargis and Joachim, Andrew, abbot of Saint Antony's, John, the Coptic patriarch, Nicodemus, abbot of the Ethiopians in Jerusalem, Abdallah, archbishop of Edessa, Timothy, metropolitan of the Chaldeans, Isaac, the Maronite envoy, Ambrogio Traversari, Basil II of Moscow. Zara Yaqob is WANTED. The WHO people with no profile or census person entry show with no id: at Constance, Hus, Jerome of Prague, Mladoňovice, Richental, Gerson, Fillastre and d'Ailly; at Florence, Mark of Ephesus, Bessarion, Scholarios, Syropoulos and Aeneas Silvius Piccolomini. John Wyclif and Bridget of Sweden carry their ids. Bernardino of Siena is left off the Florence click: no held line puts him at Ferrara or Florence. Owner: the coordinator, for a Who scan verdict.
    - Isidore of Kiev's verdict differs within the era 6 Who scan. Its main table gives STORY (`Who_Scan_Era6.md` l.226), and the Florence entry follows it. Its event rows still say "Isidore LISTED" (l.268, l.271). Open-Gaps 233, "Who scan records cleaned" (2026-11-12), closed his change order with him STORY, so the event rows are out of date. Owner: the coordinator. The audits are not edited.
    - No Roman gap in era 6: `latin-papal-church-avignon-to-lateran-v` (1300-1517) covers Rome at both councils. Parties at the councils with no census tradition at the date. Constance: the Greek-rite metropolis of Kiev under Lithuania (Gregory; `muscovite-monastic-christianity` is Moscow's, and no Ruthenian or Lithuanian Orthodox entry covers 1418); Benedict XIII's obedience; the Dominicans (Giovanni Dominici, John of Podiomitis; `the-dominican-order` ends in 1300); the Bridgettines (the Scandinavian request, Richental l.3027-3058). Florence: the Georgian church (no entry between 1245 and 1650); the Copts (none between 1300 and 1517); the church of the Syrian patriarch Ignatius (`syriac-renaissance` ends in 1300); the Melkite patriarchates; the sees of Moldo-Wallachia and Trebizond in Syropoulos's list; the Camaldolese, Augustinian and Vallombrosan orders, whose heads signed (Mansi 31 l.97190-97197); the Dominicans again, through John of Ragusa and Torquemada; and the Basel party after the transfer. `church-of-the-east-timur-to-hakkari` is only an approximate fit for the Chaldeans of Cyprus. The census has no place id for Constance, Basel, Ferrara, Florence or Lausanne. Owner: Mark, a portfolio question for the census; the place ids, the coordinator, for the map build.
    - Census text, to check: Constance. `the-hussite-and-bohemian-brethren-movement`, the story "The Sixth of July at Constance", says "the council met in the cathedral with the emperor Sigismund presiding". That tells one side as settled: Mladoňovice has the king presiding (Palacký's Documenta l.17090), and the acts name Jean de Brogny (Mansi 27 l.77804-77816). Sigismund was not yet emperor; the held lines call him king of the Romans. The story's "seven bishops" follows Mladoňovice (l.17246), but the acts' sentence names six (Mansi 27 l.78655-78661). Its "attended every session" has not been checked against a held line. The entry's `longDescription` says "the Council of Constance burned him as a heretic"; the council condemned Hus and handed him to the secular court, which burned him (Fillastre l.2577-2585; Mansi 27 l.78663-78666). `latin-papal-church-avignon-to-lateran-v`: its `why` says "The council deposed the rivals", but Gregory XII resigned (Fillastre l.2412-2418). Its `longDescription` says that by the 1440s the question "was settled in the papacy's favor", which is stronger than Bannwart's note in Denzinger (l.16208-16224): a papal rejection in 1439 and a qualified reception in 1446. Its `legacy` says "In 1870 the First Vatican Council turned the claim down once more", and the held text of Pastor aeternus (Denzinger) does not name Constance. Owner: the coordinator, for the census text and the map build.
    - Census text, to check: Florence. `byzantine-church-palaiologan`, `why`: "the Byzantine emperor and patriarch signed a union with Rome". The patriarch died before the signing (Mansi 31 l.94680-94684; Syropoulos l.45231-45232, "mortuus ante subscriptionem"), and the signed list has no patriarch (Mansi 31 l.96984-97420). "In exchange for military help" (`why` and `longDescription`) is a witness's view; no decree states an exchange. "Mark of Ephesus alone among the Greek bishops present refused to sign": Syropoulos has Isaias of Stauropolis and the Georgian envoys evade signing (l.47672-47681, 44065-44070). The story "The Pope Asks Whether Mark Has Signed" says the patriarch left "a note in favor of union that Syropoulos suspects was written for him"; no held line of Syropoulos says so, and his account of the death is silent on the note (l.45200-45244). Its teaser's "eighteen months of debate" is the narrator's own sum, from 8 January 1438 to 6 July 1439. `armenian-cilicia-after-the-kingdom` (1300-1441) does not mention the Armenian union of 1439, which the acts hold (Mansi 31 l.99049-99062), as does Issaverdens. Owner: the coordinator, for the census text and the map build.
    - Not held, and noted in the entries or `records.json`: Basel's session acts (Mansi tomi 29 and 30); a roll of Basel's members at any time; a signed list of those who voted Haec sancta or the main decrees at Constance; a witness of the time to the burning of Wyclif's bones; Luther's words at Leipzig in 1519 in full; a Coptic-side witness to the union of 1442 (Renaudot was searched); an Ethiopian text of the time on the envoys (Perruchon says Zara Yaqob's chronicles are silent on Florence); an Armenian text of 1439 (the envoys' address is held only in Latin, Mansi 35); a Russian text of the time on the rejection, which rests on Mouravieff (1838) and Harasiewicz (1862). Wyclif's own works are held but were not matched to the forty-five articles, and Syropoulos's garbled Greek was not searched. Neither profile is thin for want of these. Owner: the Library thread, to weigh for the wanted list when the fill resumes.
    - Library headers. The content note of `mansi_sacrorum-conciliorum-collectio-tomus-31-concilium-florentinum-lat_welter-facsimile1906.txt` puts the opening of the decree Laetentur caeli near l.73472 and l.97371. Line 73472 (like l.83331) cites Cyril of Alexandria's letter to John of Antioch, which opens with the same words, and l.97371 is the cantors singing them after the reading. The session and the decree, with its signatures, are at l.96226-97420 (the heading DEFINITIO at l.96276). Owner: the Library thread.
    - Scan corrections. Councils scan, era 6: the Florence row's "Mansi tomus 31 names the Armenian envoys" is not borne out; the decree does not name them, and Raynaldus names two from the catholicos's mandate (l.39752-39755). The Coptic union of 1442, left "to confirm", is held: Cantate Domino is in Raynaldus, Denzinger and Mirbt. Florence is also named in `byzantine-church-palaiologan`, which the row's count of two entries leaves out. Both rows' "No Who verdict yet" is out of date: the era 6 Who scan and its supplement have scored the main people. The Constance row's "burned Jan Hus" has the same slip as the census above. The rows' tradition lists are shorter than the entries': Constance adds `observant-reform-and-popular-preaching`, `franciscan-order-era-6`, `devotio-moderna-brethren-of-the-common-life` and `byzantine-church-palaiologan`; Florence adds `the-ethiopian-monastic-flowering`, `church-of-the-east-timur-to-hakkari`, `franciscan-order-era-6`, `muscovite-monastic-christianity` and `the-hussite-and-bohemian-brethren-movement`. Who scan, era 6: the Ferrara-Florence row gives Laetentur caeli "near 73472 and 97371", the same slip as the header above (l.257). Richental's row calls the Aulendorf codex a copy of a "lost original", cited to the Library header; Buck's preface says "vorlage", an exemplar (Richental l.406-412). Owner: the coordinator. The audits are not edited.

272. **Era 4 Who batch 10: census text to check, the four Georgian entries, re-score corrections, other profiles to check, Library items (2026-11-15).** The seven batch 10 profiles (Theophanes the Confessor, Stephen the Younger, Nikephoros of Constantinople, Nicholas Mystikos, Peter of Sicily, Ilarion of Kyiv and Michael Keroularios) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch10/`. None is a census person entry or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch10/`; Decision-Log, "Who profiles, era 4 batch 10" (2026-11-15).
    - Census text to check, not changed here: Stephen the Younger and Nicholas Mystikos (batch README, "Live census mentions", l.23 and l.25). Stephen: Iconophile Byzantine Monasticism's `why`, `longDescription` and `voices[1]`, and the `when` and text of its story "Stephen the Younger Dragged Through the Mese", say he was killed in 765; `why`, `longDescription` and the story's text give it to the Life. No held line gives 765. The Life gives 28 November in his fifty-third year (PG100 l.97215-97217), Fabricius 766 (PG100 l.88570-88571), the Short History's marker 766 (PG100 l.81476), Theophanes 20 November under Goar's 757 (PG108 l.78706-78707), and the PG108 editors 28 November 767 (PG108 l.131112-131114). The story "Stephen the Younger Dragged Through the Mese" differs on his years on Mount Auxentius, the route (a public road and the Forum of the Ox, PG100 l.96963, l.97134), the crowd (l.96917-96955), the Life's date (its caveat's "c. 809", where Fabricius gives 808, PG100 l.88570) and the coin, which a devout man gives him before he is brought in (l.95535-95536); he asks only whether he would be punished (l.95704, l.95722). Its Theophanes year, 764/5, is in no held line; Goar numbers the annal 757 (PG108 l.78706). Nicholas, the story "The Emperor Turned Away at the Door on Christmas Day": Nicholas says Leo crowned Zoe himself (PG111 l.14009-14018). De Boor gives refusals at the church door at Christmas 906 and Epiphany 907, with no procession or imperial door (DEBOOR l.6611-6616, l.9246-9248). Letter 117 in Mai's numbering is to Leo, bishop of Sylaeum (PG111 l.25241). The story says Leo VI himself had legislated against a fourth marriage. The held lines have Leo's law forbid a third (Baronius in Henschen, PG111 l.423-425), and Basil void fourth marriages (MANSI l.93963-93965). February 907 is de Boor's; he reports Krug and Muralt for 908 (DEBOOR l.5795-5802), and Mai puts the exile nine years after the election of 895, or eleven by Leunclavius (PG111 l.662-664). The pope of Letter 32 is Lando for Baronius and Anastasius III for Pagi (PG111 l.862-865). De Boor holds that the eastern legates came, and names Mansi among those who doubted it (DEBOOR l.8640-8656). The census's council of 920 is the year of the world 6428 in Mansi (MANSI l.103092) and 921 in de Boor (DEBOOR l.4693-4694). Its "accepting Constantine VII's legitimacy" is not in the account before the Tomus of Union, in the lines read. The story puts the dispensation before the deposition; Nicholas has Rome's legates arrive before his arrest (PG111 l.14277-14279), and the Life, as de Boor reads it, after his exile (DEBOOR l.8546-8561). Owner: the coordinator, for the census text at era 4's completion release.
    - Census text to check, not changed here: Peter of Sicily, Ilarion of Kyiv and Michael Keroularios (README l.26-28). Peter: the Paulicians source note lists "adoptionism", which is not among Peter's six marks (PETER l.1318-1517); the link `paulicians--bogomils` has "around 870", as Rader and Gifford give (PETER l.599; NPNF7 l.9962-9963), where Gieseler dates the embassy to 868 (PETER l.154). Ilarion: no held line gives "around 1049" or "c. 1049"; the foreword places the Sermon after 1037 and before 1050 (GORSKII l.224-230), and the edition's note says about 1050 (l.4202). The Chronicle and his confession make him metropolitan in 1051 (CROSS l.11741-11742; GORSKII l.3995); Harasiewicz gives 1031 (HARAS l.1672, l.1749). No held line says "first native-born"; the Laurentian calls him a Rusin (PSRL1 l.6897), the foreword Russian by birth (GORSKII l.761), and Mouravieff names him and Clement of Smolensk as the native Russian metropolitans (MOUR l.2076-2078). No held line calls the Sermon the first Rus' theology. The 1054-1240 voice spells him "Hilarion of Kyiv", and no held source dates an act of his after 1054. The same entry's voice has Antony dig "the first cave"; the Chronicle has Ilarion dig the crypt Antony came to (CROSS l.11751, l.11774-11775), and the Caves Paterik has Antony first live in a cave the Varangians had dug (PAT l.1091). The census tells the Sermon as his, where the foreword argues it (GORSKII l.686-716) and Cross calls it attributed (CROSS l.5800). The link's "above the Dnieper" goes past the held lines. Keroularios: The Byzantine Church after the Schism, in `why` and `longDescription`, says 1054 "was not yet a final break"; Will (WILL l.15005), Sathas (PSELL l.3947) and Blackmore (MOUR l.16006-16007) say the opposite. It has one papal legate, where the envoys' account names three, Humbert first (WILL l.14779-14783), and "during the liturgy", where the clergy were ready for Mass (WILL l.14872-14876). A link note has him in office "until 1058", which is Blackmore's year (MOUR l.16006); Will gives 1059 (WILL l.4053). Three entries and both links spell him "Michael Cerularius". Owner: the coordinator, for the census text at era 4's completion release.
    - The four Georgian entries, split off from the re-score's batch 10 (coordinator's call, 2026-11-15; Mark may overrule): Grigol Khandzteli; Giorgi Merchule; John the Iberian and John Tornike; and Euthymius the Athonite. They share one Peeters volume, and the coordinator will make them their own batch after batch 12. The re-score leaves to Mark whether Euthymius the Athonite shares a profile with John the Iberian (Rescore.md l.164). Owner: the coordinator, with Mark for the pairing.
    - Re-score corrections (Rescore.md rows, not edited; README l.42-48). Theophanes: PG108 l.318-319 is Goar's Notitia, not the Life; the row does not cite Fabricius's attribution (PG99 l.841-844); the opening scene, the ice, is his own eyewitness note in the Chronographia (PG108 l.78213-78351). Stephen: the row's "a deacon among the monks who knew him" is not in the Life, which says only that he gathered it from truthful men and Stephen's disciples (PG100 l.88782-88785). Nikephoros: the Antirrhetici begin at file l.14725, not l.14713; "about 758" is the Bollandists' (PG100 l.1668-1669), not Fabricius's; the row's 815 for the exile is one of three placings, with 814 (PG100 l.102222-102223) and 816 (PG108 l.346-347, l.365); Goar reports Baronius and an anonymous Greek chronicle for June 814 for the crowning (PG108 l.350-353), and June 829 is held for the death (PG100 l.85132-85139). Nicholas: PG111 l.1108-1135, cited for his own letters, is the start of Letter 1, to the emir of Crete, and Letter 32 is at l.13723-15700; more than his own voice and one hostile source is held (Theophanes Continuatus, Leo the Grammarian, Eutychius and the Tomus); the row's exile of 907 is de Boor's, against Krug and Muralt's 908 and Mai's nine years after the election (DEBOOR l.5798-5800; PG111 l.662-664); the election (895 or 901), the return (911 or 912) and the death (924 or 925) are also disputed. Peter: that he followed Photius is Gieseler's argument, against Montfaucon and, in part, Wolf (PETER l.265-271). Ilarion: "all that is known" is at GORSKII l.741-759; the Sermon is l.1136-2497 and the confession l.2503-2611; the row's numbers are the host OCR's. Keroularios: the speech's heading is at PSELL l.20514-20515; the row misses the Chronographia passage (PSELL l.18041-18060) and the dispute over his death. Owner: the re-score's next revision.
    - Other profiles to check, not changed here. Humbert of Silva Candida (era 4 batch 4): his card heads its meeting item "Why they never met" (card l.43), which Michael's first letter contradicts, since the envoys came before him and handed him their letter (WILL l.17236-17237). It also leaves out Michael's own word that he declined to talk with them (WILL l.18076-18085), and gives the synod's day only as Will's 20 July, where Keroularios's card adds Sathas's 24 July (README l.70). Antony and Theodosius of the Kyiv Caves (era 4 batch 9): the brief has Antony dig "a cave" on a hill outside Kyiv, where the Chronicle has him come to the hill where Ilarion had dug the crypt (CROSS l.11774-11775). Its card gives the 1462 Paterik's earlier stay of Antony's (card l.36), but not the Varangian cave at Berestovoye he first lived in (PAT l.1088-1092). Name form: batch 9's card writes "Hilarion" (card l.8), Cross's form, and batch 10 writes "Ilarion", with Hilarion on the card; the census voice has "Hilarion of Kyiv". The coordinator may want one form across both batches. Owner: the coordinator.
    - Library, wanted (the fill is paused until Mark's reset, as in Open-Gaps 269): an English of Theophanes's Chronographia or his Life; the text of Theodore the Studite's letters to Theophanes, held only as titles and openings (PG99 l.142335, l.142454); the acts of Nicaea II (Mansi tomi 12-13); an English of the Life of Stephen the Younger, and Auzépy's edition (1997), which the census cites; an English of Nikephoros's Life, Antirrhetici or Short History; an English of Nicholas's letters, and a readable Greek of the Life of Euthymius (the held scan's Greek is garble); an English of Peter's History (the census cites Hamilton and Hamilton, 1998), and Photius's books against the Manichaeans; an English of Ilarion's Sermon on Law and Grace and his confession (the census cites Simon Franklin, 1991), and the Life of Antony that Simon of Vladimir cites; a readable scan of the Polish pamphlets in Arkhiv Iugo-Zapadnoi Rossii I.7 (p. 384, on Ilarion's consecration); Skylitzes, Attaleiates, Kedrenos and Zonaras; Psellos's charge against Keroularios before the synod (Sathas cites a Paris manuscript, PSELL l.3808-3809, l.4059-4060); an English of Keroularios's letters or of Psellos's funeral speech. Owner: the Library thread.

273. **Major councils, era 7 batch 1: Marburg held back, people with no verdict, census text to check, census parties with no tradition, Library items, and scan corrections (2026-11-15).** The three era 7 batch 1 council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/`, written to `Council_Profile_Pattern.md`: the Diet of Worms (1521), the Diet of Augsburg (1530) and the Synod of Chanforan (1532). None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217, "Map Who build slice", 2026-11-11). Source: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch1/`; Decision-Log, "Major councils, era 7, batch 1" (2026-11-15).
    - The Marburg Colloquy (1529), the fourth council of batch 1, is not written. No held text tells the debate in the room or prints the signed articles; Foxe's English list of the fifteen articles stops before the clause on the Supper, and Luther has no held words spoken at Marburg. Its record is a queued want in `Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Era 7" (Schirrmacher, *Briefe und Acten*, 1876, first choice; suggested, to confirm). Owner: the Library thread, then the council thread. The Worms row there (Reichstagsakten II or Kidd 1911) is not needed for the profile.
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id. Worms: Charles V, Aleander, Johann Eck of Trier, Frederick of Saxony, Richard Greiffenklau, Joachim of Brandenburg, Albrecht of Mainz, Lewis the Palatine, Philip of Hesse, George of Saxony, Hieronymus Schurff, "Dr. Voeus", Konrad Peutinger, Johann Cochlaeus, Jean Glapion, Martin Bucer, Caspar Sturm, Matthäus Schiner, Marino Caracciolo, Justus Jonas, Leo X. Augsburg: Charles V, Lorenzo Campeggio, the seven signing princes, Gregor Brück, Beyer, Eck, Faber, Cochlaeus, Wimpina, Dietenberger, Alexander Schweiss, Ferdinand, the archbishop-elector of Mainz, Matthäus Lang, Christoph of Augsburg, Bucer, Capito, Hedio, Jacob Sturm, Vadian, Jonas, Spalatin, Agricola, Brenz, Schnepf, Joachim Camerarius. Chanforan: Antoine Saunier, Daniel de Valence, Jean de Molines, George Morel, Pierre Masson, Oecolampadius, Bucer, Jeanet Peiret, Bersour, Martin Gonin. Owner: the coordinator, for a Who verdict.
    - Census text, to check: Augsburg. `lutheran-wittenberg-and-its-congregations`, `entry.tile`: "a confession signed before the emperor at Augsburg in 1530". Bensow has both copies signed before the reading (`bensow_svenska-kyrkans-bekannelseskrifter-swe_bensow1912.txt` l.31282-31284), and no held line has them signed in the emperor's presence. The edge `lutheran-wittenberg-and-its-congregations--the-reformed-cities-zurich-and-geneva--2` has the Formula say the Zwinglians broke away "when the Augsburg Confession was first read out"; the held line says "when this Confession was presented" (`book-of-concord_symbolical-books-evangelical-lutheran-church_jacobs1911.txt` l.26605-26606). The Lutheran Wittenberg voice line for Melanchthon ("author of the Augsburg Confession") leaves out Bensow's note that the chancellor Brück wrote most of the preface and conclusion (l.31272-31275). `martin-luther` has nothing on Augsburg or Coburg.
    - Census text, to check: Chanforan. `the-waldensian-reformed-union`, `voices`: Farel "pressed the union at the 1532 assembly". No held line says he pressed it; the held witnesses have him present or invited (Gilles 1881 l.2446-2448; Muston l.6402-6405; Crespin's editors, t1 l.49905-49911). The edge `the-reformed-cities-zurich-and-geneva → the-waldensian-reformed-union` cites `perrin_history-ancient-christians-valleys-alps_1847.txt` l.16865 as Perrin, Part I; that line is Pierre Boyer's added part (l.16687), and Perrin's own Bible line is l.5383-5386. The same entry's `sources[0].note` ("not an original protocol") settles what the held lines leave open: Muston calls the Dublin manuscript "the contemporary manuscript" (l.6470-6471) and Montet "les actes" (l.939-940). `the-waldensians`, `waldensians-in-the-alps` and `the-waldensian-reformed-union` tell the year 1532 and "joined the Reformation" as settled; held witnesses contest both (Perrin dates the assembly 1535; Léger says nothing changed in doctrine or discipline; Montet calls Protestant teaching a novelty).
    - Parties with no census tradition at the date. Worms: no census text describes the Latin church in 1521 (`the-tridentine-church` begins in 1517 but its text starts with Trent). Augsburg: the four Upper German cities (Strasbourg, Constance, Memmingen, Lindau), filed under `the-reformed-cities-zurich-and-geneva`; the Catholic estates and the legate, filed under `the-tridentine-church`, whose text does not mention Augsburg; `the-anabaptist-movements` does not mention the 1530 decree. Chanforan: the dissenting barbes (no Refused tradition; `waldensians-in-the-alps` ends in 1517 and is not listed); the Waldensians of Provence and Dauphiné; the Basel, Strasbourg and Berne reformers, who fit the Reformed-cities entry only in part; the Calabrian Waldensians (Muston l.6381). No census place id exists for Worms, Augsburg, Angrogna or Chanforans. Owner: the census thread.
    - Not held, and noted in the entries or `records.json`: the Diet of Worms's own record (Reichstagsakten II) and Charles V's French declaration of 19 April 1521; Aleander's dispatches; any original-language edition of Luther's Worms speech; the Confutatio pontificia; the full recess of 19 November 1530; any 1530 Campeggio document; Luther's Coburg letters; the Chanforan manuscript at Dublin, Herminjard, Scultetus and the Olivetan Bible with its "Apologie du translateur". Owner: the Library thread.
    - Scan corrections. Era 7 Who scan, `Who_Scan_Era7.md` l.76, calls `luther_hymns_bacon-allen.txt` l.651 an "editor's account of Worms"; it is Thomas Carlyle's words, quoted by Bacon (l.603-652). The councils scan's Worms row marked the Reichstagsakten WANTED, but no row was carried into CFT-Wants until this batch. Owner: the coordinator. The audits are not edited.


274. **Library, eras 1-3 wanted fill: what stays unfilled, and what the filled texts cannot carry (2026-11-15).** Twenty-five public-domain files were vendored for the eras 1-3 rows of the combined wanted list (person rows 1-13, council rows 1-8, Library-label correction 19). Source: `Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Eras 1-3"; `Build/Ministry/Operations/Audits/2026-11-15_library-eras1-3/` (search log, review, changes); Source-Library Decision-Log, "Church Family Tree wants, eras 1-3" (2026-11-15).
    - Cannot be filled from the public domain: Melito of Sardis, Peri Pascha (era 1 row 2). The homily was first printed in 1940. The held fragments (Otto 1872, Routh 1846) are all the Library can hold. Owner: the coordinator, for the Who verdict.
    - Not found, still wanted: Iakob Tsurtaveli's Martyrdom of Shushanik in any readable text before 1931 (era 3 row 8); the whole History of Movses Daskhurantsi (era 3 row 10; only Manandian's German chapters, with the canons of Aghuen, are held); a readable Greek Life of Sabas by Cyril of Scythopolis (era 3 row 11); F. W. K. Müller's Turfan fragments of 1904 (era 1 row 1); a readable scan of the Armenian Book of Letters for the councils of Dvin. Owner: the Library thread.
    - Filled with a caution a profile must carry. Sabas: the held Latin Life (Surius, 1880) says in its own heading that it may be Metaphrastes's reworking, so its wording may not be Cyril's. Mani: the Manichaean texts held are from manuscripts later than the entry's window, and the two fuller accounts of his life are Muslim writers of the tenth and eleventh centuries. Paul of Samosata: which fragments are his is disputed. Ezana: the Christian reading of his last inscription is disputed in Littmann's own addenda. Agathangelos is usually dated after 451. Owner: the Who workers for these rows.
    - Councils with no acts: Rome 377 (a notice in Mansi III), the Donatist council against Tyconius (Augustine only), Beth Lapat 484 (lost). Dvin 607-609 is held only through Ukhtanes, a tenth-century Armenian. Owner: the council-profile workers.
    - Shelf rulings wanted (`needs-ruling` rows): the Manichaean texts on `manichaeism`; Agathangelos on `armenian-christianity-conversion-era`; Nau's Maronite texts on `maronite-christianity`; the Latin Life of Sabas; the fragments of Paul of Samosata. Naironus (1679) has no shelf, since no Maronite entry covers its date. Owner: Mark, with the other shelf rulings.

275. **The map after release 44: Safari untested, the map's browser tests not in CI, the phone zoom floor (2026-11-15).** Source: Decision-Log, "The map after release 44" (2026-11-15); the reviews in `Build/Ministry/Operations/Audits/2026-11-15_map-fixes-after-44/`.
    - **Safari not tested.** The container has no WebKit (Playwright's webkit is not installed, and the environment forbids `playwright install`). The era mark, the map owning its pinch, and the tap with no tip were tested only in Chromium, some with WebKit's behaviour imitated. Each needs a check on an iPhone:
      - the era mark sits just after each title at first load and at every zoom;
      - a pinch on the map zooms only the map, and the bars stay put;
      - a tap opens the card at once (round 1 raised that Safari might hold back a first tap after a hover change), with no tip left behind.
      Owner: Mark, then the map.
    - **The map's browser tests are not in CI.** `Build/tools/tree_map_view.test.mjs` runs by hand after `node tools/build_tree_site.mjs`. CI has no browser job (the Playwright-in-CI item, P1-8). The late-font test needs `fonts.gstatic.com`, as the live page does. Owner: the CI owner.
    - **The phone zoom floor.** The floor on a phone is the width fit (0.18 on iPhone 13), not 0.9 × the opening zoom (0.35), because the tree is wider than the screen at the opening zoom. This is Mark's call; it is one line in `minScale`. Owner: Mark.
276. **Library, eras 4-5 second fill: what stays unfilled, cautions the filled texts carry, and rulings wanted (2026-11-15).** Forty-six public-domain files were vendored for the rows the first era 4 and era 5 passes left open and for the Library wants of Open-Gaps 263, 265, 266, 268 and 272. Source: `Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5/Search_Log.md`; `Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Eras 4-5, second fill"; Source-Library Decision-Log, "Eras 4-5, second fill" (2026-11-15).
    - Still not found, era 4: Ibn Hayyan's own book (a later writer who quotes him is held); the Greek Passion of the Mar Saba martyrs; Peter the Higumen; the Tale of Boris and Gleb; a Slavonic Life of Methodius; the synod of 843; a readable Greek Life of Euthymius; Cummian's Easter letter and the Kyiv archive page on Ilarion in a readable scan. Era 5: Teodosije's Life of Sava; Cosmas the Priest; Nerses of Lambron's speech; Mansi tomus 23 and the Lyon I constitutions other than the sentence; the Lyon II decree Zelus fidei; Akropolites; Dominic's process and Humbert's Legenda; Clare's Testament and her letters in her own Latin; Salimbene's Latin; Bernold; Peter of Vaux-de-Cernay for 1215. Owner: the Library thread.
    - Cannot be filled under the date rule: an English of Theophanes, the Life of Stephen the Younger, Nikephoros, Nicholas Mystikos, Peter of Sicily, Ilarion or the trial of Maximus (none printed by 1930); Valdes's profession; the French or Latin Mirror of Simple Souls; Cyril III's own record. Owner: the coordinator, to weigh whether those rows stay WANTED.
    - Filled with a caution a profile must carry. Ibn Hayyan: every line is a quotation by al-Maqqari in Gayangos's English extracts. The Life of Constantine: readable only in the editors' Latin translation of 1870; its manuscripts are of the fifteenth century and later. Clare's letters to Agnes: a Latin version made by Joannes Tannerus, so no phrase is Clare's own Latin; her Process survives in an Italian version. Walter Daniel: the Letter to Maurice as Powicke prints it, and extracts only of the Life. The council of 861 in Deusdedit: a Roman text kept two centuries later. Theodore the Studite's letters to Theophanes and the Life of Tarasius: Latin translations only. Hadewijch: the poems only, in Middle Dutch, with no translation held. The Greek of Photius (PG 102), Mansi 12-13 and Bekkos (PG 141), and the Irish of the Annals of Ulster, cannot be quoted from the OCR. Owner: the Who and council workers for these rows.
    - Rulings wanted from Mark. (1) Mansi tomus 20 (Clermont): the one scan has no imprint leaf, so the year of the printing cannot be read; it was not taken. (2) PL 148 (Bernold): no year can be read on its OCR title page; not taken. (3) Shelf rows marked `needs-ruling`: the Life of Tarasius; the Life of Robert of Molesme (two copies); Clare's letters in Tanner's Latin; Raymond of Capua's Life of Catherine, which came with the April volume for era 6. George Metochites's Historia dogmatica, bound in the Mai volume, has no shelf row. Owner: Mark, with the other shelf rulings.
    - Corrections to earlier logs. Berno's testament is held in the PL 133 file (about file line 67228); the first era 4 log said it was not printed there. Matthew Paris, volume 4, holds the Lyon I sentence (about file line 29303). Hadewijch's 1875 edition carries dbnl's own public-domain notice, which the first era 5 log did not record. Owner: none; recorded.
277. **Library, era 6 fill: what stays unfilled, cautions the filled texts carry, and rulings wanted (2026-11-15).** Twenty-seven public-domain files were vendored for the era 6 rows of the wanted list and the Library wants of Open-Gaps "Era 6 Who batch 1" (2026-11-14), "Era 6 Who batch 2" (2026-11-15) and "Major councils, era 6" (2026-11-15); three wants were held already. Source: `Build/Ministry/Operations/Audits/2026-11-15_library-era6/` (Search_Log, R1_review, R1_changes, R2_recheck); `Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Era 6 (1300-1517), filled"; Source-Library Decision-Log, "Era 6 fill" (2026-11-15).
    - Still not found. Person rows: the Prosvetitel of Joseph of Volotsk; the Lives of Stephen of Perm, Kirill of Beloozero, Zosima and Savvatii, and Theodosius of Tarnovo; the Gadla Ewostatewos; Zara Yaqob's own books. Outside witnesses: Rashid al-Din. From the Who and council batches: Kempis's Latin Life of Gerard in a readable print; Vetter's full Tauler; Kallistos's Life of Gregory of Sinai; Palamas's letter from captivity; Petit's article on the Synodikon of Thessalonica; a witness to the burning of Wyclif's bones. All exist in print before 1931 and are not on archive.org; another host is needed. Owner: the Library thread.
    - Cannot be filled under the date rule: the full Book of Margery Kempe (first printed 1936 and 1940); the full Triads of Palamas (1959); the Acts of Estifanos (nothing found before 1931). Owner: the coordinator, to weigh whether those rows stay WANTED.
    - Held already, with corrections. Zara Yaqob's chronicle is held in a running French translation in the Perruchon volume (from about file line 2922); its header, registry note and shelf note said there was none, and are corrected. So era 6 row 101 has a usable chronicle now, and the same volume tells the Stephanites' revolt from the court's side (about file line 6720). The Kempe short treatise is held (Gardner 1910). An extract of Abu'l-Fida's Annals and his autobiography are held in the Recueil's first Oriental volume, whose header named only Ibn al-Athir. Owner: the Who workers for rows 101, 103 and 112 and outside-witness row 8.
    - Filled with a caution a profile must carry. Joseph of Volotsk: the Life in the Great Menaion names no author in the OCR, so "by Savva Chernyi" is not held; the Life, his rule, Kirill's letters and Euthymius's Life of Hilarion are in Church Slavonic or old Russian with no translation held. Jakoubek: his tract of 1415 is kept inside Mauritius of Prague's reply, and the volume calls him Jacobellus de Misa only. Tauler: a selection after Vetter. Vegio's Life of Bernardino: the heading calls him an eyewitness of much of it; its line bounds are approximate. Bridget: Books VI-VIII carry Duranti's notes, and the prologue to Book VIII is headed as Alphonsus's. Ibn Battuta, Ibn Khaldun and al-Qalqashandi: held in their translators' French and German, and not read in depth for their passages on Christians. Owner: the Who and council workers for these rows.
    - Rulings wanted from Mark. (1) Reprints of old printings: Tsamblak's Praise of Euthymius is on archive.org only in the Variorum reprint (1971) of the 1901 edition, and Ockham's letter to the chapter at Assisi only in a Johnson Reprint of the 1884 journal volume; neither was taken. (2) Library stamps with later years on or near a title leaf (Ockham 1930, Wüstenfeld 1879) were not read as reprint signs. (3) Shelf rows marked `needs-ruling`: Euthymius of Tarnovo (no census entry is the Bulgarian church of his day); the Muslim outside witnesses, set on `coptic-christianity-fatimid-to-mamluk`, `byzantine-church-palaiologan` and `st-thomas-christians-1300-1517` for want of an entry for Mamluk Egypt and Syria or the Maghreb after 1300. Owner: Mark, with the other shelf rulings.

278. **Major councils, era 7 batch 2: people with no verdict, census parties with no tradition, census text to check, Library items, and scan corrections (2026-11-15).** The four era 7 batch 2 council profiles are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/`, written to `Council_Profile_Pattern.md`: the Colloquy of Regensburg (1541), the Council of Trent (1545-1563), the Diet of Augsburg and the Religious Peace (1555) and the Colloquy of Poissy (1561). None is in the census or on the site; councils go on the site with the map build (Open-Gaps 217, "Map Who build slice", 2026-11-11). Source: `Build/Ministry/Operations/Audits/2026-11-15_council-profiles-era7-batch2/`; Decision-Log, "Major councils, era 7, batch 2" (2026-11-15).
    - People in the council records whom no Who scan has scored, shown as NOT SCORED with no id. Regensburg: Charles V; Gaspar Contarini; The bishop of Modena, son of Jerome Morone; Granvelle; Frederick the Palatine; Julius Pflug; John Gropper; John Eck; Philip Melanchthon; Martin Bucer; John Pistorius; Peter Faber; John Brentz; The bishop of Winchester; Paul III; Reginald Pole. Trent: Paul III; Giovanni Maria del Monte (later Julius III); Marcello Cervini, cardinal of Santa Croce; Reginald Pole; Cristoforo Madruzzo, cardinal of Trent; Pedro Pacheco, cardinal; Girolamo Fracastoro; Diego Lainez; Alfonso Salmeron; Maurice, elector of Saxony; Leonardus Badehornus (Badehorn); Charles V; Pius IV; Ercole Gonzaga, cardinal of Mantua; Ludovico Simonetta; Giovanni Morone; Charles, cardinal of Lorraine; Pedro Guerrero, archbishop of Granada; Count of Luna; Angelo Massarelli; Gabriel Paleotto; Servanzio; Charles Borromeo; Pius V; Abdisho IV, patriarch; Marcantonio Amulio, cardinal; John Jewel. Augsburg 1555: Ferdinand, King of the Romans; Charles V; Giovanni Morone; Pope Julius III; Pope Paul IV; Zaccaria Delfino; Luigi Lippomano, bishop of Verona; Otto Truchsess, Cardinal of Augsburg; Peter Canisius; Jerónimo Nadal; Diego Lainez; Alfonso Salmerón; Pedro de Soto; Wolfgang, bishop of Passau; Christoph, duke of Württemberg. Poissy: Theodore Beza; Peter Martyr Vermigli; Charles IX; Catherine de' Medici; Michel de L'Hospital; Charles, Cardinal of Lorraine; François, Cardinal de Tournon; Diego Laínez; Juan Alfonso de Polanco; Ippolito d'Este, Cardinal of Ferrara; Claude d'Espence; Jean de Montluc; Nicolas des Gallars, Augustin Marlorat and Jean de l'Espine; Antoine, King of Navarre; Jeanne d'Albret, Queen of Navarre; Gaspard de Coligny; Jacob Andreae. Owner: the coordinator.
    - Parties with no census tradition at the date. Regensburg: Strasbourg's church (Bucer, and Calvin, who served it in 1541; `calvin_letters-vol1_bonnet1858.txt` l.10340-10344); the census has no Strasbourg or Upper German entry, and the entry does not file Bucer under Wittenberg. Poissy: the French bishops sit under `the-tridentine-church` (1517-1650) only, a loose fit for an assembly that submitted its canons to the pope while the crown resisted the legate; the Palatine theologians, who held with the French confession, fit no census id. No census place id exists for Regensburg, Trent, Bologna, Augsburg or Poissy. Owner: the census thread.
    - Census text, to check. The live `the-tridentine-church` story "The Last Day at Trent" gives the closing tears to Massarelli's diary; no held line does. The held tears are Servanzio's diary in Waterworth's footnote and Pallavicino's narration; Massarelli's diaries are not held. The live `church-of-the-east-schism-of-1552` says Abdisho "went to Rome himself in 1562"; Amulio's letter of August 1562 says he came "anno superiore", the year before (the Trent entry's `uncertain` notes this). Owner: the census thread.
    - Library items. Pallavicino book 13: the word after "lungi da-" in Ferdinand's answer to Paul IV is lost in the held 1664 OCR (`pallavicino_istoria-del-concilio-di-trento-parte2-ita_1664.txt` l.27571), and no other copy of book 13 is held; another edition or a clean scan would settle it, and until then the brief does not use it. Sarpi's "268 Biſhops" at the close (`sarpi_history-of-the-council-of-trent_brent1676.txt` l.70215) is probably a misprint for 168; the page image is unchecked. Not held: the colloquy book and agreed articles of Regensburg; Calvin's Latin letters of 1541; Massarelli's diaries. Owner: the Library thread.
    - Scan corrections. The councils scan's "last serious joint attempt" (Regensburg), "first legal toleration" and "Calvinists left out" (Augsburg 1555) and "hope of a common French church ended" (Poissy) are found in no held source and are not used. The Trent dossier (`working/dossier_trent.md` l.144) carries round 1's false absence ("only through Sarpi and Waterworth"); it is working material and the profile files no longer say it. Owner: the coordinator. The audits are not edited.

279. **Era 4 Who batch 11: census text to check, the outside witnesses' lane, names for Mark, other profiles to check, re-score corrections, Library items (2026-11-15).** The eight batch 11 profiles (Stepanos of Taron, Eulogius of Cordoba, Paulus Alvarus, Theodore Abu Qurrah, Stephen of Mar Saba, Ishoyahb III, al-Tabari and Ibn Ishaq) are approved to proceed and held in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/`. None is a census person entry or on the site. Source: `Build/Ministry/Operations/Audits/2026-11-15_who-profiles-era4-batch11/`; Decision-Log, "Who profiles, era 4 batch 11" (2026-11-15).
    - Census text to check, not changed here: every difference in the batch README's "Live census mentions" (l.23-30), one bullet per person, each giving the census path, the held line and agree or differ. Among them: the Mar Saba story "Twenty Monks in the Cistern" (`movements[65]/documentedStories[0]`) calls its author "Stephen Mansur, a monk of Mar Saba and a relative of John of Damascus". No held line gives him Mansur, and the Bollandists keep the author apart from Stephen the Wonderworker, John's nephew (AASS l.50429-50444). The same story differs on the raid's details (the cistern, the church plate, Sergius's and Patricius's deaths, the tower) and cites a Theophanes line not found. Its "20 March 797" agrees with the Bollandists' 797, with the Acts' AM 6288 (788) and Graf's 796 or 797 as other placings. The Ibn Ishaq bullet notes that census claims on Najran give a year and name Kaleb where his version does neither. Owner: the census owner.
    - The outside witnesses' lane. al-Tabari's and Ibn Ishaq's cards read "Outside the church", but the census places each outside witness on a lane (al-Baladhuri, era 4, on Syriac East & Asia). Which lane these two take is for the map build slice (Open-Gaps 217, "Map Who build slice", 2026-11-11). The river counts are unchanged, since the batch adds no majors. Owner: the map build slice.
    - For Mark (coordinator's and re-score's flags, not decided here). Stephen's display name: the Bollandists call the Wonderworker a Sabaite too (AASS l.50431-50433), and the Jerusalem Typikon, they report, sets this Stephen apart as the Poet (l.50436-50438). "Stephen the Poet" is the held option if the name itself should tell the two apart; the profile keeps "Stephen of Mar Saba" (coordinator's call, 2026-11-15). The re-score also flags that Mark may judge al-Tabari's life too thin, that Ibn Ishaq is a judgment call since the held text is Ibn Hisham's recension, and that he may prefer Stephen as a listed line (Rescore l.156, l.157, l.160). Owner: Mark.
    - Other profiles to check, not changed here. Beth Abe: the era3/batch6 babai-the-great brief, card, audio and records and the era3/batch8 barhadbeshabba-arbaya card write "Beth Abe", where batch 11 and the era4/batch5 thomas-of-marga profile write Beth 'Abhe (README l.39). "Used here" on reader-facing cards outside this batch: era4/batch5 alopen (`uncertain`, "No source used here says" and "the sources used here"), and, by the round 2 Part C review, era4/batch8 al-baladhuri and era4/batch10 ilarion-of-kyiv. Each needs a search of all of `cic/texts` before "used here" is dropped. Owner: the coordinator.
    - Re-score corrections (Rescore.md rows, not edited; batch README l.56-63): line ranges for all eight; "Mansur" for Stephen, which no held line gives; the Bollandists' year for the raid, 797, where the row has 796 from one scan figure; Eulogius's "written at his death (859-860)", which no held line dates; Ibn Ishaq's second death placing, 768, in Evetts. Owner: the coordinator. The audits are not edited.
    - Library, wanted (the fill is paused until Mark's reset, as in Open-Gaps 269): an Armenian text or English of Stepanos's Universal History (the census cites Greenwood, 2017), and Matthew of Edessa; an English of Eulogius's and Alvarus's works (the census cites Wolf, 2019, and Colbert and Coope), and the Arabic sources the census caveat names, among them Ibn Hayyan; an English of Abu Qurrah (Lamoreaux, 2005), and Michael the Syrian's Book XII; the Greek edition of Stephen's Passion by Papadopoulos-Kerameus (1907), an English (Blanchard, 1994), and the Life of Stephen the Wonderworker. Owner: the Library thread.

280. **Live-surfaces sweep: what is left on live surfaces, and the public site's own follow-ups (2026-11-15).** The sweep (`Build/Ministry/Operations/Audits/2026-11-15_live-surfaces-sweep/`) moved review history and rulings out of the Library and the engine. These remain, each for Mark or the owning thread; `R1_changes.md` section 5 lists every line.
    - Census text outside the stories, on the map and the tree pages: "the census row ends here", "The Who scan lists him as not yet scored", "per census", "census relations line", a "Change order" link reason, the `meta` source paths, `eras[].stepStatus`, about 19 build-jargon `statusWord` values, 166 `statusDescription` values opening "Tiered ...", 22 rendered `sourcing` values opening "RICH"/"THIN". After Release 45, which edits `cft-website/index.html`.
    - The story source notes that say "consulted via summaries only" and the like: real sourcing limits, worded by Mark. The check now flags them, so any change to `cft-website/index.html` fails `--enforce` until they are worded or ruled on.
    - `cic-website/traditions/syriac-edessa-nisibis.html` shows a record id in a pull-quote's citation, from `syr.quote.theodoret-gnats`'s `speaker_or_author` printed raw by `orientation-render.mjs`. `cic-website/data/worlds/desert-monasticism.json` carries a build note with a record id and a Doc_01 section ("the year itself from desert.source.evagrius-praktikos and Doc_01 SS2.3") from `desert.figure.evagrius`.
    - These lines, the story source notes, the census wording and the current relationsSummary lines are registered as ACCEPTED_OPEN waivers in `tools/check_live_commentary.py`, so they are reported as WAIVED and do not fail an edit to their files. The relationsSummary waiver is owned by Release 45 (PR #1679) and comes off when it merges; each of the others comes off when its lines are fixed. A waiver that matches no line fails `--enforce`.
    - Spoken record fields with builder vocabulary (`ijc.force.leo-rejects-canon-28` name, `pahc.core.house-church` cautions, `rzg.force.synod-of-dort-international-dimension` description); about 25 record-body passages with rulings and review findings, which the record schema places there by design; REGISTRY.yaml's append-only notes; the hadewijch, optatus and nestle1904 header lines; the Sandbox sample card's text.
    - Library headers that still say an original-language text is "never primary evidence" or that "this project's evidence language is English", contrary to INTAKE.md's current rule: csel57-pars4 (augustine_epistulae-critical_goldbacher), ausbund_lancaster1846, borromeo_acta-ecclesiae-mediolanensis, busch_chronicon-windeshemense, faber_memoriale, harnack_vita-cypriani-commentary, three kempis_opera-omnia files (sermones-de-compunctione, tractatus, vallis-liliorum-epistulae), nestle1904_greek-new-testament, piccolomini_historia-bohemica, pius-v_apostolicarum-epistolarum, ribadeneira_vita-ignatii-loiolae. One content correction. Also the stale REGISTRY.yaml note on vonsoden_prosopographie (it calls the vendored Ketzertaufstreit article unvendored), and the Library header lines the check now reports (R1_changes.md section 6).
    - support.html needs a content refresh before it is linked again (moved from `cic-website/README.md`).
    - The public site's own follow-ups, moved from `cic-website/README.md`: a brand-kit compliance pass on the About page's "How It Works" and "Safety & Disclosure" sections before full public launch; raster favicon exports (`.ico`/PNG; BR-17 in the System Hub tracker); the Article 31 external-review disclosure, once that process is further along (the site makes no "scholarly validated" claim, which is right until then).
    - 2026-11-15, done: the Library-header item above. Seventeen headers in `cic/texts/` now state the current rule in INTAKE.md's own words, with line counts unchanged. The thirteen listed there, plus fasciculi-zizaniorum, kempis sermones-ad-novicios and the two wyclif files (de-ecclesia, de-veritate), which carried the same sentence. Review: `Build/Ministry/Operations/Audits/2026-11-15_library-headers-evidence-rule/R1_review.md`.
    - 2026-11-15, for a later Library pass: 15 of those headers state the rule but not whether their own scan is clean enough to quote (INTAKE.md section 9): augustine csel57-pars4, borromeo, busch, faber, fasciculi-zizaniorum, harnack, kempis (four volumes), nestle1904, piccolomini 1592, pius-v, wyclif de-ecclesia, wyclif de-veritate. Only ausbund and ribadeneira say second witness.
    - 2026-11-15, done: the `relations-summary-release-45` waiver comes off with data release 45, which rewrites every story "How it connects" line (Decision-Log, "The stories' 'How it connects' as reader text, in the new voice, and a check that keeps it so", 2026-11-15).
281. **Library, era 7 fill: what stays unfilled, cautions the filled texts carry, and rulings wanted (2026-11-15).** Fifty-seven public-domain files were vendored for the era 7 rows of the wanted list (person rows 113-120, outside-witness rows 10-27), the Marburg and Worms rows queued by "Major councils, era 7 batch 1" (2026-11-15), and the Library items of that entry and of "Major councils, era 7 batch 2" (2026-11-15); one want was held already. Source: `Build/Ministry/Operations/Audits/2026-11-15_library-era7/` (Search_Log, R1_review, R1_changes, R2_recheck, R2_changes, R3_check); `Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Era 7 (1517-1650), filled"; Source-Library Decision-Log, "Era 7 fill" (2026-11-15).
    - Marburg can now be written. Held: Schirrmacher's Latin report of the sessions from Aurifaber's collection (OCR lines 1210-1836; it does not print the articles), and the Weimar edition's volume 30/3 with the reports of Hedio, the Anonymous, Collin, Osiander and Brenz and the fifteen articles with their signatures. Kidd prints the fifteenth article in a Latin version with nine signatures. Owner: the council thread.
    - Still not found. Person rows: Katharina Zell's Entschuldigung of 1524, her hymn-book preface in full and her Miserere exposition; the whole of Marie Dentière's Epistre and La guerre et deslivrance; Gracián's Peregrinación de Anastasio; more of Xu Guangqi than one memorial; the Nahuatl of Sahagún's informants (Seler, 1927). Outside witnesses: Peçevi, Mustafa Ali, Selaniki, Gedaliah ibn Yahya, David Gans. Councils: the text of the recess of 19 November 1530; the second decade of Scultetus in a readable scan; the Regensburg book of 1541; Calvin's Latin letters of 1541; Jacobs's Book of Concord, volume II, in a dated scan. All exist in print before 1931 and are not on archive.org, or not readable there; another host is needed. Owner: the Library thread.
    - Cannot be filled under the date rule: Fabian Fucan (nothing in a Western language printed by 1930) and Guaman Poma (first reproduced in 1936). Owner: the coordinator, to weigh whether rows 116 and 118 stay WANTED.
    - Located and not taken for their length: de Thou (the Latin of 1733 in seven volumes, the French of 1734 in sixteen) and Vasari (Foster's five volumes, de Vere's ten). Owner: the coordinator, to say whether outside-witness rows 20 and 25 are worth the shelf space.
    - Held already. The Colloquy of Poissy is in `beza_histoire-ecclesiastique-t1-fra_baum-cunitz1883.txt` (chapter from about file line 26871); the wanted list's council row 22 said "Not located" and is corrected.
    - Filled with a caution a profile must carry. Katharina Zell: her words are in a reprint of 1753 whose black letter the OCR reads only fairly, with Rabus's letters in the same section; Röhrich is a Life of 1855. Dentière: the Epistre is abridged by its editor; Jeanne de Jussie is an opponent. Gracián: a treatise that speaks of his captivity, not an account of his life. Xu Guangqi: one memorial in an unnamed translator's English of 1850. Las Casas: first person as an eyewitness in every volume, his own actions in the third person from volume IV; Spanish only, but for MacNutt's English of the Brevísima. Sahagún: Bustamante's Spanish only. Worms: the Edict is in full in the Reichstagsakten; Kidd has extracts, and the emperor's declaration in English only. Augsburg: Förstemann leaves out the recess of 19 November; Reu's English of the Confutatio uses Jacobs's translations. Sée's Emek ha-Bakha carries a later hand's notes in the text. The outside witnesses are in their translators' languages, but for Usque, Guicciardini and Bodin's Colloquium, and none was read in depth. Owner: the Who and council workers for these rows.
    - Rulings wanted from Mark. (1) The Schirrmacher scan: the host's record calls the item the Amsterdam reprint of 1968; the scan's title page reads Gotha 1876, with old library stamps, the printer's line of 1876 on the last leaf and no reprint leaf. It was taken on the title page, as the rule reads. (2) Reu (Chicago 1930): the imprint is the last year the rule admits, and the preface is dated 15 December 1930. (3) The Olivetan Bible of 1535: the only scan carries the French national library's notice on commercial reuse and cannot be read in the OCR; not taken. (4) Access-restricted or reprint-only items not taken: the Miscellanea Ehrle volumes that should hold Sahagún's Colloquios (1924), and Massarelli's diaries, whose every scan the host dates 1964. (5) Shelf rows marked `needs-ruling`: Katharina Zell on `lutheran-wittenberg-and-its-congregations` (Strasbourg has no entry); the Ottoman witnesses and Busbecq on `orthodoxy-under-the-ottomans-parish-millet-and-n`; the Jewish chroniclers, Guicciardini and Machiavelli on `the-tridentine-church`; Bodin and Montaigne on `the-huguenots`; Leo Africanus on `the-coptic-church-under-the-ottomans`. Two built worlds' shelves gained rows: `lutheran-wittenberg-and-its-congregations` and `the-reformed-cities-zurich-and-geneva`. Owner: Mark, with the other shelf rulings.
282. **The eight's corrected briefs are the bar; the live text and audio wait for re-recording (2026-11-15).** Mark approved the corrected texts of the eight early-church briefs as the bar for every Who brief (Decision-Log, "The Who writing standard restored to the eight early-church briefs", 2026-11-15). They are in `Who-Profiles/bar/`. They fix the brief findings of "Pattern findings in the eight live person texts" and "Origen's brief ends on a dispute" (both 2026-11-11). Owner: the coordinator.
    - Still to do: the live briefs in the census and the eight audio files carry the older wording. Both change to the bar texts together when the eight are re-recorded, which waits for credits.
    - By today's count, which charges names against reading ease, three bar texts score under 60: John Chrysostom 59.7, Gregory of Nazianzus 59.3, Methodius of Olympus 57.0. They pass the profile check Mark approved (grade on the full text, reading ease with names left out). Until the grader change is merged, a script that calls `grade_text` on them reports a failure that is not one.
    - Seen in the bar texts and left, since no finding named them: "Athanasius" with no place in Origen's brief; "Peter" with no place in Athanasius's; "Bishop John" as the first naming in John Chrysostom's; "Eusebius, the bishop of Caesarea" repeating his place in Constantine's third paragraph.
    - Soft spots against the five craft tests, noted and left: Origen, "Origen also wrote eight books in answer to Celsus" connects to neither neighbor; Methodius, "Theodoret of Cyrrhus kept a passage from his sermon on martyrs" has no link to what follows; Constantine has no link between the Milan decree and Arius, and its last line is a side fact; Athanasius's exile paragraph opens with no link to the argument before it, and the brief closes on a quotation; Gregory of Nazianzus, "Gregory was angry" stands alone; John Chrysostom's fourth paragraph turns to chronicle for a stretch. The review of this change added three in the fixes themselves: Ephrem, "In the day of Theodoret of Cyrrhus" is clumsy; Methodius, "so he is not a neutral witness, and little else about Methodius is certain" joins two thoughts that do not follow from each other; Gregory of Nazianzus, "so, his translators Browne and Swallow judge, he probably never served there" stacks three commas. They stand as Mark approved them and can be smoothed at re-recording.
    - The 250 briefs written since 2026-11-12 are to be checked against the bar. 206 score below grade 8 (Decision-Log, same entry).
283. **Card fixes for the eight, for the next data release (2026-11-15).** The card findings of "Pattern findings in the eight live person texts" (2026-11-11) that are still in the live cards, with the text Mark approved. Cards are live text, so they change at a data release, not before. Owner: the coordinator.
    - Gregory of Nazianzus, What traces to them. Now: "With Basil of Caesarea he gathered the Philocalia, a book of choice passages from Origen. About Easter in 382 he sent a copy to a friend as a book useful to students of literature." To: "He sent a friend the Philocalia, a book of choice passages from Origen, as useful to students of literature. His translators Browne and Swallow date the letter about Easter in 382 and say he edited the book with Basil of Caesarea. His own letter does not name Basil." Rests on Letter 115 (`npnf207`, line 47450) and its headnote (line 47442).
    - Gregory of Nazianzus, What is uncertain. Now: "It seems he did not, with a rival bishop's troops holding the village and his father pleading with him to stay." To: "His translators Browne and Swallow think it probable he never did, with a rival bishop's troops holding the village and his father pleading with him to stay." Rests on `npnf207`, line 22993.
    - Gregory of Nyssa, What is uncertain, the restoration item. To: "Whether Gregory of Nyssa hoped that all would at last be restored is still argued. His editors Moore and Wilson say it was charged against him at least from after the time of Justinian. Germanus of Constantinople answered that others had added to his books. They list the sermons On the Poor, On the Beatitudes and Against Usurers, which speak of eternal punishment, and judge that sermons meant to stir their hearers weigh less as witnesses." Rests on `npnf205`, lines 1414 to 1416 and 1527 to 1535. "They" must read as Moore and Wilson; reword at the release if it does not.
    - Gregory of Nyssa, What is uncertain, the Theosebeia item. "It seems to rest on two passages" becomes "Moore and Wilson say it rests mainly on two passages"; "None of his writings speaks of her as his wife." becomes "They find no allusion to her as his wife in his writings." Rests on `npnf205`, lines 606 to 610.
    - Ephrem, What is uncertain. Now: "Most writers date his death to 373, and some to 378." To: "His editor John Gwynn says most authorities give 373, the Chronicle of Edessa and Jacob of Edessa among them, and that some suppose he lived to 378." Rests on `npnf213`, lines 10627 and 12335.
    - Ephrem and Methodius, How they're remembered. "Honored beyond Syria." becomes "He was honored beyond Syria."; "Honored as a martyr." becomes "He was honored as a martyr."
    - Origen, How they're remembered. "Whether it did is still disputed." becomes "Whether it did is disputed. Hefele assigns the fifteen anathemas against Origen to a local synod of 543, and Noris and the Ballerini brothers to the council itself. A few scholars, Halloix and Garnier among them, also hold that Origen's name was added to the eleventh anathema later; Hefele keeps it." Rests on `npnf214`, lines 23863 to 23878 and 23989 to 24037. This is where the dispute taken out of the brief's close now lives (Mark, 2026-11-15).
    - The legacy paragraphs of Origen and Gregory of Nazianzus: "Rufinus" becomes "Rufinus of Aquileia" at first mention. The sourcing and legacy paragraphs of Constantine: "Zachariah's name" becomes "Zachariah of Mitylene's name" at first mention in each.
    - Not yet walked: the cards' first mentions of Jerome, Theodoret, Photius and Lactantius, which take the same few words of context as the bar briefs. Walk each card against its file at the release.
284. **John Chrysostom's live brief: 'John told the rich' is not in the homily (2026-11-15).** The live brief reads: John told the rich: "Wouldest thou do honor to Christ's body? Neglect Him not when naked." Homily 50 on Matthew (`npnf110_chrysostom-homilies-matthew.xml`, lines 29603 to 30039; the quote at line 29931) never calls his hearers "the rich". He speaks to his congregation as people who give gold cups and silk cloths to the church. Found by the Opus author of the modern telling. The bar text says "his listeners". The live text and audio keep "the rich" until the eight are re-recorded. Owner: the coordinator.
285. **Era 10 rights letters, and HathiTrust (2026-11-15).** Mark's rulings of 2026-11-15 (see the Source Library Decision-Log) send these letters and leave one network item open. Owner: Mark.
    - Letter to the Vatican, asking permission to hold and render the Vatican II documents. Later Vatican texts are cite and link only until it answers.
    - Letters to the bodies that state no reuse terms, starting with Barmen and Lausanne, then: the Lambeth resolutions, the Latin American bishops' conferences, Belhar, the Kairos Document, the Kyodan confessions, and the Russian church's texts of 2000 and 2007.
    - HathiTrust: opening it in the network settings is a dashboard step. Until then, old works whose only scan is locked are logged "located, not obtainable here".

286. **Library, eras 4-5 third fill: what stays unfilled, cautions the filled texts carry, and a ruling wanted (2026-11-15).** Seven public-domain files were vendored for the Library items of Open-Gaps 269 and 279 (era 4 Who batches 9 and 11). Source: `Build/Ministry/Operations/Audits/2026-11-15_library-eras4-5-b/Search_Log.md`; `Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Eras 4-5, third fill"; Source-Library Decision-Log, "Eras 4-5, third fill" (2026-11-15).
    - Now held: John of Damascus on the images in English (Allies 1898); the acts of Nicaea II in English (Mendham 1850); a complete Life of Rimbert (Pertz 1829); Matthew of Edessa in French (Dulaurier 1858); Abu Qurrah's treatise on images in Arabic with a Latin translation (Arendzen 1897); Michael the Syrian's Books XII to XXI in French (Chabot 1905); the Life of Stephen the Sabaite in Latin (Acta Sanctorum, July III). Owner: the Who workers for era 4 batches 9 and 11, to re-read their rows.
    - Still not found: a Life of Methodius beyond the held texts; any work of Clement of Ohrid, and the short Life of him; an Armenian text of Stepanos of Taron or Matthew of Edessa that can be read, and Dulaurier's part 1 of Stepanos; Abu Qurrah's Arabic in a readable scan; the Greek Passion of the Mar Saba martyrs. Owner: the Library thread.
    - Cannot be filled under the date rule: an English of Eulogius, Paulus Alvarus or Abu Qurrah (none printed by 1930). Owner: the coordinator, to weigh whether those rows stay WANTED.
    - Filled with a caution a profile must carry. Nicaea II in English: the translator wrote against the council, and his notes share the pages of the acts. The Life of Rimbert: its author is not named; the editor places it in the time of Rimbert's successor. Matthew of Edessa, Michael the Syrian and John of Damascus: translations only. Abu Qurrah: only the Latin can be quoted. Stephen the Sabaite: a Latin translation of a Greek Life that lacks its beginning. Owner: the Who workers for these rows.
    - Ruling wanted from Mark. Bacha's French of a second treatise of Abu Qurrah (Tripoli and Rome): the title page carries no year, and 1905 is the date of the preface only; it was not taken, as Mansi XX was not. Shelf rows marked `needs-ruling`: Matthew of Edessa (on `armenian-cilicia` and `bagratid-armenian-christianity`) and John of Damascus's sermons on the Assumption. Owner: Mark, with the other shelf rulings.
287. **Library, era 9 batch 1: what stays unfilled, what is owed a date check, and what was left (2026-11-15).** Ninety-nine public-domain files were vendored for the 63 major person rows of era 9 (wanted-list rows 163-225); the rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9, batch 1"), with cautions for profile writers, and the search record is `Build/Ministry/Operations/Audits/2026-11-15_library-era9/Search_Log.md`. Owner: the Library thread, era 9 batch 2, unless said otherwise.
    - Not found on archive.org: Darby's Letters and Collected Writings before 1931; letters or an early Life of Ambrose of Optina; anything on Kiai Sadrach; anything that names Nehemiah Tile or Mangena Mokone; John Thomas's Eureka and a Life of him; Hamberg's Visions of Hung-Siu-tshuen under its own title; Bourne's History of the Primitive Methodists (1823); the Act of Secession of 1834 and a Life of de Cock; Catherine Booth's Female Ministry (1859); War on the Saints before 1931; Lipscomb's census letters of 1906; the Gereformeerde Dogmatiek; a diary or Life of Nikolai of Japan; Conselheiro's own notebooks. Next route: dbnl.org for Sadrach and de Cock. The Dictionary of African Christian Biography has entries that can be cited and linked for Tile, Mokone and Sadrach, but it is CC BY-NC 4.0 and is not vendored.
    - Located, with OCR that cannot be read: Wichern's Denkschrift (third edition, 1889); Friedrich's Life of Dollinger and Dollinger's Briefe und Erklarungen in German; Khrimian's Armenian works; Waldenstrom in Swedish. A profile can cite these from outside; they cannot be searched or quoted from the shelf.
    - Owed a date check under the ruling on undated title pages: Kuyper's Stone Lectures on Calvinism; Hudson Taylor's A Retrospect; Walsh on the Uganda martyrs, with a chapter on Charles Lwanga; Catherine Booth's Aggressive Christianity.
    - Left, by the coordinator's call under Mark's ruling that a non-commercial notice in the file means not held (Mark may overrule): Os Sertoes, third edition, 1905 (`004518-completo` on archive.org), which serves rows 186 and 187. Another printing of 1902 to 1911 is to be looked for.
    - Filled with a caution a profile must carry: Moody, Nikolai of Japan, Cyril IV, Nommensen, Lwanga, Bourne and the Fliedners have no text in their own words in this batch; Ellis's Madagascar, vol. 2, prints no date of its own; Science and Health is the 161st edition (1899), not the text of 1875.
288. **Census gaps the shelf rulings left: candidates for future census entries (2026-11-15).** Mark's shelf rulings of 2026-11-15 (see the Source Library Decision-Log, "Shelf rulings") place each outside witness on the nearest existing entry and make no new census entry. These ten places have no entry of their own, and the works below sit on a neighbor until one exists. Owner: Mark.
    - The Maronites, 1517-1815. `maronite-christianity-era-6` ends in 1517 and the next Maronite entry starts in 1815. Naironus's Dissertatio (1679) has no shelf for this reason.
    - The Bulgarian church of Euthymius of Tarnovo's day (the late fourteenth century). His Life of Hilarion of Moglena sits on `serbian-and-bulgarian-medieval-monasticism`.
    - Mamluk Egypt and Syria. Al-Qalqashandi (2 files) and Ibn Khaldun sit on `coptic-christianity-fatimid-to-mamluk`.
    - The Maghreb after 1300. Ibn Khaldun's history of the Berbers and his Prolegomena (7 files) sit on the same entry.
    - Strasbourg. Katharina Schütz Zell (Füsslin 1753; Röhrich 1855) sits on `lutheran-wittenberg-and-its-congregations`.
    - The Ottoman state. Evliya Çelebi (3 files), Kâtib Çelebi and Busbecq's Turkish Letters sit on `orthodoxy-under-the-ottomans-parish-millet-and-n`.
    - The Jews of Europe. Joseph ha-Kohen (3 files), Usque and ibn Verga sit on `the-tridentine-church`.
    - Italy's politics. Guicciardini (4) and Machiavelli (4) sit on `the-tridentine-church` and `latin-papal-church-avignon-to-lateran-v`.
    - North Africa. Leo Africanus (3 vols) sits on `the-coptic-church-under-the-ottomans`.
    - Ukrainian Orthodoxy after 1700. The Western Ukraine letters of the 1760s and the Kyiv Academy documents of 1721-1750 sit on `russian-church-nikon-to-holy-synod`, whose window is 1652-1815.
289. **The stories' "How it connects" in the new voice (data release 45): what it leaves open (2026-11-15).** Source: Decision-Log, "The stories' 'How it connects' as reader text, in the new voice, and a check that keeps it so" (2026-11-15). The release closes the "How it connects" bullet of Open-Gaps 270, "The map, direction B" (2026-11-14), including its Pliny line.
    - Story source notes. 137 of the 168 sources on the 62 story cards carry a note on how the builder read the source ("consulted via summaries only", "known to me, not consulted", "seen via snippet"), and one caveat says "this entry has it at second hand" (Silesian Children's Prayer Revival). They record real limits on how the source was read, so how to tell a visitor that, or whether to, is Mark's wording call. The list: `Build/Ministry/Operations/Audits/2026-11-15_story-relations-cleanup/Other_Fields_Findings.md`. Owner: the map, with Mark.
    - Home traditions the cards do not link. Six lines name a home tradition the census holds but the card's links leave out: Hungary Protestants (Hungarian galley pastors), Catholics of Ceylon (Joseph Vaz), Arab Evangelicals (As'ad Shidyaq), Southern African Mission Churches (Ntsikana), Caribbean Churches of Slavery and Emancipation (Sam Sharpe) and Chinese Catholics (Candida Xu). As'ad's Maronite church of 1830 is the census's Maronites 1815-1906, while the card links Maronites II, which ends in 1517; the clergy who stopped Georg Schmidt belong to the unlinked Dutch Reformed Church at the Cape. Adding them to the cards' `relatedIds` adds links, which this release does not do. Owner: the map, with the census owner.
    - The Abercius epitaph. The story's teaser and text quote the epitaph as 'the same faith'. No vendored text of the epitaph is held, the stone's words are usually rendered "Faith everywhere led the way", and the card's source note says the fuller text comes through the later Life of Abercius. The story's audio speaks the same words. The "How it connects" line follows the card ("It says he found the same faith everywhere") without quotation marks. Owner: the map, with the Library thread for a text of the epitaph.
    - Le Chambon's teaser. It says "several thousand refugees, most of them Jewish children", while the card's caveat says the numbers are genuinely disputed and its text gives estimates from about 800 to 5,000. The "How it connects" line says "many of them Jewish children" (Mark, 2026-11-15: "use many for Le Chambon"). The teaser is card text outside this release. Owner: the map, at Mark's call.
    - The Scillitan audio. The story's text now quotes the Acts word for word and gives the Caesar line to Donata. Its narration (`cft-website/audio/stories/scillitan-martyrs.mp3`) may still speak the old sentence. It was not checked, since that needs a paid call. Owner: the map, at Mark's call.
    - Old-line claims. The 84 claims on 43 stories that the old builder lines made without card or census support (`Build/Ministry/Operations/Audits/2026-11-15_story-relations-cleanup/Old_Line_Claims.md`) are not carried into the new lines, which rest on the card and census only. A claim comes back only with a held source. One entry in that list is wrong: the Forty Martyrs' "Sebaste lay in Lesser Armenia" is on the card, in its region field. The first rewrite's "towns of Lombardy" for the Great Alleluia is gone; the line follows the card's "cities of northern Italy". Owner: the map, with the Library thread.
    - Census and card disagree, seen in review and not changed here. The Herrnhut entry dates the Moravians' return to Genadendal and Magdalena at 1786; the Genadendal card says 1792 (the line follows the card). The Laestadian entry says Rosenius helped inspire a mission society of 1856, likely the Swedish Evangelical Mission of the Onesimos story, but does not name it, so the line cannot use the link. Owner: the census owner.
    - Common names with no place in any held source: Macarius, Moses the Ethiopian's teacher, stays bare in the line. Owner: the map, with the Library thread.
    - Story text checked only where it touched this work. The Scillitan fix came from review. No other story's text, teaser or caveat was re-checked against its sources. Owner: the map.
290. **Library, era 10 batch 1: what stays unfilled, what is held for Mark, and a correction to 285 (2026-11-15).** Ninety-four texts were added for the era 10 wants (`Build/Ministry/Features/Source-Library/CFT-Wants.md`, "Era 10 ... batch 1"; the search record and the cautions are in `Build/Ministry/Operations/Audits/2026-11-15_library-era10/Search_Log.md`). Owner: the Library thread, except where Mark is named.
    - Correction to 285: HathiTrust refuses automated clients itself (403). No network setting opens it. Mark fetches HathiTrust items by hand; the Library lists each wanted item with its URL and edition.
    - No held source, row by row in the wants list: the Azusa Street paper and Seymour's book; the African-Initiated Churches people (Harris, Kimbangu, Orimolade, Babalola, Lekganyane and the rest), the East African Revival people, Kivebulaya, Spartas and Kiwanuka; Rātana; the Moscow council's own prints of 1918; Balakian; Kyrion II; most of the Orthodox patriarchs; Watchman Nee and the True Jesus Church; Barth's Römerbrief; Bonhoeffer; Bartleman; Larkin; the Watchman-Examiner of 1920.
    - The Dictionary of African Christian Biography is CC BY-NC by its own usage page, so it is cite and link (Mark, through the coordinator).
    - Held for Mark: Loisy's L'Évangile et l'Église of 1902 (the only scan is a library film with a permission notice); The Apostolic Faith of 1906-1908 (the holding archive's terms say personal research only).
    - Refused hosts, for a hand fetch: Papers Past (Te Whetu Marama, the Rātana paper) and the Russian state libraries (the 1918 Definitions and Acts).
    - Taken on a coordinator's call that Mark may overrule: eleven files whose year is printed only inside the work's title (Edinburgh 1910, Lambeth 1930, Shanghai 1922), and Bultmann's Jesus (1926), dated by a dated afterword with the catalog date agreeing.
    - Latin held with no English printed by 1930 (Mortalium animos, Sacrorum antistitum, the homily to the Chinese bishops, Ab ipsis, Iniquis afflictisque): a rendering of ours needs the second independent rendering.
    - Half met: Metropolitan Sergius. His declaration is held in an English printing of 1929; no full text of an answer rejecting it is held.
291. **Library, era 8 batch 1, the global files: what stays unfilled, rulings wanted, and cautions (2026-11-15).** Thirty public-domain files were vendored for the era 8 wants of Africa, Egypt, Ethiopia, Latin America and Asia; the rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 8 (1650-1815), batch 1"), with cautions for profile writers, and the search record is `Build/Ministry/Operations/Audits/2026-11-15_library-era8/Search_Log.md`. Owner: the Library thread, era 8 batch 2, unless said otherwise.
    - Not found in a print of 1930 or earlier: the relations of Bernardo da Gallo and Lorenzo da Lucca on Kimpa Vita; Capitein; Thomas Thompson's own account; Ntsikana's hymn; the acts of the Synod of Mount Lebanon (1736); Lambert de la Motte's own writings and the Monita; Rego's Life of Joseph Vaz; a Chinese Catholic's own text; the hidden Christians' own text; the Varthamanappusthakam; Úrsula de Jesús; Hernández y Dávalos and Morelos.
    - Shelf rulings wanted (Mark): Rhodes's three works (1651, 1652, 1682) tell missions that end before `vietnamese-catholicism-to-1815` opens in 1650, and the Divers voyages names no author on its title page (the attribution is the host's); the Ceylon Sketch (1848) and the Code noir (1767) sit as context, needs-ruling; Charmot's notes in the Historia cultus Sinensium; the second parts of Proyart, Baldaeus and Valentijn.
    - Rights calls made by the coordinator under Mark's ruling of 2026-11-15 on title pages with no year, which Mark may overrule: Rhodes's Cathechismus was taken on its printed license leaf of 8 July 1651; Weld Blundell's Royal Chronicle of Abyssinia (no dated title page, preface or notice in the scan) and Merolla's English Voyage to Congo (no imprint of its own) were not taken.
    - Left for the next batch: Parry's Six Months in a Syrian Monastery (1895), from a second scan, since the Columbia scan carries a permission line; the census has no entry for the Syriac Orthodox between 1650 and 1906. Bacha's French of Abu Qurrah (Open-Gaps 279) now clears on its preface date, but its one scan is cropped; a better scan is wanted.
    - Held for Mark, as before: Ximénez (CC BY-NC-ND uploads; the volume with Cancuc is dated 1931) and the modern Vietnamese upload of Rhodes's catechism (CC BY-NC-ND).
    - Filled with a caution a profile must carry: Philip Quaque speaks only as Pascoe's digest quotes him; Maigrot's Mandate is held in Latin, with the year garbled in its date line; Ibrahim al-Jawhari is held in al-Jabarti's French and in one footnote of Butcher; Joseph Vaz only in the unsigned Sketch of 1848; in the Cathechismus only the Latin can be read; Guidi's Ge'ez text has not been checked against the print.

292. **The map after release 44: the Safari check and the phone zoom floor settled; the browser tests still out of CI (2026-11-15).** This follows Open-Gaps "The map after release 44" (2026-11-15). Source: Decision-Log, "The map after release 44: Mark's iPhone check passes" (2026-11-15).
    - Settled: the Safari check passes on Mark's iPhone ("yes the iphone looks good"). The phone zoom floor stays the width fit ("keep it as is").
    - Still open: `Build/tools/tree_map_view.test.mjs` runs by hand after `node tools/build_tree_site.mjs`; CI has no browser job (the Playwright-in-CI item, P1-8). Owner: the CI owner.

293. **Library, era 9 batch 2b: what stays unfilled, what is still to vendor, and the calls made (2026-11-15).** Sixty-one public-domain files were vendored for 49 person rows of era 9 (rows 227-245, 249-262, 267-278, 323 and 327-330 of the wanted list) and the date check on row 223; the rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9 (1815-1906), batch 2b"), with cautions for profile writers, and the search record is `Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2b/Search_Log.md`. Owner: the Library thread, era 9.
    - Not found in a print of 1930 or earlier: Daniel Coker's Dialogue (1810) and Journal (1820); Hiram Edson's account of the morning after; a bound volume of the Woman's Exponent and a Life of Emmeline Wells; Tirzah Miller's diaries; the Western Mail's revival pamphlets by "Awstin"; anything of Priscilla Lydia Sellon's own; Bellett's memoir of the early circle; Norton's Memoirs of James and George Macdonald; the Christadelphian magazine and a Life of Robert Roberts; the Southern Baptist Convention's Proceedings of 1845; the Baptist Union's record of 1887-88; Hailey's Life of Graves; Wilder's own history; Drei Bucher von der Kirche in German; Bernadette's depositions and Estrade; the Flaminian Gate pastoral as a separate print; an English Ongeloof en Revolutie.
    - Still to vendor, by the coordinator's instruction (Mark's remark of 2026-11-15, "each of them are vendering all the sources they find into the library", was a statement of fact about the Library threads and not a rule): the items under "Located, not yet taken" in this batch's search log, which pass on rights and were left out only for want of room in the session. They go first in the follow-on batch (`Handover.md` in the audit folder). Whether batch 1's "Located, not yet taken" list is taken by this thread or by batch 2a is for the coordinator to assign.
    - The follow-on batch: the era 9 texts the story, tradition and council cards rest on, for Britain, Europe and North America (134 of the 211 rows in `Texts_To_Fetch_Era9.md` in the audit folder; each title was named from memory and is to be confirmed).
    - Rights calls made by the coordinator, which Mark may overrule: Marchant's Life of Clifford was taken on its printed "First published 1924" line, with a dated introduction and the catalogue agreeing; Roberts's Christendom Astray was taken on its preface of 18 December 1883, though the scan is a reader's upload with no library catalogue behind it.
    - Held for Mark: the scan of Emma Smith's hymnbook of 1835 that carries an Intellectual Reserve copyright line (`collectionofsacr00smit`); a microfilm copy without that line was vendored.
    - Not taken, with the reason in the search log: Lohe's Neuendettelsau history in German (the OCR cannot be read); loose numbers of the Woman's Exponent; two typescripts of 1900 about Coker (unprinted, cite only).
294. **Library, era 9 batch 2a: what stays unfilled, what waits for a browser, and what was located and left (2026-11-15).** Seventy-one public-domain files were vendored for the era 9 person rows outside Britain, Europe and North America (wanted-list rows 226, 246-248, 263-266, 279-322 and 324-326) and for batch 1's retried rows; the rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9 (1815-1906), batch 2a"), with cautions for profile writers, and the search record is `Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2a/Search_Log.md`. This follows Open-Gaps "Library, era 9 batch 1" (2026-11-15). Owner: the Library thread, unless said otherwise.
    - Not found on archive.org before 1931: anything that names Nehemiah Tile in full; Iakov Netsvetov's journals; the letters of Ambrose and of Macarius of Optina, and Agapit's Life; Theophan the Recluse's letters and his Put' ko spaseniiu; Makary Glukharev's letters; the acts of the Maronite synod of 1818; anything by or on Elias Hoyek; Massaad's own letters; anything on Nerses Varzhapetian; Oikonomos's defence of the Patriarchate; the acts of the council of 1872; Philiphe Binh's own book; Liang Fa's tract; Ta'unga's own narrative; the Iglesia Filipina Independiente's Doctrina y Reglas Constitucionales (1904) and Oficio Divino (1906); the Ley Juarez of 1855; Macedo Costa's Direito contra o direito; a printed Carta pastoral of Dom Vital; Bokwe's Ntsikana; Hamberg's Visions of Hung-Siu-tshuen; Darby's Letters and Collected Writings; Catherine Booth's Female Ministry; a second printing of Os Sertoes; anything in Conselheiro's own words. The search log's "Not found" section gives the routes tried for each.
    - Waiting for a browser, on hosts that refuse automated clients (the search log's hand-fetch list): Sadrach and de Cock on dbnl.org; A Retrospect, Kuyper's Stone Lectures and the Cape Blue-books of 1884 and 1885 on HathiTrust; the Optina elders' letters on prlib.ru; Ta'unga's letters on Papers Past. Owner: Mark.
    - Located on archive.org and not yet taken: about thirty volumes, each with its identifier, under "Located, not yet taken" in the search log. Taking them is the former coordinator's instruction and waits on the present coordinator's word.
    - Seen and not taken, with the reason: Mas's Informe of 1843 on Apolinario de la Cruz (title page wanting, OCR garbled); al-Dibs's Arabic history of the Maronites and Uchimura in Japanese (OCR cannot be read); C. S. Smith's History of the African Methodist Episcopal Church (reprint copies only).
    - Three files vendored in this batch were dropped before the merge, because another Library batch had put the same scan on main first: Aglipay's Catequesis (era 10 batch 1), Launay's Histoire générale, tome 2 (era 8 batch 1) and Neatby's History of the Plymouth Brethren (era 9 batch 2b). The map rows for Launay and Neatby were moved onto main's files. Each Library thread now checks its picks' archive.org identifiers against main's registry just before it merges.
    - The list of texts the cards rest on (`Card_Texts_To_Fetch.md` in the audit folder, 106 rows for these regions) is dropped and was not started. It came from the legend check. Mark, 2026-11-15, as the coordinator passed it on: "the legend wasn't about source, it was about it calling legends true who profiles. we dont need to build out more legends we need to make sure the who and counsils are drawing from their own sources not sources writen 1000 years later".
295. **Library, era 10 batch 2: what stays unfilled, what is held for Mark, and the census gaps met (2026-11-15).** Seventy-one public-domain files were vendored for the era 10 wants of Africa, Oceania and the Orthodox, Oriental and Assyrian churches; the rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 10 ... batch 2"), and the search record, the calls and the cautions for profile writers are in `Build/Ministry/Operations/Audits/2026-11-15_library-era10-b2/Search_Log.md`. This follows Open-Gaps "Library, era 10 batch 1" (2026-11-15). Owner: the Library thread, except where Mark is named.
    - Not found on archive.org with a printed year of 1930 or earlier: anything by or on Orimolade, Babalola, Lekganyane, Spartas and the other African-Initiated Churches and Revival people; Harris's own teaching, Kimbangu's trial record and Kivebulaya's diary (outside witnesses only are held); more scans of the New York Catholic Worker; Bulgakov's Svet nevechernii; anything by Vladimir Lossky; the encyclical of January 1920 and the Pan-Orthodox acts of 1923 in Greek (both are held in English); the Serbian, Bulgarian and Romanian church journals for Cristea, Dimitrije, Kiril and Trifa; Balakian's Armenian Golgotha (1922); a dated book of Habib Girgis; Surma Khanim's Assyrian Church Customs (1920); the consecration of 1912 in the Malankara papers.
    - Reprints only: the Acts and Definitions of the Moscow council of 1917-18. Every scan on archive.org is of 1994 or later.
    - Held for Mark, a host record that claims copyright in the scan: three Māori and Tongan prints of 1897-1916 (`hehimenemotekara00unse`, `kotehahioihukara00ande`, `koegaahihimiosai00unse`) and the composite `ngahimenemongahu01auck`. Not taken under R3, an uploader's non-commercial license: three prayer books in African languages (`kitabu1928`, `shekiri1909`, `angas1921`). Owner: Mark.
    - For a hand fetch, on hosts that refuse automated clients: the twenty items of `Hand_Fetch_List.md` in the audit folder, among them Te Whetu Marama (Papers Past), the Moscow council's prints of 1918, Loisy's first edition of 1902 (Gallica), The Apostolic Faith, Balakian, Riley and the Watchman-Examiner of 1920. Owner: Mark.
    - Calls this thread made, which the coordinator or Mark may overrule (Search_Log, "Calls made during the batch"): the Malayalam monthly taken on the year printed on its calendar leaf; Jabavu's second edition, dated by its foreword and prefaces; the leaf of 1915 in Wanger's catechism of 1912; a tradition's own writer after its entry's window placed as tradition on the entry that closes in 1906. In the 25 numbers of Путь a digitizing library's page-foot stamp was stripped at intake, and each header counts the lines removed.
    - Census gaps met, with works that sit on a neighbor until an entry exists: Sundar Singh; the mission churches of southern Africa after 1906; the Coptic church from 1906 to 1940; the Serbian church between 1906 and 1920; the Māori and Pacific mission churches after 1906. This adds to Open-Gaps "Census gaps the shelf rulings left" (2026-11-15). Owner: Mark.
    - Located, dated 1930 or earlier by the searchers' reading and not yet taken: the list under "The follow-on" in the batch's `Handover.md` (The Christian East, the International Review of Missions, the Proceedings of the Church Missionary Society and about thirty books). Each still needs its own title-page check. The 408 era 10 rows of the cards' texts to fetch (`Fetch_Rows_Era10.md`) are dropped and were not started. They came from the legend check. Mark, 2026-11-15, as the coordinator passed it on: "the legend wasn't about source, it was about it calling legends true who profiles. we dont need to build out more legends we need to make sure the who and counsils are drawing from their own sources not sources writen 1000 years later".

296. **Quotations not in a held file on story, tradition and council cards: what changed and what stays open (data release 46, 2026-11-15).** Source: Decision-Log, "Quotations not in a held file: twelve cards corrected or told plainly" (2026-11-15). The verification table, the change list and both review rounds are in `Build/Ministry/Operations/Audits/2026-11-15_cft-quote-fixes/`. Owner: Mark, except where another owner is named.
    - Held for Mark, unchanged: "Dominic Sells His Books". Neither quotation is held in English. Both are held in Latin in Brother Stephen of Spain's 1233 canonization testimony (Acta Sanctorum Augusti I, l.66808-66818, l.108396-108404), not in Jordan's Libellus. Jordan's Libellus (same file, l.92447-92461) has the famine and the sale of the books, but no saying and no books annotated in Dominic's hand. The card's text and caveat give Jordan what the held texts give to Stephen, so a fix reaches past the quotations.
    - Held for Mark, unchanged: "John of Ephesus Baptises the Pagans of Asia — By Order", the word ‘compelling’ and "the fear of imperial law". The chapters the card cites are held (Payne Smith, Part III, III.36-37 and II.44; Brooks, Lives ch. 43) and so is Michael the Syrian's extract of John. None has language of compulsion. A plain telling would still claim what the held chapters do not say.
    - Card details the review noted, left unchanged: the John of Ephesus card's 96 churches and seventy thousand converts (Payne Smith II.44 gives 99 churches; Michael the Syrian's extract gives 96 and 70,000). The Comenius teaser and closing line still speak of "the rule of its affairs", while the corrected quotation (Lützow 1920) reads "control over thy destiny". Scholastica's Storm now quotes the 1608 translation as Gardner printed it in 1911, which the card's sources do not name. Owner: the map.
    - The `verification` fields on these cards still read "from reference summaries; primary text not yet read", although the quotations have now been checked against held texts. Owner: the map.
    - Verbatim wording that is hard at B2: "greatly excited" (Ælfheah) reads as eager, not angry; "of right she did more which loved more" (Scholastica). Both are as held.
    - Not yet held: English of Toledo IV canon 57 (Linder), the Apocalypse of Pseudo-Samuel (Ziadeh), the Kšaft of 1650 in Czech, Broomhall's Martyred Missionaries and China's Millions, and English of Chrysostom's homily on Lucian. Those cards are told plainly until a text is held. Owner: the Library thread.

298. **Library, era 8 batch 2: what stays unfilled, what was left out, and the rulings wanted (2026-11-15).** Thirty-seven public-domain files were vendored for the era 8 wants of the British Isles, the Methodists, North America, Catholic Europe and the Jesuits, with the volumes batch 1 found and left; the rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 8 (1650-1815), batch 2"), and the page-image reads, the calls and the cautions for profile writers are in `Build/Ministry/Operations/Audits/2026-11-15_library-era8-b2/Search_Log.md`. This follows Open-Gaps "Library, era 8 batch 1, the global files" (2026-11-15). Owner: the Library thread, unless said otherwise.
    - Held only as an extract in a later book: Samson Occom's narrative of 1768 (the opening, in Love, 1899); Nathan Cole's "Spiritual Travels" (in Walker, 1897); Robert Raikes's letters of 1783 and 1785 (in Gregory, 1877). No whole printing of 1930 or earlier was found.
    - Filled in part, one volume of several: Roberts's Hannah More (vol. 1 of 4); the Wilberforce Life (vol. 1 of 5, and the scan stops inside its appendix); Quesnel (tome 1, Matthew and Mark); Dobrizhoffer's Latin (pars I of 3); Vieira's Sermoens (three of the parts). The later volumes of Roberts and of the Wilberforce Life are located on archive.org and not taken.
    - Not found by the first era 8 search and not searched again: Hindmarsh, Rise and Progress (1861); Ann Griffiths in Welsh; Kirk's Biographies (1909); Davenport's Confession and Retractions; Herman of Alaska; Wesley's Letters and his Sermons after vol. 1; Charles Wesley's Journal, vol. 2; Whitefield's later Journals; Fletcher's Checks; the Arminian Magazine.
    - Left out, with the reason in the search log: Valentijn, deel 2 (no church section found; deel 3 is held); the Code noir collection of 1743 (the church's acts are in the held collection of 1767); Gobat's New York printing of 1850 (a later printing of a held text, by the coordinator's instruction). All three pass on rights.
    - Rulings wanted on three shelf rows marked `needs-ruling`: Parry's Six Months in a Syrian Monastery on `the-sayfo-and-the-syriac-diaspora`, since the census has no entry for the Syriac Orthodox between 1650 and 1906 (this adds to Open-Gaps "Census gaps the shelf rulings left", 2026-11-15); Charmot's Vindiciae on `chinese-catholicism-1650-1906`; Quesnel's Réflexions morales as the condemned text on `catholic-church-ancien-regime`. Owner: Mark.
    - Calls this thread made, which the coordinator or Mark may overrule: Love's Samson Occom taken under R12 on its copyright notice of 1899; Taft's Holy Women taken on its printed years, though the scan is a reader's upload with no library catalog behind it; Lemuel Haynes shelved on the New England awakening entry, where the census names him, and on `the-black-church-in-america`.
    - Not started, by the coordinator's instruction: the era 8 rows of the cards' texts to fetch, which came from the legend check; and all rendering, which waits until Mark has seen a proposal and a sample.

299. **Library, era 9, the located volumes: what stays unfilled and the calls made (2026-11-16).** Twenty-seven public-domain files were vendored: the volumes era 9 batch 2b located and did not take, with the items it named without an identifier. The rows are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9 (1815-1906), the located volumes"), and the page-image reads, the corrections to the list, the calls and the cautions for profile writers are in `Build/Ministry/Operations/Audits/2026-11-16_library-era9-located/Search_Log.md`. This follows Open-Gaps "Library, era 9 batch 2b" (2026-11-15). Owner: the Library thread, unless said otherwise.
    - Now held whole: the Dialogues on Prophecy (3 vols.), Drummond's Speeches and pamphlets (2 vols.), Froude's Remains (4 vols.), and the Lives of Samuel Wilberforce (3 vols.), Shaftesbury (3 vols.), Maurice (2 vols.) and Wiseman (2 vols.).
    - Still not held: the Pacific Garden Mission's report of 1895; Colenso's Pentateuch, part II (the scan listed as part 2 is part III); Cox's Life of Colenso, vol. 2; the Morning Watch, vol. II and vols. IV-VII; Bellett's Evangelists on Luke, Matthew and Mark (the scan holds John only). None was searched for beyond the listed scans.
    - Not taken, as later printings of held texts: In His Steps in printings of 1899; Newton's Thoughts on the Apocalypse in the printing of 1904.
    - Calls this thread made, which the coordinator or Mark may overrule: Dialogues on Prophecy, vol. II, taken from a reader's upload on its printed year of 1828; Cabot's Emerson, vol. 2, taken in the eighth edition of 1895 beside a vol. 1 of 1887; the American Church History volume taken whole with a shelf row for Hamilton's part only.
    - Held for Mark, a rights question: the Pacific Garden Mission's fortieth annual statement (`annualreportpaci1915paci`). It prints no year on its cover or title leaf. Its text is for the year ended 15 September 1916 and its auditor's letter is dated 17 November 1916; the catalog record has no date. Neither the rights rule nor R12 lists a dated report's own text as a basis, so it was not vendored. A ruling that a dated institutional report counts by its own dated text would admit it and others like it. Owner: Mark.
    - Not started, by the coordinator's instruction: the 134 card rows of batch 2b's texts to fetch, which came from the legend check; and all rendering.

300. **Library, era 10 batch 2b, the periodicals: what was taken, what is held for Mark, and what was located and left (2026-11-16).** Forty-five public-domain files were vendored: 31 numbers of The Christian East and 14 volumes of The International Review of Missions, which era 10 batch 2 found and did not take. The files are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 10, batch 2b, the periodicals"), and the page-image reads, the calls and the cautions for profile writers are in `Build/Ministry/Operations/Audits/2026-11-16_library-era10-b2b-periodicals/Search_Log.md`. This follows Open-Gaps "Library, era 10 batch 2" (2026-11-15). Owner: the Library thread, except where Mark is named.
    - Now held: every number of The Christian East, vols. I-X (1920-1929), and vol. XI, nos. 1-3 (1930); every volume of The International Review of Missions from 1914 to 1930.
    - Not taken, and ruled out by Mark: the Proceedings of the Church Missionary Society for 1910-1921 (twelve volumes, `per_proceedings-church-missionary-soc-for-africa-a_<year>`). Each title page prints a year from 1910 to 1921. They were scanned from a microfilm whose target leaf, on the item for 1912, reads "Film No 96566 ... 1801-1920 / © MM 1967 / Reproduction of this film prohibited". A film maker's notice on the scan is not a basis the rights rule or R1 to R12 list, so none was vendored. Mark's ruling R15, as the coordinator passed it on (2026-11-16, "Yes, keep them held (Recommended)"): a microfilm maker's notice on a scan blocks taking it, even when the print is old; the Proceedings from that film stay out for every year; another scan of the same print with no notice may be taken. Searched the same day: archive.org has no other scan for 1906-1921; HathiTrust's catalog search and the Google Books search refused the requests (HTTP 403 and 429). Still to try: a browser search of HathiTrust and Google Books by hand. Owner: the Library thread.
    - Held for Mark, past the line: The Christian East, vol. XI, no. 4. Its cover and masthead print "Winter, 1930-31" and a footnote cites a letter of March 11th, 1931, so it was printed in 1931 and is free from January 2027. Owner: Mark.
    - Located and left for a later batch of era 10 (Open-Gaps 303, by the coordinator): The International Review of Missions for 1912 (three numbers on the host, January, July and October) and 1913; the Proceedings of the Church Missionary Society for 1906-1909 are on the same film and stay out under the ruling above.
    - Located, era 9, not fetched and out under the ruling: the Proceedings of the Church Missionary Society before 1906, on the same film. The reel leaders of the films behind The Christian East and the International Review could not be viewed (the raw reel scans are access-restricted on the host); no notice stands in any leaf or OCR line of the items taken.
    - Two further rulings came with this batch and are recorded in the Source Library Decision-Log ("Era 10, batch 2b, the periodicals") and in `cic/texts/INTAKE.md` section 2: R13, an institution's report counts by a date printed in its own text when read on the page image (Mark, 2026-11-16: "Yes, with a page-image check (Recommended)"), under which the Pacific Garden Mission's statement of 1916 is owed to the next batch; and R14, a host's own additions may be removed at intake with the exact text, line count, host URL and original byte count recorded (Mark, 2026-11-16: "Allow it, with a note (Recommended)"), to which the headers of the Путь files on main are still to be brought. Owner: the Library thread.
    - Not on the host's list: the April 1912 number of the International Review. Not taken: the yearly index items of the International Review (each volume taken carries its own index); The Christian East after 1930.
    - Calls this thread made, which the coordinator or Mark may overrule: the International Review for 1914-1920 shelved on the Student Volunteer Movement and Edinburgh 1910 entry and the later volumes on the ecumenical movement entry; shelf rows for Bulgakov, Kartashev, Fedotov, Zankov and Parenta placed by who the writers are, where the print gives only a name; no shelf row for documents of the patriarchates of Alexandria and Jerusalem, the Old Catholics, or the Church of the East's metropolitan in India, which have no census entry.
    - Census gaps met: the Greek Orthodox patriarchates of Alexandria, Jerusalem and Antioch after 1906; the Old Catholic churches after 1906; the Church of the East in India.
    - Not started, by the coordinator's instruction: the books of batch 2's follow-on list (Open-Gaps 302); all rendering.

304. **Dominic and John of Ephesus: Mark's rulings applied, and what stays open (data release 47, 2026-11-16).** Source: Decision-Log, "Dominic Sells His Books and the John of Ephesus mission card, told from the held texts" (2026-11-16). This closes the two cards held for Mark in Open-Gaps 296. The audit is `Build/Ministry/Operations/Audits/2026-11-16_cft-held-cards/`. Owner: the map, except where another owner is named.
    - Dominic: the inquest year 1233 and "Bologna" stand in the source line, not in a held line found by this work. The when field is "undated; while he studied at Palencia", because none of the three witnesses gives a year.
    - Dominic: the English pointers (Tugwell, Lehner) and the John of Ephesus reference (Harvey) are not held.
    - John of Ephesus: the counts differ chapter by chapter. The Lives give 80,000 converts with 98 churches, 12 monasteries and 7 churches from synagogues (Brooks, PO 18, l.39043-39046), and another count in ch. 43. The Ecclesiastical History gives 99 churches and 12 monasteries (Payne Smith II.44, l.9004-9005). Michael the Syrian, quoting John, gives 96 churches and 70,000. The card gives the first two. The John of Ephesus Who page (`cft-website/tree/john-of-ephesus.html`) gives Michael's figure and "many thousands" and was not edited here.
    - Other cards with words the round 3 reviewer flagged, not edited here: "only held source" on the council-of-dvin-609 card, a public page; "still a layman" and "on his own account" on other cards.
    - Sentences of 26 to 28 words remain on the Dominic card (round 2, N1).

305. **Library, the year audit: header years against the host's dates (2026-11-16).** A read-only list of every held file under `cic/texts` whose header year differs from the host's date for the same scan, each read on the page image: 2,424 files, 1,996 in agreement, 206 that differ (header right in 189, wrong in 12, not settled by the scan in 5). No file was changed. The record is `Build/Ministry/Operations/Audits/2026-11-16_library-year-audit/README.md`. Not comparable by this method: 123 files that name no archive.org scan, 82 whose host record gives no date, 8 whose named item the host does not return, 9 with no header year. The list is done; what it found is carried by "Library, the Martyrs' Mirror swap" and "Library, the header corrections" (both 2026-11-16). Owner: the Library thread.

306. **The eight and Gregory and Benedict under the 2026-11-16 rendering rulings, and what the re-check of the 14 left for the era passes (2026-11-16).** Source: Decision-Log, "Renderings made at the point of use and checked twice; the fourteen re-checked" (2026-11-16); `Build/Ministry/Operations/Audits/2026-11-16_rendering-recheck/`.
    - For the era 3 pass: Faustus of Riez, "After grace, without which we are nothing, we affirm the labor of dutiful service." In the Latin it is one sentence, and "post gratiam" can go with "walking" or with "we affirm". Splitting it into two quoted sentences picks one reading. Either way grace stays first. The fix is to quote it whole, or to note on the card that "after grace" may go with either verb. The re-check graded it minor.
    - For the era 3 pass: Faustus of Riez, "We are owners without a home of our own, and rich without possessions." The original grounds the paradox: it holds while God's faithful servants supply the exiles' needs. Add that reason in the prose before the quote, and note on the card that "sede" may also mean his bishop's see. The re-check graded it minor.
    - For the era 3 pass: John Moschus. The three listed renderings are of the Latin in Migne, not his Greek, and the "you" of the dedication is Sophronius (`john-moschus_pratum-spirituale-sophronius-opera-grc-lat_migne-pg87-3.txt` l.3775). The brief could name him.
    - For the era 2 and era 3 passes, re-recorded there and not in a separate run (Mark, 2026-11-16: "ok"). In each case the coordinator checked the original and found the brief right and the audio script wrong:
      - Faustus of Riez's audio script drops "then" (Latin "ergo").
      - Constantius of Lyon's drops "And yet" ("Et tamen").
      - Babai the Great's adds "and", which the French does not have.
    - At release of the eight, which waits for Mark's sample read and the paid recording: put each brief's quotation originals from `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/quotation-originals.json` on its census card, and list its renderings in `tools/quote_renderings.json` with their `second_reading`. The same goes for Gregory of Tours and Benedict at the era 3 release, from their cards' `quotationOriginals`.
    - For the eight's cards at release: Ephrem's "Look, on your behalf I appoint myself to run the shelter" carries the comparison's note, because the two renderings read "on your behalf" differently (as his agent, or for their sake). The final keeps the printed "on your behalf", which allows both. Constantine's "of the same essence" is the translator's gloss on homoousios, so the brief now tells it without quotation marks.

307. **Library, the Martyrs' Mirror swap (2026-11-16).** `van-braght_martyrs-mirror_sohm1886.txt` is held from a 2012 Herald Press printing whose title leaf's verso prints "Copyright © 1938 by Mennonite Publishing House". Mark ruled "Retire it, find the 1886 scan (Recommended)" and then "Swap now, then retire (Recommended)" (Library Decision-Log, "The year audit, the Martyrs' Mirror and the live-surface list"). The clean scan is archive.org item `bloodytheatreorm00brag` (Elkhart, Indiana, Mennonite Publishing Company, 1886, read on the page image). To do, in one pull request: vendor that scan; re-point the nine census sources and the shelf rows to the same passages in it; move the 2012 file to Archive. Every record that cites the held file is in `Build/Ministry/Operations/Audits/2026-11-16_library-year-audit/martyrs_mirror_citations.json`. Until then, nothing cites lines 102 to 130 of the held file, the publisher's preface to the second English edition. Owner: the Library thread; the census re-pointing with the coordinator.
    - 2026-11-16, the swap: the Elkhart printing of 1886 is held as `cic/texts/van-braght_martyrs-mirror_sohm-elkhart1886.txt` (archive.org item `bloodytheatreorm00brag`; title leaf and verso read on the page images; no film notice). The 2012 file and its staging file are in `Archive/Retired-Library-Texts/`. The nine census sources and the four shelf rows cite the same passages in the 1886 file. By the coordinator's call, three quotations take the 1886 spacing and spelling ("many places; at Ensisheim", "you; though ... (Col. 2:5)", "to-day"), and a word the scan breaks across a line end is shown whole, which `tools/validate-census.mjs` is taught to accept. The six census `work` fields that give the full title (five of the nine, and Dirk Willems's story source) now spell it "The Bloody Theatre", as the 1886 title leaf prints it. `Build/worlds/_cross-world/CORPUS-USE.md` is regenerated. Open, for the world-document work that follows the tree's release (the coordinator, 2026-11-16: not to be edited now): `Build/worlds/hus/Source_Registry.md` row 79 and `Build/World-Builds/Anabaptist-Movements/Source_Registry.md` still cite the retired file by name and by its line numbers. In the 1886 file the Hus and Taborite passages are at file lines 46672 to 46947 (the Taborites from 46824; the confession of 1431 named at 46910 and printed from 46924).
    - 2026-11-16, released: the census change ships as data release 49 (Decision-Log, "Data release 49: the Martyrs' Mirror quotations cite the 1886 Elkhart printing", 2026-11-16). The world-document rows named above stay open, and the list above is short. These also still cite the retired file by name, some with its line numbers: the six source-readiness dossiers in `Build/worlds/_cross-world/dossiers/` (Waldensian, Rhineland, Hussite, Anabaptist, Bosnian, Family of Love); `Build/worlds/hus/Open_Gaps_Tracking.md` and `Build/worlds/jes/Open_Gaps_Tracking.md`; and, as audit trail left as written, the hus Doc01 and Doc02 review files and the Anabaptist-Movements reviews. The full list is `Build/Ministry/Operations/Audits/2026-11-16_library-year-audit/martyrs_mirror_citations.json`. Owner: the world-document work that follows the tree's release.

308. **Library, the header corrections from the year audit (2026-11-16).** Twelve held files carry a wrong year in their headers, and one a wrong part number (`evliya-celebi_narrative-of-travels-v1-pt2_hammer1846.txt`: "Part I" for "VOL. I., PART II."). The files and what each page prints are in `Build/Ministry/Operations/Audits/2026-11-16_library-year-audit/README.md`; the Martyrs' Mirror among them is handled by the swap. None of the other eleven changes a rights call. To do: correct the year in each header, in the registry and on the shelves, with no file renames. Owner: the Library thread.
    - 2026-11-16, done in part: the year is corrected in the header, the registry and the shelf rows of ten files (Groves 1869; the Unity's Historie 1870; Reitz part 5, 1717; Isidore PL 83, 1862; Subbotin vol. 1, 1875; Booth-Tucker vol. 1, 1892; Mansi 26, 1903; the New Church liturgy 1792; Augustine PL 39, 1865; Cassiodorus PL 70, where the rights basis now says 1865), and Evliya's header gives the title page's 'VOL. I., PART II.'. No file was renamed and no header changed its line count. By the coordinator's call the same day: Lake's Diognetus keeps 1917 and Putnam, said to be the file's own TEI citation, and adds that the scan the TEI links prints MCMXIII, Heinemann and Macmillan; Cassiodorus's Publisher line gives the imprint year 1865 in place of the series range, with no new line. Closed.

309. **Library, Pliny the Younger's letter to Trajan (2026-11-16).** No Pliny file is held. Letter 10.96 and Trajan's reply exist in the Library only in English, inside McGiffert's note to Eusebius III.33 (`npnf201`), and as Tertullian retells them in Apology 2 (`anf03`). Because his own text is not on the shelf, Pliny was left out of the story-process calibration set (Decision-Log, "The story process", 2026-11-16). To do: vendor a rights-clear Latin text of Letters book 10 and an English translation. Owner: the source-research thread.

310. **Library, the Greek Martyrdom of Polycarp is hard to find and damaged (2026-11-16).** Found by the Polycarp clean write (`Build/Ministry/Operations/Audits/2026-11-16_polycarp-clean-write/Source_Sheet.md`, "Source file faults"). The Greek in `cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` cannot be read, which that file's own header says. The other copy of the same 1902 edition, `cic/texts/acta-martyrum-selecta_gebhardt1902.txt`, does hold readable Greek of the Martyrdom of Polycarp. But its header gives the language as "lat" and its Content note leaves the Martyrdom out, so the Greek cannot be found from the header. Its OCR also damages words that are quoted (Δεῖ, ἕξ, Αἶρε, Πεῖσον, Ἄφετε and others); the sheet lists them. To do: correct that file's Language and Content header lines. Then decide whether a cleaner Greek text of the Apostolic Fathers should be vendored. The Library holds no readable Greek of Polycarp's letter, Ignatius or Irenaeus. Owner: the Library thread.

311. **Spoken names for census traditions (2026-11-16).** Every brief names its person's tradition, and many census names cannot be said aloud ("Post-Apostolic Household-Church Christianity"). Two cold writers of the Polycarp brief each invented a gloss, and both misled (Decision-Log, "The tradition, in words a narrator can say aloud", 2026-11-16). For now, each source sheet's researcher writes a plain spoken form from the census entry's own description, and Mark sees it at spot checks. Open question for Mark: should the census carry one approved spoken name for each tradition, so every brief uses the same words? That is a tree-wide decision. Owner: the coordinator, to bring to Mark once calibration ends.

312. **Library, file faults found by the Ignatius calibration sheet (2026-11-16).** Nine are listed under "Source file faults" in `Build/Ministry/Operations/Audits/2026-11-16_ignatius-calibration/Source_Sheet.md`. In short:
    - ANF prints Ephesians chapter 20 twice, and gives Romans 10 in one recension only.
    - McGiffert cites Irenaeus V.18.3 for V.28.4.
    - Coxe's introduction places the first "Catholic Church" in Romans; it is in Smyrnaeans 8.
    - The Origen, Athanasius and Evagrius files have OCR faults in quoted words.
    - Two file names hide what they hold. The PG 50 Chrysostom file names only the homily on Lucian but holds the homily on Ignatius. The Origen tomus 5 file names Matthew but holds the Homilies on Luke.
    No file was changed. The sheet marks the editors' faults as card notes, and the renderings were made from corrected readings. To do: correct the headers and file descriptions where the registry allows. Owner: the Library thread.

313. **Cyril and Methodius brief: one sentence held for Mark (2026-11-17).** The varied first batch (Decision-Log, "A new way to make briefs", 2026-11-17) gives each brief one revision; a brief that still fails comes to Mark. The Cyril and Methodius brief's recheck (`Build/Ministry/Operations/Audits/2026-11-17_varied-batch/cyril-and-methodius/Review.md`, "Recheck") found one BLOCKING sentence left: the gloss "he served them in their own language", the writer's own reading, not in the outline. The reviewer's replacement: It calls Clement "the first bishop of the Bulgarian tongue". Because Bulgarian priests could barely follow Greek, he wrote them plain sermons for every feast. Three MINOR wording fixes are in the same section. The brief is unchanged until Mark rules. Owner: the coordinator.

314. **What the varied first batch showed about the kit (2026-11-17).** Found across all six briefs of `Build/Ministry/Operations/Audits/2026-11-17_varied-batch/`; each point is for Mark when he reads the batch.
    - Grade: five of six land at grade 6.2 to 7.7, under the 8 to 9 aim; only Cyril and Methodius reaches 8.1. Every reviewer judged the low ones plain rather than flat by the listener read.
    - Length: none meets its outline's word target. They run 352 to 463 words (about 2:20 to 3:05); writers report they could not reach the target without dropping a beat the outline gave them.
    - Impact share: three briefs first drafted under a third (Radegund about a fifth, Clement and Cyril and Methodius about 26 to 28%); revision brought each to about 27 to 38%.
    - The checks caught real faults: every outline had at least one BLOCKING finding against the source texts, and four of six briefs had one (an invented "as a young man", a wonder told in the narrator's voice, a death scene never told, an opening never tied back in).
    Owner: the coordinator, with Mark.

315. **What round two of the varied batch showed (2026-11-17).** For Mark with the round-two read (Decision-Log, "The review bar", 2026-11-17).
    - A fresh writer working from a checked outline repeated three errors round one had already fixed: Columba's gates wonder told in the narrator's voice, Clement's "long" search, and Radegund's revolt outcome. The outlines' wording leaves room for these, so each will recur with every new writer. Proposed: when a review finds and fixes such an error, the outline gains a "do not say" line.
    - The kit's `Standard.md` leaves out that the impact must tell what the person defended; `Outline_Template.md` still marks it. Antony's first round-two draft dropped his stand against the Arians. Proposed: restore it to the standard's impact line.
    - Length: round-two briefs run 347 to 456 words (about 2:20 to 3:05) against outlines set for 2 to 3 minutes; the adult voice takes more words than the round-one voice.
    Owner: the coordinator, with Mark.

316. **Marcion of Pontus's census card holds claims the held texts do not support (2026-11-17).** Found by the batch-two researcher (`Build/Ministry/Operations/Audits/2026-11-17_varied-batch-2/marcion-of-pontus/Source_Sheet.md`). The live card gives Sinope as his city, calls him a "wealthy shipowner", says his money was "returned", gives "ten letters" of Paul in his canon and dates him to 144. No held text supports Sinope, "wealthy shipowner" or the year; Tertullian says the money was cast out with him; the ten letters are not attested in the held sources. To do: re-check the card against the held texts when the Marcion brief is released, and correct or source each claim. Owner: the coordinator, at the era 1 release.

317. **Martin of Tours's census tile implies Sulpicius never met him (2026-11-17).** Found by the batch-two researcher (`Build/Ministry/Operations/Audits/2026-11-17_varied-batch-2/martin-of-tours/Source_Sheet.md`). Sulpicius Severus visited Martin late in Martin's life, as his own Life says. The held English of Sulpicius (Roberts, `npnf211`) also mistranslates one Trier sentence ("as long as Martin survived" for "as long as Martin was at Trier"); the outline's Do not say guards it. To do: correct the tile at the era 2 release, and note the translation fault in the Library file's notes. Owner: the coordinator; the Library thread for the file note.

318. **Marcion of Pontus brief: one phrase held for Mark (2026-11-17).** After its one revision, the last recheck (`Build/Ministry/Operations/Audits/2026-11-17_varied-batch-2/marcion-of-pontus/Review.md`, "Recheck") failed one phrase: "even Tertullian granted that", which turns his wasps jibe into a concession the record does not make. The reviewer's replacement: "Tertullian wrote that just as wasps make combs, so these Marcionites make churches." Everything else passed. The brief is unchanged until Mark rules. Owner: the coordinator.
    - 2026-11-17, ruled: Mark: "yes, apply the Marcion fix". The reviewer's sentence is applied word for word, with Justin's clause kept as its own sentence. Closed.

319. **The one-hearing test across both varied batches (2026-11-17).** Mark's test (Decision-Log, "The test a brief is written to", 2026-11-17) was run on the eleven briefs reviewed before it existed (`OneHearing_Test.md` in each folder). Columba and Benedict passed, as had Martin of Tours. Nine failed, each on one line only, and none on rigor. In eight of the nine the weak line was "why the connection matters": the brief told the person and the events, but left the tie to later people or the church as a list, an unclear "his", or an outcome with no link back (Antony, Clement, Cyril and Methodius, Macrina, Radegund, Marcion, Dhuoda, Hild). Nicaea's weak line was "what happened". Each is being fixed in its brief from its outline and rechecked. For Mark: the connection is the line writers most often leave implicit, so the standard or the outline's Links field may need to ask for it more directly. Owner: the coordinator, with Mark.

320. **The narration tool sends the `[pause]` tag to models that read it aloud (2026-11-17).** Found in the Nicaea review recording (Decision-Log, "Nicaea re-recorded; the pause tag", 2026-11-17). `requestTextFor` in `Build/tools/generate_tree_narration.mjs` puts `paragraphPause` ("[pause]") between paragraphs whenever pronunciations are loaded, whatever the model. `eleven_v4` honours it; `eleven_multilingual_v2`, Daniel's model for tradition and council briefs, speaks it. Any council brief recorded through the tool with pronunciations would carry the spoken word. To do: send the pause tag only to models that read audio tags (or give each voice its own pause form), with a test, before any council brief is recorded live; check whether any live Daniel recording already carries it. Owner: the coordinator.

321. **Council cards: the tree pages do not show the new council fields (2026-11-17).** The refreshed Nicaea entry (`Build/Ministry/Operations/Audits/2026-11-17_varied-batch-2/council-of-nicaea-325/council-of-nicaea-325.entry.json`) adds `howItWorked`, `stories` and quotations, by Mark's ruling "1 and 3 on the card". `Build/tools/generate_tree_pages.mjs` and the map card do not render those fields for councils yet. To do, at the Nicaea release: render them, with tests, as release 48 did for the Who card's quotations. Owner: the coordinator.

322. **What release 50 leaves (2026-11-17).** From data release 50 (Decision-Log, "Data release 50", 2026-11-17).
- *Dhuoda's recording.* The release fixed one rendering in her brief after its review take, so her brief is live as text with no recording. A new take is about 1,150 credits, beyond the approved cap of 7,500. For Mark.
- *Cyril and Methodius.* Their brief and card are finished, but they have no census person entry, so they are not released. For Mark.
- *Marcion census faults (Open-Gaps 316).* The person card is corrected ("the money cast out with him"). The unsupported claims named in 316 ("wealthy shipowner", the year 144, "ten letters of Paul") are in the tradition entry `marcion-marcionism` (its teaser, `longDescription`, `why` and `voices`), not in the person's entry. Changing that brief makes its live recording stale, so it is a tradition-brief rewrite with its own recording, still open.
- *Martin tile (Open-Gaps 317).* The line "Sulpitius Severus was not present for the events he describes" is in the built world `gallic-monastic-ascetic-christianity` (its `entry` tile), which comes from that world's compiled data. It is still open for the world's own records. The person card and brief already say Sulpicius met Martin late in his life.
- *Benedict's uncertain note.* It still explains the modern English of Benedict's words to Totila, a quotation his new brief no longer gives, along with the Acta Sanctorum source behind it. It is left alone under the card rule (new or clearly wrong only). For Mark: drop it at the next Benedict pass?
- *Minor second-reading notes, not changed.* Antony ("urged on" for admonitus), Macrina ("on her feet"), Columba ("most reverend"), Martin ("wrong" for nefas), Hild ("Denique" not carried) and Dhuoda ("my lord" for senior). Each is recorded as "minor" in its `Second_Readings.md`.

323. **Important findings from the four-reader evaluation that the release 50 fixes do not cover (2026-11-17).** From the evaluation of the twelve (https://claude.ai/artifact/MhbuqEzrLQwQ7PbrsKm6G5; Decision-Log, "No softening: a witness, not a judge…", 2026-11-17). Mark: "yes, add 5 to 7 and log the rest". Items 5 to 7 go into this round. These stay open:
- *Card scholarship stops around 1930.* Every modern voice on the cards is a public-domain editor from before 1930, and several are confessional: Ginzel against "the Greek schism", Gasquet the Benedictine. No current scholarship appears. The historian and the university teacher both marked this important, since students would cite these editors as authorities. The Library holds mostly public-domain editions, so this is a sourcing decision: how current scholarship may be named on a card, and from what. For Mark.
- *Marcion's card* says nothing of the modern debate over whether his gospel came before canonical Luke. It needs a held source that discusses the debate, so it is for the Library thread.
- *Benedict and the Rule of the Master.* The Prologue draws on the earlier Rule of the Master, but no held text discusses it (source sheet D4), so neither brief nor card names it. The Library thread is to look for a public-domain discussion.
- *The pieces do not point to each other,* though six of them (Antony, Martin, Benedict, Columba, Hild, Macrina) make a natural monasticism thread. This waits for the links, under Mark's ruling that they come once every Who and council is done (Decision-Log, 2026-11-17).
- *The census link from Nicaea to the later Homoian churches.* The census marks Nicaea's link to "Homoian ('Arian') Christianity" as Condemned, but the Homoian churches belong to the 350s and 360s; Nicaea condemned Arius and named teachings. The row's name is right for its own period, and the card's note is corrected. Whether the link should be marked differently, or carried by a row for Arius's own party, is a question about the tree's data. For Mark.

324. **What the variety check finds in the first twelve (2026-11-17).** The released and recorded first twelve, written under the kit lines replaced on 2026-11-17 (Decision-Log, "Variety of story…"), are still over the batch variety check on three moves:
- the opening reveal, 6 of 12 (Benedict, Columba, Cyril and Methodius, Hild, Macrina, Martin);
- the setting slot, 9;
- the ending on a later writer or institution, 12.

They are not rewritten now. Each is recorded, and a rewrite would mean recording it again. For Mark: leave them as they are, or bring them under the new lines at their next revision. The check applies from the next batch.

325. **Ruling on Open-Gaps 324, the first twelve and the variety check (2026-11-17).** Mark: "leave the twelve as they are, start the next batch in a new thread". The first twelve stay as released and recorded. Entry 324 is closed by this ruling. The variety check applies from the next batch.

326. **Batch 3, the confirming twelve: what is open at the end of authoring (2026-11-18).** Source: `Build/Ministry/Operations/Audits/2026-11-17_batch-3/` (README, Ledger, Variety_Check_run2, Card_Check, Second_Readings); Decision-Log, "Batch 3: the confirming twelve, on a frozen kit" (2026-11-17).
    - Three pieces failed their recheck after their one revision and come to Mark with the reason (`Process.md` step 5): the Third Council of Toledo (Saragossa's re-blessing of priests still missing; 552 words, near four minutes), Pachomius (the revision cut "at the start", so he seems always to have done all the work himself; 481 words) and the Council of Chalcedon (Severus misrendered; must-tell material cut to make room; a narrator's verdict, "came down to one letter"; 473 words). Each folder's `Recheck.md` holds the reason. Owner: Mark.
    - Arius's card keeps a claim not found as worded: "The churches later called Arian, which held with him that the Son was not eternal" (`legacy.traces[0]`). The held sources show one Homoian bishop, Palladius at Aquileia, refusing to call the Son everlasting (Mansi 3 60104–60110, 60152–60154; Kauffmann 5510, 5669–5670), not the churches as a body. Nothing held contradicts it, so it stays, flagged (`Card_Check.md`). Owner: the next Arius card pass.
    - The Latin Imitation of Christ is held, but under a misleading name: `cic/texts/kempis_opera-omnia-sermones-de-compunctione-lat_pohl1902.txt` is Pohl's Opera vol. II and holds the Imitation (line 598 onward). Its name and header should say so. Owner: the Library thread.
    - The variety check's setting detector counts any early sentence with a year and a place. To clear it, three writers dropped or reworded a year (Wyclif's 1381, Chalcedon's 449, Pachomius's "in the year 346 or 348"). Owner: Mark, with the kit (the check is under the standard lock).
    - Moses the Black was slotted as a thin record (about one minute); the outline check found the record fuller and set two minutes. Only Alopen ran at about one minute. Owner: none; recorded for the exit report.

327. **Batch 3 after the rework: what is open (2026-11-18).** Source: `Build/Ministry/Operations/Audits/2026-11-17_batch-3/` (Ledger, each folder's `Card_Edits_2.md`, reviews and rechecks), and the Decision-Log entries of 2026-11-18. This updates the 2026-11-18 entry "Batch 3, the confirming twelve: what is open at the end of authoring". That entry's first point, the three held pieces coming to Mark, is closed: they were revised a second time and passed. All twelve were then reworked under the change order "the heart of their life, told in the first minute" and re-recorded.
    - **Person connection to build: Baudonivia wrote Radegund's Life.** Mark, 2026-11-18: "1, keep both and link them". Both stay as person entries. The typed connection, Baudonivia "wrote her life" → Radegund, is made when the connections build runs, as ruled on 2026-11-17 ("we can do the actual links later when all the who and councils are done"). Until then each card names the other in its text.
    - **Card claims not found, left in place for the checker:** Toledo's "two damaged places" in the printed text (only one found); Toledo's "nostram catholicam fidem" reading (contested); Chalcedon's "Leo's legates presided over the votes" and "the Greek text of the definition now reads 'of two natures'"; Arius's legacy trace "held with him that the Son was not eternal"; Narsai's "a long fight against Satan" (loosely supported).
    - **A claim outside this batch:** the Devotio Moderna movement's teaser says it "produced the most copied book of the Middle Ages after the Bible". The only held claim is J. M. Neale's "probably". Kempis's own teaser was corrected in release 51. The movement's teaser is for its entry's owner.
    - **Detector and length, for the batch 4 kit:** the variety detector can be beaten by dropping dates, and a recast once cut the heart of a piece (Alopen's 1625 finding). Lengths are now set per voice, from measured rates (Neo about 150 words a minute, Daniel about 128). Councils still run long: Chalcedon 4:19, Toledo 3:02.
    - **Partial second readings carried:** Kempis's "the little Gerson", Justin's "the only philosophy that is sure and useful" and Wyclif's one-sentence Hus line each carry the verdict of an earlier blind reading of the whole passage that holds them. No separate reading was made.

328. **The heart back-check of batches 1 and 2: what is open (2026-11-18).** Source: `Build/Ministry/Operations/Audits/2026-11-18_heart-backcheck/` (one `Heart_Test.md` for each piece); Decision-Log, "Heart checks on batches 1 and 2; batch 4 is their rework" (2026-11-18).
    - All twelve miss the heart in the first minute. They are reworked as batch 4. Owner: the coordinator.
    - The older person briefs, about 238 of the census's 250, were written before the heart rule, to the same habit of a scene and a witness first. Whether to screen them, and how, is for Mark once batch 4 shows what the new kit does. Owner: Mark.
    - The readers' notes beyond the heart, for the batch 4 outlines' Do not say lists:
      - *Dhuoda.* "had him taken from her" leans toward the outline's forbidden "snatched from her"; the outline asks for "had him brought to him".
      - *Macrina.* The outline's beat on Basil (contested) is not in the story.
      - *Radegund.* The nuns' revolt detail ("insulted and humiliated") goes past the outline, though Gregory supports it.
      - *Cyril and Methodius.* The outline's beats never name the brothers' translation of the Gospel, Apostle and Psalter (source sheet M20, Widely Accepted).
      - *Antony.* His guiding of the monks as a father (source sheet E9) is not in the outline.
      - *Hild.* The kings and princes who sought her advice (census `knownFor`, outline quote 2) are never used.

329. **Batch 4, the rework of batches 1 and 2: what is open at the end of authoring (2026-11-18).** Source: `Build/Ministry/Operations/Audits/2026-11-18_batch-4/` (README, each folder's Review, Revision, Card_Edits and Card_Check, Second_Readings.md, Adjustment_Check.md); `Build/Ministry/Operations/Audits/2026-11-18_cft-needs-read/`; the Decision-Log entries of 2026-11-18. This updates the 2026-11-18 entry "The heart back-check of batches 1 and 2: what is open". That entry's first point, the twelve reworked as batch 4, is done; they are authored and in the census, and only the recording is left.
    - **For Mark:**
      - Cyril and Methodius has no census person entry, so its finished story and card are not released.
      - Benedict's card keeps `uncertain[5]`, the note on the Totila rendering. The card check would remove it, but Open-Gaps 322 left it for him.
      - Whether to screen the other person briefs, about 226 of the census's 250 now that 24 have the new kit, against the heart and the one-hearing rules.
    - **Recording.** ElevenLabs reported a partial outage from about 15:40 UTC, and its API did not answer. Recording waits on it. Mark's go-ahead is "record and finish the batches" (2026-11-18). Owner: the coordinator.
    - **Batch 3's recorded pieces with the faults the listeners named.** Justin, Vardan, Narsai and Arius are told out of order or twice. Chalcedon and Toledo have too many names. Arius and Nicaea shared material until Nicaea was adjusted. Baudonivia's story is mostly Radegund's. They are recorded, so changing them means recording them again. For Mark, after the batch 5 kit.
    - **For the batch 5 kit** (`2026-11-18_cft-needs-read/`):
      - one line through the life, nothing told twice;
      - a names budget;
      - sibling pieces briefed together, with one spelling for each name;
      - the stock "almost all we know" line;
      - an optional line about today.
    - **For the site:** person pages link only to their tradition. A "named in this story" list, like the council pages have, would carry the links. Owner: a site build.
    - **For the slate:** no piece yet tells how the Church of the East came to stand apart, and Protestant figures are few so far.
    - **Readings with a stated limit:**
      - B4-17, Cyril and Methodius, "the first bishop of the Bulgarian tongue": the Greek is unreadable OCR, so the verdict rests on the Latin.
      - B4-16, "who wants to be called a heretic?": the held Latin is itself a translation of the Slavonic Life.
      - Hild's "a bishop led the church of a whole region" is the narrator's summary of three Bede passages (source sheet B1), not Bede's words.

330. **The batch 5 kit: what is open (2026-11-18).** Source: Decision-Log, "The brief kit for batch 5, as one document" (2026-11-18). This updates the 2026-11-18 entry "Batch 4, the rework of batches 1 and 2: what is open at the end of authoring". Its five kit points (one line, names, siblings, the stock how-we-know line, a line about today) are decided and in `Brief-Kit/Kit.md`.
    - **Shared quotes already live.** The first run of `tools/check_tree_overlap.py` over batches 3 and 4 finds three quotes another finished story also uses: Nicaea and Constantinople 381 both quote "shall not be set aside"; Arius shares "of one substance with the Father" with Ariminum and Seleucia, Eunomius and Constantinople 381, and Jerome's "groaned, and was astonished to find itself Arian" with Ariminum and Seleucia. Under Mark's scope ruling these stories stay as they are. Whether a creed's own formula counts as a shared quote is Mark's call when it next arises. Owner: Mark.
    - **Batch 4 recording balance.** Closed: the recheck matches the 13,619 credits charged (`Build/Ministry/Operations/Audits/2026-11-18_batch-4/recording/Balance.md`).

331. **Batch 5, twelve stories on the batch 5 kit: what is open at release (2026-11-19).** Source: `Build/Ministry/Operations/Audits/2026-11-18_batch-5/` (README, each folder's Reshape_Review, Card_Check and Recheck files, Second_Readings.md, Release.md); `Build/Ministry/Operations/Audits/2026-11-19_batch-5-read/`; the Decision-Log entry "Batch 5 hearts: church words explained, and Luther's job re-set" (2026-11-18). The twelve are authored, reshaped to the lengths Mark approved, carded, read blind and in the census; only the recording is left.
    - **Recording.** Done 2026-11-19: all twelve, 21,554 credits under a 22,000 cap (`recording/Balance.md`).
    - **Barsauma, reworked under Mark's cap ruling (2026-11-19).** Closed: the rework review's MINOR 2, Narsai in one clause, is applied word for word (Mark: "yes add narsai to barsaumas story") and the story re-recorded.
    - **Patrick's held scan reading.** Source sheet line 3009, "— I": the page image must be checked. The released story no longer quotes those lines, so the census carries none of Patrick's six readings. Owner: the Library thread.
    - **Census fields outside the story and card.** Tyndale's `sourcing` says "two volumes" are held; it should be checked against `cic/texts/`. Owner: a census pass.
    - **Library.** Wesley's Journal volume 1 has a header error. Wants: Mingana's 1928 English of Timothy's debate, Timothy's letter on Aristotle, Luther's German Bible. Owner: the Library thread.
    - **Outlines behind fixes made in the brief and card.** Cyril's outline still says "of God the Word" in six places where the record reads "one incarnate nature of the Word"; Wesley's outline beat 4 still says "a fellow priest". The released story and card are right. Owner: the next batch that reuses these outlines.
    - **Athanasius's essence** ends at word 177, past the kit's 150; the reshape reviewer advised leaving it. For Mark, if he wants it held to the rule.
    - **Drift read, for future batches, not changes to batch 5** (`2026-11-19_batch-5-read/`): one template across all twelve (held-back name reveal in 8, a résumé second paragraph in 12, later history near the end in 11, a quiet closing line in 10); church-word glosses given by rule to common words and stacked in chains; names and dates crowded in Barsauma, Athanasius and Calvin; Barsauma the one story readers lose. The scholar asks for one settled gloss per church term across the tree ("bishop", "deacon", "indulgence"), disputed scholarship marked as disputed sources are, and Foxe flagged as partisan as Socrates is. Luther's writings against the Jews are not told while Cyril's acts are. For Mark, with the batch 6 kit.

332. **The stories approved before the kit: a consistency check when eras 1 and 2 are finished (2026-11-19).** Source: Mark, 2026-11-19: "Let's make a note to check them for consistency when we finish era one and two." These are the texts Mark approved before the brief kit:
    - Standard v1, live and recorded since data release 48 (2026-11-16): Origen, Methodius of Olympus, Constantine, Ephrem, Gregory of Nazianzus, Gregory of Nyssa, John Chrysostom (`Who-Profiles/bar/`) and Gregory of Tours (era 3).
    - Polycarp of Smyrna, approved on 2026-11-16 (the clean write) and not yet live.
    - Once every other era 1 and era 2 story is on the kit, they are read beside their kit siblings. The read covers the kit's one-hearing rules: the essence in the first minute, one line through the life, names, how-we-know beside the claim, and no shared quotes. Mark then rules on what, if anything, changes. `python tools/list_story_status.py` lists them; Polycarp is named in `Earlier-Approved.yaml`. Owner: Mark, at the end of era 2.
    - The bar README's line "The live text and the audio still carry the older wording" is stale: the eight went live in data release 48. Owner: the Church Family Tree coordinator, for a doc fix.

333. **An app version of the Church Family Tree: deferred (2026-11-19).** Source: Decision-Log, "The Family Tree stays a website for now; an app is looked at later" (2026-11-19).
    - **Open.** Whether to offer the tree as an installable web app or a store app. The deciding question is what an app should do that the site does not. Owner: Mark, when he takes it up.
    - **First step for either route.** The map's data is built into `cft-website/index.html`. Moving it into its own file lets content update without re-releasing an app. Owner: a site build, only once an app route is chosen.

334. **Review checkmarks for rewritten Who profiles: remove when the rewrite is done (2026-11-19).** Source: Decision-Log, "Review checkmarks for rewritten Who profiles, seen only with a review link" (2026-11-19).
    - **Open.** The `?review` checkmarks in `cft-website/index.html` (`REVIEW_MODE`, `reviewMark` and the `.rv-done` style) are temporary. Remove them once every Who profile has been rewritten. Owner: the site thread, on Mark's word that the rewrite is done.
    - **What it counts.** A person counts as rewritten when their card has `briefReferences`. A rewritten card without that field would show no check; if that happens, the rule needs another look. Owner: the batch threads, by noticing it in review.

335. **Batch 6, era 1 (twelve stories and Polycarp): what is open at release (2026-11-19).** Source: `Build/Ministry/Operations/Audits/2026-11-19_batch-6/` (README, each folder's Review, Revision, Recheck_Story, Card_Check, `Batch_Originals_Ruling.md`, `Card_Apply.md`, `Second_Readings.md`); the Decision-Log entries of 2026-11-19 headed "Batch 6". The twelve and Polycarp are authored, carded, read blind and in the census; only the recording is left.
    - **Recording.** Waits on Mark's approval and a credit cap. Owner: the coordinator.
    - **The census check cannot test Greek.** `fold()` in `tools/validate-census.mjs` keeps only a-z and 0-9, so any Greek `printed` or `original` passes, right or wrong. Batch 6's Greek was checked by hand (`Batch_Originals_Ruling.md`), and Greek that no held print confirms was left off the cards. Owner: a tools pass.
    - **Library wants.** A modern study of Josephus's passage on Jesus (the latest held view is Chabot's note of 1899; Mark, 2026-11-19, hearts entry, item 2). A clean Greek of the Apostolic Fathers (Ignatius, Polycarp), of the Shepherd of Hermas, of Irenaeus's Against Heresies, and of Tacitus's Annals 15 in Latin; each card now prints the English where the scan could not be confirmed. Owner: the Library thread.
    - **Irenaeus's essence** completes at about word 175, after the 51-word opening quote and its gloss; the recheck ruled it meets "about 150". Reaching 150 exactly needs a change order to the outline's opening. For Mark, if he wants it held to the rule.
    - **Census fields outside the story and card.** Tatian's census `regions` lists Edessa, which no held source places him at; Hermas's earlier text spelled "Rhode", now "Rhoda" as the held text has it. Owner: a census pass.
    - **Drift counts** (`Variety_Report.txt`): seven of thirteen end on a later writer or institution, and five stack a time and place in one early sentence. For Mark, with the next kit review; nothing was recast because of them.

336. **The stories approved before the kit: reviewed in their era's batch (2026-11-19).** This updates the 2026-11-19 entry "The stories approved before the kit: a consistency check when eras 1 and 2 are finished". Mark: "Go ahead and include polycarp and others in the review process", then "All pre-kit stories" (Decision-Log, "Change order: the stories approved before the kit go through review in their era's batch", 2026-11-19). Each story approved before the kit is reviewed on the kit in its own era's batch, keeping approved wording wherever it passes: Polycarp in batch 6 (done; released with it), Origen and Methodius of Olympus in batch 7, Constantine, Ephrem, Gregory of Nazianzus, Gregory of Nyssa and John Chrysostom in the era 2 batches, Gregory of Tours in era 3. The end-of-era consistency read still follows. Owner: each era's batch.

337. **The census check now compares Greek (2026-11-19).** This closes the Greek point ("The census check cannot test Greek") of the 2026-11-19 entry "Batch 6, era 1 (twelve stories and Polycarp): what is open at release". `fold()` in `tools/validate-census.mjs` now keeps Greek letters beside a-z and 0-9. Accents, breathings and iota subscripts are set aside as Latin accents are (NFKD, then the combining marks removed), final sigma is read as σ, and NFKD reads the scans' letter forms (ϑ, ϲ, ϐ, ϕ and the like) as their plain letters. So a Greek `printed` or `original` must stand at its file and lines, and Greek quoted in a brief's prose is checked against the files it cites. `tools/tests/validate_census_quotation_originals.test.mjs` adds a Greek match (Polycarp's "Τὸ ϑέλημα τοῦ ϑεοῦ γενέσθω", written unaccented with θ) and a Greek mismatch (one word changed). Three cards failed once Greek was compared, and each was fixed under the rule in `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Batch_Originals_Ruling.md`:
    - **arius, `quotationOriginals[0].printed`** (Oehler's Epiphanius, 45736-45738). Line 45737, inside the span, is scanned apparatus; it is now a dropped range in `tools/quote_scan_readings.json`. The card copied the scan's ᾿Δρχὴν and ἀναρχός. Theodoret's Greek of the same letter prints "᾿Αρχὴν ἔχει ὁ Υἱὸς, ὁ δὲ Θεὸς ἄναρχός ἐστι." (`theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt` 70616), which confirms both readings. They are added to `tools/quote_scan_readings.json`, and the card now prints Ἀρχὴν and ἄναρχός, with its `uncertain` naming that print.
    - **macrina-the-younger, `quotationOriginals[0].printed`** (Migne PG 46, 71687-71690). The card printed the scan's φόθον, while a reading added in batch 4 read it φόβον. No held print has this Greek, so φόβον is not confirmed. The Greek is left off: `printed` is now Clarke's English, "Thou, O Lord, hast freed us from the fear of death." (`gregory-nyssa_life-of-macrina_clarke1916.txt` 230), and the unconfirmed φόβον reading is removed. The brief's rendering still follows the Greek (`tools/quote_renderings.json`, unchanged).
    - **cyril-of-alexandria, `quotationOriginals[1].original`** (Pusey 1872, 954-957). The scan sets the edition's margin number "2" after πρῶτον. A stray mark, so it is read out in `tools/quote_scan_readings.json`; the card is unchanged.
    - The census, the map's data (`cft-website/index.html`) and the two tree pages (`arius.html`, `macrina-the-younger.html`) carry the card changes. Owner: closed.

338. **Cyril and Methodius released (2026-11-19).** This closes the first "For Mark" point ("Cyril and Methodius has no census person entry") of the 2026-11-18 entry "Batch 4, the rework of batches 1 and 2: what is open at the end of authoring". Mark: "Add one entry for both (Recommended)" (Decision-Log, "Cyril and Methodius get one person entry", 2026-11-19). The census now has the person entry `cyril-and-methodius`, told within `cyrillo-methodian-slavic-christianity`, carrying the batch 4 story and card unchanged, with its eight renderings (and the card's three unpunctuated forms) listed in `tools/quote_renderings.json` against `Build/Ministry/Operations/Audits/2026-11-18_batch-4/Second_Readings.md`. An independent census pass found the new fields consistent with the card and the source sheet; its one note, that the year 863 for their arrival is Ginzel's while Lützow gives 862, is left as is, since the entry's `dates` do not state it. The story is recorded (`Build/Ministry/Operations/Audits/2026-11-18_batch-4/recording/Cyril_and_Methodius.md`, 1,343 credits).

339. **Built worlds in the standard voices: rewrite, then record (2026-11-20).** Source: Decision-Log, "Built worlds on the tree move to the standard voices, after a rewrite into the narrator's voice" (2026-11-20).
    - **The writing.** The 11 built worlds' Story, Legacy and documented stories (122 pieces) are rewritten from the world's own voice into the tree's narrator voice, through `Brief-Kit/Kit.md`, with quotes rechecked against the vendored sources. Owner: a dedicated rewrite thread.
    - **The recording.** Tree-only copies in Daniel (Story, Legacy) and Neo (stories), on the printed settings, after a sample Mark approves. `Build/tools/generate_world_narration.mjs` writes only to `cic-website/audio/worlds/`, which Church in Conversation also plays, so it needs an output folder for the tree's copies, and the map must read them. Owner: the site thread, once the texts pass review.

340. **Built worlds in the standard voices: the writing is done, hand-off for recording (2026-11-20).** This closes "The writing" in the 2026-11-20 entry "Built worlds in the standard voices: rewrite, then record". Rulings: Decision-Log, "How the built worlds' texts are rewritten for the tree" and "The narrator calls the Donatists' opponents 'Caecilian's church'" (both 2026-11-20).
    - **The texts.** All 122 pieces of the 11 built worlds are rewritten into the narrator's voice and have passed review: rewrite (Sonnet), independent review (Opus), one revision, and a targeted recheck (Opus), with no piece past the three-round cap. They are in `World-Narration/<census-id>/<key>.txt`, one per piece, keyed as `worldPieces()` in `Build/tools/generate_world_narration.mjs` keys them (`story`, `legacy`, `docstory-<story id>`). `World-Narration/README.md` gives the layout; the review trail is in each world's folder. All 122 pass `engine.m1.profile_readability` (0 failing). Every quoted span is the world's own, word for word, except one: the Arsinoite conference quote now uses its quote record's modern rendering (`alx.quote.dionysius-nepos`), checked in its source.
    - **Faults found in the worlds' own texts.** Corrected in the tree's texts and logged for each world's record owner: pahc OG-51, cappadocian OG-65, rzg 88, desert OG-51, syr 48, alx OG-42, ijc 52, witt OG-98, don OG-61 (a gap the tree's Story shares, since the rewrite keeps content). Church in Conversation keeps saying them until the records are fixed.
    - **Staleness.** Each piece keeps `<key>.orig.txt`, the world text it was rewritten from. Before recording, and whenever a world is rebuilt, compare `worldPieces()` of `cic-website/data/worlds/<id>.json` with these files; a piece whose source changed is stale and goes back through the rewrite.
    - **For the site thread: the recording.**
      - `generate_world_narration.mjs` reads the compiled world JSON and writes to `cic-website/audio/worlds/`, which Church in Conversation plays. It needs a tree mode that takes each piece's text from `World-Narration/<id>/<key>.txt` (split into paragraphs as now), refuses a piece whose `.orig.txt` no longer matches the compiled text, and writes to a tree-only folder and manifest, with a text hash per piece so the map plays a recording only for the text it shows.
      - The map (`cft-website/index.html`, which today reads `audio/worlds/manifest.json` and renders the compiled world JSON) must show these texts on built-world cards and play the tree-only recordings. Church in Conversation keeps its texts and Representative voices.
      - Voices (Mark, 2026-11-20): Daniel `onwK4e9ZLuTAKqWW03F9`, `eleven_multilingual_v2`, for Story and Legacy (22 pieces, 50,042 characters); Neo `onegjDE2z0mQtp1g0HK7`, `eleven_v4`, for documented stories (100 pieces, 104,095 characters); both `mp3_44100_64`, settings `{"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true}`. 154,137 characters in all.
      - A paid bulk run: a sample of each voice for Mark's ear first, then the run with every setting passed on the command and printed, item and character counts confirmed from the printed output, and a named cap.
    - Owner: the site thread.

341. **Built worlds in the standard voices: recorded and released (2026-11-20).** Source: Decision-Log, "Built worlds on the tree recorded in the standard voices, and released" (2026-11-20). This closes "The recording" in the entries "Built worlds in the standard voices: rewrite, then record" and "Built worlds in the standard voices: the writing is done, hand-off for recording" (both 2026-11-20). All 122 pieces are recorded and live on the tree.
    - **Open.** When a built world is rebuilt, run `generate_world_narration.mjs --world <id> --tree --dry-run`: a piece whose source changed is refused as stale and goes back through the rewrite before it is recorded again. Owner: whoever rebuilds the world.

342. **On a phone, names cross neighbouring rivers when the map is zoomed out (2026-11-21).** Source: Decision-Log, "A tradition's name moves to the other side of its mark when its first side would cross another river" (2026-11-21), and Mark's ruling in that session.
    - **What it is.** A tradition's name runs sideways, and the rivers are close together at small sizes, so some names lie across a neighbouring river's band. Measured on a 390 px phone, after names move to their clearer side: at zoom 0.2 (whole map) 25 of 52 shown names cross, at 0.35 28 of 102, at 0.5 13 of 152, at 0.7 19 of 299. On desktop it is 13 of 119 at the farthest zoom-out and 18 of 350 at 0.8. The share falls as the rivers spread apart on screen.
    - **Accepted (Mark, 2026-11-21: "i am not sure on a phone we can avoid crossing without loosing the flow and feel").** Fewer names would not fix it, because it is a width problem, not a count problem. Treating the other rivers as taken space, cutting names to the gap, or shrinking type on phones would each cost names, readability or the sense of scope. Left as it is. The names keep their light outline so the text stays readable over a river.
    - **Open if it is revisited.** Option A, treat other rivers as taken space so a crossing name is replaced by the next most connected name that fits; option B, cut the name to the gap with an ellipsis; option C, smaller type or two lines at the whole-map view on phones only.
    - **Related, not changed.** 14 of 350 traditions sit off their own river at their date in the census data (for example Cappadocian Christianity, Bogomils, Lutheran Wittenberg), which also puts their marks beside another river. On desktop the era 2 title crosses the first river's line at the opening zoom.
    - Owner: Mark, if it is revisited.

343. **Batch 7, era 1 (eleven stories, with Origen and Methodius reviewed): what is open at release (2026-11-21).** Source: `Build/Ministry/Operations/Audits/2026-11-20_batch-7/` (README, each folder's Outline_Check, Cut_Check, Review, Recheck_Story, Card_Check, `Batch_Originals_Ruling.md`, `Card_Apply.md`, `Second_Readings.md`, `Release.md`, `recording/Balance.md`); the Decision-Log entries of 2026-11-20 and 2026-11-21 headed "Batch 7". The thirteen are authored, carded, read blind, in the census and the tree pages, and recorded (22,424 credits of a 24,500 cap). Era 1 is finished.
    - **Census fields outside the story and card say more than the sources.** Tertullian's entry calls him the first to write in Latin (Mark ruled "foremost", 2026-11-20), an "advocate" (Eusebius says only versed in Roman law) and says he "invented" the Latin words (the sources say he put them to work). Cyprian's `teaser` states "two years after baptism" as fact (an editors' reckoning), and its `why` tells the "master" story as fact (Jerome's report at two removes); its `legacy` names Facundus, whom no batch source holds. Lactantius's `dates` and `end` give 325, but no held source gives a year of death, and its `why` and `teaser` say the Divine Institutes open with an address to Constantine, which some copies carry and whose authorship is disputed. Owner: a census pass.
    - **Lengths.** Mark held every story to about 4:00 and no more than about 4:30 (Decision-Log, 2026-11-20). Most landed at 4:15 to 4:30, so the 4:00 aim was mostly missed; Tertullian runs 678 words, three past the line, to keep the gloss of "Paraclete". Outlines still planned five to seven minutes of beats after the kit's count-first rule. For Mark, with the next kit review.
    - **Library wants.** A clean Greek of Eusebius's Church History (Schwartz's scan is damaged at several quoted passages), of Epiphanius's Panarion and of Dionysius's letters; the Latin of Peter of Alexandria's canons (Maffei); Stephen's Life of Wilfrid and Columbanus's letters (Anatolius); a held English of Jerome's Chronicle. Each card prints the English where the scan could not be confirmed. Owner: the Library thread.
    - **Claims left on existing cards, not found in held sources.** Peter of Alexandria: Coptic and Ethiopic lives giving his family. Novatian: Hefele's "fifth century" for how long his church lasted was not added. Owner: a card pass.
    - **Scan readings not added, by ruling.** Wilfrid's Latin (Plummer) carries only the second half of the speech, for a side-note run into one line; Lactantius's Jerome is cited from Prosper's clean copy, not Fotheringham's print. Owner: none unless a card needs the fuller text.
    - **Drift counts** (`Variety_Report.txt`): six of thirteen end on a later writer or institution, four open a sentence with "Yet", four stack a time and place early. For Mark, with the next kit review; nothing was recast because of them.

344. **The stories approved before the kit: Origen and Methodius done (2026-11-21).** This updates "The stories approved before the kit: reviewed in their era's batch" (2026-11-19). Origen and Methodius of Olympus were reviewed in batch 7 under the change order of 2026-11-19. Each took two fixes: Origen's torture under Decius restored and his death moved to the end; Methodius's Banquet of the Ten Virgins restored and his death moved to the end. Both were rechecked, re-carded and re-recorded. Still to come: Constantine, Ephrem, Gregory of Nazianzus, Gregory of Nyssa and John Chrysostom in the era 2 batches (`Launch-Prompts/CFT_Era2_Batch1_Launch_2026-11-21.md`), Gregory of Tours in era 3. Owner: each era's batch.
345. **Launch review: three small items left after the four fixes (2026-11-21).** Found in the launch-readiness review Mark asked for ("Launch readiness: four fixes before the announcement", Decision-Log, 2026-11-21).
    - The map's embedded data (`DATA` in `cft-website/index.html`) has older `informalName` values than the census for seven entries, so a card can show a stale name: Tertullian's card reads "Also called Tertullian's Voice" though the census now says "Tertullian of Carthage". The others: cappadocian-nicene-pastoral-monastic-tradition, gallic-monastic-ascetic-christianity, cyrilline-miaphysite-egyptian-christianity, church-of-the-east-timur-to-hakkari, iglesia-ni-cristo-the-way-international-unificat, the-christian-right. Some may be deliberate map labels; the map's owner decides which, and why the sync did not carry the rest.
    - The eleven built-world cards say "Conversations with [name] are coming soon to Church in Conversation." Mark's call whether that stays.
    - The tree's feedback form posts to the Church in Conversation server (`app.churchinconversation.com/api/feedback`), so feedback from the tree fails whenever that server is down.
346. **The First Churches river runs to 900 on one entry: is Christian Apocrypha a tradition on it? (2026-11-21).** Mark asked why the river runs on, empty, after the first era. A river runs from its first member's start to its last member's end. Era 2 is right: Ebionites, Montanism and Novatianism last to about 400. From 400 to 900 only `apocryphal-and-pseudepigraphal-literature` (Christian Apocrypha, 100–900) carries it, and it is a body of writings, not a community. Mark chose to review it ("c": review the record, and show where traditions end on the map). For the census owner: whether it stays a tradition on lane 0, becomes a story or a source, or takes an end date that measures a community. A record change, under its own review. The map side, an end mark for each tradition, is this thread's.

347. **The map's copy of the data synced to the census (2026-11-21).** Mark ruled the census right ("census is right, sync the map"). This closes the first point of "Launch review: three small items left after the four fixes" (2026-11-21) and goes past it: the comparison found 14 entries, not seven.
    - Synced in `DATA` in `cft-website/index.html`: Armenian Christianity, era 8, now on the Eastern Catholic river only; `regions` on three entries (Catholic Worker and its kin, Oneness Pentecostalism, Ethiopian and Eritrean Christianity); `informalName` on seven; `teaser` on two; the house church `why` ("Ignatius of Antioch"); and the file's `meta` block.
    - Left as they are: the ten built worlds' own text fields, which come from the compiled world files, and `livingEvidence` and `reviewStatus`, which the map does not carry.
    - **Open.** `meta.license.credit` in the census says "release 44 (November 15, 2026)" while `meta.release` says 49. For the census owner. The map carries no check that its copy matches the census, so it can drift again; a CI comparison of the shared fields is the fix.

348. **Batch 8, eras 2, 5, 6 and 7 (nine new people, three era 2 rewrites, Constantine reviewed): what is open at release (2026-11-21).** Source: `Build/Ministry/Operations/Audits/2026-11-21_batch-8/` (README, each folder's Researcher_Reply, Outline_Check, Review, Recheck_Story, Card_Check, `Card_Apply.md`, `Second_Readings.md`, `Census_Check.md`, `Release.md`, `recording/Balance.md`); the Decision-Log entries of 2026-11-21 headed "Batch 8" and "Kit change order: reused quotes, fewer blind readings, hearts and lengths at one stop". The twelve are authored, carded, read blind, in the census and the tree pages, and recorded. Constantine passed review unchanged and was not re-recorded.
    - **Census fields outside the story and card say more than the sources.** Cranmer's story says he "watched Ridley and Latimer burn" (Foxe says otherwise) and counts six recantations. Catherine's tradition story gives "nearly four hundred" letters and the needle in her foot; nothing held supports either. Teresa's tradition entry gives Toledo, 7 July and "shown to no one" for Báñez's report; Lewis's Life (LIFE-L 2159–2162, 2189, 2194–2196) supports the examination but places the tribunal at Madrid. Francis's tradition gives "cloth merchant", "by 1209" and Greccio unsourced. Bernard's tradition tells the Rhine story unsourced. Ambrose's `voices` calls him the "first churchman to make an emperor do public penance". Jerome's `why` and `floorNote`; the Hussite story's "emperor" (Sigismund was king until 1433); the Ambrosian tradition's "within a week" and "in 386". Owner: a census pass.
    - **Lengths.** Mark ruled four lengths after review (Decision-Log, "Batch 8: four lengths after review"). Ten stories run 656 to 680 words; Ambrose 724 (about 4:50) and Hus 766 (about 5:05). The outlines again planned more than 4:30 could hold, and nine of twelve drafts ran long. Writers also cut parts outside the cut-first lists (Hus, Catherine and others), which the reviews restored or Mark moved to the card. For Mark, with the kit review.
    - **Library wants.** Ambrose's Latin letters and sermons; Bernard's Nivard passage (damaged scan only), Otto of Freising, Odo of Deuil, an English of De consideratione and the Lives; the Italian of Catherine's letters and a clean Raymond; Francis's Three Companions, the Assisi Compilation, the 1220 letter and a clean Canticle; Barlaam's writings and Palamas's captivity letters; Bullinger's chronicle, Myconius's Life and the German record of Zwingli's first debate; Spinka, Fudge, Kaminsky and clean Piccolomini and Mansi for Hus; Jerome's Latin letters, prefaces and Rufinus's Apology; Priscus for Leo; Teresa's Spanish beyond the Life; the 1323 bull and the Contra Gentiles; a clean Foxe and the Catholic eyewitness letter for Cranmer, and corpus-map entries (AUTHOR-IDS, WORKS, RETRIEVAL-HINTS) for Cranmer. Each card prints the English where the scan could not be confirmed. Owner: the Library thread.
    - **A card claim left open.** Leo's first card source keeps its `uncertain` note though Mansi is legible at that passage. Owner: a card pass.
    - **Bernard's shield.** The card quotes only the first clause: "blasphemorum" is faulty in both prints, so the fuller reading was not added (`Card_Apply.md`). Owner: the Library thread, if a clean print is found.
    - **A template slip.** The Constantine-only section of the reviewer prompt was left in every filled review prompt. Each reviewer ignored it, and no review was affected. Owner: the next batch's prompts.
    - **Drift counts** (`Variety_Report.txt`): six of thirteen open a sentence with "Yet", five end on a later writer or institution. For Mark, with the kit review; nothing was recast because of them.
    - **The kit review** (simplify the kit: options A, B or C, 2026-11-21) awaits Mark.

349. **The stories approved before the kit: Constantine done (2026-11-21).** This updates "The stories approved before the kit: reviewed in their era's batch" (2026-11-19). Constantine the Great was reviewed in batch 8 and passed unchanged: no fix, no re-card, no re-recording. Still to come: Ephrem, Gregory of Nazianzus, Gregory of Nyssa and John Chrysostom in the era 2 batches, Gregory of Tours in era 3. Owner: each era's batch.
350. **The kit review: decided (2026-11-21).** This updates "Batch 8, eras 2, 5, 6 and 7 … what is open at release" (2026-11-21), whose kit-review item is now closed. Mark chose option A: one kit, one prompt per step, batch prompts reduced to a header (Decision-Log, "The brief kit: one kit, one prompt per step", 2026-11-21). Batch 8's length item goes with it: the length rule is now in the kit. Owner: none.
351. **A Share button on the map, held until after the launch (2026-11-21).** Mark asked what it would take to add one, then chose to hold it so the launch goes out sooner ("lets hold off on building something else i want this out soon"). Today the map has no share control; people share the site with the browser's or Facebook's own button.
    - **The plan, when it is wanted.** One pull request: a Share button in the header and in the phone menu, and a "Share this" line on each card. Phones open the phone's share sheet; computers copy the link and say "Link copied". A card shares its own tree page (`/tree/<id>`) and the header shares the home page. Shares are counted anonymously: `share` is added to `EVENT_TYPES` in `cic-worker/worker.mjs` with a test, a line goes into `tools/cft_usage_report.py`, and the Privacy page says so. Phone and computer screenshots for Mark's look before merge.
    - **Left out on purpose.** Separate Facebook, LinkedIn and X buttons (the share sheet covers them), and a preview picture for each tradition (every shared link uses the tree's one title card today; unique pictures are a larger, later job).
    - Owner: the site thread, when Mark calls for it.
352. **The home page is about 9.5 MB (2026-11-21).** The map embeds its whole data set in `cft-website/index.html`: 9,502,941 bytes raw, 2.6 MB compressed. It loads in about a second on a fast connection, but a slow phone connection pays for it, and LinkedIn's crawler refused it (limit 3,145,728 bytes). Link-preview crawlers now get a small page (Decision-Log, "Link-preview crawlers get a small home page", 2026-11-21), which fixes previews but not the weight.
    - **If it is revisited.** Load the data from a separate file after the map shell appears, or split the stories' text out; either is a larger change with its own review, and the repository's "no new embedded world data" check applies to anything that adds data to the page.
    - 2026-11-22: scoped, then Mark ruled: "yes, start the audit" (Decision-Log, "Phone loading: the audit is done", 2026-11-22). The audit is done (`Build/Ministry/Operations/Audits/2026-11-22_cft-phone-loading-audit/`): the map reads 43 fields at start-up, and 1.04 MB of the 1.36 MB it reads is `longDescription`, read only by the audio check. Still open: steps 2 to 5 of the plan, which wait for Mark's call; and the audit has not run at a phone width.
    - 2026-11-22: step 2, the build step, is done (Decision-Log, "Phone loading, step 2", 2026-11-22): `tools/slim_map_data.mjs` makes a 1.28 MB slim page, 629 entry files and one link-details file from the full page, with 9 tests in CI. Nothing reads or deploys them yet. Still open: step 3, the map change (card files on open, error and retry, a phone-width audit, then deploy), and step 5, Mark's look at the before and after.
    - Owner: the site thread, when Mark calls for it.
353. **Jovinian stays (2026-11-21).** This updates "Jovinian's live profile comes down" (2026-11-11), which is now closed without the removal. Mark: "b" (Decision-Log, "Jovinian stays, and is rebuilt on the kit", 2026-11-21). His story is rebuilt on the kit in era 2's batch 12. Owner: that batch.

354. **Batch 9, era 2, the Greek East and the Nicene century: what is open at release (2026-11-22).** Eleven stories released and recorded (`Build/Ministry/Operations/Audits/2026-11-21_batch-9/README.md`; Decision-Log entries headed "Batch 9: …", 2026-11-21 and 2026-11-22).
    - **Quality trend, for the kit.** First-draft rigor fell from 3.9 (batch 7) to 3.4 (batch 8) to 3.0; Mark asked whether the build is drifting. A fresh, unanchored read of the nine finished stories scored them voice 3.9, craft 3.7, rigor 4.2, accessibility 4.1; three blocking findings and four 3s on craft were then fixed and checked. Most first-draft blocking findings were writers cutting parts of the approved heart to fit 4:30. Causes found: outlines still too full for the length after their cut-first lists; the writer prompts did not carry Mark's ruling that writers cut only from that list; and guidance from the batch 8 prompts that the one-prompt-per-step kit no longer carries. A kit change (outline check fails an outline over length; the writer header carries the length ruling; a fresh read and a craft pass as standing steps) is to be drafted for Mark. The fresh reads' remaining minor findings are in each folder's `Fresh_Read.md`. Owner: the coordinator, for Mark.
    - **Lengths.** Cyril of Jerusalem runs about 4:55 and Epiphanius about 4:45 (Mark's ruling), Hilary and Evagrius about 4:32 to 4:33; the rest are under 4:30.
    - **Short spans "checked at card".** As in batch 8, short quoted terms carry "checked at card" with no blind reading.
    - Owner: the next batch's coordinator for the kit change; none otherwise.
355. **The stories approved before the kit: both Gregories done (2026-11-22).** This updates "The stories approved before the kit: Constantine done" (2026-11-21). Gregory of Nazianzus passed review; one spelling changed ("Apollinaris"), so he was re-recorded. Gregory of Nyssa gained one sentence (his life of Macrina) and was re-recorded. Still to come: Ephrem and John Chrysostom in batch 10, Gregory of Tours in era 3. Owner: each era's batch.
356. **Phone loading, step 3: built, waiting for Mark's look (2026-11-22).** This updates "The home page is about 9.5 MB" (2026-11-21). The map now loads each card's text when it opens and the deploy build uses the slim page (Decision-Log, "Phone loading, step 3", 2026-11-22). Cards compare identical on 1,231 comparisons and all 736 link cards; names show after 4.3 s (Wi-Fi), 4.4 s (4G) and 6.0 s (slow 4G) on an emulated phone, from 5.5, 6.9 and 16.7 s.
    - **Open.** Merging deploys churchfamilytree.com, so Mark's look comes first. After the merge: wait for the deploy, open a card on the live page, re-run the timings against it. Choices Mark may change: the link tooltip text and the stories staying in the page; idle loading of the two audio manifests.
    - **Open, separate.** Two iPhone tests in `Build/tools/tree_map_view.test.mjs` fail with and without this change.
    - Owner: the site thread.
357. **Phone loading, step 3: live (2026-11-22).** This updates "Phone loading, step 3: built, waiting for Mark's look" (2026-11-22). Merged and deployed; live first names after 4.7 s (Wi-Fi), 5.2 s (4G) and 6.8 s (slow 4G) on an emulated phone, from 5.5, 6.9 and 16.7 s (Decision-Log, "Phone loading, step 3: merged and live", 2026-11-22).
    - **Open.** Loading the two audio manifests (91 KB) when the page is idle, which might save about 0.4 s on slow 4G; not measured. Owner: the site thread, when Mark calls for it.
    - **Open, separate.** Two iPhone tests in `Build/tools/tree_map_view.test.mjs` (zoom floor; a tap leaves no hover tip) fail with and without this change. Owner: the site thread.
359. **Phone loading: audio manifests when idle, tried and dropped (2026-11-22).** This updates "Phone loading, step 3: live" (2026-11-22), which listed it as open. It gave no gain in first-names time (Decision-Log, "Phone loading: loading the audio manifests when idle was tried and dropped", 2026-11-22). Still open: the drawing work and start-up script, which set the remaining 4 to 7 s on a phone. Owner: the site thread, when Mark calls for it.
358. **Descent against influence on cards (2026-11-22).** Tradition cards and pages now separate direct descent from influence (see Decision-Log, same date). Open: option C, a map view of a tradition's family line, deferred until Mark has seen the cards. 107 of 350 traditions have no recorded direct parent or descendant; whether to fill any is a census question, not a display one. Three descent links from a tradition to a person or a movement across churches show under influence. The step-3 phone-loading session edits the same `openPanel` area of `cft-website/index.html`; the card reads `DATA.edges` fields (`id`, `from`, `to`, `type`, `confidence`, `outcome`, `note`), which the slim page keeps. Owner: the next map session, for Mark.
376. **Batch 10: what the release leaves open (2026-11-23).** Batch 10 (era 2, Antioch to Chalcedon and the edges of the empire) is in the census and the tree: twelve stories, ten rebuilt on the kit and John Chrysostom and Ephrem the Syrian reviewed. Source: `Build/Ministry/Operations/Audits/2026-11-22_batch-10/Release.md`; Decision-Log entries headed "Batch 10: …" (2026-11-23).
    - **Recording.** None of the twelve is recorded in its batch 10 text. The ten rebuilt stories are new recordings; Chrysostom and Ephrem changed wording and are re-recorded. A paid run under the recording settings, with Mark's approval in his own words and a credit cap. Owner: the batch 10 session, for Mark.
    - **The Aksumite tradition card.** The `aksumite-christianity-conversion-era` census `why` calls Frumentius "shipwrecked" and a "tutor"; Rufinus says neither (the ship put in and was attacked; he kept the king's accounts and later shared in ruling: `frumentius/Outline.md`, RUF 27310-27325). A change to another census entry is Mark's call. Owner: Mark.
    - **Two card notes the second readings flag.** Rufinus `quotationOriginals[2].uncertain` could note the scan's "qui" read as "quae"; Theodoret `quotationOriginals[0].uncertain` could cite Mansi V 88759-88763 (`Second_Readings.md`). Not changed. Owner: the next card pass that touches them.
    - **The reference stories moved.** This batch's fresh readers scored Basil 4/4/5/5 and Epiphanius 5/4/5/4 against fixed 4/4/5/4 and 4/5/4/5; a blind cross-batch scoring the same day (`Build/Ministry/Operations/Audits/2026-11-23_blind-cross-batch/Results.md`) scored them about half a point below their fixed scores. The yardstick drifts with the reader; whether to re-fix it is Mark's call. Owner: Mark.
    - **Two tool changes in the release, for review in the pull request.** `tools/validate-census.mjs` pads a scan reading that joins lines, so the lines below keep their numbers (Frumentius's PG 25 reading had shifted `athanasius-of-alexandria`); `tools/check_spelling.py` skips `englishPrinted`, the verbatim English print, as it already skipped `printed`. Owner: the release reviewer.
377. **The stories approved before the kit: Chrysostom and Ephrem done (2026-11-23).** This updates "The stories approved before the kit: both Gregories done" (2026-11-22). John Chrysostom: his Matthew sermon moved to Antioch, his first expulsion's year given only as "not long before", the closing sentence split. Ephrem the Syrian: the essence (his hymns) now within the first minute, his death moved to the end, Sozomen credited for the fear and the songs. Both passed their fresh reads and are re-recorded. Still to come: Gregory of Tours in era 3. Owner: era 3's batch.
378. **Open method questions from batch 10, for Mark (2026-11-23).** (a) Why the outlines keep running long, and three fixes at research for batch 11 on: https://claude.ai/artifact/MzbUJjBWpsjZJ377yUm3vX (A recommended: the researcher counts first and plans to the 3:00 aim). (b) Whether card writing moves to Opus, as story writing already has: Sonnet hands made two slips in this batch (a paragraph move reported but not made; a doubled phrase), and the Opus card checks found fixes on ten of the twelve Sonnet cards. Owner: Mark.
360. **Batch 9: the kit change done, nothing open (2026-11-22).** This updates "Batch 9, era 2, the Greek East and the Nicene century: what is open at release" (2026-11-22), whose one owned item was the kit change. It is in the kit (Decision-Log, "Brief kit change for batch 10", "Batch handoffs: every ruling accounted for, a fixed yardstick, and a launch template", "Recording settings in one locked file" and "The slate checks each home tradition's direct line", all 2026-11-22), and batch 10's launch prompt is written from the template (`Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Batch10_Launch_2026-11-22.md`). The lengths and the short spans "checked at card" stand as Mark ruled. Nothing in batch 9 is open. Owner: none.
361. **Phone loading: start-up drawing work, safe fixes made (2026-11-22).** This updates "Phone loading: audio manifests when idle, tried and dropped" (2026-11-22). Four safe fixes cut first names on an emulated phone by about 0.8 to 0.9 s (3.8 s Wi-Fi, 3.9 s 4G, 5.4 s slow 4G) with identical cards and DOM (Decision-Log, "Phone loading: the start-up drawing work, safe fixes first", 2026-11-22).
    - **Open.** Build the People list and marks only when used (about 0.7 s); fewer SVG nodes at start (largest, riskiest); the tour's per-frame placement (about 0.1 s). Each needs Mark's call.
    - **Open, small.** The phone opening view differs from the previous page by 11 antialiased pixels at one river edge, DOM identical. Owner: the site thread.
    - Owner: the site thread, when Mark calls for it.
362. **Phone loading: start-up fixes live (2026-11-22).** This updates "Phone loading: start-up drawing work, safe fixes made" (2026-11-22). Merged and deployed; live first names 4.3 s (Wi-Fi), 4.2 s (4G) and 6.4 s (slow 4G) on an emulated phone, from 4.7, 5.2 and 6.8 s before (Decision-Log, "Phone loading: the start-up fixes are merged and live", 2026-11-22).
    - **Open.** The estimate (about 3 s, about 5 s) is not met. Next, each Mark's call: the People list and marks built only when used; fewer SVG nodes at start; the tour's per-frame placement. Owner: the site thread, when Mark calls for it.
364. **Family line view built: option C (2026-11-22).** This updates "Descent against influence on cards" (2026-11-22), which deferred it (Decision-Log, "Family line view, line-end labels and the phone peek strip", 2026-11-22). A card's new Family line button lights the whole chain of direct descent, ancestors and descendants, in forest green; the one-step Connections view keeps its lines in lime.
    - **Open.** 107 of 350 traditions have no recorded line and get no button. Five "continued as" links have no graded edge, so the node lights and no line joins it. The longest line is 41 traditions, so most of a long line is off screen at any zoom; labels on the line name what lies past the edge.
    - **Open.** Forest green sits close to the gold influence color for readers with protanopia (simulated difference 5, where under 10 is hard to tell apart) and forest against red is marginal with deuteranopia (11). In the Family line view only forest lines are bold, and line weight, arrowheads and dashes carry the rest. Gold against red was already close under deuteranopia (5). No test with colorblind readers.
    - **Open.** Tested on an emulated iPhone 13 only, not on a real phone. Line-end labels hide while the connections tour runs and, on a phone, while a card is open.
    - Owner: the next map session, for Mark.
363. **Phone loading: People layer and layout reads checked, dropped (2026-11-22).** This updates "Phone loading: start-up fixes live" (2026-11-22). Deferring the People layer would save about 20 ms; caching the bar heights gave no measurable gain (Decision-Log, "Phone loading: deferring the People layer and caching layout reads were checked and dropped", 2026-11-22). Still open: fewer SVG nodes at start, and fewer label-fit runs (three at start-up, about 1.1 s together); each is a larger change needing Mark's call. Owner: the site thread, when Mark calls for it.
366. **The census release number had stopped at 49 (2026-11-22).** This updates "Data release 49: the Martyrs' Mirror quotations cite the 1886 Elkhart printing" (2026-11-16). Releases 50 and 51 were ruled on 17 and 18 November, but the number in the census file stayed at 49, and batches 8 and 9 changed the file after that; the data page and its citation lines told readers "release 49 (November 16, 2026)" for a file that held later data. A catch-up stamp, release 52 dated 2026-11-22, is made (Decision-Log, "Data release 52: a catch-up stamp", 2026-11-22). The file's license credit line also said release 44 and now says 52.
    - **Open.** Nothing makes a batch stamp the number when it ships. Until a batch's release step does so, the number drifts again. Owner: each batch's coordinator, as part of its release step; the site thread checks the data page after each merge.
    - **Open.** Batches 4 to 9 were not each given their own number, and the records do not say how they would map to 52 onward. They are covered by 52.
365. **Phone loading: first link card timed, card files cacheable (2026-11-22).** This updates "Phone loading: People layer and layout reads checked, dropped" (2026-11-22). The first link card takes 0.36 s (Wi-Fi), 0.58 s (4G) and 1.5 s (slow 4G) live; the card files and link details now revalidate instead of `no-store`, verified live (Decision-Log, "Phone loading: the first link card was timed, and the card files can now be cached", 2026-11-22). Still open: the home page is `no-store`, so each visit downloads about 0.36 MB compressed; revalidating it would cost a trade-off with deploy freshness and is Mark's call. Owner: the site thread, when Mark calls for it.
375. **Tradition briefs for four of the ten traditions with no tradition recording: drafted and reviewed, not in the census (2026-11-22).** Kongo Christianity (449 words), Kirishitan Japan (623), New Spain and the Andes (487) and Ming China (444) each have a source sheet, an Opus round-1 review, one revision and an Opus round-2 recheck, all PASS, in `Tradition-Briefs/<id>/`. They follow the finished world narrations (sheet, Sonnet draft, Opus review, one revision, one targeted recheck). Opus authored the modern renderings of the quoted passages. Scorer: grade 5.9 to 7.1, reading ease 76.6 to 84.2.
    - **Not done, by Mark's ruling of 2026-11-22 (option A).** Ireland, Wales, Armenia before the Bagratids and the Church of the East under the Abbasids wait for the source-research thread. Gaps for it: a source for Ireland 1056-1169, for Wales after 954, a narrative source for Armenia 554-884, and a mapped source for the Abbasid East Syriac window (the one mapped work, the Chronicle of Seert II.2, appears to end in the seventh century; Mari ibn Sulayman and Elias of Nisibis are vendored under other entries). Add rows to `download-queue-seed.yaml`; not done here.
    - **Not needed.** Lutheran Wittenberg and the Reformed cities already have finished narrator texts (World-Narration, passed 2026-11-20); no brief written.
    - **Open, for Mark.** Nothing is in the census. Each brief would become the entry's `longDescription`; the release steps are in Brief-Kit `roles/release.md`. Kirishitan runs 623 words (the finished world stories run 623 to 721), longer than the 400 first proposed, because the review's replacements added the record's force; the recheck judged the length justified.
    - **Open, small.** The Kongo, Kirishitan and China sheets cite Opus renderings in English; the Kongo and New Spain quotes are renderings, the China quotes are verbatim English of 1850. The sources carry no Japanese-language, Chinese-language or native Christian text for these traditions (card material, not audio).
    - Owner: this thread for the release; the source-research thread for the four held traditions.
370. **Search level 1: the sourced common names (2026-11-22).** This updates the build-plan row "P2-S, search" (deferred 2026-11-11). The level 1 design is converged (Decision-Log, "Search: three levels, and the level 1 design converged", 2026-11-22). Today no name in the tree contains "Nestorian", "Mormon" or "Abyssinia"; common, older and outsider names are new content, and each needs a basis.
    - **Open.** The first batch (living traditions and the best-known older and outsider names, for entries and for places) is not drafted. Search does not launch without it. Owner: the names batch session (Sonnet drafts, Opus reviews, three rounds at most).
    - **Open.** Later batches by river are not scheduled. Owner: Mark calls for each.
    - **Open.** The names file joins the numbered data release, and nothing yet makes a batch stamp the release number ("The census release number had stopped at 49", 2026-11-22). Each names batch must stamp it. Owner: each batch's coordinator.
371. **Search level 1: real-phone and screen-reader check (2026-11-22).** The design is keyboard and screen-reader first (Decision-Log, "Search: three levels, and the level 1 design converged", 2026-11-22), and the build tests it with automated checks and an emulated phone. No person has used it on a real phone or with a real screen reader (VoiceOver, TalkBack, NVDA). Open until one has. Owner: Mark, or a tester he names.
372. **Search level 1: lit results on phones (2026-11-22).** A country or a year lights its entries, and the design assumes the strip the family line view uses on phones can carry them ("Family line view built: option C", 2026-11-22). That was not read in the code before the design converged. The build session confirms it before relying on it; if the strip cannot be reused, it comes back to Mark before anything new is added to the map. Owner: the search build session.
373. **Search levels 2 and 3: the shared topic list is Mark's decision (2026-11-22).** Level 2 organizes the Library by topic in partnership with Church in Conversation, and level 3 puts topic answers on the tree (Decision-Log, "Search: three levels, and the level 1 design converged", 2026-11-22). A topic list shared by the two projects is a cross-project decision: always asked of Mark, never settled in a build thread. Neither level is designed. Level 2 waits for the Who and council builds and for the allowance to carry it. Level 1 holds an empty "Topics" group in its results for level 3. Owner: Mark.
374. **Search level 1: place data is partial (2026-11-22).** Modern countries are recorded on 294 of the 350 traditions (477 of 629 entries). A country search can only find entries that carry the data, so its results say what they cover. Filling the remaining entries is census work, not search work. Owner: the site thread, when Mark calls for it.
367. **Council marks at the farthest zoom (2026-11-22).** This updates "Space the zoom layers so every click adds something" (2026-11-21), which set the zoom at which council marks first draw. Council marks now draw at every zoom while the Councils toggle is on, and are gold (Decision-Log, "Councils show at every zoom and turn gold", 2026-11-22).
    - **Open.** On a phone at the farthest zoom a council mark sits close to the era 2 dates caption; they touch and both stay readable. Owner: the next map session, for Mark, if it bothers him.
368. **Red lines that run back in time, and ten that join traditions with no overlap in dates (2026-11-22).** Mark looked at the red (argued against, broke with) lines from Church & Empire to Montanism, Novatianism and the Ebionites. They run up the map into era 1 because a line ends at the mark where each tradition starts, though the evidence is from the 300s. Mark ruled that documented lines stay as they are: "if they are documented, then we can, its just when a line goes back in time it looks odd, but makes sense". No change was made.
    - **Open.** Ten of the 206 red lines join traditions whose date spans do not overlap, by 6 to 242 years, for example Coptic Egypt (642 to 1013) to Alexandria (150 to 400), Zurich & Geneva (1519 to 1650) to the Papal Church (1049 to 1300), and Tridentine Church to Humiliati. Their notes are about later writers arguing against earlier ones. Whether each should stay "argued against" or be another kind of link is a census question for Mark, not checked yet. Owner: a census session, for Mark.
369. **Line end marks made visible, and an arrowhead on argued-against lines (2026-11-22).** This updates "Red lines that run back in time, and ten that join traditions with no overlap in dates" (2026-11-22). The end marks of all four kinds of line were hidden under the tradition's house icon and about 4 pixels across; they now keep one size on screen and sit just outside the icon at any zoom (Decision-Log, "Line end marks made visible; argued against gets an open arrowhead", 2026-11-22).
    - **Open.** Where many lines meet one tradition, as at Church & Empire on a phone, the end marks and the line-end labels crowd each other. Owner: the next map session, for Mark, if it bothers him.
    - **Open.** The marks sit at the icon's edge by a size rule, not by measuring each icon, so on a diagonal line one can sit a little off the corner. Checked in a browser on desktop and an emulated iPhone 13, not on a real phone.
400. **The kit's modern-opinion line does not yet match Mark's refinement (2026-11-23).** Kit Part 1, Rigor, on branch `claude/happy-ritchie-u8wn8l`, sends a modern editor's or historian's judgment "to the card as a modern view". Mark's later words (Decision-Log, "Modern opinion: a separate pass, and where a modern scholar may stand", 2026-11-23) let a historical, source-bound modern scholar support a story unnamed, with the credit in the reference list after the story, within the rights and referencing rules. Batch 10's twelve meet both readings.
    - **Open.** Reword the kit line to Mark's words once batch 10's branch has reached main. Owner: the what-and-why ranking thread, in its pull request.
