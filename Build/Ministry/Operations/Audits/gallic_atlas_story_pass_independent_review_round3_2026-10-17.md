# Round 3 targeted recheck: Gallic Atlas story pass

Reviewer: Opus 5.5, independent, read-only.
Scope: worktree `agent-a792408e07913bea8`, branch `site/atlas-story-gallic-fixes`, `git diff 4a890e172 9ee272fdd` (4 files: the world_front, and the `telling` fields of the death, Honoratus and cloak stories).
Checked against:
- `gallic.story.honoratus-and-the-island`: divergence_note, tellable_as, text, absent_detail, use_note.
- `gallic.figure.honoratus`, which dates Lerins c. 400-410.
- `gallic.figure.cassian`, `gallic.story.bishop-archebius`: the Germanus of Auxerre guard.
- `gallic.core.gallic` thinness ("the house we know least from inside").
- `gallic.limit.only-on-paper`.
- Vendored `npnf211`:
  - Vita III, l. 800-816: the tribune as "familiar tent-companion", "the period of his office".
  - Inst. Pref., l. 16503-16508: "have also seen them fulfilled under our very eyes ... nothing but astonishment and no instruction in the perfect life".
- Readability: scored with `engine.m1.gates.grade_text`.

---

## 1. Round 2 findings: status

| Finding | Status |
|---|---|
| R1 Honoratus wording hedge | **Fixed.** "As far as ... sermon can be read" now covers the priesthood claim in the telling, teaser, unit 3, voice and who_speaks. In unit 3 the claim now sits inside the hedge. This matches `use_note.means` and `tellable_as`. |
| R2 unread text as source silence | **Fixed.** "Almost all ... comes from part of Hilary's funeral sermon" no longer contradicts "became a bishop", and "we cannot tell you" puts the gap in our knowledge, not in the sermon. "The island's daily life is known least of all" follows the core's own "the house we know least from inside". (See N-B for one wording point.) |
| R3 Cassian and wonders | **Fixed.** All three places now limit the refusal to the Institutes. "The wonders he had seen" and "teach nothing about how to live" rest on Inst. Pref. ("seen them fulfilled under our very eyes ... no instruction in the perfect life"). It no longer clashes with the angel card. |
| R4 sourcing "saint's power" | **Fixed.** Power is now credited to Tours only. The Cassian clause ("Egypt's customs more than the days of his own houses") fits `only-on-paper`. |
| S-1 Trier teaser | Fixed ("In return, the officers sent ... are called back"). |
| S-2 tile | Fixed. The discharge is no longer placed in the Loire valley. |
| S-3 Martin voice | Fixed ("drew him out by a trick and made him their bishop"). |
| S-4 cloak tribune | Fixed. "His commander, a tribune who shared his tent ... once his own command ended" matches Vita III. "His" now plainly refers to Martin, and "his own command" to the tribune. |
| S-5 Postumianus "his" | **Not fixed.** The new wording has a new unclear pronoun (S-B below). |
| S-6 Chaeremon interval | Fixed ("years later"). |
| S-7 discretion | Fixed ("between too much and too little"). |
| N-1, N-2, N-3 | Fixed. The death telling now matches its absent_detail, which says the city is unnamed. |

**The five trims.** I checked each one.
- "After Martin's death": Lerins is dated c. 400-410 and Martin died in 397, so the order still holds.
- "Honoratus" without "a man named": the rest of the unit introduces him well enough.
- "Sulpitius Severus, who visited Martin there": Sulpitius was already introduced in unit 4.
- "against Egypt's monks": fine.
- "around Tours, in the Loire valley": fine.
- "Cassian and Germanus": **this one cut a real identifier** (S-C below).

**Tails.** No new empty tails appear. Every hedge added or restored in this commit qualifies one specific claim, so Mark's ruling keeps it. There is no "this world", no meta "record" and no AI tell in any changed sentence.

---

## 2. New findings

