import os
import pytest
from utils.logger import get_logger

logger = get_logger("conftest")


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
