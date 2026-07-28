from pages.base_page import BasePage


class PaymentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.name_on_card = page.locator('input[data-qa="name-on-card"]')
        self.card_number = page.locator('input[data-qa="card-number"]')
        self.cvc = page.locator('input[data-qa="cvc"]')
        self.expiry_month = page.locator('input[data-qa="expiry-month"]')
        self.expiry_year = page.locator('input[data-qa="expiry-year"]')
        self.pay_button = page.locator('button[data-qa="pay-button"]')
        self.success_message = page.locator(".alert-success")

    def fill_and_pay(self, name, number, cvc, month, year):
        self.name_on_card.fill(name)
        self.card_number.fill(number)
        self.cvc.fill(cvc)
        self.expiry_month.fill(month)
        self.expiry_year.fill(year)
        self.pay_button.click()

    def is_order_confirmed(self):
        return self.is_visible(".alert-success", timeout=8000)
