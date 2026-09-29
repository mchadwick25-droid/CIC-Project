# Library decision log — rulings that govern the corpus, not one world

Hand-written, append-only, no-rewrite-history — the same discipline
`cic/texts/REGISTRY.yaml`'s own header already states for itself. An entry
records what was ruled, when, why, and what it changed; it is never edited
to match a later ruling. A later ruling gets its own entry and says plainly
what it supersedes.

This is where a rule's *reasoning* lives. The rule itself, stated plainly
with no history in the document, lives in the file it governs (here,
`cic/texts/INTAKE.md`) — the same split this project already draws between
`Ministry/`'s decision logs and the canonical documents they explain.

---

## 2026-09-29 — Cross-world placements for the Ottoman Orthodoxy sources are made now, by the Library

**Ruling, Mark's own words:** "do the cross-world now, i don't think the
build is a rigorous as you are and they may miss it".

**Context.** The 17 sources vendored for
`orthodoxy-under-the-ottomans-parish-millet-and-n` were first assigned only
to that entry, and the cross-world homes were put to Mark as a question
because cross-world placement is an "Always ask" category. He answered that
the Library should place them itself.

**What was placed** (all rows are in `cic/corpus-map/_staging/`; the reasoning
is in each row's own note):
- `the-kyiv-mohyla-orthodox-revival`: Mogila's Confession, in Overbeck's
  English and in Kimmel's Greek and Latin (tradition, assigned).
- `the-union-of-brest-and-ruthenian-greek-catholic-`: the same two Mogila
  rows (context, provisional; the file text was not checked for its treatment
  of the union).
- `the-reformed-cities-zurich-and-geneva`: Lucaris's Confession in three
  editions (context, provisional; whether Lucaris was a Calvinist is disputed)
  and Aymon's edition of Lucaris's letters (context, assigned: the first letter
  is addressed to the Republic of Geneva and the second to Diodati at Geneva,
  verified against the file's table of contents).
- `lutheran-wittenberg-and-its-congregations`: the 1584 Acta, the Tubingen
  theologians' letters (tradition, provisional, since they are Tubingen and
  not Wittenberg theologians) and the Patriarch's answers (context,
  provisional).
- `orthodoxy-under-the-ottomans-1650-1821`: Dositheus and the 1672 Synod in
  English and Greek, Georgirenes, Rycaut, Smith, and the later Greek books
  (Pedalion, Synaxaristes, Euchologion, Horologion, all provisional).
