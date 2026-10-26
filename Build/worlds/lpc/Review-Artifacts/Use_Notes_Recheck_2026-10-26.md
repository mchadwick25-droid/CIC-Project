# VERDICT: REVISE

**lpc use notes: round 2, a targeted recheck, 2026-10-26.**

- **Scope:** `git diff ea2c8540 HEAD`, with HEAD at `a6c537c5`. It covers the stage, records/lpc, `Lexicon_Deployment_Index.md` and Lexicon-Chunks.
- **Method:** only what changed was checked, against the round-1 findings in `Use_Notes_Review_2026-10-26.md`.
- **Reviewer:** Opus 5.5. No model API was called.
- **Result:** 22 of the 23 round-1 findings are fixed, and UN-22 is with the project lead. Cutting `means` to 25 words or fewer introduced 4 new P1s and 14 new P2s. Each one is a scoping word, a qualifier or the subject of a clause that fell out.

## How it was checked

- **Old against new.** The round-1 stage was loaded from `ea2c8540` and the current stage from HEAD. All 117 notes were compared field by field: the 106 changed `means`, every changed not_for line, and the 11 changed `years`. Each changed `means` was read against its record's `text`, `statement` or `plain_meaning`, plus its `modern_lens_note`, `divergence_note` and guards.
- **UN-01 at both source lines.**
  - `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml:30204` reads "thousands of certificates were daily given, contrary to the law of the Gospel".
  - `cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt:3010` reads *darentur cotidie libellorum milia contra euangelii*.
  - The term record's `divergence_note`, the `wb_lpc_s22.py` source, `Lexicon_Deployment_Index.md` and the chunk now all agree with both lines. The index and chunk say "Epistle XIV" (ANF numbering) and the record says "Epistle XX.2" (Hartel). These are the same letter.
- **Gates.** `use-note-present` and `use-note-shape` are clean.
- **Stage.** Re-applying it changes 0 of 117 files. Every note is `status: provisional`.
- **Readability.** `grade_text` over every `means` gives 0 failures. The longest is 25 words, and the whole set scores FK 8.4 and FRE 67.4.
- **Build vocabulary.** A scan of `means` and not_for for this build's own terms ("this build", "synthesis", "rated", "cross-check", "Construction Framework", "this world", "Registry", "Morin") finds no hits.

## Round-1 findings

| ID | Status | Note |
|---|---|---|
| UN-01 | Fixed | The not_for line, the record's `divergence_note`, the index and the chunk are all corrected and verified at both source lines (above). |
| UN-02 | Fixed (see R2-18) | The outcome claim is gone, and the Carthage–Rome guard is added. The new wording "kept him in" is vague. |
| UN-03 | Fixed | Now "classified in his phase only", with the added guard "a claim that Augustine's church had no penitential discipline". |
| UN-04 | Fixed on Cyprian's side (see R2-06) | Cyprian's side is now scoped to "call a custom apostolic", and the Stephen guard is added. Augustine's side lost "everywhere". |
| UN-05 | Fixed | Years are now 246 to 258. |
| UN-06 | Fixed | "ordinary" is restored, and the Optatus guard is added. |
| UN-07 | Fixed | Both the quote and the term now read "name Stephen as their target". |
| UN-08 | Fixed | Years are now 400 to 426. |
| UN-09 | Fixed | Years are now 397 to 401, and the means names the Confessions. |
| UN-10 | Fixed | Years are now 395 to 430 for `stewards`, `ye-belong` and also `good-works` ("dangers of his office"). The change is sound. |
| UN-11 | Fixed | Years are now 248 to 251. |
| UN-12 | Fixed | The scan finds no build vocabulary. The cross-check line is removed, and the "our own reading" phrasing is sound. |
| UN-13 | Fixed (see R2-07) | Both guards are added. The means lost its own scoping phrase. |
| UN-14 | Fixed | The variant guard is added. |
| UN-15 | Fixed | "joins the presbyters" appears in both notes, and the *inuictus* guard is added. |
| UN-16 | Fixed | The date now stands apart from the two texts. |
| UN-17 | Fixed | The guard on inquisitorial ancestry is added. |
| UN-18 | Fixed | "is real" replaces "valid". |
| UN-19 | Fixed | `grace` reads "In Augustine's teaching", `the-one-episcopate` reads "Cyprian taught", and `communion` reads "For Cyprian". |
| UN-20 | Fixed | Years are now 251 to 256. |
| UN-21 | Fixed, at a cost | 0 of 117 fail. The cuts caused R2-01 to R2-17. |
| UN-22 | With the project lead | Logged in OG-80. |
| UN-23 | Fixed | All 117 notes are `provisional`. |

