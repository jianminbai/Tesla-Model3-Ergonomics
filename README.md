# Tesla Model 3 驾驶人体工程学与受力分析指南

> 用人体工程学、生物力学、受力图和工程实验，系统解释 Tesla Model 3 驾驶中的坐骨、大腿、臀部、腰背和右腿不适。

这是一本持续迭代的开源指南，不是普通的座椅调节经验帖。

核心目标是回答：

- 为什么座椅调高后坐骨疼可能减轻，但大腿后侧压力会增加？
- 为什么“坐骨承重”是正常的，但“坐骨单点压痛”不正常？
- 为什么坐骨两侧软组织会被挤？
- 为什么右腿踩油门时更容易紧、硬、累？
- 为什么办公椅也有类似感觉时，不能只怪车座？
- 如何用工程实验记录座椅调整，而不是每天凭感觉乱调？

---

## 在线阅读

如果 GitHub Pages 已启用，在线地址通常为：

```text
https://jianminbai.github.io/Tesla-Model3-Ergonomics/
```

---

## 快速入口

| 入口 | 适合谁 |
|---|---|
| [快速开始](QUICKSTART.md) | 第一次打开项目的人 |
| [症状快速排查表](docs/quick_diagnosis_table.md) | 想快速判断不适来源的人 |
| [办公椅检查清单](docs/office_chair_checklist.md) | 办公久坐也不舒服的人 |
| [实验系统说明](docs/experiment_system.md) | 想量化记录座椅调整的人 |
| [插图索引](docs/diagram_index.md) | 想看受力图和流程图的人 |
| [案例库](docs/case_library.md) | 想参考结构化案例的人 |
| [Model Y 与其他车型对比](docs/model_y_and_other_cars.md) | 想迁移到其他车型的人 |
| [English Summary](docs/english_summary.md) | English readers and project overview |
| [路线图](ROADMAP.md) | 想了解项目计划的人 |

---

## 推荐阅读路线

### 路线 A：我现在就不舒服，想快速判断

1. [第七章 症状决策树](book/07-症状决策树.md)
2. [症状快速排查表](docs/quick_diagnosis_table.md)
3. [第五章 座椅调节流程](book/05-座椅调节流程.md)
4. [实验记录模板](experiments/symptom_decision_log_template.md)

### 路线 B：我想理解为什么会疼

1. [第一章 驾驶为什么会让人疼](book/01-驾驶为什么会让人疼.md)
2. [第二章 骨盆决定受力](book/02-骨盆决定受力.md)
3. [第三章 坐骨与软组织受力](book/03-坐骨与软组织受力.md)

### 路线 C：我想分析 Model 3 座椅

1. [第四章 Tesla Model 3 座椅结构分析](book/04-Tesla_Model3座椅结构分析.md)
2. [第六章 踏板几何与右腿疲劳](book/06-踏板几何与右腿疲劳.md)
3. [插图索引](docs/diagram_index.md)

### 路线 D：我想做长期实验

1. [第九章 实验系统与量化记录](book/09-实验系统与量化记录.md)
2. [实验系统说明](docs/experiment_system.md)
3. `experiments/templates/driver_daily_log.csv`
4. `scripts/analyze_experiments.py`

### 路线 E：我想看案例或对比其他车型

1. [案例库](docs/case_library.md)
2. [Case001 当前设置](experiments/case_001_current_setup.md)
3. [Model Y 与其他车型对比](docs/model_y_and_other_cars.md)

---

## 当前内容结构

