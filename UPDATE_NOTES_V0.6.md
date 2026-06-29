# V0.6 内容更新说明

本次更新目标：建立“实验系统与量化记录”，把驾驶座椅调整从经验描述升级为可记录、可复盘、可画趋势图的工程实验。

## 更新内容

### 1. 新增第九章：实验系统与量化记录

文件：

```text
book/09-实验系统与量化记录.md
```

核心内容：

- 为什么座椅调整需要实验系统
- 如何定义一次有效实验
- 每次只调整一个变量
- 驾驶、办公、身体状态三类数据如何记录
- 0-10 分症状评分规则
- 保留 / 回退 / 继续观察的量化标准
- 当前案例如何建立 14 天实验计划

### 2. 新增实验系统说明

文件：

```text
docs/experiment_system.md
```

用于解释仓库中 CSV 模板和分析脚本的使用方式。

### 3. 新增 CSV 记录模板

目录：

```text
experiments/templates/
```

包含：

```text
driver_daily_log.csv
seat_adjustment_events.csv
office_rehab_daily_log.csv
symptom_score_reference.csv
```

用途：

- `driver_daily_log.csv`：每天驾驶后的症状评分
- `seat_adjustment_events.csv`：每次座椅调整事件
- `office_rehab_daily_log.csv`：办公久坐与康复执行记录
- `symptom_score_reference.csv`：评分含义标准表

### 4. 新增分析脚本

文件：

```text
scripts/analyze_experiments.py
```

功能：

- 读取 CSV
- 生成症状趋势图
- 输出最近 7 天平均分
- 标记调整事件
- 生成 `experiments/output/summary.md`

### 5. 新增 V0.6 插图计划

文件：

```text
assets/diagrams/v0.6_experiment_system_diagram_plan.md
```

规划：

- 单变量实验流程图
- 座椅调整事件时间线
- 症状评分趋势图
- 保留 / 回退判断矩阵
- 14 天实验计划图

## 应用方式

将压缩包放到仓库根目录后执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.6-update.zip -DestinationPath . -Force

git status
git add book/09-实验系统与量化记录.md `
        docs/experiment_system.md `
        experiments/templates/driver_daily_log.csv `
        experiments/templates/seat_adjustment_events.csv `
        experiments/templates/office_rehab_daily_log.csv `
        experiments/templates/symptom_score_reference.csv `
        scripts/analyze_experiments.py `
        assets/diagrams/v0.6_experiment_system_diagram_plan.md `
        UPDATE_NOTES_V0.6.md

git commit -m "docs: add experiment system and quantitative tracking"
git push
```

## 可选：更新 mkdocs.yml

在 `正文` 部分追加：

```yaml
      - 第九章 实验系统与量化记录: book/09-实验系统与量化记录.md
```

在导航中增加：

```yaml
  - 实验:
      - 实验系统说明: docs/experiment_system.md
```
