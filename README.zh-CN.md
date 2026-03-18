中文 | [English](README.md)

# Landing Page Doctor

一个 Claude Code 技能，用于诊断 Landing Page 首屏（above the fold）转化问题，并提供可直接执行的改写建议。

给它一个 URL，拿到一份 10 项评分的结构化诊断报告。

## 它做什么

1. **采集** 桌面端 + 移动端截图，提取页面数据（标题、CTA、信任信号等）
2. **分类** 页面类型（独立工具/B2B/电商/内容）及品牌成熟度
3. **诊断** 4大类 10 项客观检查点逐项评分
4. **解读** 结合品牌成熟度解释分数含义——同一个分数对知名品牌和新产品意义完全不同
5. **输出** 结构化报告，低分项附带具体改写方案

## 10 项诊断清单

| 类别 | # | 检查项 | 满分 |
|------|---|--------|------|
| A. 价值传达 | 1 | 标题价值主张 | 10 |
| | 2 | 5秒清晰度 | 10 |
| | 3 | 首屏信息密度 | 10 |
| B. 行动引导 | 4 | CTA 可见性 | 10 |
| | 5 | CTA 文案质量 | 10 |
| | 6 | 承诺降低 | 10 |
| C. 信任建立 | 7 | 信任锚点 | 10 |
| | 8 | 信任真实性 | 10 |
| D. 技术表现 | 9 | 移动端适配 | 10 |
| | 10 | 文案可读性 | 10 |
| **总分** | | | **100** |

每项检查使用**客观特征检测**（Y/N 判断），而非主观评价，确保不同 AI 模型输出结果一致。

## 安装

```bash
npx skills add JackChen-me/landing-page-doctor
```

或手动安装：

```bash
git clone https://github.com/JackChen-me/landing-page-doctor.git ~/.claude/skills/landing-page-doctor
```

### 依赖

采集脚本需要 [Playwright](https://playwright.dev/python/)，首次运行会自动安装，也可手动安装：

```bash
pip install playwright
playwright install chromium
```

## 使用

在 Claude Code 中运行：

```
/landing-page-doctor https://your-landing-page.com
```

或者直接贴 URL 让 Claude 诊断：

```
帮我分析一下这个 Landing Page：https://example.com
```

## 报告示例

完整报告见 [`examples/linear-app.md`](examples/linear-app.md)（以 linear.app 为例）。

**报告结构：**

```
# Landing Page 首屏诊断报告

URL: https://example.com
页面类型: A. 独立工具 / SaaS
品牌成熟度: 🔴 Unknown
总分: 42/100
等级: D

## 逐项诊断
### 1. 标题价值主张 [4/10]
当前: "基于AI的智能项目管理工具"
问题: 标题在说"我是什么"，没有告诉用户"你能得到什么"
建议改为:
- 方案A: "3人团队也能10分钟理清所有任务"
- 方案B: "别再用Excel管项目了——点一下就能看到谁在干什么"

[...10 项逐条诊断 + 改写建议...]

## 诊断解读
### 分数背后的真实含义
### 如果你是独立开发者
### 最值得学习的地方

## Top 3 优先行动
1. ...
2. ...
3. ...
```

## 核心设计理念

**为什么要区分品牌成熟度**：信任项 0 分，对 Linear（知名品牌，用户靠口碑来的）和对独立开发者的新工具（冷流量，用户不认识你）完全是两回事。报告永远包含「如果你是独立开发者」的解读段。

**为什么用特征检测而非主观判断**：不问 AI「这个标题好不好」，而是拆成 5 个可检测特征（有没有第二人称？有没有数字？有没有动词？）。这样不管哪个模型跑，评分都一致。

**为什么先采集再分析**：Python 脚本预先提取结构化数据（CTA 按钮颜色、尺寸、位置、导航项数量、信任信号模式），让 AI 基于事实分析，而非仅凭截图印象。

## 文件结构

```
landing-page-doctor/
├── SKILL.md                    # 技能定义 + 工作流 + 报告模板
├── scripts/
│   └── capture.py              # 基于 Playwright 的页面采集 + 数据提取
├── references/
│   └── diagnosis-rules.md      # 10 项检查点评分标准 + 解读矩阵
├── examples/
│   └── linear-app.md           # 示例报告
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## 方法论

基于以下转化优化研究：
- Nielsen Norman Group：首屏注意力分布研究（57% 浏览时间在首屏）
- Google PageSpeed：加载时间对跳出率影响（3秒以上 53% 跳出）
- Unbounce：单一 vs 多 CTA 的转化率对比
- 大量独立开发者 Landing Page 实战诊断经验

## 深度服务

免费诊断只看首屏。想要完整转化漏斗诊断（首屏 → 功能页 → 定价 → 注册流 → 留存）？

关注「硅基杠杆OS」获取深度业务诊断服务。

## 许可证

MIT
