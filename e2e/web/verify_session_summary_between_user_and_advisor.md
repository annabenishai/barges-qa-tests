---
name: Verify session summary between user and advisor
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:34Z
default_role: both
---

## Steps

[user only] Assert "Total duration value" matches between user and advisor as duration
[advisor only] Assert "Total duration value" matches between user and advisor as duration
[user only] Assert "Summary screen advisor's fee per minute value" matches between user and advisor as rate
[advisor only] Assert "Your rate value" matches between user and advisor as rate
[user only] Assert "summary screen total value" matches between user and advisor as total
[advisor only] Assert "Total credit charged value" matches between user and advisor as total
[advisor only] Extract "Total earned value" as advisor_total_earned
Assert advisor_total_earned equals (total_advisor - duration_advisor * 0.36) * 0.36
Assert total_user equals duration_user * rate_user
[user only] Tap the "Continue" button
[advisor only] Tap the "Close chat" button

## Code

```python
def method_verify_session_summary_between_user_and_advisor(page):
    """Verify session summary between user and advisor — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: [user only] Assert "Total duration value" matches between user and advisor as duration
    # assert_cross_role_text_equal depends on the paired role's own reading, which isn't reproduced above either

    # Step 2: [advisor only] Assert "Total duration value" matches between user and advisor as duration
    # assert_cross_role_text_equal depends on the paired role's own reading, which isn't reproduced above either

    # Step 3: [user only] Assert "Summary screen advisor's fee per minute value" matches between user and advisor as rate
    # assert_cross_role_text_equal depends on the paired role's own reading, which isn't reproduced above either

    # Step 4: [advisor only] Assert "Your rate value" matches between user and advisor as rate
    # assert_cross_role_text_equal depends on the paired role's own reading, which isn't reproduced above either

    # Step 5: [user only] Assert "summary screen total value" matches between user and advisor as total
    # assert_cross_role_text_equal depends on the paired role's own reading, which isn't reproduced above either

    # Step 6: [advisor only] Assert "Total credit charged value" matches between user and advisor as total
    # assert_cross_role_text_equal depends on the paired role's own reading, which isn't reproduced above either

    # Step 7: [advisor only] Extract "Total earned value" as advisor_total_earned
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 8: Assert advisor_total_earned equals (total_advisor - duration_advisor * 0.36) * 0.36
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 9: Assert total_user equals duration_user * rate_user
    # assert_compare depends on an extract_text capture, which isn't reproduced above either

    # Step 10: [user only] Tap the "Continue" button
    # No stable locator was ever captured for 'Continue' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Continue')

    # Step 11: [advisor only] Tap the "Close chat" button
    page.click("xpath=//button[normalize-space(text())='Close Chat']")
```
