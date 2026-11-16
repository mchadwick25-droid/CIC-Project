# Era 1 rewrite pass: handover (2026-11-16)

For the session that rewrites era 1's Who and council briefs to Standard v1. Read `CLAUDE.md` first and follow it. The coordinator starts this as a Fable session.

## The job

Rewrite every era 1 Who brief and the era 1 council brief to Standard v1, with their cards and records, as one session and one pull request (Mark, 2026-11-16: "Yes, both (Recommended)"). The era goes through these steps in order:
1. Drafted.
2. Reviewed: round 1 runs the full checklist, then targeted rechecks, inside the three-round cap.
3. Read by Mark, with a sample listen.
4. Released as one data release, carrying any live fixes the era needs.
5. Recorded, only after Mark's yes.

## Scope

- **Who briefs:** 20, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era1/`.
  - Batch 1: Clement of Alexandria, Eusebius of Caesarea, Hermas, Ignatius of Antioch, Josephus, Justin Martyr, Marcion of Pontus, Valentinus.
  - Batch 2: Bardaisan of Edessa, Dionysius of Alexandria, Hippolytus of Rome, Novatian, Pontius the Deacon, Suetonius, Tacitus, Tatian.
  - Batch 3: Anatolius of Alexandria and Laodicea, Peter of Alexandria, Pliny the Younger, Polycrates of Ephesus.
- **Not in scope:** Origen and Methodius of Olympus. They are era 1 people, but they are already at Standard v1 in `Who-Profiles/bar/`.
- **Council:** `Council-Profiles/era1/councils-of-rome-and-carthage-251`.
- **Outside witnesses:** Josephus, Tacitus, Suetonius and Pliny the Younger follow the pattern's outside-witness form. That form has no "what they fought for" beat, so they keep it.

## Read first

1. `Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md` in full, above all:
   - "Standard v1: setting, impact and witnesses"
   - "The brief", with Quotes and the 2026-11-16 rendering rules
   - "Working rules"
   - the checklist, items 1 to 17
   - "How a batch is reviewed and released", with the drift guards
2. `Council_Profile_Pattern.md`, "Standard v1 for councils", and checklist items C1 to C9.
3. `Worker_Brief_Template.md`. Its two paragraphs go word for word into every writer's and reviewer's instructions.
4. The bar, `Who-Profiles/bar/`, all ten briefs. Drift guard 2: every writer and reviewer gets the standard and three bar briefs (Gregory of Tours, Benedict of Nursia and one of the eight), and every review names the bar brief it compared against. Nothing is compared against a previous batch.
5. The 2026-11-16 entries at the end of `Decision-Log.md`: Standard v1, the drift guards, the working rules, the rendering rules, and the Fable exception.
6. `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/`. It is the worked example of this whole process: drafts and references, the two-rendering check for every quotation, the review rounds, and the sample recording.

## The source and significance question, folded into this pass

There is no separate source check (Mark, 2026-11-16: "Drop it, fold the test into each era (Recommended)").
- For the source question, reuse the existing scans:
  - `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era1/`
  - `2026-11-12_who-scan-supplement/`
  - `2026-11-12_who-scan-dedupe/`
  - the 15 November Who check (the "Who Reality Check", version 3), which never reached main. Its page is https://claude.ai/artifact/77MrwWiFsTv2v21qCvPeJi, version 3; read it with the Artifact read action. Mark's rulings on its 14 late-record Whos are in the Decision-Log on the unmerged branch `claude/cft-legend-fixes`, commit `9f88aa23`, entry "Legends told as legends" (2026-11-15). Read it with `git show 9f88aa23:Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, and merge nothing from that branch. His words: "Apply your bar to each", and "lets keep beuno as a story - legend". None of the 14 is an era 1 person (Theopistus, Beuno, Brigid, David of Wales, Brendan, Ciarán, Alopen, Clement of Ohrid, Tekle Haymanot and six Coptic patriarchs), so no ruling from it carries into this pass.
- While reading each person, the writer applies the significance test. Mark's words: "yes, or defended". A Who changed or defended church history or theology beyond their own house or town, and the held sources show it. Recorders stay Whos.
- A Who that fails moves to Story (documented), Story (legend), a mention without a card, or out of use.
- **Borderline cases go to Mark as a short list, through the coordinator, before the era is written.**

## Known flags for era 1, from the Standard v1 sample read (2026-11-16)

- **Polycrates of Ephesus:** "the Roman practice won" rests on McGiffert alone. Tell it through an ancient witness, or say plainly where the record stops. McGiffert goes to the card.
- **Marcion of Pontus:** the card's tradition reads "Marcionism"; the census has "Marcion / Marcionism". Use the census name, and fix the live card in this era's release.
- **Era 1 records:** batches 1 to 3 cite chapters only, with no file or line numbers. Add file and lines for every claim.
- **Seen in all 12 sampled briefs across eras** (`Build/Ministry/Operations/Audits/`, sample read of 2026-11-16, page https://claude.ai/artifact/8PDCPGAj1hHs3iUQ6KKwTW):
  - an opening that starts on a scene with no setting;
  - modern scholars named in the brief;
  - an impact half missing or told as a list;
  - grades below 8;
  - lengths near 400 words with no reason given.

## Quotations

- Every quotation from English printed before 1931, or from any other language or older stage of a language, is told in our modern English.
- Two Opus agents render it, the second without seeing the first, and a third Opus agent compares them against the printed text and, where held, the original. The pipeline is `renderings/` in the eight's record.
- The final reading covers every clause, adds nothing, and follows the original where the printed English adds a word.
- The printed wording, with file, lines and verdict, goes on the card as `quotationOriginals`. Any difference in meaning becomes an `uncertain` note.
- At release, each rendering is listed in `tools/quote_renderings.json` with `original` (file, lines, language) and `second_reading` (record and verdict). The validator rejects an entry whose file the card does not cite.
- On the page, one line under each brief says its quotations are in our modern English. Nothing is added to the spoken text.

## Models

- Drafting, first renderings and the source-check reading run on Fable, model "fable", while the free refill lasts (Mark, 2026-11-16: "use fable for all larger projects until we use the free one up").
- Reviewers, second renderers and comparers stay on Opus.
- If a Fable call is refused or hits a limit, do not retry in a loop. Switch drafting to Opus and tell the coordinator.
- No metered model calls, under `CLAUDE.md`.

## Length

Mark's words are "target under 2 minutes, can streatch to 2:30 if needed, no hard cap" and "we are ok to go long if the content demands it". Councils: "target 2:00 but can streatch to 3".
- The ten in the bar all run at or past 2:30, and Mark has said briefs were "consistantly pushing 2:30". Aim under 2:00 in this pass.
- Write tighter rather than dropping a stance. Give one line for any brief past 2:30.

## Release and recording

- The pull request carries the era's live fixes: flagged facts and tradition names in the census.
- Mark hears one brief picked at random, beside a bar brief, before the era goes live (drift guard 3). His yes is the release.
- Recording is a paid step. Run it only after the coordinator passes on Mark's yes.
  - Use the Jon v4 settings printed in `Build/Ministry/Operations/Audits/2026-11-15_standard-v1-test/README.md`, every setting on the command.
  - Check the credit balance against the charged total before calling the run valid.
- Ask the coordinator for any Open-Gaps number before writing an entry.
