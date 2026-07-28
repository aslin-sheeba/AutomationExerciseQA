import pytest
import json

with open("data/products.json") as f:
    PRODUCTS = json.load(f)


@pytest.mark.functional
def test_search_returns_matching_products(products_page):
    products_page.open()
    products_page.search_product(PRODUCTS["search_terms"]["valid"])

    assert products_page.is_visible("text=Searched Products")
    assert products_page.get_result_count() > 0


@pytest.mark.functional
def test_search_with_no_matches_returns_zero_results(products_page):
    products_page.open()
    products_page.search_product(PRODUCTS["search_terms"]["no_results"])

    assert products_page.get_result_count() == 0
