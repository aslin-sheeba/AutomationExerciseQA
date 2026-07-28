from pages.base_page import BasePage
from config.settings import URLS


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.logo = page.locator(".logo img")
        self.signup_login_link = page.get_by_text("Signup / Login")
        self.logged_in_indicator = page.get_by_text("Logged in as")
        self.subscribe_email = page.locator("#susbscribe_email")  # site's own typo, kept intentionally
        self.subscribe_button = page.locator("#subscribe")
        self.subscribe_success = page.locator("#success-subscribe")
        self.scroll_up_arrow = page.locator("#scrollUp")
        self.category_sidebar = page.locator(".left-sidebar")

    def open(self):
        self.navigate(URLS["home"])

    def is_loaded(self):
        return self.is_visible(".logo img")

    def go_to_signup_login(self):
        self.signup_login_link.click()

    def is_user_logged_in(self):
        return self.is_visible("text=Logged in as", timeout=3000)

    def subscribe(self, email):
        self.subscribe_email.fill(email)
        self.subscribe_button.click()
