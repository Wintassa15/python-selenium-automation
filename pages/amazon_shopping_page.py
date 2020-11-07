from selenium.webdriver.common.by import By

from pages.base_page import Page


class AmazonShopping(Page):
    CART_1 = (By.ID, 'nav-cart-count-container')
    SEARCH_WORD = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')

    def open_amazon(self):
        self.open_page('https://www.amazon.com')

    def click_cart(self):
        self.click(*self.CART_1)

    def verify_shopping_cart(self):
        self.verify_text('Your Amazon Cart is empty',*self.SEARCH_WORD )