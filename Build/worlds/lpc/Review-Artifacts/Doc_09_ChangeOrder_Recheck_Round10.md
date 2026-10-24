Simulated review — informational only, not an Article 31 substitute.

# Doc_09 targeted recheck of the CO-LPC-1 revision pass and the `lpcstory006` retelling

- **Document:** `Build/worlds/lpc/Doc_09_Story_Inventory.md`, with `Story-Chunks/*`, `records/lpc/story/*`, `lpc_Story_Index.md` and `records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `9a6d4d27`; diff checked: `git diff d6b449e6 9a6d4d27`)
- **Round:** 10
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent targeted-recheck subagent, fresh context (drafted none of the fixes or renderings)
- **Drafter:** Sonnet 5.5 (revision pass) and Opus 5.5 (renderings pass)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass and renderings-pass drafters
- **Date:** 2026-10-23
- **Scope:** targeted recheck of the revision pass. Only the Round 9 findings (`Review-Artifacts/Doc_09_ChangeOrder_Review_Round9.md`: P1-1 to P1-4, P2-1 to P2-7) are checked, plus any new error the fixes introduced. The `lpcstory006` Tier 1 retelling, ruled by the project lead (`lpc_Decision_Log.md`, 2026-10-23), is checked against `Review-Artifacts/Doc09_Acta_Proconsularia_Read_lpcstory006_2026-10-23.md`. As the separate Opus check CLAUDE.md requires, every English rendering of the *Acta*'s Latin in the chunk and the story record is checked against the Latin in `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` (H), `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` (G) and `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` (K).
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 ("Cap ruling: lpc CO-LPC-1 revision pass", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc` gives 175 lines and 37,435 bytes for Doc_09; the last line ends "…and no story draws on the 411 *Gesta*.", and all eleven `## ` headings are present. The chunk is 82 lines, ending in the Absent Story Note's §11 paragraph and the closing rule; the story record is 124 lines, ending in its provenance line; the contested record is 75 lines.
- **Truncation check, method 2:** hash comparison against the committed blobs. Doc_09: `git hash-object` and `git rev-parse 9a6d4d27:<path>` both give `c345ccab665ac1bdd3dd89bfeb66edbf97584546`. The `lpcstory006` chunk, the story record and the contested record each match their `9a6d4d27` blob.
- **Method limits:** no web search and no model call. Nothing edited except this file. Generators run only on scratch copies. Pontius's English quotations checked by script against `anf05` with tags and endnotes stripped. Readability scored with `engine/m7/turn_readability.score_turn`.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P1-1 sermons on Perpetua and the Scillitans "not available" | **Fixed** | Doc_09:105 and :137 now say the sermons are vendored in Latin and unread for this document. Verified: `augustine_sermones-1-340-lat_migne-pl38.txt:89935` (SERMO CCLXXX, "In Natali martyrum Perpetuae et Felicitatis, i"), :90170 (CCLXXXI, "… ii") and :90261 (CCLXXXII, "… iii"); `augustine_sermones-guelferbytani-lat_morin1917.txt:1361` and :8466 ("De natale sanctorum Scillitanorum"). "The only story-candidate … blocked that way" is gone. §6 item 4 now notes the sermon scope (:108). One citation slip, new P2-C. |
| P1-2 *Acta* "unread", "inside Hartel only", "court's own record" | **Partly fixed** | Fixed in Doc_09 (:95, :106, :133), the chunk (Source :6, Do-Not-Retrieve :8, Usage Guidance :70-72, Absent Story Note :78-80) and the story record (sources :28, prefer_instead :39-41, justification). Not fixed in `records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md:22`, which still calls the *Acta* "the strictly documentary witness to the trial, vendored in Latin only and not read in this build". New P1-A. |
| P1-3 `lpcstory006` errors against the *Acta* | **Fixed** | (1) Bound eyes: chunk :27 and record :96-98 give both texts and say they differ on the cloths. (2) "Could not do it": gone; the sentence is given in ANF's words as Pontius's, with the disputed subject disclosed (:29, :56). (3) "Open": gone; "level" is quoted from ANF and attributed to Pontius, with *conuallis* disclosed (:58). (4) Crowd: narrowed to "what any one person in the crowd made of it", with the crowd's cry given (:78). (5) Centurion: inside the Pontius quotation only; the *Acta*'s *spiculator* stated (:29, :52). (6) Formation Ecology: :37 now rests on the crowd "which both texts attest"; the trees are under "What only Pontius says". |
| P1-4 process narration in canonical files | **Fixed in the files named** | Doc_09 Disposition (:173-175) now holds the disposition and escalation assessment only; :33's correction-history paragraph is gone; "and this note previously denied" is gone from the chunk; no story record body contains "this session" (grep over `records/lpc/story/`). The contested record's body still does (:75, "read in full this session"), counted under P2-B. |
| P2-1 closing line contradicts the document | **Fixed** | "seven review rounds" and "awaiting a disposition" are gone (:175). |
| P2-2 §7 item 1 pulls two ways | **Fixed** | :119 states Doc_01's narrower test in Doc_02 §7's words, drops "a build choice" and no longer quotes Registry row 27's stale note. |
| P2-3 §2 "without CF's markers" | **Fixed** | :41 now names `lpcstory001` (corroborated) and `lpcstory002` (portrait attaches to the man). |
| P2-4 "eight years later" | **Fixed** | `Story-Chunks/lpcstory002_the-plague-and-the-enemies.md:37` and `records/lpc/story/lpc.story.the-plague-and-the-enemies.md:83` read "a few years later". |
| P2-5 stale ranking | **Fixed** | :133 has no ranking. |
| P2-6 missing full stop | **Fixed** | :127 "…not the full range. It is…". |
| P2-7 index out of step; generator blind to change-order reviews | **Partly fixed** | Regenerated on a scratch copy (`gen_story_index.py <copy>`, "7 stories; tiers 1:7"): `diff` against `lpc_Story_Index.md` is empty. But `gen_story_index.py:340` still globs only `Doc09_Round*_Review.md`, so the Index still says "Eight independent review round(s)" and "the Round 8 fix pass is itself unreviewed" (`lpc_Story_Index.md:3`, :118). |

