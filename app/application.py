from pages.amazon_baby_department_page import AmazonBabyDepartment
from pages.amazon_music_page import AmazonMusic
from pages.amazon_new_arrival_tool_page import AmazonNewArrivalTool
from pages.amazon_product_page import AmazonProduct
from pages.amazon_shopping_page import AmazonShopping
from pages.amazon_size_selection_tool import AmazonSizeSelectionTool
from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.amazon_shopping_page = AmazonShopping(self.driver)
        self.amazon_music_page = AmazonMusic(self.driver)
        self.amazon_size_selection_tool = AmazonSizeSelectionTool(self.driver)
        self.amazon_product_page = AmazonProduct(self.driver)
        self.amazon_baby_department_page = AmazonBabyDepartment(self.driver)
        self.amazon_new_arrival_tool_page = AmazonNewArrivalTool(self.driver)
