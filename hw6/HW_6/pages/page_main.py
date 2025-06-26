from hw6.pages.base_page import BasePage
from hw6.locators.loc_page_main import LocPageMain as loc


class PageMain(BasePage):

    def set_euro_currency(self):
        self.find(loc.CURRENCY_DROP_DOWN).click()
        self.find(loc.CURRENCY_EURO).click()
        self.driver.refresh()
        currency = self.find(loc.CURRENCY_DROP_DOWN)
        return currency

    def set_pound_currency(self):
        self.find(loc.CURRENCY_DROP_DOWN).click()
        self.find(loc.CURRENCY_POUND_STERLING).click()
        self.driver.refresh()
        currency = self.find(loc.CURRENCY_DROP_DOWN)
        return currency

    def set_us_dollar_currency(self):
        self.find(loc.CURRENCY_DROP_DOWN).click()
        self.find(loc.CURRENCY_US_DOLLAR).click()
        self.driver.refresh()
        currency = self.find(loc.CURRENCY_DROP_DOWN)
        return currency

    def get_cart_button(self):
        button = self.find(loc.CARD_BUTTON)
        return button

    def get_empty_card_message(self):
        self.get_cart_button().click()
        message = self.find(loc.EMPTY_CARD_MESSAGE)
        return message.text

    def get_navbar_panel(self):
        panel = self.find(loc.NAVBAR_PANEL)
        return panel

    def list_titles(self):
        navbar = self.find(loc.NAVBAR_TITLES)
        list_elements = navbar.text.split('\n')
        return list_elements

    def get_header_3(self):
        element = self.find(loc.TEXT_HEADER_3)
        return element

    def get_search_field(self):
        field = self.find(loc.SEARCH_FIELD)
        return field
