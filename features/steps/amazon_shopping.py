from time import sleep
from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium import webdriver


cart_1 = (By.ID, 'nav-cart-count-container')
driver = webdriver.Chrome(
    executable_path="/Users/wintana/JobEasy-QAAutomation/python-selenium-automation/chromedriver-2")


@Given('Open Amazon')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    context.driver.maximize_window()
    sleep(4)


@When('click on Cart')
def click_cart(context):
    search = context.driver.find_element(*cart_1)
    search.click()

@Then('verify shopping cart is empty')
def verify_shopping_cart(context):
    search_word = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    assert 'Your Amazon Cart is empty' in search_word.text, f'expected "Your Amazon Cart is empty" but got {search_word.text}'