## New findings

| ID | Sev | Record | Field | Finding | Evidence | Fix |
|---|---|---|---|---|---|---|
| R2-01 | P1 | `lpc.witness.the-only-son-and-the-trinity` | means | "Augustine held that Jesus is God's only Son, and Arians disputed it" is false. Homoian ("Arian") bishops called Jesus God's only-begotten Son. Maximinus disputed the confession of the Trinity: the Son's full equality, with the Holy Spirit completing the one Godhead. The cut dropped the Trinity and kept the one clause the other side affirmed. | Record `text`: "That completes the Trinity that makes up the one Godhead ... This confession did not go unchallenged." | "Augustine confessed Jesus as God's only Son within one Trinity, and the Arian bishop Maximinus disputed that confession at Hippo." (21 words) |
| R2-02 | P1 | `lpc.contested.de-unitate-recensions` | means | "Whether chapters 4 and 5 of De Unitate were added later" misstates the contest. No one argues that the chapters were added. The question is whether one *form* of them, the Primacy Text, is a later interpolation or Cyprian's own revision. Both sides agree that Cyprian wrote chapters 4 and 5 in some form. | Record `claim` and `held_against[1]`. | "Whether the 'Primacy Text' of De Unitate 4 to 5 is a later hand's insertion or Cyprian's own revision stays open." |
| R2-03 | P1 | `lpc.gravity.collegial-communion-preserved` | means | "Bishops here argued hard but kept communion" brings back the outcome claim that UN-02 removed. The record says bishops *work to* keep communion, and its own guard rules out "bishops never broke communion". The new UN-02 guard (Carthage and Rome in 256) contradicts this means. | Record `description`: "they work to keep communion rather than break it". | "Bishops here argued hard but worked to keep communion, not break it, from Cyprian to Augustine." |
| R2-04 | P1 | `lpc.quote.pardon-through-a-wicked-clergyman` | means | "A bad cleric can still give forgiveness" moves the agency to the minister, which is the reverse of Augustine's point. In the record, the one who comes sincerely to the congregation that has received the Spirit receives forgiveness *in the Holy Spirit*, even through a bad Catholic cleric. Read as the cleric's own power, this states the Donatist-shaped view Augustine argues against. The cut also dropped "coming to the Church", which the record's guard ties to the sin-against-the-Spirit frame. | Record `text`, `modern_lens_note`, `claim_guards[3]`. | "Augustine says whoever comes sincerely to the Church is forgiven in the Holy Spirit, even through a bad Catholic cleric." (19 words) |
| R2-05 | P2 | `lpc.quote.the-creed-first-then-the-prayer` | means | "learned the Creed first" puts back the word that the record's own `divergence_note` and lens note replace with "received" (*accepistis*). The cut also dropped the second purpose, "to know whom to call on". | Record `divergence_note`, `modern_lens_note`. | "...they received the Creed first, to know what to believe, then the Lord's Prayer, to know whom to call on." |
| R2-06 | P2 | `lpc.witness.tradition-tested-by-apostolic-warrant` | means | "but Augustine would if the Church kept it" dropped "everywhere", so it claims Augustine accepted any church custom as apostolic. Universality is his test. | Record `text`: "A custom kept everywhere in the Church may fairly be presumed apostolic". | "...but Augustine would if the whole Church kept it everywhere." |
| R2-07 | P2 | `lpc.witness.days-before-the-sun` | means | The means now gives only the 6,000-year figure, without "by Scripture's reckoning". It also drops the admission that how those days worked is beyond our senses, which is the record's main point. The new guards cover the modern debate, but the gist leads with the number. | Record `text` and `tensions`. | "Augustine said the days before the sun are beyond our senses, and by Scripture's reckoning under 6,000 years had passed." |
| R2-08 | P2 | `lpc.term.heresy` | means | "Augustine later said yes" flattens his answer. The record says the baptism was "truly given, and does no good where the person stands". "Counts" with a plain yes reads as full acceptance. | Record `senses.informational`. | "...Cyprian's council said no, and Augustine said it was truly given but did no good outside." |
| R2-09 | P2 | `lpc.limit.womens-own-voice` | means | "no woman's own writing survives" dropped the record's scope, "from us". Taken generally it is false: Perpetua's own prison account (Carthage, 203) survives. | Record `statement`: "No text a woman wrote herself survives from us". | "...and no writing by a woman of our own survives." |
| R2-10 | P2 | `lpc.quote.ye-belong-to-my-care` | means | The cut dropped the account the bishop must give, which is the point of the passage and of its `modern_lens_note`. It also dropped "when not heard". | Record `modern_lens_note`. | "Augustine says his hearers are in his care so he can give account for them, and that he wept when not heard." |
| R2-11 | P2 | `lpc.term.libelli` | means | "though some bought one" lost "without sacrificing", so the clause no longer says what made the paper a problem. | Record `plain_meaning`. | "A libellus was a paper saying you had sacrificed, which some bought without sacrificing, and Cyprian counted them lapsed." |
| R2-12 | P2 | `lpc.witness.confessor-claim-vs-regulated-peace` | means | "the church's rules answered, but never joined the two" is ungrammatical. The rules are the subject of "never joined", so they would be joining themselves. The clause has lost its sense. | Record `text`: "We have never found the place where these become one settled rule". | "Confessors claimed they could ask peace for the lapsed, the church's process answered them, and the two never became one rule." |
| R2-13 | P2 | `lpc.quote.clamour-and-tears` | means | "begged the bishop" turns "demanded it with great zeal and clamor" into pleading, which loses the seizure the lens note stresses. | Record `text`, `modern_lens_note`. | "...grabbed Augustine and loudly demanded that the bishop ordain him as he wept." |
| R2-14 | P2 | `lpc.witness.scripture-above-councils`, `lpc.quote.earlier-councils-corrected-by-later` | means | "Augustine put Scripture first" and "Scripture stands above all" drop what Scripture stands above: bishops' letters and councils. The not_for guards (not the only authority; councils bound) still hold, so this is P2. "Old error" also flattens "the old age of error". | Record `text`. | "...and Augustine set Scripture above every bishop's letter and council." |
| R2-15 | P2 | `lpc.limit.ordinary-interior-life` | means | "apart from Augustine's tears" lost "at his baptism" and "written years later". The record uses those two points to explain why the exception is not ordinary. "seldom" also weakens "almost never", and "plain folk" is a register slip. | Record `statement`. | "The record shows what bishops decided, but almost never what ordinary believers felt, save Augustine's later memory of weeping at baptism." |
| R2-16 | P2 | `lpc.limit.411-gesta-unread` | means | "has not read its transcript" dropped "validly". The record's claim is about valid reading, not about whether the transcript was opened. | Record `statement`: "has not been validly read". | Restore "validly". |
| R2-17 | P2 | `lpc.witness.answerability-as-ground` | means | "peaceful disagreement" misdescribes the record. Its disagreements are "sharp", and the point is that they happen without separation. | Record `text`. | "...the root of the road back, the font, and disagreement without a break." |
| R2-18 | P2 | `lpc.witness.communion-over-separation` | means | On UN-02's new wording, "Augustine later opposed his ruling but kept him in": the substance is right, since Augustine argued the ruling wrong and never put Cyprian outside communion. But "kept him in" is vague and can be heard as kept in office or in favour. "his ruling" also makes the council's ruling Cyprian's alone. | Record `text`: "He never once put the man who made it outside our communion." | "...and Augustine later argued the council's ruling wrong but never put Cyprian outside communion." (Check that it still fits in 25 words.) |

