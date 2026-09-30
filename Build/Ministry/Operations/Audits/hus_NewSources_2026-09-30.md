# hus — revision after the new sources, 2026-09-30

Drafting record for the revision of `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md` and `Open_Gaps_Tracking.md`. The live files carry the result and none of this account. No review was written in this pass.

## Trigger and status

- Trigger: the Library vendored the material listed in Open_Gaps entry 26 (commit 4e4ba15a1; Foxe vol. III and Van Braght placed to `hus` in commit 46108dd02).
- The launching instruction says the project lead ruled that the three-round revision cap counts from significant new material, so this opens a fresh cycle. That ruling was relayed to the drafting worker in the instruction. The worker saw no record of it, and it is not attributed to the project lead in any live file. The live files say only that a fresh independent review is needed.
- The prior cycle ended at Round 3 with both documents approved to proceed (`Review-Artifacts/Round3_Recheck_Review.md`). The status lines of Doc_01, Doc_02 and the Registry now read "in revision, awaiting independent review". `build/hus_Build_State.yaml` records revision cycle 2 with 0 rounds used.
- The one-world, three-strand ruling of 30 September 2026 was not touched. Only evidence lines inside the strand section were updated.
- Left open, as instructed: Article 29, the Representative, and the registration of `hus`.

## What was read, and how it was checked

Every locus and quotation in the new rows was matched by a script to the vendored file after whitespace and line-break-hyphen normalisation only (no OCR correction), and each was given its line number and structure marker. A script also re-extracted every quoted string in the new rows and in the added lines of Doc_01 and Doc_02 and matched it to the assigned files. The residual non-matches were pre-existing quotations that a re-wrap presented as new text, English glosses of mine, and heading strings that the scan misprints. No page image was available, so no quotation was checked against a printed page.

Read (loci, not whole volumes):

