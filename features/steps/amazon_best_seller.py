from time import sleep
from behave import given,when,then
from selenium.webdriver.common.by import By

sellers = (By.CSS_SELECTOR, "a.nav-a[href*='bestsellers']")
links = (By.ID, 'zg_tabs')

# @given('open amazon website')
# def open_amazon(context):
#     context.driver.get("https://www.amazon.com")
#     context.driver.maximize_window()
#     sleep(4)
@when('open Bestsellers')
def best_seller(context):
    context.driver.find_element(*sellers).click()
@then('Verify there are {expected_count} links')
def verify_links(context, expected_count):
    links_number = len(context.driver.find_elements(*links))
    assert int(expected_count) == links_number