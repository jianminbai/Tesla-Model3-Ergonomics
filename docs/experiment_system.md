# 实验系统说明

本项目从 V0.6 开始支持结构化实验记录。

## 目录结构

建议使用以下目录：

```text
experiments/
├── templates/
│   ├── driver_daily_log.csv
│   ├── seat_adjustment_events.csv
│   ├── office_rehab_daily_log.csv
│   └── symptom_score_reference.csv
├── data/
│   ├── driver_daily_log.csv
│   ├── seat_adjustment_events.csv
│   └── office_rehab_daily_log.csv
└── output/
    ├── symptom_trends.png
    └── summary.md
```

`templates/` 是模板，不建议直接修改。实际记录建议放在 `experiments/data/`。

---

## 初始化数据目录

在仓库根目录执行：

```powershell
mkdir experiments\data
copy experiments\templates\driver_daily_log.csv experiments\data\driver_daily_log.csv
copy experiments\templates\seat_adjustment_events.csv experiments\data\seat_adjustment_events.csv
copy experiments\templates\office_rehab_daily_log.csv experiments\data\office_rehab_daily_log.csv
```

---

## 每天记录什么

### 1. 驾驶记录

文件：

```text
experiments/data/driver_daily_log.csv
```

每天驾驶后追加一行。

核心字段：

- 日期；
- 驾驶时长；
- 座椅状态编号；
- 坐骨单点疼；
- 坐骨两侧挤压；
- 大腿后侧紧硬；
- 麻刺；
- 右腿疲劳；
- 下车后残留。

### 2. 座椅调整事件

文件：

```text
experiments/data/seat_adjustment_events.csv
```

每次调座椅追加一行。

例如：

```text
2026-06-30,A,+1cm height,座椅整体升高约1cm,减轻坐骨两侧软组织挤压
```

### 3. 办公与康复记录

文件：

```text
experiments/data/office_rehab_daily_log.csv
```

记录：

- 当天最长连续久坐；
- 起身次数；
- 是否拉伸；
- 大腿后侧紧硬；
- 办公椅坐骨两侧挤压；
- 睡眠；
- 是否骑车或运动。

---

## 运行分析脚本

依赖：

```powershell
pip install pandas matplotlib
```

运行：

```powershell
python scripts\analyze_experiments.py
```

输出：

```text
experiments/output/symptom_trends.png
experiments/output/summary.md
```

---

## 建议实验节奏

### 第 1-3 天：基线

不调整座椅，只记录。

### 第 4-6 天：升高 1 cm

只改变高度。

### 第 7 天：复盘

比较基线和升高后的评分。

### 第 8-10 天：后移 1 cm

只改变前后位置。

### 第 11 天：复盘

判断后移是否保留。

### 第 12-14 天：稳定验证

不再调整，观察设置是否稳定。

---

## 判断规则

### 保留

- 目标症状下降 ≥ 2 分；
- 无麻刺；
- 驾驶安全不受影响；
- 下车后无残留。

### 继续观察

- 新压力出现但不麻不刺；
- 评分波动但均值下降；
- 不影响驾驶安全。

### 回退

- 麻刺；
- 放射痛；
- 无力；
- 刹车腿接近伸直；
- 身体前探；
- 下车后残留明显。
