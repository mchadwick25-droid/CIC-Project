# World Icon Family Review — IC-9 · V1.0

**Date:** 2026-07-18 (overnight) · **What this is:** the full-family review the spec's §7d
required before any final lock — run across all five locked icons *as a set*: frame
consistency, silhouette family, object legibility, appearance-flag audit, skin-tone
spread, and template/ground compatibility. Method: measured from the master SVGs (grep on
geometry and hex values, not eyeballing) plus the approved side-by-side mockups.
**Verdict up front: the family PASSES as a set — every check green, two findings fixed
in-pass, three watch items flagged for Mark (none blocking).**

Masters reviewed: `World-Icons/house-churches.svg` (Chloe V1.8) · `desert.svg` (Papnoute
V0.7) · `alexandria.svg` (Theon V0.8) · `syriac.svg` (Mar Yausep V0.2) · `bethlehem.svg`
(Albina V0.5). Locked bases: all six present in `_working-base/` (incl. Chloe's v1.7
history copy).

---

## 1. Frame consistency — PASS (measured)

All five masters share `viewBox="-15 15 150 150"` exactly. Four share the byte-identical
round-dome silhouette path (`M18 150 Q16 96 40 84 …`); Papnoute's koukoulion dome is the
one deliberate variant (`Q14 98 34 86 …`) with the **same bounding box** (x18–102,
crown y30, base y150) — the variance is his cowl, not his frame. In the approved
side-by-side mockups all five sit at identical visual weight.

## 2. Silhouette family & gender read — PASS

Two women, three men, all connected busts (no detached heads — the anti-ghost lesson
holds everywhere): Chloe forward-veiled + white under-veil; Albina veil drawn back over
grey side-parted hair + softened neckline (`#8F805E`) — the two women read as different
people, not variants; Papnoute cowled/grey-bearded; Yausep dark-haired/dark-bearded;
Theon grey-fringed/clean-shaven. No two figures share a differentiating feature set.

## 3. The objects — PASS, one watch item

Five distinct objects, five distinct silhouettes, each verified against its world's own
record before drawing: **cup** (Chloe) · **cracked jug** (Papnoute) · **open scroll with
rods** (Theon) · **closed Gospel book** (Yausep) · **wax tablet + stylus** (Albina). No
two read alike at 128px or at template scale.
- **Watch item W1 (observation only — Chloe is FINAL):** the cup is the set's only
  pure-ink object (`#2A2521` fill; every other object carries a material tone). At small
  sizes it can read as a dark shape rather than a vessel. Nothing to do now; if Mark ever
  wants a pass, a muted clay/pewter tone is a one-value change — his call, not
  recommended unprompted since Chloe is approved "on all accounts."

## 4. Appearance-flag audit — PASS after two in-pass fixes

Every master must carry its honesty flags (DOCUMENTED / INFERENCE / SILENT) and its true
lock status in its own file comment. Found and **fixed during this review**:
- **F1:** `desert.svg` lacked the INFERENCE keyword (its appearance reasoning was present
  but not in the audit vocabulary) and carried no lock marker — both added, matching the
  spec §7d record.
- **F2:** `alexandria.svg` still said **DRAFT** and `syriac.svg` literally said **"NOT
  LOCKED"** in-file, though both locks are real (spec §7d + base copies). Headers
  corrected to LOCKED with Mark's approval date and base-copy pointer.
All five now read consistently: flags present, lock status true, spec §7d named as
governing. (Chloe and Albina were already correct.)

## 5. Skin-tone spread — PASS (measured)

The set's complexions form a strictly monotonic light→deep ladder, grounded by setting,
no two values within ~10 units of each other per channel:

| | hex | grounding |
|---|---|---|
| Albina · Rome/Bethlehem | `#E5C6A0` | Roman matron (inference, pale end) |
| Chloe · Greek East | `#D8B184` | Asia-Minor olive (Option A, Mark) |
| Theon · Alexandria | `#CDA478` | cosmopolitan Mediterranean |
| Mar Yausep · Syriac | `#B58A5A` | Levantine olive (Option 3, Mark) |
| Papnoute · Desert | `#A97B4A` | sun-weathered N-African (Mark) |

No accidental ties (the earlier Chloe≈Albina tie was fixed by Chloe V1.8). Every value
remains flagged INFERENCE on documented setting; the demographic-reference artifact stays
the future formal authority.

## 6. Template & ground compatibility — PASS

All five drop into the §1b templates at 128px with objects clear of the wooden edge
(verified live on the approved mockups for Chloe/Papnoute/Theon; Yausep/Albina share the
same bbox so the geometry holds by construction — **W2, watch item:** the two Era-2
figures haven't yet been *seen* seated on the actual table mockup; one render when the
graphics pass resumes). Garment tones hold contrast on both era grounds (darkest garment
`#3A2E22` vs. lightest ground `#EDDEB9`; lightest garment `#EDE4CE` vs. its outline
carries the separation). Nameplate inversion works against every garment color.

## 7. Standing deferreds (unchanged by this review)

Jug clay-tint polish · world-tint vs role-pigment reconciliation (branding thread, spec
§8) · the warm-cream reading surface DRAFT (§1b) · **W3, watch item:** the five world
manifest colors (`#b79bf5 #5fd6be #e5c689? #eab06b #f38ec0`) — Theon's manifest color is
still unassigned in the map's color system; needed before his seat dot/map band can
render (owner: World-Map thread, rides SB-5).

---

**Verdict: FAMILY PASSES.** All five locked icons hold as one family — frame, silhouette,
objects, flags, skin spread, template fit. Two findings fixed in-pass (F1–F2), three
watch items for daylight (W1 cup tone — observation only · W2 Era-2 figures on the live
table render · W3 Theon's manifest color). IC-9 is complete; the "pending full-family
review" condition on the five locks is **satisfied** — the locks stand.

*Recorded by the UX Design thread's overnight pass; logged in the UX decision log; spec
§7d updated; Hub tracking synced.*
