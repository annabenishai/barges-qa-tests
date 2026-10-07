---
name: User connects with advisor via communication feed
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:57Z
default_role: user
---

## Steps

Tap on the Connect now button
Verify "Hubert Blaine" is visible
Assert that "Chat" button is displayed and not contains disabled attribute
Tap on the Chat button 


## Code

```python
def method_user_connects_with_advisor_via_communication_feed(page):
    """User connects with advisor via communication feed — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on the Connect now button
    page.click('[data-testid="ActivityFeedHeader__connect"]')

    # Step 2: Verify "Hubert Blaine" is visible
    # No stable locator was ever captured for 'Hubert Blaine' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Hubert Blaine')

    # Step 3: Tap on the Chat button
    page.click('[data-testid="AdvisorProfileCard__live-mode-button-chat"]')
```
