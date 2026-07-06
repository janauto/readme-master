# Agent-Deploy Spec — writing and verifying a machine-executable install section

An install section passes this spec when a fresh agent (or a tired human at midnight) can go from `git clone` to verified-working without asking a single question.

## Part 1: Writing the install section

### Requirements

1. **No placeholder without a default.** `<YOUR_API_KEY>` is acceptable only when accompanied by exactly where to get one and what happens if it's absent. `cd <your-project-dir>` is not acceptable — write the real path produced by the clone command above it.
   - **Unpublished repo (no remote URL yet)?** Don't leave `git clone <this-repo-url>` bare. Either derive the future URL from the git remote / owner info if known, or write the download-ZIP/local-copy alternative as the primary path and add an inline note: `<!-- replace with the real URL after first push -->`. The verification subagent must be told which path to exercise.
2. **Every command block is copy-paste executable in sequence.** Test the sequence, not individual commands. A block that assumes a `cd` from three paragraphs ago fails the spec.
3. **Prerequisites are explicit and versioned.** "Python 3.10+", not "Python". Include the check command: `python3 --version`.
4. **Platform splits are complete.** If Windows needs different steps, write them (or link a dedicated guide) — don't let Windows users infer from macOS commands.
5. **State the success condition.** Every install path ends with a smoke test:

   ```markdown
   Verify the installation:
   ```bash
   mytool --version
   ```
   Expected output: `mytool 1.x.x`. If you see `command not found`, see [Troubleshooting](#troubleshooting).
   ```

6. **Failure modes documented inline or linked.** The 2-3 most likely failures (PATH, permissions, missing system dep) get a one-line fix each.
7. **For skills/plugins/config packages** (projects whose "install" is copying files into another system): specify the exact destination paths for each host variant, and define the smoke test as an observable behavior ("start a task in Plan mode; the orchestrator should announce its decomposition — if it doesn't, the CLAUDE.md merge didn't take").

### Optional but valuable: an agent-targeted block

A short HTML comment or dedicated paragraph agents will read but humans can skim past:

```markdown
<!-- For AI agents: full non-interactive install:
git clone https://github.com/OWNER/REPO && cd REPO && pip install -r requirements.txt && python -m mytool --version
No credentials required. All steps idempotent. -->
```

## Part 2: Verification protocol

The point of verification is adversarial: the verifier must NOT benefit from anything you learned while writing the README.

1. **Spawn a fresh subagent.** Its entire input:
   - The full text of the new README (pasted, not a path into the analyzed repo).
   - A clean temp working directory.
   - This instruction: "Follow this README to a working installation. Do not use any knowledge not in the README. Record every point where you had to guess, improvise, search the web, or would have asked a human. Finish by running the README's own verification/smoke-test step and reporting its output. Also flag: broken links you attempted to use, commands that errored, missing prerequisites the README didn't mention."
2. **Classify the report.**
   - *Blocker*: install failed, or agent had to improvise a command → fix the README, re-run.
   - *Friction*: succeeded but guessed (ambiguous step, undocumented wait, unclear success signal) → fix the README; re-run only if the fix changed commands.
   - *Environmental*: failure caused by the sandbox (no network, no docker), not the README → note it, don't loop on it.
3. **Loop limit: 3.** If blockers remain after 3 rounds, stop and report the residual issues to the user honestly in the delivery summary — a README that documents a rough edge is better than one that hides it.
4. **No subagent available?** Do it yourself in a clean temp dir, following only the README text on screen. This is weaker (you can't unknow the repo) — compensate by being pedantic: execute exactly what's written, never a corrected version of it.

### Pass condition

- Clone/download → install → smoke test all succeeded from README text alone
- Zero improvised commands
- Smoke test output matched what the README says to expect

Record the result (pass, or residual issues) — it goes into the Phase 5 delivery summary.
