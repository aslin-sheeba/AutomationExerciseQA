import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
SLOWMO = int(os.getenv("SLOWMO", "0"))

# Central place for every URL we automate.
# If the site restructures, we change it here once instead of in every test.
URLS = {
    "home": f"{BASE_URL}/",
    "login": f"{BASE_URL}/login",
    "signup": f"{BASE_URL}/signup",
    "products": f"{BASE_URL}/products",
    "cart": f"{BASE_URL}/view_cart",
    "contact_us": f"{BASE_URL}/contact_us",
    "delete_account": f"{BASE_URL}/delete_account",
}
