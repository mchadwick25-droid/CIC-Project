# Live-reply record fixes: independent recheck, round 1, 2026-10-24

An independent Opus recheck of the record fixes in PR 1094 (https://github.com/mchadwick25-droid/CIC-Project/pull/1094, branch `claude/exciting-bardeen-sr4a1i`, head `4f3776ea`). The input was the fix list, `2026-10-24_live-reply-record-fixes_Fix-List.md`. The findings come from the 19 October claim check, `2026-10-19_live-reply-claim-check_eleven-worlds.md`. This thread made none of the fixes and edited no record. Round 1 of at most 3.

Method: for each item, the record as it stands on the PR head, read against the vendored line it cites in `cic/texts/`. Checked: (a) true to the source, (b) nothing added that the source does not carry, (c) confidence tags and contested_claim records, (d) quotes word for word, (e) reading level and voice of the touched text. A finding is blocking only if something is wrong, unsupported or misleading.

## Result

47 items checked: the 7 said to be fixed before the PR, the 38 fixes, and the 2 points PR 1089 confirmed.

- Confirmed: 37
- Confirmed with a change, not blocking: 4
- Blocking: 6 fixes, plus one quote outside the fix list in a record this PR touched (7 findings, B1 to B7)

The seven blocking findings are each a one- or two-line fix. None needs a decision from Mark. B4 needs one judgement about who said the words. That judgement belongs with the fixing thread.

## Blocking findings

**B1. Fix 3, `desert.demo.quiet-head` line 40.** The new text says the homilies are "from the eastern monasteries and not from our own desert," and states it as fact. The cited lines, `macarius_fifty-spiritual-homilies_mason1921.txt:554-555`, say only that the Macarius ascription rests on no outside evidence. The same edition then argues the opposite: "The scenery is exactly that of the Egypt of the fourth century ... particularly of the Egypt of the desert" (`:566-572`). `desert.source.macarian-homilies` rates authorship Contested. It sets the bound as "NOT securely the words of Macarius the Egyptian", which is a weaker claim than "not from our own desert". The new sentence also runs to about 35 words, past the 25-word ceiling. Fix: give it as the modern view, for example "Greek homilies under Macarius's name, which most scholars now place in the eastern monasteries rather than our desert", and split the sentence. The same flat wording is in `desert.dw.the-heart-and-the-spirit` line 29. That record is not in this PR, but it has the same defect.

**B2. Fix 10, `alx.dw.jesus` lines 32-33.** "Athanasius, still a young man and writing about 318" is stated flatly. The vendored editor hedges it. He gives it as "the date usually adopted" and reaches it by inference ("inclines us to put the composition as late as we can", `npnf204_athanasius-select-works-letters.xml:12086-12092`). The record drops the hedge its own source carries. A further note from outside the vendored texts, so it cannot be checked in the Library and should not go into the record: later scholars have also argued for a date in the 330s. Fix: "in a book usually dated about 318", and drop "still a young man", which depends on that date. Log the later-date view in `Build/worlds/alx/Open_Gaps_Tracking.md` as a claim to check.

**B3. Fix 13, `cappadocian.term.philoptochia` line 14.** The sources now point to the new unvendored `cappadocian.source.gregory-nyssa-de-pauperibus-amandis`. But the divergence_note still says "Documented via Nazianzen's and Nyssen's own poverty orations, both genuinely vendored." After fix 13 that is false for Nyssa (`npnf205_gregory-nyssa-dogmatic-treatises.txt` has the homilies only as a name, at `:1528`). Fix: say that only Nazianzen's Oration 14 is vendored, and that Nyssa's two homilies are named but not held.

**B4. Fix 15, `cappadocian.quote.basil-against-eunomius-ant`.** The re-sourcing is accurate: the quote matches Letter XVI word for word (`npnf208_basil-letters-select-works.xml:24124-24151`), with its omission marked. But the vendored corpus holds the same passage, the questions about the ant included, as Gregory of Nyssa's own text: Against Eunomius X in NPNF numbering, `npnf205_gregory-nyssa-dogmatic-treatises.txt:19688-19712`. The translation is different but the argument is the same. The record names Basil as speaker, rates the quote Documented, and has `divergence_note: null`. So the Representative will say "Basil said" with no sign that the vendored texts give the words to Nyssa as well. Fix: a divergence_note naming the Nyssa parallel, and authorship rated Contested. If the thread judges the passage to be Nyssa's, change the speaker and source to match. `cappadocian.dw.want-to-believe` line 67 and `cappadocian.dw.doubt-and-unfinished-growth` cite this quote as Basil's and should follow the same choice.

**B5. Fix 28, `syr.story.choirs-tradition` line 56 (use_note.means).** The new text says "only Jacob of Serug says Ephrem founded the choirs". Nothing supports "only". The record's own text says "only the later memory says". The vendored 1898 editor gives the same founding tradition without naming Jacob (`npnf213_gregory-great-ephraim-syrus-aphrahat.xml:11250-11254`). Fix: "only later memory, first in Jacob of Serug, says Ephrem founded the choirs."

**B6. Fix 37, `witt.quote.second-article-of-the-creed` lines 119-120.** The 19 October finding named lines 18 and 120. The frontmatter is fixed. But the body still says "every household under this program said these same words as its own weekly confession". That is household uptake stated as fact, against `witt.contested.household-catechism-reception` (Contested). Fix: the same wording as the frontmatter, "prescribed for every household; how far households took it up is Contested". This also removes build commentary from a live record.

**B7. Not in the fix list: `ijc.story.tome-that-would-not-bend` line 62 (telling).** This PR edits the record (fixes 22-23). The telling quotes the bishops as "Peter has spoken so through Leo." The vendored acts read "Peter has spoken thus through Leo" (`npnf214_seven-ecumenical-councils.xml:20000`). The record's own `text` field has "thus". The quote is not word for word. Fix: "thus".

## Confirmed with a change (not blocking)

These can ride the push for the blocking fixes.

- **Fix 4, `desert.dw.jesus` line 49 (positions).** The text no longer generalises, but the positions entry still does: "the fight once fought against persecutors is fought now against one's own thoughts - the same following, relocated". Life 47 says only that Antony was "daily a martyr to his conscience, and contending in the conflicts of faith" (`npnf204…:32399-32400`). Credit it to Athanasius on Antony, as the text now does.
- **Fix 5, `desert.core.desert` formation_logic.** "With the persecutor gone, Antony's war with demons became the total fight" goes a step past Life 47, which speaks of conscience and "the conflicts of faith", not demons. Use §47's own words. The rest of the rewrite is true to the old text, and it reads far better than before.
- **Fix 27, `pahc.force.neronian-persecution` line 38 (manifestations).** "the episcopal office" reads back the later sense that the record's own new divergence_note warns against. Use "the office of oversight", as the description does.
- **Fix 33, the six rzg records citing the Second Helvetic Confession, ch. IV.** The quotes match the vendored file word for word (`schaff_second-helvetic-confession-heidelberg-catechism_1919.txt:479-480`, `:496`). But that English is Schaff's "condensed translation of the original" (`:376-377`), not the full text. `rzg.source.second-helvetic-confession` should say so.

## Item by item

| # | Record(s) | Source line checked | Verdict |
|---|---|---|---|
| pre | `don.dw.who-jesus-was-among-us` (279, three days) | "three days" gone; 279 Donatist bishops at `pl11-zeno…:73364` | Confirmed |
| pre | `don.demo.death-wish`, `don.dw.not-a-death-wish` | "whole length" gone; Passio Marculi "vel pauca dicenda sunt", `monumenta-vetera…:894-897` | Confirmed |
| pre | `don.dw.becoming-one-of-us` On Baptism V.5.6 | `npnf104…:12744`, inside the Book on Cyprian's letter to Jubaianus (Book V), ch. 5 | Confirmed |
| pre | `don.core.donatism` Church of the Martyrs | line 88 frames it as modern scholars' summary | Confirmed |
| pre | `desert.dw.god` refusal | credited to Antony via Athanasius; `npnf204…:32913-32919` | Confirmed |
| pre | `desert.dw.strangest` father's house | "outside his house", "abode of his fathers"; `npnf204…:31272`, `:31286-31287` | Confirmed |
| pre | `gallic.dw.the-christ-who-bears-the-wounds` hours | Palestine, Mesopotamia and the East; `npnf211…:17802-17804`, `:17848-17849` | Confirmed |
| 1 | `don.dw.the-creed-we-shared` | Letter 185, `npnf104…:19321` ("Nor is this the actual question in dispute") | Confirmed |
| 2 | `don.dw.becoming-one-of-us`, `don.contested.maximianist-reception` | NPNF summary of Contra Cresconium III, `npnf104…:10353`; Latin `petschenig…:47029-47033` | Confirmed |
| 3 | `desert.demo.quiet-head` | Mason `:554-555`, `:566-572` | **B1** |
| 4 | `desert.dw.jesus` | Life 80 `npnf204…:33169-33170`; Life 47 `:32399-32400` | Confirmed with a change |
| 5 | `desert.force.martyrdom-unavailable`, `desert.dw.strangest`, `desert.core.desert` | Life 46-47, `npnf204…:32397-32400`; "martyr" appears in the Vita's own voice only at §46-47 in this sense | Confirmed (core: with a change) |
| 6 | `gallic.force.renunciation-that-stays`, `gallic.force.office-temptation-destiny` | "posted" gone; Inst. XI.18 `npnf211…:24726-24730` | Confirmed |
| 7 | `gallic.dw.christ-in-the-beggar-and-the-guest`, `gallic.dw.one-person-two-substances` | Ep. III `npnf211…:2427-2431` (Martin's other recorded word, so "in our record" is right) | Confirmed |
| 8 | `gallic.dw.christ-in-the-beggar-and-the-guest` | build narration gone from text and positions | Confirmed |
| 9 | `gallic.limit.only-on-paper` | `npnf211…:17802-17804`, `:17848-17849` | Confirmed |
| 10 | `alx.dw.jesus`, `alx.source.athanasius-de-incarnatione` | `npnf204…:12086-12092` | Source record confirmed; dw **B2** |
| 11 | `alx.figure.gregory-thaumaturgus`, `alx.source.gregory-address-to-origen` | both now Contested, Nautin named, no consensus claim | Confirmed |
| 12 | `cappadocian.force.movement-institutionalized` | sentence deleted | Confirmed |
| 13 | new `…de-pauperibus-amandis`; `…love-of-the-poor-lepers-consolation`; `philoptochia`; `poorhouse-famine-month` | `npnf205…:1528` (name only); `:32849`, `:33740` | Confirmed except `philoptochia` **B3** |
| 14 | four sources to `unvendored` | zero "Mamas" in npnf207; De vita sua only in endnotes (`:22377`); zero "Forty Martyrs" in npnf205; no three-book treatise in npnf208 | Confirmed |
| 15 | `cappadocian.quote.basil-against-eunomius-ant` | `npnf208…:24124-24151` verbatim; parallel `npnf205…:19688-19712` | Quote confirmed; attribution **B4** |
| 16 | `cappadocian.term.epektasis` | Against Eunomius VIII, `npnf205…:18778-18787`; subject is the creation; quote verbatim | Confirmed |
| 17 | `hal.dw.suffering`, `hal.dw.doubt` | Letter 39, `npnf206…:8125-8127` | Confirmed |
| 18 | `hal.core.hieronymian`, `hal.voice.craft`, new `hal.source.jerome-ep125` | Letter 125 §12, `npnf206…:25503-25515` | Confirmed |
| 19 | `hal.dw.record` | Gospels preface `npnf206…:46712-46716`; De vir. ill. 135 at `:1329-1331` | Confirmed |
| 20 | `hal.limit.f5-women-own-words` | `hal.contested.ep46-authorship` | Confirmed |
| 21 | `ijc.dw.jesus`, `ijc.demo.who-was-jesus` | Ep. XXVIII, `npnf212…:5487-5490`; Tome quote unchanged | Confirmed |
| 22 | `ijc.story.tome-that-would-not-bend`, `ijc.demo.never-settled` | `ijc.force.chalcedon-failed-consensus` (Egypt carried via scholarship, said so in the locus) | Confirmed (see B7) |
| 23 | same story | Session II `npnf214…:19992-20000`; sixteenth session `:14473-14475` | Confirmed |
| 24 | `pahc.quote.the-memoirs-of-the-apostles-are-read` | 1 Apol. 66, `anf01…:16477-16478` "which are called Gospels" | Confirmed (agrees with PR 1089) |
| 25 | `pahc.story.quintus-recantation` | Mart. Pol. ch. I-III before ch. IV Quintus, ch. V flight; `anf01…:3756-3822` | Confirmed |
| 26 | `pahc.witness.god-and-argument` | Trall. 9 `anf01…:6610-6621`; Smyrn. 7 `:8218-8224` | Confirmed |
| 27 | `pahc.force.neronian-persecution` | 1 Clem. 44, `anf01…:1914-1922`, with the translator's "title of the oversight" note | Confirmed with a change |
| 28 | eight syr records on the women's choirs | only vendored statement `npnf213…:11250-11254`; `syr.demo.woman-authority` now Widely Accepted | Confirmed except `syr.story.choirs-tradition` **B5** |
| 29 | `syr.core.syriac` | Aphrahat prose; `ephraim_prose-refutations…:20-22`; cautions rewrite true to the old text | Confirmed |
| 30 | `syr.term.ihidaya` | Dem. VI, `npnf213…:25929-25930`; Ephrem's pairing also at `:21879` | Confirmed |
| 31 | `rzg.contested.anabaptist-schism-legitimacy` | `zwingli_selected-works…:5568-5569`, quote verbatim | Confirmed |
| 32 | `rzg.limit.marburg-bolsec-perrinist-narrative`, `rzg.core…`, new `rzg.source.calvin-letters-vol2` | `calvin_letters-vol2…:15085-15092` (CCLXXXV), `:2850` (CLXIV), `:3488` (CLXXIII); last letters dated 1553 (`:21071-21117`) | Confirmed |
| 33 | six rzg records | Art. XVIII `zwingli_selected-works…:4562-4568`; SHC `schaff…:479-480`, `:496` | Confirmed with a change |
| 34 | `rzg.term.providence`, new `rzg.source.zwingli-latin-works-vol3` | `zwingli_latin-works…vol3…:13583-13584` verbatim; treatise named at `:3419-3420` | Confirmed |
| 35 | five witt records, "the how" | iron-and-fire `luther_works-v2…:7121-7125`; "I therefore permit every man to hold either of these views" `:7049`; `:7143-7146` | Confirmed |
| 36 | `witt.dw.born-in-sin-fed-at-the-table`, `witt.term.faith` | word-count claim gone | Confirmed |
| 37 | `witt.quote.second-article-of-the-creed` | Large Catechism `luther_large-catechism…:240-242`; contested record `:45-60` | Frontmatter confirmed; body **B6** |
| 38 | `witt.story.brussels-martyrs`, `witt.dw.true-priests-of-gods-own-making` | `luther_hymns_bacon-allen.txt:149-151` (heading 1522, editor 1 July 1523) | Confirmed |
| 1089 | `hal.dw.suffering` against Jerome Letter 39 | `npnf206…:8125-8127` | Confirmed |
| 1089 | `pahc.quote.the-memoirs-of-the-apostles-are-read` against 1 Apol. 66 | `anf01…:16477-16478` | Confirmed |

Two 19 October findings are not on the fix list but were checked. Both are already fixed on `main`: `gallic.force.army-and-rank-before` ("posted" gone, commit `87700580`), and `desert.dw.the-heart-and-the-spirit` ("we carried" gone; see B1 for the wording that replaced it). The changes in `engine/m9/enforce.py` waiver counts (cappadocian emic-vendored-only up from 66 to 84) follow from fix 14. They are logged as an open gap.

## Readability of the touched text

Most of the rewrites read better than what they replaced. The best are `desert.core.desert` formation_logic, `hal.core.hieronymian`, and the `syr.core.syriac` formation_logic and cautions: short sentences, one idea each, voice kept. Two participant-facing spots got worse. The first is the 35-word sentence in `desert.demo.quiet-head` (B1). The second is the aside in `syr.story.qyama-morning`'s telling, "the choir of the daughters of the covenant, as later accounts have it, who will raise the madrasha". The aside separates "who" from the choir it refers to. That is not blocking. A fix: "Among them, later accounts say, stands the choir of the daughters of the covenant."

## Status

Round 1. B1 to B7 are blocking. The findings under these seven numbers do not clear until the fix is made and a recheck confirms it (round 2: a targeted look at these seven lines only). The other 41 items are confirmed (four of them with a non-blocking change), and their Open_Gaps entries can record the independent recheck as passed. The four non-blocking changes can go with the same push.
