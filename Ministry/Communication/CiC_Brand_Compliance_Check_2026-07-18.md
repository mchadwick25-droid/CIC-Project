# Brand & Messaging Compliance Check — 2026-07-18

**By:** the Branding & Messaging thread (Brand Foundations authority). **Method:** read the standard (Vision V1.1; Brand Brief + Kit V0.2 + QuickRef; Logo & Motion Brief; UX Design Brand Brief; the 8 review rulings; both decision logs; prior passes BR-6/BR-7 so nothing already-fixed is re-flagged), then swept each target and inspected the actual SVG source, product source, and corpus copy. **Convention:** VERIFIED = inspected and seen · DECIDED = a settled brand call logged here · APPROVED = Mark's explicit word. **Boundary:** I rule on language and presentation and route fixes to owners; I do not merge code, change world content, or make Constitution/funding calls. Nothing merges before/during P1.

**Verdict up front:** the new World-Icon & Era-Ground set is **strongly compliant** — in the visual-integrity areas that most risk violation (the anti-ghost rule, emblem-not-portrait, world-speaks-for-itself), it is exemplary. The running product and public corpus show **no post-lock drift**. Findings are few and small: one routed brand ruling I now make, one spec-text inconsistency, and three next-touch/surface items. No blockers.

---

## 1. Compliant — confirmed (a compliance check must say what passed)

### World icons (all five: house-churches, desert, alexandria, syriac, bethlehem)

- **VERIFIED — anti-ghost rule (the memory-locked "real people, not ghosts").** Inspected every SVG: **no `<filter>`, no `feGaussianBlur`, no radialGradient glow, no vignette, no `<image>` raster, no figure- or fill-level transparency.** All figure fills are solid opaque hex. The only sub-1.0 values are `stroke-opacity` on hairline *ink detail* lines (a veil fold, a book-spine rule, tablet writing-marks) — ink drawn faintly, never a translucent figure. Spec §0's binding rule ("solid and fully opaque · no glow/halo/aura/bloom · never fade/materialize · speaker shown by a solid printed device, never light") is honored in the art. **PASS.**
- **VERIFIED — emblem, not portrait** (Kit / conviction "the Representative is the world, not a person"): connected-bust line emblem, reduced features (two small eyes, faint nose, softened mouth), manuscript register (iron-gall line + solid world-tint), explicitly "not a likeness." The emblem↔portrait axis is resolved on the emblem side, in writing and in the art. **PASS.**
- **VERIFIED — world speaks for itself / no anachronism / no false authority** (exemplary): Mar Yausep drawn explicitly *not* a bishop (no mitre/cross/cowl); Theon deliberately *not* vested as an ordained priest (a 4th-c.+ anachronism that would miscast a *didaskalos*); Albina kept an honest widow-patron, *not* a Hebrew scholar; desert-father iconography used "as inspiration, **no halo**." Each object was verified against its own world's construction record, with appearance-inference flagged where the record is silent. This is the world-speaks-for-itself conviction, drawn. **PASS.**

### Table templates

- **VERIFIED** — the participant's near edge is a dashed "open place" arc in gold-leaf, the same *"a chair pulled out for you"* gesture as the logo and the landing hero; figures sit solid behind a gold-leaf table. Consistent with the protected hook and the mark. **PASS.**

### Running product (post-BR-7 drift check)

- **VERIFIED** — source scan of `cic-poc` (.tsx/.ts/.py/.html): **zero** "users", zero "The Church in Conversation," zero "I am an AI," zero "I am a [role]," zero "come sit." The BR-7 fixes held; no post-lock drift. **PASS.**

### Public corpus (post-BR-6 drift check)

- **VERIFIED** — landing, FAQ, elevator: the only "come sit"/retired-word hits are in **change-log records** (documenting old→new), not live copy. BR-6 held. **PASS.**

### Era grounds

- **VERIFIED / APPROVED** — the ten era grounds are near-parchment, low-saturation, legible under ink/gold/world-colors in light and dark, forming one warm-past → cool-present flow (Mark-approved on the real timeline). Compliant with the palette discipline and the manuscript-pigment story. **PASS.**

## 2. Findings — ranked by participant visibility

