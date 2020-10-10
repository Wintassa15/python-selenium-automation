from selenium import webdriver
from behave import Given, When, Then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
@Given('open amazon help')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
@When('input cancel orders')
def input_cancel(context):
    input_field = context.driver.find_element(By.ID, 'helpsearch')
    input_field.clear()
    input_field.send_keys('cancel orders', Keys.ENTER)
    sleep(4)
@Then('verify cancel orders')
def cancel(context):
    result = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]")
    assert result.text == 'Cancel Items or Orders', f'expected result cancel orders but got {result.text} '
