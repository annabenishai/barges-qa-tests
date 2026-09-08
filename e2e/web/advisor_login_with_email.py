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

    # Step 5: Wait 30 seconds
    page.wait_for_timeout(30000)
