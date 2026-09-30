# Society of Jesus Step 0: Bounded Correction, 2026-09-30

**Authority:** the project lead chose option 1 of `Build/World-Builds/Society-of-Jesus/Step0_Review_Round3.md` (Disposition): apply finding S1 and minor findings m1–m3 only, followed by a spot-check limited to those lines. No fourth review round. Not Frozen.
**Status of the document after this pass:** independent spot-check pending. This record does not self-assign "Approved to proceed".

## What was found on entry

The working tree already held part of the correction. The corpus-map row and file headers for Polanco (L1) and Salmeron (L2) already read Tomus V (1555) and Tomus Primus / Tomus Secundus, and B2 already carried the corrected coverage dates. The Status line and §6 nevertheless said "Approved to proceed" and "independently spot-checked". No independent spot-check is on record, so both lines were reset.

## Changes

**`Step0_Movement_Scope_Confirmation.md`**
- S1: B1, B2, B5, the Tier paragraph and §4 item 5 now say institutional voice is dense to 1556, partial to 1562 (Nadal's letters), and a single correspondent's thread (Salmeron) to 1585. They add that nothing vendored gives Lainez's, Borgia's or Mercurian's own voice as General.
- m1: "previously counted", "previously recognized", "up from the ten", "despite its title" and similar removed.
- m2: volume labels use the title pages (Ignatius Tomus I, volume 22 of the MHSI series; Nadal Tomus I, 1546–1562; Lainez Tomus I, 1536–1556).
- m3: the Tier headline now says "three remaining conditions" and lists them.
- Status line and §6 reset to "independent spot-check pending".

**Corpus-map (staging, then `python cic/engine/corpus_map_merge.py`)**
- `locus` fields for Ignatius (v22), Lainez and Nadal Vol. I carry the tomus and date range from the title page. The Lainez note says the volume ends before his generalate. `cic/corpus-map/the-society-of-jesus.yaml` regenerated. L1 and L2 were already correct at source.

## Disagreement between rounds

Round 2 supplied "Lainez (General 1558–65) ... c. 1580" unverified. Re-checked against `cic/texts/lainez_epistolae-et-acta-v1-lat_1912.txt` (title page l. 76–79, "TOMUS PRIMUS 1536-1556"): not supported. Not carried.

## Verified against vendored files

- Lainez l. 77–79: TOMUS PRIMUS 1536-1556.
- Polanco l. 111 and after: TOMUS QUINTUS (1555), body "ANNUS 1555".
- Nadal l. 54 and 89–91: TOMUS I (1546-1562).
- Salmeron v2 l. 128–129: TOMUS PRIMUS 1536-1565, 1906. Salmeron v3 l. 161–164: TOMUS SECUNDUS 1565-1585, 1907.
- Ignatius v22 l. 56: TOMUS PRIMUS, Series Prima, 1903.

## Not verified

- "Volume 22 of the MHSI series" rests on the file's own provenance header, not on the title page.
- Lainez's generalate dates (1558–65) and Borgia's and Mercurian's dates are from Round 3, not from a vendored file.
- Nothing vendored was searched beyond file names and the corpus-map for Borgia, Mercurian or the Jesuit Relations.
- Open gaps OG-1 and OG-2 are in `Build/World-Builds/Society-of-Jesus/Open_Gaps_Tracking.md`.
