# V0.4 内容更新说明

本次更新目标：把前面章节中的受力分析，整理成可执行的“症状决策树”。

## 更新内容

### 1. 新增第七章：症状决策树

文件：

```text
book/07-症状决策树.md
```

包含以下决策树：

- 坐骨单点压痛
- 坐骨两侧软组织挤压
- 大腿后侧紧硬
- 大腿后侧麻刺 / 过电感
- 大腿根压力
- 右腿踩油门疲劳
- 腰被顶 / 腰托不适
- 办公椅也有类似感觉
- 调整后如何判断保留还是回退

### 2. 新增快速排查表

文件：

```text
docs/quick_diagnosis_table.md
```

用于快速从“症状”映射到：

- 可能机制
- 优先检查
- 优先调整
- 回退信号

### 3. 新增实验记录模板：症状决策树验证

文件：

```text
experiments/symptom_decision_log_template.md
```

用于记录每次症状判断和调整结果，避免凭单次感觉频繁改座椅。

### 4. 新增 V0.4 插图计划

文件：

```text
assets/diagrams/v0.4_decision_tree_diagram_plan.md
```

规划后续决策树插图：

- 坐骨疼流程图
- 大腿后侧紧硬流程图
- 右腿疲劳流程图
- 坐骨两侧软组织挤压流程图
- 调整保留 / 回退判断图

## 应用方式

将压缩包放到仓库根目录后执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.4-update.zip -DestinationPath . -Force

git status
git add book/07-症状决策树.md `
        docs/quick_diagnosis_table.md `
        experiments/symptom_decision_log_template.md `
        assets/diagrams/v0.4_decision_tree_diagram_plan.md `
        UPDATE_NOTES_V0.4.md

git commit -m "docs: add symptom decision trees and diagnosis tables"
git push
```

## 可选：更新 mkdocs.yml

在 `mkdocs.yml` 的 `正文` 部分追加：

```yaml
      - 第七章 症状决策树: book/07-症状决策树.md
```

在导航中增加快速排查：

```yaml
  - 快速排查:
      - 症状快速排查表: docs/quick_diagnosis_table.md
```
