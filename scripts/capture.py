#!/usr/bin/env python3
"""
Landing Page Doctor — Capture Script
Captures desktop + mobile screenshots and extracts first-screen data from a URL.

Usage:
    python capture.py <url> [--output /tmp/lp-doctor] [--timeout 30000]

Outputs:
    <output>/desktop.png   — Desktop viewport (1440x900)
    <output>/mobile.png    — Mobile viewport (375x812)
    <output>/data.json     — Extracted page data
"""

import argparse
import json
import os
import sys
import time


def main():
    parser = argparse.ArgumentParser(description="Capture Landing Page screenshots and data")
    parser.add_argument("url", help="URL to analyze")
    parser.add_argument("--output", default="/tmp/lp-doctor", help="Output directory (default: /tmp/lp-doctor)")
    parser.add_argument("--timeout", type=int, default=30000, help="Page load timeout in ms (default: 30000)")
    args = parser.parse_args()

    url = args.url
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    output_dir = args.output
    os.makedirs(output_dir, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Installing playwright...")
        os.system(f"{sys.executable} -m pip install playwright -q")
        os.system(f"{sys.executable} -m playwright install chromium")
        from playwright.sync_api import sync_playwright

    results = {
        "url": url,
        "captured_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # --- Desktop capture ---
        print("[1/2] Capturing desktop view (1440x900)...")
        desktop_ctx = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
        )
        desktop_page = desktop_ctx.new_page()

        start_time = time.time()
        try:
            desktop_page.goto(url, timeout=args.timeout, wait_until="networkidle")
        except Exception:
            # Fallback: some pages never reach networkidle
            try:
                desktop_page.goto(url, timeout=args.timeout, wait_until="domcontentloaded")
                desktop_page.wait_for_timeout(3000)
            except Exception as e:
                print(f"Error loading page: {e}")
                browser.close()
                sys.exit(1)

        load_time = round(time.time() - start_time, 2)
        results["load_time_seconds"] = load_time

        # Dismiss common cookie/consent banners
        desktop_page.wait_for_timeout(1500)
        try:
            for selector in [
                "button:has-text('Accept')", "button:has-text('OK')",
                "button:has-text('Got it')", "button:has-text('I agree')",
                "button:has-text('接受')", "button:has-text('同意')",
                "[class*='cookie'] button", "[class*='consent'] button",
            ]:
                btn = desktop_page.locator(selector).first
                if btn.is_visible(timeout=500):
                    btn.click()
                    desktop_page.wait_for_timeout(500)
                    break
        except Exception:
            pass

        desktop_page.screenshot(path=os.path.join(output_dir, "desktop.png"))

        # Extract page data from desktop view
        data = desktop_page.evaluate("""() => {
            const result = {};

            // Page title
            result.page_title = document.title || '';

            // Meta description
            const metaDesc = document.querySelector('meta[name="description"]');
            result.meta_description = metaDesc ? metaDesc.content : '';

            // First screen headline (largest text in viewport)
            const headings = Array.from(document.querySelectorAll('h1, h2, [class*="hero"] *, [class*="title"], [class*="heading"]'));
            const viewportHeight = window.innerHeight;
            const firstScreenHeadings = headings
                .filter(el => {
                    const rect = el.getBoundingClientRect();
                    return rect.top < viewportHeight && rect.height > 0;
                })
                .map(el => ({
                    tag: el.tagName.toLowerCase(),
                    text: el.innerText.trim(),
                    fontSize: parseFloat(window.getComputedStyle(el).fontSize),
                }))
                .filter(h => h.text.length > 0)
                .sort((a, b) => b.fontSize - a.fontSize);
            result.first_screen_headings = firstScreenHeadings.slice(0, 5);

            // Nav items count
            const navItems = document.querySelectorAll('nav a, nav button, header nav li');
            result.nav_items_count = navItems.length;

            // CTA buttons in first screen
            const allButtons = Array.from(document.querySelectorAll('a, button'));
            const ctaKeywords = /sign|start|try|free|demo|begin|get|create|注册|开始|试用|免费|体验|立即/i;
            const ctaButtons = allButtons
                .filter(el => {
                    const rect = el.getBoundingClientRect();
                    if (rect.top >= viewportHeight || rect.height === 0) return false;
                    const text = el.innerText.trim();
                    const style = window.getComputedStyle(el);
                    const isCTA = ctaKeywords.test(text) ||
                        style.backgroundColor !== 'rgba(0, 0, 0, 0)' && el.tagName === 'A' ||
                        el.tagName === 'BUTTON';
                    return isCTA && text.length > 0 && text.length < 50;
                })
                .map(el => {
                    const style = window.getComputedStyle(el);
                    const rect = el.getBoundingClientRect();
                    return {
                        text: el.innerText.trim(),
                        tag: el.tagName.toLowerCase(),
                        bgColor: style.backgroundColor,
                        color: style.color,
                        fontSize: parseFloat(style.fontSize),
                        inTopHalf: rect.top < viewportHeight / 2,
                        width: Math.round(rect.width),
                        height: Math.round(rect.height),
                    };
                });
            result.cta_buttons = ctaButtons.slice(0, 10);

            // First screen text content (skip script/style/noscript/template tags)
            const invisibleTags = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'SVG', 'IFRAME']);
            const walker = document.createTreeWalker(
                document.body, NodeFilter.SHOW_TEXT, {
                    acceptNode: (node) => {
                        const parent = node.parentElement;
                        if (!parent) return NodeFilter.FILTER_REJECT;
                        // Skip text inside invisible/non-content elements
                        let el = parent;
                        while (el && el !== document.body) {
                            if (invisibleTags.has(el.tagName)) return NodeFilter.FILTER_REJECT;
                            if (el.hidden || window.getComputedStyle(el).display === 'none') return NodeFilter.FILTER_REJECT;
                            el = el.parentElement;
                        }
                        const rect = parent.getBoundingClientRect();
                        if (!rect || rect.top >= viewportHeight || rect.height === 0) return NodeFilter.FILTER_REJECT;
                        const text = node.textContent.trim();
                        if (text.length < 2) return NodeFilter.FILTER_REJECT;
                        return NodeFilter.FILTER_ACCEPT;
                    }
                }
            );
            const texts = [];
            while (walker.nextNode()) {
                texts.push(walker.currentNode.textContent.trim());
            }
            result.first_screen_text = texts.join(' ').substring(0, 2000);

            // Images in first screen
            const images = Array.from(document.querySelectorAll('img, video, svg'))
                .filter(el => {
                    const rect = el.getBoundingClientRect();
                    return rect.top < viewportHeight && rect.height > 20;
                })
                .map(el => ({
                    tag: el.tagName.toLowerCase(),
                    alt: el.alt || '',
                    width: Math.round(el.getBoundingClientRect().width),
                    height: Math.round(el.getBoundingClientRect().height),
                    src: el.src ? el.src.substring(0, 200) : '',
                }));
            result.first_screen_images = images;

            // Trust elements detection (first screen only)
            const firstScreenText = texts.join(' ');
            const trustPatterns = {
                user_count: /(\d[\d,]*\+?\s*(用户|开发者|团队|企业|users|teams|developers|customers|companies))/i,
                stars: /(github|★|⭐|stars?)/i,
                product_hunt: /product\s*hunt/i,
                testimonial: /"|"|「|」|testimonial|review/i,
                trusted_by: /(trusted\s+by|used\s+by|loved\s+by|chosen\s+by|信赖|选择|使用)/i,
                awards: /(award|winner|#\d+\s+on|排名|获奖|best\s+of)/i,
                press: /(featured\s+in|as\s+seen\s+in|报道|媒体|techcrunch|forbes|wired|verge)/i,
                security: /(soc\s*2|gdpr|hipaa|iso\s*27001|ssl|encrypted|安全认证)/i,
                logos: document.querySelectorAll('[class*="logo"] img, [class*="client"] img, [class*="partner"] img, [class*="trust"] img, [class*="customer"] img, [class*="brand"] img').length,
            };
            result.trust_signals = {
                has_user_count: trustPatterns.user_count.test(firstScreenText),
                has_github_stars: trustPatterns.stars.test(firstScreenText),
                has_product_hunt: trustPatterns.product_hunt.test(firstScreenText),
                has_testimonials: trustPatterns.testimonial.test(firstScreenText),
                has_trusted_by: trustPatterns.trusted_by.test(firstScreenText),
                has_awards: trustPatterns.awards.test(firstScreenText),
                has_press_mentions: trustPatterns.press.test(firstScreenText),
                has_security_badges: trustPatterns.security.test(firstScreenText),
                logo_count: trustPatterns.logos,
            };

            // Brand maturity signals
            const allNavText = Array.from(document.querySelectorAll('nav a, header a')).map(a => a.innerText.trim()).join(' ');
            result.brand_signals = {
                has_pricing_page: /pricing|定价|价格/i.test(allNavText),
                has_docs: /docs|documentation|文档|api/i.test(allNavText),
                has_blog: /blog|博客/i.test(allNavText),
                has_careers: /careers|jobs|招聘/i.test(allNavText),
                has_multiple_products: /products|solutions|平台|产品/i.test(allNavText),
                nav_complexity: navItems.length,
            };

            // Content blocks count in first screen
            const blocks = Array.from(document.querySelectorAll('section, div, article'))
                .filter(el => {
                    const rect = el.getBoundingClientRect();
                    return rect.top < viewportHeight && rect.height > 50;
                    // Only count direct children type blocks
                });
            result.first_screen_block_count = Math.min(blocks.length, 20);

            return result;
        }""")

        results.update(data)
        desktop_ctx.close()

        # --- Mobile capture ---
        print("[2/2] Capturing mobile view (375x812)...")
        mobile_ctx = browser.new_context(
            viewport={"width": 375, "height": 812},
            device_scale_factor=3,
            is_mobile=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        )
        mobile_page = mobile_ctx.new_page()

        try:
            mobile_page.goto(url, timeout=args.timeout, wait_until="networkidle")
        except Exception:
            try:
                mobile_page.goto(url, timeout=args.timeout, wait_until="domcontentloaded")
                mobile_page.wait_for_timeout(3000)
            except Exception:
                pass

        mobile_page.wait_for_timeout(1500)

        # Dismiss cookie banners on mobile too
        try:
            for selector in [
                "button:has-text('Accept')", "button:has-text('OK')",
                "button:has-text('接受')", "button:has-text('同意')",
            ]:
                btn = mobile_page.locator(selector).first
                if btn.is_visible(timeout=500):
                    btn.click()
                    mobile_page.wait_for_timeout(500)
                    break
        except Exception:
            pass

        mobile_page.screenshot(path=os.path.join(output_dir, "mobile.png"))

        # Check mobile-specific issues
        mobile_data = mobile_page.evaluate("""() => {
            const viewportHeight = window.innerHeight;
            const viewportWidth = window.innerWidth;

            // Check if CTA is visible without scrolling
            const buttons = Array.from(document.querySelectorAll('a, button'));
            const ctaKeywords = /sign|start|try|free|demo|begin|get|create|注册|开始|试用|免费|体验|立即/i;
            const mobileCTA = buttons.find(el => {
                const rect = el.getBoundingClientRect();
                return rect.top < viewportHeight && ctaKeywords.test(el.innerText);
            });

            // Check for horizontal overflow
            const hasOverflow = document.body.scrollWidth > viewportWidth + 5;

            return {
                mobile_cta_visible: !!mobileCTA,
                mobile_cta_text: mobileCTA ? mobileCTA.innerText.trim() : null,
                has_horizontal_overflow: hasOverflow,
                body_scroll_width: document.body.scrollWidth,
                viewport_width: viewportWidth,
            };
        }""")

        results["mobile"] = mobile_data

        mobile_ctx.close()
        browser.close()

    # Save results
    output_path = os.path.join(output_dir, "data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Results saved to {output_dir}/")
    print(f"  - desktop.png")
    print(f"  - mobile.png")
    print(f"  - data.json")
    print(f"\nPage load time: {results.get('load_time_seconds', 'N/A')}s")
    print(f"Nav items: {results.get('nav_items_count', 'N/A')}")
    print(f"CTA buttons found: {len(results.get('cta_buttons', []))}")
    print(f"Trust signals: {json.dumps(results.get('trust_signals', {}), ensure_ascii=False)}")


if __name__ == "__main__":
    main()
