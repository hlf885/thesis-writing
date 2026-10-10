# Installation and usage

[简体中文](INSTALLATION_ZH.md) · [Skill home](../README_EN.md)

This Skill belongs to the multi-skill repository `https://github.com/hlf885/thesis-writing` and resides in `skills/paper-revision-guardian/`. Do not install the entire repository as a single skill.

Windows PowerShell:

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

Verify `%USERPROFILE%\.agents\skills\paper-revision-guardian\SKILL.md`, restart/new-session Codex if needed, then invoke `$paper-revision-guardian`. Back up custom changes before updates. No extra model API key is required beyond an operational Codex environment. Never commit private manuscripts, reviewer identities or credentials to a public repository.
