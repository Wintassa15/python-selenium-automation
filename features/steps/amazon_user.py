from behave import Given, When, Then
from selenium.webdriver.common.by import By

# select = (By.ID, 'nav-orders')
# sign_in = (By.XPATH, "//h1[@class='a-spacing-small']")


@Given('open Amazon page')
def open_amazon(context):
     # context.driver.get('https://www.amazon.com/')
     # context.driver.maximize_window()
     # context.driver.implicitly_wait(4)
    context.app.main_page.open_amazon()


@When('select orders')
def select_orders(context):
    #context.driver.find_element(By.ID, 'nav-orders').click
    context.app.main_page.select_orders()

@Then('Sign in page opens')
def sign_in(context):
    # search_word = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    # assert search_word == 'Sign-In 'f'expected result Sign-In but got {search_word.text} '
    #context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
    context.app.main_page.sign_in()