from hw6.pages.base_page import BasePage
from hw6.locators.loc_page_register import LocPageRegister as loc
from selenium.webdriver.common.action_chains import ActionChains


class PageRegister(BasePage):

    def create_new_account(self):
        firstname = self.find(loc.FIRST_NAME_FIELD)
        lastname = self.find(loc.LAST_NAME_FIELD)
        email = self.find(loc.EMAIL_FIELD)
        password = self.find(loc.PASSWORD_FIELD)
        continue_btn = self.find(loc.CONTINUE_BUTTON)
        policy = self.find(loc.PRIVATE_POLICY_CHECK_BOX)

        (ActionChains(self.driver).click(firstname).send_keys(loc.FIRST_NAME_TEST)
         .click(lastname).send_keys(loc.LAST_NAME_TEST)
         .click(email).send_keys(loc.EMAIL_TEST)
         .click(password).send_keys(loc.PASSWORD_TEST)
         .click(policy).click(continue_btn).perform())

        alert = self.find(loc.ALREADY_REG_ALERT)
        return alert

    def get_page_register_window(self):
        window = self.find(loc.REG_ACCOUNT_WINDOW)
        return window

    def get_page_register_window_header(self):
        window = self.find(loc.REG_ACCOUNT_WINDOW_HEADER)
        return window

    def get_firstname_field_value(self):
        field = self.find(loc.FIRST_NAME_FIELD)
        field.send_keys(loc.FIRST_NAME_TEST)
        return field

    def get_lastname_field_value(self):
        field = self.find(loc.LAST_NAME_FIELD)
        field.send_keys(loc.LAST_NAME_TEST)
        return field

    def get_privacy_policy_check_box(self):
        box = self.find(loc.PRIVATE_POLICY_CHECK_BOX)
        return box
