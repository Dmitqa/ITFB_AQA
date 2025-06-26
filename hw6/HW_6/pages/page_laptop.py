from hw6.pages.base_page import BasePage
from hw6.locators.loc_page_laptop import LocPageLaptop as loc


class PageLaptop(BasePage):

    def get_compare_button(self):
        button = self.find(loc.COMPARE_BUTTON)
        return button

    def get_list_button(self):
        button = self.find(loc.LIST_BUTTON)
        return button

    def get_grid_button(self):
        button = self.find(loc.GRID_BUTTON)
        return button

    def get_sort_by_field(self):
        field = self.find(loc.SORT_BY_FIELD)
        return field
