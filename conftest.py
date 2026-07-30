import os
import pytest
import requests
from utils.helpers import random_email, random_name
from utils.logger import get_logger

logger = get_logger("conftest")


@pytest.fixture(scope="session")
def registered_user():
    """
    Creates ONE real account on automationexercise.com via its public
    createAccount API before the test session starts, and hands the
    credentials to any test that needs a guaranteed-to-exist user
    (e.g. valid login, or triggering a duplicate-signup error).

    This avoids two bad patterns: hardcoding a fake email that doesn't
    exist, and relying on someone manually maintaining data/users.json.
    """
    email = random_email()
    password = "TestPass123!"
    name = random_name("QA_Registered")

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "QA",
        "lastname": "Registered",
        "company": "QA Corp",
        "address1": "1 Automation Way",
        "address2": "",
        "country": "United States",
        "zipcode": "73301",
        "state": "Texas",
        "city": "Austin",
        "mobile_number": "9998887777",
    }

    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data=payload,
        timeout=15,
    )
    body = response.json()
    assert body.get("responseCode") == 201, (
        f"Setup failed: could not create test user via API. Response: {body}"
    )

    logger.info(f"Session test user created via API: {email}")
    return {"email": email, "password": password, "name": name}


# ---------- browser/page config (pytest-playwright reads these) ----------

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 768},
    }


# ---------- Page Object fixtures (one per POM class, all reusable) --------

@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage
    return HomePage(page)


@pytest.fixture
def login_page(page):
    from pages.login_page import LoginPage
    return LoginPage(page)


@pytest.fixture
def signup_page(page):
    from pages.signup_page import SignupPage
    return SignupPage(page)


@pytest.fixture
def products_page(page):
    from pages.products_page import ProductsPage
    return ProductsPage(page)


@pytest.fixture
def cart_page(page):
    from pages.cart_page import CartPage
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    from pages.checkout_page import CheckoutPage
    return CheckoutPage(page)


@pytest.fixture
def payment_page(page):
    from pages.payment_page import PaymentPage
    return PaymentPage(page)


@pytest.fixture
def contact_page(page):
    from pages.contact_page import ContactPage
    return ContactPage(page)


# ---------- automatic failure screenshot, used by every test type ----------

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            os.makedirs("screenshots", exist_ok=True)
            safe_name = item.name.replace("/", "_")
            path = f"screenshots/FAILED_{safe_name}.png"
            try:
                page.screenshot(path=path, full_page=True)
                logger.error(f"Test failed: {item.name} | screenshot saved: {path}")
            except Exception as e:
                logger.error(f"Could not capture failure screenshot: {e}")