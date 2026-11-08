# Armenian Apostolic Church, 1650-1815: a new era-8 movement — 2026-11-08

Ruling: Mark, 2026-11-08: "add an era-8 Armenian Apostolic movement". It answers the era 8 links pass's open item "No Armenian Apostolic movement for 1650-1815" (Open-Gaps, 2026-11-08). The era is frozen, so this is a change order on one entry, made on the pattern of the 2026-10-23 change order that split VI.13 (`Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`).

## What changed

- **New movement** `armenian-apostolic-church-era-8` (VII.24a), "Armenian Apostolic Church — Etchmiadzin and Constantinople", 1650-1815, Caucasus lane, Pre-Survey Candidate, Oriental Orthodox. It continues as `armenian-christianity-zartonk`. The letter suffix marks a strand carved out of VII.24, whose own floor note said two churches appeared together there.
- **New Julfa** (`armenian-christianity-new-julfa`): `continuesAs` now names the new movement.
- **The Mekhitarists and the Catholic Patriarchate** (`armenian-christianity-era-8`, VII.24) is now the Armenian Catholic strand: `streams` Eastern Catholic only; a new floor note and teaser; shortName "Armenian Catholics"; `continuesAs` null, as on the Melkite Greek Catholic movement. Its name and other text are unchanged.
- **Seven new links**: New Julfa continued as the new movement (Documented); the new movement continued as the Zartonk (Documented); the new movement and VII.24 broke with each other (Widely Accepted); the new movement argued against VII.24 (Documented, major: by the sultan's law Catholic Armenians still had to obey the patriarch, who could punish them); VII.24 argued against the new movement (Dominant Modern Reconstruction: Avedik's fall, 1703, told only by later Catholic histories); the new movement and the Catholic Church of the period argued against each other (both Documented, minor).
- **One retired link**: era 7's `armenian-christianity-new-julfa--armenian-christianity-era-8` (continued as) rested on the line of Apostolic catholicoi. It is the census's first `retiredLinks` entry, replaced by `armenian-christianity-new-julfa--armenian-apostolic-church-era-8`.
- `meta.totalEntries` 301; Pre-Survey Candidates 220.

## Rounds

1. **Draft** (Opus): `Draft.json`. The movement record, a fact table tying each sentence to a vendored file, lines and quote (94 rows), the neighbor changes and six links.
2. **Review round 1** (separate Opus agent, full review): `Review_Round1.json`. Revise: 0 blocking, 5 substantial, 7 minor. The substantial findings: the prose showed coercion from the Apostolic side only (the Catholic party used the French ambassadors; Avedik was jailed in 1703); Ormanian's "defection" referred to two bishops, not the 1742 approval; VII.24's teaser and `continuesAs` now misrouted the line; and the reverse "argued against" link was missing.
3. **Revision** (Opus): `Revision_Round1.json`. All 12 fixed, 6 differently from the proposal, each with the reason. The reverse link is graded Dominant Modern Reconstruction, not Widely Accepted: its sources are later histories only. The fact table grew to 109 rows.
4. **Review round 2** (separate Opus agent, targeted recheck): `Review_Round2.json`. Pass. All 12 resolved; every departure judged sound; one minor wording fix (the 1860 statute was "drawn up", not in force), applied as written in `Final.json`.

Two of the three-round cap used.

## Checks

- All 137 quotes in the final draft are verbatim at their stated lines (scripted, both rounds).
- Every prose field, note and the outcome scores Reading Ease 60 or more and FK 10 or less with `engine.m7.turn_readability.score_turn`.
- Place IDs (Etchmiadzin, Constantinople, Armenia, Turkey) are copied from existing movements; none invented. The page's Etchmiadzin Cathedral link reuses New Julfa's.
- The outcome passes the major-links test as narrowed: a rule binding a group by the sultan's law, not a text taken up by vote.
- `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`, 0 errors.

## Sources and what is thin

The prose rests on Ormanian (1912), Chamich and Avdall (1827), Issaverdens (1875), Zakaria of Kanaker and Abraham of Crete (Brosset, 1876), Serpos (1783-86), the Jesuit memoir in the same tradition, and Rycaut (1679). Much of the evidence is Catholic-side; the prose names Catholic writers where a story is theirs (Gomidas, Avedik). Wanted (none vendored): the Constantinople patriarchate's own eighteenth-century records; letters or works of the catholicoi, including Simeon of Erevan's; Benedict XIV's 1742 acts; Arakel of Tabriz's Book of History; a contemporary record of Avedik's fall.

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-08): "The Armenian Apostolic movement's library bucket".
