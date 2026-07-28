import json
import pytest

with open("data/users.json", encoding="utf-8") as f:
    USERS = json.load(f)


@pytest.mark.functional
def test_login_with_valid_credentials_succeeds(login_page):

    user = USERS["existing_user"]

    login_page.open()

    login_page.login(
        user["email"],
        user["password"]
    )

    assert login_page.is_logged_in(), \
        "User was not logged in successfully"
    
@pytest.mark.functional
def test_login_with_valid_credentials_succeeds(login_page, home_page, signup_page):
    login_page.open()
    login_page.login(USERS["existing_user"]["email"], USERS["existing_user"]["password"])

    # If the account already exists on the site, we should be logged in.
    if home_page.is_user_logged_in():
        return

    # Otherwise, create the account via the UI, then verify login/creation.
    login_page.open()
    login_page.start_signup(USERS["existing_user"]["name"], USERS["existing_user"]["email"])
    signup_page.fill_mandatory_fields(
        password=USERS["existing_user"]["password"],
        first_name=USERS["existing_user"].get("first_name", "Automation"),
        last_name=USERS["existing_user"].get("last_name", "Tester"),
        address1=USERS["existing_user"].get("address", "123 Automation Street"),
        country=USERS["existing_user"].get("country", "India"),
        state=USERS["existing_user"].get("state", "State"),
        city=USERS["existing_user"].get("city", "City"),
        zipcode=USERS["existing_user"].get("zipcode", "000000"),
        mobile_number=USERS["existing_user"].get("mobile_number", "0000000000"),
    )
    signup_page.submit()

    assert signup_page.is_account_created(), "Account creation during setup did not appear"
    signup_page.continue_after_creation()

    assert home_page.is_user_logged_in(), "User does not appear logged in after account creation"
