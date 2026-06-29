# Tesla Model 3 驾驶人体工程学与受力分析指南

## 项目概述

使用人体工程学、生物力学、受力图和工程实验，系统解释 Tesla Model 3 驾驶中的坐骨、大腿、臀部、腰背和右腿不适。

## 仓库结构

```
book/                       # 正文 12 章（00-11）
docs/                       # 辅助文档（排查表、检查清单、实验说明等）
assets/diagrams/svg/        # 8 张原创 SVG 插图
experiments/                # 实验系统（模板、数据、案例）
scripts/                    # 工具脚本（站点验证、插图检查、数据分析）
.github/workflows/          # GitHub Actions 部署配置
```

## 技术栈

- 文档：Markdown + MkDocs (material theme)
- 图表：SVG
- 数据分析：Python (pandas, matplotlib)
- 部署：GitHub Actions → GitHub Pages

## 关键命令

```bash
# 本地预览网站
pip install mkdocs mkdocs-material pymdown-extensions
mkdocs serve

# 构建检查
mkdocs build --strict

# 站点验证
python scripts/validate_site.py

# 插图检查
python scripts/check_diagrams.py

# 实验数据分析
pip install pandas matplotlib
python scripts/analyze_experiments.py
```

## 版本历史

- v0.8: GitHub Pages 发布、站点导航、Issue 模板
- v0.7: 可视化插图体系、8 张 SVG
- v0.6: 实验系统、CSV 模板、分析脚本
- v0.5: 康复与办公椅联动
- v0.4: 症状决策树
- v0.3: Model 3 专项分析
- v0.2: 人体工程学基础
- v0.1: 项目启动

## 内容原则

1. 不把个体经验当成普遍结论
2. 每个调节动作尽量只改变一个变量
3. 区分疼痛、酸胀、麻木、紧硬、压迫感
4. 涉及持续症状时建议就医，不做诊断
5. 所有图使用统一颜色规范（蓝=正常、橙=观察、红=风险、绿=改善）

## 贡献方式

- 提交真实座椅案例（使用 Issue 模板）
- 内容纠错
- 插图建议
- 不同身高体型的调节反馈
- Model Y 或其他车型对比

## Git 配置

- 主分支：main
- 提交信息前缀：docs:（文档）、feat:（新功能）、fix:（修复）、chore:（维护）
