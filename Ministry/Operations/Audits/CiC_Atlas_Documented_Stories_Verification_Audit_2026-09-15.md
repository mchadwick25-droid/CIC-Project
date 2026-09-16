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

**The middle one was wrong to leave, and §10 corrects it.** That the number
comes from Weiskotten's note is the reason to remove it, not to keep it: a 1919
editor's inference is not what Possidius wrote, and the story's own caveat
already said the psalms are unspecified. The scorpion flagged below is also
settled in §10.

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

### A defect found on the way, and then fixed

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
restored to HEAD and only the two intended buckets kept.

**Fixed the same day, at Mark's instruction.** The root cause was an asymmetry
in the merge's own care: the prune path removes only files carrying the
generated header and *reports* hand-written ones rather than deleting them,
but the write path had no matching guard, so a generated bucket someone later
edited was rewritten without a word. Each bucket now carries a
`# content-digest:` of what the merge last wrote. A mismatch means someone
edited generated output — which side is right is a question only a human can
answer — so the merge skips that bucket, names it, and exits non-zero. A
digest rather than a field-by-field diff because staging *should* differ from
a bucket whenever staging is the newer truth; the question is never whether
they differ but which side moved.

Measured before changing anything, across all 56 buckets: two works lost
(gallic), three notes lost (the OG-6 corrections), one bucket unwritten
(`tertullian-s-voice`, a valid Atlas id). All of it recovered into `_staging/`
verbatim — copied from the buckets by script rather than retyped, down to a
doubled apostrophe left as it stands, because a fix that rewords the content
it is rescuing is not a fix. Drift is now zero in all three categories, and a
full merge is idempotent: of 56 buckets rewritten, 54 changed by their digest
line alone and the two that changed in substance did so only by addition.

---

## 10. The remaining fifty read, and twenty-seven corrections made

§9 left 26 quotations outstanding. Read properly, the working list was 50
distinct quoted spans across 23 entries — §9's figure counted the audit's own
traced flags, not the spans. All 50 were read against the source each cites.

**Thirty-one cite a work that is not in the library.** Whole traditions are
missing: nothing Armenian, Coptic, Arabic-Christian, West Syriac, or from the
Gaza and Judean-desert monasteries. The acquisition list and its verified
Internet Archive identifiers went to the source-research thread.

**Nineteen were checkable. Six held. Thirteen carried a finding.** That is the
result that matters, and it inverts §5's assumption. Where the cited source was
absent the story could not be checked; where it was present, it usually did not
survive the check. The corpus was hiding the problem, not causing it.

### What the thirteen were

Three classes, and the second is a habit rather than an accident.

**A quotation the cited passage does not contain (5).** `pelagianism` had
B. B. Warfield's 1887 third-person summary — sitting in `npnf105`'s own front
matter — set as Pelagius's first-person speech, and a second quotation that
appears nowhere in Letter 188 in either language. `palestinian-church` turned
one of Origen's negated rhetorical questions into a positive maxim in quotation
marks. `antiochene-exegetical` attributed to *On the Priesthood* a saying that
is real Chrysostom from a different work in the same vendored volume.
`marcion-marcionism` spliced two clauses so that a claim Eusebius reports and
immediately denies became a fact he concedes. `antiochene-church-third-century`
made a circle's name for itself out of one man's greeting to another in a
single letter, in a work the story does not cite.

**A nineteenth-century editor quoted as an ancient source (3).** The Decian
date and the Pionius pairing in `marcion-marcionism` come from the NPNF editor
*correcting* Eusebius — in a story whose whole point is Eusebius's candour.
`aquileian`'s 'in sight of the burning of Rhegium' matches the editor's
paraphrase, not Rufinus's own sentence. `latin-pastoral`'s "four penitential
psalms" is Weiskotten's 1919 footnote; Possidius says *paucissimi*, and the
story's own caveat already admitted the psalms are unspecified.

