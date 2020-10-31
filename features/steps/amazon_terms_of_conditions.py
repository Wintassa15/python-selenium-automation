from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

LINKS = (By.XPATH, "//a[contains(text(), 'Amazon applications')]")
APP_PAGE = (By.CSS_SELECTOR, "div #mgt-email-sms-left")


@given("Open Amazon T&C page")
def open_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref"
                       "=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def store_original_window(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    print(context.original_windows)


@when("Click on Amazon applications link")
def click_link(context):
    links = context.driver.find_element(*LINKS)
    links.click()


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    # context.driver.wait = context.WebDriverwait(context.driver,15)
    #context.wait.until(EC.new_window_is_opened)
    new_windows = context.driver.window_handles
    print(new_windows)
    for window in context.original_windows:
        new_windows.remove(window)
        print(new_windows)
        context.driver.switch_to_window(new_windows[0])


@then("Amazon app page is opened")
def amazon_page_opened(context):
    context.driver.find_element(*APP_PAGE)


@then("User can close new window and switch back to original")
def switch_to_original_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
