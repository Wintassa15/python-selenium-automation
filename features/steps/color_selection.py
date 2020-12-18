from behave import given, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name span.selection ")


@given('open amazon {productid} page')
def open_amazon_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('verify that user can select colors')
def user_select_color(context):
    # expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse',
    #                    'Light Wash']
    #expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Vintage Light Wash', 'Washed Black', 'Rinsed Vintage']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    # for i in range(len(colors)):
    #     colors(i).click()
    #     color_text = context.driver.find_element(*SELECTED_COLOR).text
    #     assert color_text == expected_colors[i], f'colors do not match. Expected {expected_colors[i]} but got ' \
    #                                                   f'{color_text}'

    for color in colors:
        color.click()
        assert context.driver.find_element(*SELECTED_COLOR).text != ''



