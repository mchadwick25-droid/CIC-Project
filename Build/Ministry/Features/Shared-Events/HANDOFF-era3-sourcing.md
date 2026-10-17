# Handoff: Era 3 sourcing session (Monks and Empires, 451-622)

For the fresh source-research session that takes the next era batch. The Era 2 batch is
merged; start from `origin/main` on a new branch, `library/shared-events-era3`.

## Read first

- `CLAUDE.md`, then this folder's `README.md`, `Decision-Log.md` (every ruling to date,
  including the 2026-10-17 rulings on non-English sources, part order and legend notes) and
  the Era 3 table in `Candidates.md`.
- The Nicaea dossier, `dossiers/nicaea-325_Source_Readiness_Dossier.md`: it is the exemplar
  for shape, tone and the line-anchor discipline. The ten other Era 2 dossiers show the
  shape applied to thinner events.
- `cic/texts/INTAKE.md` and the header of any file added on 2026-10-17 (for example
  `synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt`) for the header
  convention, including the sentence that states which scripts the OCR recovered.

## The five Era 3 events, in Candidates.md order

1. Henotikon of Zeno and the Acacian schism (482-519). Already good: Evagrius III prints the
   Henotikon; Zachariah, John of Nikiu, Philoxenus, Severus held. Era 2 added Evagrius in
   Greek (Bidez and Parmentier 1898), John Rufus's Plerophories (PO 8.1), the Life of Peter
   the Iberian, Timothy Aelurus in Armenian, Michael the Syrian tome II. Wanted: the Roman
   side in its own words (Gelasius I, Felix III: the Collectio Avellana, CSEL 35, was being
   vendored by Era 2 group A; check `cic/texts/` before fetching), Simplicius; the Latin
   Liber pontificalis (Duchesne 1886-1892, or Mommsen MGH 1898).
2. Synods of Beth Lapat (484) and of Acacius (486). The Synodicon Orientale (Chabot 1902,
   held) carries the 486 acts; Braun's German too. Barsauma's letters survive in the
   Synodicon's appendix. Check PO 7 (Chronicle of Seert part II) for 484-486: Era 2 group C
   found Seert's first part stops at 422 and the second starts at 484; PO 7 was verified
   as a lead and not fetched.
3. Councils of Dvin (506, 554). Nothing held. The Book of Letters (Girk' T'lt'oc', Tiflis
   1901) was searched for on archive.org by Era 2 group D and not located. Try Langlois,
   Collection des historiens de l'Arménie, vol. 2 (held? group A fetched it for Era 2:
   check), the Narratio de rebus Armeniae (Greek, in Combefis or PG 132), Ter-Minassiantz,
   Die armenische Kirche in ihren Beziehungen zu den syrischen Kirchen (TU 26, 1904, German
   with Armenian documents translated), and Arsen Sapara's Georgian history for Kyrion. The
   Georgian side (Kyrion's letters) is in the Book of Letters only; say so if it stays
   unreachable.
4. Second Council of Constantinople (553) and the Three Chapters. Good base in npnf214,
   Evagrius, Zachariah, Cyril of Scythopolis. Wanted: the Latin dissent in its own words
   (Facundus of Hermiane, Pro defensione trium capitulorum, PL 67; Victor of Tunnuna's
   chronicle, Mommsen MGH AA 11, 1894; Liberatus's Breviarium, PL 68; Vigilius's
   Constitutum, in Mansi 9); Mansi tomus 9 (Welter facsimile, identifier pattern
   `sacrorumconcilio0009phil`, verify). The "altar columns" story: the Candidates table found
   no match in the files held; the earliest text is probably the Liber pontificalis's life
   of Vigilius or Theophanes; locate before citing.
5. Third Council of Toledo (589). Only indirect sources held. Wanted: the acts (Mansi 9;
   Vives, Concilios visigóticos, 1963, is in copyright; the PL 84 Collectio Hispana scan on
   archive.org), John of Biclaro's chronicle (Mommsen MGH AA 11), Isidore's Historia
   Gothorum, Leander's homily at the council (PL 72). The Homoian side (the Gothic bishops'
   recantation statements are inside the acts) survives only there.

## Method notes from Era 2

- archive.org search, metadata and djvu.txt download all work from the sandbox; gutenberg,
  ccel.org, scaife and wikisource are reachable; the patristic sites, MDZ, Gallica and
  HathiTrust are blocked. Log any blocked need; do not work around it.
- Check what the OCR recovered before vendoring. Several Google scans recover only the
  Latin-script column: Lauchert's Greek canons and Parmentier's Theodoret recovered no Greek
  at all; the Patrum Nicaenorum Nomina recovered only the Latin lists. State this in the
  Language line of every mixed-script header.
- Migne PG volumes on archive.org (`patrologiae_cursus_completus_gr_vol_0NN`) have usable
  Greek but a garbled Latin column; vendor as second witness only.
- Some archive.org uploaders attach a CC BY-NC-ND licence to their scan of a public-domain
  printing (seen on a Patrologia Orientalis upload). Era 2 avoided those scans where a clean
  alternative existed and raised the question to Mark; check the decision log for his ruling
  before relying on such a scan.
- `cic/texts/` passed 800 MB in the Era 2 batch. The planning trigger in
  `Build/worlds/_cross-world/PLAN-texts-store-scaling.md` is 4 GB (Mark, 2026-10-17). Size
  is no reason to leave out a source the event needs. Still prefer the one volume that holds
  the event over a whole set.
- Workers run in parallel (one per two or three events) and write only vendored files,
  staging yaml, dossiers and scratchpad fragments; the coordinator merges REGISTRY and seed
  rows, regenerates README and the download queue, and commits. Strip dated comment lines
  from fragments: `tools/check_live_commentary.py` rejects them in the seed file.
- One PR per era, draft first, pushed once after the local checks pass:
  `python cic/engine/texts_registry.py` (and `--write-readme`, `--check-readme`),
  `python cic/engine/corpus_map_merge.py --check` then the merge,
  `python tools/check_live_commentary.py --base origin/main --enforce`,
  `python tools/check_paths.py --baseline tools/check_paths_baseline.txt`,
  `python Build/worlds/_cross-world/gen_download_queue.py`.
