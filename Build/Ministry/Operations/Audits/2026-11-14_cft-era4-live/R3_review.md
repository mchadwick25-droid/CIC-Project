# Era 4 on the live tree (data release 43): review round 3

Reviewer: fresh Opus agent, full effort, independent of the drafting and of rounds 1 and 2. Targeted recheck, the last round. Branch `claude/cft-era4-live` at `e9f78829`, against `origin/main`. No paid calls.

**Verdict: Approved to proceed. 0 blocking, 0 substantial, 1 minor.** Both R2 substantial findings are fixed. Every minor finding taken is fixed, and the one declined (Bede's teaser) is declined on a sound reason. The single minor finding below is a recording step, not a text fault.

`node tools/validate-census.mjs --base <origin/main census> --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` passes: `619 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four shortName length warnings carried from release 42). `python tools/check_spelling.py --base origin/main --enforce` passes: 0 British spellings, 0 in enforced trees.

How this was checked. Each R2 finding was rechecked against the census and the held lines. Every line in `git diff 0e562369 e9f78829` of the census, `tools/quote_scan_readings.json` and the Decision-Log was read. The five changed census fields were scored with `engine.m1.gates.grade_text` and read for AI tells. The atlas copy in `cft-website/index.html` carries the same five changes, and the validator confirms it matches the census.

---

## Round 2 findings

| R2 | Status |
|---|---|
| S1 Bagratid why | Fixed. "He says Armenians pray with it in private. They treat it as a strong charm against every kind of danger." Ormanian: "For private prayers there is also used a book called Narek ... is regarded as a potent talisman against all kinds of dangers." (`ormanian_church-of-armenia_gregory1912.txt` l.7744-7748). The added place ("at home") is gone. Field FK 7.7, FRE 61.5. |
| S2 Narek closer | Fixed. The story now ends "The book still carries the name of the house that raised him." It rests on Chamich, "brought up from his infancy in the convent of Narek" (`chamich_history-of-armenia-v2_avdall1827.txt` l.4814-4815). "For centuries" is gone. The story's earlier sentences already give Serpos's 1786 use in the services and Ormanian's private prayer, each dated. Field FK 8.5, FRE 67.0. |
| M1 Dhuoda attribution | Fixed. The Patrologia note now carries only the rising, "Willelmus patris mortem ulturus, Pippini auxilio Tolosam intercepit" (`eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt` l.112842-112844, OCR normalized). The death in 850 is now Bondurand's: "Guillaume fut condamné à mort en 850 et exécuté comme rebelle" (`dhuoda_liber-manualis_bondurand1887.txt` l.1833-1834). "The book's editor" is true: the file is Bondurand's edition, Le Manuel de Dhuoda (header l.3-5). "Bondurand adds" for the younger Bernard holds ("ne songea qu'à venger son père et son frère", l.1842-1843). Field FK 8.0, FRE 70.6. |
| M2 Verden caveat | Fixed. "known here only through the index to his works and a report by the scholar Jean Mabillon." The report is Mabillon's Elogium historicum, headed "(Mabill., Act. SS. ord. S. Benedicti.)" (`alcuin_opera-omnia-letters_migne-pl100-101_1863.txt` l.112776-112800). It names the letters on the tithe: "Quid de relaxandis decimis ... senserit vir pius, probant epistolae 7 et 41 (nunc 33 et 65)" (l.114700-114703, OCR normalized). Mabillon is now introduced before he is named. Field FK 9.0, FRE 64.7. |
| M3 Dionysius closer | Fixed. "Bar Hebraeus keeps only a few passages in Dionysius's own words. The rest of the journey is Bar Hebraeus's telling." The ambiguous "his own" and the recap list are gone. It agrees with the caveat ("He tells the journey without marking it as Dionysius's own words, though he quotes him on Egypt just after"). "The rest of" is right, since the quoted Egypt passages are themselves part of the journey. Field FK 8.8, FRE 69.8. |
| M4 Agathon reading | Fixed. The Evetts l.46143 reading is removed from `tools/quote_scan_readings.json`. The file now holds 12 readings new against `origin/main`, the number the Decision-Log gives. The Decision-Log's account is true to the page: the earlier reading ("I the sinner Agathon") added a word, the sentence reads "And as for me, the sinner Agathon" (l.45965, l.46143), and the file prints "the" as "I he". |
| M5 Bede's teaser | Declined, on a sound reason: the teaser is the approved card's knownFor, and every new entry's teaser equals its knownFor. At FRE 59.1 it is 0.9 below the target, which CLAUDE.md sets as a principle to write toward. Nothing in it is wrong. The decline is not yet recorded where the project keeps carried items; see M1 below. |
| M6 Decision-Log count | Fixed. "109 changes to older census text". The Agathon change is to the new entry. |

---

## MINOR

### M1. Bede's teaser below the reading-ease target is not carried in Open-Gaps 264 (`Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`, item 264)

Text left as it is (`bede-of-jarrow`, teaser and card.knownFor): "Monk and priest of Wearmouth and Jarrow who wrote the Ecclesiastical History of the English nation. He also wrote commentaries on many books of the Bible, drawn from the Fathers, and books on nature and the reckoning of time." FK 9.9, FRE 59.1.

R2 M5 was declined in `R2_changes.md` only. CLAUDE.md asks that every review outcome be tracked in Open-Gaps, not left in a thread or an audit file. Item 264 already carries "Census text not changed here, below the reading target", but it names only older fields.

Fix: add to that line of item 264: "Bede's teaser, which is his approved card's knownFor (reading ease 59.1), was kept as approved (review round 2, M5); a split into two sentences waits for the next Bede profile change." This can be done when the REVIEW-PARA is filled in. It does not block the release.

---

## Checked and holding

- **Changed fields, held lines.** All five changed census fields rest on the lines cited above. No new claim, date or place was added.
- **Reading level.** Every changed field is between FK 7.7 and 9.0 and FRE 61.5 and 70.6. The changed sentences alone: Bagratid FK 4.2, FRE 82.5; Dhuoda FK 9.1, FRE 59.6 (three sentences with two editors' names, inside a field of FRE 70.6); Dionysius FK 5.3, FRE 76.5.
- **AI tells.** None in the changed lines: no filler, no hedging, no stock closer, no recap. The Narek story ends on a concrete fact, and the Dionysius story on a plain statement of where its text comes from.
- **Atlas copy.** `cft-website/index.html` carries the same five changes. The validator checks atlas and tree against the census and reports 0 errors.
- **Decision-Log entry.** Apart from the two expected placeholders, APPROVAL-LINE and REVIEW-PARA, the two edited paragraphs are true to the branch: 12 readings, the account of Agathon's sentence, 109 changes to older text. The rest of the entry is unchanged since round 2, which checked it.
- **`Census_Text_Changes.md`.** Its New lines for the five fields match the census.