**Plain error (5).** Augustine is seventy-five on the card and *septuaginta
sex* — seventy-six — in Possidius. The 28 August date is Prosper's, not
Possidius's. Pamphilus and his companions are "sentenced to be beheaded" where
the source gives no mode of execution; Porphyry acquires an age and a job the
source does not give him; Seleucus, a confessor from the army bringing news of
Porphyry's death, becomes a member of the household coming to congratulate him.
And `homoian-arian` carried an orphaned sentence — "Almost none survive." with
no antecedent — in live published prose.

### One finding deliberately not corrected

`cyrilline-miaphysite-egyptian-tradition`, the Alexandrian delegates' 'for we
shall be killed when we go home'. Only NPNF's *abridged* extracts of the Acts
of Chalcedon are vendored; the full Acts, which the story cites, are not. §4's
rule holds — a quotation is not corrected against a source that is not the
cited one. Left standing, and open.

### Closed on the way

The Jerome scorpion, flagged and left alone in §4 for want of the cited
preface, is settled: `npnf206` carries the Ezekiel preface, and Jerome wrote
that the scorpion "lies beneath the ground **with** Enceladus and Porphyrion".
The card's "between" was the `npnf203` editor's rendering. Corrected.

### Method

Five readers worked under a brief built from this project's own documented
traps, each required to quote the source passage back; a verdict without the
words was discarded. Every claim that changed published prose was then
re-checked by hand against the vendored file. Twenty-seven exact-string
replacements were applied to `cic-website/atlas-v3.html` behind a pre-flight
that aborts unless each matches exactly once. `world-census.json` carries none
of this field and did not change.

A fifth harness defect surfaced, and it belongs with the four in §8: the
quotation extractor cannot distinguish a typographic apostrophe from a closing
quote, because in this corpus they are the same character. **17 of 541 spans
(3.1%) are mis-bounded** — mostly truncated at an internal apostrophe, one
wholly bogus where a transliteration mark (`burd‘tha`) was read as an opening
quote. Like the other four, it biased toward reporting absence. It does not
touch the verdicts above, which came from reading passages rather than matching
strings.

### What this implies for the 490

Thirteen findings in nineteen readable quotations is not a rate that stops at
these entries, and three of the thirteen are the same habit. The 44 stories
that already claim `checked directly against the primary text` are now the
least safe thing in the corpus to take on trust, because that claim is exactly
what this pass has shown to be worth re-testing.

## 11. The forty-four re-tested, and the sixteen that failed

§10 closed by naming the 44 stories tagged `checked directly against the primary
text` as the least safe thing in the corpus to take on trust. They were re-read:
126 quoted spans, each one looked up in the vendored file it cites.

**Sixteen of the forty-four failed.** Three of those — Aetius, Ulfila and Moses
of the Goths, the Aksumite letter — had already been corrected inside the
readability pass as declared gate exemptions. The remaining thirteen were fixed
here, together with `roman-church-third-century`'s "Callistus, as His Enemy Told
It", which had passed as a qualified yes while carrying four real defects. **34
corrections across 15 stories.**

Every claim was verified by hand in the vendored file before it changed
published prose. The readers' reports located the problems; they did not decide
them.

### The traps, and how often each one fired

The four documented traps from §8 account for nearly all of it, which is the
useful finding. This is not thirteen unrelated slips.

| Trap | Count | Instance |
|---|---|---|
| A Victorian editor's footnote quoted as the ancient author | 3 | Callistus and the "treadmill" — ANF's gloss sits inline beside `Pistrinum`; the Epiphanius number reaching Hippolytus through a 19th-c. annotator |
| Two hostile witnesses fused into one scene | 2 | Zoticus: Eusebius V.16 (with Julian, no place) welded to Apollonius V.18 (alone, at Pepuza) |
| Indirect report rewritten as direct speech | 4 | Sulpicius' angel given words about diminished strength it never says; the Donatist deponent's testimony reversed |
| Attributed to the wrong work or author | 5 | "comedies, tragedies and odes" is Sozomen V.18, not Socrates III.16; the treasure scene is not Ambrose I.41 |

