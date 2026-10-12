# Paper Revision Guardian — Academic Manuscript Revision Skill

**English** | [简体中文](README.md) · [Skills index](../../README_EN.md)

A Codex Skill for **minimal, evidence-grounded revision of English scientific papers** while preserving the author's established voice. It targets academic manuscripts in robotics, embodied AI, computer science and machine learning; *Advanced Robotics* is the default journal context, not a mandatory formatting standard for other journals.

## What it does

- Preserves natural original prose and revises only when accuracy, clarity or logic materially improves.
- **Contribution-led manuscript writing audit:** Preserves the author's voice
  while checking the research narrative, mechanism explanations, novelty
  statements, results-versus-discussion writing, abstract and conclusion,
  concise limitations, captions, and reviewer responses. Applies only to
  authorized text editing, without initiating research operations. See the
  [full writing policy](references/manuscript-writing-and-revision.md).
- Removes gratuitous defensive phrasing while retaining genuine limitations, adverse results and review-mandated disclosures.
- Converts narrative Stage 1/2 and First/Second/Third lists to coherent paragraphs when enumeration serves no technical purpose.
- Compares figure/table captions and textual claims to available visual and numerical evidence.
- Flags symbol, dimension, algorithm, complexity and proof issues; freezes unverified mathematical expressions.
- Preserves LaTeX labels, references, citations, formatting and journal-specific constraints.
- Reports verified edits and remaining technical uncertainty separately in Chinese.
- Audits scientific figures, including algorithm workflows,
  system architectures, experimental comparisons, and statistical
  plots. Checks consistency with the manuscript's existing visual
  style, including color palettes, typography, spacing, and layout.
  Verifies plotted values against available source data, analysis
  results, and textual claims. Enforces watermark-free publication
  figures while preserving required attribution and reporting
  unverifiable results explicitly.

## Install (Windows Codex)

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

Invoke in Codex:

```text
$paper-revision-guardian
Read my manuscript to establish an author-voice baseline, but edit only the section I specify.
Check related visuals, tables, algorithms and equations against available evidence.
Do not invent corrections or alter unverified data. Deliver a revision diff and Chinese audit report.
```

## Internals and limits

`SKILL.md` is the entry point; `references/` contains on-demand standards for prose, figures, mathematical methods, journal formatting and reviewer responses; `assets/` contains the audit template and `agents/openai.yaml` defines the invocation display.

The Skill does not guarantee scientific correctness, ideal float placement, elimination of AI markers or acceptance. Unavailable data and figures must be identified as unverified.

[English installation guide](docs/INSTALLATION_EN.md) · [中文安装说明](docs/INSTALLATION_ZH.md)

[Full Writing and Revision Policy](references/manuscript-writing-and-revision.md) · [Chinese Policy Guide](docs/WRITING_POLICY_ZH.md)

[English workflow](docs/WORKFLOW_EN.md) · [中文工作流程](docs/WORKFLOW_ZH.md) · [Usage examples](docs/EXAMPLES_EN.md) · [中文示例](docs/EXAMPLES_ZH.md)

Inspired by [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) and [awesome-ai-research-writing](https://github.com/hlf885/awesome-ai-research-writing). This is an independently organized skill, not an official fork or mirror.
