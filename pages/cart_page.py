from pages.base_page import BasePage
from config.settings import URLS


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_table = page.locator("#cart_info_table")
        self.cart_rows = page.locator("#cart_info_table tbody tr")
        self.proceed_to_checkout = page.get_by_text("Proceed To Checkout")
        self.empty_cart_message = page.get_by_text("Cart is empty!")
        self.register_login_link_in_modal = page.locator('#cartModal a:has-text("Register / Login")')

    def open(self):
        self.navigate(URLS["cart"])

    def get_item_count(self):
        return self.cart_rows.count()

    def is_empty(self):
        return self.is_visible("text=Cart is empty!", timeout=3000)

    def delete_item(self, index=0):
        self.cart_rows.nth(index).locator("a.cart_quantity_delete").click()

    def proceed_checkout(self):
        self.proceed_to_checkout.click()

    def get_product_names(self):
        return self.cart_rows.locator(".cart_description h4 a").all_inner_texts()

    def get_total_price(self):
        totals = self.cart_rows.locator(".cart_total .cart_total_price").all_inner_texts()
        return [float(t.replace("Rs. ", "").strip()) for t in totals]
