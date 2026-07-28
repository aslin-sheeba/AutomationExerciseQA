from pages.base_page import BasePage
from config.settings import URLS


class ContactPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.name_input = page.locator('input[data-qa="name"]')
        self.email_input = page.locator('input[data-qa="email"]')
        self.subject_input = page.locator('input[data-qa="subject"]')
        self.message_input = page.locator('textarea[data-qa="message"]')
        self.submit_button = page.locator('input[data-qa="submit-button"]')
        self.success_message = page.locator(".status.alert-success")
        self.home_button = page.locator("a.btn.btn-success")

    def open(self):
        self.navigate(URLS["contact_us"])

    def fill_form(self, name, email, subject, message):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)

    def submit(self):
        # The site raises a native browser confirm() dialog on submit.
        # We must accept it or the form will hang waiting for a response.
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()

    def is_submitted_successfully(self):
        return self.is_visible(".status.alert-success", timeout=8000)
