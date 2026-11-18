# Card check: Cyril and Methodius

**Verdict: FIX** (eight references).

Base: `Build/Ministry/Operations/Audits/2026-11-17_varied-batch/cyril-and-methodius/cyril-and-methodius.card.json`. There is no census entry.

## 1. Edits justified

Each edit checks against its evidence. Re-read: VC 20224-20228, 20307-20308, 20408; VM (GZ) 12201-12215, 12250-12256, 12540-12552; CONV (GZ) 13641-13642, 13662-13663; J8 (GZ) 13797-13809, 13974-13977; PG 96729-96746, 98396-98397, 98428-98429, 98681-98682, 99371-99372; LUT 1297-1302.

## 2. Nothing else moved

Confirmed.
- `dates` and `place` are identical to `datesNote` and `placeNote`.
- The first four `sources.about` items are identical.
- `name`, `tradition` and `briefLength` are dropped. They are not card keys, and the card now fits CARD_KEYS.
- All other fields are word for word.

## 3. References

The edit list's "Left alone" section is overruled by rule 3. Kept, because each grounds the brief's wording:
- "862, for the 860s".
- "Theophylact's name", for "or more later" (Source_Sheet D2).

| Field | Old text | New text |
|---|---|---|
| `briefReferences[0]` | `the letters made after prayer.` | `the letters made.` |
| `briefReferences[4]` | `Life of Constantine, lines 20379–20445: Rome, the pope comes out to meet them with Clement's relics; his illness; the monk's name Cyril; his death on 14 February, aged 42.` | `Life of Constantine, lines 20379–20445: Rome; his illness; the monk's name Cyril; his death.` |
| `briefReferences[5]` | `Methodius bishop for Pannonia; held two and a half years in Swabia.` | `Methodius bishop; held two and a half years.` |
| `briefReferences[7]` | `the earlier ban on Slavonic Mass repeated, with preaching in Slavonic still allowed.` | `the earlier ban on Slavonic Mass repeated.` |
| `briefReferences[8]` | `Svatopluk: the Slavonic letters found by Constantine, Slavonic Mass allowed,` | `Svatopluk: Slavonic Mass allowed,` |
| `briefReferences[9]` | `lines 12540–12551; his death on 6 April; the funeral` … `(Latin extract in Ginzel): Wiching set up, the disciples driven out.` | `lines 12540–12551; his death; the funeral` … `(Latin extract in Ginzel): the disciples driven out.` |
| `briefReferences[10]` | `Clement \"the first bishop of the Bulgarian tongue\"; the plain sermons.` | `Clement \"the first bishop of the Bulgarian tongue\".` |
| `briefReferences[13]` | `found in Rus and among the Danube Bulgarians; Cross's` | `found in Rus; Cross's` |

The rest of each entry is unchanged.

## 4. Census rules

Pass.
- Only allowed keys, and no `briefLength`.
- There are eight quoted spans and seven entries. "Greek" and "newly invented Slavic letters" make one run, which the validator accepts.
- Each `printed` stands at its lines, and every cited file is in `sources`.
- The quotation marks in the references are verbatim in the brief.
- No audit is named.
- No entry has a `secondReading` yet. That is expected at step 7.

## 5. Not found, and left in

The edit list has no "not found" claims.

The brief's "ploughing" is British. If the brief changes it to "plowing", `quotationOriginals[3].modern` must follow.
