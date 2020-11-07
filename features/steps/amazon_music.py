from behave import given, when, then


# @given('Open Amazon page')
# def open_amazon(context):
#     context.app.amazon_music_page.open_amazon()


@when('Click on hamburger menu')
def click_on_hamburger_menu(context):
    context.app.amazon_music_page.click_on_hamburger_menu()


@when('Click on Amazon Music menu item')
def click_on_amazon_music_menu(context):
    context.app.amazon_music_page.click_on_amazon_music_menu()


@then('7 menu items are present')
def verify_items_are_present(context):
    context.app.amazon_music_page.verify_items_are_present()

