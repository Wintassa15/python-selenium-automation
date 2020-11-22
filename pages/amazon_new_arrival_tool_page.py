from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page


class AmazonNewArrivalTool(Page):
    NEW_ARRIVAL = (By.XPATH, "//*[@href='/s/ref=sr_hi_2/?_encoding=UTF8&bbn=17020138011&ie=UTF8&qid=1498592471&rh=n%3A7141123011%2Cn%3A17020138011&ref_=sv_sl_6']")
    DEALS= (By.CSS_SELECTOR, "div.mega-menu")

    def open_product_item(self):
        self.open_page("https://www.amazon.com/gp/product/B074TBCSC8")

    def hoover_new_arrival(self):
        new_arrival_button= self.find_element(*self.NEW_ARRIVAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival_button).perform()

    def verify_user_see_deals(self):
        self.wait_for_element_appear(*self.DEALS)
