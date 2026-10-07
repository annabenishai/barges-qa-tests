---
name: Advisor login with email
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:12Z
default_role: advisor
---

## Steps

Enter 'anna.benishai+0302@ingenio.com' in the Email field
Enter 'test666' in the Password field
Tap on the Log in button
Grant permissions
Verify "Hubert Blaine" is present
Refresh the page
Wait 5 seconds

## Code

```python
def method_advisor_login_with_email(page):
    """Advisor login with email — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Enter 'anna.benishai+0302@ingenio.com' in the Email field
    page.fill('[placeholder="Email"]', 'anna.benishai+0302@ingenio.com')

    # Step 2: Enter 'test666' in the Password field
    page.fill('[placeholder="Password"]', 'test666')

    # Step 3: Tap on the Log in button
    page.click('button.button')

    # Step 4: Grant permissions
    # context.grant_permissions(["notifications", "geolocation", "camera", "microphone"])

    # Step 5: Verify "Hubert Blaine" is present
    # No stable locator was ever captured for 'Hubert Blaine' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Hubert Blaine')

    # Step 6: Refresh the page
    page.reload(wait_until="load")

    # Step 7: Wait 5 seconds
    page.wait_for_timeout(5000)
```
