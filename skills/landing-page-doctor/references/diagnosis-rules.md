# Diagnosis Rules — 10 Checkpoints

Each checkpoint uses **feature detection** (Y/N checks) to calculate scores objectively.

---

## Category A: Value Communication (30 points)

### 1. Headline Value Proposition (0-10)

Feature detection on the headline text:

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Contains second person ("你/你的/your/you") or addresses reader directly? | |
| b | Contains specific number, time, or quantified outcome? | |
| c | Free of technical jargon or product category names as the primary message? (CI/CD, SaaS, API = fail) | |
| d | Contains an action verb (省/搞定/告别/不用再/stop/save/build/get)? | |
| e | Length between 10-30 Chinese chars or 5-15 English words? | |

**Score** = sum of checks (max 10). If only brand name with no value statement = 1.

**Rewrite formula**: [Target user's pain] + [Result after using your product]

Example rewrites:
- Bad: "基于AI的智能项目管理工具" → Good: "3人团队也能10分钟理清所有任务"
- Bad: "One-stop CI/CD Platform" → Good: "Deploy in 2 minutes instead of 40"

### 2. 5-Second Clarity (0-10)

Can a first-time visitor understand what this product does within 5 seconds?

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Headline + subheadline together answer "what does this do for me"? | |
| b | No more than 1 concept/message in the first screen? | |
| c | Subheadline present and provides supporting context (not repeating headline)? | |
| d | The product category is clear without requiring prior knowledge? | |
| e | Language matches target user's vocabulary (not internal team jargon)? | |

### 3. First-Screen Information Density (0-10)

| # | Check | Points |
|---|-------|--------|
| a | Only 3 core elements visible: headline + visual focus + CTA? | +4 |
| b | 4-5 elements (slightly busy but main message clear)? | +2 |
| c | 6+ distinct content blocks visible? | +0 |
| d | Adequate whitespace (text/visual doesn't feel cramped)? | +3 |
| e | No competing conversion targets (only 1 primary CTA)? | +3 |

---

## Category B: Action Guidance (30 points)

### 4. CTA Visibility (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | CTA button visible in the top half of the first screen (no scrolling needed)? | |
| b | CTA color contrasts with page background and surrounding elements? | |
| c | CTA is a button (not just a text link)? | |
| d | Only ONE primary CTA (no competing actions at same visual weight)? | |
| e | CTA size is large enough to be noticed immediately? | |

### 5. CTA Copy (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | CTA text contains a specific action verb (not "了解更多/Learn More/Submit")? | |
| b | CTA describes what happens after clicking ("免费试用/Start Free/See Demo")? | |
| c | CTA feels low-commitment (free, no credit card, instant, 30-second)? | |
| d | Supporting micro-copy near CTA reduces anxiety ("无需绑卡/No credit card")? | |
| e | CTA text is under 8 Chinese chars or 5 English words? | |

Good CTA examples: "免费开始，不用绑卡" / "30秒创建你的第一个项目" / "看看Demo →"

### 6. Commitment Reduction (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Free tier or trial mentioned on first screen? | |
| b | No-credit-card / no-signup-required messaging present? | |
| c | Time-to-value communicated ("2分钟上手/works in 30 seconds")? | |
| d | Reversibility signaled ("随时取消/cancel anytime")? | |
| e | No aggressive pricing or purchase pressure on first screen? | |

---

## Category C: Trust Building (20 points)

### 7. Trust Anchor Presence (0-10)

Must have AT LEAST ONE trust element. Score by quantity and quality:

| # | Element | Points |
|---|---------|--------|
| a | Specific user/customer count ("2000+开发者在使用") | +3 |
| b | One real user testimonial with name/avatar | +3 |
| c | GitHub stars / PH ranking / awards | +2 |
| d | Client logos or media mentions | +2 |
| e | Security badges or certifications | +1 |

Max 10. Zero trust elements = 0 points.

**Adjust by page type**: For type A (indie tool), prioritize a/b/c. For type B (B2B), prioritize d/e. See Step 2 classification.

### 8. Trust Authenticity (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Trust elements include specific details (real name, company, numbers)? | |
| b | Testimonials feel genuine (not generic praise like "Great product!")? | |
| c | Numbers are believable and specific (not suspiciously round like "10000+")? | |
| d | Trust elements are visually integrated (not hidden or afterthought)? | |
| e | At least one trust element with a human face or personal identity? | |

---

## Category D: Technical Performance (20 points)

### 9. Mobile Responsiveness (0-10)

Evaluate from the mobile screenshot:

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | CTA button visible on mobile first screen without scrolling? | |
| b | Text is readable (no text smaller than ~14px equivalent)? | |
| c | No horizontal overflow or elements cut off? | |
| d | Tap targets are adequately sized and spaced? | |
| e | Layout adapts properly (not just a shrunken desktop view)? | |

### 10. First-Screen Copy Readability (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Headline free of unexplained abbreviations or acronyms? | |
| b | No paragraph exceeding 2 lines on first screen? | |
| c | Visual hierarchy clear (headline > subheadline > body, distinct sizes)? | |
| d | Adequate line spacing and character spacing? | |
| e | Contrast ratio between text and background is sufficient for easy reading? | |

---

## Scoring Summary

| Category | Checkpoints | Max Points |
|----------|-------------|-----------|
| A. Value Communication | #1 + #2 + #3 | 30 |
| B. Action Guidance | #4 + #5 + #6 | 30 |
| C. Trust Building | #7 + #8 | 20 |
| D. Technical Performance | #9 + #10 | 20 |
| **Total** | | **100** |

## Priority Rules for Recommendations

When generating Top 3 actions, prioritize by expected ROI:

1. **Headline rewrite** (if #1 < 7) — highest impact, zero cost to change
2. **CTA improvement** (if #4 or #5 < 7) — directly affects conversion
3. **Remove clutter** (if #3 < 7) — quick win, just delete things
4. **Add trust anchor** (if #7 < 5) — moderate effort, high impact
5. **Mobile fix** (if #9 < 7) — technical work, but 60%+ traffic is mobile
6. **Reduce commitment** (if #6 < 7) — copy change, easy to implement

---

## Score Interpretation Matrix (REQUIRED)

Raw scores are objective. But their **meaning** depends on brand maturity. You MUST apply this matrix when writing the "诊断解读" section.

### How brand maturity affects each category

| Category | 🟢 Established brand | 🟡 Growing brand | 🔴 Unknown brand |
|----------|----------------------|-------------------|-------------------|
| A. Value Communication (#1-3) | Low score is a miss but survivable — visitors have context | Moderate impact — some visitors know you, some don't | **CRITICAL** — cold traffic has zero context, every word counts |
| B. Action Guidance (#4-6) | Low score matters less if brand drives direct-URL traffic | Important — mixed traffic needs clear next steps | **CRITICAL** — user must know what to do within 5 seconds |
| C. Trust Building (#7-8) | Low score is acceptable — brand IS the trust | Important — niche recognition helps but isn't enough | **MAKE OR BREAK** — zero trust = zero conversion for cold traffic |
| D. Technical (#9-10) | Same impact regardless of brand | Same impact regardless of brand | Same impact regardless of brand |

### Interpretation rules (follow exactly)

1. **If brand is 🟢 Established AND trust scores (#7+#8) are low**:
   → Write: "该页面信任项得分低，但作为知名品牌，大部分访客已通过口碑/搜索了解产品。信任缺失对实际转化的影响远小于分数显示的程度。"
   → Then ADD: "但如果你是独立开发者，这个分数意味着灾难——冷流量没有品牌认知做缓冲，0分信任 = 0转化。"

2. **If brand is 🟢 Established AND CTA/commitment scores (#4-6) are low**:
   → Write: "该品牌可能依赖品牌驱动的直接流量（用户主动搜索/直接访问），所以弱CTA的影响被稀释。"
   → Then ADD: "独立开发者的流量大部分来自广告或内容引流（冷流量），必须在首屏给出清晰的行动路径。"

3. **If brand is 🔴 Unknown AND any score < 5**:
   → Write: "⚠️ 高危项。作为新品牌，这个分数直接拖累转化率。冷流量不会给你第二次机会。"

4. **"如果你是独立开发者" subsection is ALWAYS required**, regardless of the analyzed page's brand maturity. This subsection must:
   - Reinterpret scores from an indie developer with cold traffic perspective
   - Warn against blindly copying patterns that only work for established brands
   - Give specific, actionable advice for unknown-brand context

5. **"最值得学习的地方" subsection**: Pick 2-3 strengths that are brand-independent (e.g., clean layout, good visual hierarchy, mobile responsiveness, copy readability). These are patterns ANY page can adopt regardless of brand status.

### Example interpretation (for reference)

For a page like Linear.app (🟢 Established, B2B SaaS):
- Trust 0/20 → "Linear 品牌知名度极高，首屏不放信任元素不影响核心用户转化。但独立开发者千万不要学——你的用户不认识你。"
- CTA 14/30 → "Linear 用户大多通过推荐/搜索直接到达，弱CTA影响有限。但对冷流量驱动的新产品，首屏必须有醒目的 Hero CTA。"
- Technical 20/20 → "移动端适配和排版是标杆级别，任何页面都值得学习。"
