# 安装与使用

[English](INSTALLATION_EN.md) · [Skill 首页](../README.md)

此 Skill 位于多技能仓库 `https://github.com/hlf885/thesis-writing` 的 `skills/paper-revision-guardian/`，不能将整个仓库当作单个 Skill 克隆到安装路径。

Windows PowerShell：

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

检查 `%USERPROFILE%\.agents\skills\paper-revision-guardian\SKILL.md` 是否存在；新开 Codex 会话并输入 `$paper-revision-guardian`。若已安装，先备份自定义规则，再更新文件。无需额外付费模型 API，但 Codex 自身需要可用的模型配额。不要上传保密稿件、审稿人身份或 API 密钥到公开仓库。
