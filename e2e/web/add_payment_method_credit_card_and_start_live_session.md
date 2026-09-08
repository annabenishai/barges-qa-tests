---
name: Add payment method credit card and start live session
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-09-08T15:08:45Z
---

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