- `the-kollyvades-and-greek-renewal`: Nikodemos's Pedalion and Synaxaristes
  (tradition, provisional; the placement rests on Nikodemos's historical
  identification as a Kollyvade, not on the files' own text).
- `byzantine-church-palaiologan`: Sphrantzes, Cananus, Anagnostes and Doukas
  (context, provisional).

**Not placed.** `russian-church-stoglav-to-nikon`: Mogila's Confession reached
Moscow only after the window's mid-century, and no file text supports the
fit. It waits for that entry's own build.

**Changed.** Two new corpus-map buckets
(`byzantine-church-palaiologan`, `orthodoxy-under-the-ottomans-1650-1821`)
and added rows in six existing ones. Nothing in any built world's records or
package: the corpus map is outside the compile path.

---

## 2026-09-29 — Non-Western worlds may proceed on an honestly lopsided ecology, Ottoman Orthodoxy first; a protected English translation points to a public-domain original

**Ruling, Mark's own words, two messages in one session.** On the source
search: "remember to look for other language sources that are public
domain, so if there is an english translation version that is protected
that will most certanly come from another language source we can access".
On whether a non-Western candidate may go forward when its public-domain
ecology is strong in some genres and thin in others: "yes, allow it for
Ottoman Orthodoxy first".

**Context.** A four-candidate probe of non-Western entries in eras 6 and 7
(`ethiopian-christianity-gragn-to-fasilides`, the St. Thomas Christians
under Portuguese pressure, `orthodoxy-under-the-ottomans-parish-millet-and-n`,
`hesychasm-and-the-palamite-synthesis`) found none READY. All four were THIN
BUT VIABLE, with strong chronicles and outside witnesses and weak inside
doctrine and prayer. Mark's test for the probe was that the ecology must be
broad enough to build a full world from.

**What this rules.**
- Where an in-copyright English translation exists, the source search looks
  for the public-domain original-language edition behind it (Greek, Latin,
  Ge'ez, Church Slavonic, Malayalam, Portuguese, Italian and the rest), and
  for a clean text of it. A clean original is primary under the 2026-09-25
  ruling below, and the English is rendered from it. A garbled scan stays a
  second witness.
- `orthodoxy-under-the-ottomans-parish-millet-and-n` (VI.17) may proceed
  first, on a lopsided ecology. Each missing genre is recorded as an absence
  in the world's own gap tracking, and a Representative never fills it.

**What this does not rule.** The other three candidates are not approved;
they wait for more acquisition. Two related questions were put to Mark and
are still open: whether a public-domain scholarly translation (Conti Rossini's
French and Latin versions of Ge'ez chronicles) may stand in for a garbled
original or is a cross-check only, and whether the Beta Masaheft
Galawdewos file (CC BY-SA 4.0, based on a 2016 critical edition) may be
vendored. This entry does not answer either.

**Changed.** Nothing in `cic/texts/INTAKE.md`'s rules; its 2026-09-25 text
already covers original-language primary evidence. The Ottoman Orthodoxy
world is a build candidate, subject to its own Step 0 through Doc_02 review.

---

## 2026-09-25 — Non-English originals can be primary evidence; language is not the test

**Ruling, Mark's own words:** "non english sources are treated as primary
sources if they are primary sources to the world. language should not
matter, only the sources credibility and truth."

**Context.** Relayed through a coordinating "managing thread" session as
part of a study into how the library (Steps 0-2) should be set up to best
support a new build process, where the library owns Step 0 through Doc_02
review and a separate build thread starts at Step 3 from the library's own
handoff package. Confirmed directly by Mark in this session before being
acted on — a governance/methodology change of this kind is never executed
on a relayed claim alone, per this project's own standing rule (CLAUDE.md,
"Governance or methodology change" -> "Always ask").

**What it replaces.** `cic/texts/INTAKE.md`'s rule in force from 2026-09-02
(when original-language sourcing began) through today: an original-language
text was a second witness by definition, never primary evidence for a
Representative, because English was named as the project's own evidence
language. That framing predates this ruling and is retired, not merely
revised.

**Reasoning.** The old rule conflated two different questions — is this
text a primary source for the movement it documents, and is it in English —
and let the second answer override the first regardless of the text's own
actual evidentiary standing. A movement's own founding documents, letters,
and institutional records do not stop being primary because they were
never translated, or because the only translation available is itself
in-copyright. What should gate whether a source can be quoted is the two
things that have always mattered for any source in this corpus: whether it
is credible and true to the movement it speaks for, and whether the vendored
text is clean enough to quote from without guessing at what a garbled scan
actually says.

**What changes, concretely:**

1. A clean public-domain original-language text can be primary evidence, on
   the same footing as an English translation would be, when it is primary
   to the world it's assigned to.
2. Quote records hold the original-language text, verified against the
   vendored file - the same verification discipline this project already
   requires for every English quote.
3. The modern English a Representative speaks is an Opus translation of the
   original, independently Opus-checked, and the record states plainly that
   it is rendered from the original rather than drawn from an existing
   English edition.
4. A public-domain English translation, where one exists, becomes a
   cross-check against the Opus rendering - useful corroboration, not a
   precondition for using the original.
5. Scan quality, not language, now decides quotability. A garbled OCR
   scan stays second witness until a clean witness of the same work is
   vendored - this is Mark's OCR ruling "a" (2026-09-25), logged here
   because it's the mechanism that makes point 1 workable rather than a
   license to quote from unreadable text. Systematic, deterministically
   normalizable encoding failures (long ſ, þ, ð) are handled in the quote
   gate itself, not treated as garbling. Per-edition OCR substitution
   patterns (an edition rendering þ as `])`/`]?`, for instance) are
   recorded as `apparatus` mappings in `cic/texts/REGISTRY.yaml`, each one
   verified against page images before it's trusted. No model ever retypes
   a source to work around a bad scan.

**Files flagged, at the time of this ruling, as garbled scans held to
second-witness status under point 5** until a cleaner edition is vendored:
the Ausbund (`ausbund_lancaster1846-deu.txt`), the Hutterite Geschicht-Buch
(`hutterite-brethren_geschichtbuch_wolkan1923-deu.txt`), the 1606 Jesuit
Constitutions (`jesuit-constitutions_constitutiones-societatis-iesu-lat_1606.txt`),
Ribadeneira's 1572 Vita Ignatii Loiolae
(`ribadeneira_vita-ignatii-loiolae-lat_1572.txt`), Nadal's 1595 Adnotationes
(`nadal_adnotationes-et-meditationes-in-evangelia-lat_1595.txt`), and Pole's
1560 Oration (`pole_seditious-oration_wythers1560.txt`). This list is a
snapshot at the ruling's own date, not re-verified on every later read of
this entry - check each file's own current header for its live status.

**What this document does not do.** It does not re-run the primary/second-
witness classification for every already-vendored original-language file in
the corpus - that is a real, separate pass (`cic/corpus-map/`'s own
`_staging/` entries, one file at a time), tracked as follow-up work, not
folded silently into this log entry.

---

## 2026-09-24 — lpc's cross-link into the Petschenig Augustine anti-Donatist edition is a project-lead placement decision, not the dossier's own call

**Ruling.** Four of the six assignments in
`cic/corpus-map/_staging/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.yaml`
double-place to `latin-pastoral-congregational-christianity` (lpc) as a
second `tradition` row, alongside their existing `donatism` assignment:
De Baptismo, De Unico Baptismo contra Petilianum, Contra Cresconium, and
Contra Epistulam Parmeniani. Wired in commit `d4512b64` (2026-09-24),
whose own commit message states this cross-link was one the lpc Source
Readiness Dossier flagged and Mark authorized.

**Why this needs its own entry, not just the dossier's.**
`latin-pastoral-congregational-christianity_Source_Readiness_Dossier.md`
§2 identifies the same-work-different-language pairing pattern and the
"not presently reachable from this world's own bucket in any other form"
reasoning for the two English-less works, but the dossier itself states
that whether to actually double-place is "Doc_02's or the project lead's
call, not this dossier's." The double-placement is a cross-world
placement decision - an "Always ask" category - and the record that Mark
was asked and said yes belongs in a decision log, not folded into the
dossier's own reasoning as if the dossier had decided it.

**What this entry does not have.** Mark's authorization is known only
from commit `d4512b64`'s own message ("Mark authorized"); no verbatim
ruling text survives elsewhere. This entry records that the decision was
made and by whom it was made, not a quote that doesn't exist - do not
back-fill one.

**Scope.** Psalmus contra Partem Donati and Contra (Adversus) Fulgentium
Donatistam, from the same source file, are NOT part of this authorization
(not named in the dossier's own §2 reasoning) and stay donatism-only.
