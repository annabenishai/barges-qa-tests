---
name: User adds funds via menu
type: e2e
platform: app
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:50:53Z
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
# No generated code cached yet for user_adds_funds_via_menu (An/appium_python).
```
