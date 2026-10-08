# desert — identity-and-scaffolding record pass, adversarial review round 3 (2026-10-07)

Branch `records/identity-scaffolding-desert`, fix commits 42064e15 (records, pin, OG-21) and 4d8ad0aa (site JSON). Targeted recheck against round 2 (`desert_identity_scaffolding_review_round2_2026-10-06.md`) only. Reviewer: Opus 5.5, lower effort. No model spend; no records edited.

**Verdict: CLEARED.** This is round 3, the last the cap allows.

The oblique-scope question (does the oblique shape cover `desert.dw.god` and `desert.dw.the-heart-and-the-spirit`?) stays open with the project lead. It is not decided here.

## Round 2 findings, rechecked

- **A (commentary in edited record bodies): fixed.** In `desert.dw.the-heart-and-the-spirit`, these are gone:
  - the register line;
  - the gap paragraph and its F1-I code;
  - "before today", now "Every other interior term in this world is Evagrian and analytic";
  - both curatorial capital headers.

  The kept notes are plain prose: the two currents' disagreement, the Villecourt/Wilmart and Mason Messalian note and its register, and "What is not claimed". The fix also removed "for F4-T" from the `born-again` body and "Step3c" from the `never-settled` body.

  All 15 edited record bodies were read in full and grepped for the round 2 classes: register boilerplate, question and step codes, dated or session phrasing, and curatorial capital headers. None remain. "AUTHOR GRAVITY" is the name of a source caution, not a header. `check_live_commentary --base origin/main --enforce` exits 0.
- **B (OG-21 accuracy): fixed.** I checked it sentence by sentence against the final diff.
  1. The scope list now names 15 records, including `the-heart-and-the-spirit` ("its opening two sentences"), and says "Fifteen records in all". That matches `git diff --name-only origin/main...HEAD -- records/desert/`: 9 witnesses and 6 stories. "The 15 edited records" in the commentary sentence is now accurate, and that sentence lists the round 2 body removals correctly.
  2. Item 12 is added. It matches OG-19 (12), and the record still has "a long stilling of the passions" in its tensions while `dw.god`'s text has "quieting". Item 13 now carries both halves, matching OG-19 (13). The `judgment-and-resurrection` divergence_note still says those questions "are named in this record's own tensions field", and they are not there.

  The package line names the new package.
- **C (`pachomius-founding` punctuation): fixed.** The sentence now ends at ")." The next sentence starts on its own.
- **D (repeated phrase): applied.** The second sentence now begins "That teacher had ...".

## Opener and order

- Compared word by word with `origin/main`, the `text` of `the-heart-and-the-spirit` differs only in its first two sentences:
  - "us," became "us besides our most systematic teacher's,";
  - "the first. Our most systematic" became "his. That".

  The teacher is named in the original second sentence, so the opener adds no claim. Every other frontmatter field is unchanged against `origin/main`, including positions, tensions, sources and confidence. The rest of the text, including the Macarian sentences, is unchanged word for word.
- Neither witness was reordered. `desert.dw.god` has no diff against `origin/main`. `the-heart-and-the-spirit` changed only in `text` and in its body.

## Pin and site

- `records/worlds/desert.yaml` pins `packages/desert/2026-10-07T00-06-59Z` with `sha256:c2d91608...aa4320a`. `engine.m2.manifest.manifest_hash` over that package's `manifest.json` returns the same hash.
- In `cic-website/data/worlds/desert-monasticism.json`, `_generated_by` gives `records_commit 42064e15...`. That commit is an ancestor of HEAD (`git merge-base --is-ancestor`), and 4d8ad0aa changes only that string. `site_cli staleness-check` reports `stale: false`.

## Gates re-run at HEAD

- `engine.m10.cli records desert`: PASS
- `regate desert --base origin/main`: PASS
- `deployed desert`: PASS
- `engine.m2.cli determinism-check desert`: pass, no differing paths
- `check_live_commentary --base origin/main --enforce`: exit 0

OG-21's gates sentence holds.

## Not substantial (no further round; for the build thread)

- The `desert.story.kellia-day` body still opens "The unsourced diet element is not included." This assumes a reader knows there once was such an element. It belongs with the frontmatter build history that OG-21 already logs for the project lead in that same record. Handle them together.
