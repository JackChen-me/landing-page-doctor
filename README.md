[中文](README.zh-CN.md) | English

# Landing Page Doctor

A Claude Code skill that diagnoses Landing Page first-screen (above the fold) conversion problems and provides actionable rewrite suggestions.

Give it any URL, get a structured 10-point diagnostic report with scores and specific improvements.

## What It Does

1. **Captures** desktop + mobile screenshots and extracts page data (headlines, CTAs, trust signals, etc.)
2. **Classifies** page type (Indie SaaS / B2B / E-commerce / Content) and brand maturity
3. **Diagnoses** against 10 objective checkpoints across 4 categories
4. **Interprets** scores in context — the same score means different things for a known brand vs a new indie project
5. **Outputs** a structured report with specific rewrite suggestions

## The 10 Checkpoints

| Category | # | Checkpoint | Max |
|----------|---|-----------|-----|
| A. Value Communication | 1 | Headline Value Proposition | 10 |
| | 2 | 5-Second Clarity | 10 |
| | 3 | First-Screen Information Density | 10 |
| B. Action Guidance | 4 | CTA Visibility | 10 |
| | 5 | CTA Copy Quality | 10 |
| | 6 | Commitment Reduction | 10 |
| C. Trust Building | 7 | Trust Anchor Presence | 10 |
| | 8 | Trust Authenticity | 10 |
| D. Technical Performance | 9 | Mobile Responsiveness | 10 |
| | 10 | Copy Readability | 10 |
| **Total** | | | **100** |

Each checkpoint uses **objective feature detection** (Y/N checks) rather than subjective judgment, ensuring consistent results across different AI models.

## Install

### Via Plugin Marketplace (Recommended)

In Claude Code, add the marketplace and install:

```shell
/plugin marketplace add JackChen-me/landing-page-doctor
/plugin install landing-page-doctor@jackchen-me-landing-page-doctor
/reload-plugins
```

### Via Local Testing

```bash
git clone https://github.com/JackChen-me/landing-page-doctor.git
claude --plugin-dir ./landing-page-doctor
```

### Prerequisites

The capture script requires [Playwright](https://playwright.dev/python/). It will auto-install on first run, or you can install manually:

```bash
pip install playwright
playwright install chromium
```

## Usage

In Claude Code, run:

```
/landing-page-doctor:landing-page-doctor https://your-landing-page.com
```

Or simply paste a URL and ask Claude to diagnose it:

```
Help me analyze this landing page: https://example.com
```

## Example Output

See [`skills/landing-page-doctor/examples/linear-app.md`](skills/landing-page-doctor/examples/linear-app.md) for a full diagnostic report of linear.app.

**Report structure:**

```
# Landing Page 首屏诊断报告

URL: https://example.com
页面类型: A. Indie tool / SaaS
品牌成熟度: 🔴 Unknown
总分: 42/100
等级: D

## 逐项诊断
### 1. 标题价值主张 [4/10]
当前: "AI-Powered Project Management Platform"
问题: 标题在说"我是什么"，没有告诉用户"你能得到什么"
建议改为:
- 方案A: "Stop drowning in tasks — manage your team's work in 2 minutes"
- 方案B: "Your 3-person team can finally track everything without Excel"

[...10 items with scores and rewrite suggestions...]

## 诊断解读
### 分数背后的真实含义
### 如果你是独立开发者
### 最值得学习的地方

## Top 3 优先行动
1. ...
2. ...
3. ...
```

## Key Design Decisions

**Why brand maturity matters**: A 0/10 trust score means completely different things for Linear (a well-known brand where visitors arrive via word-of-mouth) vs an indie developer's new tool (where cold traffic has zero context). The report always includes a "what this means for indie developers" section.

**Why feature detection over subjective judgment**: Instead of asking the AI "is this headline good?", we break it down into 5 checkable features (contains second person? has specific numbers? includes action verb?). This makes scoring consistent regardless of which AI model runs the skill.

**Why capture before analyze**: The Python script extracts structured data (CTA button colors, sizes, positions, nav item count, trust signal patterns) so the AI works with facts, not just visual impressions.

## File Structure

```
landing-page-doctor/
├── .claude-plugin/
│   ├── plugin.json             # Plugin manifest
│   └── marketplace.json        # Marketplace definition
├── skills/
│   └── landing-page-doctor/
│       ├── SKILL.md            # Main skill definition + workflow + report template
│       ├── scripts/
│       │   └── capture.py      # Playwright-based page capture + data extraction
│       ├── references/
│       │   └── diagnosis-rules.md  # 10 checkpoints with scoring criteria
│       └── examples/
│           └── linear-app.md   # Example report
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## Methodology

Based on conversion optimization principles from:
- Nielsen Norman Group research on above-the-fold attention (57% of viewing time)
- Google PageSpeed data on load time impact (53% bounce at 3s+)
- Unbounce research on single vs multiple CTAs
- Practical experience reviewing indie developer landing pages

## License

MIT
