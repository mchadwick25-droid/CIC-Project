Review cap ruling, ijc record audit fixes, 2026-10-13, Reviewer model: Opus 5.5
Verdict: PASS WITH NON-BLOCKING

Scope: the one targeted recheck ordered by the Cap ruling. Checked (a) the two round-3 blocking fixes, (b) independent-review fixes 1-7 and rulings B and C, using `git diff 68fe2e9 HEAD -- records/ijc` (commit 995831c, 32 files), against the vendored texts in `cic/texts/`. Counts: 0 BLOCKING, 5 NON-BLOCKING.

## Verified clean

- (a) ijc.term.imperator-intra-ecclesiam `use_note.means` quotes "The emperor is within the Church, not above it" (npnf210:42663-42664, with "son of the Church" at 42661). ijc.limit.f5-ordinary-day `use_note.means` now says "our record does not hold it". Both round-3 blocking findings are closed.
- Fix 1: the Gibbon note is gone from ijc.dw.baptism-threshold. The "modern scholars" claims are gone from ijc.dw.ancient-custom, ijc.figure.damasus `bridge_line`, and ijc.term.martyrium (`plain_meaning`, `quick_meaning`, `senses.personal`, `senses.translational`, `use_note.means`). "Jerome says Damasus wrote verse" / "fine talent ... many brief works in heroic meter" match npnf203:41382-41383.
- Fix 2: the Hilary locus has the "volume's own introduction" qualifier back. The text now credits the judgment to that introduction ("no reason to suppose ... any wide or permanent success", npnf209:3727-3729; credit to Ambrose, 3736-3737).
- Fix 3: ijc.figure.theodosius `bridge_line` and ijc.story.emperor-penance `use_note.means` follow Ep. LI ("I dare not offer the sacrifice if you intend to be present", npnf210:44183). Both put the penance on the later historians. The Sozomen VII.25 and Theodoret V.17 loci are cited on both records.
- Fix 4: "decades later" replaces "within a generation". The coined closer is removed.
- Fix 6, the quote renderings. No quote `text` changed.
  - leo-tome: "working together with" renders "with the co-operation of".
  - julius-custom: every clause is rendered, and the closing "?" is the source's own, after note 584 (npnf204:23549-23563).
  - chalcedon: "[of God]" is kept as in `text`.
  - canon3: "prerogative of honor" is restored. "His city" refers to Constantinople, the city of the bishop just named, so nothing is added. This is acceptable.
- Fix 7: "night" is removed from every spoken field named. Ep. XX.24 (npnf210:41778-41782) has "that whole day in sadness" and Psalms repeated in the smaller basilica. Confessions IX.7 (npnf101:13766-13774) has the people keeping guard, ready to die with their bishop, singing hymns and psalms. The remaining wording ("under siege", "one standoff", "in the city at the time") rests on those two passages. No Ep. XX.24 source was needed, because nothing now says "night".
- Ruling B: participant turn 2 in ijc.demo.reading-confusion reads exactly "But what about someone like me, who will never read it like an expert?" The body note is updated. Participant turn 1 is unchanged. No participant turn in ijc.demo.someone-like-me changed.
- Ruling C:
  - The Letter 63 sec. 40 text matches npnf210:45073-45079 verbatim. The section number is at 45069.
  - The 396 date matches the volume chronology (npnf210:773). The 377 date for De Viduis is at npnf210:636-637, so ijc.dw.marriage-ranked years 377-396 is right.
  - The source `work` entry for Ep. 63 is accurate. The quote's `divergence_note` and `not_for` no longer call the source a treatise.
- Readability: every touched spoken field and representative turn grades FK <= 10 and FRE >= 60. The lowest is ijc.term.imperator-intra-ecclesiam `senses.personal` (FK 4.72 / FRE 92.4). The highest FK is ijc.figure.leo (9.28). The lowest FRE is ijc.figure.theodosius (60.1).
- `load_world_records('ijc')` loads 186 records.

## Findings

