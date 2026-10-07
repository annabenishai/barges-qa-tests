---
name: Verify new user in advisor's client feed
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:07Z
default_role: advisor
---

## Steps

Tap on "Search" field
Type "Automation test" into 'Search' field
Verify "Automation test" is visible

## Code

```python
def method_verify_new_user_in_advisor_s_client_feed(page):
    """Verify new user in advisor's client feed — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on "Search" field
    # No stable locator was ever captured for 'Search' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Search')

    # Step 2: Type "Automation test" into 'Search' field
    # No stable locator was ever captured for 'Search' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Search', 'Automation test')

    # Step 3: Verify "Automation test" is visible
    # No stable locator was ever captured for 'Automation test' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Automation test')
```
