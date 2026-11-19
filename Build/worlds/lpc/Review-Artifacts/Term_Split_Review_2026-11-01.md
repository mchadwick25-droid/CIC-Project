# LPC Term Split Review: heard_today / meant_here

- **Reviewer:** independent reviewer (Claude Opus 5.5). Did not draft the split. Read-only on records.
- **Date:** 2026-11-01
- **Scope:** the 19 `records/lpc/term/*.md` records on branch `claude/lpc-term-split` (uncommitted working tree). Each gained `senses.heard_today` and `senses.meant_here`, split from `senses.translational`, which stays.
- **Rule under review:** wording kept; only what each half needs to stand alone may change; no new claims; nothing dropped or weakened; nothing added.
- **Checks:** (1) word-by-word diff of each half against `translational`, with each change judged needed or not; (2) each half stands alone on a card under the term, with no pointer to the other half; (3) neither half says more than the record's sources support, carries a word whose modern sense misleads, or runs a sentence past about 25 words. A long sentence inherited unchanged from `translational` is an advisory, not a FAIL.

**Result: 17 PASS, 2 FAIL** (`lpc.term.preaching` P1, `lpc.term.confessor` P2).

| Term | Changes vs translational | Stands alone | Supported | Verdict |
|---|---|---|---|---|
| bishop-of-bishops | "We mean neither --" became "We mean". Needed: "neither" points at heard_today. | Yes | Yes. Advisory: meant_here 35 words, inherited. | PASS |
| catechesis | None. A clean split at the sentence boundary. | Yes. "Catechesis itself" leans on the contrast a little, but reads alone. | Yes. Advisory: Augustine sentence 27 words, inherited. | PASS |
| certificates-letters-of-peace | "the opposite document" became "the opposite of the sacrifice-certificate". Needed: names the referent, so the half no longer points back. | Yes. meant_here explains the sacrifice-certificate itself. heard_today's "who has just heard about the sacrifice-certificate" assumes reading order (inherited). | Yes. Advisory: heard_today 34 and meant_here 35 words, inherited plus the needed addition. | PASS |
| communion | None. | Yes. "the second" is internal to heard_today. | Yes. Advisory: 35 and 30 words, inherited. | PASS |
| compel-them-to-come-in | "the author's own earlier opinion" became "Augustine's own earlier opinion". Needed: "the author" has no referent on a card. Supported: `use_note.means`, `plain_meaning`, Letter 93 locus. | Yes | Yes. Advisory: heard_today 33 words, inherited. | PASS |
| confessor | "We mean the opposite direction entirely:" became "We mean the opposite:". "direction entirely" dropped. Not needed: the colon clause already resolves "opposite" inside the half. The drop weakens it. | Yes, just about. The bare "the opposite" reads as pointing at heard_today. | Yes. Advisory: 29 and 31 words, inherited. | **FAIL (P2)** |
| grace | None. | Yes | Yes. Advisory: 39 and 47 words, inherited. These are the longest in the set and worth a later readability pass. | PASS |
| heresy | None. | Yes | Yes. Advisory: 32 and 28 words, inherited. | PASS |
| libellatici-sacrificati | None. | Yes | Yes. Advisory: 33 words, inherited. | PASS |
| libelli | None. | Yes | Yes | PASS |
| plenary-council | heard_today: "the same sentence" became "Augustine's own sentence". Needed: "the same sentence" had no antecedent on a card. Supported: On Baptism II.3 locus. | Yes. Advisory: "Augustine's own sentence" still assumes the reader has seen the quote. meant_here's "one man" is unnamed (inherited). | Yes. Advisory: 35 and 33 words, inherited. | PASS |
| preaching | "For us it was" became "For us preaching was". Needed: "it" had no referent. | Yes | **No.** "the central formative act of ordinary life" is not supported (see details). "occasional" misleads in its modern sense. | **FAIL (P1)** |
| reconciliation-penitential-discipline | "Neither is private and neither is primarily about feeling for us." became "It is not private, and for us it is not primarily about feeling." Needed: "neither" points at heard_today. Same claim, same strength. | Yes | Yes. Advisory: 27 words each, inherited. | PASS |
| schism | None. | Yes | Yes | PASS |
| suffrage | "We mean neither. A corporate acclamation" became "We mean a corporate acclamation". Needed: removes the pointer and repairs a sentence fragment. | Yes | Yes. Advisory: 31 words, inherited. | PASS |
| the-flock | "We do not mean either." dropped. Needed: a pure pointer. The negations that remain ("not passive", "not remote") are full statements. | Yes | Yes. Advisory: heard_today 36 words, inherited. | PASS |
| the-lapsed | "We mean something else entirely:" became "We mean". Needed: a pure contrast pointer with no content of its own. | Yes. heard_today's fragment "Gentle, gradual, private." is inherited. | Yes. Advisory: 26 words, inherited. | PASS |
| the-one-episcopate | "We mean neither:" became "We mean". Needed. | Yes. "the same conviction" is internal to meant_here. | Yes. Advisory: 31 words, inherited. | PASS |
| the-people | "Neither is right. A corporate body" became "We mean a corporate body". Needed: removes the pointer and repairs a fragment. The added "We mean" matches the other records and adds no claim. | Yes | Yes. Advisory: 32 words, inherited. | PASS |

