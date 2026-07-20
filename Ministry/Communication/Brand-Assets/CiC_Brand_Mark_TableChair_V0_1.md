# CiC Brand Mark — the table with one chair pulled out · V0.1

**Status: RECLASSIFIED (Mark, 2026-07-18) — companion illustration, not the brand
mark.** Mark's ruling, after the cross-thread mark conflict was surfaced:
*"arriving is the brand logo, and should be the primary."* The brand logo and
primary mark — including favicon/app-icon — is **"Arriving"** (the C-as-table
with the madder dot at the threshold; see
`Ministry/Technology/CiC_Logo_and_Motion_Brief_V1_0.md`). This table-and-chair
glyph survives as a **companion illustration**: empty states, tour art, print
corners, wherever "a chair pulled out for you" deserves a picture. It is never
presented as the logo and never occupies the favicon slot. The construction,
files, and craft below remain valid for that illustration role. (Original status:
executed 2026-07-18 by the Full UX Design thread, art awaiting Mark's eye — that
review now applies to it as illustration.)

## The idea

The protected hook made visible: *"…One table. A chair pulled out for you."* Six
strokes total. The table is iron-gall ink — the fixed thing, the record. The chair is
madder red — the action color, the system's one standing invitation — set apart from
the table by a deliberate gap: pulled out, not tucked in. Nothing else. No cross, no
circuitry, no speech bubble (all refused by the Kit).

## Files

| File | Use |
|---|---|
| `CiC_Mark_TableChair_Favicon.svg` | **The favicon/app-icon master** — parchment tile (`#F7F3EB`, radius 7/32), works on light and dark browser chrome. Rasterize from this for `favicon.ico` (16/32/48), `apple-touch-icon` (180), and PWA icons (192/512). |
| `CiC_Mark_TableChair_OnLight.svg` | Transparent, for parchment/light surfaces (documents, letterhead corner, the map/tour artifacts' light register). |
| `CiC_Mark_TableChair_OnDark.svg` | Transparent, strokes lifted to the design system's dark tokens (`#EDE5D6` / `#CB6E52`), for the map/tour "old leather" register. |

## Construction (viewBox 0 0 32, stroke 2.8, round caps)

- **Table (iron-gall `#2A2521`):** top `M3.5 13 h12`; legs `M6 13 v12` and
  `M13.5 13 v12`.
- **Chair (madder `#A13E2B`):** back `M27 8 v17` (taller than the table — a chair
  for a person, not furniture in scale); seat `M27 17 h-6`; front leg `M21.5 17 v8`.
- **The gap** between table edge (x 15.5) and seat front (x 21) is 5.5 units —
  the "pulled out" reading. Do not close it; do not tuck the chair under the table.

## Usage rules

1. **The wordmark remains primary.** The mark never replaces "Church in
   Conversation" where there is room for words; it is for favicon, app icon, and
   tight-corner use only (the Kit: typographic wordmark, "no pictorial logo needed").
2. **Colors are fixed** to the design-system tokens above. Never recolored per world,
   never gradiented, never given the AI-tech treatment.
3. **Minimum size 16px.** Below that, use nothing.
4. **Clear space:** one chair-back height (17/32 of the mark) on all sides when
   placed near other elements.
5. The chair is always **madder** and always **one** — the color and the count are
   the meaning (the action accent = the standing invitation; one chair = *a* chair
   pulled out for *you*).

## Motion (added at Mark's direction, 2026-07-18: "the same concept of motion, the chair being pulled in")

**The sequence:** the table first — the record, already there — then the chair is
**pulled up** from off-right, decelerating with a hair of momentum past the mark,
settling at the decided 5.5-unit gap. Once, then stillness. Reference
implementation: `CiC_Mark_TableChair_Motion_Reference.html` (pure CSS, one
keyframe, reduced-motion static).

**The pairing with the logo's motion, named:** in the logo, the *guest* is first
and the table is built for them; in the illustration, the *table* is first and
the chair is pulled up for the guest. Same hospitality, told from its two sides.

**Binding rules:** the pull always stops at the gap — pulled out for the guest,
never tucked under (the gap is the meaning) · **the chair does not breathe** —
the logo's madder element is the guest (alive); this one is the invitation
(furniture, still) · once per surface, never replays unbidden, never pulses ·
`prefers-reduced-motion` gets the completed still illustration · never plays
adjacent to the logo's motion in one view — the adjacency guard extends to
motion.

## Next

- ~~Mark confirms the art~~ **APPROVED — Mark, 2026-07-18** (with the motion; the
  illustration set is final).
- Rasterization to `.ico`/`.png` sizes and wiring into `cic-poc` belong to the build
  thread (Increment 1 rides fine). Where the motion plays (empty states, tour
  intro) is the Full UX Design thread's placement call.
