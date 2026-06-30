# 快速开始

## 1. 先不要急着写完整书

第一阶段目标不是一次写完 10 万字，而是建立一个能持续迭代的项目骨架：

- 目录稳定
- 术语稳定
- 案例记录格式稳定
- 每章都能独立完善
- 插图后续可逐步补充

## 2. 今天你需要做的三件事

### 第一步：创建 GitHub 仓库

仓库名建议：

```text
Tesla-Model3-Ergonomics
```

描述：

```text
A Chinese open-source guide to Tesla Model 3 driving ergonomics, biomechanics and seat pressure analysis.
```

### 第二步：把本项目提交上去

在解压后的目录中执行：

```bash
git init
git add .
git commit -m "init: ergonomics guide structure and chapter draft"
git branch -M main
git remote add origin git@github.com:bai8962/Tesla-Model3-Ergonomics.git
git push -u origin main
```

如果你用 HTTPS：

```bash
git remote add origin https://github.com/bai8962/Tesla-Model3-Ergonomics.git
git push -u origin main
```

### 第三步：从实验记录开始迭代

不要先追求“写得漂亮”，先每天记录真实驾驶数据：

- 当前座椅高度变化
- 是否后移
- 前沿高度
- 坐骨压痛
- 大腿后侧紧硬
- 坐骨两侧软组织挤压
- 踩油门是否自然
- 30 / 60 / 90 分钟后的变化

模板见：

```text
experiments/driver_log_template.md
```

本地预览网站：

```bash
pip install -r requirements.txt
mkdocs serve
```

## 3. 第一周目标

第一周只做四件事：

1. 完成 README。
2. 完成第一章初稿。
3. 连续记录 5 次驾驶实验。
4. 把“升高 1 cm + 后移 1 cm”的验证结果写进 Case001。

不要同时扩展太多章节。
