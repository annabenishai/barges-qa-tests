---
name: Turn on advisor availability
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:16Z
default_role: advisor
---

## Steps

Tap the AWAY button
Tap the AVAILABLE button
Tap the Got it button if present on the Standard mode activated popup
Verify "Available" is visible

## Code

```python
def method_turn_on_advisor_availability(page):
    """Turn on advisor availability — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap the AWAY button
    page.click("xpath=(//div[normalize-space(text())='Away'])[1]")

    # Step 2: Tap the AVAILABLE button
    page.click('div.status.available')

    # Step 3: Tap the Got it button if present on the Standard mode activated popup
    try:
        page.wait_for_selector('button.primary', state='visible', timeout=3000)
        page.click('button.primary')
    except Exception:
        pass  # optional tap — only fires if the element is present

    # Step 4: Verify "Available" is visible
    # No stable locator was ever captured for 'Available' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Available')
```
