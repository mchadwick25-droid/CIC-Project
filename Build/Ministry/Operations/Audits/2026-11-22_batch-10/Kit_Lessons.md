# Batch 10 lessons for the brief kit

The proposals, from a read of the batch. Each anchor below was checked with `grep -cF` and occurs exactly once in its file.

Paths: `KIT` = `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`; `ROLES` = `.../Brief-Kit/roles/`; `B10` = `Build/Ministry/Operations/Audits/2026-11-22_batch-10/`.

---

## Durable gaps

### 1. Nobody may send a hand content after its prompt (failure 1, the coordinator's push)

**Evidence.**
- `B10/priscillian/Writer_About_Reply.md` l.3: "Then added one Saragossa clause, as asked, with an equal cut". l.39-42: the clause "a modern historian thinks, they banned Sunday fasting and women's private meetings" rests only on Hefele's supposition (Hef2 17955-18020).
- Decision-Log, "No modern opinion, guess or reconstruction in a story" (2026-11-23): "added in the 'what it was about' pass at the coordinator's push".
- `B10/About-Pass/C_Writer.md` already said "Add no quote, fact or feeling the outline does not hold". The extra request came from outside the prompt.

**Why it recurs.** The kit bars rule text from the batch header. It says nothing about a coordinator asking a hand for more after the prompt goes out. The no-modern rule would now block Hefele, but the path is still open for any content the outline does not hold. The checker and the four-fault re-read never see that content.

**Edit.** `KIT`, Part 4, The batch header. Replace:
> Rule text that would hold for the next batch belongs in this kit, not in a header.

With:
> Rule text that would hold for the next batch belongs in this kit, not in a header. No hand is sent anything after its prompt: content the outline lacks goes back to the researcher and the outline check, never straight to the writer.

### 2. A sentence outside the outline is cut, not written into the outline to match (failure 1, second half)

**Evidence.**
- `B10/priscillian/Fresh_Read_About.md` l.51-54: "BLOCKING — the Saragossa clause is outside the outline ... the story needs no change. The outline must carry it." Its fix added the Hefele clause to the outline and the source sheet, and wrote a Do not say line that allowed it ("Say: a modern historian thinks it did").
- `B10/priscillian/Fresh_Read_About_Applied.md` l.5 and `Outline_Synced.md` l.8-9 carried that out. The clause reached the recorded sample and was cut only in the modern pass (`priscillian/Modern_Pass.md` item 5).

**Why it recurs.** `roles/reviewer.md` step 3 says "Trace every sentence to `Outline.md`" but does not say what happens to a sentence that does not trace. A reviewer can "fix" it by moving it into the outline, which skips the outline check.

**Edit.** `ROLES/reviewer.md`, step 3. Replace:
> Each is BLOCKING. A clear story can still hold a factual error.

With:
> Each is BLOCKING. So is a sentence the outline does not hold: its fix cuts it, never writes it into the outline to match the story. A clear story can still hold a factual error.

### 3. The recheck's replacements have no one to apply them (failure 2)

**Evidence.**
- Seven of the ten rechecks returned FIX with exact replacements: Frumentius, Cassian, Mesrop, Pelagius, Priscillian, Theodoret, Ulfila (`B10/<slug>/Recheck.md`). Each was applied by hand in an extra file, `Recheck_Applied.md`, which no role names.
- In the what-it-was-about pass, early writers wrote from outlines that did not yet carry `About_Check.md`'s replacements. The writer prompt was changed mid-pass to sync first (commit e2a854c45, "writer step now syncs the outline"; `About-Pass/C_Writer.md` l.7; every `<slug>/Outline_Synced.md`).
- `B10/Fresh_Read_Fixes_Verified.md` l.6 (Eutyches): "The outline still cites only Zach 1167-1172 and 4095-4097 for that clause."

**Why it recurs.** Kit Part 4 step 2 and `roles/checker.md` (recheck pass) end at "Write `Recheck.md`: PASS, or FIX with the exact replacement text." No step applies that text before the writer reads the outline.

**Edit.** `KIT`, Part 4, step 2. Replace:
> The researcher applies the findings (its fix pass), and the checker rechecks only what the fix changed.

With:
> The researcher applies the findings (its fix pass), and the checker rechecks only what the fix changed. Each exact replacement the recheck gives is applied to `Outline.md` word for word before the writer starts.

### 4. The card role's quotation-mark rule contradicts the validator (failure 4)