### S-A. Cassian voice: "From them" now reads as "from the wonders"
- **Severity:** SHOULD-FIX
- **Where:** `voices` Cassian, sentences 3-4
- **Quote:** "...and in his Institutes he chose not to write up the wonders he had seen. From them he passed on purity of heart as the monk's goal and discretion as his guide."
- **Evidence:**
  - "Them" should mean the Egyptian fathers.
  - The R3 rewrite made "the wonders he had seen" the nearest plural noun, so the sentence now says Cassian drew purity of heart from wonders.
  - That contradicts the sentence before it and Inst. Pref. ("no instruction in the perfect life").
- **Fix:** "From the fathers he passed on purity of heart as the monk's goal and discretion as his guide." Scored as part of the whole voice text: FK 6.29, FRE 78.8.

### S-B. Postumianus highlight: "he" is still unclear (S-5 not closed)
- **Severity:** SHOULD-FIX
- **Where:** `highlights` "a traveler just back from Egypt"
- **Quote:** "This is Postumianus, a speaker in the Dialogues. Sulpitius wrote the words of praise he says about Martin."
- **Evidence:**
  - The nearest antecedent of "he" is Sulpitius, so the sentence can be read as "the praise Sulpitius says about Martin".
  - That blurs who speaks. The speech is put in Postumianus's mouth, and the guard in `gallic.quote.postumianus-you-have-conquered-all-the-eremites` (not_for: "an independent traveller's judgment") depends on that difference.
  - "Says about" is also clumsy English.
- **Fix:** "This is Postumianus, a speaker in the Dialogues. His praise of Martin is in words Sulpitius wrote." Scored FK 5.77, FRE 68.8, which passes the floor the fixer cited.

### S-C. The "his friend" trim leaves Germanus unintroduced in the main story
- **Severity:** SHOULD-FIX
- **Where:** `orientation.story` unit 7
- **Quote:** "In Egypt, an old man named Chaeremon told Cassian and Germanus that no one masters the good by effort alone."
- **Evidence:**
  - This is the first time the main story names Germanus. The tile says "his friend" but gives no name, and no highlight covers him.
  - A reader of a Gallic story set between 360 and 450 is likely to know the bishop Germanus of Auxerre, who lived 378-448.
  - `gallic.figure.cassian` and `gallic.story.bishop-archebius` keep Germanus of Auxerre out of this material on purpose.
  - The cut removed the only words on the page that told a reader which Germanus this is. That runs against "introduce before use".
- **Fix:** Restore "Cassian and his friend Germanus". The main story goes from 697 to 699 words. Scored as the whole unit: FK 7.02, FRE 70.6.

### N-A. Honoratus voice: "the sermon" has nothing to point back to
- **Severity:** NIT
- **Where:** `voices` Honoratus `text`
- **Quote:** "...but on the island, as far as the sermon can be read, the priesthood caught up with him."
- **Evidence:** The text names Hilary ("His disciple Hilary says") but never mentions a sermon before this clause. The sermon first appears in the hedge, which comes after.
- **Fix:** "...as far as Hilary's sermon can be read..."

### N-B. Honoratus hedge: the difficulty is our copy, not Hilary's Latin
- **Severity:** NIT
- **Where:** `voices` Honoratus `hedge`, sentence 2
- **Quote:** "Its Latin is hard to read."
- **Evidence:**
  - The divergence_note puts the problem in "rough OCR of the Latin", not in the Latin itself.
  - As written, the sentence can be read as a claim about Hilary's style.
  - This was my own round 2 wording, and I am correcting it here.
- **Fix:** "The copy we have of its Latin is hard to read." Scored as the whole hedge: FK 4.75, FRE 85.0.

---

## Verdict

**APPROVED.** All four round 2 BLOCKING findings are truly fixed against the records and the vendored text, and no BLOCKING defect is new. The three SHOULD-FIX items are one-line wording fixes with the exact text given above. None needs a new judgement, so they can be applied without another review round. A quick grep that the strings landed is enough to confirm them.

**Counts:** BLOCKING 0 · SHOULD-FIX 3 · NIT 2
