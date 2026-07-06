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

## Chinese README patterns (中文 README 写法)

When the target language is Chinese, adapt all section patterns to natural Chinese. The full language quality rules are in `SKILL.md` under "Chinese output quality" — this section provides the section-level templates.

### Title

```markdown
# 项目名 — 一句话说清这个项目能帮用户做什么
```

Focus on the **outcome for the user**, not the technical implementation. Example: "AI 自动生成可编辑的 PPTX" beats "基于 SVG 解析的 Python 工具".

### Feature bullets

Use parallel structure with bold lead-ins. Each bullet is a **complete, concise thought** — do not try to pack two ideas into one bullet:

```markdown
- **标准化结构** — 按 badge → 价值主张 → 导航 → 截图 → 快速开始 → 页脚的顺序组织内容
- **多级视觉方案** — 优先截取真实界面，工具缺失时自动降级为 Mermaid 图
- **截图即代码** — 每张截图附带生成脚本，项目变动后可一键重新生成
```

### Quick Start section

```markdown
## 快速开始

### 1. 环境要求

| 依赖 | 是否必需 | 用途 |
|---|:---:|---|
| Python 3.10+ | ✅ | 核心运行时 |

<details>
<summary><strong>Windows</strong> — 详细步骤</summary>
...
</details>

<details>
<summary><strong>macOS / Linux</strong></summary>
...
</details>

### 2. 安装
### 3. 首次运行
```

### Footer

```markdown
## 贡献与许可证

欢迎提 issue 和 PR。本项目采用 [MIT 许可证](./LICENSE)。

[⬆ 回到顶部](#项目名)
```

### Chinese-specific anti-patterns

- **翻译腔 (translationese)**: text that reads like English with Chinese characters. Signs: long compound sentences joined by dashes/semicolons, literal translations like 优雅降级/捕获/配方, excessive passive voice (被……所……).
- **Register mixing (语体混乱)**: swinging between 口语 (就上、瞎试、搞定) and 书面语 (显式、不具区分度) in the same paragraph. Pick a consistent register.
- **Unnecessary English**: use Chinese for words with natural equivalents (截图 not capture, 脚本 not recipe, 结构 not anatomy). Keep English only for standard technical terms (API, Git, CI/CD, badge).
