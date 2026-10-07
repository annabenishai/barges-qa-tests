---
name: Verify user's message shown on advisor side
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:16Z
default_role: advisor
---

## Steps

Assert "{{api:sent_message_text}}" is visible


## Code

```python
def method_verify_user_s_message_shown_on_advisor_side(page):
    """Verify user's message shown on advisor side — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Assert "{{api:sent_message_text}}" is visible
    # No stable locator was ever captured for '{{api:sent_message_text}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{api:sent_message_text}}')
```
