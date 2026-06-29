# V0.5 内容更新说明

本次更新目标：补充“康复与办公椅联动”模块，把驾驶不适从单一座椅问题扩展为：

```text
车辆座椅几何
+
办公久坐环境
+
大腿后侧 / 臀部 / 髋部软组织状态
+
骨盆控制能力
```

## 更新内容

### 1. 新增第八章：康复与办公椅联动

文件：

```text
book/08-康复与办公椅联动.md
```

核心内容：

- 为什么办公椅也有类似感觉很重要
- 如何区分“车座问题”和“身体组织状态问题”
- 腘绳肌、臀肌、梨状肌、髋屈肌与坐姿受力的关系
- 为什么大腿后侧紧硬会影响坐骨附近压力
- 车内调整与日常康复的配合顺序
- 每日 10 分钟基础方案
- 每 30 到 45 分钟的办公椅重置流程
- 什么时候应该咨询医生或物理治疗师

### 2. 新增办公椅检查清单

文件：

```text
docs/office_chair_checklist.md
```

包含：

- 办公椅高度
- 坐深
- 坐垫前沿
- 腰背支撑
- 屏幕和键盘位置
- 起身节奏
- 与驾驶座椅的联动判断

### 3. 新增康复与办公记录模板

文件：

```text
experiments/rehab_office_log_template.md
```

用于记录：

- 当天办公久坐时间
- 大腿后侧紧硬评分
- 坐骨两侧挤压评分
- 拉伸 / 放松执行情况
- 第二天驾驶反馈

### 4. 新增 V0.5 插图计划

文件：

```text
assets/diagrams/v0.5_rehab_office_diagram_plan.md
```

规划：

- 腘绳肌牵拉坐骨示意图
- 臀肌紧张与坐骨两侧挤压图
- 办公椅 vs 驾驶座椅受力对比图
- 每 45 分钟重置流程图
- 10 分钟日常方案图

## 应用方式

将压缩包放到仓库根目录后执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.5-update.zip -DestinationPath . -Force

git status
git add book/08-康复与办公椅联动.md `
        docs/office_chair_checklist.md `
        experiments/rehab_office_log_template.md `
        assets/diagrams/v0.5_rehab_office_diagram_plan.md `
        UPDATE_NOTES_V0.5.md

git commit -m "docs: add rehab and office chair integration guide"
git push
```

## 可选：更新 mkdocs.yml

在 `正文` 部分追加：

```yaml
      - 第八章 康复与办公椅联动: book/08-康复与办公椅联动.md
```

在导航中增加：

```yaml
  - 快速排查:
      - 办公椅检查清单: docs/office_chair_checklist.md
```
