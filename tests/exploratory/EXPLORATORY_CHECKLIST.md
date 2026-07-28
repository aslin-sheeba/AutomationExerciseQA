# Exploratory Testing — Session Charter

Exploratory testing is primarily **manual and mind-driven**: you're actively
looking for the unexpected, not confirming a known expectation. Automation's
role here is limited to (a) quickly resetting state so you can explore faster,
and (b) turning anything interesting you find into a permanent regression test.

## Session Charter Template

- **Area under test:**
- **Time-box:** 30–45 minutes
- **Mission:** Explore ___ looking for ___
- **Setup notes:**

## Ideas to try on this site (automationexercise.com)

- Signup form: unicode names, extremely long strings, emoji in the message box,
  negative/zero/huge mobile numbers, submitting with only the required fields
  vs. every optional field filled.
- Cart: add the same product twice, add 20+ products, remove all items then hit
  "Proceed to Checkout", open the cart in two tabs and modify in one.
- Search: SQL-injection-style strings, only whitespace, only special characters,
  extremely long search terms, case sensitivity ("DRESS" vs "dress").
- Contact form: upload a very large file, upload a non-image/non-doc file type,
  submit then immediately resubmit (double-submit).
- Navigation: browser back/forward through the checkout flow, refreshing mid-form,
  deep-linking directly to /payment without going through checkout first.

## What to do with what you find

If something looks wrong:
1. Note exact steps + screenshot (use `page.screenshot()` in a scratch script,
   or your browser devtools).
2. File it as a bug.
3. Once fixed, add a **retesting** test in `tests/retesting/` for that exact bug,
   and consider whether it also deserves a permanent **regression** test.

Exploratory testing feeds the other suites -- it isn't meant to stay manual forever.