## FAIL details

### lpc.term.preaching: FAIL (P1)

**Unsupported claim kept.** meant_here keeps "the central formative act of ordinary life" from `translational`. The 2026-11-01 Term Meanings and Spans review (finding on lpc.term.preaching) found the near-identical claim, "the main way its teaching reached plain believers", unsupported. It comes from the build's own Doc_05 analysis, not from any cited source. That review removed it from `use_note.means` and `quick_meaning`.

"Central formative act of ordinary life" is the same claim, and if anything a stronger one. It ranks preaching above every other formative act and reaches into "ordinary life", not just the assembly. Neither cited sermon (Sermon I.1; Sermon LXXXII §1) says this. The claim also sits badly with the record's own divergence note and `use_note.not_for` ("a claim that it was an organizing force of its own"). Under that note, preaching is the medium, not an independently organizing force.

Keeping it now also does something new. It gives the unsupported claim its own stand-alone card line, under the heading of what "we mean". The wording should not stay.

**Misleading modern sense.** "occasional" here means "tied to the occasion". A modern reader hears "infrequent". That contradicts the record's own "again and again" and "regular talk".

**Length.** The sentence runs to 38 words.

**Corrected meant_here** (the replacement for the unsupported clause is the record's own reviewed `use_note.means`):

> For us preaching was the bishop's regular talk to the whole gathered church, baptized and still learning alike. It came from the person personally answerable for the hearers. It was tied to the occasion and responsive rather than scripted, and openly aware of what it competed with for people's own attention.

**Consequential note, not part of this split.** `false_friend` ("rather than the central formative act") and the Lexicon-Chunk `lpclex008_preaching.md` (line 49, and line 25's "main way") carry the same unsupported claim. `translational` keeps it too. These should be fixed in the same pass, so that the card and its source fields agree.

### lpc.term.confessor: FAIL (P2)

**Unneeded drop.** "the opposite direction entirely" was cut to "the opposite". The rule allows only what a half needs to stand alone. The colon clause ("not one who hears confession, but one who made confession") already names both directions inside meant_here, so "direction entirely" never pointed at heard_today.

The cut does two things. It weakens the statement, because "entirely" goes. It also leaves the bare "We mean the opposite", which on a card reads as pointing back at the misreading in heard_today.

**Corrected meant_here** (restores the original wording, which resolves inside the half):

> We mean the opposite direction entirely: not one who hears confession, but one who made confession, under interrogation, at real risk, and survived. The word names what was done to us and what we did not say, and it carries a claim on the church's own decisions rather than an office within its ministry.

## Advisories (no FAIL)

- **Long sentences.** Sentences past about 25 words, all inherited from `translational`, appear in 16 of the 19 records. The longest are grace (39 and 47 words), the-flock heard_today (36), and the 35-word sentences in bishop-of-bishops, certificates, communion and plenary-council. They should go in a later readability pass, not this split.
- **plenary-council heard_today.** "Augustine's own sentence" assumes the reader has seen the quote. A card that shows heard_today without it could say "miss that Augustine, in the same sentence, makes that authority revisable". This is optional.