The rest were quotations from a translation other than the cited one, and
claims not in the passage at all — Melania's "the confessors", the Mantinium
peasants' "rustics", Cyprian's "in ordinary dress", which is in no letter of his
in ANF05 or in Hartel.

### Two defects this pass introduced, and what they cost

Both were caught on read-back, and both were undone and redone rather than
patched, per *no fix on a fix*.

**The Donatist letters.** The correction was right about the source and wrong
about the prose it landed in. It wrote "Three of them close the same way … In
the others", but the paragraph had only ever introduced three letters, so "the
others" pointed at nothing. The *Gesta apud Zenophilum* in fact carries six
letters from three bishops — Purpurius, Fortis and Sabinus — and three of the
six close on the plea while three carry it mid-letter. The story now says so,
which is what the distinction needed in order to mean anything.

**Ariminum.** Verifying the corrected story turned up two further defects that
had nothing to do with the original finding. The rations quotation was not the
cited edition's wording — NPNF 2.11 reads "But that appeared unseemly to the men
of our part of the world", not "This was thought unbecoming by our people" — and
"the word Sulpicius glosses as 'substance'" conflated two things he keeps apart:
the creed of Nike abolishes *Ousia*; "of one substance" is his gloss of
*Homoousion*, elsewhere. Both corrected against the vendored file.

The lesson is narrow and worth keeping: **a correction is an edit, and inherits
every risk an edit has.** The gate protects quotations and numerals. It cannot
see a pronoun left without an antecedent, and it did not.

### A gate defect, fixed

The stale-exemption check tested whether a declared span was a *substring* of
the new text, not whether it was still a *quoted span* in it. An exemption that
deliberately keeps a word in ordinary prose — "of one substance with the Father"
— therefore read as stale and aborted a correct edit. The check now compares
against the set of quoted spans. Re-run across all 545 stories afterwards: 18
quoted spans were removed file-wide, every one of them inside the 15 corrected
stories, and every one declared.

### What it cost in readability

Fidelity and readability pull against each other here, and this pass spent a
little of the second to buy the first. Replacing a short false claim with the
actual source wording added 520 words across 15 stories, and five stories
crossed back over the 20-word average-sentence line (250 → 245 of 545). The
file's medians did not move: FK 10.4, FRE 56.6, ASL 20.2, zero single-block
stories. That is the right trade in that direction, and it should be made
knowingly rather than discovered later.

### What is now known about the 545

- **545 stories rewritten** for readability, all verified against baseline.
- **95 quotations read against the vendored sources** across §9, §10 and §11 —
  the 11 Gregory, the 50 unverified, and the 126 spans in these 44.
- **63 corrections** applied in total (27 in §10, 34 here, 2 in Ariminum).
- **26 quotations remain unverifiable** pending source acquisition.

The `verification` field is now the weakest claim the corpus makes about itself.
Of the 44 stories asserting the strongest form of it, sixteen were wrong. That
is an argument for retiring the field rather than repairing it — recorded in the
Decision-Log as open, and not decided here.

## 12. The Tier-1 sources acquired, and what verifying against them actually showed

Thirteen files were fetched, date-verified, headed and registered (commit
`4841c6c7`), closing the acquisition side of §10's finding that 31 spans cite a
work not in the library. The 24 quoted spans across the 11 stories those
sources serve were then read against them. Three are under twelve characters
(`sisters`, `the Cat`, `Jacobite`) and carry no verification weight, leaving
**21 checkable spans**.

**Five are verbatim in the source the story cites. Fifteen are not verbatim
anywhere in the corpus. One is verbatim only by coincidence, in three unrelated
files.**

