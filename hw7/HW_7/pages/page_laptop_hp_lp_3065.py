import allure
from hw7.pages.base_page import BasePage
from hw7.locators.loc_page_laptop_hp_lp_3065 import LocPageLaptopHplp3065 as loc


class PageLaptopHpLp3065(BasePage):

    @allure.title("Get product title.")
    def get_title(self):
        title = self.find(loc.HEADER_1)
        return title

    @allure.title("Get product price.")
    def get_price(self):
        title = self.find(loc.PRICE)
        return title

    @allure.title("Identify cart move menu.")
    def get_card_move_menu(self):
        menu = self.find_all(loc.CARD_MOVE_MENU)
        return menu

    @allure.title("Identify 'Add to Cart' button.")
    def add_to_card_button(self):
        button = self.find(loc.ADD_TO_CARD_BUTTON)
        return button