| # | Location | Rule it engages | Finding | Fix | Severity |
|---|---|---|---|---|---|
| C1 | Spec §2 ("world-tint wash fill at ~50% opacity behind the line") | Anti-ghost §0 ("solid fills"); the actual V0.4+ locked assets | **Spec-text inconsistency, not an asset defect.** §2 still describes the retired semi-transparent wash; §0 and every shipped icon use solid fills. The *art* is compliant; the *spec sentence* contradicts it and could mislead the next icon-builder into ghosting a figure. | Edit §2 to "solid world-tint fill" to match §0 and the locked assets. | **should-fix** (doc hygiene; art is correct) |
| C2 | Spec §2.1 tint table + §8.2 — **routed to this thread** | Role-pigment integrity (Review Ruling 6 territory; UX brief role-pigments) | The four world-tints vs the five reserved role-pigments needed a reconciliation. **Ruled below (§3).** One residual: **terracotta `#C6926B` (House-Churches) is the nearest world-tint to gold-leaf `#B45309` (the Representative-voice pigment).** Not a collision in different layers, but confirm they never abut such that a world-tint reads as the role signal. | Adopt the §3 layer-separation ruling; build-time adjacency/contrast check on terracotta-vs-gold-leaf where an icon sits on/near a gold-leaf table element. | **should-fix** |
| C3 | Spec §1a / §1 — camera vs. slideshow still pending | Anti-ghost §0; logo-motion discipline | Not a violation — but the open camera decision must inherit the anti-ghost law whichever way it goes. | Confirm in the spec (already implied): **if the camera stays, it moves over solid figures with a solid speaker marker and zero glow/dimming; if it goes, the composition is simply still.** Mark's call. | **surface for Mark** (next-touch) |
| C4 | World display labels ("The House-Churches," "The Desert," "The Bethlehem Circle") in the spec/hub | Masterbrand rule (no "The") — *scope check* | **Not a violation.** The no-"The" rule governs the **masterbrand** ("Church in Conversation"), not world/content names; world labels may carry "The." Flagged only so the icon captions use the **same** world display names the world-build threads canonically use. | Confirm caption names against the world-build canon at ship; no brand change. | **next-touch** (cross-thread consistency) |

## 3. Ruling made (routed to me by the spec, §2.1/§8.2) — DECIDED

**World-tint vs. role-pigment: layer separation.** The five role-pigments (gold-leaf = Representative voice · lapis = participant · Tyrian = apparatus · graphite = Facilitator · madder = action) are **UI-function signals** — they mean *a role is speaking or acting*. The world-tints (terracotta, dark-habit, slate-teal, plum-mauve, + Alexandria) are **figure-identity fills** — they mean *which world*. They live in different layers and **never both carry meaning in the same element**: a world-tint never signals a UI role, and a role-pigment never tints a figure. So a world-tint sitting *near* gold-leaf is not a collision, the way a photograph's brown coat near a UI's orange button is not a collision. This resolves the reconciliation. **The one build-time guard (C2):** where a terracotta figure meets a gold-leaf table stroke, keep enough value separation that the eye reads *figure* and *furniture*, not one wash — a contrast check at compose time, not a repalette. (This is presentation, within my authority; if Mark wants the House-Churches tint nudged off the gold-leaf family entirely, that is his call, offered not imposed.)

## 4. What is genuinely Mark's (surfaced, not invented)

1. **C3 — the camera-vs-slideshow decision** (the spec recommends dropping it; either way the anti-ghost law binds — my only brand input).
2. **Whether to nudge the House-Churches terracotta** off the gold-leaf family (C2) — offered as optional; the layer-separation ruling already makes it compliant as-is.
3. The spec's own already-open gates (per-world object confirmation vs Source Ecology; figure-register richness; the full-family icon review) — content/construction calls, not brand ones; noted as context.

## 5. Routing

- **C1 (spec text), C3 (camera note)** → the World-Icon spec owner (the UX/visual thread that authored `CiC_World_Icon_and_Table_Template_Spec_V0_1.md`).
- **C2 build-time guard** → the build thread's compose step (Increment-1 seam), as a contrast check; and the §3 ruling folds into the Kit's role-pigment section at next revision.
- **C4** → confirm world display names with the world-build threads at ship.
- **§3 ruling** → recorded here and into the Kit's visual section (next revision).

---

*Logged in `CiC_Messaging_Branding_Kit_Decision_Log.md` under BR-25…BR-28. Nothing here blocks; the icon set is brand-approved in substance, pending Mark's eye on the art (the full-family review the spec already schedules) and the four small routed items above.*
