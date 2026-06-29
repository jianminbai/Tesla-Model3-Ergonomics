# GitHub Pages 发布指南

本指南用于把本项目发布成在线网站。

---

## 1. 本地先检查

在仓库根目录执行：

```powershell
python scripts\validate_site.py
```

安装 MkDocs：

```powershell
pip install mkdocs mkdocs-material pymdown-extensions
```

构建：

```powershell
mkdocs build --strict
```

本地预览：

```powershell
mkdocs serve
```

打开终端中显示的本地地址。

---

## 2. 启用 GitHub Actions

进入 GitHub 仓库：

```text
Actions
```

如果看到提示：

```text
I understand my workflows, go ahead and enable them
```

点击启用。

---

## 3. 推送 main 分支

```powershell
git add .
git commit -m "docs: optimize GitHub Pages site"
git push
```

推送后，GitHub Actions 会自动执行：

```text
Install dependencies
Validate site files
Build MkDocs site
Deploy to GitHub Pages
```

---

## 4. 设置 Pages

进入：

```text
Settings → Pages
```

推荐设置：

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: /root
```

保存。

---

## 5. 访问网站

发布后地址通常是：

```text
https://jianminbai.github.io/Tesla-Model3-Ergonomics/
```

第一次可能需要等待数分钟。

---

## 6. 常见问题

### 问题一：Actions 没有运行

检查：

- `.github/workflows/docs.yml` 是否存在；
- 是否 push 到 main；
- Actions 是否启用。

### 问题二：mkdocs build --strict 失败

常见原因：

- `mkdocs.yml` 中引用了不存在的文件；
- Markdown 中链接到不存在路径；
- 依赖未安装；
- 文件名大小写不一致。

先运行：

```powershell
python scripts\validate_site.py
```

### 问题三：Pages 访问 404

检查：

- Actions 是否成功；
- 是否生成 `gh-pages` 分支；
- Pages 是否选择了 `gh-pages / root`；
- 仓库是否公开；
- 等待几分钟后刷新。

### 问题四：SVG 不显示

检查：

- SVG 文件是否存在；
- Markdown 路径是否正确；
- 文件名是否包含空格或中文；
- 是否被 `.gitignore` 忽略。

---

## 7. 发布后检查清单

- [ ] 首页能打开；
- [ ] 顶部导航正常；
- [ ] 搜索可用；
- [ ] 正文章节都能打开；
- [ ] 快速排查表能打开；
- [ ] 插图索引能打开；
- [ ] SVG 图能显示；
- [ ] GitHub 仓库链接正确；
- [ ] 手机端阅读正常；
- [ ] 免责声明清晰可见。

---

## 8. 建议发布节奏

每次版本更新：

```text
生成更新包
↓
本地覆盖
↓
validate_site
↓
mkdocs build --strict
↓
commit
↓
push
↓
检查 Actions
↓
检查在线网站
```
