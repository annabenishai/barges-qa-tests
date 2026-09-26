---
name: Verify session summary between user and advisor
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-09-26T11:44:17Z
---

## Steps

[user only] Extract "summary screen large numbers value 0" as user_duration
[advisor only] Extract "Total duration value" as advisor_duration
[user only] Extract "summary screen large numbers value 1" as user_rate
[advisor only] Extract "Your rate value" as advisor_rate
[user only] Extract "summary screen total value" as user_total
[advisor only] Extract "Total credit charged value" as advisor_total_credit_charged
[advisor only] Extract "Total earned value" as advisor_total_earned
Assert advisor_total_earned equals (advisor_total_credit_charged - advisor_duration * 0.36) * 0.36
Assert user_duration equals advisor_duration
Assert user_rate equals advisor_rate
Assert user_total equals advisor_total_credit_charged
Assert user_total equals user_duration * user_rate
[user only] Tap on "Continue" button
[advisor only] Tap on "Close chat" button

## Code

```python
def method_verify_session_summary_between_user_and_advisor(page):
    """Verify session summary between user and advisor — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: [user only] Extract "Total duration value" as user_duration
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 2: [advisor only] Extract "Total duration value" as advisor_duration
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 3: [user only] Extract "Advisor's fee per minute value" as user_rate
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 4: [advisor only] Extract "Your rate value" as advisor_rate
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 5: [user only] Extract "Total value" as user_total
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 6: [advisor only] Extract "Total credit charged value" as advisor_total_credit_charged
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 7: [advisor only] Extract "Total earned value" as advisor_total_earned
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 8: Assert advisor_total_earned equals (advisor_total_credit_charged - advisor_duration * 0.36) * 0.36
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 9: Assert user_duration equals advisor_duration
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 10: Assert user_rate equals advisor_rate
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 11: Assert user_total equals advisor_total_credit_charged
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 12: Assert user_total equals user_duration * user_rate
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 13: [user only] Tap on "Continue" button
    # No stable locator was ever captured for 'Continue' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Continue')

    # Step 14: [advisor only] Tap on "Close chat" button
    page.click("xpath=//button[normalize-space(text())='Close Chat']")
```
