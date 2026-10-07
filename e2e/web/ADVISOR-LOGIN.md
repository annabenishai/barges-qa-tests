---
name: Advisor Login
type: e2e
platform: web
owner: qa-mobile-web
source: dashboard-generated
updated_at: 2026-10-07T05:51:45Z
---

## Steps

1. Call method: Advisor login with email

## Methods

### Advisor login with email

Enter 'anna.benishai+0302@ingenio.com' in the Email field
Enter 'test666' in the Password field
Tap on the Log in button
Grant permissions
Verify "Hubert Blaine" is present
Refresh the page
Wait 5 seconds

## Code

```python
# Platform template: web (Playwright recording).
# This test case calls 1 reusable method(s): Advisor login with email.
# Their own generated code lives on the dashboard's Methods page (kept in sync across every test case that calls them) — the actions below are this run's own recording of the full flow.
import logging

logger = logging.getLogger(__name__)


import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('ADVISOR-LOGIN_2026-09-15', async ({ page, context }) => {
  
    // Fill input field
    await page.fill('[placeholder="Email"]', 'anna.benishai+0302@ingenio.com');

    // Take screenshot
    await page.screenshot({ path: 'step.png' });

    // Fill input field
    await page.fill('[placeholder="Password"]', 'test666');

    // Take screenshot
    await page.screenshot({ path: 'step.png' });

    // Click element
    await page.click('button.button');

    // Take screenshot
    await page.screenshot({ path: 'step.png' });

    // Take screenshot
    await page.screenshot({ path: 'step.png' });

    // Take screenshot
    await page.screenshot({ path: 'step.png' });
});
```
