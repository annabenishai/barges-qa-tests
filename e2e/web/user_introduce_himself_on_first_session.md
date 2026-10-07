---
name: User introduce himself on first session
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:27Z
default_role: both
---

## Steps

Type "Automation test" into the Nickname field
Tap on "Female" button
Type "{{fake_birthdate}}" into the Date of birth field
Tap on "Start chat" button

## Code

```python
def method_user_introduce_himself_on_first_session(page):
    """User introduce himself on first session — a reusable step sequence, edited on the dashboard's Methods page. Every test case that calls it runs this exact code."""
    # Platform template: web (Playwright).
    # Step 1: Type "Automation test" into the Nickname field
    page.fill('[data-testid="IntroduceScreen__nickname-input"]', 'Automation test')

    # Step 2: Tap on "Female" button
    page.click('#intro-gender-F')

    # Step 3: Type "{{fake_birthdate}}" into the Date of birth field
    page.fill('[data-testid="IntroduceScreen__dob-picker__input"]', '02/16/2006')

    # Step 4: Tap on "Start chat" button
    page.click('[data-testid="IntroduceScreen__submit-btn"]')
```
