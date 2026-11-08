# SSEVM — instructions for the Builder (Claude Code)

SSEVM = **Self-Sustainable Eco-Village Model**. This repository holds the shared plan and
structure. Later each location gets its own repository with the same structure
(SSEVM-Madinah, SSEVM-Brunei, SSEVM-Aceh…). The "M" may also stand for Mission or Madrasah.

You are the Builder. The SSEVM Architect gives you one task at a time in an issue or a
comment with "@claude". Build it on a new branch and open a pull request. Never merge,
never push to `main`. The Architect reviews and merges.

## Rules (from the owner)

1. **Privacy, always first.** One private word must never appear in this repository: no
   file, page, commit message, branch, issue or PR text. `tools/privacy-check.sh` matches it.
   Run `bash tools/privacy-check.sh` before every commit; it must print "clean". If you are
   unsure whether a word is allowed, leave it out and ask in the PR.
2. Plain words for a non-coder owner. Calm, spacious pages that work on a phone.
3. Every page is self-contained HTML (no paid services, no keys, no tracking).
4. Page titles: `<Name> - vNN - Jnn - DD.MM.YY - h.mm AM/PM` with the real Sydney time
   (`TZ=Australia/Sydney date`).
5. Health is the most important part: the village health plan links to the MSA Health app
   (https://madrasatul-muslimeen.github.io/app/). Education links to MSA. Link, never copy.
6. Write "Siyagah" in full. After "Rasulullah" always write "Sallallahu A'laihi Wa Sallam".
7. Figures for energy, water, land and buildings are rough planning ranges and must say so;
   a qualified designer checks them before anything is built.
8. Never spend money or credits.

## Layout

| Folder | What goes there |
|---|---|
| `plan/` | The overall village plan pages (concept plan, phases) |
| `village/` | Focus 1: homes, masjid, madrasah, clinic, hall, food, governance, money |
| `offgrid/` | Focus 2: energy, water, waste and toilets, food growing, building methods, site layout |
| `health/` | The village health plan (linked to MSA Health) |
| `education/` | The madrasah plan (linked to MSA) |
| `locations/` | Notes per location until each gets its own repository |
| `tools/` | Checks (`privacy-check.sh`) |