| span | cited source | how it resolved |
|---|---|---|
| `what women there are amongst the Christians.` | Chrysostom, *De Sacerdotio* | already confirmed in §4 |
| `no one can have conferred on you but yourself` | Augustine, *Letter* 188 | **verbatim, already vendored** |
| `unmixed poison` | Augustine, *Letter* 188 | **verbatim, already vendored** |
| `according to the rules of poetic art` | Kylie 1911 | **closed by this acquisition** |
| `a hundred thousand` | John of Ephesus, PO XIX | **closed by this acquisition** |
| `sick at heart` | Gregory of Tours IX.19 | verbatim only in Gregory of Nyssa, Augustine and Chrysostom — coincidence, not the cited source |

### The finding that matters, and it is not the one the acquisition was for

**The Atlas quotes modern translations.** Every one of the fifteen
not-verbatim spans is the right passage, in the right work, saying what the
story says it says — rendered by a translator whose words are not in any
public-domain edition. The pattern is consistent enough to read off directly:

- Bede II.13 — Atlas `So this life of man appears for a little while … we know
  nothing … any greater certainty`; Giles 1903 has "for a short space … we are
  utterly ignorant … contains something more certain."
- Egeria 37 — Atlas `holds the extremities of the sacred wood firmly in his
  hands`; Bernard 1896 has "takes hold of the extremities of the holy wood with
  his hands." Atlas `took a bite`; Bernard has "fixed his teeth in it."
- Gregory of Tours IX.19 — Atlas `sick at heart`; Dalton 1927 has "with
  bitterness of heart."
- Leoba — Atlas `I beg you not to disdain to send me a few words`; Kylie 1911
  has "deign to correct the homely style of this letter, and to send me for a
  model some words of thine."

This is a different problem from the one §5, §9 and §10 diagnosed. Those read
the gap as acquisition: the cited passage was not on disk, so nothing could be
checked. It was on disk in the sense that mattered — the substance checks out
in all seven stories read this way. What is not on disk, and cannot be
acquired, is **the wording**, because the wording belongs to a translation
still in copyright.

**Acquiring a public-domain edition verifies that a passage exists and says
what is claimed. It cannot verify a quotation.** That distinction was not
visible before these files were on disk, and it governs what the remaining
Tier-2 and Tier-3 acquisitions can be expected to deliver.

### Two things the acquisition was not needed for

Pelagius' *Letter to Demetrias* was the headline Tier-1 target, acquired as
Migne PL 30 after §5 recorded it as appearing "only as a line in Schaff's
bibliography." **Both its quoted spans were already verifiable** in
`npnf101_augustine-confessions-letters.xml`, vendored long since: Augustine's
*Letter* 188 quotes *Epistle to Demetrias* ch. xi verbatim — "your spiritual
riches no one can have conferred on you but yourself" — and supplies "unmixed
poison" in his own reply. The story's own source list names Letter 188. The
quotation was never unverifiable; it was never looked for in the source the
story already cited.

PL 30 is still worth having — it is the full Latin — but it closed nothing.

### Still open, and why

- `for we shall be killed when we go home` — cites the full Acts of Chalcedon,
  which remain unvendored. Unchanged from §10, where it was deliberately left.
- Romanos' `Today the Virgin gives birth to him who is above all being` —
  Pitra 1888 is Greek, and its OCR is unusable for a verbatim check. Acquiring
  it did not help and was not going to.
- The Benjamin summons and Radegund's demand to be consecrated — narrative
  present in both sources, quoted wording not verbatim, same translation
  pattern as the rest.

### The decision this raises, which is not settled here

Three ways to treat a story whose quotation is a modern rendering: re-render it
to the public-domain edition now vendored, which costs prose quality and reads
worse; keep it and mark it as quoted from an edition the corpus cannot hold;
or drop the quotation marks and report the substance. **That is a methodology
change, so it is Mark's, and it is recorded here rather than acted on.** It is
also the second argument this audit has produced for retiring `verification` as
a stored field: the field cannot express "right passage, right sense, wording
from a translation we do not own," which is the actual state of most of the
corpus's quotations.
