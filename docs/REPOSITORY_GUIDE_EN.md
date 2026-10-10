# Thesis Writing Repository Guide

[简体中文](REPOSITORY_GUIDE_ZH.md) · [Home](../README_EN.md)

This repository is a **collection of independent Codex Skills**, not a single Skill. Future additions may cover literature review, academic drafting, experimental analysis, revisions and peer-review responses.

Each Skill resides in `skills/<kebab-case-name>/` and its directory name must equal the `name:` entry in its `SKILL.md`. The repository root holds bilingual navigation and shared policies. Put task-specific instructions in the Skill's `SKILL.md`, supporting knowledge in `references/`, templates in `assets/`, and optional scripts in `scripts/`.

Maintain paired Chinese `README.md` and English `README_EN.md` with capabilities, limitations, installation steps and examples. Update both root indexes after adding a Skill.

To use the Skill, copy its own directory (not the entire collection) into `%USERPROFILE%\.agents\skills\<skill-name>\`, verify the direct child `SKILL.md`, and invoke `$<skill-name>` in Codex.

Before publishing, inspect the YAML header, reference paths, Markdown links, scripts/tests and confidentiality. Do not publish private manuscripts, unpublished experiments, reviewer identities, tokens or keys. The repository currently has no chosen open-source license; respect upstream attribution and licensing before importing third-party code.
