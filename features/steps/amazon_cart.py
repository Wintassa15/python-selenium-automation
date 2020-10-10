from selenium import webdriver
from behave import Given, When, Then
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path="/Users/wintana/JobEasy-QAAutomation/python-selenium-automation/chromedriver-2")
search = (By.ID, 'twotabsearchtextbox')
search_icon = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
select_item = (By.CSS_SELECTOR, "img.s-image[src='https://m.media-amazon.com/images/I/811mZ5F0YVL._AC_UL320_.jpg']")
add_cart = (By.CSS_SELECTOR, "input#add-to-cart-button")
number_items = (By.XPATH, "//span[@class='sc-without-fresh-inline']")


@Given('open amazon website')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    context.driver.maximize_window()
    sleep(4)


@When('input teddy bear into search field')
def teddy_bear_search(context):
    search_item = context.driver.find_element(*search).click()
    context.driver.send_keys("teddy bear")
    search_icon.click()


@Then('select an item')
def select(context):
    context.driver.find_element(*select_item).click()


@Then('add to cart')
def add_item(context):
    context.driver.find_element(*add_cart).click()


@Then('verify number of items')
def verify_number(context):
    verify = context.driver.find_element(*number_items)
    assert 'Subtotal (1 item)' in verify.text
