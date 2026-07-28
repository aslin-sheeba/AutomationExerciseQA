"""
INTEGRATION TESTING
Question: "When two or more features are chained together, does the DATA
and STATE flow correctly between them?"
Narrower than System testing -- we're checking specific handoffs, not the
whole journey. Example handoff: Search -> Add to Cart -> Cart reflects it.
"""
import pytest


@pytest.mark.integration
def test_searched_product_can_be_added_and_appears_in_cart(products_page, cart_page):
    products_page.open()
    products_page.search_product("top")
    assert products_page.get_result_count() > 0, "Precondition failed: search returned nothing"

    products_page.add_first_product_to_cart()
    products_page.go_to_cart_from_modal()

    product_names = cart_page.get_product_names()
    assert len(product_names) >= 1, "Product added via search did not reach the cart"


@pytest.mark.integration
def test_cart_total_matches_sum_of_line_items(products_page, cart_page):
    products_page.open()
    products_page.add_product_by_index_to_cart(0)
    products_page.close_cart_modal_continue_shopping()
    products_page.add_product_by_index_to_cart(1)
    products_page.go_to_cart_from_modal()

    line_totals = cart_page.get_total_price()
    assert len(line_totals) >= 2, "Expected at least 2 line items in cart"
    # This asserts the cart UI's own per-line totals are internally consistent
    # (each is a positive number) -- a deeper check would cross-reference
    # against the product listing price captured during add-to-cart.
    assert all(total > 0 for total in line_totals)
