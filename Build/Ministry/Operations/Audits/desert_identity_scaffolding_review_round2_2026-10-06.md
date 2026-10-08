# desert — identity-and-scaffolding record pass, adversarial review round 2 (2026-10-06)

Branch `records/identity-scaffolding-desert`, fix commits 51016404 (records, pin, OG-21) and 8cd73923 (site JSON). Targeted recheck against round 1 (`desert_identity_scaffolding_review_round1_2026-10-06.md`) only. Reviewer: Opus 5.5. No model spend; no records edited.

**Verdict: REVISE.** This is round 2 of the cap of three.

The oblique-scope question (does the oblique shape cover `desert.dw.god` and `desert.dw.the-heart-and-the-spirit`?) is still open with the project lead and is not decided here. Neither witness was reordered. `desert.dw.god` is untouched on the branch. `the-heart-and-the-spirit` changed only its opening clause.

## Round 1 findings, rechecked

- **1 (OG-21 oblique reason): fixed.** The new reason matches round 1's wording sentence by sentence. It names SS69, SS72-80 and SS81 as direct statements and says all are Athanasius's report, Contested as Antony's own words, and concentrated in a few episodes. It applies the ruling to `desert.dw.jesus` only and says the scope is open with the project lead and that neither other witness was reordered. "Found oblique throughout, none of it partial" is gone. "The reviewer (round 1) agrees `desert.dw.jesus` is oblique and holds the world partly direct" is accurate.
- **2 (`kellia-day` absent_detail): fixed.** The record now reads "was found to support". The Palladius spare-diet passages and the frontmatter build history are logged for the project lead, not fixed, as asked.
- **3 (dangling id): fixed.** OG-21 now says the removed body sentence was the only occurrence. Confirmed: `desert.limit.f4-t-born-again-and-tithe` occurs nowhere in `records/`.
- **4 (carried known-wrong list): fixed for the round 1 list.** OG-21 now names items 5, 9, 13, 14, 17, 18 and 19, and moves item 20 and item 15 to "not edited". The item numbers match OG-19. It is now incomplete again because of the newly edited record; see finding B.
- **5 (orphan in `the-heart-and-the-spirit`): fixed.** The opener reads "besides our most systematic teacher's, and we will not flatten it into his". The antecedent comes from the next sentence. No new claim. The Macarian quoted sentence is unchanged word for word; only the line wrapping changed.
- **6 (`virgin-who-hid-athanasius` body): fixed.** The "WHY THIS AND NOT ..." paragraph is removed, and the closing paragraph is trimmed to the pointer. Also applied: the round 1 suggestion for `angel-hands-the-tablet`'s body pointer, and the optional `pachomius-founding` trim.

No claim or sourcing changed in the fix commit. No new orphan.

## Findings

**A. SUBSTANTIAL — commentary left in an edited live file: `desert.dw.the-heart-and-the-spirit` body.** Fix 5 put this record into the PR's edited set. Under CLAUDE.md, the PR must therefore also remove the commentary already in its body. The body still carries the same classes this pass removed from the other 14 records:
- the register boilerplate, "The text follows the desert register: short sentences, everyday words; every claim, name, quote, hedge, and reviewed constraint is kept.";
- the build-history paragraph, "This record closes a gap that was total rather than partial: before it, no record in this world mentioned the Holy Spirit at all, while F1-I carries ... as a canon question. The cell was answered by desert.dw.god ...". This is a question code plus narration of the corpus state before the record existed;
- the process phrase "before today" in "Every interior term this world held before today was Evagrian".

`check_live_commentary --enforce` passes, but the gate does not catch these lines. OG-21's sentence "Commentary removed from the markdown body of the 14 edited records" is therefore not true of all edited records. **Fix:** remove the register line and the first paragraph. Remove "before today", for example "Every other interior term in this world is Evagrian and analytic". Remove the curatorial headers "WHY THIS IS A SECOND VOICE AND NOT MORE OF THE FIRST." and "THE BOUND IS DOING REAL WORK HERE, not ritual hedging." Keep the genuine source notes:
- the two currents' disagreement;
- the Villecourt/Wilmart and Mason Messalian note, and the register it sets;
- "WHAT IS NOT CLAIMED", as plain prose.

Then rebuild the package, repin, and recompile the site if it is stale.

**B. SUBSTANTIAL — OG-21 inaccurate after the fix.**
1. "Records changed (spoken fields only ...)" still lists 14 records and omits `desert.dw.the-heart-and-the-spirit`. That record is mentioned later as an "Also:", but this list is the entry's statement of scope. Add it, and update "the 14 edited records" once finding A is applied.
2. The carried known-wrong list for edited records omits two items:
   - OG-19 item 12: `the-heart-and-the-spirit` still misquotes `desert.dw.god` in its tensions ("a long stilling of the passions", where `dw.god`'s text has "quieting"). This record is now edited, and the claim is carried unchanged.
   - The first half of OG-19 item 13: the `judgment-and-resurrection` `divergence_note` still says the cell's born-again and tithe questions "are named in this record's own tensions field". They are not there. Once the body sentence was removed, the record no longer points anywhere true for them. OG-21 gives only the four/five half.

   **Fix:** name both as carried unchanged, with their OG-19 items.

**C. Not substantial — `desert.story.pachomius-founding` body punctuation.** The trim left "...in a story record);" followed by the capitalised "The text uses Palladius's own wording". End the sentence at ")" with a full stop.

**D. Not substantial — optional wording.** The new opener of `the-heart-and-the-spirit` is followed straight away by "Our most systematic teacher had ...". The phrase repeats in back-to-back sentences. "That teacher had ..." would read better and adds nothing. Leave it, or apply it with finding A.

## Checks passed

- Pin: `records/worlds/desert.yaml` gives `packages/desert/2026-10-06T23-52-06Z` and `sha256:ca7d572e...656062d`. `engine.m2.manifest.manifest_hash` over that package's `manifest.json` returns the same hash.
- Site JSON: `records_commit 51016404...` is an ancestor of HEAD (`git merge-base --is-ancestor`). The commit changes only `_generated_by`. `site_cli staleness-check` reports `stale: false`.
- Gates re-run at HEAD:
  - `regate desert --base origin/main`: PASS, every miss already failed at the base and is unchanged.
  - `deployed desert`: PASS, pin read from disk, and the `source_anchor` note is unchanged.
  - `determinism-check desert`: PASS.
  - `check_live_commentary --base origin/main --enforce`: exit 0.

  OG-21's gates sentence is accurate.
- OG-21's other sentences: the item numbers checked against OG-19 match. The `kellia-day` Palladius lines (203, 337) and the frontmatter build-history note are as round 1 stated. The `admission_conform` note and "no live admission was run" are unchanged.

## Required for round 3

Findings A and B. Then rebuild the package, repin, and recompile the site if it is stale. C is a one-character fix worth making in the same commit. The oblique-scope question stays with the project lead.
