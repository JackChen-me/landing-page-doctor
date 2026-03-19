# Diagnosis Rules — 14 Checkpoints (v2.0)

Each checkpoint uses **feature detection** (Y/N checks) to calculate scores objectively.

**Scoring**: 14 items × 0-10 = 140 raw points. Final score = (raw / 140) × 100, rounded.

**Anti-inflation rule**: If all sub-checks technically pass but the checkpoint's real-world intent clearly fails, apply a **-2 "reality check" deduction** and document the reason. Example: headline passes all word-count and verb checks but communicates nothing meaningful.

---

## Category A: Value Communication (40 points)

### 1. Headline Value Proposition (0-10)

Feature detection on the headline text:

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Contains second person ("你/你的/your/you") or addresses reader directly? | |
| b | Contains specific number, time, or quantified outcome? | |
| c | Free of technical jargon or product category names as the primary message? (CI/CD, SaaS, API = fail unless target audience is developers and term is universally understood) | |
| d | Contains an action verb (省/搞定/告别/不用再/stop/save/build/get/paste/create)? | |
| e | Length between 10-30 Chinese chars or 5-15 English words? | |

**Score** = sum of checks (max 10). If only brand name with no value statement = 1.

**Anti-inflation guard**: If headline uses animated/rotating words, verify that EACH variant independently makes sense. If any variant creates confusion or contradicts others, apply -2.

