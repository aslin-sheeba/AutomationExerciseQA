"""
SANITY TESTING
Question: "Did the specific thing that was just changed/fixed actually work?"
Narrow and shallow by design -- unlike regression, we are NOT re-checking
the whole surrounding area, just the fixed behavior.

Scenario used here: imagine a bug ticket said "search is case-sensitive,
so 'DRESS' returns 0 results even though 'dress' returns matches" and it
was just fixed.

NOTE: the original version of this test asserted the site trims leading/
trailing whitespace in search. That was an assumption I never verified --
your last run proved it's false (the site does NOT trim whitespace), so
that test was checking a fictional fix against real production behavior.
Replaced it with a scenario I'm not asserting blind: run it once, and if
it turns out the site IS case-sensitive too, that's a real, useful finding
-- not a framework bug.
"""
import pytest


@pytest.mark.sanity
def test_search_is_not_case_sensitive(products_page):
    products_page.open()
    products_page.search_product("dress")
    lowercase_count = products_page.get_result_count()

    products_page.open()
    products_page.search_product("DRESS")
    uppercase_count = products_page.get_result_count()

    assert lowercase_count > 0, "Baseline lowercase search returned no results"
    assert uppercase_count == lowercase_count, (
        f"Sanity check failed: 'DRESS' returned {uppercase_count} results, "
        f"'dress' returned {lowercase_count}. Search appears case-sensitive."
    )