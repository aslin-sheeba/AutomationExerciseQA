"""
REGRESSION TESTING
Question: "Now that something else in the app changed, did we break any of
the OTHER features that used to work?"
Broader and deeper than sanity/smoke -- this is the suite you run before
every release. It reuses the exact same POM classes as every other suite.
"""
import pytest
from utils.helpers import random_email


@pytest.mark.regression
def test_home_page_still_reachable_from_every_key_page(home_page, products_page,
                                                          cart_page, contact_page):
    for page_obj in (products_page, cart_page, contact_page):
        page_obj.open()
        home_page.page.locator(".logo img").click()
        assert "automationexercise.com" in home_page.get_url()


@pytest.mark.regression
def test_add_to_cart_still_works_after_search(products_page, cart_page):
    products_page.open()
    products_page.search_product("dress")
    products_page.add_first_product_to_cart()
    products_page.go_to_cart_from_modal()

    assert cart_page.get_item_count() >= 1


@pytest.mark.regression
def test_newsletter_subscription_still_accepts_valid_email(home_page):
    home_page.open()
    home_page.scroll_to_bottom()
    home_page.subscribe(random_email())

    assert home_page.is_visible("#success-subscribe", timeout=5000)
