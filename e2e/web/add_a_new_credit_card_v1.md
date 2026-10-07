---
name: Add a new credit card_v1
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:33Z
default_role: user
---

## Steps

Tap on "Add a new credit or debit card"
Wait 10 seconds
Type "Automation test" into the Cardholder name field
Type "{{fake_card_number}}" into the Card number field
Type "{{fake_card_number}}" into the Card number field if "Incorrect card number" is present
Type "{{fake_card_number}}" into the Card number field if "Incorrect card number" is present
Type "{{fake_card_expiry}}" into the Expiration date field
Type "{{fake_card_cvv}}" into the CVV field
Type "{{fake_zip}}" into the ZIP code field
Tap the "Add card" button
Tap "OK" button if present

## Code

```python
# No generated code cached yet for add_a_new_credit_card_v1 (W/playwright_python).
```
