---
name: Advisor accept call
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:48:40Z
default_role: advisor
---

## Steps

Tap on "ANSWER CHAT" button

## Code

```python
def method_advisor_accept_call(page):
    """Advisor accept call — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on "ANSWER CHAT" button
    page.click('button.incoming-chat-popup_answer')
```