- Palacký, *Documenta*: Part I heading; the letters headed "Gallo (Havlikoni) praedicatori in Bethlehem", "Amicis Constantiae" and "Amicis suis Constantiae"; the *Relatio* headings and Part V (the degradation, the answer to the marshal, the hymn).
- Novotný: nos. 95, 139*, 140 and 141 with their headings, manuscript lists and notes.
- Erben vol. 1: the exposition of the creed (chapters XXVI to XXVIII). Vol. 2: heading and a whole-line search for the cup. Vol. 3: the *Dcerka* opening, the contents, and Erben's editorial note on two spurious letters.
- Chelčický: the Preface, chapters I, II, XIV and XXIII; the chapter list; located chapters LXVIII to LXXIII.
- Březová: the Four Articles as the Praguers sent them (Latin and Czech, pp. 391 to 394), the twelve Taborite articles (opening), the Taborite priests' articles (opening), the Picards and Adamites (Latin and Czech), Goll's notes on the chalice and on the author's office.
- Brown's *Fasciculus* vol. I: the contents list, the Confession (headings and the Christ, Church and Eucharist sections in outline) and the *Excusatio* (heading, the priests' labour sentence, the offer of a Bohemian version, the "utraque specie" sentence).
- Palacký, *Urkundliche Beiträge* vol. 1: no. 34 (the legate's reply and the quoted four points) and the headings of nos. 193, 381 and 542. Vol. 2: nos. 962 to 964 and the heading of no. 912.
- Piccolomini 1524: the contents list, the chapter heading for the Adamites and the Poggio passage, compared with the 1592 file. Comenius 1702: sections 60 to 64. Foxe: the inquisitor's testimonial. Van Braght: the Hus entry and the Taborite notice. Thomson: the "Authorship and Date" passage.

## Findings that changed earlier claims

1. Hus's own Czech exposition of the Nicene Creed shows every clause that Doc_01 §8 and entry 4 listed as not found in his words. The Article 4 check is rewritten on that basis.
2. Workman's English gives the third clause of Hus's last hymn as "conceived"; the Latin of the *Relatio* reads *natus* ("born"). Doc_01 §8 had carried Workman's word.
3. Erben (1868) called two cup letters spurious. Palacký and Novotný print them from manuscripts, including the Mladoňovic manuscript Erben said would have held them. Novotný no. 95 sets a possible early interest in the cup against Workman's "little interest". The Doc_02 confidence map splits the old "Hus took up the cup late and defended it from prison: Documented" into two rows (Documented; Contested).
4. The Four Articles are on the shelf in Latin: in a papal legate's reply (cup first) and in Březová (preaching first, garbled). Doc_01 §3 had treated "the first Article" as settled.
5. Taborite articles are on the shelf through Březová (twelve articles; the priests' articles). Palacký's Taborite documents that were read are German summaries only. The Taborite strand is no longer voiceless, but it is not first-witness.
6. The Unity has a Latin confession and an *Excusatio* on the shelf as a second witness. Both kinds and the Christ clauses appear in outline. The print's heading says the *Excusatio* answers two letters of Dr. Augustine to the king, which differs from Seifferth's "letters to Dr. Augustine". The second quotation of row 43 is found in the Latin.
7. Comenius (1702, second witness) describes a drawing of slips in 1467. The Doc_02 line "Nothing in the vendored texts mentions a lot" is corrected.
8. The Compactata date is now on documents (Palacký nos. 962 to 964, no. 964 in Latin), and its confidence moves from Widely Accepted to Documented.
9. Corpus figures: 23 files, 35,341,097 characters (36,047,134 bytes) by Python `len()` and by `wc -m` under `LC_ALL=C.UTF-8`; 22,880,482 characters when three whole-volume files are cut to the sections the corpus map names. The old figure of 6.65M characters for eight works and the "21 per cent" tradition share are replaced. The shelf is 396 text files in 403 entries. `REGISTRY.yaml` lists 396.

## Changes by file

- `Source_Registry.md`: rows 55 to 79 added (25). Rows 34, 35, 49, 50 and 51 marked superseded, with no Confidence letter. Rows 5, 11, 13, 16, 22, 29 to 33, 39, 43 and 48 corrected where a statement had become false. Legend gains the witness-status rule. The saturation statement is rewritten (still not closed).
- `Doc_02_Source_Ecology.md`: §1, §2 (Hus transmission and visibility; five new author blocks), §3 items 1, 2, 4, 5 and 6, §4, §6 (Women, lay, Taborites, early Unity, Czech speakers, forces lens), §7 items 1, 3, 4, 6 and a new item 8, the whole confidence map, §9 counts and limits, §10.
- `Doc_01_World_Identification_Boundaries_Orientation.md`: the status line; §2 (Compactata, Tábor source); §3 gravities 1, 2, 3 and 6; §4 (sword, cup, Czech); §5 (Taborite, Adamite and Unity evidence lines; the costs of two alternatives; the "does not decide" line); §7 (Wyclif and Piccolomini notes); §8 rewritten; §9 item 5.
- `Open_Gaps_Tracking.md`: entries 27 to 35 appended in a new Section F. One wording fix in the Library's entry 26 (R5 line: "the item 1873" became "the volume 1873") so that `gaps` passes; the fact is unchanged.
- `build/hus_Build_State.yaml`: revision cycle recorded.

## Checks run

- `python -m engine.m10.cli gaps hus`: FAIL at HEAD on one line of entry 26 (the words "item 1873" match the bare-number pattern). After the wording fix: PASS.
- `python tools/check_live_commentary.py --surface worlds`: the hus files carry no REWRITE or ROUTE line other than the Registry's dated columns.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exits 1 across the whole branch because of other files (other worlds' registries, `cic/corpus-map/` files). For the hus files it reports no REWRITE or ROUTE in Doc_01, Doc_02 or Open_Gaps_Tracking.md. `Source_Registry.md` carries REWRITE (iso-date) on 54 table rows and KEEP (iso-date) on 21 more, and every one of them carried the same date fields before this pass. They are the template's required "Added" and "Discovery (channel / instrument / date)" fields, and they cannot be dropped without breaking the Registry schema.

## Not verified

- No quotation was checked against a page image.
- Palacký's Vienna-manuscript variants for the *Relatio*, and the word-by-word agreement of Palacký's and Novotný's Latin, were not collated.
- The year 1420 for the Taborite twelve articles, the 1421 date of the Picards' end, and the identification of Palacký's "Amicis Constantiae" with Novotný nos. 139* and 140 rest on the chronicle's sequence, a noisy line and heading content.
- Chelčický's chapters on killing, the Taborite priests' articles beyond the opening lines, the *Postilla*, Novotný's introduction, the remainder of Palacký's volumes and the Foxe and Van Braght sections were located and not read.
- The 5 July date for "the day after the feast of St Procopius" is general knowledge, not the vendored text.
- The reading "nine blank and three inscribed" in Comenius comes from a garbled line.

## The cap ruling's record

The project lead's ruling that the three-round cap counts from significant new material is recorded in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` (the entry "Three-round cap counts from significant new material", 2026-09-29), in his words: "Option 1, count from the new material, significant new material".