**Evidence.**
- `B10/Release_Modern.md` "Stopped": `ERROR priscillian: quotation not found verbatim in the files it cites: "sixty years on"`. The phrase was the brief's own words in a `briefReferences` entry.
- `B10/priscillian/Card_Check_Modern.md` l.12 passed it, because the rule allows it: "quotes 'sixty years on' verbatim from the brief".
- `tools/validate-census.mjs` l.461-480 (`checkQuotes`): every double-quoted span of 8 or more letters in card prose must stand in a file the card cites, or be listed in `tools/quote_renderings.json`. The brief's narration is neither.
- Card hands ran only `--skip-quotes`, since the full run "is killed for memory" in their sessions (`priscillian/Card_Edits.md` l.3; `ulfila/Card_Edits.md` l.5). So the error reached release.
- Fixed by hand: `priscillian/Card_Edits.md` l.119.

**Why it recurs.** The root cause is the rule in `roles/card.md`, which allows exactly what the validator fails. It is not the skipped run. The rule should match the validator, so the `--skip-quotes` run card hands can finish is enough.

**Edit.** `ROLES/card.md`, the census paragraph. Replace:
> In `briefReferences`, use no quotation marks unless the words stand verbatim in the brief.

With:
> In card prose, put quotation marks only around a source's own words, as a cited file or the brief's quotations give them, since the census validator looks for every quoted span there. Give the brief's narration without them.

### 5. Card hands' scratch work is not kept apart (failure 3, second half)

**Evidence.**
- `B10/README.md` open items: "the card writers shared scratch scripts; the Frumentius writer re-ran a shared `build.py` that may have rewritten `eutyches.card.json`."
- Commit 70866899c removed `john-cassian/scratch_census.json` (129,041 lines) and `scratch_edit.py`. Open-Gaps 384, "Closed": the scratch census copy was committed and "stays in history".
- Commit 099b55004 removed another stray scratch file.
- The fix moved twice: `About-Pass/E_Card.md` put scratch "inside your own folder", which is how the census copy got into the repo. `Modern-Pass/J_Card.md` and `L_Apply_Card_Fixes.md` moved it outside the repo, per story.

**Why it recurs.** Card writers build cards in parallel and run the validator on a census copy. `roles/card.md` says nothing about where scratch goes.

**Edit.** `ROLES/card.md`. Replace:
> Do not edit the census, the existing card or the brief, and do not commit.

With:
> Do not edit the census, the existing card or the brief, and do not commit. Keep any scratch script or census copy outside the repository, in a folder for this story alone, and never run another hand's script.

### 6. The card check does not confirm what was sent to the card, or how a modern view is credited

**Evidence.**
- Decision-Log, "Batch 10: the cards carry what the outlines sent them" (2026-11-23): about 106 "to the card" items, many not carried, and "the card checks did not enforce the line until Theodoret's checker raised it". A whole extra card pass followed (`B10/Card_Pass_2_Prompt.md`, `Card_Pass_2_Check_Prompt.md`).
- `Modern-Pass/K_Card_Check.md` had to add: "Check above all that each modern view on the card is credited by name to its modern source and marked as modern."

**Why it recurs.** The writer half of `roles/card.md` has the line ("Whatever the outline, review or fresh read sends to the card goes under `uncertain` ..."). The check pass, items 1 to 7, never asks for it. Under the no-modern rule, every batch will now send modern views to the card.

**Note.** That ruling said "This batch carries out the role's existing line; no kit change." It changed the writer's duty, not the check. This edit adds the check, so it is Mark's call.

**Edit.** `ROLES/card.md`, the check pass. Replace:
> 1. Each edit or field is justified by its evidence.

With:
> 1. Each edit or field is justified by its evidence, and each item the outline, review or fresh read sends to the card is on it, a modern view credited by name to its modern source.

### 7. The checker does not test what the outline calls "not held"

**Evidence.**
- `B10/council-of-ephesus-431/About_Check.md` finding 1 (BLOCKING): the outline said the only account of Pelagius's teaching was Percival's summary. The council's own canons (NPNF214 36504-36527) and the sibling's sheet held it.
- `B10/eutyches/About_Check.md` finding 4: a "not held" reason was wrong, since Perry holds the charge.
- `B10/john-chrysostom/Gaps.md`: the causes of his fall "sit in a vendored text the reviewer had open, but were never researched" (Socrates VI, `npnf202`).
- `B10/rufinus-of-aquileia/Gaps.md` l.12: "What made Origen dangerous was never researched."
- The ad-hoc checker (`About-Pass/B_Checker.md` item 2) added "Spot-check that an item marked not held is truly not in `cic/texts/`". That check found the Ephesus error.

**Why it recurs.** Under "Explain it or leave it out", a false "not held" quietly drops a meaning. `roles/checker.md` item 7 spot-checks only "a search for the subject".

**Edit.** `ROLES/checker.md`, item 7. Replace:
> no held primary text or major later witness is missing, and every claim that rests only on an editor or a modern historian is marked modern.

With:
> no held primary text or major later witness is missing, every claim that rests only on an editor or a modern historian is marked modern, and each thing the sheet or outline calls not held is searched for in `cic/texts/` by its name forms.

