# Step 0 Review, Round 1 — The Hussite and Bohemian Brethren Movement

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` (Revision 1, drafted 2026-09-25).

## Verdict

**Substantial revision needed.** The floor conclusion (A1 "clears") and the Tier 1 value both hold up. But the document's account of how it got to both is wrong in places: it claims a fresh derivation the census record contradicts, it characterizes the Lollardy relationship as indirect when the vendored text shows direct textual borrowing, and it states the sourcing gap too narrowly.

**What was checked:** CLAUDE.md; the Step 0 document; the dossier; the corpus-map; the full census entry (including `statusWord`/`statusDescription`, not just `floorNote`); REGISTRY.yaml; the headers and bodies of both vendored Hus files; the Lollardy and Anabaptist corpus-maps; the census entries for Lollardy and Devotio Moderna; and the Lollardy Step 0 document.

## Substantial findings

**F1. §0 and A3 make a false claim about the census record.** The document states the census status is "plain 'Pre-Survey Candidate,' with no `statusWord` or `statusDescription` recording an earlier gate," and that A3 "performs the check itself" with "no prior Step 0 gate." The census entry in fact carries `statusWord: "Researched — strong candidate"` and a `statusDescription` recording an existing Tier 1 finding, plus two scope notes this document never engages: the movement's Prague formation (1402–14) precedes the 1415 window this world claims, and the Unitas (Unity of the Brethren) segment "wants a later entry to carry it forward." This is the same record shape Lollardy's own Step 0 document correctly carried forward — "genuinely fresh, unlike Lollardy" is inaccurate, and §5 repeats the error. **Fix:** reframe as a carry-forward check of the existing finding, and address both scope notes directly (the window-boundary question and the Unitas-segment question).

**F2. B3, §0, and §4 item 3 mischaracterize the Lollardy relationship.** The document calls it "historically real but indirect" and "not a text-sharing overlap." The vendored *De Ecclesia* file's own translator introduction contradicts this directly (Schaff, c. lines 1509–1561): "Huss appropriated paragraph after paragraph from his predecessor and transferred them often with little verbal change to his own pages," drawing on Wyclif's own *De Ecclesia* and *De potestate Papae*, with matching passages printed side by side by Loserth — "Never did a man owe more to mortal teacher than Huss did to John Wyclif." The vendored *Letters* add Letter VI, a direct exchange with an English Wycliffite (Richard Wyche), read aloud in the Bethlehem Chapel. The relationship is direct and textually documented, not indirect. This also weakens the Tier rationale: *De Ecclesia* is called the anchor of "a strong, focused seed," but by its own translator's account its doctrine is substantially Wyclif's, and Lollardy's corpus already vendors seven Wyclif/Wycliffite works. Separating the two worlds may still be the right call given their diverging outcomes, but the stated reason is inaccurate.

**F3. The sourcing gap is stated too narrowly.** Only the missing Unity of the Brethren voice is named. The real gap is larger: the *Letters* run June 1408 to July 1415; *De Ecclesia* dates from 1413. Every word of the vendored corpus predates or barely opens this world's own 1415–1517 window. Nothing speaks for the Utraquists, the Taborites, the 1420 Four Articles, the crusade years, or the 1436 Compactata itself — yet A3 and B4 lean on exactly those undocumented events as evidence for the person-defined-movement clearance and the "institutional and political" audience appeal. Historically true, but not yet voiceable from what's vendored.

**F4. A1 mischaracterizes Hus's dispute with Rome as partly "eucharistic-practical (utraquism)."** Per Workman's own note in the vendored *Letters*, the lay chalice was introduced by Jakoubek in 1414 and Hus "had taken little interest in the matter" until embracing it late, from prison. A direct search of *De Ecclesia* for utraquism/"both kinds"/"sub utraque" found nothing on the topic. Utraquism was not what Hus's own condemnation concerned. Does not change the floor result, but is a factual error inside the floor characterization.

**F5. Overstates what was actually read.** A1 and §5 say the two works were "read this pass" / "fetched and read directly." The files' own provenance headers say sampling only ("beyond the opening pages and a mid-document sample"), consistent with the dossier's own §6 ("Doctrinal floor: not assessed in depth this pass"). A1 also cites no specific passage as positive evidence for its own "no complication" finding, and its check is scoped to Hus only, not the movement's other strands (Taborites, Pikarts, early Unity).

**F6. Misattributes a census field.** The 1501 hymnbook claim is attributed to `relationsSummary`; it actually appears in `why`/`longDescription`. `relationsSummary` does not mention the hymnbook. (The dossier makes the same error; this document copied it forward.)

**F7. The census's own richer sourcing record is never reconciled.** Census `sourcing` field reads "Rich: confessions, hymnody, discipline records" and names primary sources this document never mentions (Peter of Mladoňovice's eyewitness *Relatio*, Four Articles/Taborite texts in Fudge 2002, Unity confessions/discipline/hymnody, Spinka's 1972 Letters edition) — mostly modern, in-copyright, not vendorable, but the document's "gap" framing should say the material exists but isn't public-domain/vendored, not imply it may not exist at all.

## Minor findings (wording only, not independently grounds for revision)

- §6 lists the 1501 hymnbook among "uncontested historical fact" while §1 correctly hedges it as "often called" first — the "first" claim is contested, not uncontested.
- "His career at the university" overstates the Letters' own range (they begin June 1408, nothing from 1402–07).
- The XML-extraction boilerplate caveat is inapplicable (files are .txt).
- A3's claim that Lollardy's A3 was "cleared on comparable grounds" should say "carried forward," matching Lollardy's own document.
- The Appeale rejection reasoning holds up; "better scanning technology" names the wrong fix (re-OCR/transcription would be the actual route), and the vendored Letters already cover Hus's own appeals language directly.

## Confirmed accurate

Rights-basis and host metadata (NOT_IN_COPYRIGHT, archive.org IDs) match across corpus-map, REGISTRY.yaml, and file headers. *De Ecclesia*'s content matches its "central ecclesiological treatise" description. The Letters do cover the Bethlehem Chapel period and the Constance imprisonment. Core dates/events (1415 burning, 1436 Compactata, 1420s–30s crusades, hedged 1501 hymnbook claim, post-window Herrnhut) are correct. The Menno Simons sourcing comparison checks out. A5 is sound. No fabricated sources found.

## Disposition

Per `cic-build-cycle`: F1–F4 and F7 each change a claim's substance, a sourcing conclusion, or a scope boundary — this meets the project's own bar for substantial revision. Revise, then send back through review.
