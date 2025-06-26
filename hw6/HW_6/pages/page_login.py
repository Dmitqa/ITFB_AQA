from hw6.pages.base_page import BasePage
from hw6.locators.loc_page_login import LocPageLogin as loc


class PageLogin(BasePage):

    def get_new_customer_window(self):
        window = self.find(loc.NEW_CUSTOMER_WINDOW)
        return window

    def get_new_customer_window_header(self):
        window = self.find(loc.NEW_CUSTOMER_HEADER)
        return window

    def get_new_customer_continue_button(self):
        button = self.find(loc.NEW_CUSTOMER_CONTINUE_BUTTON)
        return button

    def get_returning_customer_email_field(self):
        field = self.find(loc.RETURN_CUSTOMER_EMAIL)
        return field

    def get_text_from_returning_customer_email_field(self):
        field = self.get_returning_customer_email_field()
        field.send_keys(loc.RETURN_CUSTOMER_EMAIL_TEXT)
        return field
