---
name: User selects remaining balance and start session
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:20Z
default_role: user
---

## Steps

Swipe left to "Tap to use your remaining balance"
Tap on "Tap to use your remaining balance"
Assert "Hang up" button displayed


## Code

```python
def method_user_selects_remaining_balance_and_start_session(page):
    """User selects remaining balance and start session — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Swipe left to "Tap to use your remaining balance"
    for _attempt in range(6):
        if page.locator('[data-testid="DurationItem__balance"]').count() > 0:
            break
        page.mouse.wheel(-page.viewport_size['width'] * 0.1, 0)
    else:
        raise Exception("'Tap to use your remaining balance' not found after 6 swipes left")

    # Step 2: Tap on "Tap to use your remaining balance"
    page.click('[data-testid="DurationItem__balance"]')
```
