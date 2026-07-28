# AutomationExercise QA Framework

Full site automation suite against **https://automationexercise.com**, a demo
e-commerce site built specifically for automation practice (it ships with
`data-qa` attributes for stable locators).

## Stack
Python → Pytest → Playwright → Page Object Model → 9 testing-type suites

## Why this site
It gives us enough real surface area to make every testing type meaningful,
not just a login form:
- Signup / Login
- Product search & catalog
- Cart
- Checkout & Payment
- Contact form
- Newsletter subscription

## Structure

```
pages/        -> ONE class per real page. Every test suite reuses these.
tests/
  functional/   -> does each feature work in isolation
  smoke/        -> is the build alive enough to test further
  sanity/       -> did this one specific fix work
  retesting/    -> does this exact previously-failed bug report now pass
  regression/   -> did anything else break
  integration/  -> do 2+ features hand off data/state correctly
  system/       -> full end-to-end journey across the whole site
  uat/          -> business user stories
  exploratory/  -> charter + checklist (manual-first, feeds the suites above)
config/        -> settings.py: all URLs and env config in one place
data/          -> JSON test data (fill in data/users.json with a real account)
conftest.py    -> page-object fixtures shared by every suite
```

## Setup

```powershell
cd AutomationExerciseQA
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

## Before running

Edit `data/users.json`:
- `existing_user` needs a real account you've created on the site (or run
  `tests/functional/test_signup_functional.py::test_new_user_can_sign_up` once
  and reuse that email/password).

## Running suites

```powershell
pytest -m smoke              # fast, run this first
pytest -m functional
pytest -m sanity
pytest -m retesting
pytest -m regression
pytest -m integration
pytest -m system
pytest -m uat
pytest                        # everything
```

Failed tests auto-save a screenshot to `screenshots/` and every run writes a
timestamped log to `logs/`.

## Reporting

This scaffold doesn't wire in an HTML reporter yet. Cleanest option: add
`pytest-html` (`pip install pytest-html`, then `pytest --html=reports/report.html
--self-contained-html`). If you want to reuse your own `qa-reporter-pro`
package instead, share its actual public API (class/function names) and I'll
wire it into `conftest.py` the same way — one hook, reused by every suite here.

## Extending to more pages

To automate another page (e.g. Products Detail, My Account):
1. Add one class to `pages/`.
2. Add one fixture to `conftest.py`.
3. Write tests for it under whichever `tests/<type>/` folders make sense.
No existing test or page object needs to change.
