---
name: Exchange chat messages during long paid session
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:07Z
default_role: both
---

## Steps

Wait 20 seconds
[advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
[advisor only] Tap the 'Send' button
Wait 70 seconds
[user only] Type "{{fake_message_long}}" into the 'Your message...' field
[user only] Tap the 'Send msg' button
Wait 70 seconds
[advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
[advisor only] Tap the 'Send' button
Wait 70 seconds
[user only] Type "{{fake_message_long}}" into the 'Your message...' field
[user only] Tap the 'Send msg' button
Wait 70 seconds
[user only] Tap the 'Hang up' button


## Code

```python
def method_exchange_chat_messages_during_paid_session(page):
    """Exchange chat messages during paid session — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Wait 20 seconds
    page.wait_for_timeout(20000)

    # Step 2: [advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
    page.fill('[placeholder="Say hello to your client"]', 'Class school sometimes condition him note hear owner 41~]). 😢😢')

    # Step 3: [advisor only] Tap the 'Send' button
    page.click('div.send-button')

    # Step 4: Wait 70 seconds
    page.wait_for_timeout(70000)

    # Step 5: [user only] Type "{{fake_message_long}}" into the 'Your message...' field
    # No stable locator was ever captured for 'Your message...' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Your message...', 'Management season partner begin hundred military. Yet back executive both. Each represent need several look pull. Drive appear check together. 899385&^<$ 🤔✨')

    # Step 6: [user only] Tap the 'Send msg' button
    # No stable locator was ever captured for 'Send msg' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Send msg')

    # Step 7: Wait 70 seconds
    page.wait_for_timeout(70000)

    # Step 8: [advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
    page.fill('[placeholder="Say hello to your client"]', 'Card chair chance wish reduce group 2259$* 🤔👍')

    # Step 9: [advisor only] Tap the 'Send' button
    page.click('div.send-button')

    # Step 10: Wait 70 seconds
    page.wait_for_timeout(70000)

    # Step 11: [user only] Type "{{fake_message_long}}" into the 'Your message...' field
    # No stable locator was ever captured for 'Your message...' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Your message...', 'Poor huge parent. Real hear worry reflect chance road decide. Throughout still fight. More ball finish a money age interesting skin. 941[^) 🔮🔮')

    # Step 12: [user only] Tap the 'Send msg' button
    # No stable locator was ever captured for 'Send msg' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Send msg')

    # Step 13: Wait 70 seconds
    page.wait_for_timeout(70000)

    # Step 14: [user only] Tap the 'Hang up' button
    # No stable locator was ever captured for 'Hang up' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Hang up')
```