---

## The `lpcstory006` retelling against the ruling

The ruling (option 1): retell at Tier 1 on what both texts attest, mark Pontius-only details as his, state the contradiction.

- **What both attest is told plainly and only that is credited to both.** The night watch (Pontius §15; *Acta* 2, K 4877-4881), the crowd (Pontius §16; K 4915-4917), the sentence, with the dependence disclosed ("On the sentence the two texts are not independent witnesses", chunk :21), the people's part (Pontius §18 *publicata uoce*; K 4913-4915; Harnack 1913 line 1748 ties them), and his own hand at his eyes. This matches the reading note §4 rows 1, 9 and 10.
- **Pontius-only details are marked as his.** Chunk :29 ("What only Pontius says… they are his"), the record's last paragraph ("We tell that part as Pontius's reading"), Tier Justification :53, and the claim guards in the record (:42-46). The trees, Zacchaeus, the hurried executioner, the trembling fingers, the strengthened hand and the rank of centurion all sit there, matching reading note rows 2-4 and 6-8.
- **The contradiction is stated.** Chunk :27 and :54; record :96-98 and the claim guard; Usage Guidance :72 tells the Representative to name both.
- ***Acta*-only details** (*Deo gratias*, the kneeling, the gold, the burial) are labelled "Here only the *Acta* speaks". They fall within the core the reading note's recommended option listed, and they are never credited to Pontius.
- **Every Pontius quotation in the chunk and record** matches `anf05` §§11 and 15-18 verbatim (thirteen strings, script-checked; §11 at `anf05:28001-28004`).
- **Latin quotations and line pointers in the Tier Justification** hold at K 4877-4881, 4907-4911, 4913-4919, 4921-4927 and 4950; H 41344 (*couuallis scripsi*; chunk :58), 41463 (*beatum Cyprianum*), 41626 (doxology); Harnack 1913 lines 1743, 1748 and 2574-2576.

## English renderings of the *Acta*: clause-by-clause check

Latin cited from K, which agrees with G and H at each passage (reading note §2, re-checked at K).

