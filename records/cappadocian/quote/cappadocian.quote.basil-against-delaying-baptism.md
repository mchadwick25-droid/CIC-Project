---
id: cappadocian.quote.basil-against-delaying-baptism
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-T
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: "The Prolegomena's own text notes that St. Augustine (In Julian. vi.) cites this homily
    as St. Chrysostom's, 'but the quotation has not weakened the general acceptance of the composition as
    Basil's, and as one of those referred to by Amphilochius' (Orat. ii.) - an ancient authorship wobble the
    source itself resolves in Basil's favor, carried here rather than smoothed over. Separately: this excerpt
    is Homily XIII's own translated sermon prose, in quotation marks and tied to a specific section number
    (endnote 646, '§5.'), but it survives in this vendored file only as a quotation embedded inside the
    Prolegomena's own 'Works: Homiletical' survey (div1 Prolegomena > div2 Works > div3 Homiletical) - the
    homily itself has no standalone div anywhere in npnf208_basil-letters-select-works.xml, unlike the
    Hexaemeron homilies or De Spiritu Sancto, which are fully vendored as their own divisions. This is a
    different, more favorable gap than cappadocian.source.basil-against-eunomius documents for the
    three-book treatise: there, the Prolegomena only discusses the work in third-person summary with no
    quotation at all; here, real quoted, translated, section-numbered sermon prose is genuinely present -
    just as a curated excerpt rather than the homily's complete text. The text is checked directly against
    what the vendored file prints, but what the file prints is itself the NPNF editor's own selected
    citation of Basil's homily, not the homily's own complete, independently-checkable text (which is not
    vendored at all, per world_core's own caution and this world's established verification_state mapping:
    A-grade direct primary-text access is verified-direct; content resting on a citing authority's own
    selection/quotation is verified-via-authority). That is why this record's verification_state is
    verified-via-authority."
sources:
- source_id: cappadocian.source.basil-antiphonal-psalmody-baptismal-letters
  locus: "Homily XIII, On Holy Baptism, §5 (per endnote 646) - quoted within the Prolegomena's own 'Works:
    Homiletical' survey, para id vi.ii.v-p130 (npnf208_basil-letters-select-works.xml, lines 7017-7024);
    this is the 'baptismal protreptic to delay-prone catechumens' half of this source record's own `work`
    field, not yet pinned to an exact locus before this record"
  license: public-domain
text: >-
  Art thou a young man? Secure thy youth by the bridle of baptism. Has thy
  prime passed by? Do not be deprived of thy viaticum. Do not lose thy
  safeguard. Do not think of the eleventh hour as of the first. It is
  fitting that even at the beginning of life we should have the end in
  view.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader might expect deathbed baptism to have been a fringe habit
  that only strict clergy bothered to scold. Basil's own pulpit tells a
  different story: he treats the delay as common and respectable enough to
  need a direct counter-argument, aimed at both ends of life at once - the
  young man tempted to wait, and the man whose "prime hath passed" who
  might now reason it is too late to bother, or safer to wait a little
  longer still. Both get the same answer: don't treat the last hour as
  though it were the first one, and don't assume you get to choose which
  hour is yours.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether this world would call what happened to them being born again"
  - "participant asks whether this world baptised babies or only adults who chose it for themselves"
relations:
- type: associated-with
  target: cappadocian.dw.baptism-and-new-birth
modern_rendering: >-
  Are you young? Guard your youth with baptism's bridle. Has your prime passed by? Do not
  go without your viaticum. Do not lose your safeguard. Do not treat the eleventh hour as
  if it were the first. Even at the beginning of life, it is fitting that we already have
  the end in view.
use_note:
  means: "Basil's Homily on Holy Baptism, known here only through an excerpt quoted in the NPNF Prolegomena, urges young and old alike not to postpone baptism."
  not_for:
    - "the whole text of the homily as checked here, when only an editor's excerpt survives in the vendored volume"
    - "a claim that this world baptized infants or did not, a question cappadocian.dw.baptism-and-new-birth says the record cannot settle"
    - "deathbed baptism as a fringe habit rather than a practice common enough to need a sermon"
  years: {from: 360, to: 379}
  status: provisional
