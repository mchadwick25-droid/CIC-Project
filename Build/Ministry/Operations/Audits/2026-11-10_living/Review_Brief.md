# P2-V review brief: adversarial review of the living-flag decisions

You are the adversarial reviewer (Opus) for P2-V, the Church Family Tree's check of every living
flag. Read first: `Research_Brief.md` in this folder (the rule the researchers applied), the frozen
Addendum it names (§1, R2 to R5), and the definition below. Then review `decisions_draft.json`.

## The definition (what the method page will say)

The mark means the tradition the entry names is alive today, in 2026. It belongs to the tradition,
not the entry's dates. An episode (a revival, a reform, one period of a church) is living when the
wider tradition it belongs to is alive. Surviving ideas are not enough: a school, a party or a sect
whose own community ended is not living. A later group taking an old name is not an heir without a
record of an unbroken community. Decline is not an ending; an end needs a recorded terminus. Each
mark rests on dated evidence, graded CD or CR. Disputed descent gets a confidence grade.

## The consistency rule (apply it across all batches; the researchers did not all draw it the same way)

Classify each entry by **what kind of thing it names**:

1. **A church, or one period of a church, in a place** (the Roman church in the third century; the
   Carolingian church; Armenian Christianity after Avarayr). Living when *that church's community
   in that place* continues to today, through later entries or a present-day body. Ended when that
   local community ended (North Africa's Latin church, Nubia, Caucasian Albania) even though the
   wider communion lives on. Where more than one present-day body claims it, grade the descent.
2. **A religious order, rule or community of vowed life** (Benedictines, Cistercians, Carmelites,
   Hospitallers). Living when the order exists today. Ended on a recorded end (suppression with no
   restoration, death of the last member).
3. **A movement, revival or reform inside a church** (Oxford Movement, Kollyvades, Second Great
   Awakening). Living as an episode when the tradition it belongs to is alive (G-5 (a) practice),
   with that tradition's carrier named.
4. **A school, circle of writers, or party in a controversy** (the Greek apologists, the
   Alexandrian catechetical school, Pelagians, the Quietist controversy). Not living ("influence")
   unless the entry itself names a continuing community and the record shows it. Where an entry
   reads as both a school and a local church (Cappadocian Christianity, the Church of Aquileia,
   the Anatolian church), decide by its own text: what it says it is about.
5. **A sect or separate body** (Montanists, Cathars, Shakers, Christadelphians). Living when the
   body exists today; ended on a recorded end.

## What to check, entry by entry

- **Consistency** under the rule above, across batches. List every entry whose verdict or class
  differs from how a like entry was decided elsewhere. Say which way it should go and why.
- **Never invent**: every `basis` claim must rest on the entry's own census text, a cited evidence
  item, or a tree link. Flag any fact in `basis` that rests on nothing (a date, a merger, a
  population exchange, a successor body) the evidence and the entry do not show.
- **R3 grades**: CD needs a *verified independent* source that is not journalism alone. A news
  report alone gives CR. Check each CD. `evidenceItems[].verified` is true only where the quote was
  found in both the saved page and a fresh fetch (`research/quote_check.json`).
- **R2 dates**: an item must carry its own date of 2011 or later. A rotating home page is weak;
  flag one used as the only item.
- **R4**: `basis` describes records and texts, never people's beliefs.
- **Descent grades**: present where descent is disputed, absent where it is plain, on the five
  levels. The line entries (`group: "line"`) copy the weakest "continued as" link on their line;
  say whether that reads honestly.
- **Ends**: a "not living" verdict on a currently-true flag (`outcome: "dropped"`) needs a recorded
  end in the entry's own text or a dated source. Decline is not enough.
- **Carriers**: a carrier must be the entry that actually carries the same tradition, not merely a
  living neighbour in the same lane.
- **Readability** of `basis` (it goes into the public data file): short sentences, active voice,
  plain words, nothing past 25 words, no AI tells, no atlas IDs, no "census", "edge" or "grade".
- **Limits**: nothing here may add or retire an entry or change dates. If a fix would need that,
  name it as a change order, do not propose it as a fix.

A finding is **substantial** only when something is wrong, unsupported or misleading. "Could be
stronger" is not a finding.

## Output

Write `reviews/Opus_Review_Round1.json`: `{ "verdict": "approve" | "revise", "summary": "...",
"findings": [ { "id": "...", "atlasId": "...", "severity": "substantial" | "cosmetic",
"problem": "...", "fix": { field: new value, ... } } ], "changeOrders": [ ... ] }`. A `fix` gives
the exact new values for the decision's fields (`verdict`, `group`, `carrier`, `descentConfidence`,
`basis`, `grade` and so on), so a reviser can apply it without judgment. Do not edit
`decisions_draft.json` itself.
