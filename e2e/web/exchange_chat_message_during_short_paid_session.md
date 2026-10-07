---
name: Exchange chat message during short paid session
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:48:43Z
default_role: session
---

## Steps

Wait 20 seconds
[advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
[advisor only] Tap the 'Send' button
[user only] Type "{{fake_message_long}}" into the 'Your message...' field
[user only] Tap the 'Send msg' button
[user only] Tap the 'Hang up' button


## Code

```python
def method_exchange_chat_message_during_short_paid_session(page):
    """Exchange chat message during short paid session — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Wait 20 seconds
    page.wait_for_timeout(20000)

    # Step 2: [advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
    page.fill('[placeholder="Say hello to your client"]', 'Drug above us 648&=!@ 🙏')

    # Step 3: [advisor only] Tap the 'Send' button
    page.click('div.send-button')

    # Step 4: [user only] Type "{{fake_message_long}}" into the 'Your message...' field
    # No stable locator was ever captured for 'Your message...' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Your message...', 'Fact win bit personal positive against. Decade energy instead above board outside. My any perhaps goal someone why law. Might attack national cup. 356454)>+>. 😍😂😢')

    # Step 5: [user only] Tap the 'Send msg' button
    # No stable locator was ever captured for 'Send msg' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Send msg')

    # Step 6: [user only] Tap the 'Hang up' button
    # No stable locator was ever captured for 'Hang up' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Hang up')
```
