from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.order_comment = page.locator('textarea[name="message"]')
        self.place_order_button = page.get_by_text("Place Order")
        self.address_details = page.locator("#address_delivery")
        self.review_order_table = page.locator("#cart_info_table")

    def add_comment(self, text):
        self.order_comment.fill(text)

    def place_order(self):
        self.place_order_button.click()
