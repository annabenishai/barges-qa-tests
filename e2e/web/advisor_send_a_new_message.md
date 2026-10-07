---
name: Advisor send a new message
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:04Z
default_role: advisor
---

## Steps

Type "{{fake_message_short}}" into the 'Message your client' field
Extract "Message your client" as sent_message_text
Tap the Send button
Assert "{{api:sent_message_text}}" is visible


## Code

```python
def method_advisor_send_a_new_message(page):
    """Advisor send a new message — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Type "{{fake_message_short}}" into the 'Message your client' field
    page.fill('div.notranslate', 'None ok help energy begin 02<,/ 😊')

    # Step 2: Extract "Message your client" as sent_message_text
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 3: Tap the Send button
    page.click('button.client-card-messages__send-button')

    # Step 4: Assert "{{api:sent_message_text}}" is visible
    # No stable locator was ever captured for '{{api:sent_message_text}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{api:sent_message_text}}')
```
