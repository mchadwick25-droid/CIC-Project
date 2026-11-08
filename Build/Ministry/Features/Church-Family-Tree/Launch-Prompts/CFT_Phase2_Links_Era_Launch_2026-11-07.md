# Church Family Tree, Phase 2: links for one era (P2-L1 to P2-L10)

Paste this into a fresh session, with the era number filled in: "Build P2-L{N}, links for
era {N}, per `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
Converged, auto mode." One era per session. Start the next era in a new session once this
one's pull request is merged.

## The job

For every movement in era {N}, every relationship that its own text names becomes a sourced
link, or the text stops claiming it. The text is the movement's `relationsSummary`,
`longDescription`, `why` and `legacy` in `cic-website/data/world-census.json`.

- A relationship the sources support becomes a link in `edges`, with:
  - one of the six types;
  - one of the five grades;
  - a plain note;
  - sources, with a vendored locus and a verbatim quote wherever a source is primary;
  - `citation_specificity` and `verification_state`;
  - `outcome`, for a major link of the judged types (step 4b).
- A relationship the vendored sources do not support is qualified in the prose ("may have",
  with the reason) or taken out. Never left standing as fact.
- A link to a movement in another era is in scope when this era's movement is the one whose
  text names it.

## Read first

1. `CLAUDE.md`, all of it. Trust, readability and the review cap bind every step.
2. `Build/Ministry/Features/Church-Family-Tree/Build-Plan.md` (Phase 2) and `Decision-Log.md`.
3. `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/`: `README.md` and
   `Drafting_Brief.md`. The six types, the five grades, the source shape and the "grade the
   relationship, not the events" rule are settled there. Use them unchanged. Its wanted-texts
   list may already answer a gap in this era.
4. `tools/validate-census.mjs`: what a link must carry to pass.

## Steps

1. **Inventory (Haiku subagent).** For each movement in era {N}, list every relationship its
   text names: the other movement, the claim, the sentence it came from. Also list the links
   it already has. Write the list to the audit folder.
2. **Draft (Opus subagents, a few movements each).** Brief them with `Drafting_Brief.md`
   plus this era's inventory. For each named relationship, they draft a link, a qualified
   sentence, or a removal, with the reason. They search `cic/texts/` and
   `cic/corpus-map/` for the source. Missing texts go to a `wants` list, never invented.
3. **Quote check (a script, not a model).** Every primary quote must appear verbatim in its
   vendored file at the stated lines. The validator enforces this; run it.
4. **Two-way check.** Every relationship named in the prose has a link, or its sentence was
   qualified or removed. Every link is named somewhere in its movements' text, or its note
   says why it stands alone. List both directions in the audit README.
4b. **Major links (Mark, 2026-11-08).** "Gave rise to", "continued as" and "broke with" are
   major by type and need nothing more. An "influenced", "argued against" or "in contact with"
   link is major only when one of its own listed sources shows a lasting outcome beyond the
   quarrel: a council, canon or law condemning a group; a split into a separate church; a
   teaching, text or practice taken up by the other side; or a rule or practice changed. Such a
   link carries `outcome`: one plain public sentence naming that result, every fact drawn from
   a source already on the link, under about 30 words. Leave the field off when the test is not
   met. The drafting record gives each outcome its source locus and lists the links judged
   minor; the reviewer checks each outcome like any other claim, within the same rounds. The
   audit README counts major links by type and by outcome.
5. **Review (a second, separate Opus 5.5 agent).** Brief it with the census, the sources and
   the drafting record, not with the drafters' conclusions, so its read is independent. Round 1
   is a full review. Later rounds are targeted rechecks of what
   changed. The cap is three rounds, and every review file counts. If a document has not
   cleared after three, stop and escalate.
6. **Prose.** Every new or rewritten sentence meets the reading target. Score each changed
   paragraph with `engine.m7.turn_readability.score_turn`, with a Reading Ease of 60 or more.
   Keep each movement's own voice.
7. **Apply and rebuild.**
   - `python -m engine.m6.cli atlas-sync`, to carry the edges into the map.
   - `node Build/tools/generate_tree_pages.mjs`, for the tree pages and their anchors.
   - `node tools/build_tree_site.mjs`, with 0 mismatched copies.

## Checks before the pull request

- `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`: 0 errors.
  - No published link ID disappears without a `retiredLinks` entry. IDs are permanent.
- `python -m engine.m6.cli check` and `atlas-check --edges-only`: clean.
- `node --test Build/tools/generate_tree_pages.test.mjs`.
- Commentary (`--enforce`), spelling and paths checks: clean.
- Open the map and two tree pages in a browser: the new lines draw and the anchors resolve.

## Output

- `cic-website/data/world-census.json`: links and prose for era {N}, plus the regenerated map
  data and tree pages.
- `Build/Ministry/Operations/Audits/<date>_links-era-{N}/`, containing:
  - `README.md`: counts, the two-way check, rounds, open items and wanted texts;
  - the inventory;
  - the drafting record, with a reason for each link;
  - each review file.
- One pull request for the era: opened as a draft, pushed once after the local checks pass,
  then marked ready. Merge it when CI is green, then check the live tree.
- A status line in `Build-Plan.md`. A decision-log entry only for a real decision.

## Stop and ask Mark

- A relationship whose grading would change a method rule or a settled ruling.
- A movement whose own text is wrong, not just unsupported, where the fix is more than a sentence.
  Log it, flag it, and leave it for the census entry's owner.
- The review cap reached.
- Any metered model call. None is planned. All drafting and review runs in-session.

## Budget

- Opus drafts and a separate Opus 5.5 agent reviews (Mark, 2026-11-07, for this link work).
  Haiku does the inventory and the mechanical work.
- Keep exploration in subagents, so the main thread holds conclusions, not file dumps.
- Heavy eras (9 and 10, about 50 movements each) may split into two pull requests by lane. Say
  so in the first one.