| Rendering (site) | Latin | Every clause | Nothing added | One thought, ≤25 words | Modern sense |
|---|---|---|---|---|---|
| "the whole people of the brethren came there." (chunk :17, record) | *illuc uniuersus populus fratrum conuenit* (K 4877-4879) | Yes, as a quoted fragment | Yes | Yes (8) | Sound |
| "had stayed in the street, before the door of the officer's lodging." (chunk :17, record) | *quoniam omnes in uico ante ianuam hospitii principis manserant* (K 4881), after *et cum hoc sanctus Cyprianus conperisset, custodiri puellas praecepit* (K 4879-4881) | The *quoniam* clause, quoted as a fragment; the clause between the two fragments (*custodiri puellas praecepit*) is not rendered. See P2-D | Yes | Yes | *uicus* "street" defensible |
| "a large crowd gathered at Sextus's place, as the proconsul Galerius Maximus had ordered." (chunk :19, record) | *multa turba conuenit ad Sexti secundum praeceptum Galeri Maximi proconsulis* (K 4882-4884) | Yes | Yes | Yes (15) | Sound |
| "You have been caught as the author and standard-bearer of the most wicked crimes. So you yourself will be an example to those you gathered to you in your crime. Discipline will be made firm by your blood." (chunk :21) | *et ideo cum sis nequissimorum criminum auctor et signifer deprehensus, eris ipse documento his, quos scelere tuo tecum adgregasti: sanguine tuo sancietur disciplina* (K 4907-4909) | Yes: *cum* clause, main clause, relative clause, final clause; *et ideo* carried by "So" | Yes | Yes (14, 16, 8) | "Discipline" is the Roman sense of public order; it matches ANF's Pontius at the same point and the chunk pairs them, so it does not mislead |
| *Deo gratias*, "Thanks be to God." (chunk :21, record) | *Cyprianus episcopus dixit: Deo gratias* (K 4910-4911) | Yes | Yes | Yes | Sound |
| "Then the crowd of the brethren called out." / *Et nos cum ipso decollemur*, "Let us too be beheaded with him." (chunk :23, record) | *Post hanc uero sententiam turba fratrum dicebat: Et nos cum ipso decollemur* (K 4913-4915) | Yes | "called out" for *dicebat* (were saying) is a slight lift in force, acceptable in narration | Yes | Sound |
| "Because of this an uproar rose among the brethren, and a large crowd followed him." (chunk :23, record) | *propter hoc tumultus fratrum exortus est et multa turba eum prosecuta est* (K 4915-4917) | Yes | Yes | Yes (15), two clauses as in the source | Sound |
| The field paragraph (chunk :25) | *in agrum Sexti productus est et ibi se lacerna byrro exspoliauit et genu in terra flexit et in orationem se domino prostrauit. et cum se dalmatica exspoliasset et diaconibus tradidisset, in linea stetit et coepit spiculatorem sustinere. cum uenisset autem spiculator, iussit suis, ut eidem speculatori uiginti quinque aureos darent. linteamina uero et manualia a fratribus ante eum mittebantur* (K 4917-4923) | Yes, all nine clauses, one sentence each | Yes | Yes | "tunic" for *dalmatica* avoids the misleading modern vestment sense; "cloak" for *lacerna byrro* sound |
| The field, compressed (record :101-103) | as above | No: cloak, waiting and cloths left out. Summary, not presented as a rendering. P2-D | Yes | Yes | Sound |
| "Then the blessed Cyprian covered his eyes with his own hand. When he could not tie the strips of cloth on himself, the presbyter Julianus and the subdeacon Julianus tied them for him." (chunk :27, record :96-98) | *postea uero beatus Cyprianus manu sua oculos sibi texit. qui cum lacinias manuales ligare sibi non potuisset, Iulianus presbyter et Iulianus subdiaconus ei ligauerunt* (K 4923-4927) | Yes | Yes | Yes (11, 22) | "strips of cloth" for *lacinias manuales* sound |
| The burial (chunk :31) | *ita beatus Cyprianus passus est, eiusque corpus propter gentilium curiositatem in proximo positum est. inde per noctem sublatum cum cereis et scolacibus ad areas Macrobii Candidiani procuratoris, quae sunt in uia Mappaliensi iuxta piscinas, cum uoto et triumpho magno deductum est* (K 4927-4952) | All but the first clause, *ita beatus Cyprianus passus est* ("so the blessed Cyprian suffered"), which is not rendered anywhere in the story. P2-D | Yes | Yes | "with prayer" for *cum uoto* is a fair reading; "grounds" for *areas* sound |
| The burial, compressed (record :103-105) | as above | No: the pagans' curiosity, the first resting place and "beside the pools" left out. P2-D | Yes | Yes | Sound |

**Result.** Nothing is added anywhere, every rendered sentence is under 25 words, and no word carries a misleading modern sense. Four renderings leave a clause out (P2-D). None changes the meaning of what is rendered.

---

## New findings

