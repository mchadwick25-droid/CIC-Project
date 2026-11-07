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
