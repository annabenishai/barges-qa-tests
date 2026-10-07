---
name: User fill rate & review popup if visible
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:03Z
default_role: user
---

## Steps

Tap the Thumbs up button
Type "Great session, thank you!" into the review field
Tap on "Submit" button if visible

## Code

```python
def method_user_fill_rate_review_popup_if_visible(page, review_message: str = 'Great session, thank you!'):
    """User fill rate & review popup if visible — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    TIMEOUT_SHORT = 3000

    # Step 1: Tap the Thumbs up button
    page.click('[data-testid="RateReviewAfterChat__thumbs-up"]')

    # Step 2: Type the review message into the review field
    page.fill('[data-testid="RateReviewAfterChat__comment"]', review_message)

    # Step 3: Tap on "Submit" button if visible
    try:
        page.wait_for_selector('[data-testid="RateReviewAfterChat__submit-btn"]', state='visible', timeout=TIMEOUT_SHORT)
        page.click('[data-testid="RateReviewAfterChat__submit-btn"]')
    except TimeoutError:
        pass  # optional tap — only fires if the element is present
```