### 8. A story approved before the kit is reviewed with no source sheet (failure 6)

**Evidence.**
- `B10/john-chrysostom/Gaps.md`: "MANY GAPS. Each step of his fall is told as an event without its cause. The causes sit in a vendored text ... never researched into the story."
- `B10/ephrem-the-syrian/Reviewer_Prompt.filled.md` l.4-5: "reviewed here, not researched again ... No outline. There is no `Outline.md` or `Source_Sheet.md`." The reviser, bound to "only what the outline holds", had nothing to fix from.
- Both later needed an `Outline.md` made from nothing in the what-it-was-about pass (`About-Pass/A_Researcher.md` step 3: "create `Outline.md` if the folder has none").

**Why it recurs.** Gregory of Tours is still to come in era 3 (Open-Gaps 377). The reviewer must now block every named thing a listener can't explain, so a pre-kit story will fail with no outline to fix it from.

**Edit.** `KIT`, Part 4, step 0. Replace:
> A story approved before this kit is reviewed in its era's batch, keeping its approved wording wherever it passes.

With:
> A story approved before this kit is reviewed in its era's batch, keeping its approved wording wherever it passes. The researcher first makes its source sheet, with the Library sweep, giving what each charge, teaching, book, quarrel or decision it names was about.

### 9. Recording leaves stale audio and stale paragraph times (failure 5)

**Evidence.**
- `B10/recording/Balance.md`: two Priscillian samples (3,977 credits) whose text later changed. The first was "removed before release".
- `B10/Release_About.md` "Not done": `list_story_status.py` marked Priscillian, Chrysostom and Ephrem "Recorded: yes" from audio older than their briefs. Open-Gaps 384 has the tool fix; owner, the next tool session.
- Open-Gaps 381: "Paragraph times are not remade when a brief is re-recorded ... Nothing in the recording run prompts it." Batch 10's times were made by hand after the run (commit af953a576).

**Why it recurs.** Kit step 9 records a sample for Mark's ear first, so a sample whose text then changes will happen again. Nothing in step 9 removes such audio or runs the alignment.

**Edit.** `KIT`, Part 4, step 9. Replace:
> Every setting in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Recording_Settings.md` is passed on the command and printed, and the balance is read before and after.

With:
> Every setting in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Recording_Settings.md` is passed on the command and printed, and the balance is read before and after. Then `python Build/tools/align_tree_narration.py --only <ids>` remakes the paragraph times, and its `--check` lists none stale. A recording whose text later changes comes off the branch until it is recorded again.

### 10. The release runs two checks more loosely than CI does

**Evidence.**
- `About-Pass/G_Release.md` item 5 and `Modern-Pass/M_Release.md` item 4 both had to add `check_live_commentary.py --base origin/main --enforce` and `check_open_gaps_numbers.py`.
- CI runs both as gates (`.github/workflows/ci.yml` l.446 and l.486).
- `roles/release.md` step 5 runs `check_live_commentary.py` with no flags, which reports but does not enforce. It does not run the Open-Gaps check, although each batch appends Open-Gaps entries (`Launch_Template.md` l.19).

**Why it recurs.** A release that passes locally can still fail CI, which costs a second push (CLAUDE.md: one full CI run per pull request).

**Edit.** `ROLES/release.md`, step 5. Replace:
> `python tools/check_live_commentary.py`; `python tools/check_spelling.py --enforce --base origin/main`;

With:
> `python tools/check_live_commentary.py --base origin/main --enforce`; `python tools/check_open_gaps_numbers.py`; `python tools/check_spelling.py --enforce --base origin/main`;

---

## Already covered

