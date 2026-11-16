# The rendering sample: Groen van Prinsterer, Ongeloof en Revolutie (2026-11-16)

Thread B (Library), session_01JMNsS9WRK3s4XStRhyW6qw. The sample Mark asked to see before any rendering work:
a finding guide for one non-English text, three passage renderings each with an independent second rendering,
and the reviews. The page he saw: https://claude.ai/artifact/5tLkistBZ921HAPq7YARtG. The stored result is in
`cic/renderings/`. Mark's decision is in the Library Decision-Log, "The rendering sample".

The text: `cic/texts/groen-van-prinsterer_ongeloof-en-revolutie-nld_2e-uitg1868.txt` (19,291 lines, about
148,000 words of Dutch, scanned text of fair quality).

## What was done, in order

1. **A guide in 206 small parts.** Eight readers each took a span of the book and wrote the parts from the
   Dutch (`briefs/GUIDE_BRIEF.md`).
2. **First review, 24 parts at random** (`guide-206-parts/R1_review_sample24.json`): 6 sound, 16 minor, 2
   substantial. Both substantial faults misreported Groen's position: lines 7922-8049 gave the revolutionary
   view of the state as his own; lines 262-393 dropped his criticism of Lamartine.
3. **Second pass over all 206 parts** for those fault types (`briefs/PASS2_BRIEF.md`,
   `guide-206-parts/second_pass_change_log.json`): 178 parts changed, 550 changes.
4. **Recheck of 22 parts** (`guide-206-parts/R2_recheck_sample22.json`): 18 sound, 4 minor, 0 substantial.
   The four minor findings were applied. The result is `guide-206-parts/guide_206_parts.json`.
5. **Three passages rendered twice**, by two renderers who did not see each other's work
   (`briefs/RENDER_BRIEF.md`, `renderings/first_rendering.json`, `renderings/second_rendering.json`). Every
   scanning fault in the passages was read on the page image.
6. **Review of the renderings** (`renderings/review.json`): all three "meet the bar with minor fixes"; one
   substantial finding, "the Upheaval" for *Omwenteling*. The fixes are in the stored renderings. The stored
   renderings were not reviewed again after the fixes.
7. **Mark's decision**: renderings as they are; guides at chapter or section level, about 20 to 40 parts a
   book, every part reviewed.
8. **The guide redone in 40 sections**, written from the 206 checked parts (`briefs/SECTION_BRIEF.md`,
   `section-guide/sections_before_review.json`).
9. **Every section reviewed against the Dutch** by eight reviewers, each reading one span of the book in full
   (`briefs/REVIEW_BRIEF.md`, `section-guide/review_every_section.json`): 3 sound, 33 minor, 4 substantial;
   125 findings. The reviewers wrote the corrected text, which is what is stored. It was not reviewed again.

## What to carry forward

- **Two renderings that agree are not proof.** Both renderers wrote "the Upheaval". The brief had told both
  to treat *Revolutie*, *Omwenteling*, *Hervorming* and *Reformatie* as distinct words, which pushed them
  the same way. Give each renderer the bare passage and the bar, nothing that steers a word choice.
- **Whose view.** The commonest serious fault in a guide is a view the author sets out in order to attack,
  reported as his own. The second commonest is a dropped limiting word. Both are in the briefs now.
- **A sample review is not enough for a guide.** The first review found 2 substantial faults in 24 parts;
  the full review of the 40 sections found 4 in 40 after two earlier passes.
- **Footnotes.** The print sets them at the foot of the page and the scanned text lands them some lines after
  their prose. At section level they are noted inside the section, with their lines.
- **The scanned text needs the page image** before any passage is rendered: 17 faults in three short passages.
- **A garbled date.** The scanned text gives lecture XIV's date line as "1794—4845" at line 14447 and
  "1794—1815" in the contents list at line 17866. The page image (printed p. 360) reads 1794—1845.

## Size and cost

The stored guide is 40 sections: about 9,600 words of our prose, 1,733 names and 603 quotation entries.

Subagent tokens, as the harness reports them (reading is most of it; nothing here was a metered call):

| Step | Model | Tokens |
|---|---|---|
| 206-part guide, eight readers | Fable | 1.52M |
| Second pass, eight readers | Fable | 1.74M |
| Two sample reviews | Opus | 0.42M |
| 40 sections written from the 206 parts | Fable | 0.37M |
| Review of every section, eight reviewers | Opus | 1.56M |
| Two renderings of three passages | Fable | 0.20M |
| Review of the renderings | Opus | 0.10M |

A guide written at section level from the start needs one reading pass by the writers and one by the
reviewers: about 1.5M on Fable and 1.6M on Opus for a book of this length, or roughly 21 tokens for each word
of the source. Three passage renderings with their review came to about 0.3M.
