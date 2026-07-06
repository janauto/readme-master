# README Anatomy — section order, snippets, and anti-patterns

Modeled on top-tier open-source READMEs (the reference exemplar is hugohe3/ppt-master). Sections in order; skip any section the project has no honest content for — an absent section is fine, a hollow one is not.

## 1. Title + one-line value proposition

```markdown
# ProjectName — what it does for whom, in one clause
```

The clause after the em-dash is the most-read sentence in the repo. It must state the *outcome* ("AI generates natively editable PPTX from any document"), not the implementation ("a Python tool using SVG").

## 2. Badge row

Only badges that render truthfully:

```markdown
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](../../releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/OWNER/REPO.svg)](../../stargazers)
```

Version from the manifest/tags; license from the LICENSE file; stars only for public repos; CI badge only if a workflow exists. A badge that 404s or shows "not found" damages credibility more than no badge.

## 3. Language switcher (only if a translation exists or is being created)

```markdown
English | [中文](./README_CN.md)
```

## 4. Centered navigation

```markdown
<p align="center">
  <a href="LIVE_DEMO_URL"><strong>Live Demo</strong></a> ·
  <a href="./docs/"><strong>Docs</strong></a> ·
  <a href="./examples/"><strong>Examples</strong></a> ·
  <a href="../../issues"><strong>Issues</strong></a>
</p>
```

Link only to destinations that exist. 3-6 items.

## 5. Visual showcase

The first scroll must show, not tell. Options by asset availability:

- **Single hero**: one centered image/GIF right after the nav.
- **Gallery table** (multiple screenshots): HTML table, 2-3 columns, each cell = linked image + one-line caption in `<sub>`:

```markdown
<table>
  <tr>
    <td align="center" width="50%">
      <img src="docs/assets/shot-dashboard.png" alt="Dashboard view" /><br/>
      <sub><b>Dashboard</b> — real-time metrics at a glance</sub>
    </td>
    <td align="center" width="50%">
      <img src="docs/assets/shot-editor.png" alt="Editor view" /><br/>
      <sub><b>Editor</b> — click any element to edit</sub>
    </td>
  </tr>
</table>
```

- **Mermaid diagram** (no-UI projects): the architecture/flow diagram *is* the hero. Put it here, not buried at the bottom.

## 6. What-it-is + differentiation

One short paragraph of what the project does, then — when the project genuinely competes in a category — a comparison table:

```markdown
| Approach | Output | Editable? |
|---|---|:---:|
| Alternative A | ... | ❌ |
| **This project** | ... | ✅ |
```

Comparison rows must be defensible statements about categories, not attacks on named competitors. If the original README contains a decision-record or evidence table (common in research/config repos), this is where it lives — keep it intact, it *is* the differentiation.

## 7. Quick Start

Numbered steps, heaviest information collapsed:

```markdown
## Quick Start

### 1. Prerequisites
| Dependency | Required? | Purpose |
|---|:---:|---|
| Python 3.10+ | ✅ | Core runtime |

<details>
<summary><strong>Windows</strong> — step-by-step</summary>
...platform-specific commands...
</details>

<details>
<summary><strong>macOS / Linux</strong></summary>
...
</details>

### 2. Install
### 3. First run
```

The install commands themselves must follow `agent-deploy-spec.md` — that spec governs this section's content; this file only governs its shape.

## 8. Documentation index (if the repo has ≥3 doc files)

```markdown
| | Document | Description |
|---|---|---|
| 📖 | [Guide](./docs/guide.md) | Core workflow |
| ❓ | [FAQ](./docs/faq.md) | Common issues |
```

## 9. Footer block

In order, each only if applicable: Contributing → License → Acknowledgments → Contact → Star History:

```markdown
## Star History
<a href="https://star-history.com/#OWNER/REPO&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=OWNER/REPO&type=Date&theme=dark" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=OWNER/REPO&type=Date" />
 </picture>
</a>

[⬆ Back to Top](#anchor-of-h1)
```

## Style rules

- **Front-load value**: a visitor decides in ~10 seconds. Title → badges → visual → "what's in it for me" must all fit in the first screen.
- **Scannable**: bold lead-ins on bullets, tables over prose for structured facts, `<details>` for anything long.
- **Preserve the author's voice and language.** Restructure, don't rewrite personality away. A Chinese README stays Chinese unless the user asks for bilingual.
- **Every link resolves.** Check each relative link against the actual file tree before delivering.
- **Blank line before every list and after every header** (CommonMark — GitHub renders wrong without it).

## Anti-patterns

- Fake or 404 badges; star-history on a repo with 3 stars (it reads as aspiration, not proof — skip until ~50+).
- Marketing adjectives with no evidence ("blazingly fast" with no benchmark).
- Deleting the original README's tables/caveats/evidence because they're "ugly".
- A gallery of empty-state screenshots.
- Doc-index links to files that don't exist ("coming soon" tables).
- Centered `<p>` blocks overused — one nav bar, maybe one hero caption; not every paragraph.
