# Opus fifth read of the whole shipped surface — 2026-10-27

Ordered by Mark's second cap ruling. A fresh reader who rebuilt the shipped surface from the live files (the engine's `display_locus`, the use-note path, and the evidence block run in memory). One blocking finding on `don.contested.augustine-precipice-charge`. Mark ruled a third time: apply all fixes and run a repeatable method-word scan instead of a sixth Opus read.

Fifth read of the four honest-limits records. I edited nothing and made no model calls or network requests. I rebuilt the shipped surface myself from the live files: display_locus on every locus, use_note through the same path as builders._with_note, and the evidence block through engine.m4.evidence.assemble_evidence run in memory on the don and pahc records (no Facilitator `asks`).

**There is one blocking problem.** Record 4 (the cliff charge) reaches grieving visitors, and every surface it shows names the method of death and pairs it with Judas.

## (1) Verdicts

1. **don.limit.fate-of-those-who-end-their-own-lives: NEEDS CHANGES.** The text itself is safe. But the record does not fire on most real suicide questions, and record 4 fires in its place or beside it (findings 1 and 2).
2. **alx.limit.faith-alone-later-frame: NEEDS CHANGES.** One fact is wrong (finding 3).
3. **pahc.limit.assurance-and-the-dead: READY** to mark reviewed. Only nits.
4. **don.contested.augustine-precipice-charge: NOT FIT as it stands.** The siblings' not_for lines (not-a-death-wish, circumcellion-character) are clean: neither names a method or Judas.

## (2) Findings

**F1. BLOCKING. Record 4 shows the method and the Judas pairing on suicide questions.**

It reaches grief questions in three ways (simulated in memory):
- "My son jumped to his death. Is he with God?" goes to cell F6-E, because retrieve_when (lines 32–33: "threw themselves from cliffs", "jumped or were thrown") lends those words to F6-E. That question gets record 4, not-a-death-wish and the Passio Marculi story. Record 1 does not come back.
- "My brother killed himself. What would your people say happened to him?" (cells F1-T, C-E) pulls record 4 in by retrieval fill on the word "say".
- The F6-T question "…what happens when someone has died, if they killed themselves?" brings record 4 in beside record 1, by fill on "died".

What the voice receives:
- The head: "Some Donatist martyrs died by jumping from cliffs." (line 38)
- The means line: "threw themselves from cliffs" (line 47)
- The not_for line on "Augustine's verdict linking these deaths to Judas and the devil" (line 52)
- In the held_against lines you list as spoken: "whether they threw themselves down or were thrown down" (line 41), "thrown from the cliff" (line 42), and "Petilian's own taunt that the traitor hung himself … same master as Judas" (line 44).

What the visitor's card shows after display_locus:
- The label is the claim itself.
- "those who 'cast themselves down headlong from the summits of lofty mountains'"
- "'their daily sport to kill themselves, by throwing themselves over precipices'"
- "Marculus's death at the cliff: 'quem traditores occidere non timuerunt'" (cliff plus "traitors")

Should record 4 fire on a suicide question? No. Its cell is F6-E (outside accounts, and "isn't that a death wish"), which is a historical question. Tuning retrieve_when cannot stop it firing: fill reaches it on generic words, and `do_not_retrieve_when` must stay empty under the gate. So the fix has to make every surface safe even when it does fire.

Corrected text (I checked that none of it names a method or Judas):
- **claim:** `Some Donatists honoured as martyrs took their own lives. Two Catholic bishops say so.`
- **held_against line 2:** `Augustine's own case admits doubt. Of Marculus and Donatus, the deaths most often cited, he calls it a great question whether they died by their own act or were put to death by command (II.46).`
- **held_against line 3:** `The one Donatist account of such a death, the Passio Marculi, tells it as an execution. Marculus was put to death by his enemies.`
- **held_against line 5:** `His harshest verdict on these deaths (II.114) answers a taunt in Petilian's own letter. It is a judgment in a quarrel, not a report of events.`
- **means:** `Two Catholic opponents charge that Donatists honoured as martyrs people who took their own lives; this is hostile polemic about a contested group, not an independent report.`
- **not_for line 4:** `a claim that Augustine's harshest verdict on these deaths applies to anyone outside this dispute`
- **retrieve_when:** `participant asks whether Optatus's and Augustine's charges against the Donatist martyrs are true` and `participant asks how Marculus or Donatus died`
- **Optatus locus:** `Against the Donatists, Book III, chapter 4 (optatus_against-the-donatists.txt, line 2014): the charge that some sought death out of desire for a false martyrdom`
- **Letter 185 locus:** `Letter 185, chapter 3 (npnf104 line 19454): the charge that they killed themselves as a daily habit`
- **Passio locus:** `the Latin account of Marculus's death, told as an execution (monumenta-vetera-donatistarum_migne-pl8.txt, lines 1232-1235)`

Run through display_locus, these show only: "Against the Donatists, Book III, chapter 4: the charge that some sought death out of desire for a false martyrdom" / "Letter 185, chapter 3: the charge that they killed themselves as a daily habit" / "the Latin account of Marculus's death, told as an execution". None of them names a method, a traitor or Judas.

