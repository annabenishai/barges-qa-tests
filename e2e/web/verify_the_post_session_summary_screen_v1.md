---
name: Verify the post-session summary screen_v1
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:48:57Z
default_role: both
---

## Steps

[user only] Extract "Total duration value" as user_duration
[advisor only] Extract "Total duration value" as advisor_duration
[user only] Extract "Summary screen advisor's fee per minute value" as user_rate
[advisor only] Extract "Your rate value" as advisor_rate
[user only] Extract "summary screen total value" as user_total
[advisor only] Extract "Total credit charged value" as advisor_total_credit_charged
[advisor only] Extract "Total earned value" as advisor_total_earned
Assert advisor_total_earned equals (advisor_total_credit_charged - advisor_duration * 0.36) * 0.36
Assert user_duration equals advisor_duration
Assert user_rate equals advisor_rate
Assert user_total equals advisor_total_credit_charged
Assert user_total equals user_duration * user_rate
[user only] Tap the "Continue" button
[advisor only] Tap the "Close chat" button

## Code

```python
# No generated code cached yet for verify_the_post_session_summary_screen_v1 (W/playwright_python).
```
