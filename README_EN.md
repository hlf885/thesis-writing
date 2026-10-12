# Thesis Writing Skills

[简体中文](README.md) | **English**

A growing collection of Codex Skills for academic manuscript drafting, revision, literature research, technical verification and peer-review response. Each Skill lives in its own directory under `skills/`; the repository root only provides navigation and shared documentation.

## Available Skills

| Skill | Purpose | Chinese | English |
| --- | --- | --- | --- |
| **paper-revision-guardian** | Preserve authorial voice; improve contribution-led research narratives, mechanism explanations and reviewer responses; reduce defensive prose; audit figures, equations and algorithms | [中文](skills/paper-revision-guardian/README.md) | [English](skills/paper-revision-guardian/README_EN.md) |

Full writing policy: [English, 14 rules](skills/paper-revision-guardian/references/manuscript-writing-and-revision.md) · [中文说明](skills/paper-revision-guardian/docs/WRITING_POLICY_ZH.md) · [English usage examples](skills/paper-revision-guardian/docs/EXAMPLES_EN.md)

## Installation (Windows Codex)

Clone the repository, then copy **only** the Skill folder into the Codex user-level discovery directory:

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

Verify that `%USERPROFILE%\.agents\skills\paper-revision-guardian\SKILL.md` exists. Start a new Codex session and invoke `$paper-revision-guardian`.

## Layout

```text
thesis-writing/
├── README.md
├── README_EN.md
├── docs/
│   ├── REPOSITORY_GUIDE_ZH.md
│   └── REPOSITORY_GUIDE_EN.md
└── skills/
    └── paper-revision-guardian/
        ├── SKILL.md
        ├── README.md
        ├── README_EN.md
        ├── agents/
        ├── references/
        ├── scripts/
        ├── assets/
        └── docs/
```

New skills use `skills/<kebab-case-name>/` and contain a matching YAML `name` plus bilingual READMEs. No unpublished manuscript or confidential reviewer records should be committed to this public repository.

[Repository guide](docs/REPOSITORY_GUIDE_EN.md) · [中文维护规范](docs/REPOSITORY_GUIDE_ZH.md)

No open-source license has yet been selected. Third-party skills linked for inspiration are not bundled or relicensed here.
