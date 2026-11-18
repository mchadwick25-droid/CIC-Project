# Review r3: river-notes removal (1e3d37c8..17a60c43, cft-website/index.html)

Result: 1 BLOCKING, 1 MINOR. Checks 1 and 4 are clean. Check 3 renders cleanly.

## BLOCKING 1: three more stories still cite the removed notes (check 2)

The commit fixed two stories. Three others still point at the notes. All of them are on the map and show this text under "How it connects" (checked in Chromium).

- `plinys-two-ministrae` (line 116379): "The lore block for the Origin lane already quotes Pliny's 'as to a god' line…". Only the removed Origin notes had that quote. Nothing on the map quotes it now, so the sentence is false.
- `simeon-on-the-pillar` (line 116832): "(the 'sons of the covenant' its lore names)". This pointed at the removed Syriac East notes. No record has a "lore" field. The story's related Syriac Orthodox record does not name the order.
- `juliana-and-corpus-christi` (line 117461): "the Corpus Christi procession the Latin West lore names as a standard carrier of lay piety." The removed notes were its only support. The story never mentions a procession. Cutting only the clause leaves "The feast she started is the Corpus Christi procession", which makes the feast and the procession the same thing. The whole sentence probably has to go.

## MINOR 1: "What sets this river apart" wording (check 3)

This code is older than the commit. It stands out more now that the paragraph opens the card.

- A sentence that starts with a numeral right after "Era N." reads like a decimal. Origin: "to Era 4. 1 of its 6 traditions". Protestant & Evangelical: "to Era 10. 2 of its 78".
- River names that contain "and" blur the list. Origin: "most often with Latin West and Church and Empire".
- "lean toward “argued against” (12 of 19)" is hard to parse. Across families uses "lean toward" and "most often" for its single connection.
- The project grader (`engine.m1.gates.grade_text`) scores 8 of 15 paragraphs below FRE 60. Latin and Protestant gets FK 10.6 and FRE 36.6. The long river names cause much of this.
- The heading promises character, but the paragraph gives counts. Mark kept the heading, so this is a note only.

No AI tells.

## Check 1: clean

- The live surfaces (cft-website/, cic-website/, tools/, Build/tools/, engine/m6/) no longer contain `RIVER_LORE`, `riverCoherence`, `originStory`, a `lore` field or `.statusdesc`. The only hits are in Build/Ministry.
- Before the commit, `statusdesc` was used only on the removed line.
- Rivers match records by lane number, not by the removed key.
- The census file has no lore keys.
- No tool reads "How it connects", so no narration audio contains the cut clauses.
- Passing checks:
  - validate-census: 0 errors.
  - The three test files that read the map: 49 of 49 pass.
  - build_tree_site: 0 mismatched.
  - check_live_commentary: nothing flagged on the map file.

## Check 3: renders

- All 15 river cards open, at 1366px and at 390px wide.
- There are no page errors, no NaN or undefined values, no empty headings and no odd joins.
- The phone layout has no sideways scroll.
- On a phone, the first tap in the zoomed-out view zooms in. That is by design.

## Check 4: clean

- Both edited sentences are grammatical and true.
- Scillitan: the story's teaser and caveat still carry the "oldest Latin document" claim. No record mentions the martyrs. The Carthage record begins with Cyprian, "c. 240s".
- Elcho: the Rātana record itself still names Silas Eto.

## Outside scope (not counted)

- "How it connects" shows raw record ids in 56 of 62 stories.
- The edited Elcho sentence still says "the map's lane 7", but the map never shows lane numbers.
- Port 8791 was taken by another process, so I used 8817.

## Recheck at 68abdd6f

I rebuilt the site (0 mismatched). All 15 river cards open with no page errors. validate-census reports 0 errors, all 49 tests pass, and check_live_commentary finds nothing to fix.

### (1) BLOCKING 1 is closed

No text on the map, the census or the tree pages still relies on the notes. The other matches are ordinary record content.

