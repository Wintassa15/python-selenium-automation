from time import sleep
from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium import webdriver

cart_1 = (By.ID, 'nav-cart-count-container')
SEARCH_WORD = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
# driver = webdriver.Chrome(
#     executable_path="/Users/wintana/JobEasy-QAAutomation/python-selenium-automation/chromedriver-2")


@Given('Open Amazon')
def open_amazon(context):
    # context.driver.get("https://www.amazon.com")
    # context.driver.maximize_window()
    # sleep(4)

    context.app.amazon_shopping_page.open_amazon()


@When('click on Cart')
def click_cart(context):
    # search = context.driver.find_element(*cart_1)
    # search.click()
    context.app.amazon_shopping_page.click_cart()

@Then('verify shopping cart is empty')
def verify_shopping_cart(context):
    # search_word = context.driver.find_element(*SEARCH_WORD)
    # assert 'Your Amazon Cart is empty' in search_word.text, f'expected "Your Amazon Cart is empty" but got {search_word.text}'
    context.app.amazon_shopping_page.verify_shopping_cart()