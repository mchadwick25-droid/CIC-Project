# V7 controlled test: rubric

Ten dimensions, each scored and reported on its own. There is no composite score (Mark, §6). Each dimension is scored 0, 1 or 2 against the anchors below. The reader also writes one sentence of reason for each score.

| # | Dimension | 2 | 1 | 0 |
|---|---|---|---|---|
| 1 | **Source accuracy** | Every quotation, attribution, date and named fact matches the cited source | One slip of detail that does not change the meaning | A misquotation, wrong attribution, or invented fact |
| 2 | **Contextual integrity** | Each source is used as it works in its own setting and argument | A source is used slightly loosely, but its setting would not overturn the point | A source is pulled out of its argument, occasion or audience so that the point changes |
| 3 | **Interpretive fidelity** | The explanation claims what the source can bear, and the answer marks interpretation as interpretation | Mild overreach, or interpretation not clearly marked | The explanation claims what the source does not establish, or a supposition is presented as teaching |
| 4 | **Answers the question** | Answers what the visitor asked, early and directly | Answers part, or answers late | Talks around the question |
| 5 | **Fidelity to the world** | One author's view, a circle's view and the world's view are kept distinct, as far as the evidence supports; tensions inside the world are shown where they matter | One blurring of whose view is whose | One author is made to speak for the world, or a practice is presented as universal |
| 6 | **Natural and engaging** | Reads as a thoughtful person talking, with the world's own imagery | Correct but flat, or a little stiff | List-like, defensive, or full of disclaimers |
| 7 | **Honest uncertainty** | Uncertainty and disagreement are stated plainly where they exist, and not invented where they do not | Uncertainty present but vague, or a little overstated | A disputed or uncertain matter is presented as settled, or a settled one is hedged into nothing |
| 8 | **World embodiment** | A member speaking from within the world: its convictions, practices and ways of seeing | Mostly from within, with some outside description | An encyclopedia describing the world from outside |
| 9 | **Conversational quality** | Natural, direct and sized to the question. A simple question gets a simple answer. | A little long, or a little indirect, for what was asked | A lecture in reply to a simple question, or a fragment in reply to a deep one |
| 10 | **General-user accessibility** | An ordinary adult can follow it without specialist knowledge; terms are explained before they are used | One unexplained term, or one hard sentence | Needs specialist knowledge to follow |

**Depth** is reported beside these as in CP.9 (rich, adequate, thin, flat). Mark named depth as non-negotiable, and it is a success rule in `Test_Plan.md` §8.

## Error log

Readers and human reviewers list each error they find, apart from the scores:

| Field | Values |
|---|---|
| sentence | The words, quoted from the answer |
| type | One of Mark's failure list: out of context; claim beyond the source; one author as the tradition; does not answer; beyond the author's intent; modern projection; flattened uncertainty. Or: invented; misquoted; other (say what). |
| severity | tier 1: false or invented. tier 2: misleading scope, context or interpretation. tier 3: craft. |
| sure | sure, fairly sure, unsure |
| evidence | The source and lines that show the error, when the reader can name them |

## How the readers work

- **Model readers.** Two independent Opus readers per answer, at the highest effort, plus a third Opus pass that adjudicates (`Test_Plan.md` §6).
  - They read blind: no arm labels, and answers are shuffled with a seed written into the run file before the draw.
  - Each reader gets:
    - the question and the whole answer;
    - every cited record, with its reading card where one exists. The card is marked as project-authored and is checked against the source.
    - the source passage with its surrounding division;
    - the world's lexicon risk flags.
  - Every error is bound to the exact words of the answer and of the source.
  - Seeded defects come first. The readers' scores count only if they catch at least 9 of every 10 seeded defects.
  - Where a question has a trap note (the optional hard-case set only), the note is opened after the blind scores are filed. The reader may then add errors, marked "after trap note".
  - Both arms are scored fresh by the same readers. The October reviews of A are reported beside the fresh scores, never in place of them (`Test_Plan.md` §6).
- **Agreement** is reported per dimension: exact agreement, and agreement within one point. A dimension where exact agreement falls below 60% is reported as "readers unreliable here". **Assumption:** the 60% line is set here, before the run.
- **Mark's own reading** uses the same error log, in plain words, on the review page described in `Test_Plan.md` §6. He records error yes or no, type, severity, how sure he is, and a note. He gives no dimension scores unless he wants to.