The new loci point at lines that say what the old wording quoted. Optatus line 2014 and Letter 185 at line 19454 are verbatim. In the Passio, the executioner pushes Marculus at lines 1232–1235 ("carnifex … in praeceps impulit martyrem").

**F2. SHOULD FIX, and needs a ruling. Record 1 rarely fires.** It has no `retrieval` block. In the simulation it came back for only one of eight natural phrasings, the one worded like the F6-T canon question. "Is suicide a sin?", "My son took his own life. Is he with God?" and "What happens to someone who ends their own life?" all missed it.

Proposed addition (lines 31–33):
```
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what happens to a person who took their own life or died by suicide"
  - "participant asks whether someone who killed themselves is with God, forgiven or damned"
```
Tested in memory with the F1 retrieve_when, it brought record 1 back for "takes their own life damned", "took his own life", and "did your martyrs kill themselves". It still missed "Is suicide a sin?", "ends their own life" and "killed himself… what happened to him". The deeper cause is in the engine. Fill pulls records in on single common words, and suicide vocabulary in one record's hints decides which cell a grieving visitor lands in. That is a fleet-level matter for Mark, not something this record can close. Real routing also depends on the Facilitator's `asks`, which I did not run.

**F3. SHOULD FIX. Record 2, line 30: "That commentary survives only in Rufinus's later Latin" is too wide.** Greek excerpts survive: the Tura papyrus covers Romans 3:5–5:7, which includes this passage, and there are catena fragments. The record's own search note says only that the Greek "is not vendored". Corrected text: `The full commentary survives only in Rufinus's later Latin, which shortens it. These are not Origen's exact words.`

**F4. NIT. Record 4 locus, line 18: "17573" should be 17575.** Paragraph 197 begins at line 17575; line 17573 is blank. Display is unaffected. Corrected tail: `…17532, 17550, 17575, 17715)`.

**F5. NIT. Blank YAML list entries with trailing spaces.** Record 1 line 39 and record 3 line 46 hold leftover blank lines inside not_for. Delete them.

**F6. NIT. Record 1 voice (lines 22–23).**
- The opening restates the visitor's question, which sounds like a rule being read aloud.
- "an answer of ours… words of ours" doubles up.
- "set terms on their fate" is abstract for B2.

Suggested: `I cannot give you an answer of ours. In our words that I know, there is no teaching on it. Optatus, who wrote against us, charged some of our people with seeking death to be counted as martyrs. That was a quarrel over who may be called a martyr. It was not a teaching about the dead. It is not mine to judge anyone who has died this way, or to say what has become of them.`

**F7. NIT. Record 3, line 34: "We will not name anyone's end for you."** A grieving visitor may hear "end" as how the person died. Suggested: `We cannot speak for any one person. We can tell you what our writers hoped.`

## Verified

- **Record 1:** Optatus III.4 at line 2014 is verbatim and the chapter is right. Its locus displays with no method. The statement gives no verdict and attaches no condition. The absence claim is limited to "the words of ours that I know", so it is no wider than what was searched. Years 311–439 are inside the window.
- **Record 2:**
  - Paedagogus I.6 is at lines 19356–19368.
  - Quis Dives 27 is at lines 56877–56880. Sections 27–29 do say love God, love your neighbour and do the Father's will.
  - Origen on Romans: "sola fide" is at line 13331 and the "past, not future" sins at lines 13410–13414.
  - Years 180–254 are honest to the sources.
- **Record 3:**
  - 1 Clement 50 is at lines 2124–2127 and Polycarp 9 at lines 3489–3491.
  - Trallians 9 is at lines 6618–6623, and it is the first (shorter) recension.
  - Polycrates is at anf08 lines 72582–72585.
  - Nothing denies that the dead are with the Lord, and nothing promises a destination.
- **Record 4:**
  - Every Answer to Petilian paragraph checks out against its line: 46 at 16209, 110 at 16857, 114 at 16889–16891, 160 at 17232, 193 at 17532, 195 at 17550 and 204 at 17715. Paragraph 197 is the one off-by-two noted in F4.
  - The Passio quote is at line 1313.
  - Years 366–417 are honest.
- **All four:** every source id exists. No record contains crisis wording or a redirect. Each means line is one sentence, and no not_for line opens with an imperative. The divergence_note reaches neither the voice nor the card.

## (3) Could not verify / outside scope

- I did not run the Facilitator classification or the live `asks`. Whether these grief messages are silenced as distress before retrieval is unknown.
- I did not check Origen Book III's chapter boundaries in the Latin.
- Outside the four records: the don compiled prompt, which is always in context, carries not-a-death-wish's own text. It includes "tells the readers to hurry… We will not pretend that sounds like a man talking anyone out of dying", plus several "thrown from a cliff" lines (Passio Marculi story, line 736 of the compiled prompt). That text is present on every suicide question whatever retrieval returns. It deserves its own safety read.

Simulation scripts: /tmp/claude-0/-home-user-CIC-Project/923cd92d-73ee-5833-a013-9b19000d9f81/scratchpad/sim.py and /tmp/claude-0/-home-user-CIC-Project/923cd92d-73ee-5833-a013-9b19000d9f81/scratchpad/sim2.py.
