import allure
from hw7.pages.base_page import BasePage
from hw7.locators.loc_page_login import LocPageLogin as loc


class PageLogin(BasePage):

    @allure.title("Identify 'New Customer' window.")
    def get_new_customer_window(self):
        window = self.find(loc.NEW_CUSTOMER_WINDOW)
        return window

    @allure.title("Identify 'New Customer' window header.")
    def get_new_customer_window_header(self):
        header = self.find(loc.NEW_CUSTOMER_HEADER)
        return header

    @allure.title("Identify 'Continue' button.")
    def get_new_customer_continue_button(self):
        button = self.find(loc.NEW_CUSTOMER_CONTINUE_BUTTON)
        return button

    @allure.title("Identify 'E-Mail Address' field.")
    def get_returning_customer_email_field(self):
        field = self.find(loc.RETURN_CUSTOMER_EMAIL)
        return field

    @allure.title("Get entered in 'E-Mail Address' field text.")
    def get_text_from_returning_customer_email_field(self):
        field = self.get_returning_customer_email_field()
        field.send_keys(loc.RETURN_CUSTOMER_EMAIL_TEXT)
        return field
