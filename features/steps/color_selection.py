from behave import given, then
from selenium.webdriver.common.by import By

COLOR_OPTION = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name span.selection ")


@given('open amazon {product_id} page')
def open_amazon_page(context, product_id):
    context.driver.get("https://www.amazon.com/gp/product/{product_id}/")


@then('verify that user can select colors')
def user_select_color(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse',
                       'Light Wash']
    colors = context.driver.find_elements(*COLOR_OPTION)
    for i in range(len(colors)):
        colors(i).click()
        selected_colors = context.driver.find_element(*SELECTED_COLOR).text
        assert selected_colors == expected_colors[i], f'colors do not match. Expected {expected_colors[i]} but got ' \
                                                      f'{selected_colors}'
