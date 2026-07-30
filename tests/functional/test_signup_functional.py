"""
FUNCTIONAL TESTING
Question we're answering: "Does this individual feature work, on its own,
when used correctly?" No concern yet for how it interacts with anything else.
"""
import pytest
from utils.helpers import random_email, random_name


@pytest.mark.functional
def test_new_user_can_sign_up(login_page, signup_page):
    login_page.open()
    login_page.start_signup(random_name(), random_email())

    signup_page.fill_mandatory_fields(
        password="TestPass123!",
        first_name="Jordan",
        last_name="QA",
        address1="221B Baker Street",
        country="United States",
        state="California",
        city="Los Angeles",
        zipcode="90001",
        mobile_number="9999999999",
    )
    signup_page.submit()

    assert signup_page.is_account_created(), "Account creation confirmation did not appear"


@pytest.mark.functional
def test_signup_rejects_email_already_in_use(login_page, registered_user):
    # registered_user is created via the API before the session starts, so
    # this email is guaranteed to already exist -- no placeholder guessing.
    login_page.open()
    login_page.start_signup("Existing Person", registered_user["email"])

    assert login_page.has_signup_email_exists_error(), \
        "Expected 'Email Address already exist!' message was not shown"