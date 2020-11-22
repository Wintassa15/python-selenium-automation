from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page


class AmazonBabyDepartment(Page):
    DEPARTMENT = (By.ID, "searchDropdownBox")
    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.ID, "nav-search-submit-text")
    CURRENT_CATEGORY = (By.CSS_SELECTOR, ".nav-a.nav-b")

    # def open_amazon(self):
    #     self.open_page("https://www.amazon.com/")

    def select_baby_department(self):
        dd = self.find_element(*self.DEPARTMENT)
        select = Select(dd)
        select.select_by_value("search-alias=baby-products")

    def search_for_toy(self):
        self.input("VTech Pull and Sing Puppy", *self.SEARCH)

    def click_search_button(self):
        self.click(*self.SEARCH_ICON)

    def verify_baby_department_is_selected(self,):
        self.wait_for_element_appear(*self.CURRENT_CATEGORY)
       # self.driver.wait = WebDriverWait(self.driver, 15)

        #self.find_element(*self.CURRENT_CATEGORY)

