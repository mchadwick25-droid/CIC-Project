Simulated review — informational only, not an Article 31 substitute.

# Doc_09 Story Inventory (lpc): second targeted recheck, with the Opus check of the *Acta* renderings

- **Document:** `records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md`, `Build/worlds/lpc/Story-Chunks/lpcstory006_the-death-of-cyprian.md` and `records/lpc/story/lpc.story.the-death-of-cyprian.md`, with `Build/worlds/lpc/scripts/wb_lpc_s26.py` and `Build/worlds/lpc/Doc_09_Story_Inventory.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `cd31eb55`; fixes read as `git diff 9a6d4d27 cd31eb55`)
- **Round:** 11
- **Reviewer:** Opus 5.5
- **Reviewer model:** claude-opus-5-5
- **Model note:** the harness reports that this run switched to Opus 5 (1M context) because Opus 5.5 could not be used. When the switch happened is not recorded, so some or all of this review may be Opus 5.
- **Reviewer agent:** independent second-recheck subagent, fresh context; drafted none of the fixes or renderings
- **Drafter:** Sonnet 5.5 and Opus 5.5 (revision passes)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass and renderings-pass drafters, after `Doc_09_ChangeOrder_Recheck_Round10.md`
- **Date:** 2026-10-23
- **Scope:** second targeted recheck. Only the findings Round 10 left open are checked — P1-A (the contested-claim record) and P2-D (the four *Acta* renderings that left a clause out) — together with the separate Opus check of renderings the project's working rules require: every English rendering of the *Acta*'s Latin in the chunk and the story record, against the Latin in `cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` (K), `cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` (G) and `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` (H) — every clause rendered, nothing added, one thought per sentence, under about 25 words, no misleading modern sense, and no summary presented as a rendering. Nothing else in Doc_09 is re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23, "Cap ruling: lpc, a second targeted recheck for Doc_04, Doc_05 and Doc_09" (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc -l -c` gives the contested record 76 lines / 6,224 bytes, the chunk 82 lines / 15,737 bytes, the story record 131 lines / 8,613 bytes, Doc_09 175 lines / 37,772 bytes. The contested record ends on "that question is reserved for the project lead."; the chunk ends on its Absent Story Note's pointer paragraph and the closing rule; the story record ends on its provenance line; Doc_09 ends on "no story draws on the 411 *Gesta*." All eleven `## ` headings of Doc_09 are present.
- **Truncation check, method 2:** hash comparison against the committed blobs. `sha256sum` of each working file equals `git show cd31eb55:<path> | sha256sum` (contested record `e8d602676eaf…`, chunk `abd7f5939447…`, story record `688037207b95…`, Doc_09 `b09aedcb932d…`). `git status --short` reports no modification under `records/lpc`.
- **Method limits:** no web search, no model call. Nothing edited but this file. The record generator was run only on a copy, writing into a scratch directory outside the repository. Readability scored with `engine/m7/turn_readability.py`.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P1-A. The contested record called the *Acta* "strictly documentary" and unread, and quoted build text the retelling had removed | **Fixed** | The sources locus (`records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md:22-25`) now reads "an early Christian compilation built around the records of Cyprian's hearings; its compiler is unnamed; one edition, Hartel's, which Gebhardt and Knopf also print; vendored in Latin and read at source; it carries its own Christian framing, so it is not a court transcript", matching the chunk's Source field (line 6) and Doc_09 §6 item 2. `held_against` item 2 is rewritten to the same effect and now says the *Acta* "adds Deo gratias, the kneeling and the gold pieces" — Round 10's P2-A ("confirms") is fixed with it. `held_against` item 3 and `concedes` no longer quote removed build text: they now say "Doc_09 §8 item 7 names a question this build cannot settle … lpcstory006 no longer depends on the answer" and "The tier's genus clause excludes an eyewitness, and Pontius is one", which match Doc_09 §8 item 7 (line 139). The body no longer reads "read in full this session" (Round 10's P2-B), so no process narration remains in it. **Generator in step:** `Build/worlds/lpc/scripts/wb_lpc_s26.py:625-695` carries the same new text; run on a copy into a scratch directory, the regenerated record's front matter differs from the committed one in `canon_cells` alone, and its body is identical, so a re-run no longer restores the false source status. |
| P2-D. Four *Acta* renderings left a clause out | **Fixed** | (1) The guard order is now rendered in both files — chunk line 17, story record lines 72 to 74: "The whole people of the brethren came there. When holy Cyprian learned of this, he ordered the young women to be guarded. He did so because all of them had stayed in the street, before the door of the officer's lodging", for *illuc uniuersus populus fratrum conuenit, et cum hoc sanctus Cyprianus conperisset, custodiri puellas praecepit, quoniam omnes in uico ante ianuam hospitii principis manserant* (K 4877 to 4881; H 41515). It is correctly moved into the chunk's "*Acta* alone" list (line 52), with Gebhardt's variant *castigari* disclosed (G 6608, verified). (2) *ita beatus Cyprianus passus est* is now rendered, at the head of the burial in both files (chunk line 31; record line 109) — see N2 on where it sits. (3) The record's field paragraph (lines 96 to 101) now renders all ten clauses of K 4917 to 4923, one thought per sentence, longest 17 words. (4) The record's burial paragraph (lines 109 to 112) now carries the pagans' curiosity, the first resting place and *iuxta piscinas*, all of K 4927 to 4952. |

---

## The Opus check of every *Acta* rendering

Latin read in K and cross-read in G (nos. XI) and H; the three agree at every passage used.

| Rendering (site) | Latin | Every clause | Nothing added | One thought, ≤25 words | Modern sense |
|---|---|---|---|---|---|
| The night, four sentences (chunk 17; record 72-74) | K 4877-4881 | Yes, all four clauses | "He did so because" carries *quoniam*; no new fact | Yes (8, 12, 17) | *uicus* "street", *puellas* "young women", *custodiri* "guarded" all sound; the *castigari* variant is disclosed in the chunk |
| "a large crowd gathered at Sextus's place, as the proconsul Galerius Maximus had ordered." (chunk 19; record 79-81) | *multa turba conuenit ad Sexti secundum praeceptum Galeri Maximi proconsulis* (K 4882-4884) | Yes | Yes | Yes (15) | Sound |
| The sentence, three sentences (chunk 21) | *et ideo cum sis nequissimorum criminum auctor et signifer deprehensus, eris ipse documento his, quos scelere tuo tecum adgregasti: sanguine tuo sancietur disciplina* (K 4907-4909) | Yes for the *sententia* quoted; the decree read from the tablet, *Thascium Cyprianum gladio animadverti placet* (K 4909-4910), is not rendered — see N1 | Yes | Yes (14, 16, 8) | "Discipline" in the Roman sense of public order, and the chunk pairs it with ANF's Pontius at the same point |
| *Deo gratias*, "Thanks be to God." (chunk 21; record 85-86) | K 4910-4911 | Yes | Yes | Yes | Sound |
| The cry, with *Et nos cum ipso decollemur* (chunk 23; record 88-90) | K 4913-4917 | Yes, both sentences | "called out" for *dicebat* is a slight lift in force, acceptable in narration | Yes (15) | Sound |
| The field, nine sentences (chunk 25; record 96-101) | K 4917-4923 | Yes, all ten clauses | Yes | Yes (longest 17) | "tunic" for *dalmatica* avoids the modern vestment sense; "cloak" for *lacerna byrro*, "wait for" for *sustinere* sound |
| The eyes, two sentences (chunk 27; record 103-106) | K 4923-4927 | Yes | Yes | Yes (11, 22) | "strips of cloth" for *lacinias manuales* sound |
| The burial (chunk 31; record 109-112) | K 4927-4952 | Yes, every clause including *ita beatus Cyprianus passus est* | "martyrdom" supplies what *passus est* carries by idiom, and the same text names him *martyr* at K 4955; accepted, not raised | Yes | "with prayer" for *cum uoto*, "grounds" for *areas*, "torches" for *scolacibus* all fair |

**Result.** Every clause of every passage the two files quote is now rendered, with the one exception at N1. Nothing is added anywhere. No sentence runs past 25 words, each carries one thought, and no word carries a misleading modern sense. No summary is presented as a rendering: where the story record compresses, it says so in its own voice ("The *Acta* gives the sentence in nearly the same words", line 84), and the record's provenance line states that "the English renderings of the *Acta* are this build's own".

---

## New findings

### N1 (P2). The tablet's own words are the one clause not rendered

- **Where:** `Build/worlds/lpc/Story-Chunks/lpcstory006_the-death-of-cyprian.md:21` ("**The sentence.** The proconsul read it from a tablet.") and `records/lpc/story/lpc.story.the-death-of-cyprian.md:82`.
- **Evidence:** in the *Acta* the proconsul first speaks the *sententia* (*dixit uerbis huiusmodi*, K 4906) and then reads a written decree from the tablet: *et his dictis decretum ex tabella recitauit: Thascium Cyprianum gladio animadverti placet* (K 4909-4910). Both files render the spoken *sententia* and neither renders the decree, so the paragraph announces a tablet and then gives everything except what was on it — including the mode of death, which no *Acta* rendering in either file states. The framing also attaches the tablet to the spoken words rather than to the decree that followed them; Pontius's own tablet detail (`cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml:28066`) is a different moment.
- **Why P2:** nothing rendered is wrong, and the decree adds no contested fact; it is a completeness defect of the same kind as Round 10's P2-D, in the passage the paragraph is built on.
- **Fix:** render it — "Then he read the decree from a tablet: 'It is decided that Thascius Cyprianus be put to death by the sword.'" — and let the tablet sentence follow the *sententia* as it does in the Latin.

### N2 (P2). The death is rendered under a heading that credits it to the *Acta* alone

- **Where:** chunk line 31 ("**The burial.** Here only the *Acta* speaks. So the blessed Cyprian suffered martyrdom.") and record line 109 ("Only the Acta tells the burial. So the blessed Cyprian suffered martyrdom.").
- **Evidence:** *ita beatus Cyprianus passus est* (K 4927) is now rendered, as Round 10 asked, but placed after a sentence that restricts the paragraph to the *Acta*. Pontius tells the same death: *donec ad perpetrandam pretiosi uiri mortem … centurionis manum concesso desuper uigore firmatam … expediret* (H 41354-41357), the sentence both files quote in ANF's English. So the one fact both texts plainly share now reads as the *Acta*'s own, and the chunk's "Attested by both" list (line 51) does not include the death either.
- **Why P2:** an attribution slip in framing, not a false claim about a source's contents, and the surrounding paragraphs correctly mark the *Acta*-only burial details.
- **Fix:** "Both texts say he died. Only the *Acta* tells the burial." — then the burial clauses.

### N3 (P2). "Tells it more briefly" is no longer true of what is given

- **Where:** chunk line 17 and record line 72: "The *Acta* tells it more briefly, and it adds one detail".
- **Evidence:** the expanded *Acta* rendering now runs 37 words against about 28 words of Pontius quoted beside it, so the comparison inverts. The wording is a remnant of the shorter rendering Round 10 reviewed ("says the same in fewer words").
- **Fix:** "The *Acta* tells the same night, and it adds one detail".

---

## Other Round 10 P2s, outside this recheck's ordered scope and still open

Listed so they are not lost, not as findings of this round: P2-C, `Build/worlds/lpc/Doc_09_Story_Inventory.md:105` still cites "Doc_01 line 26" for the sermon-scope statement, which now stands at `Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md:30`. P2-E, `records/lpc/story/lpc.story.the-death-of-cyprian.md:96` still reads "Only the Acta tells what came before the blow", though Pontius narrates the bound eyes and the hurried executioner. P2-7, `Build/worlds/lpc/scripts/gen_story_index.py:340` still globs only `Doc09_Round*_Review.md`, so `Build/worlds/lpc/lpc_Story_Index.md` still reports eight review rounds. P2-F, re-scored on the current text: the chunk's story text FK 6.0 / FRE 75.3 and the record's `text` FK 6.5 / FRE 73.6, both below the grade-8 floor, no hard failures — essentially unchanged, and mostly the *Acta*'s own short sentences.

---

## Summary

The P1 Round 10 left open is fixed in the contested-claim record and in the generator that produces it, verified by a scratch regeneration. All four renderings that had dropped a clause now render it, and on a full clause-by-clause check of every *Acta* rendering in the chunk and the story record, nothing is added, every sentence carries one thought under 25 words, no word misleads in its modern sense, and no summary is dressed as a rendering. Three new P2s remain: the decree on the tablet is still unrendered (N1), the newly rendered death clause sits under an *Acta*-only heading (N2), and "more briefly" no longer describes the passage (N3). No new P0 or P1. These and the carried P2s belong in the next ordinary pass, logged under OG-53.

VERDICT: Approved to proceed
