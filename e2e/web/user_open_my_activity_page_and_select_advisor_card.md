---
name: User open my activity page and select advisor card
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:00Z
default_role: user
---

## Steps

Tap on the Profile menu button
Tap on the My activity button
Tap on the order card for "Hubert Blaine"
Verify "Hubert Blaine" is visible

## Code

```python
def method_user_open_my_activity_page_and_select_advisor_card(page):
    """User open my activity page and select advisor card — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on the Profile menu button
    page.click('[data-testid="HeaderAuthSection__profile-menu-btn"]')

    # Step 2: Tap on the My activity button
    page.click('[data-testid="HeaderAuthSection__my-activity-link"]')

    # Step 3: Tap on the order card for "Hubert Blaine"
    page.click('[data-testid="OrderRow__link-4192"]')

    # Step 4: Verify "Hubert Blaine" is visible
    page.wait_for_selector('[data-testid="OrderRow__link-4192"]', state='visible', timeout=15000)
```
