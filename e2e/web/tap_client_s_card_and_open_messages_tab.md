---
name: Tap client's card and open Messages tab
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:30Z
default_role: advisor
---

## Steps

Tap on "testAutuserfBM"
Tap on the "Messages" tab


## Code

```python
def method_tap_client_s_card_and_open_messages_tab(page):
    """Tap client's card and open Messages tab — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on "testAutuserfBM"
    page.click('[placeholder="Search client nickname, name or ID"]')

    # Step 2: Tap on the "Messages" tab
    page.click("xpath=(//button[normalize-space(text())='Message'])[1]")
```
