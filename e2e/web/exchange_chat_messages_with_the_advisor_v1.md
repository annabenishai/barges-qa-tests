---
name: Exchange chat messages with the advisor_v1
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:31Z
default_role: session
---

## Steps

Wait 10 seconds
[advisor only] Type "{{fake_message_long}}" into the 'Say hello to your client' field
[advisor only] Extract "Say hello to your client" as advisor_message_1
[advisor only] Tap the 'Send' button
[advisor only] Assert "{{api:advisor_message_1}}" is visible
[user only] Assert "{{api:advisor_message_1}}" is visible
[user only] Type "{{fake_message_short}}" into the 'Your message...' field
[user only] Extract "Your message..." as user_message_1
[user only] Tap the 'Send msg' button
[user only] Assert "{{api:user_message_1}}" is visible
[advisor only] Assert "{{api:user_message_1}}" is visible
[advisor only] Type "{{fake_message_short}}" into the 'Say hello to your client' field
[advisor only] Extract "Say hello to your client" as advisor_message_2
[advisor only] Tap the 'Send' button
[advisor only] Assert "{{api:advisor_message_2}}" is visible
[user only] Assert "{{api:advisor_message_2}}" is visible
[user only] Type "{{fake_message_short}}" into the 'Your message...' field
[user only] Extract "Your message..." as user_message_2
[user only] Tap the 'Send msg' button
[user only] Assert "{{api:user_message_2}}" is visible
[advisor only] Assert "{{api:user_message_2}}" is visible

## Code

```python
# No generated code cached yet for exchange_chat_messages_with_the_advisor_v1 (W/playwright_python).
```
