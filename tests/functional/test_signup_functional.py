"""
FUNCTIONAL TESTING
Question we're answering: "Does this individual feature work, on its own,
when used correctly?" No concern yet for how it interacts with anything else.
"""
import pytest
import json
from utils.helpers import random_email, random_name


with open("data/users.json") as f:
    USERS = json.load(f)


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
def test_signup_rejects_email_already_in_use(login_page):
    # NOTE: replace with an email you know already exists on the site
    # to run this meaningfully.
    existing_email = USERS["existing_user"]["email"]
    login_page.open()
    login_page.start_signup("Existing Person", existing_email)

    assert login_page.has_signup_email_exists_error(), \
        "Expected 'Email Address already exist!' message was not shown"
