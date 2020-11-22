from behave import given, when, then


@given("Open Amazon B074TBCSC8 product item")
def open_product_item(context):
    context.app.amazon_new_arrival_tool_page.open_product_item()


@when("hoover over New arrivals")
def hoover_new_arrival(context):
    context.app.amazon_new_arrival_tool_page.hoover_new_arrival()


@then("Verify user sees all the deals")
def verify_user_see_deals(context):
    context.app.amazon_new_arrival_tool_page.verify_user_see_deals()
