---
name: Advisor sign out
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:10Z
default_role: advisor
---

## Steps

Tap on the "Settings" button
Tap on the "Sign out" button
Verify the advisor email field is visible

## Code

```python
def method_advisor_sign_out(page):
    """Advisor sign out — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on the "Settings" button
    # No stable locator was ever captured for 'Settings' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Settings')

    # Step 2: Tap on the "Sign out" button
    # No stable locator was ever captured for 'Sign out' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Sign out')

    # Step 3: Verify the advisor email field is visible
    # No stable locator was ever captured for 'the advisor email field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: the advisor email field')
```
