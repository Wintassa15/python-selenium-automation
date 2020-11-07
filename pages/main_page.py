from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDERS_ICON = (By.ID, 'nav-orders')
    SIGN_IN = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def open_amazon(self):
        self.open_page('https://www.amazon.com')

    def select_orders(self):
        self.click(*self.ORDERS_ICON)

    # Check Below
    def sign_in(self):
        self.find_element(*self.SIGN_IN)
