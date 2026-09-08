def method_user_connects_with_advisor_via_my_activity(page):
    """User connects with advisor via my activity — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: [web only] Tap on the Connect now button
    page.click('a.connectButton--s0k4r')

    # Step 2: Verify "Hubert Blaine" is visible
    # No stable locator was ever captured for 'Hubert Blaine' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Hubert Blaine')

    # Step 4: Tap on the Chat button
    page.click('[data-testid="AdvisorProfileCard__live-mode-button-chat"]')
