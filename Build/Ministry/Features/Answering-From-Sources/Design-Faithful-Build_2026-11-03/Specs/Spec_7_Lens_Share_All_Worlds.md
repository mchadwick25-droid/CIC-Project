# Spec 7: lens share and vectors for all twelve worlds (chunk D7)

**Model:** Sonnet. Read-only counts and a local build; no design.

**Purpose.** Each world searches only its own shelf. Before the held-out runs, know how much of each world's shelf its lens reaches, and which passages its own records cite that the lens leaves out.

**Inputs.** The merged search (`Sandbox/answering-library/search/`), the index, each world's corpus-map rows and records.

**Outputs.** One report in the Design-Faithful-Build folder: for each of the 12 built worlds, passages on the shelf, passages in the lens, the share; and the list of passages its records cite that are outside its lens, by file and row. Vectors built for every world with the local embedder (kept outside the repo, keyed by index version and lens hash).

**Must not touch.** Rows, records, the index, the search code.

**Test written first.** The run reproduces the four known shares (lpc 84.8%, alx 69.3%, syr 79.3%, rzg 100%) exactly.

**Done when.** The report is merged. A world with cited passages outside its lens goes to chunk D8 (row narrowing for that world, on request). **Cost:** none.
