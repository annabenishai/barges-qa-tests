---
name: Search client and verify correct card shown
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:02Z
default_role: advisor
---

## Steps

Type "testAutuserfBM" into the 'Search client nickname, name or ID' field
Assert "testAutuserfBM" is visible



## Code

```python
def method_search_client_and_verify_correct_card_shown(page):
    """Search client and verify correct card shown — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Type "testAutuserfBM" into the 'Search client nickname, name or ID' field
    page.fill('[placeholder="Search client nickname, name or ID"]', 'testAutuserfBM')

    # Step 2: Assert "testAutuserfBM" is visible
    # No stable locator was ever captured for 'testAutuserfBM' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: testAutuserfBM')
```
