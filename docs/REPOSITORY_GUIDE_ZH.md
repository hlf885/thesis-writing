# Thesis Writing 仓库维护规范

[English](REPOSITORY_GUIDE_EN.md) · [首页](../README.md)

这是论文写作类 Codex Skill 的**集合仓库**，不是单个 Skill。每项能力独立管理，未来可添加文献综述、学术英文写作、实验分析、论文返稿和审稿回复等技能。

## 目录与命名

每个 Skill 必须置于 `skills/<kebab-case-name>/`，文件夹名称与 `SKILL.md` 的 `name:` 完全一致。根目录 README 只存放 Skill 索引、使用说明、总览。单个 Skill 的规则放在 `SKILL.md`，细节放在 `references/`，模板放在 `assets/`，可选只读工具放在 `scripts/`。

建议 Skill 配备 `README.md` 中文说明及 `README_EN.md` 英文说明，并为重要功能、限制、适用对象、操作案例写清楚。新增后更新根目录双语索引。

## 安装与使用

不要把仓库根目录作为单个 Skill 安装；把需要的 Skill 子文件夹复制到 Windows `%USERPROFILE%\.agents\skills\<skill-name>\`，确保其根部含 `SKILL.md`。在 Codex 中使用 `$<skill-name>`。

## 质量与安全

提交前检查 YAML 头、参考文件相对路径、双语 Markdown 链接、样例调用；有脚本时执行测试。不要上传未公开稿件、原始实验数据、审稿人身份、凭据和密钥。未经作者验证的科研结论不能写成已核实结论。

本仓库目前未选择统一开源许可证；添加许可证前需要检查第三方内容归属。
