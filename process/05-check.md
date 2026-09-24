# Stage 5 · Check

Prove the kit works before anyone installs it.

- **Input:** the built repo from stage 4.
- **Output:** a kit that passes the checker, the consistency review, and a dry run.
- **Gate:** `python scripts/check_kit.py` prints 0 errors and 0 warnings, and every issue from Steps 2-4 is fixed.
- **Time:** 20-40 minutes.

---

## Step 1 · Run the checker until it is clean

From the team folder:

```
python scripts/check_kit.py
```

1. Fix every error, then every warning. Warnings count: a kit ships at 0 and 0.
2. Rerun after each batch of fixes.
3. Never edit the checker to make an error go away. If the checker is wrong, fix the checker in the factory (`templates/team-repo/scripts/check_kit.py`), copy it into the kit, and note it in the factory CHANGELOG.

---

## Step 2 · Consistency review

The checker catches structure. This review catches meaning. Go through the one-source-of-truth table in [04-build.md](04-build.md) (Step 4) row by row:

1. Open the owner file and note the exact value.
2. Search every "must match" file for it (`grep -rn "<value>" kit docs README.md`).
3. Fix every mismatch in the non-owner file.

Then check these five things by reading:
1. Every command in the USER-GUIDE's "Things you can say" is in the lead charter's "Client commands", word for word, and the reverse.
2. Every specialist's "Must read" section equals its routing row.
3. The setup interview's coverage map covers every brain-file section, and every section's guidance comment in the brain file matches what the questions collect.
4. Every bank is written by the routine or the learning loop and read by at least one routing row.
5. The production steps follow `depends_on`, and DELIVERY.md sections follow the same order.

---

## Step 3 · Residue and gap scan

Run from the team folder and read every hit:

```
grep -rniE "pillar|newsletter|ritual|PACK\.md|\bpacks?\b|EIC|Editor-in-Chief|Almanac|lead magnet|KEYWORD" kit docs README.md
grep -rnE "TODO|TBD|lorem|XXX|FIXME|\?\?\?" kit docs README.md
```

1. For a content team, the first scan's hits are expected; review them anyway.
2. For any other team, every hit is a leftover from the reference kit: rewrite it for this domain.
3. The second scan must return nothing.

---

## Step 4 · Dry run (paper test)

Play the installing bot and the first client, following the kit's words literally. Do not fix anything while you read: write every problem down first.

1. **Install (Grokbot).** Walk `kit/INSTALL.md` Steps 1-10. At each step, ask: do I know exactly what to do, where the file is, and what counts as done?
2. **Install (Hermes).** Walk `kit/INSTALL-HERMES.md` the same way, checking every Hermes-specific instruction against `agent-team-factory/docs/HERMES-NOTES.md`.
3. **Setup.** Invent a fictional client in one line (for example "Maya, owner of a 12-person bakery"). Follow `workflows/setup.md` through Stage 4 for the Company section and one domain section, using `setup-interview.md` exactly as written.
4. **One cycle.** Follow `workflows/routine.md` to send questions and file 2 fictional answers, then `workflows/production.md` to write one ticket for the first specialist, then the QA check (R6) on a two-line fictional draft, then compile DELIVERY.md.
5. **Log.** For every step where an instruction was missing, ambiguous, or contradicted another file, write one line: file, section, the problem, the fix.

Keep the dry run to about 30 minutes. A helper agent can do it: give it the kit folder, the five steps above, and "report problems only, do not edit files".

---

## Step 5 · Fix and recheck

1. Fix every logged problem in the owner file first (Step 4 table in 04-build.md), then in the files that copy it.
2. Run `python scripts/check_kit.py --write-manifest`, then `python scripts/check_kit.py`.
3. Repeat Steps 1-3 until they are clean.

---

## Checklist

- [ ] Checker: 0 errors, 0 warnings.
- [ ] Consistency review: every row of the source-of-truth table matches; the five reading checks pass.
- [ ] Residue scan reviewed; gap scan returns nothing.
- [ ] Dry run done for both installs, setup, and one cycle; every problem fixed.
- [ ] Final checker run clean after the fixes.
