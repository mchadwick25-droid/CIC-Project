# Era 10, P2-E10b: adversarial review, Round 2

Reviewer: independent Opus 5.5 review · 2026-11-08 · Round 2 (targeted recheck)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10b_Proposed.json` and `CiC_Step0_Era10_P2E10b_Trace.md` on `claude/era10-step0-history` at 8eef08559, diffed against 6bf45206a ("P2-E10b: Review Round 1"). The new rows are IX.52 and IX.54 to IX.58, with 46 register edits and 2 meta edits.

**Scope.** This round checks only two things: whether each Round 1 finding is closed, and the new material. The new material is the Section A floorNotes for IX.54, IX.55 and IX.57, the added statement-of-faith sources, the IX.16 whole-field `set` rewrites, the readability rewrites, the meta counts and the IX.53 hold.

**Method.**
- **Applying the proposal.** I applied it with `scratchpad/e10b-fix1/apply.py` to a scratch census, copied to `scratchpad/e10b-rev2/census.json`. There were 0 edit or meta check failures: 307 rows, totalEntries 307, Pre-Survey Candidate 225.
- **Validating it.** `node tools/validate-census.mjs <scratch> --atlas cft-website/index.html` gave 307 movements, 579 edges, 10 eras, **0 errors** and 2 warnings. Both warnings were there before this proposal. With `--tree cft-website/tree`, the only errors were the 6 expected missing tree pages for the new rows.
- **Diffing.** I diffed every new-row field and every register edit between 6bf45206a and HEAD (68 changed items) and read each one.
- **Checking the statements of faith.** I fetched the three carrier statements and re-read them verbatim:
  - hslda.org/post/what-we-believe: byline "April 22, 2020"; "leaders, directors, and employees"; "We do not require members of HSLDA to be Christian or religious";
  - citygatenetwork.org/statement-of-faith: no date on the page;
  - vineyardusa.org/Vineyard-Core-Values-Beliefs.pdf: "three persons of one substance"; "fully God and fully human in one person"; "raised from the dead on the third day".
- **Checking the 1994 date.** bible.ca/cr-vinyard.htm reproduces "as of the Board meeting of November 1994".
- **Checking scores.** I re-scored 6 fields with the drafter's `fre.py`, which uses `engine/m7/readability.py`'s counter. All 6 match the trace table.
- No repo file was edited. No metered model call was made.

---

## SUBSTANTIAL findings

**S2-1. IX.54 `floorNote` gives a recent, undated statement to the 1913 union.**
- *Location:* newRows IX.54 `floorNote`: "No question. The union, later named Citygate Network, published a statement of faith. It named one God…"
- *Evidence:*
  - The only text seen is Citygate Network's live page. I confirmed this run that it carries no date. The earliest capture is 2025.
  - The Section A research says plainly: "It evidences the present network's confession, not the IUGM's." The trace says the same: "evidence for the later network's confession, not the IUGM's of 1913".
  - The participant sentence makes "the union" the subject and gives no date or recency. A reader of a 1906 to c. 2010 entry will take it as the union's confession inside the window. That is the reading the research warns against.
  - IX.55 states its 2020 date, and IX.57 says where its 1994 date comes from. IX.54 says nothing about its date.
- *Fix (mechanical):* "No question. Citygate Network, the name the union took later, published a statement of faith. The only copy seen was undated and recent. It named one God, eternally Father, Son and Holy Spirit. It said that Jesus Christ was God, born of a virgin, and that he rose bodily from the dead."

**S2-2. IX.53 is held without a change order to Mark's ruling.**
- *Location:* the trace, "Direction 1 (IX.53)" and "Held with IX.53"; `_meta.atlasIds`; `metaEdits` (307 and 225).
- *Evidence:*
  - **Mark's ruling.** The Decision-Log entry "ERA 10 GATE: Mark takes every recommendation" says: "Six movements are added under the recent-movement evidence rule: faith missions, …". G-57(a), which is ruled, carries no Section A condition. Round 1 found the original "not yet assessed" floorNote honored it.
  - **The analogy does not hold.** The trace compares the hold to G-69 and G-72, but those holds were the recommendations Mark ruled on. Here Mark ruled that the row is added.
  - **A named line goes too.** The hold also takes the Wycliffe line (G-56(a): "Wycliffe in IX.53") out of the release.
  - **No authority on record.** CLAUDE.md says a change to a settled decision is a change order, "named and reasoned — never a quiet edit". The trace names it and gives reasons. But its authority is "the thread's direction", and the Decision-Log records no change order.
  - **The reasoning itself is sound.** No carrier text was seen. It is consistent to apply Section A to every row in this release. So the defect is authority, not substance.
- *Fix:*
  - Record a named change order in `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`: "IX.53 held pending a carrier's statement of faith, with the G-56(a) Wycliffe line held with it". If the direction was Mark's, quote his words. Recording it is then mechanical.
  - If the direction was not Mark's, ask him one question: hold IX.53, or build it under G-57(a) with a "not yet assessed" floorNote and the Round 1 fixes carried in the held note. The proposal stands whichever way he rules. Only the meta counts change (308 and 226 if it is built).

---

## MINOR findings

**M2-1. M-6 is still open in IX.57 `statusDescription`.**
- "The entry on the charismatic renewal and the Jesus movement ends where the Vineyard began, in 1982." IX.45's census `end` is still 1980, and its `dates` read "1960-1980s". The `relationsSummary` fix is right. The `statusDescription` restates the claim Round 1 found wrong.
- *Fix (mechanical):* "The entry on the charismatic renewal and the Jesus movement hands on to the Vineyard, formed in 1982." This follows IX.45's own text: "as the wave handed on to … the Vineyard association in 1982".

**M2-2. IX.16 `legacy`: the whole-field `set` keeps present tense and a narrator's aside.**
- The `set` rewrites the whole field, so it now owns two release-21 sentences. "Court records are part of these bodies' public record too" is in the present tense. "Those are matters of public record and part of any honest telling" is commentary in the narrator's voice. Ruling 4 and the no-AI-tells rule both bear on it.
- *Fix (mechanical):* "Court records were part of these bodies' public record too." Delete the last sentence.
- The rest of IX.16 is clean:
  - no Iglesia ni Cristo text is left beyond the pointer, and the `id` is permanent;
  - the facts for The Way, the Unification Church and La Luz del Mundo are intact: 1942, 1955, 1971, 1975, 1 May 1954, 1966, 6 April 1926, 1964, the Family Federation name, the 1982 conviction and the documented story;
  - no change history is narrated;
  - the `statusDescription` drops the "open question" on splitting the row, but `statusWord` still carries it.

**M2-3. IX.52: "Lambeth" is used without being introduced.**
- The `why` and `longDescription` rewrites changed "met in the Lambeth Conference" to "met at Lambeth". "Lambeth Conference" now appears only in `sourcing` and `voices`. A B2 reader meets "Lambeth" in the teaser, why, longDescription, floorNote and statusDescription with no clue that it is a conference.
- *Fix (mechanical):* `why`: "Their bishops met in the Lambeth Conference." `longDescription`, first sentence: "The bishops of the Anglican churches met in the Lambeth Conference in 1920, 1930, 1968 and 1998, among other years."

**M2-4. Carried items are flagged but not yet tracked.**
- The revision flags these items "for the thread", but none is yet in `Open_Gaps_Tracking.md`:
  - the `kind` question (M-10), IX.57 included;
  - E2's item text for Pueblo and the arena (C-5): the trace still points at a review's reading, not at evidence;
  - the IX.53 hold and its two wanted items;
  - the Vineyard publisher's own dated copy (the 2002 and 2009 captures);
  - the 2012 AGRM capture as the lead for an earlier IX.54 date.
- CLAUDE.md requires every known gap to be tracked there.
- *Fix (mechanical):* add the entries before the gate.

---

## COSMETIC findings

- **C2-1.** IX.52 `why` and `legacy` both open "By 2006, Kevin Ward found, most…". Vary one of them.
- **C2-2.** IX.24 `relationsSummary`: the release-21 text has "At the 1974 Congress", and the new sentence has "At the 1974 congress". Match the case.
- **C2-3.** IX.52 `longDescription`: "moral duty" replaces Resolution 15's "moral obligation" in reported speech ("they said"). Keep the source's word.
- **C2-4.** IX.55 `floorNote`: "leaders and staff" for "leaders, directors, and employees" is fair. "Leaders, directors and staff" would match the text exactly.
- **C2-5.** IX.16 `relationsSummary` keeps the release-21 reason "because none is large or well studied enough to have its own". It reads oddly now that the largest body has its own entry, and the row's own source note calls these movements large. Optional: "Three separately founded bodies share this entry."

---

## Round 1 findings: closure

| Finding | Status | Note |
|---|---|---|
| S-1 | Closed | IX.33 sentence as given. The BGEA source note keeps "extended from three weeks to more than eight". |
| S-2 | Closed | IX.52 and IX.58 are CR, and IX.52 stays settled. IX.53 is moot (held, S2-2). M5 E4 is carried in the held note. |
| S-3 | **Closed, changed approach accepted** | G-64's condition is "settled on a carrier's dated statement". It does not ask for a statement from the window. Compare G-69(a), which says "a dated statement from the Oxford Group years" when it means one. HSLDA is G-64's named carrier. I verified the statement's 22 April 2020 date this run. The floorNote gives the date and says the statement bound staff, not members. No ruling is reinterpreted. |
| S-4 | **Closed, changed approach accepted** | The quotation and its attribution are gone. "Told the story of homeschooling as a social movement" rests on the book's subject and subtitle ("…in the Homeschooling Movement"). The `why` paraphrase ("an organized movement, not a scatter of private choices") follows Round 1's own rewrite. |
| S-5 | Closed | The IX.24 sentences follow "…act together." in the order given. "This evangelical age" removes the ambiguity, and no "It" now turns toward the IMB or CPM. |
| M-1 | Closed | "presented"; "set out its teaching". |
| M-2 | Closed | The pointer is deleted, the relationsSummary pointer is plain, and the dangling "one" is fixed. |
| M-3 | Closed, except M2-2 | The seven `set` fields are plain and keep their facts. |
| M-4 | **Closed, changed approach accepted** | `validate-census.mjs` lines 211-217 confirm the rule: each modern country's `place` must stand on the place label. IX.56's label already names two places. IX.57's empty list follows the census practice for "N. America". A relabel ("United States · Canada") was possible but is not required (nothing is wrong). |
| M-5 | Superseded | The floorNotes are rewritten in the past tense (see S2-1). |
| M-6 | **Open in statusDescription** | See M2-1. The relationsSummary is closed. |
| M-7, M-8, M-12 | Closed | |
| M-9 | Moot | Carried in the held note. |
| M-10 | Carried | `_meta.kind` records it. The Open-Gaps entry is still owed (M2-4). |
| M-11 | Closed | See the sample below. |
| C-1 to C-4, C-6 | Closed | The key order matches, with `kind` last. The applier applies `metaEdits` as written and recounts. |
| C-5 | Partly closed | Boulder is dropped. Pueblo and the arena still trace to a review's reading (M2-4). |

## New material: clean checks

- **IX.55 `floorNote`.** Each claim matches the HSLDA page verbatim: one God in three Persons; "God became a flesh-and-blood human … Jesus Christ, the Son"; "rose bodily"; binding on leaders, directors and employees, not members. "In 2020" is the page's own byline date.
- **IX.57 `floorNote`.** The doctrine is the publisher's 2023 booklet text, quoted exactly ("three persons of one substance"; "fully God and fully human in one person"; "raised from the dead on the third day"). The 1994 copy's "fully man" does not change the doctrine.
  - "Copies of it published by others date its adoption by the association's board to November 1994" is accurate. The board-adoption sentence appears on bible.ca and religionfacts, not on any publisher page seen.
  - It is fair: it gives the date its true provenance without casting doubt on it, and it does not describe the reproducing sites.
- **The added statement-of-faith sources.** These are the IX.54 Citygate, IX.55 HSLDA and IX.57 AVC/Vineyard USA entries. All three are typed `primary`, and each note matches what was seen: "The page carries no date"; "binding its leaders, directors and employees … members need not be Christian"; "1994 adoption date … seen only in copies published by others". No new source claims more than its note.
- **The other sourcing fixes.** Gaither's book is now correctly outside "university presses" (Palgrave Macmillan). IX.57's "the work of four scholars" is right: Percy, Miller, Poloma and Bialecki, five works in all.
- **Readability sample.** I checked 30 rewrites, old against new: every one in IX.52 and IX.54 to IX.58, plus IX.24, IX.33, IX.45, IX.30 and IX.28.
  - Apart from M2-3 and C2-3, each keeps every fact and adds none. Each also reads more plainly.
  - IX.58 `why` gains "Among them", which is more accurate than before: the four promises listed are not all seven.
  - "From Boulder" is the only fact dropped, and it was untraced (C-5).
  - No new sentence passes 25 words. The release-21 long sentences in other entries' fields are disclosed for the census-wide pass.
- **Meta.** 301 + 6 = 307 rows. Pre-Survey Candidate 219 + 6 = 225, since all six new rows are Pre-Survey Candidates. Every status count matches a recount of the applied census.
- **Window.** The 2020 date in the IX.55 `floorNote` is the date of the Section A evidence, not a claim about the movement's history. It is stated honestly, as the trace's rule asks ("a date where one is seen"). No other post-2010 date was added outside `livingEvidence`, its mirrored sources and the publication years of scholarship.

---

## Verdict

**GATE-ELIGIBLE AFTER FIXES.** There are two substantial findings.
- **S2-1** is mechanical: a one-field rewrite of IX.54's `floorNote`.
- **S2-2** is mechanical only if the IX.53 hold was Mark's direction. Then it needs only a named change order in the Atlas Decision-Log. If it was not his, it needs one question to Mark, and the proposal stands whichever way he rules.
- **M2-1 to M2-4** are mechanical.

A Round 3 recheck should cover only S2-1, S2-2 and M2-1 to M2-3.
