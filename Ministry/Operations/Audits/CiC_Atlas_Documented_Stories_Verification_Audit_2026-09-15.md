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

**Re-tested later the same day, and half wrong — see §9.** The *Dialogues*
were acquired and read, closing all eleven; 26 remain. The sentence above is
right that the block is the corpus and wrong about why: the texts are not
unreachable, only un-fetched.

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

---

## 9. Addendum, same day: the corpus was not the constraint it was taken for

§5 closed by saying the verification pass was blocked on the corpus. Mark
asked for that to be re-tested rather than accepted. Two of the three things
that sentence rested on turned out to be false.

**The texts are not sitting unread in the library.** §5's verdicts were
reached by searching each quotation against its own entry's `corpus-map`
bucket, so `ABSENT` only ever meant "not in that bucket". Since the full ANF
(1–10) and NPNF (both series, 1–14) sets are vendored, and the median bucket
holds 3 files against a library of 117, a mapping gap looked likely. All 60
absent quotations were re-run against the entire 250 MB library. **Nothing was
recovered.** Six returned as exact matches and all six are coincidences of
short generic phrasing — 'sick at heart' in Gregory of *Nyssa* against a story
citing Gregory of *Tours*; 'greatly troubled' in Budge's *Paradise of the
Fathers* against a story citing Gregory's *Dialogues*; 'a hundred thousand',
'the great grace', 'I am a Christian', 'fellow-Lucianists' likewise. This is
§8's finding a third time: a machine locates a string, a reader locates a
passage.

**The sandbox does not block the archives.** `CORPUS-USE.md` states that it
"blocks every patristic text host (ccel.org, archive.org, wikisource,
gutenberg, newadvent, tertullian.org), so nothing here was ever fetched by a
build thread." The dedicated patristic hosts are blocked — tertullian.org,
newadvent, sacred-texts and documentacatholicaomnia all refuse to connect.
The general archives are not: archive.org served 588 KB end to end. The
project already knew. `world-build-docs/ijc/BUILD-LOG.md` §12 records that on
**2026-09-13** a build thread fetched, re-verified and vendored Paulinus of
Milan's *Vita Ambrosii* and Ammianus Marcellinus from the Internet Archive,
noting it was reachable "even where ccel.org/newadvent.org/tertullian.org are
not." Both files are on disk. Three live files still assert otherwise, one of
them the generator that keeps reprinting it: `gen_corpus_table.py:172`,
`cic/engine/texts_registry.py:6` and `:390`. CLAUDE.md carries the same claim.
Flagged, not corrected here — that is another thread's content.

### The eleven Gregory quotations, read

Gardner's 1911 re-edition of the 1608 English was vendored
(`gregory-great_dialogues_gardner1911.txt`) and Book II chapters 3 and 33–34
read line by line, the method that produced four corrections in Possidius.
Here it produced none.

| in the story | in the source | |
|---|---|---|
| 'his way of life would not suit theirs' | "their manners were divers from his, and therefore that they should never agree together" | sound |
| 'they saw that under him they could no longer do what was unlawful' | "when they saw that under him they could not live in unlawful sort" | sound |
| 'as if a stone had struck it' | "as though the sign of the cross had been a stone thrown against it" | sound |
| 'God forgive you, brethren… Go and find an abbot to your liking' | "Almighty God have mercy upon you, and forgive you… seek ye out some other father suitable to your own conditions" | sound |
| 'in the praises of God and in holy conversation' | "they spent the whole day in the praises of God and spiritual talk" | sound |
| 'of the joys of the heavenly life' | "discoursing of the joys of heaven" | sound |
| 'What are you saying, sister? I cannot possibly stay outside my cell.' | indirect in this edition — see below | **flagged** |
| 'greatly troubled' | "began to be heavy and to complain of his sister" | sound |
| 'God forgive you, sister. What have you done?' | "God forgive you, what have you done?" | sound |
| 'I asked you and you would not listen; I asked my Lord and he listened.' | "I desired you to stay, and you would not hear me, I have desired our good Lord, and he hath vouchsafed to grant my petition" | sound |
| 'She could do more, because she loved more.' | "of right she did more which loved more" | sound |

**The one flag, and why it is not a correction.** Benedict's refusal is direct
speech on the card and indirect report in this edition: *"saying that he might
not by any means tarry all night out of his Abbey."* That is the exact shape
of §4's second Possidius correction. The 1608 keeps direct speech elsewhere in
this same chapter — both of Scholastica's replies and Benedict's own complaint
— which weakly suggests the Latin is indirect here too. Weakly is not enough.
This is a freely-restructured Jacobean translation, not the cited edition, and
§4's own rule holds: a quotation is not corrected against a source that is not
the cited one. Gregory's Latin is not vendored and was not reachable from any
host this sandbox can see. The flag stands open.

### Where this leaves it

Eleven of the 37 are closed. **Twenty-six remain**, and their character has
changed: they are no longer unreachable, only un-fetched. §5's conclusion was
right about the corpus and wrong about why — the gap is acquisition, and
acquisition is now possible.

### A defect found on the way, not fixed here

`cic/engine/corpus_map_merge.py` regenerates every bucket in
`cic/corpus-map/` from `_staging/`, and the generated files' own headers tell
you to run it. Running it silently reverts work that exists only in the
generated files: `gallic-monastic-ascetic-christianity.yaml` loses two works
vendored on 2026-09-13 (Cassian's Latin *Institutes* including Book VI, and
Eucherius of Lyon), and `alexandria-catechetical.yaml` loses the 2026-09-09
OG-6 correction that removed the unattested claim that Peter of Alexandria
headed the catechetical school. Drift runs the other way too — the merge emits
a `tertullian-s-voice.yaml` bucket that is not in the repository at all. The
merge was run here for the one new staging file; every collateral change was
restored to HEAD and only the two intended buckets kept. **The generator is
not currently safe to run**, and the next thread that follows those headers
will destroy source-fidelity corrections without being told.
