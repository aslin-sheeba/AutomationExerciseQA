"""
USER ACCEPTANCE TESTING (UAT)
Question: "From a REAL BUSINESS USER's point of view, does the product do
what they actually need, in a way that makes sense to them?"
Written as user stories, not technical steps. Automation here supports UAT
by covering the repeatable parts; a human still reviews UX/wording/feel.
"""
import pytest


@pytest.mark.uat
def test_user_story_find_a_product_by_keyword_and_confirm_price_shown(products_page):
    """
    As a shopper,
    I want to search for an item by keyword,
    So that I can quickly see if it's available and how much it costs,
    without having to browse the whole catalog.
    """
    products_page.open()
    products_page.search_product("jean")

    assert products_page.get_result_count() > 0, \
        "A shopper searching for a common keyword should see results"

    # A business user cares that a price is visibly present on each result,
    # not just that "something" rendered.
    first_card_price = products_page.product_cards.first.locator(".productinfo h2")
    assert first_card_price.is_visible(), "Product price is not visible to the shopper"


@pytest.mark.uat
def test_user_story_get_help_via_contact_form_without_creating_account(contact_page):
    """
    As a visitor who is not ready to create an account,
    I want to send a question through the Contact Us form,
    So that I can get help before committing to sign up.
    """
    contact_page.open()
    contact_page.fill_form(
        name="Curious Visitor",
        email="curious.visitor@example.com",
        subject="Question before I sign up",
        message="Do you ship internationally? Just checking before I create an account.",
    )
    contact_page.submit()

    assert contact_page.is_submitted_successfully(), \
        "A visitor should be able to reach support without an account"
