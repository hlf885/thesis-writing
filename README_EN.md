# Thesis Writing Skills | Academic Writing Skill Collection

**English** | [简体中文](README.md)

A scalable collection of Codex Skills for academic writing, manuscript revisions and peer-review workflows. Each skill lives in its own directory under `skills/`, so future literature review, drafting, methods, or rebuttal skills remain independent.

## Available skill

| Skill | Focus | Documentation |
| --- | --- | --- |
| **paper-revision-guardian** | Preserve author voice, minimize unnecessary edits, avoid defensive writing, review figures/tables, mathematics, algorithms, and reviewer responses | [English](skills/paper-revision-guardian/README_EN.md) · [中文](skills/paper-revision-guardian/README.md) |

## Install on Windows Codex

Clone the repository, then copy **only** `skills/paper-revision-guardian` to `$HOME\.agents\skills\paper-revision-guardian`. The folder containing `SKILL.md` is the installable unit, not this repository root.

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

Then invoke `$paper-revision-guardian` in a new Codex session.

## Layout and conventions

Each skill must have a `SKILL.md`, a Chinese `README.md` and an English `README_EN.md`. Its folder name should match the YAML `name:` field. Add new skills at `skills/<descriptive-kebab-case-name>/` and update both root README indexes.

[中文维护规范](docs/REPOSITORY_GUIDE_ZH.md) · [English maintenance guide](docs/REPOSITORY_GUIDE_EN.md)

Do not commit unpublished manuscripts, private reviewer comments or credentials. This repository does not yet declare an open-source license.
