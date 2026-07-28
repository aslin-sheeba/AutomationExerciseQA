"""
SYSTEM TESTING
Question: "Does the ENTIRE application, end-to-end, behave correctly as one
connected system?" This is the widest-scope automated suite: it walks the
full user journey across every feature the other suites tested in isolation.
"""
import pytest
from utils.helpers import random_email, random_name


@pytest.mark.system
def test_full_journey_signup_shop_contact(
    login_page, signup_page, home_page, products_page, cart_page, contact_page
):
    # 1. Sign up a brand new account
    login_page.open()
    email = random_email()
    login_page.start_signup(random_name(), email)

    signup_page.fill_mandatory_fields(
        password="TestPass123!",
        first_name="System",
        last_name="Tester",
        address1="1 Automation Way",
        country="United States",
        state="Texas",
        city="Austin",
        zipcode="73301",
        mobile_number="9998887777",
    )
    signup_page.submit()
    assert signup_page.is_account_created()
    signup_page.continue_after_creation()

    # 2. Confirm the system now recognizes the user as logged in
    assert home_page.is_user_logged_in()

    # 3. Browse and add a product to the cart
    products_page.open()
    products_page.search_product("dress")
    products_page.add_first_product_to_cart()
    products_page.go_to_cart_from_modal()
    assert cart_page.get_item_count() >= 1

    # 4. Use the contact form as a logged-in user
    contact_page.open()
    contact_page.fill_form(
        name="System Tester",
        email=email,
        subject="Post-purchase question",
        message="Full system flow test: signup, shop, then contact.",
    )
    contact_page.submit()
    assert contact_page.is_submitted_successfully()
