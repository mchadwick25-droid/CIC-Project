# Live-reply record fixes, eleven worlds — adversarial review, round 2

- **Reviewed:** commit `7d17eef6` ("Revise record fixes per the round 1 review"), `git diff HEAD~1 HEAD -- records/`. 27 files, 2 of them new.
- **Against:** `Build/Ministry/Operations/Audits/2026-10-23_live-reply-record-fixes_Review_Round1.md` (B1–B9, N1–N12).
- **Method:** targeted recheck. I checked only three things: whether each round-1 blocking finding is resolved; whether each addressed non-blocking item was done correctly; and whether the diff adds any new defect. I checked every new quote and locus against `cic/texts/`. I ran `python -m engine.m10.cli records <world>` for the ten touched worlds. All ten pass. I made no model calls and edited no records.
- **Date:** 2026-10-23
- **Reviewer:** independent Opus context

## Verdict: PASS WITH FIXES

All nine round-1 blocking findings are resolved. The two new rzg source records are accurate. I found nothing invented in them. One new blocking finding remains: the Mamas source record's `citation` still places the work in an edition that does not hold it. The fix is one line.

## Round-1 blocking findings

| id | resolved | evidence |
|---|---|---|
| B1 | Yes | `hal.dw.record.md:30` now reads "which Jerome held truest". `use_note.means` (:54) never carried the claim. |
| B2 | Yes | `desert.demo.quiet-head.md:40` now reads "Greek homilies our record holds, from the eastern monasteries and not from our own desert". This matches the sibling dw. |
| B3 | Yes | `syr.term.ihidaya.md:53` now reads "Whether our teachers meant both senses on purpose, they do not say." That is an emic hedge. The scholarly reading moved to `divergence_note` (:16), which is etic metadata. |
| B4 | Yes | New `rzg.source.zwingli-latin-works-vol3` is cited from `rzg.term.providence` with locus "On True and False Religion, ch. [24] Merit". The file has the heading "[24]. Merit" and, at `cic/texts/zwingli_latin-works-correspondence-vol3_heller1929.txt:13583`, "the last. Now providence is the mother of predestination, as it" (continues "were," at :13584). The divergence_note now says only that quote was read directly. `verification_state` stays `verified-via-authority`, which is right for the Calvin part. |
| B5 | Yes | The limit's locus now matches the core's current thinness wording (`rzg.core...md:98-99`). It is a condensed paraphrase, not a verbatim quote, and is not presented as one. New `rzg.source.calvin-letters-vol2` is cited from the limit and the core. Loci checked in the letter bodies, not just the contents: CLXIV at `calvin_letters-vol2_bonnet1858.txt:2850-2853` "CLXIV.— To Amy Perrin. / Complaints regarding the conduct of Perrin" (April 1546). CLXXIII at :3488-3490 "CLXXIII.— To Farel. / Violence of the family of Amy Perrin"; the editor's note at :3521 says Farel's letter went "to Amy Perrin, in order to calm his resentment". CCLXXXV at :15085-15087 "CCLXXXV. — To THE Ministers of Switzerland. / Statement of the controversy with Bolsec regarding Election." Its note at :15105 names "Jerome Bolsec". All three concern what the records say they concern. |
| B6 | Yes | `don.contested.maximianist-reception.md:47-49` now says the quoted words are "the NPNF editor's English summary of Book III, not Augustine's own text", and narrows to "III". Confirmed: `npnf104_augustine-anti-manichaean-anti-donatist.xml:10353` sits in the synopsis paragraph that opens "Book III." (`v.ii.ii-p53`): "The Synod had granted a season of delay during which all who returned should be held innocent." |
| B7 | Yes | `witt.dw.true-priests...md` text and `witt.story.brussels-martyrs.md` `text` and `telling` now state "On the first of July, 1523" plainly. The heading/editor provenance stays in `divergence_note` (story :15, dw :17, :24) and `use_note.means`. No editor talk is left in emic speech. |
| B8 | Yes | `de-vita-sua` `rights_status` now says not acquired; its `discovery_channel` and `verification_state: named-not-rechecked` already fit. `mamas-festival` now has `named-not-rechecked`, an unvendored `rights_status`, and a matching `discovery_channel`. `grep -i mamas` on npnf207 finds nothing, as the edition field now says. See new finding R2-B1 for one field left behind. |
| B9 | Yes | `syr.demo.woman-authority.md:14` is now Widely Accepted. Line 85 now reads "then the standing later accounts report (the choirs)". |

## New rzg source records

- **`rzg.source.zwingli-latin-works-vol3`.** Title, editor, publisher, 1929 date and "Copyright, 1929 by the American Society of Church History" match the file header (lines 1-30) and `cic/texts/REGISTRY.yaml:2772-2789`. The work dates (1525, Antibolon 1524) match the header's content note and the volume's own text (:117, :404). The discovery channel (registry entry 2026-09-25) matches. The file is in the rzg corpus map (:561-576). Nothing invented.
- **`rzg.source.calvin-letters-vol2`.** Title, Bonnet as editor, Philadelphia 1858, "translated from the Latin and French" with no translator named, and "NOT_IN_COPYRIGHT" all match the file header (lines 1-12, :82) and `REGISTRY.yaml:2752-2759`. The file is in the corpus map (:201-211). Nothing invented.

## Addressed non-blocking items

