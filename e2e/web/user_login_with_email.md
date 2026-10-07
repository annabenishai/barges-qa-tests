---
name: User login with email
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:40Z
default_role: user
---

## Steps

Tap on JOIN NOW button
Tap on Continue with email button
Tap the Accept button on the cookies banner
Tap on Sign in button
Enter 'mykhailo.orban+0603001@ingenio.com' in the email field
Enter 'qwerty' in the password field
Tap on the Login button
Verify that the header avatar is visible
Reload the page



## Code

```python
def method_user_login_with_email(page):
    """User login with email — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on Let's connect button
    page.click('[data-testid="HeaderAuthSection__join-btn"]')

    # Step 2: Tap on Continue with email button
    page.click('[data-testid="MainAuthScreen__email-btn"]')

    # Step 3: Tap on Sign in button
    page.click('[data-testid="AffiliateSignUpForm__sign-in-link"]')

    # Step 4: Enter email in the email field
    page.fill('[data-testid="SignInForm__email-input"]', os.getenv('USER_EMAIL'))

    # Step 5: Enter password in the password field
    page.fill('[data-testid="SignInForm__password-input"]', os.getenv('USER_PASSWORD'))

    # Step 6: Tap on the Login button
    page.click('[data-testid="SignInForm__submit-btn"]')

    # Step 7: Tap the Accept button on the cookies banner
    page.click('[data-testid="CookieConsentBanner__accept-btn"]')

    # Step 8: Verify that the header avatar is visible
    page.wait_for_selector('[data-testid="HeaderAuthSection__header-avatar"]', state='visible', timeout=15000)
```