**Rewrite formula**: [Target user's pain] + [Result after using your product]

Example rewrites:
- Bad: "基于AI的智能项目管理工具" → Good: "3人团队也能10分钟理清所有任务"
- Bad: "One-stop CI/CD Platform" → Good: "Deploy in 2 minutes instead of 40"

### 2. 5-Second Clarity (0-10)

Can a first-time visitor understand what this product does within 5 seconds?

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Headline + subheadline together answer "what does this do for me"? | |
| b | No more than 1 core concept in the first screen? (Supporting elements like social proof don't count as extra concepts, but embedded interactive demos with their own CTA DO count as a second concept) | |
| c | Subheadline present and provides supporting context (not repeating headline)? | |
| d | The product category is clear without requiring prior knowledge? | |
| e | Language matches target user's vocabulary (not internal team jargon)? | |

### 3. Target Audience Anchoring (0-10) ★ NEW

Does the page explicitly communicate WHO this product is for?

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Target user is named or described on the first screen ("for SaaS founders / 为设计师打造 / built for teams")? | |
| b | Pain point or use case speaks to a specific audience (not "anyone who wants to...")? | |
| c | Language/examples reflect target user's world (industry terms they'd use, scenarios they'd recognize)? | |
| d | Social proof (if present) features people from the target user type (not unrelated personas)? | |
| e | The visitor can self-identify ("this is for me") within 5 seconds? | |

**Score cap**: If target audience is never mentioned or implied anywhere on the first screen → max 2.

**Why this matters**: Generic pages convert poorly. "Built for SaaS founders who hate writing social posts" outperforms "AI content generation tool" by 2-3x on cold traffic.

### 4. First-Screen Information Density (0-10)

| # | Check | Points |
|---|-------|--------|
| a | Only 3 core elements visible: headline + visual focus + CTA? | +4 |
| b | 4-5 elements (slightly busy but main message clear)? | +2 |
| c | 6+ distinct content blocks visible? | +0 |
| d | Adequate whitespace (text/visual doesn't feel cramped)? | +3 |
| e | No competing conversion targets (only 1 primary CTA at highest visual weight)? | +3 |

**Counting rule for a/b/c**: Count these as distinct visual elements: nav bar, badge/label, each headline, subheadline, each CTA button, input fields, platform/tab selectors, testimonial/social proof areas, images/videos, interactive demos. Group items that form a single visual unit (e.g., headline + subheadline = 1, but headline + separate URL input = 2).

**Anti-inflation guard for d**: If `first_screen_block_count` from data.json is 15+, whitespace score can be at most +1 regardless of perceived spacing.

---

## Category B: Action Guidance (30 points)

### 5. CTA Visibility (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | CTA button visible in the top half of the first screen (no scrolling needed)? | |
| b | CTA color contrasts with page background AND is the most visually prominent clickable element? | |
| c | CTA is a button (not just a text link)? | |
| d | Only ONE primary CTA at the highest visual weight? (Secondary CTAs must be visually subordinate — smaller, ghost/outline style, or text link) | |
| e | CTA size is large enough to be noticed immediately (min ~120px wide)? | |

**Anti-inflation guard for d**: If two or more CTAs have similar visual weight (same size, both filled with color, both prominent), this is N=0 even if one has a slightly different shade. Compare `width`, `height`, `bgColor` from data.json.

### 6. CTA Copy (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | CTA text contains a specific action verb (not "了解更多/Learn More/Submit")? | |
| b | CTA describes what happens after clicking ("免费试用/Start Free/See Demo")? | |
| c | CTA feels low-commitment (free, no credit card, instant, 30-second)? | |
| d | Supporting micro-copy near CTA explicitly reduces ENTRY barrier anxiety? Must specifically address credit-card/payment concern if CTA leads to signup. "Cancel anytime" alone is NOT sufficient — that addresses EXIT, not ENTRY. | |
| e | CTA text is under 8 Chinese chars or 5 English words? | |

**Tighter rule for d**: If the CTA leads to a signup/trial and there is no explicit "no credit card" / "无需绑卡" / "no payment info required" messaging → N=0, even if "cancel anytime" is present.

Good CTA examples: "免费开始，不用绑卡" / "30秒创建你的第一个项目" / "看看Demo →"

### 7. Commitment Reduction (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Free tier or trial mentioned on first screen? | |
| b | No-credit-card / no-signup-required messaging present? | |
| c | Time-to-value communicated ("2分钟上手/works in 30 seconds")? | |
| d | Reversibility signaled ("随时取消/cancel anytime")? | |
| e | No aggressive pricing or purchase pressure on first screen? | |

---

## Category C: Trust & Proof (30 points)

### 8. Trust Anchor Presence (0-10)

Must have AT LEAST ONE trust element. Score by quantity and quality:

| # | Element | Points |
|---|---------|--------|
| a | Specific user/customer count FOR THIS PRODUCT ("2000+开发者在使用 [本产品]") — must be the product's own user count, not a customer's success metric | +3 |
| b | One real user testimonial with verifiable identity (real full name + company, OR linkable social profile, OR real photo) | +3 |
| c | GitHub stars / PH ranking / awards | +2 |
| d | Client logos or media mentions | +2 |
| e | Security badges or certifications | +1 |

Max 10. Zero trust elements = 0 points.

**Tighter rule for a**: User count must clearly refer to THIS product's own users. Numbers mentioned inside a testimonial about someone else's success (e.g., "my product got 2000 users thanks to [this tool]") do NOT count as a user-count anchor for this tool → +0 for this sub-item.

**Tighter rule for b**: Testimonials with only initials or @handles that cannot be clicked to verify → half credit (+1 instead of +3). Full +3 requires: real photo OR verifiable full name + company OR clickable link to a real social profile.

**Adjust by page type**: For type A (indie tool), prioritize a/b/c. For type B (B2B), prioritize d/e. See Step 2 classification.

### 9. Trust Authenticity (0-10)

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Trust elements include specific, verifiable details (real name, real company, real numbers)? | |
| b | Testimonials feel genuine AND varied in structure? (If ALL testimonials follow the same sentence pattern like "[handle] — [product] got [metric] thanks to [tool]", this reads as manufactured → N=0 even if content is specific) | |
| c | Numbers are believable and specific (not suspiciously round like "10000+")? | |
| d | Trust elements are visually integrated (not hidden or afterthought)? | |
| e | At least one trust element with a real human face or verified personal identity? | |

**Anti-inflation for b**: Formulaic consistency across all testimonials is a strong signal of fabrication. 3+ testimonials all following the exact same grammatical structure → N=0.

### 10. Product Visualization (0-10) ★ NEW

Does the first screen show what the product actually looks like or does?

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Product screenshot, UI mockup, or app interface visible on first screen? | |
| b | Screenshot/mockup shows realistic product state (not empty/placeholder content)? | |
| c | Video demo, GIF, or interactive preview available on first screen or within one click? | |
| d | Visual clearly communicates core functionality (not decorative illustration or abstract art)? | |
| e | Visual matches what the user will actually see after signing up (not aspirational/conceptual art)? | |

**Score cap**: If there is ZERO product visualization of any kind on the first screen → max 2 (partial credit possible for good illustrations that hint at functionality).

**Why this matters**: For SaaS/tools, "show don't tell" is the most effective trust-builder. Users who can see the product before signing up convert 30-50% better than those who can't. A 30-second GIF demo is worth more than 500 words of feature description.

**How to check**: Use `product_visualization` from data.json. Look for `has_screenshot`, `has_video`, `has_gif`, `has_interactive_demo`.

---

## Category D: Conversion Readiness (20 points) ★ NEW

### 11. Pricing Visibility (0-10) ★ NEW

Is pricing information transparent and accessible?

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | Pricing mentioned somewhere on the page (not necessarily first screen — anywhere counts)? | |
| b | Specific price points visible (not just "affordable" or "contact us")? | |
| c | Free tier / freemium clearly distinguished from paid plans? | |
| d | Pricing page accessible via primary navigation (within 1 click)? | |
| e | No "contact sales" as the ONLY pricing path (for tools/SaaS targeting individuals or small teams)? | |

**Score cap**: If navigation has a "Pricing" link but clicking it shows no actual prices on the page → max 3. Setting a pricing expectation and then breaking it is WORSE than not having a pricing link at all.

**Context**: For 🟢 Established brands, low pricing visibility is more acceptable (users trust the brand enough to explore). For 🔴 Unknown brands, hidden pricing = "this must be expensive" assumption → high bounce.

**How to check**: Use `pricing_signals` from data.json (`has_price_on_page`, `has_pricing_section`, `price_mentions`). Cross-reference with `brand_signals.has_pricing_page` for nav link presence.

### 12. CTA Path Consistency (0-10) ★ NEW

Do all CTAs lead to a coherent conversion flow?

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | All sign-up/start CTAs point to the same destination (not mixing /signin vs /signup, or different landing paths)? | |
| b | CTA text matches what happens after clicking (e.g., "Start Free" doesn't lead to a pricing page)? | |
| c | No broken links or dead ends from first-screen CTAs? | |
| d | Secondary CTAs (e.g., "See Demo", "How it works") lead to meaningful content (not just an anchor scroll to a generic section)? | |
| e | Navigation CTA (e.g., header "Try Free") and Hero CTA use consistent language and point to the same destination? | |

**How to check**: Compare `href` values in `cta_buttons` from data.json. Flag mismatched paths (e.g., one CTA going to `/auth/signin` while another goes to `/auth/signup`). Also compare nav CTA vs hero CTA text consistency.

---

## Category E: Technical Performance (20 points)

### 13. Mobile Responsiveness (0-10)

Evaluate from the mobile screenshot:

| # | Check | Y=2 / N=0 |
|---|-------|-----------|
| a | CTA button visible on mobile first screen without scrolling? | |
| b | Text is readable (no text smaller than ~14px equivalent)? | |
| c | No horizontal overflow or elements cut off? | |
| d | Tap targets are adequately sized and spaced? | |
| e | Layout adapts properly (not just a shrunken desktop view)? | |

### 14. First-Screen Copy Readability (0-10)

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
| A. Value Communication | #1 + #2 + #3 + #4 | 40 |
| B. Action Guidance | #5 + #6 + #7 | 30 |
| C. Trust & Proof | #8 + #9 + #10 | 30 |
| D. Conversion Readiness | #11 + #12 | 20 |
| E. Technical Performance | #13 + #14 | 20 |
| **Total** | | **140** |

**Final score** = (raw total / 140) × 100, rounded to nearest integer.

## Priority Rules for Recommendations

When generating Top 3 actions, prioritize by expected ROI:

1. **Add product visualization** (if #10 < 5) — highest impact for SaaS, shows what user gets
2. **Headline rewrite** (if #1 < 7) — highest copy ROI, zero cost to change
3. **CTA improvement** (if #5 or #6 < 7) — directly affects conversion
4. **Add trust anchor** (if #8 < 5) — moderate effort, high impact for unknown brands
5. **Show pricing** (if #11 < 5) — removes key objection for cold traffic
6. **Remove clutter** (if #4 < 7) — quick win, just delete things
7. **Anchor target audience** (if #3 < 5) — copy change, helps visitor self-identify
8. **Fix CTA paths** (if #12 < 7) — technical fix, prevents conversion leakage
9. **Mobile fix** (if #13 < 7) — technical work, but 60%+ traffic is mobile
10. **Reduce commitment** (if #7 < 7) — copy change, easy to implement

---

## Score Interpretation Matrix (REQUIRED)

Raw scores are objective. But their **meaning** depends on brand maturity. You MUST apply this matrix when writing the "诊断解读" section.

### How brand maturity affects each category

| Category | 🟢 Established brand | 🟡 Growing brand | 🔴 Unknown brand |
|----------|----------------------|-------------------|-------------------|
| A. Value Communication (#1-4) | Low score is a miss but survivable — visitors have context | Moderate impact — some visitors know you, some don't | **CRITICAL** — cold traffic has zero context, every word counts |
| B. Action Guidance (#5-7) | Low score matters less if brand drives direct-URL traffic | Important — mixed traffic needs clear next steps | **CRITICAL** — user must know what to do within 5 seconds |
| C. Trust & Proof (#8-10) | Low score is acceptable — brand IS the trust | Important — niche recognition helps but isn't enough | **MAKE OR BREAK** — zero trust = zero conversion for cold traffic |
| D. Conversion Readiness (#11-12) | Low score is tolerable — users will explore on their own | Important — users need a clear path | **CRITICAL** — hidden pricing or broken CTA paths = instant bounce for cold traffic |
| E. Technical (#13-14) | Same impact regardless of brand | Same impact regardless of brand | Same impact regardless of brand |

### Interpretation rules (follow exactly)

1. **If brand is 🟢 Established AND trust scores (#8+#9+#10) are low**:
   → Write: "该页面信任项得分低，但作为知名品牌，大部分访客已通过口碑/搜索了解产品。信任缺失对实际转化的影响远小于分数显示的程度。"
   → Then ADD: "但如果你是独立开发者，这个分数意味着灾难——冷流量没有品牌认知做缓冲，0分信任 = 0转化。"

2. **If brand is 🟢 Established AND CTA/commitment scores (#5-7) are low**:
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
- Trust 2/30 → "Linear 品牌知名度极高，首屏不放信任元素不影响核心用户转化。但独立开发者千万不要学——你的用户不认识你。"
- CTA 14/30 → "Linear 用户大多通过推荐/搜索直接到达，弱CTA影响有限。但对冷流量驱动的新产品，首屏必须有醒目的 Hero CTA。"
- Technical 20/20 → "移动端适配和排版是标杆级别，任何页面都值得学习。"