| Ad-hoc instruction or failure | Covering line |
|---|---|
| Explain each charge, teaching, book, quarrel or decision, from each side, enemy credited (A_ steps 1-2) | `roles/researcher.md` 1: "For every charge, teaching, book, quarrel or decision, give what it was about in its own terms, from each side the held texts give, an enemy's included." Kit Part 1: "An enemy's charge is given in its own content ... never dropped because only an enemy says it." |
| Plain sense in one line with source and confidence (A_ step 3) | Kit Part 3, Story beats: "it also gives what that was about, in one plain line with its source." |
| If not held, leave it out (A_ step 2) | Kit Part 1: "If there is no room to explain it, the story does not name it." `researcher.md`: "If a source is not held, say so." |
| Room for it: cut events before meanings (A_ step 4, B_ item 4) | Kit Part 3, Length: "never cut ... what a named charge, teaching, book, quarrel or decision was about ... cut an event before its meaning." `checker.md` 3: "So is a cut-first list that drops what a named charge ... was about." |
| Checker: witness and confidence right (B_ items 1, 3) | `checker.md` 1: "says no more than its source, and carries the right confidence level and witness kind." |
| Writer: weave it in, never a bolted-on "this was about" sentence (C_ item 1) | Kit Part 1, Accessibility: "work any puzzling word or custom into the sentence as part of what happens"; Part 1, Explain it or leave it out. No batch 10 file shows a bolted-on explanation. |
| Writer: re-hear as a first-time listener, can you say what each was about (C_) | `writer.md`: "hear it once as the standard's listener"; Kit Part 1, the test: "what it was about". |
| Fresh read lists each named thing and blocks the unclear (D_, I_) | `reviewer.md` 1: "List each charge, teaching, book, quarrel or decision the story names: one a listener could not explain after one hearing is BLOCKING." |
| Find every sentence resting on a modern source, even unnamed, dates and causes included (H_ step 1, I_ step 1) | Kit Part 1, Rigor: "Nothing in the story rests on a modern opinion, guess or reconstruction, credited or not." `reviewer.md` 3 and `checker.md` 1 block it. `Kit_Edit_Check_No_Modern.md` finding 1 removed such a list on purpose, since a list narrows the rule. |
| Where old sources are silent, say so or cut; a modern find told as an event (H_ step 2) | Kit Part 1, Rigor, same bullet. |
| A Do not say line for each modern claim removed (H_ step 3) | Kit Part 4, Keeping the kit clean: "An error a writer could repeat goes into that outline's Do not say list." |
| Card: add new references, remove ones the brief no longer tells (E_ 1, 3; J_ 2; K_) | `card.md` New 1: "Add the references the brief draws on"; check pass 3: "A `briefReferences` entry that names something the brief no longer tells is removed." |
| Card: carry "to the card" items (E_ 2; J_ 1) | Writer side: `card.md`: "Whatever the outline, review or fresh read sends to the card goes under `uncertain` or the field it belongs to." (Check side: gap 6.) |
| Card quotations, one per span, secondReading rules (E_ 4; J_ 3) | `card.md` census paragraph: "Give `quotationOriginals` one entry for each quoted span in the brief, and none for a span the brief no longer quotes." |
| Card check against starting card, nothing else moved (F_, K_) | `card.md` check pass 2. |
| Apply card-check fixes word for word (L_) | Kit Part 4 step 8 and `release.md` 1: "Apply each `Card_Check.md` FIX ... word for word." |
| Census: change only the two fields, diff to prove it; no re-dump (G_ 2, M_ 2) | `release.md` 2: "Change no other field." The first release made the field-by-field diff under the standing role (`Release.md`). No batch shows a re-dump. |
| `quote_scan_readings.json` readings where a scan breaks a quote (G_ 4) | `release.md` 5: "Fix a failure only where the fix is mechanical." The first release added 14 readings under it, each checked (`Release.md`). |
| Readability on every brief (G_ 5) | `release.md` 5: "`python -m engine.m1.profile_readability` on each brief". |
| A changed quote gets a blind second reading (About-Pass/Second-Reading) | Kit Part 4 step 7 and `second-reader.md`. |
| Release stops on a content failure (Release_Modern) | `release.md` 5: "If a check fails for a reason in a brief's or card's content, stop and report it." It worked as written. |

---

## Batch-10-only

- **Card.pass2.json / card.json swapped (failure 3, first half).** This came from the ad-hoc re-pass wording that reused `<slug>.card.json` as both start and result (fixed in E_Card, commit 013272086). The standing role names the start `{CARD}` (`Card.existing.json`) and the result `{SLUG}.card.json`, and says "Do not edit ... the existing card".
- **The what-it-was-about and modern passes as a whole (A_ to M_).** They were targeted re-passes over finished briefs: `.v3`/`.v4` diffs, Gaps.md leads, "add no new quotes", Card.pass2/pass3. Under the kit as it now stands, batch 11 does all of this in the first pass. Re-passes over the live tree belong to the what-and-why ranking thread (Decision-Log, "The live stories reopened ...", 2026-11-23).
- **Lengths for the pass (persons 675, council 585, Chrysostom and Ephrem up to 450).** These were Mark's ruling for batch 10 alone (`Release_About.md`, rulings table).
- **Second and third releases (G_ 1, M_ 1, 3: verify already-applied fixes by script, no re-apply).** These were needed only because the batch was released three times.
- **Ephrem's Palladius quote drifted from both Clarke and the project's rendering.** It was a pre-kit live text, and it is closed by its second reading. The recurring cause, pre-kit stories with no sheet, is gap 8.
- **Not proposed, already open with Mark:** why outlines run long (Open-Gaps 378a, three fixes at research) and whether card writing moves to Opus (Open-Gaps 378b). `list_story_status.py` counting stale audio is a tool fix (Open-Gaps 384), not kit text.
