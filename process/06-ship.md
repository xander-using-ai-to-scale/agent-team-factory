# Stage 6 · Ship

Package the kit, publish the repo, verify it, and hand the requester everything they need to install it.

- **Input:** the checked kit from stage 5.
- **Output:** a GitHub repo, the zip in `dist/`, and the handoff message.
- **Gate:** the requester has the repo link, the zip link, and both start prompts with the link filled in.
- **Time:** 5-10 minutes.

---

## Step 1 · Package

From the team folder:

```
python scripts/check_kit.py
python scripts/build_zip.py
```

1. The checker must print 0 errors and 0 warnings.
2. The zip lands in `dist/<team_slug>-kit-v<kit_version>.zip`. Its top-level folder is `kit/`.

---

## Step 2 · Commit

1. `git init -b main` in the team folder (skip if it is already a repo).
2. For a public repo, set the commit email to the requester's GitHub no-reply address so their personal email stays private: `git config user.email "<id>+<login>@users.noreply.github.com"`. Get `<id>` and `<login>` from `https://api.github.com/users/<login>` (public, no login needed).
3. `git add -A` and commit with a message like `<Team name> kit v<kit_version>`.

---

## Step 3 · Ask two things (one message)

```
Stage 6/6 · Ship · 2 quick questions

1. Repo name?
   A. <team_slug> (recommended)
   B. Something else
2. Visibility?
   A. Public: any Grokbot or Hermes can install from the link (recommended for kits meant to be installed by link)
   B. Private: only people you invite; bots need the zip attached instead
```

---

## Step 4 · Publish

1. If the GitHub CLI is logged in (`gh auth status`), run:
   ```
   gh repo create <owner>/<name> --public --source . --remote origin --push --description "<Team name> kit v<kit_version>: <purpose>"
   ```
   (use `--private` if chosen).
2. If it is not logged in, never ask for or handle a token. The requester logs in themselves (`gh auth login --web`), or runs the create-and-push command in their own terminal with their own token. Give them the exact one-line command, then watch for the push (for a public repo: `git ls-remote https://github.com/<owner>/<name> refs/heads/main` until it returns your commit).

---

## Step 5 · Verify on GitHub

1. The repo exists with the chosen visibility (`https://api.github.com/repos/<owner>/<name>`, or `gh repo view`).
2. The file count on `main` equals your local count (`git ls-files | wc -l`).
3. The zip is on GitHub: `https://github.com/<owner>/<name>/raw/main/dist/<zip name>`.

---

## Step 6 · User guide as a Google Doc (optional)

If the requester wants the user guide as a Google Doc and a Google Drive connector is available, create a Google Doc from `docs/USER-GUIDE.md` (markdown converts to headings, lists, and tables). Read it back once to confirm the tables converted. It stays private in their Drive: the requester shares it.

---

## Step 7 · Hand off

Send one message with:

1. The repo link and the zip link.
2. The Grokbot start message (from `BOOTSTRAP-PROMPT.md`) with `[PASTE REPO LINK HERE]` replaced by the real link, in a code block.
3. The Hermes start message (from `BOOTSTRAP-PROMPT-HERMES.md`), filled in the same way, in a code block.
4. The user guide link (or the file path).
5. "Material for setup drops" from the Team Brief, if any: what the client can drop in during setup.
6. What was not done, stated plainly (for example "not yet installed on a live Grokbot").

Start it with the state line `Stage 6/6 · Shipped`.

---

## Checklist

- [ ] Checker clean; zip built.
- [ ] Commit made with a private-safe email for public repos.
- [ ] Repo name and visibility confirmed by the requester.
- [ ] Repo published and verified: visibility, file count, zip link.
- [ ] Handoff sent with both filled-in start messages.
