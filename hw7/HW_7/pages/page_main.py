import allure
from hw7.pages.base_page import BasePage
from hw7.locators.loc_page_main import LocPageMain as loc


class PageMain(BasePage):

    @allure.title("Selection Euro as a current currency.")
    def set_euro_currency(self):
        with allure.step("Click on 'Currency' menu."):
            self.clicking(self.find(loc.CURRENCY_DROP_DOWN))
        with allure.step("Select 'Euro' from dropdown menu."):
            self.clicking(self.find(loc.CURRENCY_EURO))
        with allure.step("Refresh page."):
            self.driver.refresh()
        with allure.step("'Euro' selected as a current currency."):
            currency = self.find(loc.CURRENCY_DROP_DOWN)
        return currency

    @allure.title("Selection Pound sterling as a current currency.")
    def set_pound_currency(self):
        with allure.step("Click on 'Currency' menu."):
            self.clicking(self.find(loc.CURRENCY_DROP_DOWN))
        with allure.step("Select 'Pound sterling' from dropdown menu."):
            self.clicking(self.find(loc.CURRENCY_POUND_STERLING))
        with allure.step("Refresh page."):
            self.driver.refresh()
        with allure.step("'Pound sterling' selected as a current currency."):
            currency = self.find(loc.CURRENCY_DROP_DOWN)
        return currency

    @allure.title("Selection US dollar as a current currency.")
    def set_us_dollar_currency(self):
        with allure.step("Click on 'Currency' menu."):
            self.clicking(self.find(loc.CURRENCY_DROP_DOWN))
        with allure.step("Select 'US dollar' from dropdown menu."):
            self.clicking(self.find(loc.CURRENCY_US_DOLLAR))
        with allure.step("Refresh page."):
            self.driver.refresh()
        with allure.step("'US dollar' selected as a current currency."):
            currency = self.find(loc.CURRENCY_DROP_DOWN)
        return currency

    @allure.title("Identify 'Cart shopping' button.")
    def get_cart_button(self):
        button = self.find(loc.CARD_BUTTON)
        return button

    @allure.title("Get message if click on Cart shopping(empty) button.")
    def get_empty_card_message(self):
        with allure.step("Identify and click 'Cart shopping' button."):
            self.clicking(self.get_cart_button())
        with allure.step("Get massage after click."):
            message = self.find(loc.EMPTY_CARD_MESSAGE)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'screenshot',
                attachment_type=allure.attachment_type.PNG)
        return message.text

    @allure.title("Identify 'Navbar' panel.")
    def get_navbar_panel(self):
        panel = self.find(loc.NAVBAR_PANEL)
        return panel

    @allure.title("Get list of navbar titles.")
    def list_titles(self):
        with allure.step("Identify navbar panel."):
            navbar = self.find(loc.NAVBAR_TITLES)
        with allure.step("Get navbar titles list."):
            list_elements = navbar.text.split('\n')
        return list_elements

    @allure.title("Identify Header #3.")
    def get_header_3(self):
        element = self.find(loc.TEXT_HEADER_3)
        return element

    @allure.title("Identify search field.")
    def get_search_field(self):
        field = self.find(loc.SEARCH_FIELD)
        return field
