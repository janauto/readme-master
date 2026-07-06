# docs/assets — visuals as code

Every image in the main README is generated, not hand-placed, so it can be
rebuilt after the project changes. This is the same "screenshots as code"
discipline `readme-master` enforces on the projects it documents.

| File | Role |
|---|---|
| `readme-before-after.png` | Hero: the same repo's README before and after the skill runs |
| `before-after.html` | Source layout the hero is rendered from |
| `crop-pg-default.png`, `crop-pg-random.png` | Real UI screenshots shown in the "after" panel |
| `capture.py` | Renders `before-after.html` with Playwright → `readme-before-after.png` |

## Regenerate

```bash
pip install playwright pillow && playwright install chromium
python docs/assets/capture.py
```

The two `crop-pg-*.png` panels are the actual browser screenshots produced by
the **palette-gen** benchmark case (see [`evals/`](../../evals/evals.json)) —
a real 2-line README rewritten by the skill — not mockups. The `# → 2` smoke
test shown in the hero is that project's own verification command.
