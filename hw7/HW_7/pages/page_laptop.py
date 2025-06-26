import allure

from hw7.pages.base_page import BasePage
from hw7.locators.loc_page_laptop import LocPageLaptop as loc
# from hw7.loggers import logger_console


class PageLaptop(BasePage):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.logger = logger_console

    @allure.title("Identify 'Product Compare' button.")
    def get_compare_button(self):
        button = self.find(loc.COMPARE_BUTTON)
        return button

    @allure.title("Identify 'List' button.")
    def get_list_button(self):
        button = self.find(loc.LIST_BUTTON)
        return button

    @allure.title("Identify 'Grid' button.")
    def get_grid_button(self):
        button = self.find(loc.GRID_BUTTON)
        return button

    @allure.title("Identify 'Sort By' field.")
    def get_sort_by_field(self):
        field = self.find(loc.SORT_BY_FIELD)
        return field
