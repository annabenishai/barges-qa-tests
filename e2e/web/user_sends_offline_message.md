---
name: User sends offline message
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:21Z
default_role: user
---

## Steps

Extract "Send the advisor up to" as messages_before
Type "{{fake_message_short}}" into the 'Your message' field
Extract "Your message" as sent_message_text
Tap the 'Send' button
Assert "{{api:sent_message_text}}" is visible
Extract "Send the advisor up to" as messages_after
Assert messages_after equals messages_before - 1


## Code

```python
def method_user_sends_offline_message(page):
    """User sends offline message — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Extract "Send the advisor up to" as messages_before
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 2: Type "{{fake_message_short}}" into the 'Your message' field
    page.fill('[data-testid="ActivityComposer__textarea"]', 'Guess effort 238]$ 🙌')

    # Step 3: Extract "Your message" as sent_message_text
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 4: Tap the 'Send' button
    page.click('[data-testid="ActivityComposer__send-btn"]')

    # Step 5: Assert "{{api:sent_message_text}}" is visible
    # No stable locator was ever captured for '{{api:sent_message_text}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{api:sent_message_text}}')

    # Step 6: Extract "Send the advisor up to" as messages_after
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 7: Assert messages_after equals messages_before - 1
    # assert_compare depends on an extract_text capture, which isn't reproduced above either
```
