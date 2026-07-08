---
name: readme-master
description: Transform any project's README.md into a polished, front-page-quality document — badges, centered navigation, real screenshots/GIF demos or generated diagrams, tiered quick-start, and a machine-executable install section verified by a fresh agent deploying from the README alone. Use this skill whenever the user wants to improve, beautify, rewrite, restructure, or professionalize a README or repository landing page; add screenshots, demos, badges, or architecture diagrams to project docs; prepare a repo for open-source release; or make installation reproducible for AI agents — even when they don't say "README" explicitly (e.g. "my repo looks bare", "make my project look professional on GitHub", "帮我美化项目主页", "补全项目说明文档").
---

# readme-master

Turn any repository's README into the kind of front page that makes people star the project — and makes an AI agent able to deploy it with zero human intervention.

## What this skill produces

1. A rewritten `README.md` (language follows the original project; bilingual `README_CN.md`/`README.md` pair only if the user asks).
2. Visual assets in `docs/assets/` — real screenshots/GIFs when the project can run (optionally composited into one branded hero banner around the real screenshot — see `references/visual-capture.md`), generated diagrams when it can't.
3. Capture scripts committed alongside the assets ("screenshots as code") so visuals can be regenerated after the project changes.
4. A deploy-verification report: proof that a fresh agent, given only the README, completed installation.

