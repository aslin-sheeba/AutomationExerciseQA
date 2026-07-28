"""
SMOKE TESTING
Question: "Is this build stable enough to even bother testing further?"
Shallow, fast, covers the whole site's critical paths -- not deep validation.
If any of these fail, stop and don't run the rest of the suite.
"""
import pytest


@pytest.mark.smoke
def test_home_page_loads(home_page):
    home_page.open()
    assert home_page.is_loaded()


@pytest.mark.smoke
def test_login_page_loads(login_page):
    login_page.open()
    assert login_page.is_visible('input[data-qa="login-email"]')


@pytest.mark.smoke
def test_products_page_loads(products_page):
    products_page.open()
    assert products_page.is_loaded()
    assert products_page.get_result_count() > 0


@pytest.mark.smoke
def test_cart_page_loads(cart_page):
    cart_page.open()
    # Either it's empty or it has the cart table -- both are "loaded" states
    assert cart_page.is_empty() or cart_page.is_visible("#cart_info_table")


@pytest.mark.smoke
def test_contact_us_page_loads(contact_page):
    contact_page.open()
    assert contact_page.is_visible('input[data-qa="name"]')
