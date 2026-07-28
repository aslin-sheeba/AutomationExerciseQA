import pytest
from utils.helpers import random_email


@pytest.mark.functional
def test_contact_form_submits_successfully(contact_page):
    contact_page.open()
    contact_page.fill_form(
        name="QA Tester",
        email=random_email(),
        subject="Automation practice",
        message="This is a functional test of the contact form submission flow.",
    )
    contact_page.submit()

    assert contact_page.is_submitted_successfully()
