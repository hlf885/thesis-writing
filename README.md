# Thesis Writing Skills｜学术论文写作 Skill 集合

[English](README_EN.md) | **简体中文**

面向 Codex 的学术论文写作、审校与返修 Skill 集合。采用 **一个 Skill 一个目录** 的布局，以便后续新增文献综述、论文起草、方法写作、返稿、审稿回复等独立 Skill。

> 原文风格优先、科研事实与证据优先、最小必要修改；技术错误必须核查，不能为了“去 AI 味”而隐藏真实研究限制。

## 已发布 Skill

| Skill | 主要用途 | 中文说明 | English |
| --- | --- | --- | --- |
| **paper-revision-guardian**（英文论文返稿） | 语言与论证审校；反防御性写作；保留原作者风格；核查图表、公式、伪代码与审稿回复 | [中文介绍](skills/paper-revision-guardian/README.md) | [English overview](skills/paper-revision-guardian/README_EN.md) |

这里只列出已经实现的 Skill。新增 Skill 应以独立子目录发布，并更新本索引。

## 安装（Windows Codex）

从本仓库下载或克隆代码，**只复制需要的 Skill 目录**，不要把整个 `thesis-writing` 根目录当作单个 Skill 安装。

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

确保文件存在：`%USERPROFILE%\.agents\skills\paper-revision-guardian\SKILL.md`。重新打开 Codex 后使用：

```text
$paper-revision-guardian
请审校指定英文论文的返稿，保持原文风格，采用最小必要修改，并核验重要技术结论。
```

[中文安装与维护说明](skills/paper-revision-guardian/docs/INSTALLATION_ZH.md) · [English installation guide](skills/paper-revision-guardian/docs/INSTALLATION_EN.md)

## 仓库结构

```text
thesis-writing/
├── README.md                      # 中文仓库索引
├── README_EN.md                   # English repository index
├── docs/                          # 整体布局、命名与维护规则
├── skills/
│   └── paper-revision-guardian/
│       ├── SKILL.md
│       ├── README.md
│       ├── README_EN.md
│       ├── agents/
│       ├── references/
│       ├── scripts/
│       ├── assets/
│       ├── docs/
│       └── tests/
└── .github/workflows/             # 校验
```

## 新增 Skill 的约定

- 每个 Skill 放在 `skills/<kebab-case-name>/`。
- 文件夹名与 `SKILL.md` 中 `name:` 完全一致。
- 每个 Skill 应有中文 `README.md` 和英文 `README_EN.md`，且相互跳转。
- 任务特定参考材料、模板和脚本只放在对应 Skill 内。
- 根目录只保存集合导航、全局说明、CI 等公共内容。
- 重要变更应记录在该 Skill 自己的更新日志。

[仓库管理指南（中文）](docs/REPOSITORY_GUIDE_ZH.md) · [English guide](docs/REPOSITORY_GUIDE_EN.md)

## 研究诚信、许可与隐私

不得公开未发表论文、敏感审稿意见、个人身份信息、实验原始数据或 API 密钥。本仓库尚未选定统一开源许可证；见[许可与归属说明](skills/paper-revision-guardian/docs/LICENSING_ZH.md)。
