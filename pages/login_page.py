from pages.base_page import BasePage
from config.settings import URLS


class LoginPage(BasePage):
    """
    Handles BOTH boxes that live on /login:
      - 'Login to your account' (existing user)
      - 'New User Signup!' (kicks off account creation, handed off to SignupPage)
    """

    def __init__(self, page):
        super().__init__(page)

        # Login box
        self.login_email = page.locator('input[data-qa="login-email"]')
        self.login_password = page.locator('input[data-qa="login-password"]')
        self.login_button = page.locator('button[data-qa="login-button"]')
        self.login_error = page.get_by_text("Your email or password is incorrect!")

        # Signup box
        self.signup_name = page.locator('input[data-qa="signup-name"]')
        self.signup_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')
        self.signup_error = page.get_by_text("Email Address already exist!")

    def open(self):
        self.navigate(URLS["login"])

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def start_signup(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def has_login_error(self):
        return self.is_visible("text=Your email or password is incorrect!", timeout=3000)

    def has_signup_email_exists_error(self):
        return self.is_visible("text=Email Address already exist!", timeout=3000)
