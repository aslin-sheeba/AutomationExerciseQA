"""
Parent class for every Page Object.
Every page-specific class (HomePage, LoginPage, ProductsPage, ...) inherits
this so we write navigation/screenshot/wait logic exactly once.
"""


class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def take_screenshot(self, path):
        self.page.screenshot(path=path, full_page=True)

    def is_visible(self, locator, timeout=5000):
        try:
            self.page.locator(locator).wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")
