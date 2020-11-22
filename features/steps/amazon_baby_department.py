from behave import given, when, then


# @given("Open Amazon Page")
# def open_amazon(context):
#     context.app.amazon_baby_department_page.open_amazon()


@when("Select Baby Department")
def select_baby_department(context):
    context.app.amazon_baby_department_page.select_baby_department()


@when("Search for VTech Pull and Sing Puppy")
def search_for_toy(context):
    context.app.amazon_baby_department_page.search_for_toy()


@then("Verify Baby department is selected")
def verify_baby_department_is_selected(context):
    context.app.amazon_baby_department_page.verify_baby_department_is_selected()
