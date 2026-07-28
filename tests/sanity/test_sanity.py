"""
SANITY TESTING
Question: "Did the specific thing that was just changed/fixed actually work?"
Narrow and shallow by design -- unlike regression, we are NOT re-checking
the whole surrounding area, just the fixed behavior.

Scenario used here: imagine a bug ticket said "search box does not trim
whitespace, causing valid searches to return 0 results" and it was just fixed.
"""
import pytest


@pytest.mark.sanity
def test_search_trims_leading_and_trailing_whitespace(products_page):
    products_page.open()
    products_page.search_product("  dress  ")

    assert products_page.get_result_count() > 0, \
        "Sanity check failed: search with padded whitespace returned no results"
