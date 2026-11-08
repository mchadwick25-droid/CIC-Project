# Step 0 — Era 10: A Century of Global Christianity (1906–2010) · re-run as history · V2.0

**Status: draft for Mark's gate. Nothing below changes the census until he rules.** This record
re-runs era 10's Step 0 as history under the change order of 2026-11-08 (Atlas World Map
Decision-Log, "Change order: era 10 becomes history, 1906–2010"). It sits beside the frozen
`CiC_Step0_Era10_V1_0.md`, which stays as it is. Its proposed census edits are in the companion
file `CiC_Step0_Era10_V2_0_Proposed_Edits.json`. Its reviews are the `CiC_Step0_Era10_V2_Review_Round*`
files in this folder.

## Revision log (after Round 1)

Round 1 (`CiC_Step0_Era10_V2_Review_Round1.md`) found seven substantial, nine minor and three
cosmetic defects. Each is answered below, one line each.

- **R1-S1** fixed. Whole-item removals are now structural operations in the JSON (`removeItem`, `retireEntry`), defined in its `_meta` and run after every substring edit: seven stories, four voices, seven source items that document only post-2010 events, and the IX.31 drop. The blanking substring edits are gone. IX.36's Mars Hill story is added.
- **R1-S2** fixed. The Summary, G-13 and a new G-39 list all seven story removals.
- **R1-S3** fixed, as the review gives, with two departures. IX.5: the repo does not pin the year Pew's count describes, so the line says only that the study was published later, in 2011. IX.30's caveat reads "The page states only the dated published record", since it covers a study as well as acts. A widened scan found more of the same kind, fixed the same way (listed under each §2 entry).
- **R1-S4** fixed. The JSON carries D-P7's text; IX.20 Q1 and G-21 name it.
- **R1-S5** fixed. G-4(a) now states the rule the edits follow. Hummel (2023), Bowler (2013) and *Let Them Not Return* (2017) are restored, labeled as later. The IX.30 parenthetical is corrected.
- **R1-S6** fixed by re-classing. D-E2 and D-E3 are skeletons held until a base exists; B2 is "not yet assessable"; D-E2's Tier 1 signal is dropped; D-E3's placeholder `why` sentence is removed. G-31 and G-32 recommend naming them as gaps. No source was added.
- **R1-S7** fixed. G-40 to G-49 carry IX.4 Q1, IX.18 Q1, IX.19 Q1, IX.33 Q1, IX.38 Q1, IX.48 Q1 and X3, plus three the review did not list (IX.29 Q1, IX.44 Q1, D-P8). IX.5 Q1 and IX.30 Q1 are named under G-4. Conditional edits are drafted for IX.19 Q1, IX.33 Q1 and X3.
- **R1-M1** fixed (D-E1 tense and edit-history clauses; D-E6 "2000" to "2010").
- **R1-M2** fixed (IX.18, IX.23, IX.26, IX.29, IX.32 statusDescription and IX.32 floorNote).
- **R1-M3** fixed (§4 and §7 labels renumbered; §5 cross-references to the movements now read §4; file names corrected).
- **R1-M4** fixed (G-15 and §3 agree; one candidate name, with naming as a sub-option; id note; anchors recounted to eight, seven verified).
- **R1-M5** fixed (G-5 header).
- **R1-M6** fixed ([S] marks on NTPG's year and *Simply Christian*, carried into G-10).
- **R1-M7** fixed, with one departure: IX.10 reads "published steadily from then to 2010", not "…and after", because "and after" still reaches past 2010. The repo dates his books to 2012.
- **R1-M8** fixed in part. Every named sentence is split, and 50 others. Sentences over 25 words fall from 45 to 5: three teasers, one quote, and one IX.45 sentence that would lose its meaning if split. Reading Ease rises from 58.0 to 59.6; grade falls from 8.7 to 8.0. More splitting would push the grade below its floor of 8. The gap left is word length (names and terms), not sentence length.
- **R1-M9** fixed (IX.10 confidence note).
- **R1-C1** fixed (drafter voice and assembly residue). **R1-C2** fixed ("every anchor is dated 2015 or later"). **R1-C3** recorded in §3 and D-E6 (`dateNote`).
- **G-6** rewritten to Mark's "What follows 2010" ruling. **§8** added.

**Check after revision.** All 430 substring edits apply exactly once, in order, to a copy of
release 19, and all 19 structural operations match exactly one item. On the era 10 rows left after
the edits, the review's own scan finds 146 hits, down from 238. A widened scan (adding `sourcing` and
story `when`) finds no year after 2010 and no undated present tense, apart from 17 later works
labeled as later and 63 uses that are not claims about today (the noun "current", "contemporary
press", the title *Christianity Today*, past or narrative tense inside a dated story or sentence, and
the page describing its own method).

## 0. What governs this run

- **The window is 1906–2010.** The era opens with Azusa Street (1906) and the Edinburgh missionary
  conference (1910). It closes with the 2010 centenary meetings, Edinburgh 2010 and Lausanne's Cape
  Town congress. The 1906 boundary with era 9 does not move.
- **"Living" means living as of 2010.** A body still active in 2010 ends at 2010. Nothing after
  2010 is claimed.
- **One standard for all ten eras.** Each entry is assessed as eras 1 to 9 were: Section A (the
  floor), Section B's five criteria (B1 Sourcing, B2 Ecology, B3 Uniqueness, B4 User needs, B5
  Scale), a tier, and the five `formation_confidence` grades for contested claims. The per-world
  construction standard does not apply.
- **The Living-Era Protocol Addendum V1.0 is retired for era 10.** Its contemporary-attestation
  grades, open "present" ends and recency floor no longer apply. Its habits of describing
  published texts rather than people, and of dating every statement, still guide the tone.
- **Sources.** Only vendored Library texts and secondary works the repo already cites. Every [S]
  (unverified) flag from the V1.0 research files is carried forward, never upgraded. No vendored
  text in `cic/texts/` is an era 10 primary source; the gaps go to the wanted list (§7).
