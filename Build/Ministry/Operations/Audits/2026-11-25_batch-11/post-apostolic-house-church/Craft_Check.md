# Craft check: The Post-Apostolic House Churches

Kit Part 3, step 5: the changes after the fresh read, as `Fresh_Read.md` lists them, checked in `post-apostolic-house-church.brief.txt` against `Outline.md` and `Source_Sheet.md` only. No `.v1`/`.v2`/`.v3` file was opened. Nothing else was edited.

## Verdict: FIX (outline only)

The brief's seven changed sentences pass. Each says no more than its source, fixes the fault it was made for or the part of it the outline allows, and reads on one hearing. The brief needs no change. The outline still holds "Bithynia", and its Cut first 23 still holds the faulty Dionysius wording. The exact replacements are below. Two items stay open for Mark, as `Fresh_Read.md` says.

## The changed sentences

| # | New text | Holds? | Fault fixed? | One hearing |
|---|---|---|---|---|
| F1 | "Pliny, a Roman governor ruling a province," | Yes. "Governor": the heart's "a governor's trials" (mirbt 2795–2797), and L2/L6 (his edict, those "brought before me"). "Ruling a province" is the fresh trust read's own exact change, sourced there to an old witness (Tertullian, anf03 1566–1567), which the outline does not yet cite. Replacement 2 below writes it in. | Yes: Bithynia (McGiffert's note only, S7) is gone. | Reads. "Governor ruling" is a little redundant, but it is understood. Where: the opening now names no province. That is what the old texts give, so no place can be added (Mark item 1). |
| F2 | "The well-off gave what they chose, for orphans, widows, the sick, prisoners and strangers." | Yes. Beat 6, "Those who could gave what they chose"; J7, the collection for orphans, widows, the sick, prisoners and strangers. "Well-off" is εὐποροῦντες (Fresh_Trust F2, 1apol-grc 1772–1776). "For" is a fair compression of "left with the one who presides, who helps…". | Yes. The givers and their free choice are back, and the gifts no longer read as the shared bread. | Reads. |
| F3 / T2-1 | "…that his church still drew counsel from the letter Rome had sent in the quarrel, written through Clement." | Yes. R2: "draw advice … as also from the former epistle, which was written to us through Clement" (npnf201 25113–25117). The new Do not say (Outline 178) holds "drew counsel from". | Yes. The Lord's day is no longer moved onto Clement's letter. | Still the heaviest sentence (credit clause, Clement unexplained), as Fresh_Listen found. The MINOR note against changing it stands: the trust fix's wording and the required credit fix it in place. |
| Justin | "Justin, himself a Christian, wrote…" | Yes. Links: "Justin Martyr: one of them" (Outline 116). Quote 2's own "we all stand up together" (Outline 91) shows it too. | Half. *Who* he was is now given. *Why* he wrote is not in the outline (Sibling, Outline 57: the defence is the Greek Apologists'). Adding it here would add matter. Mark item 2. | Reads. |
| Easter | "others kept it only on Sunday." | Yes. V4, "on no other but the Lord's day"; Words to explain, the Sun's day = Sunday (Outline 44). | Yes, for the Easter clause. The essence keeps "Lord's day" (heart, untouched). Justin's "day named after the Sun" now meets "Sunday" in the narration. | Reads. |
| Irenaeus | "Irenaeus of Lyon reminded him…" | Yes. Names: "Irenaeus of Lyon" (Outline 99). | Partly. A place, not a role. No role is in the outline. MINOR, so noting it is enough. | Reads. |
| Ending | "Those elders kept a different day, yet lived at peace…" | Yes. V1 (npnf201 31527–31553), and Ending 1's "the elders before Soter". | Yes. The subject is now plain. | Reads, and closes on the subject. |

Nothing outside the outline was added. No other sentence differs from `.v3` as `Fresh_Read.md` lists it.

## Scorer and length

- `wc -w`: **673** (cap 675).
- `profile_readability`: 674 words, grade 7.5 (names out 7.0), reading ease 74.8, 16.9 words a sentence, longest 36. Pass. On grade 7.5: no changed sentence reads flat. F2 and the Easter clause are full sentences of cause and purpose, not one-act runs. The two name additions lengthen and do not flatten.
- `check_brief_craft.py`: 0 to look at.

## Outline replacements (FIX)

These carry out F1 and F3 in the outline. Replacements 1–3 touch the Mark-approved heart and Setting, so they are given for his ruling (Mark item 1), not applied.

1. **The heart, When and where (line 9).**
   Old: "Antioch in Syria, Smyrna and the province of Asia, Bithynia, Corinth, Philippi, Rome (Source Sheet §1)."
   New: "Antioch in Syria, Smyrna and the province of Asia, the province Pliny governed (unnamed in the held old texts), Corinth, Philippi, Rome (Source Sheet §1)."
2. **Setting, Places (line 31).**
   Old: "Bithynia, "a Roman province on the Black Sea";"
   New: "Pliny's province, unnamed: "a Roman governor ruling a province" (Tertullian, "ruler of a province", anf03 1566–1567; Eusebius, "one of the most noted of governors", npnf201 19448). "Bithynia" rests only on McGiffert's modern note (npnf201 19457): not told;"
3. **Openings 1 (line 64).**
   Old heading: "**(Recommended) Before dawn in Bithynia.**" New: "**(Recommended) Before dawn, under Trajan.**"
   Old: "Pliny, the Roman governor of Bithynia on the Black Sea, questioned people" New: "Pliny, a Roman governor ruling a province, questioned people"
4. **Do not say: add at the end.** "Pliny "the Roman governor of Bithynia on the Black Sea", or any named province → "a Roman governor ruling a province". The place rests only on McGiffert's note (npnf201 19457); the letter names none (mirbt 2768–2800)."
5. **Cut first 23 (line 226).** It still quotes the faulty sentence.
   Old: "that his church still read aloud on the Lord's day the letter Rome had sent in the quarrel, written through Clement."
   New: "that his church still drew counsel from the letter Rome had sent in the quarrel, written through Clement."
6. **Do not say lines 177–178.** These are two entries for one error, with the same left side. Replace both with one: ""Corinth read Clement's letter on the Lord's day" → "drew counsel from" it. The Lord's-day reading was of Rome's new letter (Soter's); the older one is read and drawn on, with no day given (npnf201 25113–25117)."
7. **Ending 1 (line 108).** It quotes the text as it stood before this pass. Old: "others kept it only on the Lord's day." New: "others kept it only on Sunday." Old: "Irenaeus reminded him" New: "Irenaeus of Lyon reminded him". Old: "They kept a different day" New: "Those elders kept a different day".

The Source Sheet's S7 row, its Plain spoken words ("Bithynia, a Roman province on the Black Sea") and its 2e heading carry the same place. They belong to the researcher's pass with replacement 2.

## Open for Mark (unchanged from `Fresh_Read.md`)

1. Bithynia: replacements 1–3 above, or a ruling that the place is Widely Accepted.
2. Why Justin wrote to the emperor: not in the outline. The listener's BLOCKING on Explain it is only half met until the researcher adds a held line, or Mark rules that "himself a Christian" is enough for a man who is here "only as the man who set down the Sunday".