Scope is the README and its assets. Do not create a full docs suite; link to files that already exist, and flag (don't fabricate) links to docs that don't.

## Core principles

- **Never invent facts.** No fake badges, fabricated star counts, imaginary features, sponsors, or links to nonexistent docs. Every claim in the new README must be traceable to the actual codebase or the original README. A beautiful lie is worse than a plain truth — maintainers lose trust in the whole document the moment they spot one invented detail. This applies to generated visuals too: a composited hero banner may only frame a **real** captured screenshot, never an invented or mocked-up UI.
- **Never lose facts.** The original README's substantive content (decisions, caveats, evidence, tables) must survive the rewrite, possibly restructured. Beautification that deletes information is vandalism.
- **Degrade, don't block.** Every capture tool can be missing; every project can fail to run. Each failure lowers the visual ceiling, never halts the workflow. The decision tree in `references/visual-capture.md` defines the fallback at each step.
- **The README is an API for agents.** Installation sections are consumed by AI agents as much as humans now. Commands must be copy-paste executable with no placeholders lacking defaults, and the section must end with a verifiable smoke test.

## Chinese output quality (中文写作规范)

When the project's README is in Chinese, or the user requests Chinese output, the generated text **must read naturally to a native Chinese speaker**. The single most common failure mode is 翻译腔 (translationese) — Chinese text that follows English syntax patterns.

### Sentence structure

- **Prefer short sentences.** Chinese readers expect frequent sentence breaks. Break English-style compound sentences (connected by dashes, semicolons, or relative clauses) into 2–3 shorter Chinese sentences.
- **Lead with the topic.** Chinese uses topic-comment structure: "这一步的意义在于……" not "The significance of this step is…" mapped word-for-word.
- **Use natural Chinese connectors**: 因此、所以、不过、此外、首先…然后…最后, rather than overusing dashes and semicolons for logical flow.

### Word choice — common traps

| English term | Bad (翻译腔) | Good (自然中文) |
|---|---|---|
| graceful degradation | 优雅降级 | 自动降级 / 兜底 |
| capture (screenshots) | 捕获 | 截图 / 截取 |
| recipe (build scripts) | 配方 | 脚本 / 配置文件 |
| anatomy (structure) | 解剖 | 结构 / 模板 |
| adversarial verification | 对抗式验证 | 交叉验证 / 自动化验证 |
| pass condition | 通过条件 | 验收条件 / 通过标准 |
| a/one X skill | 一个 X 技能 | 一款 X 技能 |
| tiered fallback | 分级降级 | 多级兜底方案 |

Keep English for terms with no natural Chinese equivalent: API, Git, CI/CD, badge, agent, token. Use Chinese for words that have well-known equivalents: 截图 not capture, 脚本 not recipe, 结构 not anatomy.

### Register consistency

Do not mix overly casual (口语) phrasing like 就上、瞎试、搞定 with formal academic terms like 显式要求、不具区分度 in the same paragraph. Pick one register and hold it. For README text, aim for **清晰的技术书面语** — professional but not stiff.

### Punctuation

Use Chinese punctuation throughout Chinese text: ，。！？；：""''（）——. Do not mix English commas/periods into Chinese sentences.

### Quantifiers (量词)

Use appropriate 量词: 一款技能、一份文档、一套方案、一张截图、一条命令. Never use 一个 as a universal quantifier.

## Workflow

Work through five phases in order. Read the referenced file at the start of the phase that needs it — not before.

### Phase 0 — Environment detection

Run `scripts/detect_env.sh` (or check manually on non-bash systems) to learn which capture tools exist: `playwright`, `shot-scraper`, `vhs`, `asciinema`+`agg`, `ffmpeg`, `mmdc`, `docker`. Also detect the host environment:

- **Claude Code / CLI agent**: prefer shot-scraper/Playwright for web capture, vhs for terminal recording.
- **Cowork / desktop app**: a Chrome extension may be available for opening and screenshotting live pages; Bash sandbox still supports the Python/CLI tools.

If a tool that would raise the visual ceiling is missing (e.g. vhs for a CLI project), offer the user a one-line install command once, then proceed with the fallback regardless of their answer. Don't stall.

### Phase 1 — Project analysis

Read the project (local folder, or clone the GitHub URL). Produce a short internal analysis before writing anything:

1. **Project type**: web app / CLI tool / library / config-or-docs package / mixed. Detection heuristics are in `references/visual-capture.md`.
2. **Runnable entry points**: `package.json` scripts, `docker-compose.yml`, `main.py`, `Makefile`, demo pages, published URLs mentioned in existing docs.
3. **Existing README gap list**: what's missing versus the anatomy in `references/readme-anatomy.md` (badges? visuals? quick start? doc index? agent-executable install?).
4. **Facts inventory**: license, language, version, install steps, dependencies, existing docs/ files that can be linked.

Share a 5-10 line summary of the gap list with the user, then continue (don't wait for approval unless they respond).

### Phase 2 — Visual assets

Read `references/visual-capture.md` and follow its decision tree:

- Web UI → try to run the project and capture real screenshots (and a short GIF if tooling allows).
- CLI → scripted terminal recording (vhs `.tape`) or static styled output.
- Library/config/docs → Mermaid architecture/flow diagrams (GitHub renders these natively — zero dependencies) plus well-chosen code examples.

Rules that apply to all branches:

- Auto-attempt running the project; on any failure (missing deps, required credentials, port conflicts) fall back one tier and move on. Never ask the user to debug the project for you — the skill's job is the README.
- Save all assets to `docs/assets/` with relative paths and meaningful alt text.
- Commit the capture scripts (`.tape` files, `shots.yml`, capture commands in a small `docs/assets/README.md`) next to the images so anyone can regenerate them later.

### Phase 3 — README construction

Read `references/readme-anatomy.md` and rebuild the README section by section. That file defines the full anatomy (badges → value proposition → nav → visual showcase → comparison table → quick start → doc index → footer), with copy-paste snippets and anti-patterns.

Match the original project's language and voice. A research-notes repo should not suddenly sound like a SaaS landing page — elevate structure and scannability, keep the author's register.

### Phase 4 — Agent-deploy verification

Read `references/agent-deploy-spec.md`. Two steps:

1. **Write the install section to spec**: prerequisites table with versions, per-platform collapsibles, every command copy-pasteable, ending with a smoke test command and its expected output.
2. **Verify with a fresh agent**: spawn a subagent whose only input is the new README text (no repo context, clean working directory). Instruct it to follow the README to a working install and report every point where it had to guess, improvise, or would have asked a human. Fix the README for each reported gap and re-run. Stop after 3 loops or on full pass; if issues remain, list them for the user honestly.

If no subagent capability exists in the current environment, perform the verification yourself in a clean temp directory, deliberately ignoring everything you know about the project that isn't written in the README.

### Phase 5 — Delivery

1. Show the user a summary of changes (not the full file): section-level before/after, list of new assets, verification result.
2. On confirmation, write `README.md` (back up the original to `README.old.md` if not in git) and the `docs/assets/` files.
3. Offer optional follow-ups: bilingual version, CI job that regenerates screenshots, README_CN sync.

## When things go wrong

- Project won't run at all → the README can still be excellent: generated diagrams + code examples + honest install docs. Say so and proceed.
- Repo is private/unpublished → omit stars/star-history badges; use only badges that render (license, language, version from manifest).
- Original README is empty → Phase 1 must dig deeper into the code; state inferred claims conservatively ("appears to", or verify by running).
- User's project is itself a skill/plugin/config package → the "install" being verified is the package's own install instructions; the smoke test is whatever the package defines as working (e.g. an agent following the config successfully).
