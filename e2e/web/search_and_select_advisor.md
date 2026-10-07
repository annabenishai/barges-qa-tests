---
name: Search and select advisor
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:49:24Z
default_role: both
---

## Steps

Tap on "Find advisor' field
Type "Hubert Blaine" into 'Find advisor' field
Tap on "Hubert Blaine"
Verify "Hubert Blaine" is visible


## Code

```python
def method_search_and_select_advisor(page):
    """Reusable method 'search_and_select_advisor' (Search and select advisor) — see the dashboard's Methods page for every test case that calls it."""
    # Step 1: Tap on "Find advisor' field
    # No stable locator was ever captured for "Find advisor' field" — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: Find advisor' field')

    # Step 2: Type "{{api:advisor_name}}" into the advisor name field
    # No stable locator was ever captured for 'advisor name field' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.fill('TODO: advisor name field', '{{api:advisor_name}}')

    # Step 3: Tap on "{{login_field:name:advisor}}"
    # No stable locator was ever captured for '{{login_field:name:advisor}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{login_field:name:advisor}}')

    # Step 4: Verify "{{login_field:name:advisor}}" is visible
    # No stable locator was ever captured for '{{login_field:name:advisor}}' — every run resolved it live instead
    # of a cacheable selector. Fill in a real CSS selector before running this.
    # page.click('TODO: {{login_field:name:advisor}}')
```
