# P2-G3b build: review brief for the person entries (Opus, round 1, full review)

You are an independent reviewer. Repo: read the vendored texts and corpus map in `/tmp/claude-0/-home-user-CIC-Project/169e494a-41f0-5483-9c1c-9d54f9275f46/scratchpad/g3b/lib1577` (a checkout of the Library PR that adds the texts these entries rest on) and the rulings in `/home/user/CIC-Project`; both read only. No model calls, no
network. Work from the census and the vendored texts, not from the drafters' conclusions.

Read the release 29 review brief and apply it in full:
`Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/Review_Brief.md` (facts against the
cited lines, grades, rulings, two-way check, readability, the mechanical helper). The drafting
brief is `../Person_Drafting_Brief.md` (in this folder's parent). The rulings these entries carry
out: `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, entries "The people list ruled;
P2-G3 applied as data release 29" and "The later-worlds people ruled (P2-G3b)" (2026-11-10).

Check also, for each entry:
1. **Ruling B** (answer C as written): Paula's Letter XLVI issued in her name counts as her own
   words; Pamphilus's Apology for Origen, which Eusebius calls written jointly with him, counts as
   his own words, with Jerome's denial named as the other side. An entry that says the person has
   no words of their own, or treats the Apology as not his, breaks the ruling (blocking).
2. **Record shape** matches release 29's person entries (`origen` and peers): status fields, kind,
   toldWithin, field set. `modernCountries` IDs copied from an existing census entry for the same
   place (check them); none typed from memory.
3. **Dates** sourced, or stated as the census's; start years used to order the home people row.
4. **concerns**: each assigned link's note or quotes are about this person; no existing value
   overwritten; flagged choices are sound.
5. **rows**: the replaced item really is this person.
6. **Renderings**: any English rendering of a non-English line in the prose must render every
   clause, add nothing, and use no word whose modern sense misleads. If one falls short, give the
   corrected rendering in your fix.
7. **legacy** says how the later traditions name the person without claiming influence the
   sources do not show.

Run `cd /tmp/claude-0/-home-user-CIC-Project/169e494a-41f0-5483-9c1c-9d54f9275f46/scratchpad/g3b/lib1577 && python3 ../build/check_draft.py <Draft.json>` on each draft.

Output `review.json` in your folder: `{"round":1,"scope":[...],"verdict":"approve|revise","findings":
[{"id","target","field","severity":"blocking|substantial|minor","problem","evidence","fix"}],
"checked":"..."}`. Severity as in the release 29 brief; no "could be stronger" findings. Reply
with a short summary.

## For this draft (`../p5/Draft.json`: Pamphilus, Bonaventure, Heraclius)

- The 13 entries already shipped (data release 31, on main in `/home/user/CIC-Project`) went
  through three review rounds; check these three against the same standard and against the fixes
  made there (floorNote only the doctrinal-floor note; caveats in sourcing; no unsourced dates).
- **Glosses.** Every place the prose says what a Latin, French or Italian line says (fact rows
  marked "plain gloss") is a rendering. Check each against the original: every clause, nothing
  added, no word whose modern sense misleads. Where one falls short, give the corrected sentence.
- **Heraclius's own words.** Answer C counts "a document issued or signed in their name". The
  Ecthesis was issued as his edict; a later letter has him say Sergius wrote it. Judge from the
  sources whether the entry states this fairly, and whether the Ecthesis still counts as issued in
  his name. If you judge it does not, say so as a blocking finding with the evidence.
- Pamphilus: ruling B counts the jointly written Apology as his own words; Jerome's denial is named.
