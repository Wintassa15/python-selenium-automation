from behave import given, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name span.selection ")


@given('open amazon {productid} page')
def open_amazon_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('verify that user can select colors')
def user_select_color(context):

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        assert context.driver.find_element(*SELECTED_COLOR).text != ''


