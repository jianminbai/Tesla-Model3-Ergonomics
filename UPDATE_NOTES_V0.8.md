# V0.8 内容更新说明

本次更新目标：完成 GitHub Pages 发布优化，让项目从“仓库文档”升级为“可公开访问、可导航、可维护的网站”。

## 更新内容

### 1. 重构 README 首页

文件：

```text
README.md
```

新增：

- 项目一句话定位
- 快速入口
- 阅读路线
- 当前版本能力
- 实验系统入口
- 图表入口
- 免责声明
- Roadmap 摘要

### 2. 完善 MkDocs 导航

文件：

```text
mkdocs.yml
```

新增完整导航：

- 首页
- 快速开始
- 正文 1-10 章
- 快速排查
- 实验系统
- 图表
- 项目维护

### 3. 优化 GitHub Actions 发布流程

文件：

```text
.github/workflows/docs.yml
```

新增：

- Python 环境
- 依赖安装
- MkDocs 构建检查
- gh-pages 部署

### 4. 新增第十一章：GitHub Pages 发布与项目运营

文件：

```text
book/11-GitHub_Pages发布与项目运营.md
```

内容：

- 为什么要做成网站
- GitHub Pages 设置
- MkDocs 使用
- 内容版本管理
- Issue 收集案例
- Release 节奏
- 从个人案例到开源知识库

### 5. 新增站点发布指南

文件：

```text
docs/github_pages_publish_guide.md
```

内容：

- 如何启用 Actions
- 如何设置 Pages
- 如何本地预览
- 常见错误排查
- 发布后的检查清单

### 6. 新增导航地图

文件：

```text
docs/navigation_map.md
```

用于说明读者应该如何使用该网站。

### 7. 新增站点检查脚本

文件：

```text
scripts/validate_site.py
```

功能：

- 检查关键文件是否存在
- 检查章节文件是否存在
- 检查 SVG 是否存在
- 检查 mkdocs.yml 是否存在
- 输出站点发布前检查结果

### 8. 新增 Issue 模板

目录：

```text
.github/ISSUE_TEMPLATE/
```

包含：

```text
seat_case_report.md
content_correction.md
diagram_request.md
```

用途：

- 收集真实座椅案例
- 收集内容纠错
- 收集插图需求

## 应用方式

将压缩包放到仓库根目录后执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.8-update.zip -DestinationPath . -Force

git status
git add README.md `
        mkdocs.yml `
        .github/workflows/docs.yml `
        .github/ISSUE_TEMPLATE/seat_case_report.md `
        .github/ISSUE_TEMPLATE/content_correction.md `
        .github/ISSUE_TEMPLATE/diagram_request.md `
        book/11-GitHub_Pages发布与项目运营.md `
        docs/github_pages_publish_guide.md `
        docs/navigation_map.md `
        scripts/validate_site.py `
        UPDATE_NOTES_V0.8.md

git commit -m "docs: optimize GitHub Pages publishing and site navigation"
git push
```

## 本地检查

```powershell
python scripts\validate_site.py
pip install mkdocs mkdocs-material
mkdocs build --strict
mkdocs serve
```

## GitHub Pages 设置

进入仓库：

```text
Settings → Pages
```

推荐：

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: /root
```

发布后地址通常为：

```text
https://jianminbai.github.io/Tesla-Model3-Ergonomics/
```
