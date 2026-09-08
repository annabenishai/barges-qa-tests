---
name: Add payment method credit card and start live session
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-09-08T19:15:54Z
---

## Steps

Tap on "Add a new credit or debit card"
Wait 10 seconds
Type "Automation test" into the Cardholder name field
Type "{{fake_card_number}}" into the Card number field
Type "{{fake_card_expiry}}" into the Expiration date field
Type "{{fake_card_cvv}}" into the CVV field
Type "{{fake_zip}}" into the ZIP code field
Tap on "Add card" button
Tap on "Pay" button
Wait 15 seconds
Tap on "Start live chat" button

## Code

```python
def method_add_payment_method_credit_card_and_start_live_session(page):
    """Reusable method 'add_payment_method_credit_card_and_start_live_session' (Add payment method credit card and start live session) — see the dashboard's Methods page for every test case that calls it."""
    # Step 1: Tap on "Add a new credit or debit card"
    # No stable locator was ever captured for 'Add a new credit or debit card' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Add a new credit or debit card')

    # Step 2: Wait 10 seconds
    page.wait_for_timeout(10000)

    # Step 3: Type "{{login_field:name:user:default}}" into the Cardholder name field
    # No stable locator was ever captured for 'Cardholder name field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Cardholder name field', '{{login_field:name:user:default}}')

    # Step 4: Type "{{fake_card_number}}" into the Card number field
    # No stable locator was ever captured for 'Card number field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Card number field', '4869292053880543')

    # Step 5: Type "{{fake_card_expiry}}" into the Expiration date field
    # No stable locator was ever captured for 'Expiration date field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: Expiration date field', '06/35')

    # Step 6: Type "{{fake_card_cvv}}" into the CVV field
    # No stable locator was ever captured for 'CVV field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: CVV field', '951')

    # Step 7: Type "{{fake_zip}}" into the ZIP code field
    # No stable locator was ever captured for 'ZIP code field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: ZIP code field', '61717')

    # Step 8: Tap on "Add card"
    # No stable locator was ever captured for 'Add card' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Add card')

    # Step 9: Tap on "Pay"
    # No stable locator was ever captured for 'Pay' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Pay')

    # Step 10: Verify "{{fake_card_last_four}}" is visible
    # No stable locator was ever captured for '{{fake_card_last_four}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{fake_card_last_four}}')

    # Step 11: Tap on "Start live"
    # No stable locator was ever captured for 'Start live' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Start live')
```
