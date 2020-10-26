# *Make a test case to verify, every product on the page has a text ‘Regular’ and a product name: https://www.amazon.com/wholefoodsdeals
# NOTE: ONLY USE BOTTOM SECTION:
from behave import given, then
from selenium.webdriver.common.by import By

PRODUCTS = (By. CSS_SELECTOR, "#wfm-pmd_deals_section li")
REGULAR_PRICE_FIELD = (By.CSS_SELECTOR, "span[class*='regular-price']")
PRODUCT_NAME = (By.CSS_SELECTOR, "span[class*='product-name']")


@given('Open Amazon whole foods website')
def open_wholefoods_page(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")


@then('Verify it has  text ‘Regular’ and a product name')
def verify_product(context):
    products = context.driver.find_elements(*PRODUCTS)
    regular_price = context.driver.find_element(*REGULAR_PRICE_FIELD)
    product_name = context.driver.find_element(*PRODUCT_NAME)
    for items in products:
        assert regular_price != '' and product_name != '', F'Expected both to appear but missed {regular_price} or {product_name}'



