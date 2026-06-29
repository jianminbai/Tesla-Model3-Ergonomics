# V0.7 内容更新说明

本次更新目标：建立“可视化插图与图表体系”，让项目从文字指南升级为图文结合的工程化手册。

## 更新内容

### 1. 新增第十章：可视化插图与图表体系

文件：

```text
book/10-可视化插图与图表体系.md
```

核心内容：

- 为什么本项目必须使用 SVG 图
- 插图类型：受力图、姿态图、结构图、流程图、趋势图
- 统一颜色规范
- 图文引用规范
- 如何避免医学化误导
- 后续插图迭代流程

### 2. 新增视觉风格指南

文件：

```text
docs/visual_style_guide.md
```

包含：

- 颜色规范
- 线条规范
- 标签规范
- 中文字体建议
- 风险标注原则
- SVG 文件命名规则

### 3. 新增插图索引

文件：

```text
docs/diagram_index.md
```

列出当前已有 SVG 插图、适用章节和 Markdown 引用方式。

### 4. 新增 8 张 SVG 插图

目录：

```text
assets/diagrams/svg/
```

包含：

```text
01_pressure_distribution.svg
02_pelvis_postures.svg
03_model3_seat_top_view.svg
04_seat_height_force_change.svg
05_pedal_dynamic_load_chain.svg
06_symptom_decision_overview.svg
07_experiment_system_flow.svg
08_rehab_office_triangle.svg
```

### 5. 新增 SVG 检查脚本

文件：

```text
scripts/check_diagrams.py
```

功能：

- 检查 SVG 是否存在
- 检查文件命名
- 生成简单索引摘要

## 应用方式

将压缩包放到仓库根目录后执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.7-update.zip -DestinationPath . -Force

git status
git add book/10-可视化插图与图表体系.md `
        docs/visual_style_guide.md `
        docs/diagram_index.md `
        assets/diagrams/svg/01_pressure_distribution.svg `
        assets/diagrams/svg/02_pelvis_postures.svg `
        assets/diagrams/svg/03_model3_seat_top_view.svg `
        assets/diagrams/svg/04_seat_height_force_change.svg `
        assets/diagrams/svg/05_pedal_dynamic_load_chain.svg `
        assets/diagrams/svg/06_symptom_decision_overview.svg `
        assets/diagrams/svg/07_experiment_system_flow.svg `
        assets/diagrams/svg/08_rehab_office_triangle.svg `
        scripts/check_diagrams.py `
        UPDATE_NOTES_V0.7.md

git commit -m "docs: add visual diagram system and SVG illustrations"
git push
```

## 可选：更新 mkdocs.yml

在 `正文` 部分追加：

```yaml
      - 第十章 可视化插图与图表体系: book/10-可视化插图与图表体系.md
```

在导航中增加：

```yaml
  - 图表:
      - 插图索引: docs/diagram_index.md
      - 视觉风格指南: docs/visual_style_guide.md
```