---
Found by following the build brief's own trail. `grep -n "Homily
XIII"` on `cic/texts/npnf208_basil-letters-select-works.xml` returns one
hit, line 7005: "In Homily XIII., on Holy Baptism, St. Basil combats an
error which had naturally arisen out of the practice of postponing
baptism." A structural check (`grep -n 'div1'`) shows this file's only
top-level divisions are Title Page, Preface, Genealogical/Chronological
Tables, Prolegomena (id="vi"), De Spiritu Sancto, The Hexaemeron, The
Letters, and Indexes - there is no "Homily XIII" or "On Holy Baptism"
div anywhere, so, like cappadocian.source.basil-against-eunomius's
three-book treatise, this homily's complete text was never vendored on
its own.

Unlike that treatise, though, the Prolegomena does not just summarize
Homily XIII in the third person - it quotes it. Lines 7017-7024 (para
id `vi.ii.v-p130`, inside div3 "Homiletical" (`vi.ii.v`), div2 "Works"
(`vi.ii`), div1 "Prolegomena" (`vi`)) read, in full: 'Baptism is good at
all times.[§5.] "Art thou a young man? Secure thy youth by the bridle of
baptism. Has thy prime passed by? Do not be deprived of thy viaticum. Do
not lose thy safeguard. Do not think of the eleventh hour as of the
first. It is fitting that even at the beginning of life we should have
the end in view."' The bracketed "[§5.]" is endnote 646, an internal
section citation into the homily itself - the editors are citing a
specific paragraph of a real translated text, not paraphrasing a
scholarly impression of one. The next paragraph (lines 7026-7034, "§6.")
quotes a second passage from the same homily, on the eunuch of Acts
viii. 27 who did not delay his own baptism; it was left out of this
record's `text` field to keep the excerpt tightly on the "delay is a
dangerous bet against an unknown hour of death" argument the dw actually
makes, rather than splicing two separately-numbered sections into one
field.

Checked per the build brief's step 4: `ls cic/texts/ | grep -i basil`
turns up `basil_address-to-young-men_padelford1902.txt`,
`basil_ascetic-works-longer-shorter-rules_clarke1925.txt`, and
`morison_st-basil-and-his-rule_1912.txt` alongside the NPNF volume; none
of the three concerns baptismal delay (young-men is on classical
literature for students, the ascetic rules govern monastic life, and the
Morison volume is a modern secondary study). A file-wide sweep for
`viaticum|eleventh hour|delay.*baptism|postpon.*baptism|hour of death`
turns up three other hits, all irrelevant to baptismal delay specifically:
line 38202 is a Benedictine editorial endnote on Canon 217 about
unbaptized men, Ambrose of Milan and Nectarius, being elevated straight
to a bishopric, not about deathbed baptism of ordinary believers; line
38533 is Canon 217 §73 on restoring a lapsed apostate to communion "in
the hour of death," a penance question, not a baptism one; line 26901
("the hour of death, the imminent sentence of God") is inside an
unrelated letter of consolation to a fallen virgin meditating on her own
mortality, not a baptism argument. No other Basil-on-delayed-baptism
material exists in the vendored corpus.

Normalization: the source hard-wraps prose and double-spaces after
periods (e.g. "baptism.  Has thy prime"); normalized to single spaces
for the `text` field. The source's own curly quotation marks (opening
the excerpt at "Art" and closing it after "view") were dropped, as was
the inline endnote marker after "times." (§5) that sits outside the
quotation itself. No word was added, dropped, substituted, or reordered.

Fit to cappadocian.dw.baptism-and-new-birth: that dw's claim is that many
of this world's baptisms were adult and deliberately delayed, "some of
us waited until we were dying," and that "our own preachers argued hard
against that delay, calling it a dangerous game with an uncertain hour of
death." This excerpt is that argument in Basil's own translated words,
addressed to both a young man who might defer and an older man who might
now reason it is too late to start: baptism should not wait for a
self-chosen "eleventh hour," because no one is promised he will recognize
it as his last.

The spoken form is a modern-English translation, never the archaic original; the original stays as the record's own text field, shown at Level 3.
