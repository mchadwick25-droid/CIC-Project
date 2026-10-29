# Fleet run 1, second-pass review: rubric

Purpose: a strategic, decision-oriented read of ONE world's 28 answers. The first-pass review failed any answer with one flaw ("any P1 = FAIL"). This pass asks the questions that matter for go-live: is it scholarly acceptable, is it readable and succinct, and is it worth what it costs.

You are judging a Representative: a voice speaking from inside a historical Christian community, using only that world's records. The answer must stay inside the world's own time window and its records.

## Lens 1: RIGOR (accuracy and context). Standard = scholarly acceptability, NOT perfection.
Ask: would a competent historian of this period and tradition accept this answer as accurate, in context, and honestly hedged where the evidence is thin?
Grade each answer:
- **SOUND**: accurate and in context; claims traceable to the cited records; limits stated honestly.
- **ACCEPTABLE**: small imprecision, thin coverage, an uncited generalisation, or an omission, but nothing a scholar would call wrong or misleading. Ships as is.
- **NOT ACCEPTABLE**: a scholar would object. Only use for: factual error; invention (a person, text, place, event or attribution not in the records); anachronism (knowledge after the world's window, e.g. later councils, churches, movements); a quote used against its own context or misattributed; a contested claim stated as settled; a false denial ("our record says nothing" when a record does speak); or the answer addresses a different question than asked.
Rules: verify before you mark NOT ACCEPTABLE. Find the cited record(s) at records/<world>/<type>/<record id>.md (types: doctrinal_witness, quote, source, honest_limit, world_core, force, gravity, term, figure, story, contested_claim, demonstration, voice_craft). Read the record's use_note (means / not_for), claim_guard and any caution. Quote the exact record text that contradicts the answer, or state that no record supports the claim. If you cannot verify from the records, say "unverified" and grade ACCEPTABLE, not NOT ACCEPTABLE. Do not use outside scholarship to fail an answer unless the error is plain and well known, and then say so.
For each NOT ACCEPTABLE give a cause layer: RECORD-GAP (no record covers it), RETRIEVAL (a record exists but was not cited/offered), VOICE (the model said more or other than the records), ENGINE-CUT (an orphan pronoun or dangling lead-in shows a removed sentence), or HARNESS.

## Lens 2: ACCESS and CRAFT (readable, understandable, succinct). Grade each as GOOD / FAIR / POOR.
- **Readable**: plain adult English, serious but clear (target: reading grade about 8 to 10, Flesch Reading Ease 60 or more; measures are given per answer, use them as a guide, not a rule). Sentences mostly 12 to 20 words; none past about 30. No unexplained jargon.
- **Understandable**: a non-specialist could follow it without help. POOR if it has orphaned pronouns ("he" with no one named), a "so" or "yet" with nothing before it, a teaching announced and never given, build vocabulary or system talk ("the records I hold", "this turn", "the voice", raw [[tags]], record ids), or chatbot cadence ("The short answer first. Yes.").
- **Succinct**: length fits the question. POOR if padded, repetitive, lectures, or a long list when the question asked for one thing. Typical good answers are 120 to 260 words; judge against the question, not a number.

## Lens 3: COST. Do not grade cost. Per-answer cost and tokens are given in the measures. In your world summary, say which answers were longer than their value (words beyond what the question needed), since output tokens are the part we can change.

## Overall call per answer (one word)
- **SHIP**: Rigor SOUND or ACCEPTABLE, and no POOR in access/craft.
- **FIX**: Rigor SOUND or ACCEPTABLE but at least one POOR in access/craft.
- **BLOCK**: Rigor NOT ACCEPTABLE.

## Output
Write ONE file: /tmp/claude-0/-home-user/233cea43-1945-55ed-85c1-124ce73e9be5/scratchpad/fr1/out/<world>.json containing:
{"world": "...", "answers": [ {"n": 1, "cell": "C-I", "rigor": "SOUND|ACCEPTABLE|NOT ACCEPTABLE", "cause": null or layer, "rigor_note": "one or two sentences; for NOT ACCEPTABLE quote the answer's words and the record text or 'no record'", "readable": "GOOD|FAIR|POOR", "understandable": "GOOD|FAIR|POOR", "succinct": "GOOD|FAIR|POOR", "craft_note": "one sentence, quote the offending words if POOR", "overall": "SHIP|FIX|BLOCK", "words_beyond_need": integer estimate }, ... 28 items ],
 "world_summary": {"top_rigor_problems": [...up to 3...], "top_access_problems": [...up to 3...], "cost_note": "...", "go_live_view": "one paragraph: is this world fit to put in front of participants now, and the single most valuable fix"} }
Keep notes short. Be fair: grade what is there, credit what is good, and do not fail answers for style alone.
Do NOT read anything under Build/worlds/*/Review-Artifacts or engine/m3/reports (earlier reviews): form your own view.
