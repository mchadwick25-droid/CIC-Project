# Desert Monasticism (Papnoute) prose flags

One escalation. Mechanically fixed without asking: dash-fragment voices,
Syncletica→Sarah swap, stale "(disclosed on its tile)" pointer, Story/Legacy
paragraph splitting, tile depth, Jacob-style contested-claim hedges — see the
shipping commit for the full list. Render verified clean (320/390/1280/1440,
both themes, 0 console errors, both JSON payloads parse).

## Q1 · desert-monasticism / alexandria-catechetical · relationsSummary · class (E) naming/identity, cross-world consistency

Desert's own shipped `relationsSummary` read "Child of Alexandria's milieu;
parent of all later monasticism" before this pass. Desert's own canonical
record, `desert.contested.alexandria-continuity`, exists specifically to test
that exact claim — it states the claim ("Desert monastic formation belongs to
Alexandria's own formation ecology as its intensified continuation") and then
weighs four `held_against` points against it (a founding act with no
constitutive origin in Alexandria's institutions; sharply diverging geography,
social structure, and transmission medium; a documented contrast in
scriptural-engagement mode; Alexandria's own episcopal authority arriving only
late and externally, via the Origenist controversy) before reaching: "This is
a distinct-world reading, not a flat denial of any relationship at all." The
only thing conceded is narrow and itself disputed — one contested reading of
Antony's own Letters (Rubenson's) that raises, without settling, a question of
conceptual affinity.

I rewrote Desert's own `relationsSummary` to match Desert's own canonical
record (now: "A distinct formation world from Alexandria's own, not its
continuation — though one disputed reading of its founder's letters leaves
the question of contact open; parent of monastic life across the wider
Christian world"). That part is a fix-it-yourself call — the record already
decides it, per the same discipline that governed everything else in this
pass.

**What I did not touch, and am flagging instead:** Alexandria's own shipped
`relationsSummary` (from the earlier Alexandria pass, not this one) reads
"Influenced Desert Monasticism directly; scholarship parent of the Bethlehem
Circle." "Directly" is stronger than what Desert's own canonical record — the
one built specifically to test this exact cross-world claim — actually
supports. The two worlds' shipped text now disagree with each other about the
same relationship, and Desert's side is the one with a dedicated
contested_claim record behind it.

Options:
1. **(Recommended)** Soften Alexandria's "Influenced Desert Monasticism
   directly" to something that doesn't overstate past what Desert's own
   record concedes — e.g. "A contested influence on Desert Monasticism, real
   at one disputed point and denied as a general continuation; scholarship
   parent of the Bethlehem Circle." Small, surgical, leaves everything else
   on Alexandria's entry alone.
2. Leave Alexandria's text as shipped and treat Desert's own record as the
   more careful, later-built account that simply supersedes an earlier,
   looser claim made before this record existed — accept the inconsistency
   as a known artifact of build order rather than fix it.
3. Revisit both worlds' `relationsSummary` fields together in one pass,
   in case there are other cross-world relationship claims (e.g. Alexandria's
   own "parent of the Bethlehem Circle") that deserve the same check.

**Default if unanswered:** ship with Desert's own corrected text (already
done) and leave Alexandria's untouched (option 2) — the weakest-claim option,
since editing a different world's already-shipped, exemplar-status text is a
bigger action than this pass's own assigned scope, and no participant-facing
harm comes from leaving a soft overstatement on one entry while the other now
states the honest position.

Sources: `records/desert/contested_claim/desert.contested.alexandria-continuity.md`
(the full weighing); `records/desert/contested_claim/desert.contested.antony-literacy.md`
(the Rubenson/Letters thread the one live concession rests on);
`cic-website/atlas-v3.html`, alexandria-catechetical entry's own
`relationsSummary` field (unedited by this pass).
