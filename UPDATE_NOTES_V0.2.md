# V0.2 内容更新说明

本次更新目标：把项目从 V0.1 骨架推进到 V0.2 可读版本。

## 更新内容

1. 补全 `book/02-骨盆决定受力.md`
   - 骨盆作为驾驶坐姿“受力中转站”的完整解释
   - 后倾 / 中立 / 过度前倾的受力差异
   - 靠背、腰托、座椅高度、前沿高度对骨盆的影响
   - “蜷缩在座椅里”何时合理、何时错误
   - 骨盆中立自测与工程验证方法

2. 补全 `book/03-坐骨与软组织受力.md`
   - 坐骨承重正常，坐骨单点压痛异常
   - 坐骨后缘、尾骨方向、两侧软组织挤压的区别
   - 大腿后侧紧硬与坐骨压力的关系
   - 办公椅也有类似感觉时的判断
   - 软组织挤压记录表

3. 强化 `experiments/case_001_current_setup.md`
   - 当前设置复盘
   - 前沿抬高后的受力变化
   - 升高 1 cm、后移 1 cm 的实验假设
   - 保留 / 回退条件
   - 记录表格

## 使用方式

在仓库根目录执行：

```powershell
Expand-Archive .\Tesla-Model3-Ergonomics-v0.2-update.zip -DestinationPath . -Force
git status
git add book/02-骨盆决定受力.md book/03-坐骨与软组织受力.md experiments/case_001_current_setup.md UPDATE_NOTES_V0.2.md
git commit -m "docs: complete pelvis and sit bone pressure chapters"
git push
```
