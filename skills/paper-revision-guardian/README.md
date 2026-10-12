# Paper Revision Guardian — 英文学术论文返稿 Skill

[English](README_EN.md) | 简体中文 · [返回技能集合](../../README.md)

**目标**：在不改变作者原本风格和未经证实的技术含义的前提下，对英文科研论文实施最小必要修改，消除无效的防御性写作，检查论证、图表、数学、算法、LaTeX 和审稿人要求。

主要用于机器人、具身智能、计算机科学、机器学习等领域，默认面向 *Advanced Robotics*；实际期刊要求始终优先。

## 核心原则

- 原作者文风优先，不将正常英文全部重写成模板化 AI 句式；能不改则不改。
- **贡献主线与研究叙事审校**：在保留作者用词、句式和论证方式的前提下，检查问题与缺口、核心贡献、机制解释、结果和讨论、摘要及结论是否一致；减少开发日志式叙述、空泛创新宣传和重复防御。仅进行用户授权的文字修改，不擅自要求补实验或改动数据。详见[中文写作规范](docs/WRITING_POLICY_ZH.md)。
- 删除纯粹预防想象中质疑的冗余解释，不掩盖重要的负面结果与真实局限。
- 一般叙事中不必要的 Stage 1 / Stage 2、(1)/(2) 合并成自然段落，但保留算法、数学推导和可复现实验必需的步骤。
- 图注、表注必须与图表实际内容一致，正文聚焦有证据的关键发现。
- 不擅自改动公式或实验数据；未验证的技术错误单独报告。
- 保留现有的 LaTeX 公式、标签、引用、命令与期刊格式。
- 支持论文视觉材料审校，包括算法流程图、系统架构图、实验结果图及统计分析图。检查图片与原论文配色、布局、字体及视觉风格的一致性，核验图中数值与实验数据、统计结果和正文结论的对应关系，并检查最终投稿图片是否存在水印或无关标记。对于无法核验的数据明确说明，不擅自修改原始实验结果。

## 安装

本 Skill 位于集合仓库 `hlf885/thesis-writing` 的 `skills/paper-revision-guardian/`。

```powershell
git clone https://github.com/hlf885/thesis-writing.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\thesis-writing\skills\paper-revision-guardian" "$HOME\.agents\skills\paper-revision-guardian"
```

在 Codex 中调用：

```text
$paper-revision-guardian
目标期刊：Advanced Robotics。
阅读全文以建立英语文风基线，但仅修改指定章节。
检查防御性写作、机械分点、正文与图表的一致性和技术风险。
不要修改未经核实的实验数据或数学公式。交付修订副本及中文修改记录。
```

## 组成

`SKILL.md` 为执行入口，`references/` 提供风格、图表、数学、期刊和审稿专项规则，`assets/` 提供返稿报告模板，`agents/openai.yaml` 提供 UI 调用配置。

当前自动检查以可检查的内容为限，**不能保证**识别所有数学错误、保证图像最佳位置、完全消除 AI 痕迹或获得录用。

## 文档

[中文安装说明](docs/INSTALLATION_ZH.md) · [English installation](docs/INSTALLATION_EN.md)

[完整中文论文返修写作规范](docs/WRITING_POLICY_ZH.md) · [英文执行规则](references/manuscript-writing-and-revision.md)

[中文工作流程](docs/WORKFLOW_ZH.md) · [English workflow](docs/WORKFLOW_EN.md) · [中文使用示例](docs/EXAMPLES_ZH.md) · [English examples](docs/EXAMPLES_EN.md)

参考启发：[anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)、[awesome-ai-research-writing](https://github.com/hlf885/awesome-ai-research-writing)。本 Skill 是独立整理版本，不代表原项目。