**Cuts the coordinator asked about.**
- **Constantine witness:** cleared. Dropping the Petilian clause lost no scoping word. Augustine's partiality is still guarded in not_for ("a claim that Augustine was a neutral witness, since Petilian's side..."), and "his power did not come from the old gods" is faithful to City of God V.25.
- **`scripture-above-councils`:** see R2-14.
- **`ordinary-interior-life`:** see R2-15.

**Other cuts checked and cleared:** `the-trees-and-the-trembling-executioner`, `thousands-of-certificates-daily`, `penitential-discipline`, `the-silent-century`, `the-one-episcopate`, `grant-me-chastity-but-not-yet`, `restless-heart-and-the-unrepentant-enemy`, `apostolic-origin-undefended`, `conciliar-authority-theory`, `sacramental-ordination-validity`, `grace` and `numidicus`.

## Pattern

Every new finding comes from one thing: cutting to 25 words removed a qualifier ("everywhere", "validly", "from us", "worked to", "by Scripture's reckoning", "at his baptism") or the subject of a clause ("in the Holy Spirit", the Trinity). Round 1's P1s came from compression too. The fix is to keep each `means` to one idea and cut extra clauses, never qualifiers. Every fix proposed above stays within 25 words and one sentence. The reviser should re-score each one with `grade_text`.

