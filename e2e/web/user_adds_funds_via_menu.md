---
name: User adds funds via menu
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:38Z
default_role: user
---

## Steps

Tap on the Profile menu button
Tap on the Add funds button
Extract "Credit balance:" as balance_before
Tap "{{random_match:Get $}}"
Tap on the Get funds button
Tap on the Pay button
Tap on ok button
Wait 3 seconds
Extract "Credit balance:" as balance_after
Verify balance_after increased since balance_before


## Code

```python
def method_user_adds_funds_via_menu(page):
    """User adds funds via menu — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on the Profile menu button
    page.click('[data-testid="HeaderAuthSection__profile-menu-btn"]')

    # Step 2: Tap on the Add funds button
    page.click('[data-testid="HeaderAuthSection__add-funds-link"]')

    # Step 3: Extract "Credit balance:" as balance_before
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 4: Tap "{{random_match:Get $}}"
    # No stable locator was ever captured for '{{random_match:Get $}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{random_match:Get $}}')

    # Step 5: Tap on the Get funds button
    page.click('[data-testid="AddFunds__cta"]')

    # Step 6: Tap on the Pay button
    page.click('#purchase-details-pay-button')

    # Step 7: Tap on ok button
    page.click('[data-testid="PaymentProcessingScreen__ok-button"]')

    # Step 8: Wait 3 seconds
    page.wait_for_timeout(3000)

    # Step 9: Extract "Credit balance:" as balance_after
    # extract_text steps aren't reproduced in generated standalone code yet

    # Step 10: Verify balance_after increased since balance_before
    # assert_compare depends on an extract_text capture, which isn't reproduced above either
```
