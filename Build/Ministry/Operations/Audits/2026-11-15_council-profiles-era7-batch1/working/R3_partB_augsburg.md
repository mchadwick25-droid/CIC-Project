## Council profiles, era 7 batch 1, round 3: Part B (Diet of Augsburg 1530)

**Council.** `diet-of-augsburg-1530`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1530.brief.txt`, `audio/diet-of-augsburg-1530.audio.txt`, `diet-of-augsburg-1530.entry.json`, `records.json` key `diet-of-augsburg-1530` (identical to `working/records_diet-of-augsburg-1530.json`, script check), and the README's "Diet of Augsburg (about 2:30)" line. The scope is `git diff 7e0ce987c HEAD` on those files (branch `claude/cft-councils-era7-batch1`, head d20f98a85), checked against `R2_recheck.md` Part B and `R2_changes.md` Part B and preface.
**Brief.** 400 words (`wc -w`), 2:30.0 at 160 wpm, at the ceiling. `grade_text`: FK 7.91, Flesch 60.26. Longest sentence 25 words (the unchanged opening, "At three on a Saturday afternoon ... at Augsburg."). No sentence over 25 words. The figures match `R2_changes.md`.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag (script check after stripping the two tags).
**Entry.** The JSON parses. No changed entry sentence is over 25 words. The one script hit, `decided[13]` (28 words), is unchanged and is the splitter artifact at a quotation's closing full stop that round 2 noted.
**README.** The Augsburg line is unchanged in this round and still matches the brief.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or any fixing. No repo file was edited except this part. No model, network or paid calls were made. `cic/texts/` is unchanged since 7e0ce987c, so all line numbers stand.

Abbreviations as in rounds 1 and 2 (AUG, BOC, BENS, WAT, SARPI, PALL, FPR, ZW2, LW4, BOSS, NIEM).

## Verdict: PASS (no blocking, no substantial, one minor)

All seven round 2 points are closed, and the one substantial point (B2-S1, the translator) is closed. Every changed quote and rendering is faithful. The brief's two changes read cleanly aloud and keep each claim with its witness.

The one minor point is in the B2-S1 fix itself. "The Book of Concord's English" reads as the whole volume's English. The joint committee made only the confession's translation; the volume's editor H. E. Jacobs translated the Apology, which this entry also quotes from the same book (B3-M1).

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| B2-S1 | CLOSED, with a new point | `record[0].note`: "The Book of Concord's English was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German." BOC l.1466-1471: "This Translation is made from the Latin Editio Princeps of 1530-31 ... carefully prepared by a Joint Committee of The General Council, The General Synod, The United Synod of the South, and the Joint Synod of Ohio ... The words in brackets are inserted from the German Editio Princeps." Four bodies, the Latin basis and the bracketed German are right. "Melanchthon's" first printing: BENS l.31324-31326 ("beslöt Melanchton ... själf utgifva texten, hvilket skedde mot slutet af år 1530 och på våren 1531") and l.31345 ("denna Melanchtons första upplaga"). The witness label "H. E. Jacobs's Book of Concord" stands (BOC l.2, "editor and translator"; l.306 signed preface). See B3-M1 on "The Book of Concord's English". |
| B2-M1 | CLOSED | Brief p.2: "and two other confessions." p.5 then names the four cities' and Zwingli's (ZW2 l.1972-1977, 1990-1994). The sentence is 22 words; the brief stays at 400. |
| B2-M2 | CLOSED | Brief p.8: "Waterworth puts the term in a September draft. Buchheim, writing on Luther's side in 1885, puts it in the final decree of 19 November." (7 and 16 words.) WAT l.2497-2505 ("On the 22nd of September ... the proposed edict ... time was now allowed them till the I5th of the ensuing April"); FPR l.3488-3493 ("This Imperial Decree ... was finally issued on the 19th of November with the additional clause ... a time of respite ... until the 15th April, 1531"). Buchheim's authorship and date: FPR header (Philadelphia, 1885) and l.1576-1583 ("By Professor Buchheim"). "They refused" still follows both accounts (WAT l.2541-2544; PALL l.17600-17601). The fixer applied the entry change at `issue[4]`, the right index: "Buchheim, writing on Luther's side in 1885, quotes the writ's aim 'to settle the prevailing discord'." FPR l.3337 ("His avowed object was 'to settle the prevailing discord"). The `record` label "An 1885 historian on Luther's side" is a label, not a spoken sentence, and may stay. |
| B2-M3 | CLOSED | `uncertain[0]`: "He says the printed German surely differs considerably from the text read at Augsburg, while the Latin is mainly unchanged." Claim 107: "Bensow judges that the printed German text surely differs considerably from the one read at Augsburg; ...". BENS l.31339-31341: "De största förändringarna äro vidtagna i den tyska texten, hvilken säkerligen betydligt afviker från den i Augsburg upplästa. Den latinska texten är däremot i det hufvudsakliga oförändrad." "Surely" renders "säkerligen"; "mainly unchanged" renders "i det hufvudsakliga oförändrad". Claim 107's remaining clauses are Bensow's at l.31343-31348 (Mainz manuscript, "hvars noggrannhet är underkastad starka tvifvel"), inside the cited range l.31330-31348. |
| B2-M4 | CLOSED | `traditions[0].note`: "They refused the Catholic reply (Melanchthon) and the first terms of the decree (Waterworth's September draft; Pallavicino's first recess)." "September" now sits with Waterworth only. "First recess" stands on Pallavicino himself: PALL l.17567-17569 ("publicò il Recesso"), l.17600-17603 ("Essendo queste condizioni ripudiate da principali Protestanti; venne Cesare ad vn secondo Editto ... rammemorando ciò che si conteneva nel primo, e 'l rifiuto d'esso", OCR garbled). |
| B2-M5 | CLOSED | Contested claim 13, side one: "Told before the 13 July draft of the reply, with no date given: Waterworth (... l.2440-2446)". WAT l.2440-2446: the commission "of seven, but which was afterwards reduced to three, of each party" is told, then "On the I3th of July the reply of the Catholic Theologians was completed, but ... it was required to be made shorter". "Draft" is fair, since Waterworth has the reply amended before 3 August (l.2446-2450). |
| B2-M6 | CLOSED | Absent detail 5, new first two sentences: "LW4 holds his Exhortation to the Clergy Assembled at the Diet, written at Coburg (... l.15631 on, 15664-15669), and C. M. Jacobs reports his letter to Melanchthon of 29 April about it (l.15668-15670). Jacobs quotes his letter to Melanchthon of 5 July (l.6245-6247)". LW4 l.15631-15634 (title), l.15645-15646 ("Luther's first work at Feste Coburg"), l.15664-15669 ("On April 23, he took up his residence at the castle — Feste Coburg ... He began work on the Exhortation as soon as he was settled in the castle. On April 29 he wrote to Melanchthon that the work was growing under his hands"), signed "CHARLES M. JACOBS" l.15723. The 5 July letter: l.6245-6247, in the Sermon's introduction, signed "CHARLES M. JACOBS" l.6284, so "Jacobs" is C. M. Jacobs, named in the sentence before. The absence itself still holds (searches below). |
| B2-M7 | CLOSED | Not applied to `R1_changes.md`, which stays as the round 1 record. `R2_changes.md` Part B records the correction: three words cut ("two", Waterworth's "J.", "church"). With B2-M1 applied, `R1_changes.md` Part B's line on "the two other confessions" is again true of the brief. Correcting in the later, append-only record is the right way to fix an audit trail. |
| B-M10 | OPEN, by design | Census differences are still held for the batch's single Open-Gaps entry at merge (`R2_changes.md` Part B, "For Open-Gaps"). No tradition id changed in round 2, so no census recheck was needed. |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**B3-M1. Minor (the committee given the whole volume's English, in the entry's `record` note: new text from the B2-S1 fix).**

Location: entry `record[0].note`.

Text: "The Book of Concord's English was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German."

Evidence: the joint committee made the confession's translation only. H. E. Jacobs's 1911 preface: "for the translation of the Augsburg Confession ... we have substituted the translation officially approved by the General Council after its preparation by a joint committee of the various synodical bodies" (BOC l.286-293). The preface to the first edition: "The Apology of the Augsburg Confession, the Smalcald Articles and the Formula of Concord were translated by the Editor" (BOC l.328-330); the Large Catechism by A. Martin (l.322-323). Read as written, "The Book of Concord's English" covers the volume. This entry quotes the Apology's preface from the same book ("How could they assent ...", `fromThoseThere` "Melanchthon's preface (H. E. Jacobs's Book of Concord)"), and that English is Jacobs's, not the committee's. The note sits under the confession's own witness row, so most readers will take it for the confession; the wording still claims more than the held line gives. Also, the bracketed words come from the "German Editio Princeps" (BOC l.1470-1471), not from the German in general.

Fix, entry `record[0].note`, its second and third sentences: "Its English in the Book of Concord was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German first printing." (15 and 18 words.) The rest of the note stays as it is. The brief is untouched.

## Verified

- **Brief, the two changed sentences, against their source lines in context.**
  - p.2: "and two other confessions" (ZW2 l.1972-1977, Bucer and Capito's confession of the four cities; l.1990-1994, Zwingli's Fidei ratio). Both are named in p.5, after the brief's own record sentence, which is now a fair forward reference.
  - p.8: "Waterworth puts the term in a September draft" (WAT l.2497-2505, the proposed edict of 22 September). "Buchheim, writing on Luther's side in 1885, puts it in the final decree of 19 November" (FPR l.3488-3493; FPR header; side, FPR l.3450-3451 as round 2 found). Split from one gapped sentence into two; each keeps its own witness, and "They refused" follows both.
- **Quotes, verbatim.** No quote in the brief changed. In the entry, `issue[4]` keeps "'to settle the prevailing discord'" (FPR l.3337, verbatim) and "'heresy'" (unchanged).
- **Translations.** "Surely ... considerably ... mainly unchanged" for BENS l.31340-31342 (faithful, nothing added). "First recess" for PALL l.17600-17603 ("nel primo"), faithful. The `record` note's "words added from the German" for "The words in brackets are inserted from the German Editio Princeps" (BOC l.1470-1471), faithful apart from B3-M1's precision point.
- **Split and joined sentences.** Brief p.8 (above). `record[0].note` now has five sentences: the committee and its basis are BOC l.1466-1471; "Melanchthon's" first printing is Bensow's (l.31324-31326, 31345), which the note's witness row also cites; the Gutenberg and Bensow sentences are unchanged. Absent detail 5: the Exhortation and 29 April letter sit with LW4 and C. M. Jacobs; the 5 July letter with C. M. Jacobs; the Sermon and Melanchthon's letters unchanged.
- **Records.** Claim 107, contested claim 13 and absent detail 5 checked against every cited line. `records.json` key equals the working file. The JSON parses.
- **Audio.** Identical to the brief apart from the two tags.
- **Writing.** No AI tells in any changed reader-facing string: no empty contrasts, no "X and never Y", no summing-up lines, no filler, no editor's view told as settled. "Surely" is Bensow's own hedge, now attributed. Every changed sentence earns its place, and the brief stays at the ceiling without the fixes adding words.

## Searches run (absences)

No new absence was added in round 2. Absent detail 5 ("Luther's letters from Coburg about the Diet") was rewritten, so its absence was rechecked over `cic/texts/*.txt`, case-insensitive:
- `coburg|koburg|coburgk|choburg|gruboc|grubok` (34 files). Read the relevant hits: LW4 (l.6236, 15645-15669, the Sermon's and Exhortation's introductions), BENS l.31232, 31238, 31311 (the journey and the copy sent to Coburg, not a letter of Luther's), Table Talk l.3307 (a distance), Spener l.2152 (a later Coburg superintendent); the rest are unrelated (Palacky's Hussite-war Koburg, the printer Koburger in Schwenckfeld, Glassberger, Perry's "Coburgi 1770").
- `from (the )?(castle of )?coburg|aus coburg|ex coburg|coburgi|in eremo nostr|vom reichstag|reichstage? zu augs`, and `luther.{0,60}(an|to|ad) (melan|philipp)` restricted to lines with 1530. No hit is a held letter of Luther's from Coburg; Spener l.1343 names the Diet in passing.
- **The absence holds.** The rewritten note now names the held Coburg writing (the Exhortation) and the two reported letters, so it no longer suggests that nothing is held.

## Counts

Blocking 0. Substantial 0. Minor 1 (B3-M1).
