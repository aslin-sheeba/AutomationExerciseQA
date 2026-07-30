import pytest
import json

with open("data/users.json") as f:
    USERS = json.load(f)


@pytest.mark.functional
def test_login_with_invalid_credentials_shows_error(login_page):
    login_page.open()
    login_page.login(USERS["invalid_user"]["email"], USERS["invalid_user"]["password"])

    assert login_page.has_login_error(), "Expected login error message was not shown"


@pytest.mark.functional
def test_login_with_valid_credentials_succeeds(login_page, home_page, registered_user):
    login_page.open()
    login_page.login(registered_user["email"], registered_user["password"])

    assert home_page.is_user_logged_in(), "User does not appear logged in after valid login"