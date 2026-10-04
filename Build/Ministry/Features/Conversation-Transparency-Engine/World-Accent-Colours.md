# World accent colours and portraits in the app

The participant app shows each seated world with a portrait and an accent colour. Since slice 9 (System Hub decision 47 and Entry 109) both live in the world's registry entry, `records/worlds/<code>.yaml`, under `app`, with the world's place in the world list. GET /api/worlds serves them. This file keeps the reasoning behind each colour, which used to sit as comments in `cic-poc/frontend/src/data/worlds.ts`.

Every accentColor below is a lightened variant of the hue each per-world
comment grounds (kept there for provenance/hue reasoning), raised to
clear WCAG AA against the app's dark background (#17130F) in both of
its actual uses - as text (.turn__speaker, .arrival__seat-detail) and
as a button/swatch fill with dark text on top (.world-card__interview,
.arrival__seat-portrait). Script-computed, not eyeballed: every value
here measures >=5.3:1 as text on the dark ground and >=5.0:1 for dark
surface-text laid on top of it as a fill. Hue and relative saturation
are preserved from each grounding pick, only lightness raised.

Stays distinct from gold-leaf and from --color-representative's own
reserved dark-safe value (#DC9A3E).
**alx**: accent `#DE670B`, portrait `/images/portraits/thumb/alexandria.webp`.

**pahc**: accent `#439975`, portrait `/images/portraits/thumb/house-churches.webp`.

**desert**: accent `#9D893B`, portrait `/images/portraits/thumb/desert.webp`.

**hal**: accent `#B77889`, portrait `/images/portraits/thumb/bethlehem.webp`.

**syr**: accent `#5493A0`, portrait `/images/portraits/thumb/syriac.webp`.

**ijc**: accent `#B67D50`, portrait `/images/portraits/thumb/empire.webp`.

Hue grounded in #A0522D (a warm sienna/terracotta, echoing the loaf's own baked crust) -
checked against every color above and the two reserved semantic tokens (--color-tyrian
#6B3FA0, the lexicon/transparency apparatus's own pigment; --color-participant/"lapis"
#1E40AF) for a distinct hue.
**cappadocian**: accent `#CB7247`, portrait `/images/portraits/thumb/cappadocian.webp`.

Hue grounded in #5A6B74 (a cool slate blue-grey, this world's own repeated
cold-of-Gaul theme) - checked against every color above and the two reserved semantic tokens
for a distinct hue and temperature (per gallic_Representative_Portrait_Grounding_Brief.md).
**gallic**: accent `#798D97`, portrait `/images/portraits/thumb/gallic.webp`.

Hue grounded in #6A2525 (a deep oxblood/martyrdom
red, this world's own martyrs'-graves-read-aloud practice and the Deo laudes
acclamation) - checked against every color above and the two reserved semantic tokens for a
distinct hue; the nearest neighbor is hal's own muted rose, 16 degrees away in hue.
H/S held from the grounding value, L raised to 61.8% - the first point clearing both
thresholds (>=5.3:1 vs the dark ground, >=5.07:1 vs --color-surface #1E1913 as dark
text on top of it as a fill).
**don**: accent `#CD6F6F`, portrait `/images/portraits/thumb/donatism.webp`.

No light-mode-derived hue for this world; computed directly for the
dark ground. Hue/saturation grounded in this world's own repeated austerity/subtraction theme
(the silenced Zurich organ, the plain black gown, worship built around subtraction
rather than ornament - Doc_07 SS5's "subtraction, not addition" formation logic) -
a restrained, cool charcoal-slate (H=240deg), deliberately the fleet's lowest
saturation (12%, below gallic's own 14.9%, the next-quietest) while still reading
as a distinct accent rather than plain grey. Script-computed: L=58.1% is the first
point clearing >=5.0:1 against BOTH the dark ground (5.31:1) and --color-surface as
dark text laid on top of it as a fill (5.01:1) simultaneously - matching don's own
>=5.3:1/>=5.0:1 margin pattern. Checked against every value above and the two
reserved semantic tokens (--color-tyrian #6B3FA0, --color-participant/"lapis"
#1E40AF) for hue distance; nearest neighbor is lapis at 14.1deg, low collision risk
given the near-fourfold saturation gap between them.
**rzg**: accent `#8787A1`, portrait `/images/portraits/thumb/theophilus.webp`.

Reuses the accent color already fixed for this world in
cic-website/table.html rather than picking a new one - #579C40, a moderate forest green.
Verified against this file's own two dark-mode thresholds: 5.49:1 vs the dark
ground #17130F (clears >=5.3:1) and 5.18:1 vs --color-surface #1E1913 as dark text on top of it
as a fill (clears >=5.0:1).
**witt**: accent `#579C40`, portrait `/images/portraits/thumb/nikolaus.webp`.