- **What follows 2010** (Mark's later ruling in the same sitting). The tree says nothing past 2010, and
  the method page and the era 10 band say so in his line: "The tree's history runs to 2010. Movements
  since then will be added as they become history." A body active in 2010 keeps its living mark but
  makes no claim about where it stands today. The line lands with the census changes after the gate (§8).
- **Scope widened in the same sitting.** Mark asked that the survey cover Christian movements and
  trends outside formal church bodies (Bible translation, campus ministries, church planting,
  world missions and their kin). The unit is the movement, never the organization (§4).

**How it was made.** Four Opus drafters worked in parallel: three re-assessed the 49 existing
entries (IX.1–17, IX.18–33, IX.34–49), and one ran the completeness sweep, IX.50, the era record,
the movements and the wanted list. Their drafts were assembled here. A separate Opus 5.5 reviewer
reviews the record (round 1 full, later rounds targeted rechecks, three rounds at most).

## Summary

| | Count |
|---|---|
| Existing entries re-assessed | 49 |
| Kept | 48 |
| Proposed for dropping | 1 (IX.31, Deconstruction: every anchor is dated 2015 or later) |
| End "present" → 2010 | 32 (IX.18's "contemporary" included) |
| Other date changes | 1 (IX.28: c. 1990–2015 → c. 1990–2010) |
| Living as of 2010 | 45 yes · 3 no (IX.6, IX.17, IX.34) · IX.31 n/a. No flag changes from the census; 15 depend on how P2-V defines "living" (G-5) |
| Register edits to participant-facing text | 430 substring edits, each exact and unique in its field as it stands when it runs, applied in sequence without conflict; plus 19 structural operations (18 whole-item removals and the IX.31 drop) |
| New entries drafted | 1 ready for the gate (Iglesia ni Cristo split), plus IX.50 held for Mark's direct ruling |
| Skeletons, not for entry yet | 4 (Bible translation movements; the Anglican Communion in the twentieth century; the independent mission movement; student and campus movements) |
| Movements outside church bodies assessed | 13 groups (§4) |
| Gate questions | 49 (§6) |

**Tiers (V2.0):** Tier 1 (11): IX.1 · IX.4 · IX.5 · IX.6 · IX.11 · IX.23 · IX.24 · IX.33 · IX.34 ·
IX.35 · IX.43. Tier 2 (29): IX.2 · IX.3 · IX.7 · IX.8 · IX.9 · IX.10 · IX.12 · IX.13 · IX.14 ·
IX.19 · IX.20 · IX.21 · IX.22 · IX.27 · IX.29 · IX.30 · IX.32 · IX.36 · IX.37 · IX.38 · IX.39 ·
IX.40 · IX.41 · IX.42 · IX.44 · IX.45 · IX.46 · IX.47 · IX.48. Tier 3 (3): IX.25 · IX.28 · IX.49.
Register (4): IX.15 · IX.16 · IX.17 · IX.26. Label (1): IX.18. Dropped (1): IX.31.
11 + 29 + 3 + 4 + 1 + 1 = 49. No tier changed from V1.0; IX.28's rise to Tier 2 is open (G-9).
The V1.0 candidates IX.33–IX.49 carried tier signals, now stated as tiers.

**Register edits, in summary.** The "dated reading of a living tradition" sentence is removed from
every status where it appears, as in eras 1 to 9. "Today", "still", "now" and present-tense
counts become statements dated to 2010 or earlier. Facts after 2010 come out, and the gap is left
open rather than filled. Facts from 2000–2010 that the record already cites, and that the earlier
2000 cut-off would have removed, stay in. Seven whole stories that fall after 2010 are proposed
for removal: three under G-13 (IX.7, IX.11, IX.16), one under G-11 (IX.36) and three under G-39
(IX.28, IX.30, IX.32). A tradition's own texts and events after 2010 come out. Later outside
scholarship and later inquiries about in-era matters may stay, labeled as later (G-4).

## 1. Survey update and completeness sweep (procedure step 1)

#### 1A. The structural finding: era-9 rows that era 10 never picks up

The era-10 roster takes over only some of the living era-9 rows. A count from the census: **37 living era-9 rows end at the 1906 boundary, and 17 of them have an era-10 successor or a link into era 10. The other 20 have nothing.**

No pick-up at all: VIII.5 Oxford Movement / Anglo-Catholic; VIII.6 Salvation Army; VIII.14–17 (the LDS, JW, Christian Science and Christadelphian register rows; see 1C); VIII.22 Laestadianism; VIII.28 Orthodoxy after 1821 (the Balkan autocephalies); VIII.30 the Victorian Church of England; VIII.31 the Russian Synodal century (IX.22 picks up VIII.11 Optina, not VIII.31); VIII.33 Old Catholics; VIII.34 Methodism; VIII.35 Baptists; VIII.36 Quakerism; VIII.37 Unitarian-Universalist (register); VIII.39 Philippine Catholicism; VIII.41 confessional Lutheranism; VIII.45 Japanese Christianity; VIII.48 Latin American Catholicism; VIII.50 Dutch neo-Calvinism.

**Precedent check: the earlier eras do not pick up every row either.** By the same count, era 7 picks up 14 of 21 rows at its boundary and era 8 picks up 5 of 11. So the eras 1–9 standard is not "every living row must have a successor." It is "fill the gap where the reference histories treat the later chapter as formation-grade." V1.0 used the same test (Survey §5).

**What changes now that the window closes at 2010.** V1.0 gave two reasons for leaving its largest gaps undrafted:
- **20th-century Anglicanism:** "the realignment's recency" (GAFCON 2008 [S]). (2010 revision.) GAFCON 2008 now falls inside the era, two years before its end. So the recency point is real again, but only for the window's last two years. The 1906–2008 story does not depend on it. The realignment can be the entry's closing line, dated and [S].
- **The post-Soviet Orthodox revival (1991–present):** "the honest window is young and politically entangled". (2010 revision.) To 2010 the window is 1991–2010, nineteen years. That is long enough to be a real story, but it is still unsourced in the repo.

**D-P1. 20th-century Anglicanism: put it to the gate as a named gap. Do not draft a full row yet.**
- In-repo anchors are thin:
  - VIII.30's sources (the 1867 Lambeth Conference, era 9);
  - IX.32's Newbigin story (the Church of South India, a united church, 1947);
  - IX.3 (the East African Revival began among Anglicans around 1930);
  - IX.46's story (Anglican member churches of the WCC);
  - CHC vol. 9 (McLeod, 2006), cited across the era.
- No source base is staged, and no repo source covers Lambeth's 20th century or the Communion's turn to the Global South.
- A skeleton is in the companion JSON's `newEntries` (D-E5). It holds only these repo-anchored facts, so the gate can see how thin it is.
- **D-Q1.**
  - (a) Adopt the skeleton now as a Tier 2 signal, with B1 graded Thin in-repo.
  - (b) Name it as the era's largest gap, send it to the source-research thread, and draft at V2.0 Round 2 once a base exists. **Recommended:** a row with no base would be the first in the census drafted on Thin.
  - (c) Add only a disclosure line on VIII.30, and no row.

**D-P2. The post-Soviet Orthodox revival (2010 revision): name it as a gap. No row this run.**
- IX.22 already carries the Moscow Patriarchate's canonization of the new martyrs in August 2000, inside the era.
- A 1991–2010 window can now support a story by the eras 1–9 standard. But the repo holds no base for it beyond IX.22's 2000 line.
- **D-Q2a.**
  - (a) Name it as an open receiver gap for VIII.31 and IX.22, with no row and the base wanted. **Recommended.**
  - (b) Fold 1991–2010 into IX.22's closing line and move IX.22's end.
  - (c) Draft a skeleton now.

**D-P3. Name three more gaps for the gate. Draft none of them.**
- (i) **20th-century Orthodoxy in the Balkans and Eastern Europe** outside Russia and Georgia. VIII.28 has no successor. IX.12 (Romania's Lord's Army) covers one renewal movement, not the churches. No in-repo base.
- (ii) **The Protestant denominational families after 1906** (Methodist, Baptist, Lutheran and Holiness denominations). VIII.4's legacy names the Holiness denominations (the Church of the Nazarene and others), with no era-10 home. IX.35 covers only the American mainline and its theology.
- (iii) **Japanese Christianity after 1906.** VIII.45 has no successor. VIII.45's sources cite Uchimura's own writings, which open the Non-Church (Mukyōkai) line. No era-10 base.

All three go on the wanted list. **D-Q2:** (a) name all three in the V2.0 record as open receiver gaps, with no rows (**recommended**); (b) draft skeletons now; (c) leave them unnamed. Option (c) repeats the V1.0 silence that Round 2 criticized.

#### 1B. V1.0's declined-and-named list, re-judged as history to 2010

| Item | V1.0 disposition | As history to 2010 | Proposal |
|---|---|---|---|
| 20th-c. Anglicanism | named, not drafted (recency) | recency reason gone | D-P1 / D-Q1 |
| Post-Soviet revival | named, not drafted | window 1991–2010 (2010 revision) | D-P2 / D-Q2a |
| Word-of-Faith / prosperity | lines in IX.11 floorNote, IX.45 orbit | a teaching current; the 2026-07-16 scope rule ("formation communities, not schools of thought") still applies | keep as named lines; no row |
| TSPM/CCC (1951/1954, 1980 [S]) | context lines in IX.5 | all in-window; unchanged | keep as lines in IX.5 |
| NAR | register-shaped, not drafted | (2010 revision) its naming and spread now fall largely inside the window, but nothing in-repo dates any of it | keep V1.0's disposition: named, not drafted, register-shaped; base wanted |
| Korea scope note | distributed (IX.2, IX.11, IX.16) | unchanged | keep the scope note |
| IFI 1947 Declaration [S] | relations note on Frozen VIII.39 (Q10) | in-window; unchanged | keep; this is a touch on a Frozen row, so it is Mark's |
| Liberation theology as a lane | line in IX.8's orbit | school-of-thought rule | keep as a line |
| UK house-church restorationism (1970s [S]) | line in IX.45's orbit | in-window | keep as a line |
| Opus Dei / new ecclesial movements | lines in IX.7 / IX.47 | IX.47's relationsSummary already names Opus Dei (1928) | keep as lines |

#### 1C. The two structural boundary questions

**D-P4. The register rows' era-10 segments (LDS, JW, Christian Science, Christadelphians).**
- These rows are capped at 1906 under the register-cap convention. Only VIII.10 has an era-10 successor (IX.44, SDA), and the Frozen E9 record charged that one case.
- No in-repo source covers any of these four bodies after 1906.
- **D-Q3.**
  - (a) A one-line disclosure on each Frozen row, saying the body continued after 1906 and the register does not follow it into era 10. **Recommended.** It is V1.0's lean, and it answers "participants will ask" without four rows that no source supports.
  - (b) Four era-10 segment rows.
  - (c) One family register row for "the restorationist register bodies in the 20th century."
- Either way, editing the Frozen rows is Mark's call.

**D-P5. MacArthur / Grace to You placement.** As history to 2010, the record holds:
- the MacArthur Study Bible (1997 [S]);
- the "Bible-teaching media" shape (Survey §3, option iii).

The *Strange Fire* conference (2013) is outside the era and drops out. Mark's new direction on movements outside church bodies (§4) creates a fourth home: a Christian broadcasting and Bible-teaching media movement (§4, M8).
- **D-Q4.**
  - (i) Named lines in IX.33's continuation lane (V1.0's lean).
  - (ii) IX.29's teaching world.
  - (iii) No placement this run.
  - (iv) A named carrier inside M8, if M8 is adopted. **Recommended.** It fits the shape the survey itself described ("radio/study-Bible/conference") without stretching IX.33's 1970s window.

#### 1D. The banked IX.16 split (Iglesia ni Cristo to its own row)

- V1.0's blocker was that no drafted row existed.
- **D-P6:** A draft now exists (the companion JSON's `newEntries`, D-E1). It is built only from IX.16's own census copy and sources:
  - registration on 27 July 1914;
  - the church's own claim that Felix Manalo was God's messenger;
  - *Pasugo* from February 1939;
  - the 1963 and 2009 successions ([S] in the survey);
  - INC's own counts, with no independent count.
- (2010 revision.) The 2009 succession now falls inside the era and is kept.
- **D-Q5.**
  - (a) Split INC out now as its own register row. It needs a new atlasId: IX.51 if IX.50 stays held, or IX.50 if Mark declines IX.50. That numbering is itself Mark's call.
  - (b) Keep the four-body composite, and record the split as considered and declined.
  - (c) Split all four bodies into their own rows.
- **Recommended: (a).**
  - INC is the largest body in the composite.
  - IX.16's own relationsSummary justifies the packing by saying "none is large or well-studied enough." For INC, the copy contradicts the size half of that. The study half holds: its sources note that scholarship is thin.
  - Splitting INC also leaves the other three bodies an honest composite.
- **Downstream flag (from V1.0):** the new row needs one relations line toward the Philippine story (VIII.39, Philippine Catholicism, era 9).

#### 1E. The banked IX.20 stale line

- IX.20's relationsSummary still says the lane "previously ended at 1500". That is false: VI.25 (1517–1650) and VIII.49 (1855–1900) both exist.
- V1.0's banked text reads: "continuation of VIII.49's re-founded empire church (chain written at the E9 Freeze); the lane's true disclosed silence is 1650–1855."
- **That banked text is itself unusable.** It narrates process ("chain written at the E9 Freeze") in a participant-facing field. CLAUDE.md treats that as corruption of a live surface.
- **D-P7. Proposed text:** "Continues the Ethiopian church of Tewodros and Menelik. The tree has no entry for Ethiopian Christianity between 1650 and 1855."
- The census check confirms the 1650–1855 silence: VI.25 ends in 1650, VIII.49 begins in 1855, and there is no Ethiopian row in era 8.

#### 1F. Roster consequences of the 2010 close

These list only what the sweep shows; §2 carries each entry's detail.
- **IX.31** (Deconstruction, "c. 2010s-present"). (2010 revision.) Every anchor is dated 2015 or later, so its whole story falls after 2010. The options are drop, or fold its pre-2010 roots into IX.28 as a line. Dropping a row moves it to `retiredMovements` (a `retireEntry` operation in the JSON), and that is Mark's call (G-8).
- (2010 revision.) **IX.36** (1998; TGC 2005–07, T4G 2006 and Hansen 2006/2008 now fall inside; the Mars Hill end of 2014 falls outside), **IX.49** (FFOZ 1992 and the 2009 shift fall inside), **IX.28** (1990–2015, so its end becomes 2010; Rob Bell's 2011 book falls outside), **IX.32**, **IX.18** and **IX.48** (Ancient Faith Radio 2004 inside; the Hanegraaff chrismation of 2017 outside). All of these now hold a real 1906–2010 story. Each drafter tests what falls past 2010.
- (2010 revision.) **Pentecostal growth in Africa, Asia and Latin America** now falls inside the window through 2010. IX.11 (1950s–), IX.4, IX.25 and IX.5 already carry it, so their ends become 2010. **No new row is needed**: the sweep found no growth story that those four do not already hold.
- **The "Overlay Current" form** (Decision-Log 2026-07-16, nineteenth pass) was justified by "the historiographical horizon", meaning "nothing has settled". The wet-ink rendering fades "unfinished at the right". Under history to 2010, that reason no longer holds for era 10. **D-Q6:**
  - (a) Keep the overlay flag but drop the "still forming" reading. The overlay keeps only its "overlays, not territories" meaning (non-exclusive membership). **Recommended:** that meaning is still true of 1906–2010 currents, and it is the natural home for §4's movements.
  - (b) Retire the overlay form for era 10.
  - (c) Keep it as it is. That contradicts ruling 2 ("era 10 makes no claims about the time after 2010").

#### 1G. Overlap and double-counting among the 49

| Pair | Finding | Proposal |
|---|---|---|
| IX.11 / IX.25 | RCCG (1952) appears in both: IX.11 tells its Nigerian home, IX.25 its 1994 London plant. The two are distinct (home church against diaspora mission), with one shared body. | Keep both. Each names the other in one line. Not a double count. |
| IX.24 / IX.30 | A global congress network against a congregational church model. They share an evangelical base, but neither carries the other's content. | Keep both. No action. |
| IX.23 / IX.47 | Back to back in time (1906–1962, 1962–). The chain VIII.29→IX.47→IX.23 is in place (continuesAs checked). Not overlapping. | Keep both. IX.7 (Catholic lay renewal from the 1930s) runs alongside both. Its Catholic Charismatic Renewal wing should cross-reference IX.45, which already says the Catholic wing "lives in IX.7". |
| IX.33 / IX.29 | Real shared prehistory: both `why` fields open on the Niagara conferences of the 1870s, and both carry Scofield-era print. V1.0 ruled that IX.29 keeps the culture and IX.33 the church contest. | Keep both. **D-P8:** only one row should lead with Niagara in its `why` (IX.29, whose start of 1875 rests on it). IX.33 should open on *The Fundamentals* (1910) and its 1920 naming, and mention Niagara only in relationsSummary. In §6 as G-49. |
| IX.35 / IX.18 / IX.46 | IX.35 hands off to IX.18 at 1990. IX.46 is the institution, IX.35 the theology. | Keep. |
| IX.1 / IX.15 / IX.43 | The Oneness split (1913) from IX.1. COGIC sits in IX.43. Clean. | Keep. |
| IX.5 / IX.15 | The True Jesus Church sits between them (V1.0's packing seam). | Keep the V1.0 disclosure. |
| IX.24 / §4 mass evangelism and missions | Lausanne 1974 was "called by Billy Graham's organization" (IX.24's story). | See §4, M4 and M5. |

---

## 2. The 49 entries, re-assessed (Sections A and B, tiers, dates, living, register)

Each entry gives its disposition, tier, dates, living-as-of-2010 flag, Section A, Section B (B1–B5), sourcing grade, register edits in summary (full text in the companion JSON), the links touching it, its open questions and its wanted texts. Local question labels feed §6.

### 2a. IX.1–IX.17

Proposals only; nothing in the census is changed. Every register edit is in the companion JSON's `entries`, and the whole file is checked by applying it in order to a copy of the census.

#### IX.1 — Azusa Street & Early Pentecostalism (`azusa-street-and-early-pentecostalism`)
**Disposition:** keep — the origin episode of the era's Pentecostal family; its window is a real episode end inside the era, so nothing moves. · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1906-1920s (1906–1920) (V1.0: 1906-1920s (1906–1920)) · **Living as of 2010:** yes — The Pentecostal tradition this revival began was a living, practicing body in 2010; the mission itself had closed in 1931. Flag: depends on the open P2-V 'living' definition (episode window closed before 2010; the tradition it names was alive in 2010).

**Section A:** A1 floor: no question (floorNote 'No question'); classical Holiness-Pentecostal, trinitarian; the 1913 Oneness rupture is carried at IX.15. A3: no interpretive-fidelity question. Unchanged from V1.0.

**Section B:** B1 Rich and self-documenting — the mission's own paper, Seymour's 1915 church order, participant memoirs, the hostile press. B2 Full lived world: worship, testimony, race and the color line, print, polity, the 1911 split — most of the eight lenses. B3 Distinct as the origin episode; IX.2 is its polygenesis counterweight, IX.11/IX.45 its later wings. B4 Pentecostal believers, historians, pastors, and anyone asking about race and the American church. B5 Tiebreak only: the descendant family is century-scale. V1.0 reasoning holds unchanged.

**Sourcing (B1 grade):** Rich. Rich — The Apostolic Faith (Los Angeles, 1906–08); Seymour, Doctrines and Discipline (1915); Bartleman (1925) and the Valdez/Catley recollections; the Los Angeles Times of 18 Apr 1906 and the hostile press file; Robeck (2006, verified), Anderson (2004/2013, verified); Espinosa (2014) and Wacker (2001) [S]; CHC vol. 9 volume-level, chapter [S].

**Confidence notes:** 'Almost every Pentecostal church … traces back to what happened on that street' (why) and 'Almost every movement in this era's Pentecostal family runs back through here' (legacy): Contested — the Azusa-origin reading stands against the polygenesis reading that IX.2 itself states and Anderson (verified) carries. Presented in the row as settled; see Q1.

**Register:** 3 edits (listed in the JSON); 3 edits: the 'continues beyond it' line put in the past; the dated-reading clause removed; 'exists today' in the why recast to the twentieth century.

**Links touching it:** 3 (the-holiness-movement → IX.1; the-black-church-in-america → IX.1; IX.1 → IX.4). The IX.1 → IX.4 note ('the balance is still studied') speaks in the present tense — flag for P2-L10. The other two are fine history.

**Source notes:** All V1.0 [S] flags carried: The Apostolic Faith issue-run detail [S]; Bartleman and Seymour editions [S]; the hostile press file [S]; Espinosa and Wacker [S]. Robeck and Anderson verified. No source in this row documents only post-2010 events. Robeck 2006 and Espinosa 2014 are later scholarship on the 1906–22 events and stay. Library (cic/texts/REGISTRY.yaml, cic/corpus-map/): no vendored text bears on this entry.

**Open questions for Mark:** Q1 — The Azusa-origin claim is stated as settled ('almost every Pentecostal church … traces back'), but the polygenesis reading (IX.2's own claim; Anderson) contests it. Options: (a) keep the sentence, tense-fixed only, and tag the claim Contested in the record; (b) soften the copy to 'a great many Pentecostal churches of the century traced their line back to what happened on that street, though revival also broke out on its own elsewhere'; (c) leave as is. Recommendation: (b) — it states the uncertainty plainly in the row the participant reads, and it matches IX.2's own copy.

**Wanted:** The Apostolic Faith (Los Angeles, 1906–1908, 13 issues) — PD — for the source-research thread.; William J. Seymour, The Doctrines and Discipline of the Azusa Street Apostolic Faith Mission (Los Angeles, 1915) — PD — for the source-research thread.; Frank Bartleman, How Pentecost Came to Los Angeles (1925) — PD — for the source-research thread.; Charles F. Parham, A Voice Crying in the Wilderness (1902; rev. 1910) and his Apostolic Faith (Baxter Springs) — PD — for the source-research thread (the 1906 visit from Parham's side).; William H. Durham, Pentecostal Testimony (Chicago, 1911–12) — PD — for the source-research thread.; Los Angeles Times, 18 Apr 1906, 'Weird Babel of Tongues' — PD — for the source-research thread.

#### IX.2 — The 1904-07 Revival Family (Wales; Mukti India; Pyongyang Korea) (`the-1904-07-revival-family-wales-mukti-india-pyo`)
**Disposition:** keep — the legal single pre-1906 crossing banked at E9; a real episode end in 1910. · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1904-1910 (1904–1910) (V1.0: 1904-1910) · **Living as of 2010:** yes — The churches the revivals left (Welsh chapels, Indian and above all Korean Protestantism) were living, practicing bodies in 2010; the revival wave itself subsided c. 1910. Flag: depends on the open P2-V 'living' definition (episode window closed before 2010; the tradition it names was alive in 2010).

**Section A:** A1: no question. A3: none. Unchanged.

**Section B:** B1 Rich — near-verbatim journalism (Western Mail, Stead), the Mukti press and Abrams, Blair and the Korean church histories. B2 Three lived settings with testimony, confession, prayer practice (dawn prayer, praying aloud), mission and nation. B3 Distinct: the polygenesis counter-case to IX.1. B4 Korean, Welsh and Indian Christians; historians of revival. B5 Korea's later scale is a tiebreak note only. Unchanged.

**Sourcing (B1 grade):** Rich. Rich — Western Mail reports by 'Awstin' (1904–05); Stead, The Revival in the West (1905); Penn-Lewis with Roberts, War on the Saints (1913); Mukti Prayer-Bell; Abrams (1906); Blair (1910; reissued 1977) and the Korean church histories (Kil Sŏn-ju); Jones (2004), Oak (2013) [S]; CHC vol. 9. Only the Pyongyang January 1907 start is verified; the rest [S].

**Confidence notes:** Korean origin lines (Allen 1884, Underwood/Appenzeller 1885, Nevius 1890, Sŏ Sang-yun): Widely Accepted, [S] in V1.0 — carried, not upgraded.

**Register:** 2 edits (listed in the JSON); 2 edits: the dated-reading clause removed; 'are still the record' made timeless.

**Links touching it:** 0.

**Source notes:** All V1.0 [S] flags carried (editions of every primary; Jones and Oak). No post-2010-only source. Library: no vendored text bears on this entry (the-welsh-revival-tradition corpus-map file serves the eighteenth-century revival, not 1904).

**Open questions for Mark:** none

**Wanted:** W. T. Stead, The Revival in the West (1905) — PD — for the source-research thread.; Minnie Abrams, The Baptism of the Holy Ghost and Fire (1906) — PD — for the source-research thread.; William N. Blair, The Korea Pentecost (1910) — PD — for the source-research thread.; Western Mail revival reports by 'Awstin', 1904–05 — PD — for the source-research thread.; Jessie Penn-Lewis with Evan Roberts, War on the Saints (1913) — PD — for the source-research thread.; Mukti Prayer-Bell (Pandita Ramabai's mission press) — PD — for the source-research thread.

#### IX.3 — The East African Revival (Balokole) (`the-east-african-revival-balokole`)
**Disposition:** keep — real episode end at Luwum's martyrdom (1977), applied at the E10 Freeze. · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1930s-1970s (1930–1977) (V1.0: 1930s-1970s (1930–1977)) · **Living as of 2010:** yes — The revival fellowships went on inside East African Anglicanism in 2010 [S — V1.0 carried this unverified]; the wave itself had subsided by the 1970s. Flag: depends on the open P2-V 'living' definition (episode window closed before 2010; the tradition it names was alive in 2010).

**Section A:** A1: no question. A3: none. Unchanged.

**Section B:** B1 Moderate-to-rich — testimony culture, convention records, Kivengere and Church, and two verified standards (Peterson 2012; Ward & Wild-Wood 2012). B2 Confession practice, hymn, fellowship, tension with mission authority, martyrdom — a full lived world. B3 Distinct African-led revival inside mission Anglicanism. B4 African Christians, historians of mission, pastors. B5 Tiebreak only. Unchanged.

**Sourcing (B1 grade):** Moderate-to-rich. Moderate-to-rich — Kabale convention and fellowship records; Nagenda's addresses; Kivengere, I Love Idi Amin (1977); Church, Quest for the Highest (1981; missionary pen); the Luwum record (1977; Westminster Abbey 1998); Peterson (2012) and Ward & Wild-Wood (2012) both verified; CHC vol. 9.

**Confidence notes:** Continuation of the fellowships inside Anglicanism through 2010: Widely Accepted, [S] — carried, not upgraded.; Luwum's death date (16/17 Feb 1977): [S] in V1.0 — carried.

**Register:** 7 edits (listed in the JSON); 7 edits: the 'persist … to this day', 'still sung today', 'remains its best-known martyr' and 'still gathering' lines put in the past; the dated-reading clause removed; the 'only recently' phrase made timeless.

**Links touching it:** 1 (east-african-christianity-uganda-martyrs → IX.3) — fine history.

**Source notes:** V1.0 [S] flags carried: testimony and convention editions [S]; Church (1981) [S]; Luwum details [S]; Sanneh/Walls [S]. No post-2010-only source; the 2012 standards are later scholarship and stay. Library: none.

**Open questions for Mark:** none

**Wanted:** A dated record that the fellowships were active in the 2000s (e.g. a convention record) would lift the living-as-of-2010 call off [S]; Ward & Wild-Wood (2012, verified) may already carry it — to check.

#### IX.4 — African-Initiated Churches (Harrist; Aladura; Zionist/ZCC; Kimbanguist) (`african-initiated-churches-harrist-aladura-zioni`)
**Disposition:** keep — the four-family row with per-body notes stays the census's deliberate design; end moves 2026 → 2010. · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1880s-2010 (1880–2010) (V1.0: 1880s-present (1880–2026)) · **Living as of 2010:** yes — All four families (Harrist, Aladura, Zionist/ZCC, Kimbanguist) were large, practicing churches in 2010.

**Section A:** Per body. Harrist and Aladura mainstreams: creedally conventional on their own church constitutions [S] — clear, as in V1.0. ZCC: no published confession, by the church's own choice — recorded open with the constraint named, as in V1.0. Kimbanguist: V1.0's dated divergence arc now runs inside the era for two of its three legs — the 2005 moderate official doctrine and the 2008 Nkamba revocation in favor of the popular teaching (Kimbangu as the Holy Spirit incarnate; the three sons as the Trinity's incarnations) — so the R2-style finding stands on dated own-voice texts, disclosed, not harmonized. The third leg, the 2021 exclusion from the WCC, falls after 2010 and drops. The finding describes published teaching, never members. c2 per body unchanged (Harrist/Aladura likely-clear on the community limb; Kimbanguist and ZCC open).

**Section B:** B1 Moderate-to-rich — three verified standards (Sundkler 1948, Peel 1968, Martin 1975), verified founding anchors (Tile 1880s, Mokone 1892, Kimbangu 1921, ZCC 1924), own liturgies and constitutions; colonial-record gravity severe. B2 Full lived worlds per family: prophecy, healing, pilgrimage, liturgy, polity, colonial conflict. B3 Distinct: Africa's own initiative, not mission or Pentecostal derivative. B4 African Christians and diaspora, historians, pastors, seekers. B5 Several very large bodies (tiebreak). Unchanged except A.

**Sourcing (B1 grade):** Moderate-to-rich. Moderate-to-rich — Harris via hearers' records (1926 Benoit notes) and later Harrist catechisms; Cherubim & Seraphim founding records (1925), CAC records (1930), Church of the Lord (Aladura) constitutions; the 1921 Kimbangu military-court record (hostile-legal); ZCC practice-borne record; Sundkler (1948/1961), Peel (1968), Martin (1975) verified; Anderson (2001) [S].

**Confidence notes:** Harrist/Aladura 'creedally conventional by their own constitutions': Widely Accepted on V1.0's [S] — no constitution cited by name and year.; Kimbanguist 2005 doctrine and 2008 Nkamba reversal: Documented (V1.0: verified dated arc).; 'Grew into one of the largest [churches] in Africa' (story): the church's own scale — no independent count cited.; Start in the 1880s: Documented (Tile 1880s and Mokone Nov 1892 both verified).

**Register:** 13 edits (listed in the JSON); 13 edits: the 2021 WCC exclusion removed from statusDescription and floorNote (the 2005/2008 arc kept, re-sentenced); the teaser's '1900s to today' set to '1880s to 2010' (also fixing its clash with the 1880s start); present tenses put in the past; the 'steadily being gathered' clause dropped; the dated-reading clause removed.

**Links touching it:** 2 (IX.1 → IX.4; the-missionary-movement-s-native-churches-seramp → IX.4). The IX.1 → IX.4 note ('the balance is still studied') is present-tense — flag for P2-L10.

**Source notes:** DROP as post-2010-only: the 2021 WCC-exclusion leg of 'the later trinitarian-controversy record' (keep the 2005/2008 legs); the World Christian Encyclopedia 3rd ed. (2019) adherence counter (2019 counts) — unless its 2010 figures are cited as such, flagged. V1.0 [S] flags carried: Harrist/Aladura/ZCC editions [S]; Anderson 2001 and Shank [S]; Harris trek 1913–15 [S]; Aladura 1918/1930 [S]. Verified: Sundkler, Peel, Martin, Tile, Mokone, Kimbangu 18 Mar 1921, ZCC 1924, the Kimbanguist 2005/2008/1969 arc. Library: none.

**Open questions for Mark:** Q1 — The Kimbanguist 2021 WCC exclusion now falls after the era. Options: (a) drop it and keep the 2005/2008 arc with the 1969 admission as background (as drafted); (b) keep it as a declared post-era note — breaks ruling 2. Recommendation: (a). In §6 as G-40.

**Wanted:** The Kimbanguist 2005 doctrinal statement and the 2008 Nkamba assembly text, by title — to cite by name and year.; The 1926 Benoit interview notes on Harris — archival; rights to be checked.

#### IX.5 — The Chinese Church - Indigenous & Suffering (`the-chinese-church-indigenous-and-suffering`)
**Disposition:** keep — end moves 2026 → 2010. · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1920s-2010 (1920–2010) (V1.0: 1920s-present (1920–2026)) · **Living as of 2010:** yes — The registered and house churches, the True Jesus Church and the Little Flock line were all practicing in 2010.

**Section A:** A1/A3 per body, on published texts only. The November 1998 house-church Confession of Faith [S] — trinitarian, creed-close — stays the own-voice anchor. The Nee-then-Lee line stays a genuinely open, per-body question, with the CRI 2009 reassessment (inside the era) as its dated counter-note, unchanged from V1.0. The True Jesus Church's Oneness confession is the IX.15 seam. The safety discipline stays as ethics, not as an addendum rule: people active in 2010 may still be living and at risk.

**Section B:** B1 Moderate-to-rich, uneven by circumstance — rich founder corpora (Nee, Wang, Sung), state records under coerced-genre flags; Lian Xi (verified), Bays [S]; thin and unsafe exactly where growth was greatest. B2 Full lived world: house meetings, prison, testimony, state contest. B3 Distinct indigenous-and-suffering lane; kin of IX.12. B4 Chinese Christians and diaspora, historians, seekers, deconstructing believers drawn to the house-church pattern. B5 Very large, contested scale — tiebreak only. Unchanged.

**Sourcing (B1 grade):** Moderate-to-rich. Moderate-to-rich (uneven by circumstance) — Nee, The Spiritual Man (1928) and the Little Flock corpus (Living Stream frame flagged); Wang Mingdao (1950; 1955); Sung's family-edited diaries; TJC records (1917–); the Christian Manifesto (1950) and TSPM records; the November 1998 Confession [S]; Lian Xi (2010, verified); Bays (2012) [S].

**Confidence notes:** Scale: Contested — Pew (2011 publication), official TSPM/CCC figures and movement claims differ.; The 1998 Confession's text and signatories: [S] — carried; signatories stay unnamed for safety.

**Register:** 11 edits (listed in the JSON): 'to today', 'ever since', 'has gone on since', 'present-day community', 'still faces today' and the present-tense scale lines put in the past; the Pew figure kept, labeled as a study published later, in 2011; the floorNote's 'stands doctrinally' put in the past; the dated-reading clause removed. The CRI 2009 lines stand unchanged.

**Links touching it:** 1 (the-missionary-movement-s-native-churches-seramp → IX.5) — fine history.

**Source notes:** FLAG: Pew 2011 (c. 67M) is a 2011 publication; the repo does not pin the year its estimate refers to. Keep, worded as 'a Pew study published later, in 2011'; if its reference year is after 2010, drop. Keep the excluded-by-safety source note; its 'present-day state' wording should read 'living, non-public believers'. V1.0 [S] flags carried: founder-corpus editions [S]; Jesus Family records [S]; TSPM records [S]; Bays [S]. Lian Xi and TJC 1917 verified. Library: none.

**Open questions for Mark:** Q1 — The Pew count was published in 2011, one year past the era's end. Options: (a) keep it, labeled as a later study ('a Pew study published later, in 2011'), as G-4(a) allows (drafted); (b) drop it and leave the scale contest without a figure. Recommendation: (a). The year the count describes is not pinned in the repo and must be checked before publication; if it is after 2010, take (b). In §6 under G-4.

**Wanted:** Watchman Nee, The Spiritual Man (Chinese original, Shanghai, 1928) — PD-by-date candidate — for the source-research thread (rights to be checked for a Chinese 1928 imprint).; The November 1998 house-church Confession of Faith — the published text, to pin its wording (not PD; published).

#### IX.6 — The Confessing Church (`the-confessing-church`)
**Disposition:** keep — closed tradition, principled dates both ends. · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1933-1945 (1933–1945) (V1.0: 1933-1945) · **Living as of 2010:** no — The Confessing Church ended with the war in 1945; its texts lived on, the body did not.

**Section A:** A1: no question. A3: none. Standing method unchanged; Barmen's drafting cross-referenced to IX.35, not double-carried.

**Section B:** B1 Rich — Barmen, Dahlem, Rundbriefe, Finkenwalde, prison letters, the Stuttgart Declaration, and the hostile state files. B2 Full lived world under catastrophe, including its own silences. B3 Distinct. B4 Every named audience. B5 Small body, outsized legacy — tiebreak only. Unchanged.

**Sourcing (B1 grade):** Rich. Rich — Barmen (May 1934), the Bethel draft (1933), Dahlem (Oct 1934); Bonhoeffer's Discipleship (1937), Life Together (1939), Letters and Papers (1951); the Rundbriefe and Finkenwalde records; the 1936 memorandum; the Stuttgart Declaration (Oct 1945); Gestapo and Deutsche Christen files; Barnett (1992), Scholder (1987–88), Bethge (rev. 2000). All [S] in V1.0.

**Confidence notes:** none beyond the [S] flags carried.

**Register:** 3 edits (listed in the JSON); 3 edits: the 'not a dated reading like the living traditions' sentence recast as plain history; two present-tense reception lines ('is a confessional text', 'is read') put in the past.

**Links touching it:** 0.

**Source notes:** All V1.0 [S] flags carried. No post-2010-only source. Library: none vendored.

**Open questions for Mark:** none

**Wanted:** The Barmen Theological Declaration (1934) — post-1930, not PD by US date; a rights check for a vendored German text.

#### IX.7 — Catholic Lay Renewal Traditions (Catholic Worker; Focolare; Charismatic Renewal; L'Arche) (`catholic-lay-renewal-worlds-catholic-worker-foco`)
**Disposition:** keep — four distinct movements, per body; end moves 2026 → 2010. · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1930s-2010 (1930–2010) (V1.0: 1930s-present (1930–2026)) · **Living as of 2010:** yes — All four movements were active in 2010.

**Section A:** A1: no floor question for any of the four. c2 per body, re-read as of 2010: the Catholic Worker had passed beyond its founders; the Charismatic Renewal had no single founder; L'Arche's founder was still alive in 2010 (his 2019 death is in the row), so its succession test lay outside the era; for Focolare the record on file gives no founder's death date, so its status in 2010 is not established here. Both had institutional form (statutes; a federation). The L'Arche founder-abuse record concerns conduct within the era (the 2020 inquiry: 1970–2005; the 2023 commission: from 1952), documented in later reports; kept as labeled later sources (cross-entry principle).

**Section B:** B1 Rich per movement — own papers, founders' books, Malines Documents, the L'Arche reports. B2 Full lived worlds (hospitality, community, worship, disability). B3 Distinct lay-renewal lane; IX.45 carries the North Atlantic charismatic wider wing. B4 Catholics, seekers, people with disabilities and their families, pastors. B5 Tiebreak only. Unchanged.

**Sourcing (B1 grade):** Rich. Rich per movement — Day, The Long Loneliness (1952), Loaves and Fishes (1963), The Catholic Worker (1933–), Maurin's Easy Essays; Lubich's writings and the Focolare General Statutes; Ranaghan & Ranaghan (1969) and the Malines Documents (1974–); Vanier, Community and Growth (1979); L'Arche International's 2020 inquiry and the 2023 Study Commission report (later documents); Piehl (1982). All [S] in V1.0.

**Confidence notes:** Focolare 'statutes approved by Rome' by 2010: Widely Accepted; approval year not pinned ([S]-debt carried).; 'All four had institutionalized beyond their individual founders': holds for institutional form; for L'Arche the founder was living in 2010 — see Q2.

**Register:** 12 edits and 1 removal (listed in the JSON): 'to today', 'still running', 'are still going' put in 2010 terms; the L'Arche reports labeled as later documents in why, longDescription, statusDescription, floorNote and the L'Arche voice; the post-era reception sentence about L'Arche's handling of its founder's record removed (gap left); the dated-reading clause removed; story[1] removed whole, pending Q1 (G-13).

**Links touching it:** 0.

**Source notes:** KEEP, labeled later: L'Arche International 2020 inquiry; 2023 Study Commission report — they document conduct inside the era (pending the cross-entry principle). V1.0 [S] flags carried: all editions [S]; Focolare statute year-pinning [S]-debt; L'Arche document detail [S]. Library: none.

**Open questions for Mark:** Q1 — Story[1], 'What L'Arche Found About Its Founder' (2020–2023), narrates post-2010 events (the 2019 death, the inquiry, the publications) about conduct inside the era. Options: (a) remove it from era 10 and keep the abuse record in the summary fields only; (b) re-center it on what the reports found about 1952–2005, using only facts already in the story, with the reports cited as later sources; (c) keep it as a declared exception. Recommendation: (b); until rewritten, (a). Q2 — c2 as of 2010: narrow the statusWord's 'likely-cleared per body' for L'Arche (founder living and leading in 2010) and for Focolare (founder status not on file)? Options: (a) narrow to 'cleared for the Catholic Worker; L'Arche untested in 2010; Focolare to confirm'; (b) keep, reading 'institutionalized' as institutional form only. Recommendation: (a).

**Wanted:** The Catholic Worker (1933–) — post-1930, not PD; rights check.; Focolare General Statutes, first approved text, with year — would pin the 'approved by Rome' claim.

#### IX.8 — Latin American Base Communities (`latin-american-base-communities`)
**Disposition:** keep — real episode end in the 1990s contraction; nothing moves. · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1960s-1990s (1960–1990) (V1.0: 1960s-1990s (1960–1990)) · **Living as of 2010:** yes — The base communities had contracted in the 1990s but still met in 2010, and their pastoral practice lived on in Latin American church life [S]. Flag: depends on the open P2-V 'living' definition (episode window closed before 2010; the tradition it names was alive in 2010).

**Section A:** A1: no question. A3: none. Liberation theology as an academic lane stays a named line here, not a row (V1.0).

**Section B:** B1 Rich — participatory documents by nature (Solentiname commentary), Medellín and Gutiérrez verified, martyr records. B2 Full lived world: Bible reading, politics, martyrdom, the Pentecostal sibling. B3 Distinct. B4 Catholics, historians, seekers, pastors in poor communities. B5 Tiebreak only. Unchanged.

**Sourcing (B1 grade):** Rich. Rich — Medellín (1968, verified) and Puebla (1979) [S]; Cardenal, El Evangelio en Solentiname (from 1975); CEB assembly records (1975–); Romero's homilies and diary; the 1980 churchwomen; the UCA Jesuits (1989); Gutiérrez (1971/1973, verified); Boff (1977); the 1984/1986 CDF instructions; Burdick (1993), Lernoux (1980), Martin (1990).

**Confidence notes:** The base communities' contraction in the 1990s and continuation into 2010: Widely Accepted, [S] — carried.

**Register:** 7 edits (listed in the JSON); 7 edits: 'contracted after the 1990s' corrected to 'in the 1990s' (matching the row's own status line); 'lives on/continue … today' put in the past; Romero's 2018 canonization, Cardenal's 2019 reinstatement and the 2022 beatification removed (gaps left); the dated-reading clause removed.

**Links touching it:** 0.

**Source notes:** DROP from text (events after 2010): Romero's 2018 canonization, trimmed from the primary line. Pew 2006 stays usable as a counter inside the era. V1.0 [S] flags carried: Puebla, Solentiname editions, CEB records, Boff, Burdick, Lernoux, Martin [S]; Medellín and Gutiérrez verified. Library: none.

**Open questions for Mark:** none

**Wanted:** none

#### IX.9 — Emigre Orthodoxy & the Paris School (`emigre-orthodoxy-and-the-paris-school`)
**Disposition:** keep — real episode end at OCA autocephaly (1970); IX.48 receives it. · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1920s-1970s (1920–1970) (V1.0: 1920s-1970s (1920–1970)) · **Living as of 2010:** yes — The tradition the Paris generation built (St Sergius, St Vladimir's, the OCA) was active in 2010. Flag: depends on the open P2-V 'living' definition (episode window closed before 2010; the tradition it names was alive in 2010).

**Section A:** A1: no question. A3: none. The Optina-genealogy nuance stays (the Bulgakov/Berdyaev renaissance stands beside Optina, not simply after it).

**Section B:** B1 Rich — Schmemann's journals, Skobtsova, institute records, the 1935–37 Sophia file both sides. B2 Full lived world in exile. B3 Distinct from IX.22 (inside Russia) and IX.48 (America). B4 Orthodox, converts, theologians, historians. B5 Tiebreak only. Unchanged.

**Sourcing (B1 grade):** Rich. Rich — Schmemann, Journals 1973–1983 (2000) and For the Life of the World (1963); Skobtsova, Essential Writings (2003); St Sergius records (1925–); Bulgakov and the Sophia file; Florovsky (1937); Lossky (1944); Arjakovsky (2013), Plekon (2002). All [S] in V1.0.

**Confidence notes:** Optina → Paris link: Inferential-Thin, as the edge already grades it.; Sophia question 'still open in 2010': Widely Accepted.; Skobtsova's 2004 canonization: [S] in V1.0 — carried.

**Register:** 4 edits (listed in the JSON); 4 edits: 'still put into students' hands' and 'today descends' put in the past; 'still open' in story[0] dated to 2010; the dated-reading clause removed. The 2004 canonizations now fall inside the era and stay.

**Links touching it:** 1 (the-optina-elders-and-russian-ascetic-renewal → IX.9) — fine history.

**Source notes:** Skobtsova's 2004 canonization and Essential Writings (2003) sit inside the era and stay. All V1.0 [S] flags carried. Library: none.

**Open questions for Mark:** none

**Wanted:** none

#### IX.10 — The Coptic Monastic & Sunday-School Revival (`the-coptic-monastic-and-sunday-school-revival`)
**Disposition:** keep — end moves 2026 → 2010; the Girgis start fork stays as frozen (keep 1940s + disclose). · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1940s-2010 (1940–2010) (V1.0: 1940s-present (1940–2026)) · **Living as of 2010:** yes — The Coptic Orthodox Church, its Sunday schools and its repopulated monasteries were active in 2010.

**Section A:** A1: no question. A3: none. Unchanged.

**Section B:** B1 Rich — both renewal streams wrote copiously; Suriel (verified) and CHC vol. 5 ch. 21 (verified) carry it in English. The new-martyrs leg (2015) and Girgis's canonization (2013) fall after 2010 and drop, which costs the row a vivid strand but not its base. B2 Full lived world: catechesis, monastic life, patriarchal conflict with the state (1981–85). B3 The map's longest unbroken lane; distinct. B4 Orthodox, Copts and diaspora, historians, seekers drawn to the desert. B5 Tiebreak only.

**Sourcing (B1 grade):** Rich. Rich — Girgis's Arabic corpus and the Sunday-school organization (c. 1918; divergence disclosed); Matthew the Poor and the St Macarius corpus; Kyrillos VI papers (1959–71); Shenouda III's books (from 1971); Suriel (2017, verified); Hasan (2003) [S]; CHC vol. 5 ch. 21 (O'Mahony, verified at E9).

**Confidence notes:** The 1918 Sunday School Committee: [S], since the two research runs diverge (the survey verified it; the sources run could not page-verify it) — the church's traditional date. No date string rests on it.; Matthew the Poor's readership outside Egypt by 2010: Widely Accepted (English Orthodox Prayer Life, SVS 2003, inside the era).

**Register:** 10 edits and 2 removals (listed in the JSON): the 2015 Libya martyrs removed from teaser, why, longDescription and legacy, and their voice and source items removed whole (gaps left; the 'names its dead' imagery kept, past tense); Girgis's 2013 canonization removed; Shenouda 'published steadily from then to 2010'; the legacy put in 2010 terms; the dated-reading clause removed.

**Links touching it:** 1 (coptic-revival-under-cyril-iv → IX.10) — fine history.

**Source notes:** DROP as post-2010-only: the new-martyrs source line (the 21 Libya martyrs, 2015; Mosebach, The 21, ET 2019); 'canonized 2013' trimmed from the Girgis line; Shenouda 'books (1971–2012)' read to 2010. Girgis 1918: the verification-divergence disclosure carried; never upgraded. Library: none.

**Open questions for Mark:** none

**Wanted:** Habib Girgis, al-Karma (from 1907) — PD by date (Arabic) — for the source-research thread; the organizing record of 1918 would settle the date divergence.

#### IX.11 — Global South Pentecostal Christianity (`global-south-pentecostal-christianity`)
**Disposition:** keep — end moves 2026 → 2010. · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1950s-2010 (1950–2010) (V1.0: 1950s-present (1950–2026)) · **Living as of 2010:** yes — The named churches (Assembleias de Deus, RCCG, Yoido, Igreja Universal, El Shaddai) were all large and active in 2010.

**Section A:** A1: no row-level question; only per-community bounded windows are honest (the row's own rule). The prosperity-gospel line rests on dated texts; the Lausanne critique documents are undated in the record (to pin; they very likely fall inside the era, Cape Town 2010 included, but that is not asserted here). The CD/CR 'contemporary register' language is retired; scale claims are self-report or definitional aggregate unless an independent count is named.

**Section B:** B1 Moderate-to-rich, unevenly mediated — own print per community; Anderson (verified); Pew 2006 and 2011 (verified) usable as in-era counters; WCE 2019 drops. Martin, Kalu, Miller & Yamamori [S]. B2 Full lived worlds per community. B3 Distinct Global South lane; IX.25 the diaspora, IX.45 the North Atlantic middle. B4 Global South believers and diaspora, pastors, historians of world Christianity. B5 Very large — tiebreak only.

**Sourcing (B1 grade):** Rich. Rich but unevenly mediated (census line kept) — RCCG records (1952–), Yoido and Cho, The Fourth Dimension (1979), Assembleias de Deus (1911–), Igreja Universal (1977–), El Shaddai (1984); prosperity teaching and the family's own published critiques; Anderson (2004/2013, verified); Pew 2006/2011 (verified); Martin (1990; 2002), Kalu (2008), Miller & Yamamori (2007) [S]; CHC vol. 9.

**Confidence notes:** 'By the end of the century the Assembleias de Deus were the largest Protestant body in Latin America' (story[0]): Widely Accepted on self-counts; no independent count cited.; Scale totals: Contested by definition; the definitional spread is the datum.

**Register:** 10 edits and 1 removal (listed in the JSON): 'to today'/'present edge' put in 2010 terms; the prosperity argument put in the past; the hundreds-of-millions and 'now largely Global South' lines recast to 2010; the CD/CR 'contemporary register' language retired; the dated-reading clause removed; story[1] (2014 conviction) removed whole (G-13).

**Links touching it:** 0.

**Source notes:** DROP as post-2010-only: WCE 3rd ed. (2019). Pew 2006 and 2011 stay (Pew 2011 flagged as one year past, like IX.5). FLAG: the 'Lausanne evaluations' need titles and dates. V1.0 [S] flags carried; Anderson verified. Library: none.

**Open questions for Mark:** Q1 — Story[1], 'The Founder of the Largest Church Is Convicted' (2014): the 2002 share purchase and 2008 retirement fall inside the era, but the complaint (2011), charge (2013), conviction (2014) and death (2021) do not. Options: (a) remove it from era 10; (b) cut it back to its in-era facts (founding, cell groups, 2008 retirement), dropping the conviction — the story then loses its point; (c) keep it as a declared exception. Recommendation: (a).

**Wanted:** The titles and dates of the Lausanne prosperity-gospel critiques the row cites.

#### IX.12 — Persecuted-Church Traditions of the Communist Era (Initsiativniki Baptists; Romania's Lord's Army) (`persecuted-church-worlds-of-the-communist-era-in`)
**Disposition:** keep — real documented end (1991). · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1945-1991 (1945–1991) (V1.0: 1945-1991) · **Living as of 2010:** yes — The Initsiativniki (as the CCECB) and the Lord's Army were active bodies in 2010 [S], though the persecution that defines the row ended in 1991. Flag: depends on the open P2-V 'living' definition (episode window closed before 2010; the tradition it names was alive in 2010).

**Section A:** A1: no question. A3: none. Unchanged.

**Section B:** B1 Moderate-to-rich — samizdat bulletins, Khristianin, Vins, Trifa's weekly, Dorz, post-1991 archives; Bourdeaux, Sawatsky [S]. B2 Full lived world under persecution, led by wives and mothers. B3 Distinct; kin of IX.5. B4 Eastern European Christians, historians, persecuted-church advocates. B5 Tiebreak only. Unchanged.

**Sourcing (B1 grade):** Moderate-to-rich. Moderate-to-rich — Council of Prisoners' Relatives bulletins (1964–); the 1961 Initiative Group letters; Khristianin; Vins (ET 1975); Trifa's Oastea Domnului (1923–); Dorz; CARC/CRA and Securitate files opened after 1991; Bourdeaux (1968) and the Keston archive; Sawatsky (1981); Chadwick (1992). All [S] in V1.0.

**Confidence notes:** The member movements' life in 2010: Widely Accepted, [S].; 'Hundreds of thousands by the 1930s' (Lord's Army): the movement's own scale — self-report.

**Register:** 5 edits (listed in the JSON); 5 edits: the 'continuing life' and 'live on' lines put in the past; 'is now recognized' and 'preserves' made past; the dated-reading clause removed.

**Links touching it:** 1 (russian-evangelicals-stundists → IX.12) — fine history.

**Source notes:** All V1.0 [S] flags carried. The post-1991 archives stay: they document pre-1991 events. Library: none.

**Open questions for Mark:** none

**Wanted:** Iosif Trifa, Oastea Domnului weekly, issues of 1923–1930 — PD by date (Romanian) — for the source-research thread.

#### IX.13 — Messianic Judaism (`messianic-judaism`)
**Disposition:** keep — end moves 2026 → 2010. · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1960s-2010 (1960–2010) (V1.0: 1960s-present (1960–2026)) · **Living as of 2010:** yes — Messianic congregations, the MJAA, the UMJC and Jews for Jesus were active in 2010.

**Section A:** A1 per body, unchanged from V1.0: the UMJC's 'Defining Messianic Judaism' (2005) and the MJAA statement of faith (HCAA 1915, renamed 1975) are the dated texts — both inside the era; mainstream confessions trinitarian, no floor question. Year-pinning of the MJAA statement stays [S]-debt.

**Section B:** B1 Moderate — recent, self-documenting, contested from two sides; Stern (1988, 1998), Kinzer (2005); Harris-Shapiro (1999), Cohn-Sherbok (2000), Ariel (2000) [S]; Rudolph & Willitts (2013, verified) as later scholarship. B2 Liturgy, festival, identity, Israel, double-direction contest. B3 Distinct from IX.49 (gentile Torah-observance) — that boundary depends on IX.49's own re-opened disposition. B4 Jewish believers, Christians and Jews asking the oldest question, historians. B5 Small — tiebreak only.

**Sourcing (B1 grade):** Moderate. Moderate — the HCAA's 1915 statement (MJAA from 1975); the UMJC's 1979 doctrinal basis and 'Defining Messianic Judaism' (2005); Jews for Jesus (1973–); Stern (1988; 1998); Kinzer (2005); Jewish communal and Christian responses; Harris-Shapiro (1999), Cohn-Sherbok (2000), Ariel (2000) [S]; Rudolph & Willitts (2013, verified).

**Confidence notes:** UMJC and MJAA statements: Documented as texts; year-pinning [S] — carried.

**Register:** 12 edits (listed in the JSON): 'to today'/'living return' set to 2010; 'recent' dropped from the sourcing line; 'is recent', 'is argued', 'ever since', 'has governed … since' and the present-tense legacy and story lines put in the past; the floorNote's 'a living body can change' clause recast; the dated-reading clause removed. The 2005 texts and the 2008 ruling now fall inside the era and stay.

**Links touching it:** 0.

**Source notes:** DROP as post-2010-only: the Pew 2013 US Jewish survey counter. V1.0 [S] flags carried: own statements year-pinning [S]; Stern and Kinzer editions [S]; outside standards [S]. Rudolph & Willitts verified. Library: none.

**Open questions for Mark:** none

**Wanted:** The Hebrew Christian Alliance of America's 1915 statement of faith — PD by date — for the source-research thread (it would pin the MJAA statement's base text).

#### IX.14 — Ecumenical Community Traditions - Taize & Iona (`ecumenical-community-worlds-taize-and-iona`)
**Disposition:** keep — end moves 2026 → 2010; V1.0's c2 CLEAR stands (the 2005 transition is inside the era). · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1938/1940-2010 (1938–2010) (V1.0: 1938/1940-present (1938–2026)) · **Living as of 2010:** yes — Both communities were active in 2010.

**Section A:** A1: no question. c2: V1.0's CLEAR stands. Brother Roger's murder (16 Aug 2005) and the community's continuation under Brother Alois are inside the era, a completed founder-to-successor transition. Only the 2023 handover to Brother Matthew falls after 2010 and drops. Iona's 1967/1969 record (MacLeod's retirement; the rule changed over his objection) is a second, earlier community-limb datum.

**Section B:** B1 Rich — both rules, the communities' own print and worship material, Spink and Ferguson [S]. B2 Full lived worlds: rule, worship, youth pilgrimage, work and justice. B3 Distinct ecumenical-community lane. B4 Seekers, young people, worship leaders, ecumenists. B5 Tiebreak only. Unchanged.

**Sourcing (B1 grade):** Rich. Rich — the Rule of Taizé (1954); Brother Roger's writings; the founding record (1940); Council of Youth (1974) and European meetings (1978–); MacLeod, Only One Way Left (1956); the Iona Rule and membership records (1938–), Coracle, Wild Goose material; Spink (1986; rev. 2005), Ferguson (1988; 1990). All [S] in V1.0.

**Confidence notes:** Roger's murder 16 Aug 2005 and the Alois succession: [S] in V1.0 — carried.

**Register:** 9 edits (listed in the JSON); 9 edits: the 2023 Matthew handover removed from statusDescription, why, longDescription, legacy, voices and story[0]; 'to today', 'still going', 'have been held every year since' put in 2010 terms; the floorNote's 'well past their founders' deaths' dated to 2010; the dated-reading clause removed.

**Links touching it:** 1 (insular-irish-monastic-christianity → IX.14) — its 'still held' refers to Bede's eighth century; fine history.

**Source notes:** DROP as post-2010-only: the Alois → Matthew (2023) leg of the succession records. Roger d. 2005 → Alois stays. All V1.0 [S] flags carried. Library: none (the adomnan_life-of-saint-columba_huyshe1905.txt file serves Columba's Iona, not this community; not cited).

**Open questions for Mark:** none

**Wanted:** none

#### IX.15 — Oneness Pentecostalism (`oneness-pentecostalism`)
**Disposition:** keep on the register — end moves 2026 → 2010. · **Tier:** Register (Floor Question) (V1.0: Register (Floor Question)) · **Dates:** 1913-2010 (1913–2010) (V1.0: 1913-present (1913–2026)) · **Living as of 2010:** yes — The UPCI, PAW, ALJC and other Oneness bodies were practicing churches in 2010.

**Section A:** A1 register disposition carried, per body, dated: the April 1913 Arroyo Seco meeting and the AG's 1916 Statement (both verified) document the rupture on both sides. UPCI: the Articles of Faith in the annual Manual (verified as the right text) — for history, cite a Manual of 2010 or earlier by year [the wording itself still S]. PAW and ALJC: recorded OPEN with their gaps named, unchanged. c2 null, argued (no single founder). Seams IX.15↔IX.5 (TJC) and IX.15↔IX.16 (LLDM) stay disclosed.

**Section B:** B1 Rich own record (both sides' confessions; Haywood; UPCI Manual); Reed (2008), French (1999), Ramirez (2015) [S]. B2 Full lived world, including the interracial PAW story. B3 Distinct register family. B4 Oneness believers and their neighbors; Pentecostal historians; race and church. B5 Tiebreak only.

**Sourcing (B1 grade):** Rich. Rich (own record) — UPCI Articles of Faith in the annual Manual (verified); Arroyo Seco (Apr 1913, verified); Ewart (1914; The Phenomenon of Pentecost, 1947); the AG Statement of Fundamental Truths (Oct 1916, verified); Haywood's writings and hymns; PAW records; UPCI merger vote 25 Sep 1945 (verified); Reed (2008), French (1999), Ramirez (2015) [S].

**Confidence notes:** PAW Oneness from 1916; ALJC 1952 merger: [S] — carried.; 'The largest Oneness denomination' (story[1], UPCI): self-report — no independent count.

**Register:** 8 edits (listed in the JSON); 8 edits: 'to the present' → 2010; teaser 'from 1913' → '1913 to 2010'; 'still what a visitor notices', 'publishes', 'are living churches' and 'is still its confession' put in the past; the dated-reading clause removed.

**Links touching it:** 0.

**Source notes:** DROP as post-2010-only: the WCE 2019 constituency aggregate. The UPCI Manual must be cited by a year of 2010 or earlier. V1.0 [S] flags carried (Ewart, Haywood, PAW records, Reed, French, Ramirez). Library: none.

**Open questions for Mark:** none

**Wanted:** The Assemblies of God Statement of Fundamental Truths (October 1916) — PD — for the source-research thread.; G. T. Haywood's writings and hymns (to 1931) — PD — for the source-research thread.; A UPCI Manual of 2010 or earlier, for the Articles' dated wording.; A dated PAW and ALJC statement of faith from before 2010 — closes the two open sub-findings.

#### IX.16 — Iglesia ni Cristo; The Way International; Unification Church; La Luz del Mundo (`iglesia-ni-cristo-the-way-international-unificat`)
**Disposition:** keep on the register — end moves 2026 → 2010; the V1.0 INC row-split fork stays an open, un-executed question. · **Tier:** Register (Floor Question) (V1.0: Register (Floor Question)) · **Dates:** 1914-2010 (1914–2010) (V1.0: 1914-present (1914–2026)) · **Living as of 2010:** yes — All four bodies were active in 2010.

**Section A:** A1 per body on texts up to 2010: INC (Pasugo from 1939; registration 1914, verified) — messenger claim, non-trinitarian; The Way (Jesus Christ Is Not God, 1975) — title-level non-trinitarian; Unification (Divine Principle, 1966; English year 1973 vs 1996 divergence carried) — new-revelation authority; LLDM (apostle claim; Oneness descent). c2 'record' per body as of 2010: INC survived successions in 1963 and 2009; LLDM in 1964; The Way two changes of leadership; the Unification Church still led by its founder (d. 2012) — the 'record' fits it most strongly. The 2012 and 2014 successions and the 2019–22 LLDM case fall outside the era.

**Section B:** B1 Moderate — own texts strong (Pasugo verified), scholarship thin for INC/Way/LLDM; Barker (1984) [S]. B2 Full lived worlds per body. B3 Distinct register bodies, grouped for economy, not confession. B4 Members and ex-members, neighbors, Philippine and Mexican participants. B5 INC very large (self-report) — tiebreak only.

**Sourcing (B1 grade):** Moderate. Moderate — Pasugo/God's Message (Feb 1939–, verified) and the 1914 registration (verified); Wierwille, Power for Abundant Living (1971) and Jesus Christ Is Not God (1975); Divine Principle (1966; ET 1973 or 1996 — divergence carried); LLDM's own apostleship confession (founding 1926, verified); Barker (1984) and the NRM literature [S]; the 1982 Moon tax-trial court record (in the row's story).

**Confidence notes:** Divine Principle English year: Contested (1973 vs 1996, two research runs) — carried undecided.; INC 'largest church founded in the Philippines': the church's own counts; no independent count.; INC 2009 succession; Martindale's 2000 resignation: [S] — carried.

**Register:** 6 edits and 1 removal (listed in the JSON): 'still led', 'now the Family Federation', 'is led' put in the past; the legacy rewritten to the state of 2010 (INC 1963/2009, LLDM 1964, The Way's two changes; Moon still leading), the 2012/2014 successions and the 2022 conviction removed and replaced by the 1982 Moon conviction already in the row's own story; floorNote put in the past; the dated-reading clause removed; story[0] (2019–22) removed whole (G-13).

**Links touching it:** 0.

**Source notes:** DROP as post-2010-only: the 2022 California guilty plea and sentencing of Naasón Joaquín García (LLDM primary line); 'succession through … Naason Joaquin' trimmed to the 1964 succession; The Way's 'current statements-of-belief' to be replaced by a dated statement of 2010 or earlier. V1.0 [S] flags carried: Way and UC editions [S]; Barker [S]; UC founding 1 May 1954 [S]. Pasugo, INC 1914, Vesper Chimes 1942, Wierwille dates and LLDM 1926 verified. Library: none.

**Open questions for Mark:** Q1 — Removing the 2022 LLDM conviction (legacy, sources, story[0]). V1.0 called it 'part of any honest telling'; under ruling 2 it lies after 2010, and the man led only from 2014. Options: (a) remove it and story[0], replacing the legacy's court-record example with the 1982 Moon conviction already in story[1] (as drafted); (b) keep it as a declared exception. Recommendation: (a). Q2 — The INC row-split (V1.0's banked, un-executed lean). History to 2010 does not change the grounds. Options: (a) carry it banked to the V2.0 gate unchanged; (b) close it now as 'keep packed'. Recommendation: (a) — it still needs a drafted row before it can be applied.

**Wanted:** A dated Way International statement of belief from 2010 or earlier.; Divine Principle English translation — the 1973 edition and the 1996 Exposition, to settle the divergence.; Any in-era public court or press record bearing on La Luz del Mundo's leadership — for the research thread to check, not assumed.

#### IX.17 — Branch Davidians & Apocalyptic Splinters (`branch-davidians-and-apocalyptic-splinters`)
**Disposition:** keep on the register — closed movement, real documented end (1993). · **Tier:** Register (Floor Question) (V1.0: Register (Floor Question)) · **Dates:** 1929-1993 (1929–1993) (V1.0: 1929-1993) · **Living as of 2010:** no — The Mount Carmel community ended in the fire of 19 April 1993; remnant groups outlasted it [S], but the movement the row names did not. Flag: depends on P2-V if remnant groups were to count as 'living'.

**Section A:** A1 register disposition carried: person-defined ground in extreme form, on the movement's own texts (Houteff 1930/32; Roden; Koresh 1993). Not a live c2 application (closed movement), as V1.0 stated. Unchanged.

**Section B:** B1 Moderate (context-only by design) — own texts, the state-authored ending (hearings 1993/1995; Danforth 2000), Tabor & Gallagher (1995), Newport (2006) [S]. B2 Thin by design — kept for map honesty, not as a formation world. B3 The register's edge case. B4 Participants who ask about Waco. B5 Small.

**Sourcing (B1 grade):** Moderate. Moderate (context-only by design; census line blank) — Houteff, The Shepherd's Rod (1930; 1932); Roden publications; Koresh's Seven Seals manuscript (1993); the congressional hearings (1993, 1995) and the Danforth Report (2000); Tabor & Gallagher (1995); Newport (2006, later scholarship). Houteff 1929, Mount Carmel 1935 and the 1993 siege/fire (76 dead) verified; the rest [S].

**Confidence notes:** Cause of the fire: Contested — stated in the story as disagreement, not settled.; Remnant groups outlasting 1993: [S] — carried, no group named.

**Register:** 4 edits (listed in the JSON); 4 edits: 'remnant existence today' and 'no present community' put in historical terms; 'is now known' made past; the legacy's remnant line and reception sentence put in the past and split; Newport (2006) kept, now inside the era.

**Links touching it:** 0.

**Source notes:** The Danforth Report (2000) and Newport (2006) sit inside the era and stay. V1.0 [S] flags carried. Library: none.

**Open questions for Mark:** none

**Wanted:** Victor T. Houteff, The Shepherd's Rod, vol. 1 (1930) — PD by date (US, 2026) — for the source-research thread. Vol. 2 (1932) is not yet PD.

### 2b. IX.18–IX.33

Proposals only; nothing in the census is changed. Every register edit is in the companion JSON's `entries`, and the whole file is checked by applying it in order to a copy of the census.

Status sentence: "This status is a dated reading of a living tradition, not a permanent verdict." is removed on every row it appears on, matching eras 1 to 9 (see cross-cutting X1).

#### IX.18 — Progressive Christianity (a broad label, not one movement) (`progressive-christianity-a-broad-label-not-one-m`)
**Disposition:** keep (label row, re-dated to 1990–2010) · **Tier:** Label (A3), no tier — unchanged (V1.0: Label (A3)) · **Dates:** c. 1990-2010 (V1.0: contemporary, 1990–2026) · **Living as of 2010:** yes — Bodies claiming the label existed in 2010 (the Center, founded 1994; emerging-church networks). Depends on P2-V: whether a label, not a body, can be 'living' at all.
**Section A:** A3 label row, held to its own law: no entry-level finding, ever. Per-body illustration only, on dated texts: the Center's points (first version 1994; revision 2003 [S]). The 2011 revision [S] is after the era and is not cited. **Section B:** B1 Thin, by design (label context; Dorrien verified). B2 n/a (a label is not a lived world). B3 distinct: the label, not IX.35's mainline bodies. B4 strong: participants ask about the word. B5 n/a.
**Sourcing (B1 grade):** Thin (label-context only, by design). **Confidence notes:** 'By 2010 the label was claimed by mainline congregations…' moves a present-tense description to 2010; only the Center and the emerging-church networks are staged. Grade: Widely Accepted for the networks, Inferential-Thin beyond them.
**Church or movement/trend: neither — a label row; it names many church bodies and some trends, and is judged on none.**
**Register:** 10 edits (in the JSON); fields touched: floorNote, legacy, longDescription, statusDescription, teaser, why. The statusDescription's process commentary ('now or ever'; 'it now has the history it lacked') is cut.
**Links touching it:** 0
**Source notes:** (1) Dorrien (2001–06): verified, in era. Hollinger (2013): later scholarship on the mainline trajectory — keep. (2) Bass, Christianity for the Rest of Us (2006): in era — keep, as participant-adjacent journalism, not scholarship (V1.0's flag kept). (3) The 'fast-growing current' reference item: drop — a present-state claim, out of scope. (4) The '8 Points' item: keep, scoped to the 1994 and 2003 versions; version-year pinning stays [S].
**Open questions for Mark:** Q1 (IX.18) — Keep the label row, re-dated c. 1990–2010? Options: (a) keep, with the discipline unchanged; (b) fold it into IX.35 as a closing line (a cross-entry decision); (c) drop. Recommendation: (a). In §6 as G-41. Under the 2010 cut-off its documented expression, the emerging church, falls inside the era, so the row has real in-era content.
**Wanted:** The Center for Progressive Christianity's points, 1994 and 2003 versions, dated editions — not PD; needed to pin the one illustration this row cites.

#### IX.19 — The Sayfo & the Syriac Diaspora (`the-sayfo-and-the-syriac-diaspora`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1915-2010 (V1.0: 1915-present, 1915–2026) · **Living as of 2010:** yes — Syriac Orthodox and Church of the East communities were practicing churches in 2010, mostly in the diaspora.
**Section A:** No question (A1 passes; no A3 question exists). **Section B:** B1 Moderate-to-rich (Gaunt 2006 and Let Them Not Return 2017 verified — later scholarship on 1915; Naayem 1921 and the 1919 memoranda [S]). B2 strong: catastrophe, dispersal, re-gathered institutions. B3 unique: the Syriac lane's only era-10 row. B4 strong (descendant communities; trauma-informed care). B5 n/a.
**Sourcing (B1 grade):** Moderate-to-rich. **Confidence notes:** 'By 2010 … parish registers recorded families…' and 'by 2010 the families … lived more in Södertälje and Chicago than in Anatolia' re-date the record's present claims: Widely Accepted, with no counter staged.
**Church or movement/trend: church (two church families carried together).**
**Register:** 10 edits (in the JSON); fields touched: documentedStories, legacy, longDescription, relationsSummary, statusDescription, teaser, voices. *Let Them Not Return* (2017) is restored to the legacy, labeled as later (G-4); the 2015 commemorations stay out. Atto's voice is labeled as a later account. The three 'erasure' lines are drafted for Q1, conditional on G-42.
**Links touching it:** 1 (VIII.40→IX.19, continued as, Widely Accepted). Note is dated and past-tense — clean.
**Source notes:** (1) Gaunt 2006 and Gaunt/Atto/Barthoma 2017: verified; later scholarship on 1915 — keep. (2) Atto 2011, Brock 2001: [S] — keep the flag. (3) The '2015 centenary commemoration records' (reference item): flag/drop — a post-2010 event. (4) Library: cic/texts/wigram_assyrians-and-their-neighbours_1929.txt bears directly (it covers the Hakkari expulsion of 1915 and the 1918 aftermath; an outside witness, an Anglican mission head; already cited on the VIII.40→IX.19 link). cic/texts/malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt and cic/texts/maclean-browne_catholicos-of-the-east-and-his-people_1892.txt are pre-Sayfo background only.
**Open questions for Mark:** Q1 (IX.19) — The teaser, relationsSummary and legacy say the map's 1300–1915 silence is one 'living Syriac communities' read (or 'experience') as erasure. That is a present-day claim about readers. Options: (a) keep it as a map-level disclosure, dropping 'living' and putting the verb in the past ('experienced as erasure'); (b) recast it to map-voice only, with no claim about readers; (c) remove it. Recommendation: (a), drafted as three conditional edits. It keeps the E9 named-gap ruling's language without a claim about today. In §6 as G-42.
**Wanted:** Joseph Naayem, Shall This Nation Die? (New York, 1921) — PD — for the source-research thread (story 0 is still 'primary text not yet read').; The Assyro-Chaldean delegation's memoranda to the Paris Peace Conference (1919) — PD by date — for the source-research thread.; The British parliamentary report on the Armenian massacres that Bryce compiled (named in story 0) — PD — for the source-research thread.; Mar Eshai Shimun XXIII, The Assyrian Tragedy (1934) — rights check (after the ~1930 line).

#### IX.20 — Modern Ethiopian & Eritrean Christianity (`modern-ethiopian-and-eritrean-christianity`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1900-2010 (V1.0: 1900-present, 1900–2026) · **Living as of 2010:** yes — The Ethiopian Tawahedo church, the Eritrean church (autocephalous 1993; under severe state pressure from 2006) and the P'ent'ay churches were all practicing in 2010.
**Section A:** No question. **Section B:** B1 Moderate-to-rich (all [S]; Binns 2017 and Eshete 2009 are later scholarship on pre-2010 events). B2 strong (an empire church, occupation, the Derg, an evangelical counter-current). B3 unique (the Africa lane's Oriental Orthodox row for 1900–2010). B4 solid. B5 tiebreak only: one of the largest ancient churches.
**Sourcing (B1 grade):** Moderate-to-rich. **Confidence notes:** 'By 2010 … a large minority' and 'one of the largest ancient churches anywhere': scale claims re-dated to 2010, Widely Accepted, no counter named. 'After the Derg fell … counted … among its martyrs' rests on the 1992 reburials in the record.
**Church or movement/trend: church (with an evangelical church current carried beside it).**
**Register:** 11 edits (in the JSON); fields touched: documentedStories, legacy, longDescription, relationsSummary, statusDescription, teaser, voices, why. The relationsSummary edit carries D-P7's text, conditional on G-21.
**Links touching it:** 1 (VIII.49→IX.20, continued as). Clean.
**Source notes:** (1) The Eritrea primary item: keep the 1993 autocephaly, Antonios deposed in 2006, and the post-2002 persecution records (in era). Flag/drop '(d. 2022)'. (2) The Tawahedo institutional item: flag/drop its '2018 reconciliation' clause. (3) Binns 2017, Eshete 2009, Campbell 2014/2017, Gudina Tumsa (2003 edition of his 1974–79 papers): keep. All [S] flags kept. (4) Library: cic/texts/kebra-nagast_queen-of-sheba-and-menyelek_budge1922.txt (already on the VIII.49→IX.20 link) bears on the lane's continuity, not on 1900–2010 events. The ethiopian-synaxarium_book-of-saints-ethiopian-church-*_budge1928.txt files are liturgical background only.
**Open questions for Mark:** Q1 (IX.20) — V1.0 banked a replacement for the stale '…ended at 1500' line, to be 'applied whenever the row is next opened' (Mark's, Frozen-adjacent). That banked text narrates process and cannot go into a live field (§1E). Options: (a) this re-run opens the row: apply D-P7's text instead — "Continues the Ethiopian church of Tewodros and Menelik. The tree has no entry for Ethiopian Christianity between 1650 and 1855." — plus the matching teaser fix (both drafted, marked CONDITIONAL in the JSON); (b) keep it banked. Recommendation: (a). The row is being rewritten anyway, and the stale line is false. In §6 as G-21.
**Wanted:** Graziani's telegrams of 1937 as printed (Italian state documents) — rights check.; EECMY, 'On the Interrelation between Proclamation of the Gospel and Human Development' (1972) — rights check; the row's key own-voice document.

#### IX.21 — The Ukrainian Greek Catholic Underground (`the-ukrainian-greek-catholic-underground`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1946-1989 (V1.0: 1946-1989, 1946–1989) · **Living as of 2010:** yes — The Ukrainian Greek Catholic Church was a legal, practicing church in 2010. The underground episode itself ended in 1989. P2-V flag: yes depends on reading 'living' as the tradition the entry names, not its episode window.
**Section A:** No question. **Section B:** B1 Moderate-to-rich (both sides' archives; all [S]). B2 strong (underground sacramental life). B3 unique. B4 solid. B5 n/a. End 1989 is a real documented terminus (the 1989 legalization) — kept.
**Sourcing (B1 grade):** Moderate-to-rich. **Confidence notes:** 'By 2010 … the largest of the Eastern Catholic churches': [S] in the survey — kept [S]; Widely Accepted if a counter is staged.
**Church or movement/trend: church.**
**Register:** 5 edits (in the JSON); fields touched: documentedStories, legacy, statusDescription.
**Links touching it:** 1 (VIII.38→IX.21, continued as). Clean.
**Source notes:** (1) All five items: pre-2010 events. Keep. Slipyj's Memoirs (2014 edition) and Plokhy (2015) are later publications about pre-2010 events — keep. (2) Library: cic/texts/pelesz_geschichte-der-union-bd2-deu_1880.txt (on the VIII.38 link) is pre-era background.
**Open questions for Mark:** none
**Wanted:** Sheptytsky, 'Thou Shalt Not Kill' (1942) — rights check.; The acts of the Lviv 'Sobor' (Moscow Patriarchate, 1946) — rights check.

#### IX.22 — The Russian New Martyrs & the Catacomb Church (`the-russian-new-martyrs-and-the-catacomb-church`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1917-1991 (V1.0: 1917-1991, 1917–1991) · **Living as of 2010:** yes — The Russian Orthodox Church, which canonized the new martyrs in August 2000, was practicing in 2010. P2-V flag: yes depends on reading 'living' as the tradition the entry names, not its episode window. Whether separate catacomb or True Orthodox remnants were living in 2010 is not in the record and is not claimed.
**Section A:** No question. **Section B:** B1 Rich (post-1991 archives and both sides' 1927 documents; [S]). B2 strong. B3 unique. B4 solid. B5 n/a. The August 2000 canonization and the May 2007 Act of Canonical Communion and Butovo consecration all fall inside the era and stay. End 1991 is a real documented terminus and stays.
**Sourcing (B1 grade):** Rich. **Confidence notes:** 'In 2010 the division of 1927 was still visible in the calendar' rests on the record's own facts (Kirill canonized August 2000, Joseph not; ROCOR's 1981 act). Documented.
**Church or movement/trend: church.**
**Register:** 7 edits (in the JSON); fields touched: documentedStories, legacy, longDescription, statusDescription, voices.
**Links touching it:** 1 (VIII.11→IX.22, continued as, Inferential-Thin). Clean.
**Source notes:** (1) Story 0 source 'the Act of Canonical Communion, 17 May 2007': in era — keep. (2) The Jubilee Council (Aug 2000): in era — keep. (3) Library: cic/texts/paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt (on the VIII.11 link) is pre-era. cic/texts/conybeare_russian-dissenters_1921.txt covers pre-1917 dissent and does not bear on the catacomb church.
**Open questions for Mark:** Q1 (IX.22) — Story 0's counts ('more than nine hundred … over three hundred canonized') are undated in the record and may include canonizations after 2010. Options: (a) keep them, put into the past tense, with a date check before publish (drafted); (b) cut the counts and leave the gap. Recommendation: (b) unless the check confirms a 2010-or-earlier figure.
**Wanted:** Patriarch Tikhon's anathema of 1918 — PD by date — for the source-research thread.; Metropolitan Sergius's Declaration of 29 July 1927 (Izvestia, 19 August 1927) — PD by date — for the source-research thread; the story quotes it 'in standard translation' and the quote is not yet checked against a text.

#### IX.23 — The Post-Vatican-II Parish Tradition (`the-post-vatican-ii-parish-world`)
**Disposition:** keep · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1962-2010 (V1.0: 1962-present, 1962–2026) · **Living as of 2010:** yes — Catholic parish life under the reformed rites was practicing worldwide in 2010.
**Section A:** No question. The council texts themselves carry the row (1963/1964/1965; RCIA 1972 [S]). **Section B:** B1 Rich. B2 strong. B3 unique (IX.47 precedes it). B4 strong. B5 tiebreak: century-scale. The traditionalist tension now rests on 1974 and 1988 texts only.
**Sourcing (B1 grade):** Rich. **Confidence notes:** 'By 2010 … had become the ordinary route by which adults entered' re-dates a present claim; Widely Accepted. 'In 2010 the Society was still outside full communion' rests on the record: the 2009 lifting of excommunications, with no regularization.
**Church or movement/trend: church (one church's parish tradition).**
**Register:** 12 edits (in the JSON); fields touched: documentedStories, legacy, longDescription, relationsSummary, statusDescription, teaser, voices, why. The statusDescription's 'not a present-day description of a feeling' is cut.
**Links touching it:** 1 (VI.22→IX.23, influenced, Inferential-Thin). Clean.
**Source notes:** (1) The traditionalist primary item: keep Lefebvre 1974, SSPX 1970, the 1988 consecrations, Summorum Pontificum (2007) and the 2009 lifting (all in era). Flag/drop Traditionis Custodes (2021). (2) O'Malley 2008, Massa 2010, Alberigo/Komonchak 1995–2006: keep. (3) Tissier de Mallerais 2004 (story 1): keep; it is positioned, as the census says. (4) Library: the Cherubini bullarium (on the VI.22 link) is pre-era background.
**Open questions for Mark:** none
**Wanted:** none

#### IX.24 — Lausanne-Era Global Evangelicalism (`lausanne-era-global-evangelicalism`)
**Disposition:** keep · **Tier:** Tier 1 (V1.0: Tier 1) · **Dates:** 1974-2010 (V1.0: 1974-present, 1974–2026) · **Living as of 2010:** yes — The Lausanne network was active in 2010; its Third Congress met in Cape Town in October 2010, the era's own closing marker.
**Section A:** No question. The three-dated self-description ladder (1974, 1989, 2010) stays whole inside the era; Seoul 2024 leaves. **Section B:** B1 Rich (Covenant verified; Let the Earth Hear His Voice [S]; Stanley 2013 is later scholarship). B2 strong. B3 unique. B4 strong. B5 n/a. Both stories stay (1974–75; October 2010).
**Sourcing (B1 grade):** Rich (institutional). **Confidence notes:** 'By 2010 integral mission … had become mainstream evangelical language, largely because of 1974' — Dominant Modern Reconstruction (Stanley). The superlative 'most widely subscribed … statement' is removed, not re-dated: no counter is staged.
**Church or movement/trend: movement/trend — a network, not a church, in its own words.**
**Register:** 8 edits (in the JSON); fields touched: legacy, longDescription, relationsSummary, statusDescription, teaser, why.
**Links touching it:** 0.
**Source notes:** (1) Primary item 1: keep the Covenant (1974), Manila (1989) and Cape Town (2010); flag/drop the Seoul Statement (2024). (2) Dudley-Smith 2001, Stanley 2013: keep.
**Open questions for Mark:** none
**Wanted:** J. D. Douglas (ed.), Let the Earth Hear His Voice (1975) — not PD; [S] to verify the Padilla and Escobar papers and paragraph 5 quoted in story 0.

#### IX.25 — African Diaspora & Reverse-Mission Churches in Europe (`african-diaspora-and-reverse-mission-churches-in`)
**Disposition:** keep · **Tier:** Tier 3 (V1.0: Tier 3) · **Dates:** 1960s-2010 (V1.0: 1960s-present, 1960–2026) · **Living as of 2010:** yes — RCCG's British parishes, KICC (1992), Jesus House (1994) and the Kyiv church (1994) were all practicing in 2010.
**Section A:** No question. Carrier device: named carrier bodies, each dated (RCCG 1952 / UK 1980s / Jesus House 1994; KICC 1992; Embassy of God 1994 [all S]). There is no single confession, and that is recorded. **Section B:** B1 Moderate (ter Haar 1998, Adogame 2013, the 2005 Charity Commission report; all [S]). B2 moderate. B3 unique. B4 solid. B5 n/a. Both stories stay inside the era (1994–2004; 2002–2005).
**Sourcing (B1 grade):** Moderate. **Confidence notes:** 'By 2010 the direction of Christian mission had reversed' re-dates the record's claim — Widely Accepted. The 'largest congregation' claims stay framed as the churches' own counts.
**Church or movement/trend: movement/trend (reverse mission) carried by named church bodies — a trend row with churches as its carriers.**
**Register:** 13 edits (in the JSON); fields touched: documentedStories, legacy, longDescription, relationsSummary, sourcing, statusDescription, teaser, voices, why. Both story caveats now read that the page describes only dated public acts, with no 'living person' line. Adogame's voice is labeled as a later account.
**Links touching it:** 0.
**Source notes:** (1) All items: in-era events. Keep. Adogame 2013 is later scholarship — keep. (2) The 'largest congregation' reference item: keep as a disclosure that the claims are self-reported.
**Open questions for Mark:** Q1 (IX.25) — Two story details are undated and may fall after 2010: KICC's moves 'to larger premises in east London and then to Chatham' (cut from the draft and marked for a date check), and how Adelaja's 2009 proceedings ended (the caveat now stops at 2010 knowledge). Recommendation: cut both unless a date check confirms they fall in or before 2010.
**Wanted:** Gerrie ter Haar, Halfway to Paradise (1998) — not PD; the in-era study, [S], to verify.

#### IX.26 — Ratana Church & Pacific Adjustment Movements (`ratana-church-and-pacific-adjustment-movements`)
**Disposition:** keep (register row, question-framed) · **Tier:** Register (question-framed) — unchanged (V1.0: Register) · **Dates:** 1925-2010 (V1.0: 1925-present, 1925–2026) · **Living as of 2010:** yes — Te Haahi Rātana was a practicing church, and a political presence, in 2010.
**Section A:** A1/A3: the mangai question stays open, put to the church's own published hymns, prayers and creed (the faithful angels and the Mangai [S]). The service-book edition dates are [S]-debt, and an in-era assessment must cite an edition dated 2010 or earlier. c2: the office-run is held open (the office persisted by succession through the century, which cuts toward the community limb). The composite tail is named minimally: Silas Eto's CFC (1960 [S]). **Section B:** B1 Moderate (Henderson 1972 and Newman 2006 verified). B2 strong. B3 unique. B4 solid. B5 n/a.
**Sourcing (B1 grade):** Moderate. **Confidence notes:** 'In 2010 … a fixture of the political calendar' re-dates a present claim; Widely Accepted (Newman 2006 covers the period).
**Church or movement/trend: church (with a composite tail of Pacific churches).**
**Register:** 9 edits (in the JSON); fields touched: documentedStories, legacy, longDescription, statusDescription, teaser, voices. The statusDescription's 'for now' is cut.
**Links touching it:** 0.
**Source notes:** (1) All items: pre-2010 events. Newman 2006 is a later publication — keep. Te Ara is the reference layer — keep. (2) The Pacific-family item stays the base's thinnest leg ([S]).
**Open questions for Mark:** none
**Wanted:** The Rātana service book, creed and hymnal in an edition dated 2010 or earlier — rights check; this is the text the open question has to be put to.; Te Whetu Marama o te Kotahitanga, early issues from 1924 — rights check (possibly PD) — for the source-research thread.

#### IX.27 — The Armenian Church after the Genocide (Medz Yeghern) (`the-armenian-church-after-the-genocide-medz-yegh`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** 1915-2010 (V1.0: 1915-present, 1915–2026) · **Living as of 2010:** yes — The Armenian Apostolic Church (Etchmiadzin and Cilicia) was practicing in Armenia and the diaspora in 2010.
**Section A:** No question. **Section B:** B1 Moderate-to-rich (Balakian 1922; Kévorkian 2011 and Suny 2015 are later scholarship; [S]). B2 strong. B3 unique. B4 strong (trauma-informed care). B5 n/a. The 2015 canonization was the row's headline in teaser, why, longDescription, voices and legacy; it is removed everywhere and the gap is left.
**Sourcing (B1 grade):** Moderate-to-rich. **Confidence notes:** 'By 2010 its worldwide diaspora outnumbered the church in Armenia itself' re-dates a present scale claim. Widely Accepted, but no counter is staged; it could be cut instead if Mark prefers.
**Church or movement/trend: church.**
**Register:** 8 edits and 2 removals (in the JSON); fields touched: documentedStories, legacy, longDescription, relationsSummary, statusDescription, teaser, why. The 2015 canonization voice and source items are removed whole. Story 1's 'has held from the first' is put in the past.
**Links touching it:** 1 (VIII.32→IX.27, continued as). Clean (Kévorkian 2011 is cited for 1915).
**Source notes:** (1) The 2015 canonization primary item: drop — a post-2010 event. (2) The institutional item's 'post-1991 re-establishment': in era — keep. (3) Balakian ET 2009 is an edition of a 1922 work — keep; Kévorkian, Suny: keep. (4) Library: cic/texts/ormanian_church-of-armenia_gregory1912.txt (on the VIII.32 link) gives the church's condition just before 1915 — background.
**Open questions for Mark:** Q1 (IX.27) — With 2015 gone, the teaser needs a new hook. Drafted: '…through dispersal, the Soviet decades and the Cold War split between its two sees' (all in the record). Options: (a) take it; (b) lead with Tourian's 1933 killing (story 0). Recommendation: (a).
**Wanted:** Grigoris Balakian, Armenian Golgotha, Armenian original (1922) — PD by date — for the source-research thread.

#### IX.28 — The Emerging Church & Post-Evangelical Movement (`the-emerging-church-and-post-evangelical-movemen`)
**Disposition:** keep (end 2010) · **Tier:** Tier 3 (open: Tier 2 possible, see Q3) (V1.0: Tier 3) · **Dates:** c. 1990-2010 (V1.0: c. 1990-2015, 1990–2015) · **Living as of 2010:** yes — Emergent Village and the emerging-church networks, books and conferences were active in 2010; the wind-down (c. 2013 [S]) comes after the era.
**Section A:** A3 per community, never by label (unchanged; the floorNote is put in past tense). The movement's own dated texts carry it (Tomlinson 1995; McLaren 2001/2004; Bell 2005; Tickle 2008 [all S]). **Section B:** B1 Rich and self-documenting (books, conference records, the 2002– blogs; Carson 2005 as hostile-adjacent dating; Marti & Ganiel 2014 later; all [S]). B2 moderate (a conversation across congregations, with its own communities and networks). B3 distinct from IX.18 (a body-level conversation, not a label). B4 strong — Mark named the 'emergent church'. B5 n/a. Only Love Wins (2011), the 2011 story and the wind-down (c. 2013) fall after 2010.
**Sourcing (B1 grade):** Rich (self-documenting; platform-fragile). **Confidence notes:** End 2010 is the era's close, not a terminus; the 2015 'judgment end' is retired. Network dates (YLN/Terra Nova c. 1997–2001; Emergent Village from c. 2001) stay [S]. The link-rot and Internet Archive lines were notes about the archive's condition today, not the tradition's history; they are recast in the past (X3, G-46).
**Church or movement/trend: movement/trend, not a church body — a conversation across existing congregations, a few communities of its own, and loose networks (Emergent Village). It belongs with the 'movements and trends' class if Mark creates one.**
**Register:** 14 edits and 1 removal (in the JSON); fields touched: documentedStories, floorNote, legacy, longDescription, relationsSummary, statusDescription, teaser, voices, why. Story 1 (2011) is removed whole (G-39). The archive-condition lines in teaser, voices[4] and legacy are recast in the past (G-46). Story 0's caveat drops its 'living person' line.
**Links touching it:** 0.
**Source notes:** (1) The movement's-own-books item: keep Tomlinson 1995, McLaren 2001/2004, Bell 2005, Tickle 2008; flag/drop Love Wins (2011) and 'the split it provoked'. (2) The blog layer: keep from 2002, scoped to 2010. (3) The end-anchor 'wind-down' item: flag — it documents c. 2013, after the era. (4) Carson 2005, Marti & Ganiel 2014, Walker 1985/1998, Tomlinson 2008: keep. (5) Story 1's sources (2011): drop with the story.
**Open questions for Mark:** Q1 (IX.28, the 'emergent church' Mark named) — Under the 2010 cut-off most of its life falls inside the era (Holy Joe's 1990; Tomlinson 1995; YLN c. 1997; Emergent Village c. 2001–; McLaren 2001/2004; Bell 2005; Tickle 2008). Options: (a) keep it, c. 1990–2010, living as of 2010 (drafted); (b) drop or defer it as mainly later — no longer true; (c) fold it into IX.18. Recommendation: (a), firmly. Only Love Wins (2011) and the wind-down fall outside. Q2 (IX.28) — Church or movement/trend? Judgment: movement/trend. It never formed a church body; it ran through existing congregations, a few communities of its own and loose networks. Q3 (IX.28) — Tier. Options: (a) keep Tier 3 (the V1.0 'smaller frame'); (b) raise it to Tier 2, now that its whole documented arc to 2010 sits inside the era with rich own-voice texts. Recommendation: (b), mildly. B1 is rich and B4 is Mark-named, while B2 (a conversation, not a lived world) is the honest brake.
**Wanted:** Records of the Young Leaders Network / Terra Nova and Emergent Village, c. 1997–2010 — [S]; the network leg's own paper.

#### IX.29 — Dispensational Prophecy Culture (`dispensational-prophecy-culture`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** c. 1875-2010 (V1.0: c. 1875-present, 1875–2026) · **Living as of 2010:** yes — The reading culture, its institutions (DTS) and its best-selling texts were in active use in 2010; the Left Behind series was complete (1995–2007).
**Section A:** No plain-reading question. Carrier device: dated mass-texts (Scofield 1909/1917; Larkin 1918; Lindsey 1970; Left Behind from 1995 [all S]). **Section B:** B1 Rich. B2 strong (a reading practice across bodies). B3 unique (VIII.23 carries the formation; this row carries the culture — the overlap is disclosed, as frozen). B4 strong. B5 tiebreak: mass scale. The Left Behind series (1995–2007) now sits wholly in era.
**Sourcing (B1 grade):** Rich. **Confidence notes:** Sales and distribution figures (Scofield 2M by 1945; Whisenant's 300,000 and 4M) are publisher counts: Documented as claims, Contested as a measure of reach.
**Church or movement/trend: movement/trend — a reading culture across many church bodies, with institutional anchors but no church of its own.**
**Register:** 9 edits (in the JSON); fields touched: legacy, longDescription, relationsSummary, statusDescription, teaser. The statusDescription's 'not an undated present-tense claim' is cut.
**Links touching it:** 1 (VIII.23→IX.29, influenced, Dominant Modern Reconstruction). Clean.
**Source notes:** (1) Hummel, The Rise and Fall of Dispensationalism (2023): keep as later scholarship, but never for post-2010 claims. The legacy names it as later: "Hummel's study came later, in 2023." (2) Mangum & Sweetnam 2009, Canfield 1988, Marsden 3rd ed. 2022: keep.
**Open questions for Mark:** Q1 (IX.29) — The legacy line calling the 'one story' reading (IX.32) 'a reaction against the chart' depends on IX.32 staying. It does under this draft. Recommendation: keep. In §6 as G-47.
**Wanted:** The Scofield Reference Bible (1909) — PD — for the source-research thread.; The Scofield Reference Bible, revised (1917) — PD — for the source-research thread.; Clarence Larkin, Dispensational Truth (1918) — PD — for the source-research thread.; Niagara Creed (1878) and the 1878 New York prophecy-conference proceedings — PD — for the source-research thread (shared with IX.33).

#### IX.30 — The Megachurch & Seeker Movement (`the-megachurch-and-seeker-movement`)
**Disposition:** keep · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** c. 1975-2010 (V1.0: c. 1975-present, 1975–2026) · **Living as of 2010:** yes — Willow Creek, Saddleback, the Willow Creek Association and Hillsong were all active in 2010.
**Section A:** No question. Carrier device: Willow Creek 1975, Saddleback 1980, McGavran 1970, Warren 1995, WCA 1992, 'Shout to the Lord' 1993 ([S]). **Section B:** B1 Rich institutional (church-growth literature; REVEAL 2007 in era). B2 moderate-to-strong (a church-building model with a formation system). B3 unique. B4 strong. B5 tiebreak. Story 0 (2004–07) stays, with its caveat's 2018–19 lines removed. Story 1 (2020–21) and the collapse records (2014, 2021, 2021–22) are removed whole.
**Sourcing (B1 grade):** Rich (institutional). **Confidence notes:** 'By 2010 the model was everywhere' re-dates a present claim — Widely Accepted. 'By then the Hartford Institute's research studied it' rests on Thumma & Travis (2007).
**Church or movement/trend: movement/trend — a model of building churches, used by many independent churches; not a church body.**
**Register:** 9 edits and 2 removals (in the JSON); fields touched: documentedStories, legacy, longDescription, relationsSummary, sourcing, statusDescription, teaser, voices, why. Story 1 and the collapse-records source item are removed whole (G-39, G-26). Bowler's *Blessed* (2013) is restored to the legacy, labeled as later (G-4).
**Links touching it:** 0.
**Source notes:** (1) REVEAL (2007–): in era — keep. (2) The memoir-and-collapse item (Zacharias 2021, Mars Hill 2014 / CT 2021, Hillsong 2021–22): drop — post-2010 only. (3) Thumma & Travis 2007: keep. Bowler 2013: keep as later scholarship, named as later in the legacy. (4) Story 0's source 'Independent Advisory Group report (28 February 2019)': drop with the caveat line. Story 1's sources (2020–21): drop with the story.
**Open questions for Mark:** Q1 (IX.30) — Story 0's caveat named the founder's 2018 resignation and the 2019 report. The resignation is a post-2010 event. The report is a later inquiry, but the record does not date the conduct it examined inside the era, so G-4(a) does not keep it. Options: (a) remove both (drafted); (b) keep a caveat line on safeguarding grounds. Recommendation: (a), but flag it for the Facilitator/safety owner, since the story celebrates a figure whose later record is public. In §6 under G-4.
**Wanted:** none

#### IX.31 — Deconstruction & Ex-vangelical Communities (`deconstruction-and-ex-vangelical-communities`)
**Disposition:** drop (begins after 2010) · **Tier:** — (drop) (V1.0: Tier 2 (Mark's R7 hand-selection, 2026-08-14)) · **Dates:** c. 2010s-present (no era-10 window) (V1.0: c. 2010s-present, 2010–2026) · **Living as of 2010:** n/a — Not applicable: no anchor for this current falls in or before 2010. The earliest is Searching for Sunday (2015); the name 'exvangelical' dates from 2016.
**Section A:** Not run: there is no 1906–2010 entry to assess. **Section B:** Not run. Every namable anchor is 2015 or later. Harris's I Kissed Dating Goodbye (1997) is pre-era but is a purity-culture text, not this current.
**Sourcing (B1 grade):** n/a in era (every anchor is 2015 or later). **Confidence notes:** —
**Church or movement/trend: movement/trend (out of era).**
**Register:** 0 edits and 1 structural operation (in the JSON): `retireEntry`, conditional on G-8.
**Links touching it:** 0. Its relations copy reaches IX.28, IX.30, IX.32 and IX.18; those lines are removed in this slice's drafts.
**Source notes:** (1) Every item documents 2015 or later. None carries into era 10. (2) The safety-clause material is not lost: the Facilitator governs real distress whatever the census holds.
**Open questions for Mark:** Q1 (IX.31) — Even with the cut-off moved to 2010, nothing in the row is dated 2010 or earlier, so it is out of the era. That reverses V1.0 Q9 (Mark's hand-selected retention, 2026-08-14). Options: (a) drop it from era 10; (b) fold a pointer into IX.28 — but that would be a claim about after 2010. Recommendation: (a). Two pre-2010 destination lines it carried could go elsewhere: the Coming Home Network (1993, verified) to IX.23's orbit, and Webber (1985) to the named Anglican gap. ACNA (2009) is now in era too, for the Anglican gap.
**Wanted:** none

#### IX.32 — The Narrative-Kingdom Renewal (the Bible as one story fulfilled in Jesus) (`the-narrative-kingdom-renewal-the-bible-as-one-s`)
**Disposition:** keep (end 2010) · **Tier:** Tier 2 (V1.0: Tier 2) · **Dates:** c. 1990-2010 (V1.0: c. 1990-present, 1990–2026) · **Living as of 2010:** yes — A teaching current active in 2010 (Wright's Surprised by Hope 2008, verified, and Simply Christian 2006 [S]; Willard; church curricula). P2-V flag: yes depends on reading 'living' as the tradition the entry names, not its episode window. It never had a body or members.
**Section A:** No plain-reading question. The floorNote rests on the in-era carrier texts: Newbigin 1989, Willard 1998, Wright 1992/1996/2008. **Section B:** B1 Moderate-to-rich (Wright's NTPG: title and publisher verified, year [S]; Surprised by Hope 2008 verified; Simply Christian 2006 [S]; the rest [S]; no monograph). B2 moderate (books, classrooms, curricula). B3 unique (story vs chart, against IX.29). B4 strong, but BibleProject (2014) and McKnight (2011), what participants will name, are after the era. B5 n/a. Tier 2 kept: Wright's popular books carry it to a general readership inside the era (Surprised by Hope 2008, verified; Simply Christian 2006, [S]).
**Sourcing (B1 grade):** Moderate-to-rich. **Confidence notes:** 'From about 1990 … spread through evangelical and mainline churches' — Widely Accepted. 'Church curricula adoption' in the sourcing field is undated ([S]).
**Church or movement/trend: movement/trend — a teaching current with no body; it belongs with the 'movements and trends' class.**
**Register:** 15 edits and 5 removals (in the JSON); fields touched: floorNote, legacy, longDescription, relationsSummary, sourcing, statusDescription, teaser, why. Story 1 (2014–19), the McKnight and BibleProject voices and their two source items are removed whole (G-39, G-10, G-26). The statusDescription and floorNote lose their process commentary. The sourcing line says no monograph had appeared by 2010.
**Links touching it:** 0.
**Source notes:** (1) Flag/drop McKnight (2011) and BibleProject (2014) — after the era. Keep Wright 1992/2006/2008, Newbigin, Willard, Guder 1998. (2) Story 0's sources list is a copy of the row's sources and does not include the autobiography and biography its caveat names — a defect, flagged. (3) Story 1's sources (2014–2020): drop with the story.
**Open questions for Mark:** Q1 (IX.32) — Its best-known carriers (McKnight 2011, BibleProject 2014) fall just after the era. Options: (a) keep, c. 1990–2010 at Tier 2 (drafted); (b) lower it to Tier 3; (c) drop. Recommendation: (a). Newbigin, Willard and Wright, popular books included, give a full 1990–2010 arc, and story 0 is strong history.
**Wanted:** Newbigin's own autobiography and the authorized biography named in story 0's caveat — titles to be confirmed and staged (not PD).

#### IX.33 — Fundamentalism (`fundamentalism-1910-1970s`)
**Disposition:** keep · **Tier:** Tier 1 (V1.0: Tier 1 (candidate signal)) · **Dates:** c. 1910-1970s (V1.0: c. 1910-1970s, 1910–1970) · **Living as of 2010:** yes — Separatist fundamentalist congregations and institutions were practicing in 2010. The window ends at the 1970s handoff. P2-V flag: yes depends on reading 'living' as the tradition the entry names, not its episode window.
**Section A:** No question — the movement's stated cause was the historic doctrinal content itself. **Section B:** B1 Rich (Niagara Creed 1878, Hodge-Warfield 1881, The Fundamentals 1910–15 and Laws 1920 all verified; Doctrinal Deliverance 1910, Scopes 1925 and 1929 [S]). B2 strong. B3 unique (one side of the IX.33↔IX.35 rupture). B4 strong (Mark-mandated). B5 n/a. The window is unchanged; nothing in the row passes 2000 except the present-tense continuation lines.
**Sourcing (B1 grade):** Rich. **Confidence notes:** NAE 1942, Fuller 1947, Graham 1957 and Moral Majority 1979 stay [S], as in V1.0.
**Church or movement/trend: movement/trend across denominations, which later formed churches of its own (OPC 1936; independent Baptists).**
**Register:** 6 edits (in the JSON); fields touched: legacy, statusDescription, teaser. The sixth is the conditional Q1 status copy (G-43).
**Links touching it:** 1 (IX.33→IX.35, 'broke with', Dominant Modern Reconstruction). The note is past-tense and clean. Flag only: V1.0 Q8 ruled this edge 'Documented', but the census carries Dominant Modern Reconstruction — for the link pass P2-L10.
**Source notes:** (1) All items: pre-2010 texts. Marsden 3rd ed. (2022) is a later edition — keep. (2) No vendored Library text bears on it (no Fundamentals, Machen or Scofield in cic/texts/).
**Open questions for Mark:** Q1 (IX.33) — Its statusDescription still reads 'Proposed for a future survey; not yet reviewed', which is stale after the 2026-08-14 Freeze adopted it. Options: (a) replace it with Tier 1 status copy in the form IX.23 uses (drafted, conditional: "Tiered Strong (Tier 1). It is assessed on its own dated texts, from The Fundamentals (1910–15) to the naming of 1920."); (b) leave it to the A3 statusWord harmonization backlog. Recommendation: (a). In §6 as G-43.
**Wanted:** The Fundamentals, 12 vols. (1910–1915) — PD — for the source-research thread.; A. A. Hodge and B. B. Warfield, 'Inspiration', Presbyterian Review (April 1881) — PD — for the source-research thread.; J. Gresham Machen, Christianity and Liberalism (1923) — PD by date — for the source-research thread.; The Scopes trial transcript, The World's Most Famous Court Trial (1925) — PD by date — for the source-research thread.; Minutes of the PCUSA General Assembly, 1910 (the Doctrinal Deliverance) — PD — for the source-research thread.; Curtis Lee Laws, Watchman-Examiner (1920), the naming article — PD — for the source-research thread.

### Cross-cutting questions (all rows in this slice)
X1 — The status sentence. Harmonized at assembly: the dated-reading sentence is dropped on every era 10 row, as in eras 1 to 9, rather than replaced (gate question G-3 offers the alternative).
X2 — Scholarship published after 2010 (Atto 2011, Adogame 2013, Stanley 2013, Hummel 2023, Kévorkian 2011, Suny 2015, Marti & Ganiel 2014 …). Options: (a) keep it as sources and scholar voices where it describes in-era history, never for post-2010 claims (drafted; voice lines like 'is the standard account' left as statements about the historiography); (b) remove it from participant-facing voices and keep it in sources only. Recommendation: (a).
X3 — Notes on the archive's own condition ('now largely link-rotted', 'fragile with the platforms', 'the Internet Archive is doing more…'; IX.28). These are present-day facts about the sources, not about the tradition, and the "What follows 2010" ruling makes no claim about today. Options: (a) keep them as sourcing notes; (b) recast them in the past. Recommendation: (b), drafted: "conference records kept on fragile platforms"; "the movement's real archive from 2002, kept on platforms that later decayed"; "It also left a preservation problem. A movement that documented itself almost entirely on platforms kept an archive that decayed with them." In §6 as G-46.
X4 — P2-V. 'Living as of 2010' depends on reading 'living' as the tradition an entry names, not its episode window or its lack of a body, for IX.18 (label), IX.21 (underground ended 1989), IX.22 (persecution ended 1991), IX.32 (teaching current, no body) and IX.33 (window ends 1970s). Each is set to yes and flagged.
X5 — Church or movement/trend, one line per entry, is in each section above. Movement/trend: IX.24, IX.25 (a trend carried by church bodies), IX.28, IX.29, IX.30, IX.32, IX.33 (later formed churches). Label: IX.18. Church: IX.19–IX.23, IX.26, IX.27.
X6 — Dropped stories leave gaps that are not filled: IX.28 story 1 (2011), IX.30 story 1 (2020–21) and IX.32 story 1 (2014–19). Each is removed whole, and each of those rows keeps one story. In §6 as G-39.

### 2c. IX.34–IX.49

Proposals only; nothing in the census is changed. Inputs: the census rows, `CiC_Step0_Era10_V1_0.md` §1–§6, `…Candidate_Entries_E.json`, `…Sources_E.json`, the Step 0 Methodology V1.0, `cic/texts/REGISTRY.yaml` and `cic/corpus-map/`. The whole JSON is checked by applying it in order to a copy of the census.

Common to every living row: the clause "This status is a dated reading of a living tradition, not a permanent verdict." comes out of `statusDescription`. It is the retired addendum's clause. Every "to today" in a teaser becomes "to 2010". No CD/CR grade appears in any census field of this slice, so none needed replacing. Every [S] mark from V1.0 is carried as it was, and none is upgraded.

V1.0 tier signals for these candidates: T1 for IX.34, IX.35 and IX.43; T3 for IX.49; T2 for the rest.

---

#### IX.34 — The Social Gospel (`the-social-gospel`)
**Disposition:** keep · **Tier:** 1 (V1.0: 1) · **Dates:** c. 1886–1918 (V1.0: same) · **Living as of 2010:** no. The movement ended by 1918, and its stream passed to IX.35. The answer does not turn on P2-V.
**Section A:** No floor question. Its claim concerned the Kingdom's social scope, not the doctrine of God. A3 does not arise. V1.0's reasoning holds.
**Section B:** B1 rich own corpus (1907 and 1918 verified). B2 a full world: pastorate, fellowship (1892), novel, newspaper week, creed. B3 the social-reform pole of the rupture cluster, distinct from IX.33 and IX.35. B4 pastors, historically interested learners, thoughtful believers; WWJD gives seekers a way in. B5 tiebreak only.
**Sourcing (B1 grade):** Rich: Rauschenbusch 1907/1912/1917, Gladden 1886 [S], Sheldon 1896 [S], the Social Creed 1908 (verified), Evans 2017 [S].
**Confidence notes:** The 1907–1918 gravity window stands on two verified anchors (V1.0 §5). The pre-1906 start is a disclosed reach-back. "The war's blow to its optimism" stays [S]. As an interpretive claim it would carry Dominant Modern Reconstruction.
**Register:** 1 edit. WWJD "is still in circulation" becomes "was still in circulation a hundred years after the novel".
**Links touching it:** 0.
**Open questions for Mark:** none.
**Wanted:** Christianity and the Social Crisis (1907), A Theology for the Social Gospel (1917), Applied Christianity (1886), In His Steps (1896), the Social Creed (1908). All PD — for the source-research thread.

#### IX.35 — The Mainline Century — Liberal Protestantism & Neo-Orthodoxy (`the-mainline-century-liberal-and-neo-orthodox`)
**Disposition:** keep · **Tier:** 1 (V1.0: 1) · **Dates:** c. 1900–1990 (V1.0: same; the 1990 end is the judgment handoff to IX.18, unchanged) · **Living as of 2010:** yes. The mainline bodies lived in 2010, though the window closes c. 1990. This depends on P2-V.
**Section A:** A real A3 shape exists inside the lane. Non-realist readings sit beside confessional reaffirmation, as at Barmen 1934. It is assessed per body and per dated text, never on the label. At world level the row clears under A5/Article 21, because its established strands include ones that meet the floor. The dated texts an A3 reading would start from are the Auburn Affirmation (1924) and the denominations' own confessions. No content claim is made here.
**Section B:** B1 rich; the rupture texts are verified. B2 a full world: seminaries as teaching offices, denominations, councils. B3 the only academic liberal-Protestant lane (the González find). B4 academically minded users, pastors, deconstructing Christians. B5 century-scale.
**Sourcing (B1 grade):** Rich: Fosdick 1922, Machen 1923, Auburn 1924, Barth 1919/22 and Bultmann 1941 are verified; Dorrien and Marsden verified; Longfield 1991 [S]; Niebuhr and Tillich [S].
**Confidence notes:** The mid-1960s membership peak is [S]. It is Widely Accepted, but no dated counter is cited.
**Register:** 6 edits. The present-tense hand-off to "what is now called progressive Christianity" is dated to c. 1990. "The mainline denominations are alive" becomes "were alive in 2010". The floorNote's "reaches into the present" becomes "reaches past 1990".
**Links touching it:** 1 (fundamentalism → IX.35, "broke with"). Its note is past tense.
**Open questions for Mark:** 1. P2-V: should living:true stand on the bodies rather than the window? (a) keep true; (b) false for episode-window rows. Recommend (a).
**Wanted:** Fosdick 1922, Machen 1923, the Auburn Affirmation 1924, Briggs 1891/1892–93 and Harnack (trans. 1901) are all PD — for the source-research thread. A dated membership counter for the 1960s, not PD.

#### IX.36 — New Calvinism (Young, Restless, Reformed) (`new-calvinism-young-restless-reformed`)
**Disposition:** keep. It was a drop at the 2000 cut-off and is now re-assessed under the 2010 ruling. · **Tier:** 2 (V1.0: 2) · **Dates:** c. 1998–2010 (V1.0: c. 1998–present) · **Living as of 2010:** yes. Acts 29, TGC, T4G and their churches were active networks in 2010.
**What changed with 2010:** The movement's naming (Hansen, 2006/2008), its institutions (TGC 2004–07, T4G from 2006) and its common confession (TGC 2007) now fall inside the window. Its defining crisis does not: the Acts 29 handoff (2012), Driscoll's removal and Mars Hill's dissolution (2014), T4G's end (2022), Cosper's podcast (2021) and Keller's death (2023) all fall after 2010. The R7 recency argument is retired with the addendum.
**Section A:** It clears A1 on a dated own-voice text, TGC's Confessional Statement adopted at the 2007 launch (verified). The floorNote's "TGC founding documents 2005" is corrected to 2007, per V1.0's verified resolution of the TGC dating.
**Section B:** B1 rich in window. B2 a real lived world: conferences, church-planting, publishing, Redeemer's parish life after 9/11. B3 the child of IX.24 and the sibling of IX.28; distinct. B4 young evangelicals, pastors, deconstructing Christians. B5 moderate.
**Sourcing (B1 grade):** Rich: Hansen 2006 and 2008, TGC 2004–07 and Acts 29 1998 are verified. Mars Hill 1996 and T4G 2006 each carry a verification divergence, kept. Piper 1986 [S]. Vermurlen 2020 [S].
**Confidence notes:** none new.
**Register:** 13 edits and 2 removals. The 2014 crises come out of why, legacy, relationsSummary and sourcing. "(2006–2022)" becomes "(from 2006)". The podcast voice is replaced from the row's own story by Mars Hill Church (1996), and the podcast's source item is removed whole. Keller's 2023 death comes out of story 1, and so does its caveat's "last words" and "now dead" line: "He was a public figure, and the page does not assess his theology." Story 0 is removed whole (G-11). The legacy becomes "In 2010 it was a living current, and a young one: its main institutions were only a few years old." Piper's voice reads "was the current's most-cited earlier text".
**Links touching it:** 0.
**Open questions for Mark:**
1. documentedStories[0], "The Year Mars Hill Came Apart" (March–October 2014), lies wholly after 2010. (a) Remove it whole (a `removeItem` operation) and leave the slot empty until a 1998–2010 story is drafted from cited sources [recommended]. (b) Keep it as a disclosed one-step-past note.
2. Confirm keep at Tier 2 under the 2010 ruling. The MacArthur placement (V1.0 Q3; Strange Fire 2013 is post-2010) stays as V1.0 left it.
**Wanted:** none.

#### IX.37 — Indonesian Christianity — the Independent Century (`indonesian-christianity-the-independent-century`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1906–2010 (V1.0: 1906–present) · **Living as of 2010:** yes. The HKBP, GMIT and the Javanese churches were living.
**Section A:** No question. The churches are Lutheran, Reformed and Catholic, and confessional.
**Section B:** B1 moderate-to-rich. B2 a full world: revival, mass conversion, a church under Pancasila. B3 the only era-10 Indonesian row; it receives VIII.26. B4 historically interested learners and thoughtful believers; the 1965–71 conversions raise hard questions for pastors. B5 large.
**Sourcing (B1 grade):** Moderate-to-rich: HKBP 1930 (verified); Tari 1971, Peters 1973, Willis 1977, Cribb 1990 and Aritonang & Steenbrink 2008 [S]; the GMIT records (access limited).
**Confidence notes:** The superlative "among the largest Lutheran bodies" was V1.0's unclassed scale claim. It is removed, not regraded, because no counter is cited. "One of the largest Christian populations in the Muslim-majority world" stays as Widely Accepted. The death toll of 1965–66 stays a range, as written.
**Register:** 13 edits. The Lutheran superlative comes out of three fields and one voice. The Pancasila line is dated "in the decades that followed". "Both books are still read" becomes "The church they describe went on." "Whose grandchildren are the church now" comes out, with the gap left. The historiography sentence moves to the past tense.
**Links touching it:** 1 (indonesian-christianity → IX.37). Flag: its note says "It is the same church, the HKBP", in the present tense.
**Open questions for Mark:** 1. The HKBP scale claim. (a) Drop [drafted, recommended]. (b) Re-date it "by 2010" as Widely Accepted with no counter. (c) Restore it once LWF figures are cited. Recommend (a) now, (c) later.
**Wanted:** LWF membership figures for the HKBP (not PD). Indonesian census religion tables, 1971/1990 (not PD).

#### IX.38 — Northeast India & the Mar Thoma Church — the 20th Century (`northeast-india-and-mar-thoma-twentieth-century`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1906–2010 (V1.0: 1906–present) · **Living as of 2010:** yes. Both church families were living.
**Section A:** No question.
**Section B:** B1 moderate. B2 a full world: revival, hymnody, war and mediation, convention life. B3 receives VIII.27; the bridge lane is kept. B4 historically interested learners; the Mizo accord story serves pastors. B5 regional scale.
**Sourcing (B1 grade):** Moderate, down from the census's "Moderate to rich". Every anchor is [S]: the revival waves, the scale claim, the Mar Thoma century, Frykenberg 2008, Downs 1992. The Mizo and Malayalam records sit under access flags.
**Confidence notes:** "Mizoram and Nagaland among the most heavily Christian regions on earth" was the B5 claim V1.0 flagged. It is already in the past tense ("became, on the usual counts"). Proposed grade: Widely Accepted, pending a census counter. The Maramon crowd of 1918 stays collected tradition, as tiered.
**Register:** 13 edits. The hymnody "is now" becomes "became". The accord "has held for four decades" becomes "was still holding in 2010, more than twenty years on". The convention's "crowds in the hundreds of thousands" comes out, with no date for that figure. The legacy is dated to 2010. The pandal passage moves to the past tense.
**Links touching it:** 1 (era-9 Northeast India → IX.38). Past tense.
**Open questions for Mark:** 1. The scale claim's grade. (a) Widely Accepted as written [recommended]. (b) Hold it out until a counter is cited. In §6 as G-44.
**Wanted:** Census of India 1991 religion tables (not PD). Any pre-1930 English mission report of the Mizo revivals — PD — for the source-research thread. Also, `sources[0].note` says the hymnody "is now" the church's practice. The sources field was outside this pass; flagged.

#### IX.39 — The Malankara Churches — Orthodox & Jacobite (`the-malankara-churches-orthodox-and-jacobite`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1912–2010 (V1.0: 1912–present) · **Living as of 2010:** yes. Both churches were living.
**Section A:** No question. Both are Oriental Orthodox. One row holds both wings, so the roster takes no side, as in V1.0.
**Section B:** B1 moderate-to-rich. B2 a full world: liturgy, Catholicate, litigation as ecclesiology. B3 the ancient St Thomas majority, otherwise invisible after 1889. B4 historically interested learners and the diaspora. B5 regional.
**Sourcing (B1 grade):** Moderate-to-rich: 1912, 1958, 1975 and 1995 verified; the 1934 constitution [S]; both churches' records [S]; the court record beyond the cluster [S]; Frykenberg [S].
**Confidence notes:** The validity of the 1912 consecration is Contested; both positions are stated, and that stays.
**Register:** 17 edits. The 2017 Supreme Court ruling comes out of every field (sourcing, why, relationsSummary, longDescription, legacy, voices, story). The 1995 ruling becomes the last dated court event. The 2012 centenary literature comes out of voices[1]. "Still in force, depending on whom you ask" becomes "each side went on holding its own act to be the valid one".
**Links touching it:** 1 (era-9 Northeast India → IX.39, "broke with"). Past tense.
**Open questions for Mark:** none.
**Wanted:** The 1958 Supreme Court judgment (a public record, not a Library text). The 1934 constitution text (rights unclear). Library: three pre-window texts are mapped to this id: `howard_christians-of-st-thomas-and-their-liturgies_1864.txt`, `philipos_syrian-christians-of-malabar_howard1869.txt` and `whitehouse_lingerings-of-light-in-a-dark-land_1873.txt`. They are background, not 1912–2010 evidence. Trim the 2017 ruling from `sources[]` at the census pass (partial items, G-26).

#### IX.40 — The Georgian Orthodox Church Restored (`the-georgian-orthodox-church-restored`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1917–2010 (V1.0: 1917–present) · **Living as of 2010:** yes.
**Section A:** No question.
**Section B:** B1 moderate. B2 a full world: restoration, martyrdom, Soviet survival, national church. B3 the Caucasus lane resumes here. B4 historically interested learners; the persecuted-church theme. B5 national.
**Sourcing (B1 grade):** Moderate: 1917 and 1943 verified. The 1990 tomos is survey-verified but held [S] by the sources run; the divergence stays disclosed. Ambrosi 1922 [S]. Kyrion's death in 1918 [S], its cause unresolved. Kartvelishvili verified. Grdzelidze et al. 2006.
**Confidence notes:** The cause of Kyrion II's death is Contested and is left open, as the record leaves it.
**Register:** 11 edits. Ilia II "has been" Catholicos-Patriarch becomes "became … in 1977 and still held the office in 2010". The post-Soviet line is dated "in the years after". "Is now uncontested" becomes "after which no one contested it". "He is commemorated as a hieromartyr" comes out: the canonization is undated and may be post-2010, and the gap is left. The legacy line on thin English scholarship is put in the past: "English-language scholarship on the modern Georgian church was thin, and this map names that thinness rather than papering over it."
**Links touching it:** 0.
**Open questions for Mark:** 1. Kyrion's commemoration. (a) Leave it out until it is dated [recommended]. (b) Restore it undated, as "later commemorated".
**Wanted:** The date of Kyrion II's canonization. Ambrosi's 1922 Genoa memorandum in a 1920s printing — PD — for the source-research thread.

#### IX.41 — Churches of Christ (`churches-of-christ-twentieth-century`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1906–2010 (V1.0: 1906–present) · **Living as of 2010:** yes.
**Section A:** Clears A1 on the plain reading. The Frozen VIII.3 finding carries: the content is confessed, subscription is refused. No dated creed exists by design, and that is stated, not blurred. A3 does not arise.
**Section B:** B1 rich in existence, but every anchor is [S]. B2 a full world: a cappella worship, journals as government, colleges, missions, the Keeble story. B3 one wing of the 1906 division; IX.42 is the other. B4 thoughtful believers and pastors, plus the segregation story. B5 moderate.
**Sourcing (B1 grade):** Rich: the journals, Hughes 1996, the Stone-Campbell Encyclopedia 2004, Harrell 2000. The 1906 census anchor is verified but inherited from VIII.3.
**Confidence notes:** The "two thousand congregations, perhaps a tenth" figure is approximate, as stated.
**Register:** 14 edits. Present-tense descriptions of the body ("recognize", "confess", "still have no headquarters", "is still the practice", "both say the other left") move to the past or are dated to 2010. The floorNote is dated "through the century".
**Links touching it:** 1 (Stone-Campbell → IX.41). Past tense.
**Open questions for Mark:** none.
**Wanted:** U.S. Census Bureau, Religious Bodies: 1906 (1910) — PD — for the source-research thread; it settles the start anchor first-hand. The Gospel Advocate, 1906 volumes — PD.

#### IX.42 — Disciples of Christ & the Independent Christian Churches (`disciples-of-christ-and-independent-christian-churches`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1906–2010 (V1.0: 1906–present) · **Living as of 2010:** yes, both streams.
**Section A:** As IX.41 (the parent finding carries).
**Section B:** B1 rich in existence; every anchor [S]. B2 a full world: the Design, the ecumenical commitment, the Peoples Temple oversight question. B3 the second wing, with the third stream disclosed in the row (V1.0). B4 pastors and historically interested learners. B5 moderate.
**Sourcing (B1 grade):** Rich: the 1968 Design, McAllister & Tucker 1975, the Encyclopedia 2004, Webb 1990/2003, Hall 1987.
**Confidence notes:** The withdrawal counts vary between sources, as stated.
**Register:** 7 edits. The legacy is dated to 2010 ("Both streams were alive in 2010"). "Still cooperate" becomes "Afterward … cooperated". "Has not been answered" becomes "went unanswered".
**Links touching it:** 1 (Stone-Campbell → IX.42). Past tense.
**Open questions for Mark:** none.
**Wanted:** Religious Bodies: 1906, the Disciples entry — PD — for the source-research thread.

#### IX.43 — The Black Church in the Twentieth Century (`the-black-church-in-the-twentieth-century`)
**Disposition:** keep · **Tier:** 1 (V1.0: 1) · **Dates:** 1906–2010 (V1.0: 1906–present) · **Living as of 2010:** yes.
**Section A:** No question.
**Section B:** B1 rich in existence, but V1.0 verified no anchor and staged no base. B2 the fullest world in the slice. B3 receives VIII.1; distinct from IX.1's worship lane. B4 the marginalized-voices duty and every named audience. B5 century-scale.
**Sourcing (B1 grade):** Rich: denominational records, the SCLC papers, Cone 1969–70 [S]; Branch 1988, Fitts 1985 and McWhorter 2001 in the stories.
**Confidence notes:** How Wright fell in 1961 is Contested between the parties, and that is stated.
**Register:** 7 edits. The 2001 and 2002 convictions stay: they are in window and cited. "Which is in the wall now" becomes "which was set into the wall". The legacy is dated, and its "until now nothing carried it" becomes "no entry carried it before this one".
**Links touching it:** 1 (VIII.1 → IX.43). Past tense.
**Open questions for Mark:** none.
**Wanted:** Carter G. Woodson, The History of the Negro Church (1921) — PD — for the source-research thread. COGIC's printed record before 1930 — PD where it exists.

#### IX.44 — The Seventh-day Adventist Church in the 20th Century (`seventh-day-adventist-church-twentieth-century`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1906–2010 (V1.0: 1906–present) · **Living as of 2010:** yes.
**Section A:** A1 is resolved on dated own-voice texts: the 1931 yearbook statement and the 1980 Dallas Fundamental Beliefs, both explicitly trinitarian and both verified. This completes the Frozen VIII.10 window question as V1.0 recorded. The history ruling does not move it. The floorNote's "a living body can go on to change its confession" is the retired addendum's caveat. It is replaced by "dated texts of 1931 and 1980; no later text before 2010 is cited here." A revision inside the window, if any, must be checked first (see Wanted).
**Section B:** B1 rich. B2 a full world: Questions on Doctrine, Glacier View, a global institution. B3 the register family's one charged era-10 segment. B4 participants from the body, plus seekers asking "is it Christian?". B5 large.
**Sourcing (B1 grade):** Rich: 1915, 1931 and 1980 verified; Knight 2000; Questions on Doctrine 1957; Andreasen 1959; Ministry 1980. V1.0 staged no base.
**Confidence notes:** "Some twenty-two million members by its own count" is not dated to 2010 or earlier. It comes out of three fields. No dated figure is cited, so the gap is left.
**Register:** 12 edits. The membership figure comes out. The floorNote caveat is replaced. "Has never closed" becomes "did not close"; the 2003 reissue stays. Ford's 2019 death and the undated "has since revisited" clause come out.
**Links touching it:** 1 (VIII.10 → IX.44). Past tense.
**Open questions for Mark:** 1. The VIII.10 completion, recorded on IX.44 with a closure note on VIII.10 (V1.0 Q6), is unchanged by the ruling. Confirm no reopening. Recommend no change. In §6 as G-48.
**Wanted:** The General Conference session records 1985–2010: any revision of the Fundamental Beliefs inside the window must be checked before the floorNote's "no later text" line stands (not PD). The GC statistical report for 2010 (not PD), only if a scale line is wanted. Ellen G. White's writings before 1915 — PD — for the source-research thread. The 1931 statement enters US public domain in 2027.

#### IX.45 — Charismatic Renewal & the Jesus Movement (`charismatic-renewal-and-the-jesus-movement`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1960–1980s (V1.0: same; a real episode window, not an open end) · **Living as of 2010:** yes. The wave subsided, but its bodies lived. This depends on P2-V.
**Section A:** No question.
**Section B:** B1 rich; the four anchors are verified. B2 a full world: worship, music, communes, parish renewal. B3 the North Atlantic middle between IX.1 and IX.11. B4 seekers, deconstructing Christians, pastors. B5 large.
**Sourcing (B1 grade):** Rich: Bennett 1970, Synan 1997, Newsweek and Time 1960 and 1971; the Frisbee documentary 2005; the Frisbee memoir 2012 and Eskridge 2013 (post-2010 works about earlier events, flagged). V1.0 staged no base.
**Confidence notes:** The claim that both movements left Frisbee out of their histories rests on checkable published histories, as stated.
**Register:** 5 edits. The New Calvinist and 2000s church-planting lines stay, now inside the window. "Live on" becomes "lived on". "Is now the default" becomes "spread through". Calvary Chapel and the Vineyard are dated to 2010.
**Links touching it:** 0.
**Open questions for Mark:** 1. P2-V, as at IX.35. Recommend living:true.
**Wanted:** none.

#### IX.46 — The Ecumenical Movement & the World Council of Churches (`the-ecumenical-movement-and-the-wcc`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1921–2010 (V1.0: 1921–present) · **Living as of 2010:** yes.
**Section A:** A council, not a confession-bearing body. Member confessions are assessed per body only. The WCC Basis stays uncited, as V1.0 struck it; the gap stays named.
**Section B:** B1 rich. B2 an institution-world rather than a congregational one: conferences, assemblies, the PCR story. B3 receives VIII.25; the counterpart to IX.24. B4 academically minded users and pastors. B5 century-scale.
**Sourcing (B1 grade):** Rich: IMC 1921, Amsterdam 1948 and New Delhi 1961 verified; L&W 1925 and F&O 1927 [S]; Bate 1927; Rouse & Neill 1954; Sjollema 2015 (post-2010, about earlier events).
**Confidence notes:** none new.
**Register:** 9 edits. The council's nature, the Orthodox membership and the Catholic relation all move to the past. The legacy is dated to 2010. "Written by both parties still" becomes "both parties went on writing its history".
**Links touching it:** 1 (SVM/Edinburgh 1910 → IX.46). Past tense.
**Open questions for Mark:** none.
**Wanted:** Bate (ed.), Lausanne 1927 Proceedings — PD — for the source-research thread. World Missionary Conference 1910 Reports — PD. The Amsterdam 1948 Basis (not PD), needed before the Basis can be cited.

#### IX.47 — The Catholic Church — Pius X to the Eve of the Council (`the-catholic-church-pius-x-to-the-council`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1906–1962 (V1.0: same; both ends principled) · **Living as of 2010:** yes. The church lived; the window closes in 1962 and hands to IX.23. This depends on P2-V.
**Section A:** No question.
**Section B:** B1 rich in existence; every anchor [S]; no staged base. B2 a full world: the modernist crisis, the worker-priests, ressourcement. B3 fills the 1906–1962 Roman hole. B4 historically interested learners and Catholic participants. B5 century-scale.
**Sourcing (B1 grade):** Rich: the anti-modernist documents, Divino Afflante Spiritu, Petre 1912, Sagovsky 1990, Arnal 1986, Poulat 1965.
**Confidence notes:** The Pius XII wartime record stays Contested in copy. The edit dates the argument "for decades afterward".
**Register:** 3 edits. "Is still argued about" becomes "was argued about for decades afterward". "There are worker-priests in France today" comes out, with the gap left.
**Links touching it:** 1 (long-19th-century Catholic → IX.47). Past tense.
**Open questions for Mark:** 1. P2-V. Recommend living:true.
**Wanted:** Pascendi and Lamentabili (1907), the oath Sacrorum antistitum (1910), Petre, Life of Tyrrell (1912), and Tyrrell, Christianity at the Cross-Roads (1909). All PD — for the source-research thread.

#### IX.48 — American Orthodoxy — Autocephaly & the Convert Wave (`american-orthodoxy-autocephaly-and-the-convert-wave`)
**Disposition:** keep · **Tier:** 2 (V1.0: 2) · **Dates:** 1970–2010 (V1.0: 1970–present) · **Living as of 2010:** yes.
**Section A:** No question.
**Section B:** B1 moderate-to-rich. B2 a full world: autocephaly, the St Herman canonization, the EOC reception. B3 receives IX.9; distinct from IX.22. B4 seekers and deconstructing Christians, with the post-2010 wave set aside. B5 small. The 1970–2010 story is solid and stands without the post-2000 wave.
**Sourcing (B1 grade):** Moderate-to-rich: 1987 and 1989 verified; 1970 [S]; Stokoe & Kishkovsky 1995; memoirs [S]; Ancient Faith media from 2004; Slagle 2011 (a post-2010 study of 2000s conversions, flagged).
**Confidence notes:** The validity of the 1970 autocephaly is Contested, with Constantinople's objection stated. That stays.
**Register:** 13 edits and 1 removal. Ancient Faith Radio (2004) stays, re-dated "from 2004". Hanegraaff (2017) and "the deconstruction era's channels" come out of why, teaser, longDescription and relationsSummary, and the Hanegraaff source item is removed whole. Slagle's study is labeled as later: "The one dedicated scholarly study, Amy Slagle's fieldwork, was published later, in 2011." The Hanegraaff voice is replaced from the row's own story by Patriarch Alexy I (1970). "And continue to" becomes "went on withholding recognition through the century".
**Links touching it:** 1 (Alaskan mission → IX.48, graded Inferential-Thin). Past tense.
**Open questions for Mark:** 1. Name. (a) Keep "& the Convert Wave"; 1987 was a wave [recommended]. (b) "& the Convert Stream". In §6 as G-45. The row's overlayCurrent:true is a site-wide question (G-7), flagged rather than ruled here.
**Wanted:** A pre-2010 jurisdictional report on convert numbers (not PD).

#### IX.49 — Hebrew Roots & Torah-Observance Movements (`hebrew-roots-and-torah-observance-movements`)
**Disposition:** keep. It was a drop at the 2000 cut-off and is now re-assessed under the 2010 ruling. · **Tier:** 3 (V1.0: 3) · **Dates:** c. 1990s–2010 (V1.0: c. 1990s–present) · **Living as of 2010:** yes. FFOZ, the One-Law teachers and the Sacred Name assemblies were active.
**What changed with 2010:** The current's one well-documented argument, FFOZ's 2009 shift from One Law to Divine Invitation and the rebuttals (verified, both sides dated), now falls inside the window. 119 Ministries (c. 2010 [S]) sits at its edge. FFOZ's statements on the cost of the change are dated 2010–11; the 2011 part falls outside, so it is flagged.
**Section A:** Per body only, never on the label. Some Sacred Name bodies carry non-trinitarian confessions by their own dated statements (Assemblies of Yahweh 1969 [S]).
**Section B:** B1 thin. B2 thin but real: Sabbath and feast-keeping, study groups, one documented internal argument. B3 distinct from IX.13. B4 participants will ask. B5 no counter exists.
**Sourcing (B1 grade):** Thin: FFOZ 1992 and 2009 verified; Hegg 2009; The Faith 1937 [S]; Melton 2009; Nickels 1977/1999.
**Confidence notes:** none beyond the [S] dates.
**Register:** 13 edits. "Since the 1990s … has taken up" becomes "From the 1990s … took up", in why and longDescription. Identity statements move to the past. The legacy is dated to 2010. "Have marked the current's two wings since" becomes "by 2010 … marked". The map-voice lines on platform fragility stay. Story 0's caveat drops "are living".
**Links touching it:** 0.
**Open questions for Mark:** 1. Disposition. (a) Keep with end 2010, Tier 3, as V1.0 leaned [recommended]. (b) Fold into named lines elsewhere (V1.0 found the IX.13 host too costly). (c) Drop.
**Wanted:** The Faith (Warren, Ohio), from 1937. Rights are unclear (check renewal); for the source-research thread. FFOZ's 2010 statement on the cost of the change, by date.

## 3. The held candidate IX.50, judged as history to 2010

**This is Mark's direct ruling. Nothing below decides it.**

**What survives the 2010 close.** These anchors come from V1.0's own research, with their verification marks unchanged:
- Moral Majority founded 6 June 1979 [S];
- the Religious Roundtable's National Affairs Briefing, Dallas, 21 August 1980, with Reagan's "I endorse you and what you're doing" (verified);
- Moral Majority dissolved in 1989 (verified);
- the Christian Coalition founded in 1989 by Pat Robertson, with Ralph Reed as executive director (verified);
- Limbaugh's national program from 1 August 1988 and Fox News from 7 October 1996 (both verified, as media carriers only);
- the Faith and Freedom Coalition founded on 14 May 2009 by Reed, and Falwell's death on 15 May 2007 (both verified; back inside the era, below).

**Date to re-check (R1-C3).** V1.0 carries the Dallas briefing as 21 August 1980, verified. Reagan's
address is usually dated 22 August; the briefing ran 21–22 August. The participant text says only
"August 1980", so nothing shown is wrong. Re-check before any finer date is published.

**What drops out.**
- **Post-2010 events:** the BJC/FFRF January 6 report (2022); Limbaugh's death (2021) and Robertson's (2023).
- **The name "Christian Nationalism":** the naming wave that made it the movement's common label is 2019–2022, after the era.
- **Back inside the era (2010 revision):** the Faith and Freedom Coalition, founded 14 May 2009 by Reed (verified); Falwell's death on 15 May 2007 (verified).
- **Kept, but only as secondary scholarship:** Whitehead & Perry 2020, Du Mez 2020, Stewart 2020 and Gorski 2019/2020 may still be cited as histories of the pre-2010 current, the way eras 1–9 cite modern scholars. They are not evidence of anything after 2010.

**Re-assessment by the Step 0 standard.**
- **Name, if adopted:** "The Christian Right", as draft D-E6 carries it. Not "Christian Nationalism", whose naming wave (2019–2022) is after the era. The naming is Mark's own sub-choice under G-15. The draft's id still reads `christian-right-and-christian-nationalism`; ids are permanent, so it must be settled before first publication.
- **Dates:** start 1979. That start rests on an [S] date, while 1980 is verified. End 2010.
- **Living as of 2010:** yes. The Faith and Freedom Coalition was founded in 2009 (verified), so the current was organizing inside the era's last two years.
- **Section A:** still no independent confession to test, and the finding is still provisional. Its three legs are the founders' circle, Falwell's "coalition of moralists" and Whitehead & Perry's definition, and all three remain [S]. With history to 2010, the third leg becomes a later scholar's description of the 1979–2010 current, which is a legitimate use.
- **B1:** Moderate-to-rich. Eight dated anchors, seven of them verified, plus independent scholarship.
- **B2:** Thin. This is unchanged and is the crux.
- **B3:** Real. No row owns this political shape that cuts across church bodies.
- **B4:** Strong.
- **B5:** Large, which is a tiebreak only.
- **Tier:** 3.

**What is new since V1.0.** Mark's 2026-11-08 direction ("movements or trends, not the organization … clearly Christian movements") gives the gate a frame V1.0 lacked. The Christian Right is that kind of thing: a movement outside formal church bodies, carried by organizations (Moral Majority, the Christian Coalition). If Mark adopts a distinct kind for such movements (§4, D-Q8), IX.50 would fall under it. Its thin formation ecology would then be disclosed as the mark of that kind, not counted as a failure to be a church.

**D-Q7 (Mark's direct ruling).**
- (i) **Adopt it as a Tier 3 row, 1979–2010.** Revised draft D-E6 is in the companion JSON's `newEntries`. The post-2010 material is removed, and B2's thinness is written into the row's own copy.
- (ii) **Disclosure lines only, on IX.33 and IX.24.** V1.0's drafted IX.24 clause must change from "(1979– )" to "(1979–2010)". The IX.33 line stays as it is ("Moral Majority 1979").
- (iii) **No row and no lines.**

**Lean (advisory; the ruling is Mark's).** The lean depends on the outcome of D-Q8.
- If Mark adopts a movement kind under D-Q8, take (i), filed under that kind. The frame then fits what the record shows.
- If he does not, take (ii). A Tier 3 row whose formation lens is thin, filed as if it were a church body, describes it worse than two honest disclosure lines do.

Either way, V1.0's copy rules stand:
- dated, published record only;
- no characterization of living persons;
- nothing about Fox News's programming beyond its founding facts.

---

## 4. Movements outside formal church bodies

**Mark's direction, as relayed:** "they are movements or trends, not the organization, like bible translation, or campus ministries or church planting or world missions (remote) post war, children ministries and sunday school ministries, it may be marked differently than churches, but they were clearly christian movements". His further examples: "10/40 window"; "unreached people groups and church planting movements".

**Unit rule (Mark's):** the entry is the movement or trend. Organizations (Wycliffe/SIL, Cru, InterVarsity/IFES, YWAM, OM, World Vision and others) appear only as named carriers inside an entry. They never get entries of their own.

#### 4A. Existing rulings (Atlas Decision-Log and the V1.0 record)

1. **2026-07-16, fifth pass (Mark: "include all"), Amendment B.** Approved:
   - rows of exactly this kind in era 9: **VIII.24 The Sunday School & Bible-Institute Movement** and **VIII.25 The Student Volunteer Movement & Edinburgh 1910**;
   - two scope rules: *"formation communities, not schools of thought"* and *"events/councils are context except where a lived world expresses them"*;
   - **the "Bible-translation cross-era theme thread"**, which the External Review frames as "a cross-era hover-discoverable thread, **not new rows**".

   So the census already admits movements outside church bodies as rows, and VIII.24's own statusDescription leaves open "whether this is a tradition, or a set of formation methods operating inside other traditions". **But Bible translation specifically has a prior ruling: a theme thread, not rows. A Bible-translation entry would be a change order to that ruling.** The External Review also listed "the ecumenical movement / WCC" as "context". V1.0's gate later overrode that by adopting IX.46.
2. **2026-07-16, nineteenth pass:** the **Overlay Current** form (`overlayCurrent`, rendered as "wet ink"). It exists for entries that "overlay other more established movements". That is the closest existing device for a movement drawn differently from a church (see D-Q6 and D-Q8).
3. **Family Tree Decision-Log, decision 14:** a **movement-or-person `kind` field**, kept separate from status (Build-Plan **P2-G2**, still to do).
4. **Family Tree Decision-Log, decision 15:** three marks: dot (ended), leaf (living), portrait (person).

**Nowhere does the method or a frozen ruling say how movements outside church bodies are scored under Section A**, which tests a confession, and such a movement has none of its own. V1.0 handled the nearest cases (IX.24, IX.46, IX.29, IX.30, IX.32) with the "carrier device": per-body assessment through the carriers' dated texts, as Article 21's "assessed at the world level against its established strands". **D-Q10** asks Mark to confirm that rule for this kind.

#### 4B. How a movement entry is told apart from a church entry (D-Q8. Mark decides.)

**A naming problem comes first.** The census already calls every entry a "movement" (`movements[]`), and the P2-G2 kind field is "movement-or-person". So "movement" cannot also be the name for this new kind without colliding. Possible names for the new kind's value: `current`, `crosscurrent`, or `cross-church movement`. **`current`** is used below as a working term only.

**Data options:**
- **(D1)** Add a third value to P2-G2's kind field: `kind: "church" | "current" | "person"`. The existing "movement" value is renamed "church" or "body". **Recommended:** one orthogonal field, as decision 14 intended. A current keeps the same record, page, links, grades and permanent ID.
- **(D2)** Keep kind as movement/person and reuse the existing `overlayCurrent: true` flag to mean "current". This is cheap. But it already carries the "still forming" meaning, and nine rows have it set, some of which are church-shaped (IX.48 American Orthodoxy, for one).
- **(D3)** A new lane ("Cross-Family currents") instead of a kind. There is precedent: IX.18 sits in lane "-" (Cross-Family, laneOrder 50). But it mixes "where it sits" with "what it is", the same mistake decision 14 avoided for persons.

**Drawing options:**
- **(R1)** Draw a current as a translucent band across the lanes it touches, behind the church marks, with its own legend row. This builds on the wet-ink overlay but drops the fade at the right edge, since the era is now history. **Recommended:** it shows the thing a current is, running through many churches at once.
- **(R2)** Its own mark shape (a fourth shape beside dot, leaf and portrait, for example a ring or a chevron) in the current's home lane. This is simple, but it hides the "across many bodies" fact.
- **(R3)** A separate "Currents" band above or below the lanes, with links down into the churches that carried each one. Very clear, but it takes vertical space on phones.
- **(R4)** No visual difference; only a badge on the page. This is the lowest cost, but it ignores Mark's "may be marked differently".

**Recommendation: D1 + R1.**
- D1 reopens P2-G2's schema item, which is still marked to do, so the timing is right.
- R1 renders inside P2-K1's "2 to 4 options rendered for Mark" step.
- **Retroactive scope (portfolio-level, so Mark's):** if a current kind is adopted, the following would be candidates for it:
  - era 9: VIII.2 (revivalism) and VIII.4 (Holiness);
  - era 10: IX.24, IX.29, IX.30, IX.32 and IX.46.
- That is a cross-era decision, listed here and not proposed.

#### 4C. The movements, judged one by one as history to 2010

The same standard applies to each: Section A (through the carriers' dated texts, per D-Q10), B1–B5, Tier, and living as of 2010. **Repo anchoring is thin across the board. Only what the repo already holds is stated.** Drafts and skeletons are in the companion JSON's `newEntries`.

**M1. Bible translation in the 20th century.**
- **In-repo anchors:**
  - VIII.7's legacy: "Hundreds of languages got a written form, a grammar and printed books for the first time." That is about the era-9 missions, but it is the direct lead-in.
  - VII.10's 1804 BFBS story and VIII.31's Russian Bible Society: earlier eras.
  - Sanneh, *Disciples of All Nations* (OUP, 2008) [S], cited in the era-10 sources research.
- **Not in-repo:** every 20th-century carrier fact, including the Wycliffe/SIL founding and the United Bible Societies.
- **Section A:** no confession of its own. The carriers' statements (for example Wycliffe's) are not staged, so A is not yet assessable on dated texts.
- **B1:** Thin in-repo.
- **B2:** Not yet assessable: no source is cited. The judgment held for when a base exists: moderate (translators' communities, language work, reception by local churches).
- **B3:** High. No row holds it.
- **B4:** Strong for learners and believers.
- **B5:** Large.
- **Tier:** a Tier 2 signal, *pending a base*.
- **Living in 2010:** yes, as a judgment. This needs a dated source.
- **D-Q11 (a change order to the 2026-07-16 theme-thread ruling):**
  - (a) A current entry, "Bible translation movements, 1906–2010", as skeleton D-E4.
  - (b) Keep the theme thread, and add the 20th century to it as named lines in the receiving entries.
  - (c) Both: an entry plus the cross-era thread. **Recommended**, since Mark's new direction names Bible translation first. But it is a change order, so it is Mark's to name. Draft only once a base exists.

**M2. Student and campus movements.**
- **In-repo anchors:**
  - VIII.25: the SVM "never got over the First World War", and "by the middle of the century it had in effect come to an end";
  - Parker, *The Kingdom of Character* (1998);
  - Hopkins, *John R. Mott* (1979);
  - IX.48's story: Campus Crusade staff (Gillquist, Braun, Sparks) left in the late 1960s;
  - Bebbington, *Evangelicalism in Modern Britain* (1989), cited on VIII.4, which covers the British student-evangelical line as background. The repo cites it for Keswick, not for student work.
- **Carriers Mark named (founding dates not in-repo):** the SCM/WSCF, IVF/InterVarsity/IFES, the Navigators, Campus Crusade.
- **Section A:** via the carriers' dated statements; not staged.
- **B1:** Thin-to-moderate in-repo.
- **B2:** Not yet assessable: no source is cited. The judgment held for when a base exists: moderate-to-rich (small groups, camps, conferences, a discipleship method).
- **B3:** High. It is the successor to VIII.25.
- **B4:** Strong. Many of the named audiences passed through it.
- **B5:** Large.
- **Tier:** Tier 2 signal, *pending a base*.
- **Living in 2010:** yes, as a judgment.
- **Proposal D-P12:** a current entry, "Student and campus movements, c. 1920–2010", held as skeleton D-E3 until a base is staged. The method asks for citation-grounded reasoning on Sourcing and Ecology, and no source yet grounds B2 (G-31). The start of c. 1920 meets VIII.25's end, and the fork is stated in the skeleton.

**M3. Church planting, the church-growth school, and Church Planting Movements (CPM).**
- **In-repo anchors (IX.30, IX.36, IX.45):**
  - McGavran, *Understanding Church Growth* (1970);
  - Willow Creek (1975), Saddleback (1980), *The Purpose Driven Church* (1995), the Willow Creek Association (1992);
  - Calvary Chapel (1965) and Vineyard (1982);
  - Acts 29 (1998), a church-planting network.
- **CPM as a named approach** (rapid multiplication of new churches): **no in-repo source at all.** (2010 revision.) Its rise as a named method now falls largely inside the window, so the date objection is gone. But the repo holds nothing that dates or describes it.
- **Overlap:** heavy with IX.30 (church growth, at home) and with M5 (missions abroad).
- **D-Q12.**
  - (a) No entry of its own. Church growth stays in IX.30. Church planting abroad and CPM become named lines in M5, with CPM marked as having no in-repo date. **Recommended:** the repo-held content is already in IX.30, and a separate entry would double-count it.
  - (b) A current entry, "Church-planting movements, 1955–2010".
  - (c) CPM as its own entry. The window no longer rules this out; the nil sourcing does, for now. The recommendation is unchanged, now resting on sourcing alone.

**M4. Mass evangelism (the crusade tradition).**
- **In-repo anchors:**
  - IX.24: Lausanne 1974 "called by Billy Graham's organization";
  - IX.33: Graham's break with separatism in 1957;
  - Stanley, *The Global Diffusion of Evangelicalism: The Age of Billy Graham and John Stott* (IVP, 2013), cited on IX.24;
  - VIII.2's statusDescription: "Finney and Moody's later revivalism sits inside existing entries".
- **Not in-repo:** crusade dates, Billy Sunday, and the other carriers.
- **Overlap:** IX.24 is the network that grew out of it, while the crusade itself is a different formation practice (rallies, decision cards, counselors, follow-up). Note that VIII.2's ruling put revivalism inside existing entries.
- **D-Q13.**
  - (a) Named lines in IX.24 and IX.33, following VIII.2's ruling for era 9. **Recommended** for consistency, unless a base shows a distinct formation story.
  - (b) A current entry, "Mass evangelism, c. 1906–2010", as a Tier 2 signal pending a base.

**M5. World mission after 1906, including frontier missions and unreached peoples (the 10/40 Window).**
- **In-repo anchors:**
  - VIII.25's legacy: the Edinburgh generation's "zeal for preaching also went the other way… into the independent mission groups that grew all through the twentieth century", a current that nothing in era 10 picks up;
  - IX.46: IMC 1921 (verified), and its merger into the WCC in 1961 (verified);
  - IX.24: Lausanne 1974, and Padilla and Escobar on integral mission;
  - VIII.7: faith missions to 1906 (the China Inland Mission);
  - Stanley 2009 (Edinburgh) and 2013;
  - Walls, *The Missionary Movement in Christian History* (Orbis, 1996) [S];
  - Sanneh 2008 [S].
- **Not in-repo:** YWAM, OM and post-war frontier missions; **the unreached-people-groups idea, the "people group" framing and the 10/40 Window.** A search of the whole repo found no mention.
- **Section A:** via the carriers; not staged.
- **B1:** Moderate up to 1974 in-repo, Thin after it.
- **B2:** Not yet assessable: no source is cited. The judgment held for when a base exists: rich (missionary households, training, letters home, sending churches).
- **B3:** High. It is the receiver VIII.25's legacy names.
- **B4:** Strong.
- **B5:** Large.
- **Tier:** Tier 2 signal, *pending a base*. No Tier 1 signal is given while B1 is thin for the last 36 years and B2 is not yet assessable.
- **Living in 2010:** yes, as a judgment.
- **Proposal D-P13:** a current entry, "The independent mission movement, 1910–2010", as the receiver of VIII.25's second current. It is held as skeleton D-E2 until a base is staged (G-32).
- **Start fork:** 1910 (Edinburgh; the repo anchors it) or 1945 (Mark's "post-war"; no repo anchor between 1945 and 1974). The skeleton carries 1910, with the post-war expansion as its main body once sourced.

**Unreached people groups and the 10/40 Window (Mark's examples).**
- The fit is a named line inside M5, or a related entry of its own.
- **Nothing about either is in the repo:** no origin, date or person. (2010 revision.) Both now fall well inside the window, so the window is no longer an obstacle. The obstacle is nil sourcing.
- **D-Q14.**
  - (a) One named line inside M5: "missions organized around people groups rather than countries, and the 10/40 Window framing", left undated until sourced. **Recommended:** the scope rule says a framing or strategy lives inside the community that carried it (the "schools of thought" rule), and with no in-repo anchor a separate entry would be drafted on nothing.
  - (b) Two related entries: M5 and "The unreached-peoples movement". This can be reconsidered once a base exists.
  - (c) M5 renamed to carry it ("World mission and the unreached-peoples movement").

**M6. Children's ministries and Sunday-school ministries after 1900.**
- **In-repo anchors:**
  - VIII.24 (1780–c. 1900, living:false). Its statusDescription says it "makes no living-continuation claim that would call for a later cap".
  - IX.10: Habib Girgis's Coptic Sunday-school movement, with the General Sunday School Committee of 1918 (verified at the survey run, [S] at the sources run; V1.0 disclosed this divergence).
- **Not in-repo:** Western children's ministries after 1900.
- **Note:** VIII.24 is marked living:false and ends c. 1900. A 20th-century entry would contradict that deliberate end unless it is told as a new current, not a continuation.
- **D-Q15.**
  - (a) No entry now. Name it as a gap, and note the IX.10 line as the era's one Sunday-school movement. **Recommended:** no repo base, and VIII.24's end was a considered judgment.
  - (b) A current entry, "Children's and Sunday-school ministries, 1906–2010", once sourced.

**M7. Relief and development.**
- **In-repo anchors:**
  - IX.24's integral mission (1974);
  - IX.46's story (the Special Fund grant, the Programme to Combat Racism context);
  - IX.7, the Catholic Worker.
- **Not in-repo:** World Vision, Compassion, Christian Aid, Tearfund, Caritas. A census search found no mention of them.
- **B2:** Thin-to-moderate, as a judgment. Agencies form staff and donors more than communities.
- **Tier:** Tier 3 signal.
- **D-Q16.**
  - (a) Named, not drafted. Put it on the wanted list. **Recommended.**
  - (b) A current entry once sourced.

**M8. Christian broadcasting and media.**
- **In-repo anchors:**
  - IX.41's story: the Herald of Truth radio and TV program (1952);
  - IX.16: Wierwille's Vesper Chimes radio ministry (1942);
  - VIII.24's legacy: Bible-institute graduates staffed "radio ministries and publishing houses";
  - IX.17's 1993 radio broadcast;
  - IX.50's media carriers (Limbaugh 1988, Fox 1996). These are secular outlets and do not belong here.
- **Not in-repo:** Christian radio's start, the major broadcasters, and televangelism.
- **B2:** Moderate, as a judgment: listening as a devotional practice.
- **B4:** Strong.
- **Tier:** Tier 3 signal.
- **D-Q17.**
  - (a) A current entry, "Christian broadcasting, c. 1920–2010", once sourced, with Grace to You as a named carrier (D-Q4, iv). **Recommended in principle; draft only once a base exists.**
  - (b) Named lines only.

**M9. The ecumenical movement.** It is **already IX.46** (1921–), the movement as a whole and not only the WCC. Edinburgh 1910 is in VIII.25. **D-P14:** no new entry. If D-Q8 adopts a current kind, IX.46 is the clearest era-10 case for it. Check the overlap with VIII.25's first current: it is clean, since IX.46 starts in 1921, where VIII.25 hands off.

**M10. Communities (Taizé, Iona, L'Abri, new monastic).**
- Taizé and Iona are IX.14; L'Arche and Focolare are in IX.7.
- L'Abri is not in-repo.
- These are formation communities, which the census already treats as church-form rows, not as currents.
- **D-P15:** no new entry. L'Abri goes on the wanted list as a possible named line.

**M11. Others of the same kind, surveyed for 1906–2010 (named only; no repo anchor unless stated).**
- **The liturgical movement** (a cross-church current up to Vatican II). The census mentions it once. It is a strong candidate for a current entry (a Tier 2 signal), since IX.23 receives its outcome.
- **The Oxford Group / Moral Re-Armament.** Not in-repo.
- **The Keswick / "deeper life" convention movement after 1906.** VIII.4 holds it to 1906.
- **The Bible-conference and Bible-institute network after 1906.** It is partly in IX.29 and IX.33.
- **Christian schooling and home schooling.** Not in-repo.
- **Contemporary worship music.** It is partly in IX.30 (Hillsong 1983) and IX.45.

**D-Q18:** (a) record all as named gaps, with the liturgical movement flagged as the strongest (**recommended**); (b) draft the liturgical movement now. That would need a base.


**M12. Rescue missions (city gospel missions: shelter, meals and preaching for homeless and addicted people). Mark's example.**
- **In-repo anchors: none.** A census and era-file search found no rescue mission, named mission or founder.
- **Nearest rows:**
  - **VIII.6, the Salvation Army** (1865–1906). Its copy says it published "its scheme for shelters" in 1890, and its legacy names its "shelters… rehabilitation programs". That is the same work, done by a church body.
  - **IX.34, the Social Gospel** (c. 1886–1918): urban and industrial reform. It is a theology of social reform, not the evangelistic shelter mission.
- **The era question is real.** On general knowledge the American rescue-mission current began before 1906. That would make its start era-9 business. But the repo dates nothing about it, so no year is stated.
- **D-Q19 (era placement).**
  - (a) An era-10 current entry for 1906–2010 only, with a disclosed reach-back. This follows the IX.29/IX.34 precedent of entries whose start falls before 1906.
  - (b) An era-9 entry with an era-10 continuation. **That changes a Frozen era**, so it is Mark's alone.
  - (c) No entry: a named line beside VIII.6 and IX.34.
- **D-Q20 (form):** an entry of its own, or a named line beside the Salvation Army. **Recommended: wanted-list only for now (D-Q19 (c) in the meantime).** The repo sourcing is nil. Choosing between (a) and (b) needs a dated founding record first, and only then can the era question be answered honestly.

**M13. Christian education: the Christian day-school movement and Christian homeschooling. Mark's examples, beside M6.**
- **In-repo anchors: none.** The census mentions Christian schools only in the ancient sense (Alexandria) and Sunday schools in eras 8–9. The era-10 files mention only the Coptic Sunday School (IX.10). Nothing in the repo dates a 20th-century day-school movement, and nothing mentions homeschooling.
- **Distinctness from older church schooling** (parish and parochial schools across eras 5–9) cannot be shown without a source. This is exactly the test Mark set ("where the record supports a distinct 20th-century movement").
- **Homeschooling** (2010 revision) now falls mostly inside the window. Only claims a source dates before 2010 could be used, and the repo holds none.
- **D-Q21 (form):**
  - (a) One family current entry, "Christian education movements, 1906–2010", with named lines for day schools, homeschooling and children's/Sunday-school ministries. M6 would fold in.
  - (b) Two entries: day schools and homeschooling.
  - (c) Named gaps only.
- **Recommended: wanted-list only now, and (a) if a base is found.** One family entry keeps three thin strands from becoming three thin rows, and M6's VIII.24 problem (its deliberate end around 1900) is easier to handle inside a family entry that starts fresh in the 20th century.

**Wanted (W24):**
- rescue missions: a standard history and the founding records of the earliest city missions (dates to be confirmed by the source-research thread);
- Christian day schools: a standard history of the 20th-century movement, Protestant and Catholic;
- homeschooling: a standard history dated before 2010.
- None of these is PD by date, except any pre-1930 mission reports the thread finds.

**D-Q10 (method).** Section A for a current: should it run "at the world level against its established strands" (Article 21), through the carriers' dated statements, as V1.0's carrier device does? Or should a current carry no Section A finding, like the IX.18 label? **Recommended: the carrier device.** It is already used for IX.24 and IX.46, and it keeps every current tied to the floor through dated texts.

**Wanted for §4 (W23):**
- founding records, own statements and one standard history for each of: Wycliffe/SIL and the United Bible Societies (M1); the SCM/WSCF, IVF/IFES, the Navigators and Campus Crusade (M2); the church-planting and CPM literature dated before 2010 (M3); crusade evangelism (M4); 20th-century faith and frontier missions, YWAM, OM, the unreached-people-groups and 10/40 Window literature dated before 2010 (M5); 20th-century Sunday-school and children's ministries (M6); World Vision, Compassion and Christian Aid (M7); the beginnings of Christian radio (M8); L'Abri (M10); the liturgical movement and the Oxford Group (M11);
- Tatlow's history of the British SCM (1933; title to be confirmed). It is not PD by date.

## 5. The era record, the method-page line and the date display

**D-P9. Proposed fields for `eras[9]`.**

| Field | Now | Proposed | Note |
|---|---|---|---|
| `dates` | "1906-present" | **"1906-2010"** | Same hyphen style as eras 1–9 ("1815-1906"). |
| `title` | The Global Church Era | keep | Already historical. |
| `academicName` | World Christianity | keep | |
| `keyEvents` | Azusa (1906), WWI (1914–18), Vatican II (1962–65) | (2010 revision, to show the bookends) **D-Q9a:** (a) three slots, the same as every other era: **"Azusa Street Revival (1906) and Edinburgh Missionary Conference (1910)"**, **"Second Vatican Council (1962–65)"**, **"Edinburgh and Cape Town centenary meetings (2010)"**. **Recommended:** it keeps the three-slot pattern and shows both bookends. (b) Four slots: Azusa (1906), Edinburgh (1910), Vatican II, the 2010 centenaries. This needs a check that the era card renders four. (c) Keep the current three. That leaves the bookends out. | WWI drops in (a). Sources: Edinburgh 1910 is in-repo (VIII.25, IX.46); the Cape Town Commitment (2010) is in-repo (IX.24's sources); **Edinburgh 2010 is not cited anywhere in the repo**, so it is wanted (W25) before the line is published. |
| `tag` | "The center of gravity moves south and east" | (2010 revision) **D-Q9b:** (a) **"A century of global Christianity"**, Mark's own words. **Recommended:** it names the bookended span. (b) Keep "The center of gravity moves south and east". (c) "A century of global Christianity, as its center moves south". | The `dates` field already carries the span. |
| `stepStatus` | "Step 0 run complete — era frozen" | while the re-run is open: **"Step 0 re-run as history to 2010 — awaiting the gate"**; after Mark's gate: **"Step 0 run complete — era frozen"** (same as eras 3–9) | |
| `rec` | "The Step 0 assessment for this era has not yet run…" | (flag only) | This string is stale on eras 3–10 alike. It is a doc-hygiene item outside this thread. Flag it; do not touch it. |
| era 10 band line | — | **"The tree's history runs to 2010. Movements since then will be added as they become history."** (Mark's ruling) | Which `eras[9]` field or display slot carries it is settled at the census pass; it lands with the census changes (§8). |

**D-P10. The method page and the era band (Mark's "What follows 2010" ruling).**
- **Ruled, not a question.** The method page and the era 10 band carry Mark's line: **"The tree's history runs to 2010. Movements since then will be added as they become history."** It lands with the era 10 census changes after the gate, not in this run (§8).
- **Still open: the sentence that defines "living".** Ruling 1 asks the method page to say that "living" means as of 2010. Mark's line already says where the history ends, so only the definition is left. Three versions, all at about grade 8, active voice:
  - (A) **"On this tree, a living tradition is one that still existed as a practicing body in 2010."** *(Recommended.* Sixteen words, and it does not repeat Mark's line.)*
  - (B) "'Living' means living in 2010, where the tree's history ends."
  - (C) "A leaf marks a tradition that was still practiced in 2010." This links to the leaf mark (Family Tree decision 15). But the leaf is not drawn yet, and P2-V's written definition is still open, so (C) should wait for both.
- **Note:** P2-V (the tree's written definition of "living") is still open. This sentence should become that definition's opening line, not a second definition beside it. Two options were declined in the ruling and are not offered: a "since 2010" note on living entries, and a rolling cut-off.

**D-P11. How `dates` should read for a body still active in 2010.**
- **The precedent is already set.** Every era 1–9 row that was living at its boundary shows the boundary year: VIII.5 Oxford Movement "1833-1906", living:true, and 36 others like it. Era 10 is the only era that wrote "present".
- **D-Q9.**
  - (a) **"1913-2010"**, the same form as eras 1–9. The leaf mark and the method sentence say it is living. **Recommended:** it makes era 10 match the other nine, and it is what ruling 3 ("one standard for all ten eras") implies.
  - (b) **"1913-2010 (living)"** or **"from 1913"**. This reads more clearly on its own. But it applied to era 10 alone it would make the 37 era-9 rows read as ended by contrast.
  - (c) **"1913–"** (open end). This puts back the "present" claim that ruling 4 retired.
- **Rider:** if Mark thinks "1913-2010" really does read as an ending, the same risk applies to the 37 era-9 rows. The fix should then be fleet-wide, for example a display rule that shows "to 1906 · living" or "to 2010 · living" for every boundary-capped living row. Era 10 should not get it alone.
- **Machine fields:** `end` should be 2010 in every case. The display string and the leaf carry the meaning.

---

## 6. Questions for Mark at this gate

Each question has options and a recommendation, so it can be answered by number. The local labels
(A-, B-, C- entry questions; D-Q, D-P sweep items) point back to the sections above. **IX.50 (G-15)
is Mark's direct ruling; the conditional lean given there is advisory.** G-39 to G-49 were added after
Round 1; the numbers before them did not move.

### Era-wide

- **G-1. The era record** (`eras[9]`; §5, D-P9/D-Q9a/D-Q9b). Dates "1906-2010"; tag "A century of
  global Christianity"; key events "Azusa Street (1906) and Edinburgh (1910)", "Second Vatican
  Council (1962–65)", "Edinburgh and Cape Town centenaries (2010)"; stepStatus "Step 0 re-run as
  history to 2010 — awaiting the gate", then the standard frozen text. Options: (a) as drafted;
  (b) keep the current key events and change only the dates and tag. **Rec. (a)**, with the 2010
  centenaries sourced before publishing (wanted list).
- **G-2. How a body active in 2010 shows its dates** (D-Q9). (a) "1913-2010", as eras 1–9 already
  show living rows ("1833-1906"), with the living mark saying it lived on; (b) "1913-2010 (active)";
  (c) "from 1913". **Rec. (a)**; if it reads as an ending, fix it for all eras together.
- **G-3. The status sentence.** (a) remove "This status is a dated reading of a living tradition,
  not a permanent verdict" from every era 10 status, as in eras 1–9 (applied in the edits);
  (b) replace it with "This status reads the historical record to 2010." **Rec. (a).**
- **G-4. What may be cited after 2010** (A Q1; B X2; IX.5 Q1; IX.30 Q1). (a) a tradition's own texts
  and events after 2010 come out. Later outside scholarship and later inquiries about in-era matters
  may stay, in sources and in prose, labeled as later. An inquiry stays only where the record dates the
  matter it examined inside the era. The edits follow this rule: they keep the 2020 and 2023 L'Arche
  reports on conduct of 1952–2005 (labeled later in five fields), Pew 2011 (IX.5), Slagle 2011
  (IX.48), Hummel 2023 (IX.29), Bowler 2013 (IX.30), *Let Them Not Return* 2017 (IX.19) and the later
  voices of Atto (IX.19) and Adogame (IX.25). They remove IX.30's 2018 resignation (a post-2010 event)
  and its 2019 advisory report, whose subject the record does not date inside the era. (b) nothing
  published after 2010 at all. **Rec. (a).** Pew's count must be checked for the year it describes.
- **G-5. Fifteen rows whose "living" flag turns on P2-V** (A Q7; B; C Q3). Fifteen rows
  (IX.1, 2, 3, 8, 9, 12, 18, 21, 22, 32, 33, 35, 45, 47 marked living; IX.17 marked not living)
  turn on whether "living" asks about the episode or the tradition it names. Two of them, IX.18 and
  IX.32, now end in 2010; their question is whether a label, or a current with no body, can be
  "living" at all. (a) keep the flags as
  drafted (the tradition was alive in 2010) and settle the rule at P2-V; (b) hold all fifteen until
  P2-V. **Rec. (a)**; the flags match the census as it stands.
- **G-6. The method page and the era 10 band** (D-P10; Mark's "What follows 2010" ruling). The
  line is ruled, not asked: "The tree's history runs to 2010. Movements since then will be added as
  they become history." It goes onto the method page and the era 10 band, and lands with the census
  changes after the gate (§8). What is open is the sentence that defines "living": "On this tree, a
  living tradition is one that still existed as a practicing body in 2010." (a) adopt it as the
  opening of P2-V's written definition, beside Mark's line; (b) adopt it now as a stand-alone line.
  **Rec. (a).**
- **G-7. The overlay-current ("wet ink") form** (D-Q6). (a) keep it to mean "overlays other
  bodies" and drop "still forming"; (b) retire it for era 10. **Rec. (a).**

### The roster

- **G-8. IX.31, Deconstruction.** Every anchor is dated 2015 or later. (a) drop it from era 10,
  reversing the 2026-08-14 hand-selection (a `retireEntry` operation in the JSON); (b) fold its roots
  into IX.28; (c) keep it. **Rec. (a).**
- **G-9. IX.28, the emerging church** (B Q). (a) keep, c. 1990–2010, Tier 3, living as of 2010;
  (b) the same at Tier 2; (c) drop as mainly post-2000. **Rec. (a)**, with a mild lean to (b).
  It is a movement or trend, not a church body (see G-28).
- **G-10. IX.32, the narrative–kingdom renewal.** (a) keep to 2010 at Tier 2, carried by Wright's
  popular books (*Surprised by Hope*, 2008, verified; *Simply Christian*, 2006, [S]), with the McKnight
  and BibleProject voices removed whole; (b) drop. **Rec. (a).** Since one of the two popular books is
  [S], the Tier 2 call leans on the verified 2008 book, Newbigin and Willard.
- **G-11. IX.36, New Calvinism** (C Q1). (a) keep, c. 1998–2010, Tier 2; remove the 2014 story
  "The Year Mars Hill Came Apart" whole and leave its slot empty; correct the floorNote to the 2007
  Confessional Statement; (b) keep the story as later history. **Rec. (a).**
- **G-12. IX.49, Hebrew Roots** (C Q2). (a) keep at Tier 3, ending 2010; (b) drop. **Rec. (a).**
- **G-13. Stories that fall after 2010** (A Q2). IX.7's L'Arche findings (2020–23), IX.11's Cho
  conviction (2014) and IX.16's LLDM case (2019–22). (a) remove all three whole; re-center the L'Arche
  story on 1952–2005 later, under G-4; (b) keep them as later history. **Rec. (a).** Seven stories
  are removed in all: these three, IX.36's under G-11, and three more under G-39.
- **G-14. Split Iglesia ni Cristo out of IX.16** (D-Q5; draft D-E1, 1914–2010, built only from
  IX.16's own copy). (a) split it, with an atlasId of Mark's choosing (IX.51 recommended, so IX.50
  stays with its own question); (b) keep it banked. **Rec. (a).**
- **G-15. IX.50, the Christian Right — Mark's direct ruling** (§3, D-Q7). (i) a Tier 3 row,
  1979–2010 (draft D-E6); (ii) disclosure lines on IX.33 and IX.24 only; (iii) nothing. The advisory
  lean is (i) if G-28 adopts a separate kind for movements, otherwise (ii). B2 is thin, and its
  Section A finding rests on three unverified sources. **Naming, a separate choice if (i):** (n1)
  "The Christian Right", as drafted; (n2) "The New Christian Right"; (n3) "The Christian Right,
  1979–2010". "Christian Nationalism" is not offered, since its naming wave is after the era. The
  draft's id must be settled with the name, before first publication.
- **G-16. Named gaps, no rows yet** (D-Q1, D-Q2, D-Q2a): twentieth-century Anglicanism (skeleton
  D-E5; the student and mission skeletons are G-31 and G-32), the post-Soviet revival, Balkan Orthodoxy, the Holiness and other Protestant
  denominational families, Japan after 1906. (a) name them as gaps and draft once a base is staged;
  (b) draft rows now. **Rec. (a)**; the repo holds nothing to build them on.
- **G-17. The era 9 register rows** (LDS, Jehovah's Witnesses, Christian Science, Christadelphians;
  D-Q3). (a) one-line disclosures on the frozen era 9 rows, a frozen-row touch; (b) era 10 rows.
  **Rec. (a).**
- **G-18. MacArthur and Grace to You** (D-Q4). (a) a named carrier in a Christian-broadcasting
  movement (G-36); (b) named lines in IX.33, as V1.0 ruled. **Rec. (a)** if G-36 adds broadcasting,
  otherwise (b).

### Entry fixes

- **G-19. IX.1's claim that almost every Pentecostal church traces to Azusa Street** (A Q4). IX.2's
  many-origins reading contests it. (a) soften the copy so it does not state the claim as settled;
  (b) keep it and tag it Contested. **Rec. (a).**
- **G-20. IX.7, L'Arche's founder test** (A Q5). It was untested in 2010, when the founder was
  still alive and leading. (a) narrow the statusWord; (b) leave it. **Rec. (a).**
- **G-21. IX.20's stale line** (D-P7; IX.20 Q1). V1.0 banked a replacement that narrates process and
  cannot go into a live field. (a) apply D-P7's text, as the JSON now carries it: "Continues the
  Ethiopian church of Tewodros and Menelik. The tree has no entry for Ethiopian Christianity between
  1650 and 1855." (b) keep it banked. **Rec. (a)**: this re-run opens the row.
- **G-22. IX.27** (B Q). The 2015 canonization, its old headline, comes out; a new teaser is
  drafted. (a) accept; (b) keep the old teaser. **Rec. (a).**
- **G-23. Fact checks.** IX.14 said Taizé (1940) began "two years earlier" than Iona (1938); the
  edits correct it to "two years later". IX.44's floorNote now says no text after 1980 is cited,
  pending a check of the 1985–2010 revisions of the Adventist Fundamental Beliefs. Undated details
  to check: IX.22's canonization counts, KICC's moves in IX.25, the outcome of Adelaja's 2009 case.
  (a) apply the IX.14 fix and send the rest to the wanted list; (b) hold all. **Rec. (a).**
- **G-24. Facts removed with the gap left open** (C Q4, A Q8): among them the Adventists' 22
  million (undated), the 2017 Malankara ruling, Hanegraaff's 2017 chrismation, Desmond Ford's death
  (2019), Kyrion II's undated canonization, the unsupported "largest Lutheran bodies" claim.
  (a) accept the removals; (b) review them one by one. **Rec. (a).**
- **G-25. 2000–2010 facts that stay because the record cites them** (C Q5, A Q8): for example the
  2001–02 Birmingham convictions, the 2003 reissue of Questions on Doctrine, Ancient Faith Radio
  (2004), Taizé's 2005 succession, Skobtsova's 2004 canonization, the UMJC's 2005 statement.
  (a) accept; (b) review one by one. **Rec. (a).**
- **G-26. Sources lists** (C Q7). Seven whole source items that document only a tradition's own
  post-2010 events are encoded now as `removeItem` operations: IX.10's 2015 martyrs, IX.27's 2015
  canonization, IX.30's collapse records, IX.32's McKnight and BibleProject, IX.36's 2021 podcast and
  IX.48's Hanegraaff chrismation. Items that mix in-era and post-2010 material (the 2017 Malankara
  ruling, IX.36's Acts 29 record, IX.20's 2018 and 2022 clauses and others in §2) are trimmed at the
  census pass, and later studies of in-era history are labeled as later there. (a) accept both;
  (b) leave the lists. **Rec. (a).**
- **G-27. Link notes.** A few link notes touching era 10 speak in the present tense (for example
  "It is the same church" on the Indonesian link, "the balance is still studied" on IX.1 → IX.4).
  (a) fix them in the era 10 link pass, P2-L10; (b) fix them at the census pass. **Rec. (a).**

### Movements outside formal church bodies (§4)

- **G-28. How a movement entry is told apart from a church entry** (D-Q8). Data: (a) a `kind`
  field of church | current | person, extending P2-G2's planned person kind ("movement" cannot be
  the value, because every census entry is already a "movement"); (b) a boolean `parachurch`;
  (c) no new field, with a lane of its own. Drawing: a translucent band across the lanes the
  movement touches. **Rec. (a)** with the band. Whether it reaches back to eras 1–9 (VIII.24,
  VIII.25) is Mark's call.
- **G-29. Section A for a movement with no confession of its own** (D-Q10). (a) assess it through
  the dated statements of the organizations that carry it, as V1.0 did for IX.24 and IX.46;
  (b) exempt such movements from Section A. **Rec. (a).**
- **G-30. Bible translation** (M1, D-Q11). The 2026-07-16 ruling made it a cross-era theme thread,
  not rows. (a) a change order: an era 10 entry as well as the thread, once a base is staged
  (skeleton D-E4); (b) keep it a thread only. **Rec. (a).**
- **G-31. Student and campus movements** (M2; skeleton D-E3, c. 1920–2010). The method asks for
  citation-grounded reasoning on Sourcing and Ecology. No cited source grounds B2, and the carriers'
  founding dates are not in the repo. (a) name it as a gap and draft once a base is staged, as G-16
  does; (b) enter it now. **Rec. (a).**
- **G-32. The independent mission movement** (M5; skeleton D-E2, 1910–2010), with unreached peoples
  and the 10/40 Window as a named line inside it (D-Q14). B1 is thin after 1974, and no cited source
  grounds B2. (a) name it as a gap and draft once a base is staged, with the 10/40 line inside it once
  sourced; (b) enter it now; (c) unreached peoples as its own entry. **Rec. (a)**; the repo holds no
  source on the 10/40 Window yet.
- **G-33. Church planting and church-planting movements (CPM)** (M3, D-Q12). (a) named lines in
  IX.30 and the mission movement; (b) its own entry. **Rec. (a)**; CPM has no source in the repo.
- **G-34. Mass evangelism** (M4, D-Q13). (a) named lines in IX.24 and IX.33; (b) its own entry.
  **Rec. (a).**
- **G-35. Sunday school, children's ministries, Christian schools and homeschooling** (M6, M13;
  D-Q15, D-Q21). (a) wanted list now; one "Christian education" family entry once a base exists;
  (b) two entries later. **Rec. (a).**
- **G-36. Relief and development, Christian broadcasting, and others** (M7, M8, M11; D-Q16–18).
  (a) wanted list now; broadcasting becomes an entry once sourced; the liturgical movement is the
  strongest further gap; (b) drop them. **Rec. (a).**
- **G-37. Rescue missions** (M12; D-Q19, D-Q20). No source in the repo. Its start probably lies in
  era 9, which is frozen. (a) wanted list now, then a named line beside the Salvation Army
  (VIII.6); (b) an era 10 entry. **Rec. (a).**
- **G-38. Which existing rows are movements rather than churches** (B's judgment): churches IX.19–23,
  IX.26, IX.27; movements or trends IX.24, IX.25, IX.28, IX.29, IX.30, IX.32, IX.33; IX.18 a label.
  (a) take this as the working list for G-28 and finish it across all 49 at the census pass;
  (b) leave the existing rows as they are. **Rec. (a).**

### Added after Round 1 (G-39 to G-49)

- **G-39. Three more stories that fall after 2010** (§2b X6). IX.28's "Farewell, Rob Bell" (2011),
  IX.30's "The Report the Board Published" (2020–21) and IX.32's "Free, and About the Whole Story"
  (2014–19). (a) remove all three whole, leaving one story on each row; (b) keep them as later
  history. **Rec. (a).** With G-11 and G-13, this makes seven removals.
- **G-40. IX.4, the Kimbanguist 2021 WCC exclusion** (IX.4 Q1). (a) drop it and keep the 2005/2008
  arc, with the 1969 admission as background (drafted); (b) keep it as a declared post-era note,
  which breaks ruling 2. **Rec. (a).**
- **G-41. IX.18, the label row** (IX.18 Q1). (a) keep it, c. 1990–2010, with its discipline
  unchanged; (b) fold it into IX.35 as a closing line; (c) drop it. **Rec. (a)**: its documented
  expression, the emerging church, falls inside the era.
- **G-42. IX.19, the "erasure" line** (IX.19 Q1). The teaser, relationsSummary and legacy say that
  "living" Syriac communities read (or "experience") the 1300–1915 silence as erasure, a claim about
  today. (a) drop "living" and put the verb in the past, "experienced as erasure" (drafted,
  conditional); (b) recast it to map-voice only; (c) remove it. **Rec. (a).**
- **G-43. IX.33's stale status copy** (IX.33 Q1). It still reads "Proposed for a future survey; not
  yet reviewed." (a) replace it (drafted, conditional): "Tiered Strong (Tier 1). It is assessed on
  its own dated texts, from The Fundamentals (1910–15) to the naming of 1920." (b) leave it to the A3
  statusWord backlog. **Rec. (a).**
- **G-44. IX.38's scale claim** (IX.38 Q1). "Mizoram and Nagaland among the most heavily Christian
  regions on earth", already in the past tense. (a) grade it Widely Accepted as written; (b) hold it
  out until a census counter is cited. **Rec. (a).**
- **G-45. IX.48's name** (IX.48 Q1). (a) keep "Autocephaly & the Convert Wave"; (b) "& the Convert
  Stream". **Rec. (a)**: the 1987 reception was a wave.
- **G-46. Notes on the archive's own condition** (§2b X3; IX.28). (a) keep them as present-day
  sourcing notes; (b) recast them in the past (drafted, conditional). **Rec. (b)**: they are claims
  about today, which the "What follows 2010" ruling rules out.
- **G-47. IX.29's "reaction against the chart" line** (IX.29 Q1). It depends on IX.32 staying (G-10).
  (a) keep it; (b) cut it if G-10 drops IX.32. **Rec. (a)**, with (b) as the fallback.
- **G-48. IX.44 and the VIII.10 completion** (IX.44 Q1). The finding rests on dated texts of 1931 and
  1980, so the history ruling does not move it. (a) confirm no reopening; (b) reopen it. **Rec. (a).**
- **G-49. Which row leads with Niagara** (§1G, D-P8). Both IX.29 and IX.33 open their `why` on the
  Niagara conferences. No edit is drafted. (a) at the census pass, open IX.33 on *The Fundamentals*
  (1910) and its 1920 naming, using only IX.33's own copy, and move Niagara to its relationsSummary;
  (b) leave both. **Rec. (a).**

## 7. Wanted list (for the source-research thread)

#### 7A. Registry check: what is already vendored that bears on era 10

- The headers of all 1,531 files in `cic/texts/` were checked for era-10 movements and authors: Azusa, *The Apostolic Faith*, Rauschenbusch, Gladden, Sheldon, *The Fundamentals*, Scofield, Machen, Fosdick, Seymour, Pascendi, Edinburgh 1910, Kimbangu, Aglipay, Ellen White, Torrey and Warfield, the SVM, Mott, Bible societies, Moody, Pius X. **No vendored file is an era-10 primary text.**
- The 1906–1930 dates in the registry belong to translations of ancient and early-modern works (for example `palladius_lausiac-history_clarke1918.txt`, `luther_works-v1-selected_jacobs-spaeth1915.txt`).
- Near misses, background only, none to cite for era 10:
  - `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt` (papal sources to 1911; it may hold Pius X documents up to 1911 and needs checking before any citation for IX.47);
  - `kralice-bible_biblj-svata-kralicka-ces_bfbs1887.txt` (an 1887 British and Foreign Bible Society printing; Bible-society background for §4's M1, but pre-era).
- **Result: era 10 has no vendored primary text. Every era-10 B1 grade rests on cited secondary works and on staged research.**

#### 7B. Public-domain early texts (published before 1930). PD — for the source-research thread

| # | Text | Bears on |
|---|---|---|
| W1 | *The Apostolic Faith* (Los Angeles, 1906–08) | IX.1 (PD) |
| W2 | Seymour, *The Doctrines and Discipline of the Azusa Street Apostolic Faith Mission* (1915) | IX.1 (PD) |
| W3 | Frank Bartleman's Azusa account (1925; title to be confirmed) | IX.1 (PD) |
| W4 | *The Fundamentals* (12 vols., 1910–15) | IX.33 (PD) |
| W5 | Curtis Lee Laws, *Watchman-Examiner* editorial (1920) | IX.33 (PD) |
| W6 | Machen, *Christianity and Liberalism* (1923); Fosdick, "Shall the Fundamentalists Win?" (1922); the Auburn Affirmation (1924) | IX.33/IX.35 (PD in the US by pre-1929 publication; confirm against the registry's rule) |
| W7 | Rauschenbusch, *Christianity and the Social Crisis* (1907) and *A Theology for the Social Gospel* (1917); the FCC Social Creed (1908); Sheldon, *In His Steps* (1896); Gladden, *Applied Christianity* (1886) | IX.34 (PD) |
| W8 | Pius X, *Lamentabili* and *Pascendi* (1907), with contemporary English translations; the anti-modernist oath (1910). Check `mirbt…1911.txt` first. | IX.47 (PD) |
| W9 | Scofield Reference Bible (1909; rev. 1917); Larkin, *Dispensational Truth* (1918) | IX.29 (PD) |
| W10 | Assemblies of God, Statement of Fundamental Truths (1916) | IX.15 (PD) |
| W11 | World Missionary Conference, Edinburgh 1910, Report of Commission I and others | VIII.25/IX.46/§4 M5 (PD) |
| W12 | Ellen G. White's writings to 1915 | IX.44 (PD) |
| W13 | Pandita Ramabai's Mukti account (1907; title to be confirmed); Welsh-revival journalism (1904–05); Korea mission periodicals of 1907 | IX.2 (PD) |
| W14 | Patriarch Tikhon's 1918 epistles | IX.22 (PD) |
| W15 | Barth, *Der Römerbrief* (1919/1922) | IX.35 (US-PD by date only. Barth died in 1968, so it is not PD in the EU. Check the registry rule.) |

#### 7C. Later texts (not PD by date) and secondary works that would settle open questions

- **W16. Anglican 20th century (D-Q1):** Lambeth Conference reports, 1908–1998; a standard history of the Anglican Communion; the Church of South India's 1947 constitution.
- **W17. Balkan/Eastern European Orthodoxy, Holiness denominations, Japanese Christianity after 1906 (D-Q2):** one standard history each.
- **W18. The register rows' 20th century (D-Q3):** dated own-voice texts. If (b) is chosen: the JW name adoption, the LDS 1978 statement and the like.
- **W19. INC (D-Q5):** dated *Pasugo* doctrinal articles; an independent scholarly study; the 1963 succession record (currently [S]).
- **W20. IX.50 (D-Q7):**
  - Moral Majority's 1979 founding record (to lift the [S]);
  - Falwell's "coalition of moralists" source;
  - Whitehead & Perry's definition, verified;
  - (no longer needed for living: the Faith and Freedom Coalition's 2009 founding is verified).
- **W21. IX.20:** a source for the era-8 Ethiopian silence (1650–1855), if a row is ever wanted.
- **W22. MacArthur (D-Q4):** a dated record of Grace to You's founding; the MacArthur Study Bible (1997 [S]) verified.
- **W23.** The §4 movement list (under §4, "Wanted for §4").
- **W25 (2010 revision).** Records of the 2010 centenary meetings: the Edinburgh 2010 conference (not cited in the repo); the Cape Town Commitment (2010), already in IX.24's sources, to be checked as a text; the GAFCON 2008 Jerusalem Statement, if D-Q1 drafts (V1.0 holds GAFCON 2008 as [S]).

## 8. Follow-ups after the gate

These land after Mark rules, not in this run.

- **The method page and the era 10 band.** Mark's line, "The tree's history runs to 2010. Movements
  since then will be added as they become history.", goes onto both, with the "living" sentence G-6
  settles. It lands with the era 10 census changes.
- **P2-L10, the era 10 link pass.** Fix the link notes that speak in the present tense (G-27): "the
  balance is still studied" on IX.1 → IX.4, "It is the same church" on the Indonesian link, and any
  others the pass finds.
- **P2-V, the written definition of "living".** It settles G-5's fifteen flags and opens with the
  sentence G-6 adopts.
- **The source-research wanted list (§7).** It goes to the source-research thread, including the
  checks this record leaves open: the year Pew's count describes (IX.5), IX.22's canonization counts,
  KICC's moves and Adelaja's case (IX.25), the 1985–2010 Adventist revisions (IX.44), the Dallas
  briefing date (IX.50), and a base for the four skeletons (D-E2 to D-E5).

---

Per-entry wanted texts are listed under each entry in §2 and in the companion JSON.
