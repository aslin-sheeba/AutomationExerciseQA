from pages.base_page import BasePage
from config.settings import URLS


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_title = page.get_by_text("Searched Products")
        self.product_cards = page.locator(".features_items .product-image-wrapper")
        self.cart_modal = page.locator("#cartModal")
        self.continue_shopping_button = page.locator(".modal-footer .btn-success")
        self.view_cart_link_in_modal = page.locator('#cartModal a:has-text("View Cart")')

    def open(self):
        self.navigate(URLS["products"])

    def is_loaded(self):
        return self.is_visible(".features_items")

    def search_product(self, term):
        self.search_input.fill(term)
        self.search_button.click()

    def get_result_count(self):
        return self.product_cards.count()

    def add_first_product_to_cart(self):
        first_card = self.product_cards.first
        first_card.hover()
        first_card.locator("a.add-to-cart").first.click()

    def add_product_by_index_to_cart(self, index):
        card = self.product_cards.nth(index)
        card.hover()
        card.locator("a.add-to-cart").first.click()

    def close_cart_modal_continue_shopping(self):
        self.continue_shopping_button.click()

    def go_to_cart_from_modal(self):
        self.view_cart_link_in_modal.click()
