# Atlas Documented Stories — Verification Audit, 2026-09-15

Requested by Mark, in session: survey the documented stories, then "do the 76
checkable quotations," then "do the rest of the possidius-style reads."

**Scope.** The `documentedStories` field in `cic-website/atlas-v3.html`: 545
stories across 278 of 292 entries, all ten eras, 132,366 words of published
text. The field exists only in that file — `world-census.json` carries none of
it. This audit covers fidelity and register in those stories. It does not
touch the cards' own prose, which the Voice & Style Guide governs and which a
separate pass has already been through.

**Nothing below was investigated by guessing.** Every figure was measured over
the whole corpus, and every verdict on a quotation names the passage that was
read to reach it. Where the method failed, §8 says so.

---

## 1. What the corpus says about itself

| `verification` | stories | share |
|---|---|---|
| from reference summaries; primary text not yet read | 490 | 89.9% |
| checked directly against the primary text | 44 | 8.1% |
| adapted from this project's own reviewed Doc_09 Story Inventory | 11 | 2.0% |

Tier: 441 tier 1, 91 tier 2, 13 tier 3. Sources: 2–4 per story, median 4;
1,111 primary and 817 reference citations; **no story lacks a primary
citation**.

`tier` and `verification` are internal — neither renders to a visitor.
`verification` was removed from the rendered story meta line on 2026-09-15,
under Mark's ruling to strip the system explaining its own system from the
cards. That was right for build status, and `caveat` — which carries the
source-level hedging a reader needs — still renders. It does mean nothing on
the card now distinguishes a story checked against the primary text from one
that was not.

## 2. Quotation exposure

227 stories (42%) contain a quotation. **177 unverified stories carry 369
quoted spans** in teaser and text, 386 including caveats; the longest runs to
75 words. The corpus quotes with curly single quotes exclusively and contains
no double quotation marks at all.

Of the 981 primary-source notes attached to unverified stories, **19%** say
anything about route or translation. The rest cite a primary text plainly.

## 3. What was actually checked

The 76 quotations sitting in unverified stories whose entry has a bucket in
`cic/corpus-map/` were searched against that entry's whole vendored corpus,
then each flag was traced to the passage it cites.

| | quotations |
|---|---|
| corrected (Possidius, read line by line) | 3, plus one unattested detail removed |
| confirmed sound (Chrysostom) | 1 |
| exact but generic — terms, not passages | 6 |
| unverifiable: the cited passage is not on disk | 37 |
| cite an author with nothing by them in the bucket at all | 29 of the 76 |

## 4. The corrections made

`latin-pastoral-congregational-christianity`, "The Psalms on the Wall of
Augustine's Room", against `cic/texts/possidius_vita-augustini_weiskotten1919.txt`,
which carries the Latin, Weiskotten's English and his notes. Commit `283c9392`.

| in the story | in the source | action |
|---|---|---|
| 'trees and stones fall' | "wood and stones should fall"; Latin *ligna et lapides* | restored verbatim |
| Augustine "quoted to his companions a saying he had made his own" | he "was consoled by the thought of a certain wise man who said" | reframed |
| 'he had nothing to leave' | "nothing from which to make it"; Latin *unde faceret* | restored verbatim |
| "copied out in large letters" | in neither the Latin nor the English | removed |

Three further items in the same story looked wrong and were not, and are left
alone: 'Psalms of David that deal with repentance' renders *Psalmos Davidicos,
qui sunt paucissimi de poenitentia*; "the four penitential psalms" comes from
Weiskotten's own note that the shortest of the seven are four; "fixed to the
wall opposite his bed" renders *iacens in lecto contra parietem positos*.

The second row is the one that matters most: an indirect report turned into a
direct-speech scene.

**Confirmed sound.** `antiochene-exegetical-christianity-chrysostom-ce`,
'do not make me a widow a second time' — verbatim in the vendored *De
Sacerdotio*, which itself introduces the speech with "she said in substance",
so the surrounding paraphrase is inherited from the translation.

**Flagged, not changed.** `aquileian-christianity`, Jerome's scorpion. The
story has 'lies buried'; the only rendering on disk says "now lies
underground" — but that rendering is a secondary work quoting Jerome, not the
preface the story cites. A quotation is not corrected against a source that is
not the cited one.

## 5. The blocking finding

**Of 545 stories, one had its cited source vendored completely enough to
audit.** Auditing it produced four corrections.

The 37 unverifiable quotations are not near-misses. Gregory the Great's
*Dialogues* Book II, cited by eleven of them, is absent — the entry's 1.8
million vendored words contain no "Scholastica", no "Vicovaro", no "Subiaco".
Pelagius' *Letter to Demetrias* appears only as a line in Schaff's
bibliography. Not vendored at all: Koriwn's *Life of Mashtots*, Moses of
Khoren, Romanos the Melodist's kontakia, Theodore Abu Qurrah, Venantius'
*Life of Radegund*, Gregory of Tours' *History of the Franks*, Auxentius'
letter on Ulfila. Gregory of Nazianzus on Sasima survives in that entry's
corpus only as editors' footnotes about him.

The verification pass is blocked on the corpus, not on effort or judgement.

## 6. A structural gap worth fixing on its own

`WANTS-REGISTER.md` is generated from `records/`: it finds a `source` record
whose `edition` names no vendored file, which is exactly the condition
described above. The atlas stories' 1,111 primary citations live in
`atlas-v3.html`, not in `records/`, so **the generator cannot see any of
them.** The fleet's own instrument for "sources we depend on and cannot read"
is blind to the largest single block of citations in the project.

## 7. What was deliberately not done

- **No rows added to `download-queue-seed.yaml`.** Its own header requires a
  candidate "actually verified against a real host, not when it merely seems
  likely." None of the 37 has been checked against a host, and adding them
  would break the rule the file exists to keep.
- **No `ACCEPTED_OPEN` waiver.** That mechanism lives in
  `engine/m1/cross_world.py` and covers registry/census wiring consistency,
  not prose or source findings. Filing there would misuse it.
- **No rewrite of the register defects.** 545 of 545 stories are a single
  paragraph; text runs 201–265 words with an interquartile range of 8, and
  99% sit within a tenth of the median 245. Median sentence 29 words against
  18 on the card around them, longest 133. Real, and second in priority:
  which stories survive verification should decide what gets rewritten.

## 8. Method limits, stated because they changed the answer

Mechanical matching could not settle any of this. The harness
(`verify_quotes.py`, session scratch) was wrong four times before it was
right, each time in the direction of over-reporting absence:

1. Quoted spans counted as zero — the corpus uses curly single quotes and the
   search looked for double quotes.
2. The rarest-word anchor was chosen from a list that included words absent
   from the corpus, so one unknown word scored a whole quote 0.00 unexamined.
3. The anchor's positions were capped at the first 400, hiding matches later
   in a 43-million-word corpus.
4. A single anchor word is the wrong choice against a paraphrase, because the
   rarest word is usually the one that was substituted and so is absent from
   the very window being sought.

Two triage tests were also too loose: an author-level match passed all eleven
Gregory the Great quotations on the *Register of Epistles* when the *Dialogues*
were meant, and an any-of probe reported the *Life of Radegund* present when it
had matched only "venantius".

The conclusion those failures point to is the finding itself: **a machine can
locate a candidate passage; only reading the cited passage can say which way
it falls.** Whatever this becomes, it is a scholar's pass, not a script.