## Verdict

**Revise.** R2-01 to R2-04 are P1 and must be fixed. The P2s are small wording changes and should go in the same edit. The notes stay `provisional`.

This is the second review file on these notes. Under the review cap (CLAUDE.md, "Scaling the build"), a third round is the last before escalation. That round should be a narrow check of these 18 rows, the four P1s first, and nothing else.

---

## Round 3: a narrow recheck, 2026-10-26

- **Scope:** `git diff HEAD~1` at `ccc9bc1e`. That is 18 `means` lines in the stage and the 19 records they write. No not_for line or `years` changed.
- **Checks:**
  - Each new line was read against its round-2 row and its record.
  - `use-note-present` and `use-note-shape` pass.
  - Re-applying the stage changes 0 of 117 files.
  - `grade_text` finds 0 failures, and the longest `means` is 25 words.

| ID | Sev | Status | Check |
|---|---|---|---|
| R2-01 | P1 | Fixed | "God's only Son within one God in three ... an Arian bishop at Hippo fought that belief". The contested object is now the Trinitarian confession, which matches the record. |
| R2-02 | P1 | Fixed | "One form of two chapters ... a later hand's insertion or Cyprian's own rewrite". This names the real question. Dropping the label "Primacy Text" loses no scope. |
| R2-03 | P1 | Fixed | "worked to keep communion, not break it". This is the record's own scope. |
| R2-04 | P1 | Fixed | "one who comes to the Church in good faith is forgiven in the Spirit, even through a bad priest". The agency is back in the Spirit and the Church. "Catholic" can go, because the record's `divergence_note` reads it as a concession, not a condition. "Priest" is narrower than *clericus*; see the note below the table. |
| R2-05 | P2 | Fixed | "got" stands for *accepistis*, and "to know whom to ask" is restored. |
| R2-06 | P2 | Fixed | "the whole Church kept it in all lands" keeps universality. |
| R2-07 | P2 | Fixed | "past our senses" and "by Scripture's count" are restored. |
| R2-08 | P2 | Fixed | "truly given but did no good there". |
| R2-09 | P2 | Fixed | "a woman of our own". |
| R2-10 | P2 | Fixed | The account and "when not heard" are restored. |
| R2-11 | P2 | Fixed | "some bought one without making it". |
| R2-12 | P2 | Fixed | The sentence is grammatical, and "never became one rule" matches the record. |
| R2-13 | P2 | Fixed | "loudly told their bishop to make him a priest". This is right for Augustine's ordination as a presbyter in 391. |
| R2-14 | P2 | Fixed | "above all bishops and their meetings" and "above them all" (the councils) now name what Scripture stands above. |
| R2-15 | P2 | Fixed | "almost never" is back, as are "at his baptism" and "told long after". |
| R2-16 | P2 | Fixed | "has not been properly read" carries the sense of "validly". |
| R2-17 | P2 | Fixed | "disagreement without a break". |
| R2-18 | P2 | Fixed | "Cyprian's council said it would cast out no one ... never cast Cyprian out". The ruling is the council's, and the claim is scoped to what was said and done. |

**New issues:** none at P1 or P2.

One cosmetic note, not counted. In R2-04, "priest" is narrower than the record's "cleric". It does not change the meaning, and the reviser may keep it.

### Verdict, round 3

**Approved to proceed.** Every round-1 and round-2 finding is closed, except UN-22, which is the project lead's engine decision (OG-80). The notes may now be switched from `provisional` to `reviewed`.
