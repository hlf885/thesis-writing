# 使用示例

[English](EXAMPLES_EN.md) · [Skill 首页](../README.md)

## 单段英文最小润色

```text
$paper-revision-guardian
对以下英文段落进行最小必要润色。判断是否存在防御性写作、逻辑重复、机械连接词和非母语表达；无问题则保留原句。
输出 Part 1 修订英文、Part 2 中文直译、Part 3 中文修改记录。
```

## 4.8 节与图表同步审校

```text
$paper-revision-guardian
目标期刊为 Advanced Robotics。
阅读全文建立写作风格基线，但仅处理第 4.8 节、Figure 8–11 和 Table 2 及对应图注表注。
核查可见图表、正文引用数值、实验条件、公式和算法。
对未经证实的技术问题仅记录，不更改原始数据。
保留原稿，交付 diff、修订版和中文审计报告。
```

## 正式返稿与审稿人意见

```text
$paper-revision-guardian
读取审稿意见、我的回应草稿与论文源文件。
逐条建立 reviewer comment、证据、修改位置和回应的对应关系。
避免不必要的自我辩解，但必须完整回应真实问题。
将未完成的实验和无法验证的内容标记出来。
```