Correction to round 1: the Pliny the Younger person record does quote the line ("unto Christ as God"). The finding still stood, because the sentence cited the removed notes.

### (2) Story texts

All three are grammatical. Juliana is true to its story and records. The new Pliny sentence is true.

- MINOR: Simeon now says "the Syriac record's own world of village Aramaic asceticism". The Syriac Orthodox record mentions neither villages nor Aramaic. Its only ascetics are those in John of Ephesus's Lives. The removed parenthesis was the phrase's only support.

### (3) River-card sentences

The counts match my own recount for all 15 rivers. 11 of 15 paragraphs now meet the bar (FK ≤ 10, FRE ≥ 60), up from 7. No AI tells.

- BLOCKING: "then to" turns ties into rankings.
  - Africa: "most often to Latin West, then to Greek East", but both have 15.
  - Africa and Latin: its two rivers tie at 2 each. Its "most often “continued as”" also ties with "gave rise to".
  - Origin, Church and Empire and Non-Nicene tie for second place, so their "then to" choice is arbitrary.
- MINOR: link labels used as verbs lose direction. "are most often “gave rise to”" reads badly. Across families reads backwards: its one link runs from the Mainline Century into this river.
- MINOR: four paragraphs stay under FRE 60 (52.9–58.2): Latin West, Latin and Protestant, Protestant & Evangelical and Across families. FK stays at 8.1 or less. Long river names cause this.

### (4) New faults

The tie rankings above are new.

- MINOR (latent): "Outside the river" also counts cross-church movements, which sit in their own column. Each counts under the river nearest its lane number. Today this changes nothing shown.

### Outside scope (not counted)

The Pliny text's untouched first clause is false: "Predates every Anatolian movement on the map by more than a century". Montanism (Phrygia, from 165) and the Scattered Households (Asia Minor, from 70) are on the map.

## Recheck 2 at 0edf0bf7

I rebuilt the site (0 mismatched) and opened all 15 river cards. There were no page errors. The 49 tests pass and validate-census reports 0 errors.

### (1) The BLOCKING is closed for all 15 rivers

A script checked each card against my own recount. All 15 match.

- Africa: "it links equally often to Latin West and to Greek East".
- Africa and Latin: "the most common kinds are “continued as” and “gave rise to” (2 each)". Its two rivers are named as equal.
- Origin, Church and Empire and Non-Nicene tie for second place, so "then to" is dropped.
- Across families: "Its one recorded connection is a “gave rise to” link, with Protestant & Evangelical." It no longer reads backwards.

The Simeon sentence is grammatical and matches its caveat.

### (2) New faults: none blocking

- MINOR (new): on six cards, two sentences in a row start with "Of its…". That sounds templated.
- MINOR (latent): the one-link sentence always writes "a", so a kind like “influenced” would get "a “influenced” link". No card shows this today.
- MINOR (older): Syriac and Protestant links outside only to Syriac East, yet says "most often".

### (3) Reading levels

11 of 15 paragraphs meet FK ≤ 10 and FRE ≥ 60. Four stay at FRE 54.4–59.2, with FK 7.9 or less: Latin West, Latin and Protestant, Protestant & Evangelical and Across families. Long river names cause this. No AI tells.

## Recheck 3 at aea7d944

Rebuilt (0 mismatched). The working tree holds someone's uncommitted feature-bar edit. It changes no text checked here.

- Pliny: grammatical, with no leading slug and no new claim. Both remaining claims are true.
  - MINOR (older wording): "the same province's church" is loose. The record covers Neocaesarea in Pontus and Olympus in Lycia. Neocaesarea lay outside Pliny's Bithynia-Pontus.
- The river-card sentences also changed. All 15 match my recount, with no page errors. My three Recheck 2 MINORs are fixed.
  - MINOR (latent): a single cross-church link would print "inside the river". No card shows this.
- 12 of 15 paragraphs meet the reading bar. Three are at FRE 56–58, FK 7.6 or less. All 49 tests pass.
