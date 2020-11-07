from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class AmazonMusic(Page):
    HUMBERGER_MENU = (By.ID, 'nav-hamburger-menu')
    MUSIC_MENU = (By.XPATH, "//div[text()='Amazon Music']")
    MENU_ITEMS = (By.CSS_SELECTOR, "ul.hmenu-visible li a[class = 'hmenu-item']")

    # def open_amazon(self):
    #     self.open_page('https://www.amazon.com')

    def click_on_hamburger_menu(self):
        self.click(*self.HUMBERGER_MENU)

    def click_on_amazon_music_menu(self):
        self.click(*self.MUSIC_MENU)


    def verify_items_are_present(self):
        self.find_elements(*self.MENU_ITEMS)
        sleep(4)
        links_number = len(self.MENU_ITEMS)
        assert 7 == links_number, f'expected 7 but got {links_number}'