```text
book/                                # 正文 12 章
├── 00-前言.md
├── 01-驾驶为什么会让人疼.md
├── 02-骨盆决定受力.md
├── 03-坐骨与软组织受力.md
├── 04-Tesla_Model3座椅结构分析.md
├── 05-座椅调节流程.md
├── 06-踏板几何与右腿疲劳.md
├── 07-症状决策树.md
├── 08-康复与办公椅联动.md
├── 09-实验系统与量化记录.md
├── 10-可视化插图与图表体系.md
└── 11-GitHub_Pages发布与项目运营.md

docs/                                # 辅助文档
├── quick_diagnosis_table.md         #   症状快速排查表
├── office_chair_checklist.md        #   办公椅检查清单
├── experiment_system.md             #   实验系统说明
├── case_library.md                  #   案例库
├── model_y_and_other_cars.md        #   Model Y 与其他车型对比
├── english_summary.md               #   英文摘要
├── diagram_index.md                 #   插图索引
├── visual_style_guide.md            #   视觉风格指南
├── navigation_map.md                #   导航地图
└── github_pages_publish_guide.md    #   发布指南

assets/diagrams/svg/                 # 8 张原创 SVG 插图
├── 01_pressure_distribution.svg
├── 02_pelvis_postures.svg
├── 03_model3_seat_top_view.svg
├── 04_seat_height_force_change.svg
├── 05_pedal_dynamic_load_chain.svg
├── 06_symptom_decision_overview.svg
├── 07_experiment_system_flow.svg
└── 08_rehab_office_triangle.svg

assets/images/realistic/             # 真实感教育图片
├── 01_realistic_pressure_distribution.png
├── 02_realistic_pelvis_postures.png
├── 03_realistic_pedal_load_chain.png
└── 04_realistic_seat_office_body_triangle.png

experiments/                         # 实验系统
├── templates/                       #   CSV 记录模板
├── data/                            #   实际记录数据
├── output/                          #   分析脚本输出
└── case_001_current_setup.md        #   当前案例

scripts/                             # 工具脚本
├── validate_site.py
├── check_diagrams.py
└── analyze_experiments.py
```

---

## 项目方法论

本项目采用三层内容结构：

### 1. 人体工程学与生物力学原理

解释：

- 压力与压强；
- 骨盆姿态；
- 坐骨承重；
- 大腿后侧张力；
- 踏板控制负荷。

### 2. Tesla Model 3 专项结构分析

解释：

- 坐垫后部；
- 坐垫前沿；
- 坐垫侧翼；
- 靠背角度；
- 腰托；
- 座椅高度；
- 前后位置；
- 电动车踏板几何。

### 3. 工程实验与真实案例

通过 CSV、Markdown 模板和趋势图记录：

- 每次座椅调整；
- 每天驾驶反馈；
- 办公久坐影响；
- 康复动作执行情况；
- 保留 / 回退 / 继续观察的判断。

---

## 已有可视化图

当前已有 SVG 插图包括：

- 压力分布示意图；
- 骨盆三姿态受力图；
- Model 3 坐垫俯视结构图；
- 座椅高度变化受力图；
- 右腿踩油门动态负荷链；
- 症状快速决策总览；
- 座椅调整工程实验流程；
- 车座、办公椅、身体状态三角模型。

查看：

[插图索引](docs/diagram_index.md)

当前新增真实感教育图片包括：

- 真实感座椅压力分布；
- 真实感骨盆姿态对比；
- 真实感右腿踏板负荷链；
- 真实感车座、办公椅、身体状态联动。

查看：

[插图索引](docs/diagram_index.md)

---

## 本地预览网站

安装依赖：

```bash
pip install -r requirements.txt
```

本地启动：

```bash
mkdocs serve
```

构建检查：

```bash
python scripts/sync_site_docs.py
mkdocs build --strict
```

---

## 实验数据分析

初始化数据目录：

```powershell
mkdir experiments\data
copy experiments\templates\driver_daily_log.csv experiments\data\driver_daily_log.csv
copy experiments\templates\seat_adjustment_events.csv experiments\data\seat_adjustment_events.csv
copy experiments\templates\office_rehab_daily_log.csv experiments\data\office_rehab_daily_log.csv
```

安装依赖：

```powershell
pip install -r requirements.txt
```

生成趋势图：

```powershell
python scripts\analyze_experiments.py
```

输出：

```text
experiments/output/symptom_trends.png
experiments/output/summary.md
```

---

## 免责声明

本文档用于人体工程学理解、座椅调节思路和工程记录，不构成医学诊断或治疗建议。

如果出现以下情况，应咨询医生或物理治疗师：

- 麻木、刺痛离开座椅后仍持续；
- 疼痛沿大腿后侧向小腿放射；
- 出现无力；
- 夜间痛明显；
- 休息后不缓解；
- 调整座椅和减少久坐 1 到 2 周仍无改善。

---

## License

- 文档内容：CC BY-NC 4.0
- 脚本代码：MIT License (see [LICENSE](https://github.com/jianminbai/Tesla-Model3-Ergonomics/blob/main/LICENSE))
