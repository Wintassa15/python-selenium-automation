
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

search = (By.ID, 'twotabsearchtextbox')
search_icon = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
select_item = (By.CSS_SELECTOR, "img.s-image[src='https://m.media-amazon.com/images/I/811mZ5F0YVL._AC_UL320_.jpg']")
add_cart = (By.CSS_SELECTOR, "input#add-to-cart-button")
#number_items = (By.XPATH, "//span[@class='sc-without-fresh-inline']")
number_items=(By.ID, 'sc-subtotal-label-buybox')
open_cart = (By.CSS_SELECTOR, "nav-cart")


@given('open amazon website')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    context.driver.maximize_window()
    sleep(4)


@when('input teddy bear into search field')
def teddy_bear_search(context):
    search_item = context.driver.find_element(*search)
    search_item .send_keys("teddy bear")
    context.driver.find_element(*search_icon).click()
    #search_icon.click()
    sleep(3)


@when('click on the product')
def click_product(context):
    context.driver.find_element(*select_item).click()


@when('click on add to cart')
def add_item(context):
    context.driver.find_element(*add_cart).click()


@then('verify number of items')
def verify_number(context):
    context.driver.find_element(*open_cart).click()
    verify = context.driver.find_element(*number_items)
    assert 'Subtotal (1 item)' in verify.text
