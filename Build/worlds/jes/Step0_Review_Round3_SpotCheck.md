Simulated review — informational only, not an Article 31 substitute.

# Step 0 (Society of Jesus): bounded spot-check of the Round 3 correction

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** correction worker, commit db705b7d8 (commit trailer reads "Claude Sonnet 5.5")
- **Round:** 3 (the bounded spot-check that closes the Round 3 Disposition's option 1; a bounded spot-check under the project lead's direction (option 1 of the Round 3 Disposition: S1 and m1–m3 only). This is not a new revision round and does not count toward the three-round cap)
- **Truncation check, method 1:** structural count. Headings §0 to §6 are all present, in order (lines 9, 13, 17, 49, 83, 92, 96). §4 items 1 to 6 are all present. The file ends on a complete sentence ("… once approved to proceed.") and a newline.
- **Truncation check, method 2:** byte and hash comparison. `wc -c` equals `git cat-file -s HEAD:<path>` (20,041 bytes). `git hash-object` equals `git rev-parse` of the blob at HEAD 3d8dd7139 and at db705b7d8 (e4413e31…). The file has no uncommitted changes. The generated `cic/corpus-map/the-society-of-jesus.yaml` also matches its HEAD blob (90386d9c…).
- **Date:** 2026-09-30
- **Documents:** `Build/World-Builds/Society-of-Jesus/Step0_Movement_Scope_Confirmation.md`; `cic/corpus-map/_staging/` (Ignatius v22, Lainez v1, Nadal v1); `cic/corpus-map/the-society-of-jesus.yaml`, as changed in db705b7d8
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Clear.** 0 P0, 0 P1, 2 P2.

S1 is fixed. Every date claim about institutional voice matches the title pages of the vendored files. The minor findings m1, m2 and m3 are fixed. The corpus-map edits are true to the files, and the merge check passes. The Status line and §6 no longer claim an independent check that was not on record.

Nothing in the changed lines misstates the historical world or invents a source. Neither P2 blocks. Moving the Status line to "Approved to proceed" is for the drafter to record under the project lead's option 1; this spot-check does not assign it.

## Check 1: S1, institutional voice against the title pages

| Claim in the document | File | Title page reads | Holds |
|---|---|---|---|
| Lainez, Tomus I, 1536–1556, ends before his generalate | `lainez_epistolae-et-acta-v1-lat_1912.txt` | `TOMUS  PRIMUS` l. 77, `1536-1556` l. 79, Madrid 1912 | Yes |
| Polanco *Chronicon*, Tomus V, 1555 only, printed 1897 | `polanco_chronicon-v1-lat_1894.txt` | `TOMUS   QUINTUS` l. 111, `(1555)`, `«897`; body opens `ANNUS    1555.` | Yes |
| Nadal letters, Tomus I, 1546–1562 | `nadal_epistolae-v1-lat_1898.txt` | `TOMUS    I  — (1546-1562)` l. 54; `TOMUS   PRIMUS` l. 89, `(1546-1562)` | Yes |
| Salmeron, Tomus Primus 1536–1565 (1906) | `salmeron_epistolae-v2-lat_1906.txt` | `TOMUS  PRIMUS` l. 128, `1536-1565`, `1906` | Yes |
| Salmeron, Tomus Secundus 1565–1585 (1907) | `salmeron_epistolae-v3-lat_1906.txt` | `TOMUS  SECUNDUS` l. 161, `1907` l. 173 | Yes |
| Nothing vendored in the voice of Lainez, Borgia or Mercurian as General | `cic/texts/` listing | No file by Borgia or Mercurian. The only Lainez file is Tomus I (above). The 19 Jesuit files match the 19 `work:` rows of the corpus-map. | Yes |

So "dense to 1556, partial to 1562 via Nadal, a Salmeron thread to 1585" holds. B1, B2, B5, the Tier paragraph and §4 item 5 all state it the same way. The dates of the Generals (Lainez 1558–65, Borgia 1565–72, Mercurian 1573–80) agree with the standard record. No vendored file states them.

## Check 2: m1, m2, m3

- **m1.** A search for "previous", "up from", "added since", "now ", "no longer", "not ten" and "despite its title" finds nothing in the body. "Revision 3" appears only as status metadata, which Round 3 accepted.
- **m2.** Ignatius is "Tomus I … volume 22 of the MHSI series". The title page reads `TOMUS PRIMUS` (l. 56), Series Prima, 1903. The title page prints no series number; "22" rests on the archive item ID `monumentaignatia0022igna` and the header. Salmeron is Tomus Primus and Tomus Secundus, and Polanco Tomus V; both labels match their title pages. The filename mismatch (`v2`/`v3`, `v1`) is stated plainly.
- **m3.** The Tier paragraph says "three remaining conditions" and names three: second-witness status, no PD English Constitutions, and scale. That is accurate.

## Check 3: corpus-map

The three `locus` fields match the title pages above. The Lainez note's added clause ("this first tomus covers 1536-1556, before his own generalate began in 1558") is true to the file. The generated YAML carries the same values. `python cic/engine/corpus_map_merge.py --check` exits 0 (883 works, 1,277 assignments, 69 entries). `tools/check_live_commentary.py --surface cic-corpus-map --base db705b7d8~1` reports 0 hits.

## Check 4: other changed lines

No other claim in the changed lines is wrong, unsupported or invented. The word total (3,370,675) and the count of 19 works are unchanged from the reviewed text.

## Check 5: Status line and §6

The Status line now reads "Reviewed at Revision 3 … independent spot-check pending. Not yet approved to proceed." §6 reads "bounded correction applied; independent spot-check pending." Neither claims a check that was not on record. The project lead's option 1 is recorded in `Build/Ministry/Operations/Audits/SocietyOfJesus_Step0_Correction_2026-09-30.md`.

## Findings

**P2-1. §4 item 5 and B2: Ignatius named among the sources that are "dense to 1556".** Ignatius's own vendored letters stop well before 1556. The Latin Tomus I ends at `EPIST. 235.—EXEUNTE ANNO 1547`, and the English selection covers 1524–1547. The claim "dense to 1556" still holds through Lainez Tomus I and Polanco Tomus V. But Ignatius's own voice in hand does not reach his death. A clause such as "Ignatius's letters to 1547" would make this exact. Round 3 used the same wording, so this is polish only.

**P2-2. Lainez corpus-map note: older change history left in a canonical file that this commit edited.** The note still opens with "Corrects a prior dossier 'genuinely closed' verdict, which only checked for an English translation". That is change history, not a description of the work. The project rule says an edit to a live file also removes the commentary already in it. The checker does not flag this sentence. It is the same class as Round 3's L3, so it goes to the Library thread's owner.

## Outside this scope, noted only

- §5 "Process findings for System Hub" is process narration inside a canonical file. It should move to `Build/Ministry/`.
- The Jesuit Source Readiness Dossier is stale against the corrected volume labels.
- Commit db705b7d8 also carries the move of the Hussite Step 0 files to `Build/worlds/hus/`, with a content change in that Step 0 (76% similarity). That work is outside this spot-check and was not reviewed.

## Disposition

Approved to proceed (Step 0 only; not Frozen). Self-disposed by the Library thread after this spot-check, per the project lead's option 1; the reviewer set no disposition.
