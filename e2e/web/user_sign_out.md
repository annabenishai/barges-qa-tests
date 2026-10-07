---
name: User sign out
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:25Z
default_role: user
---

## Steps

Tap on the profile icon
Tap on the "Sign out" button
Tap on the "Yes" button on the sign out popup
Verify the email field is visible

## Code

```python
def method_user_sign_out(page):
    """User sign out — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Tap on the profile icon
    page.click('TODO: profile icon')

    # Step 2: Tap on the "Sign out" button
    page.click('TODO: Sign out')

    # Step 3: Tap on the "Yes" button on the sign out popup
    page.click('TODO: Yes')

    # Step 4: Verify the email field is visible
    page.click('TODO: the email field')
```