**P1-A. The contested record still says the *Acta* is unread and "strictly documentary", and quotes build text that no longer exists.**
- *Where:* `records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md:22` (sources locus: "the strictly documentary witness to the trial, vendored in Latin only and not read in this build; named here rather than silently omitted, per lpcstory006's own Absent Story Note"); :56-58 (held_against quotes Doc_09: "the escalation at §8 item 7 -- which half of CF V7.4's Tier 3 definition governs … at lpcstory006 -- remains open"); :62 (concedes quotes "on the genus clause read alone, this story cannot be Tier 3 at all").
- *Evidence:* the reading note §3 (Christian framing at H 41463, H 41625-41626); the chunk Source field (:6) and Doc_09 §6 item 2 (:106), which now say the *Acta* has been read and is a Christian compilation; Doc_09 §8 item 7 (:139), which now says "`lpcstory006` no longer depends on the answer". A grep over `Build/worlds/lpc` and `records/lpc` outside `Review-Artifacts/` finds neither quoted sentence in the chunk or Doc_09; "cannot be Tier 3 at all" survives only in this record and `scripts/wb_lpc_s26.py:646`.
- *Why P1:* it is the exact defect Round 9 graded P1 at the other sites (a false source-status claim about the *Acta*), in a canonical record that sits beside the story it qualifies and is associated with it. The revision pass edited this record (held_against item 2) and left the false locus standing two fields above.
- *Fix:* restate the locus as the chunk does (an early, unnamed Christian compilation built around the hearing records, one edition in three printings, read at source). Remove or restate the two quotations of text the retelling removed, so the record states that `lpcstory006` no longer rests on the Tier 3 question. Carry the same text into `scripts/wb_lpc_s26.py` if that script is kept as the record's source.

**P2-A. The contested record's held_against item 2 says the *Acta* "confirms" *Deo gratias* and the kneeling.** :51-52. Pontius has neither; the chunk lists both under "The *Acta* alone" (:52). Fix: "gives", or split confirmed from *Acta*-only details as the chunk does.

**P2-B. Process narration in the contested record body.** :75 ("read in full this session", "exactly where Doc_09's own Disposition leaves it"). Same rule as Round 9 P1-4. Fix in the P1-A edit.

**P2-C. A stale line pointer in Doc_09.** :105 cites "Doc_01 line 26" for "all of Augustine's sermons are inside the world". In the current Doc_01 that statement is at line 30 ("**Sermon Scope:**"); line 26 is the beginning-point paragraph. Fix: cite Doc_01's Sermon Scope paragraph by name.

**P2-D. Four *Acta* renderings leave a clause out** (table above): the girls' guard order between the two night-watch fragments; *ita beatus Cyprianus passus est* in the chunk's burial, so the story never says, in the *Acta*'s words, that he died; and the record's compressed field and burial paragraphs. Fix: render *ita beatus Cyprianus passus est* ("So the blessed Cyprian suffered.") at the head of the burial in both files; let the record's two paragraphs follow the chunk clause for clause, or mark them as summaries.

**P2-E. The record says "Only the Acta tells what came before the blow."** :101. Pontius also narrates the moments before the blow (the eyes, the hurried executioner), as the same record says two paragraphs later. Fix: "Only the Acta tells these things before the blow."

**P2-F. Readability below the grade-8 floor.** `score_turn` gives the chunk's Story Text FK 5.9 / FRE 75.8 and the record's `text` FK 6.8 / FRE 72.7, both `below_floor=True`, no hard failures. CLAUDE.md treats grade 8 as a floor worth staying above. Most of the drop comes from the short, plain *Acta* sentences, which is the source's own register; noted for the next pass, not a revision trigger.

**Observation, not counted.** `scripts/wb_lpc_s24.py:823-860` still emits the death-of-Cyprian story record at Tier 3 with "Then the bishop bound his own eyes", and `wb_lpc_s26.py:631, :666` still carries the old contested text. Neither was changed in this pass. The sibling force-record generator `wb_lpc_s25.py` already regenerates every force record differently from the committed records, so these scripts are not the live source; a rerun would revert the retelling. Whether to retire them or bring them in step is for the build thread.

## Summary

Round 9's four P1s are fixed in Doc_09, the chunk and the story record. The `lpcstory006` retelling does what the ruling asked: the jointly attested core is told plainly, Pontius-only details are marked as his, and the disagreement over the cloths is stated. Every Pontius quotation is verbatim, and every *Acta* rendering adds nothing and keeps the meaning, though four leave a clause out. One substantial defect remains: the contested record beside the story still calls the *Acta* unread and "strictly documentary", and it quotes build text the retelling removed. Under the Cap ruling this goes to the project lead.

VERDICT: Substantial revision required
