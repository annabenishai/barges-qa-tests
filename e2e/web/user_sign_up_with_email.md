---
name: User sign up  with email
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:00Z
default_role: user
---

## Steps

Tap on "JOIN NOW" button
Tap on Continue with email button
Enter '{{date:DDMMYYHHmmss}}@bargestech.com' in the email field
Enter '{{date:DDMMYYHHmmss}}@bargestech.com' in the retype email field
Enter 'test123' in the password field
Tap on the "BEGIN YOUR JOURNEY" button
Tap on 'I understand' button on T&P popup
Tap the Accept button on the cookies banner
Verify that the header avatar is visible


## Code

```python
def method_user_sign_up_with_email(page):
    """User sign up  with email — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on "JOIN NOW" button
    page.click('[data-testid="LohpNav__join-now"]')

    # Step 2: Tap on Continue with email button
    page.click('[data-testid="MainAuthScreen__email-btn"]')

    # Step 3: Enter '{{date:DDMMYYHHmmss}}@bargestech.com' in the email field
    page.fill('[data-testid="SignUpForm__email-input"]', '061026151118@bargestech.com')

    # Step 4: Enter '{{date:DDMMYYHHmmss}}@bargestech.com' in the retype email field
    page.fill('[data-testid="SignUpForm__retype-email-input"]', '061026151119@bargestech.com')

    # Step 5: Enter 'test123' in the password field
    page.fill('[data-testid="SignUpForm__password-input"]', 'test123')

    # Step 6: Tap on the "BEGIN YOUR JOURNEY" button
    page.click('[data-testid="SignUpForm__submit-btn"]')

    # Step 7: Tap on 'I understand' button on T&P popup
    page.click('[data-testid="TcPpConsentModal__accept-btn"]')

    # Step 8: Tap the Accept button on the cookies banner
    page.click('[data-testid="CookieConsentBanner__accept-btn"]')

    # Step 9: Verify that the header avatar is visible
    page.wait_for_selector('[data-testid="HeaderAuthSection__header-avatar"]', state='visible', timeout=15000)
```
