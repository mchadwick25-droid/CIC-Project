# Recheck, release 50: Martin of Tours

Round 2, targeted: only what changed between `martin-of-tours.r50.brief.txt` and `martin-of-tours.brief.txt`, against `FIXES.md` and `Fixes_R50.md`. Held texts opened at the cited lines (NP11, HALM, GT, and Gregory's Latin in `gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt`).

## One hearing

- **Who:** Martin, a fourth-century Roman soldier from Pannonia who became a monk and then bishop of Tours in Roman Gaul, and kept living as a monk once he was bishop.
- **What happened:** He shared his cloak, asked to leave the army as "Christ's soldier", founded a monastery, tore down temples (and was resisted and hurt), begged at Trier that no blood be shed over Priscillian, and yielded once, sharing communion for a day to save lives but refusing to sign.
- **Why the connection matters:** His monks became bishops, Sulpicius's Life carried him abroad, kings honored his tomb, and two centuries later Gregory used his yielding at Trier to warn bishops who were silent before a king.

All three lines come clear from one hearing.

## Verdict: REVISE

One blocking finding, in a sentence the fix changed.

## Fix-list items

| Item | Made? | Check |
|---|---|---|
| MUST: temples and the sacred pine, in Sulpicius's voice | Yes | NP11 1244–1248, 1296–1298, 1319–1323, 1365–1369; HALM 6792–6795, 6860–6861, 6895–6897, 6954–6958. Told plainly and credited to Sulpicius ("Sulpicius tells", "he says"). The falling-pine wonder stays out. The near-total conversion claim is not carried. Matches the outline's Do not say. |
| "though he refused to sign it" | Yes | NP11 5193–5198; HALM 11909–11910. |
| Last paragraphs in time order; Paris setup | Order yes. Setup made, but wrong (B1) | Funeral and Life, then the church and Clovis, then Paris. No years added; neither 507 nor 577 is on the source sheet, so leaving them out is right. |
| Setting: one place, one century; plain word for Caesar | Yes | "in Roman Gaul in the fourth century" (S3, S4). "the Roman commander Julian" (L4: "the commander he asked for discharge"). |
| "it was said": name the witness | Yes | NP11 2491–2495, HALM 8333 ("dicuntur"); absence from Ep. III, NP11 2362–2366. |
| Do not end on Maximus's fall | Yes | The retribution stays in Gregory's voice, and the last words are now Martin's act and its reason. |
| Card: chronology problem | Yes | See Card below. |

Nothing outside the fix list changed except the witness line, which the across-the-set rule asks for. No uncertainty tags; one "in what is now" (Hungary).

## Findings

### B1. BLOCKING: the bishops feared the queen, not "the fury of King Chilperic"

The new setup reads: "At a council in Paris, the bishops sat silent before the fury of King Chilperic."

That is not what Gregory says. The king had left ("The king returned to his lodging", GT 5785–5786). The bishops stayed silent because "they feared the fury of the queen at whose instance this was being done" (GT 5794–5795; Latin "Timebant enim reginae furorem", arndt-krusch 16694). Gregory then urged them to give the king counsel "not to burst out in fury at God's servant" (GT 5798–5799). The king's fury was what Gregory feared might come. It is not what the bishops sat silent before. The released text's "an angry king" was loose. The fix makes it a named, specific claim the source does not hold. The fix list asked for "a one-clause setup", and the trial gives one (GT 5755–5760: Chilperic had Praetextatus, bishop of Rouen, held "until he should be heard by the bishops").

Change the last paragraph to:

> At a council in Paris, where King Chilperic had put a bishop on trial, the other bishops sat silent. Gregory, bishop of Tours almost two hundred years later, warned them that the judgment of the eternal King had pursued Maximus until he lost his throne and his life. Maximus had forced Martin to yield, he said, and Martin gave way to free the condemned from death.

This also cuts "only" from the last sentence. Gregory's "quo facilius addictos morte liberaret" ("in order the more easily to free the condemned", GT 5815–5817) states a purpose, not the sole one (Second_Readings 9). On its own that would be MINOR. It goes in the same edit.

### M1. MINOR: length (writer's question)

519 words. That is 15% over the outline's 450 and about 3 minutes 47 seconds at Daniel's 137 words a minute, past the Standard's "up to three for a major figure". I judge it does not cause a one-hearing failure. The added temples paragraph is required material (MUST). Every paragraph is one scene, and the paragraphs now run in time order. The afterlife is three short paragraphs, and only the Paris one is dense, which B1's setup clause helps. The length is a cost to the listener, not a failure of the test. So it is not blocking.

If Mark or the listener read wants it nearer the outline, the fix list allows one cut: drop the whole Paris paragraph (about 65 words, to about 455). The piece then ends on Clovis and Martin's lands. That loses Gregory, a link on the tree, and the outline's DEFENDED afterlife (I4), though Q2 at Trier still carries the principle. I recommend keeping Paris with B1's wording. The choice is the listener read's, not this recheck's.

## Second readings (appended to `Second_Readings.md` under "Release 50 fixes")

| # | Text | Verdict |
|---|---|---|
| 3 | temples torn down, churches or monasteries built | same |
| 4 | the pine; "the local people rose against him" | minor |
| 5 | driven off and hurt | same |
| 6 | preaching moved them to pull down their own temples | same |
| 7 | pressed to confirm in writing; refused | same |
| 8 | Sulpicius, not there, heard of almost two thousand monks | same |
| 9 | Gregory's warning and Martin's yielding | minor ("only": fixed by B1) |

No quotation was added or changed; Q1 and Q2 are as before.

## Card

One line added to `uncertain`: "The two writers' years do not fit together. Gregory puts Martin's birth in the eleventh year of Constantine's reign. Sulpicius has him sworn in at fifteen, baptized at twenty and out of Julian's army about two years later. Gregory's birth year would make him much older than that when he left the army."

Sourced: D1; GT 1414–1416 (opened: "In the eleventh year of his reign ... Martin was born"); NP11 726, 807, 815–816, 836–842. Minimal: one entry, no other field moved. It gives no birth year and no age, as D1 requires. It sits next to "Sulpicius gives no years…" and does not repeat it. Passes.

## Score

`python -m engine.m1.profile_readability`: 519 words, grade 8.0 (names out 7.1), reading ease names out 73.6, 16.7 words a sentence, longest sentence 29 words: pass. B1's wording adds about four words and keeps every sentence under 30.

## Applied (coordinator, 2026-11-17)
B1 applied, with the reason for the silence kept from the source: "At a council in Paris, where King Chilperic had put a bishop on trial, the other bishops sat silent, fearing the queen's fury." Gregory: "For they feared the fury of the queen at whose instance this was being done" (Brehaut 5794–5795). "only" dropped as advised.
