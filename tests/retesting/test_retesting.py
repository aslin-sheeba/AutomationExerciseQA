"""
RETESTING (a.k.a. confirmation testing)
Question: "Does the exact scenario from a previously FAILED bug report now pass?"
This is different from sanity: sanity checks the fix generally works;
retesting re-runs the *original failing steps from the bug report*, verbatim.

Example bug report we're confirming here:
  BUG-102: "Adding a product to the cart, then removing it, still shows the
  item in the cart count / table."
"""
import pytest


@pytest.mark.retesting
def test_bug_102_removed_item_no_longer_in_cart(products_page, cart_page):
    products_page.open()
    products_page.add_first_product_to_cart()
    products_page.go_to_cart_from_modal()

    count_before = cart_page.get_item_count()
    assert count_before >= 1, "Setup failed: nothing was added to cart"

    cart_page.delete_item(0)

    # Give the UI a moment to update the table after the delete click
    cart_page.page.wait_for_timeout(500)

    count_after = cart_page.get_item_count()
    assert count_after == count_before - 1, \
        f"BUG-102 has regressed: item count is {count_after}, expected {count_before - 1}"