1. NON-BLOCKING. ijc.figure.damasus, `bridge_line`.
   - Old (68fe2e9): "The bishop of Rome who wrote verse. Jerome says he made many short poems in heroic meter. Modern scholars link that verse to Rome's care for the martyrs' graves. Jerome himself does not."
   - New: "The bishop of Rome wrote verse, and Jerome says he had a fine talent for it. He published many brief works in heroic meter."
   - Source: npnf203:41382-41383, "Damasus, bishop of Rome, had a fine talent for making verses and published many brief works in heroic metre."
   - Problem: the sources are matched. But "The bishop of Rome wrote verse" reads as a general statement about the office, not about this man. It also grades FK 4.82, below the FK 8-10 aim that fix 5 set for this field.
   - Suggested replacement (FK 5.85, FRE 77.2): "He was the bishop of Rome who wrote verse. Jerome says he had a fine talent for making verses and published many brief works in heroic meter."

2. NON-BLOCKING. ijc.term.imperator-intra-ecclesiam, `senses.personal`.
   - Old: "Inside those walls the claim was no theory. The people kept watch in the church, ready to die with their bishop. They sang hymns and psalms so that grief would not wear them down."
   - New: "Inside those walls the claim was no theory. The people kept watch in the church, ready to die with their bishop, and they sang hymns and psalms so that grief would not wear them down."
   - Source: Confessions IX.7 (npnf101:13766-13773), "kept guard in the church, prepared to die with their bishop ... lest the people should pine away in the tediousness of sorrow".
   - Problem: the field is accurate, but it grades FK 4.72. Fix 5 named this field for a rejoin toward FK 8-10.
   - Suggested replacement (FK 7.25, FRE 78.7, no new claim): "Inside those walls the claim was no theory. The people kept watch in the church, prepared to die with their bishop, and they sang hymns and psalms together so that the long weariness of sorrow would not wear them down."

3. NON-BLOCKING. ijc.demo.reading-confusion, representative turn 3 (exchange[3].text).
   - Old: "... Nobody wrote down what the listening felt like from the inside, and we will not pretend to know. So you are not behind. Those are the ways our people met this book, as far as our record shows."
   - New: "... Nobody wrote down what the listening felt like from the inside, and we will not pretend to know, so you are not behind. Those are the ways our people met this book."
   - Source: no source issue.
   - Problem: the rejoin turns "you are not behind" into a result of "we will not pretend to know". That is a non sequitur. The reason the participant is not behind is the two shared ways of meeting the book.
   - Suggested replacement for the last two sentences (whole turn FK 6.76, FRE 82.2): "Nobody wrote down what the listening felt like from the inside, and we will not pretend to know. So you are not behind, because those are the ways our people met this book."

4. NON-BLOCKING. ijc.demo.someone-like-me, body note (line 58). This is not spoken, but it is a canonical file.
   - Current: "Augustine, a layman in the city that night, not a chancery voice, ..."
   - Source: Ep. XX.24 and Confessions IX.7 do not support "night". Fix 7 removed "night" from the turn ("in the city at the time"), but the body note still has it.
   - Suggested replacement: "Augustine, a layman in the city at the time, not a chancery voice, ..."

5. NON-BLOCKING. ijc.term.primatus, `senses.evidential` and `senses.informational`. These fields are outside this recheck's spoken-field scope and were not touched here. Log them in ijc `Open_Gaps_Tracking.md`.
   - Current (evidential): "Jerome, who worked in Damasus's chancery, records the verse inscriptions."
   - Current (informational): "built in stone under Damasus".
   - Source: Jerome De Viris 103 (npnf203:41382-41383) mentions verses only, not inscriptions. The record's own locus says "the notice names no inscription".
   - Problem: fix 1 asked for primatus to be kept consistent. The evidential sentence contradicts both its own locus and the vendored text. ijc.term.martyrium `senses.informational` has the same unattributed reading: "public, legible claims that this see's memory of its dead runs back to the apostles unbroken".
   - Suggested replacement (evidential): "Jerome records that Damasus wrote verse." Re-source or attribute the "built in stone" and inscription-program wording in a later pass.
