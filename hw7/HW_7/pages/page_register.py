import allure
from hw7.pages.base_page import BasePage
from hw7.locators.loc_page_register import LocPageRegister as loc
from selenium.webdriver.common.action_chains import ActionChains


class PageRegister(BasePage):

    @allure.title("Create new account.")
    def create_new_account(self):
        with allure.step("Filling required fields"):
            firstname = self.find(loc.FIRST_NAME_FIELD)
            lastname = self.find(loc.LAST_NAME_FIELD)
            email = self.find(loc.EMAIL_FIELD)
            password = self.find(loc.PASSWORD_FIELD)
            new_account_fields = [firstname, lastname, email, password]
            new_account_values = [loc.FIRST_NAME_TEST, loc.LAST_NAME_TEST, loc.EMAIL_TEST, loc.PASSWORD_TEST]
            self.filling(new_account_fields, new_account_values)
        with allure.step("Accept private policy."):
            policy = self.find(loc.PRIVATE_POLICY_CHECK_BOX)
            ActionChains(self.driver).click(policy).perform()
        with allure.step("Press 'Continue' button."):
            continue_btn = self.find(loc.CONTINUE_BUTTON)
            self.clicking(continue_btn)
        with allure.step("Get alert banner after create new account"):
            alert = self.find(loc.ALREADY_REG_ALERT)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'screenshot',
                attachment_type=allure.attachment_type.PNG)
        return alert

    @allure.title("Get 'Register Account' window.")
    def get_page_register_window(self):
        window = self.find(loc.REG_ACCOUNT_WINDOW)
        return window

    @allure.title("Get 'Register Account' window header.")
    def get_page_register_window_header(self):
        window = self.find(loc.REG_ACCOUNT_WINDOW_HEADER)
        return window

    @allure.title("Fill value in 'First name' field.")
    def get_firstname_field_value(self):
        field = self.find(loc.FIRST_NAME_FIELD)
        self.filling([field], [loc.FIRST_NAME_TEST])
        return field

    @allure.title("Fill value in 'Last name' field.")
    def get_lastname_field_value(self):
        field = self.find(loc.LAST_NAME_FIELD)
        self.filling([field], [loc.LAST_NAME_TEST])
        return field

    @allure.title("Get 'Privacy Policy' check box.")
    def get_privacy_policy_check_box(self):
        box = self.find(loc.PRIVATE_POLICY_CHECK_BOX)
        return box