| id | correct | note |
|---|---|---|
| N1 | Yes | "(NPNF numbering)" added in both places. `verification_state` is now `verified-direct`, which fits the direct check. |
| N2 | Yes, with a note | Both alx records are now Contested with a scoping divergence_note. "Nautin disputed both" is supported by `Build/worlds/alx/Doc_02_Source_Ecology.md:147` ("the authenticity and dating were questioned by Nautin"). Nothing in the notes is unverifiable. See R2-N1. |
| N3 | Yes | `desert.dw.jesus.md` now carries the exact words. Verbatim at `npnf204_athanasius-select-works-letters.xml:32399-32400`: "daily a martyr to his conscience, and contending in the conflicts of faith". The unsupported gloss is gone. "One command turned Antony's life" fixes the compression. See R2-N2 on sentence length. |
| N4 | Yes | The repeated sentence is cut. |
| N5 | Yes | "weeks later" is now "later". `ijc.force.chalcedon-failed-consensus` is cited; citing a force record in `sources:` follows existing practice (e.g. gallic). |
| N6 | Yes | "Once," removed. |
| N7 | Yes | The divergence_note gives the translator's literal sense. It matches `anf01_apostolic-fathers-justin-irenaeus.xml:1918-1922`: "Literally, “on account of the title of the oversight.”" |
| N8 | Yes | "took Christ at his word" in both records. |
| N9 | Yes | Lower-cased. |
| N12 (part) | Yes | SHC ch. IV added to the two rzg records, with the locus quote "can not be represented by any image" as checked in round 1. |

Not addressed: N10 and N11 (both optional), and the N12 rzg force-sources item. `Build/worlds/rzg/Open_Gaps_Tracking.md:358` registers only two such force records; round 1 counted 19. That gap should be registered at its true size.

## New findings

| id | file:line | severity | finding | evidence | required change |
|---|---|---|---|---|---|
| R2-B1 | records/cappadocian/source/cappadocian.source.gregory-nazianzus-on-the-mamas-festival.md:23 | BLOCKING | The `citation` field still says the work is in "Nicene and Post-Nicene Fathers, 2nd series, vol. 7". The record's own `edition` field now says the work is not in that file. The citation is wrong and contradicts the record. | `grep -i -n "mamas\|new sunday" cic/texts/npnf207_cyril-jerusalem-gregory-nazianzen.xml` finds no hits | Drop the NPNF vol. 7 location from `citation`, as the de-vita-sua record already does ("Gregory of Nazianzus, on the Mamas festival"). |
| R2-N1 | records/alx/figure/alx.figure.gregory-thaumaturgus.md:14-15; records/alx/source/alx.source.gregory-address-to-origen.md:14-15 | NON-BLOCKING | The notes name Nautin's dissent but not where the debate stands. Doc_02 says the consensus upholds the traditional date. A reader of "Contested" alone may think the field is evenly split. | `Build/worlds/alx/Doc_02_Source_Ecology.md:248` "Nautin's authenticity/dating dispute; consensus reaffirms c. 238" | Add "most later scholarship upholds c. 238" to both divergence_notes. |
| R2-N2 | records/desert/doctrinal_witness/desert.dw.jesus.md:36-37 | NON-BLOCKING | "When persecution ended, Athanasius says, Antony went back to his cell and was there daily a martyr to his conscience, and contending in the conflicts of faith." is about 30 words, over the ~25-word ceiling. | (writing standard, CLAUDE.md "Accessible and rigorous") | Split it, e.g. end at "his cell." and start "There, Athanasius says, he was daily a martyr...". |
| R2-N3 | records/rzg/honest_limit/rzg.limit.marburg-bolsec-perrinist-narrative.md:35-36; rzg.source.calvin-letters-vol2.md:19 | NON-BLOCKING | Vol. II ends in 1553 (last letter CCCXXXIX, "[1553.]", `calvin_letters-vol2_bonnet1858.txt:21085-21089`). The Perrin letters it holds date from 1546-1553. The statement names a crisis "largely settled by 1555", then says "we have Calvin's own letters" for the Perrin conflict. A reader could take that to cover 1555. Vol. III, which would, is an open acquisition gap (`REGISTRY.yaml:2748-2751`). | as cited | In the source record body, scope the Perrin locus to "1546-1553". Optionally say the same in the limit's `why_sources_cannot_answer`. |

## Round 2 addendum

Checked against the uncommitted working-tree diff (`git diff -- records/`), same date and reviewer.

- **R2-B1: resolved.** The Mamas `citation` now reads "Gregory of Nazianzus, on the Mamas festival". It no longer places the work in NPNF vol. 7.
- **R2-N2: resolved.** The sentence now ends at "his cell." The next sentence is "There he was daily a martyr to his conscience, and contending in the conflicts of faith." The quoted words are still verbatim with `npnf204_athanasius-select-works-letters.xml:32399-32400`.
- **R2-N3: partly resolved.** The Calvin-letters `locus` in both the limit (:22) and the core (:45) now reads "1546 to 1553 (letters CLXIV, CLXXIII; this volume ends in 1553, before the 1555 crisis)". The body of `rzg.source.calvin-letters-vol2.md` (:29) is unchanged and still unscoped.
- **Remaining implication (NON-BLOCKING).** Two places still pair the 1555 crisis with Calvin's letters without saying the letters stop in 1553. The first is the limit's participant-facing `statement` (:34-37): "The third is the Perrinist crisis, fought out at Geneva and largely settled by 1555 ... For the Bolsec dispute and the Perrin conflict we have Calvin's own letters, written as he lived them." The second is the core thinness field (:98-99): "the Perrinist crisis (1555). Calvin's own letters give first-hand accounts of Bolsec and of the Perrin conflict." Neither says outright that the letters narrate 1555. A reader could still infer it. Suggested fix: "For the Bolsec dispute and the earlier Perrin quarrels, up to 1553, we have Calvin's own letters." Make the same change in the core and in the source record body.
