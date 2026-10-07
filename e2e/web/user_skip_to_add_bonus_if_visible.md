---
name: User skip to add bonus if visible
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:20Z
default_role: user
---

## Steps

Tap the "Skip" button on bonus popup if visible

## Code

```python
def method_user_skip_to_add_bonus_if_visible(page):
    """User skip to add bonus if visible — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap the "Skip" button on bonus popup if visible
    try:
        page.wait_for_selector('[data-testid="AdvisorBonusScreen__skip-btn"]', state='visible', timeout=3000)
        page.click('[data-testid="AdvisorBonusScreen__skip-btn"]')
    except TimeoutError:
        pass  # optional tap — only fires if the element is present
```
