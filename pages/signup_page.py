from pages.base_page import BasePage


class SignupPage(BasePage):
    """
    The 'Enter Account Information' page you land on after start_signup()
    on LoginPage. Kept separate because it's a genuinely different form,
    even though it's part of the same signup journey.
    """

    def __init__(self, page):
        super().__init__(page)
        self.title_mr = page.locator("#id_gender1")
        self.title_mrs = page.locator("#id_gender2")
        self.password = page.locator("#password")
        self.days = page.locator("#days")
        self.months = page.locator("#months")
        self.years = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.company = page.locator("#company")
        self.address1 = page.locator("#address1")
        self.address2 = page.locator("#address2")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile_number = page.locator("#mobile_number")
        self.create_account_button = page.locator('button[data-qa="create-account"]')

        self.account_created_heading = page.locator('h2[data-qa="account-created"]')
        self.continue_button = page.locator('a[data-qa="continue-button"]')

    def fill_mandatory_fields(self, password, first_name, last_name, address1,
                               country, state, city, zipcode, mobile_number):
        self.title_mr.check()
        self.password.fill(password)
        self.days.select_option("10")
        self.months.select_option("5")
        self.years.select_option("1995")
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.address1.fill(address1)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)

    def submit(self):
        self.create_account_button.click()

    def is_account_created(self):
        return self.is_visible('h2[data-qa="account-created"]', timeout=8000)

    def continue_after_creation(self):
        self.continue_button.click()
