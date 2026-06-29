# V0.3 内容更新说明

本次更新目标：补全 Tesla Model 3 专项分析，让项目从“通用驾驶人体工程学”进入“车型专项受力分析”。

## 更新内容

### 1. 补全第四章：Tesla Model 3 座椅结构分析

文件：

```text
book/04-Tesla_Model3座椅结构分析.md
```

新增内容：

- Model 3 座椅为什么需要单独分析
- 坐垫后部、前沿、侧翼、靠背、腰托、座椅高度、前后位置的受力关系
- 为什么容易出现坐骨单点压痛
- 为什么容易出现大腿后侧紧硬
- 为什么坐骨两侧软组织会被挤压
- 为什么右侧不适比左侧更常见
- Model 3 座椅调整的变量优先级
- 工程验证清单

### 2. 新增第六章：踏板几何与右腿疲劳

文件：

```text
book/06-踏板几何与右腿疲劳.md
```

新增内容：

- 驾驶坐姿与办公坐姿的核心差异
- 右腿为什么既承重又操作
- 油门脚跟支点、脚踝角度、髋膝角度的关系
- 为什么离开油门后右侧压力可能瞬间减轻
- 座椅前后、高度、前沿对右腿的影响
- 右腿疲劳的工程判断表

### 3. 新增 V0.3 插图清单

文件：

```text
assets/diagrams/v0.3_diagram_plan.md
```

用于后续绘制 Model 3 专项图，包括：

- 坐垫俯视压力图
- 侧翼挤压横截面图
- 座椅高度变化力线图
- 后移 1 cm 的腿部几何图
- 右腿踩油门动态负荷图

## 应用方式

将压缩包放到仓库根目录后执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.3-update.zip -DestinationPath . -Force

git status
git add book/04-Tesla_Model3座椅结构分析.md `
        book/06-踏板几何与右腿疲劳.md `
        assets/diagrams/v0.3_diagram_plan.md `
        UPDATE_NOTES_V0.3.md

git commit -m "docs: add Model 3 seat structure and pedal geometry analysis"
git push
```

## 可选：更新 mkdocs.yml

如果要在网站导航中显示第六章，请在 `mkdocs.yml` 的 `正文` 部分追加：

```yaml
      - 第六章 踏板几何与右腿疲劳: book/06-踏板几何与右腿疲劳.md
```
