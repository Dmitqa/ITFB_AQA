import allure
from hw7.locators.loc_page_register import LocPageRegister as loc


@allure.epic("Test Register page.")
@allure.feature("Create new account.")
@allure.title("Create new account with exist Email address.")
def test_page_register_new_account_negative(page_register):
    alert = page_register.create_new_account()
    assert alert.text == "Warning: E-Mail Address is already registered!"


@allure.epic("Test Register page.")
@allure.feature("Register account window.")
@allure.title("Window is displayed.")
def test_page_register_window_visible(page_register):
    window = page_register.get_page_register_window()
    assert window.is_displayed()


@allure.epic("Test Register page.")
@allure.feature("Register account window.")
@allure.title("Check window header text.")
def test_page_register_window_header(page_register):
    title = page_register.get_page_register_window_header()
    assert title.text == "Register Account"


@allure.epic("Test Register page.")
@allure.feature("Register account window.")
@allure.title("Check 'First name' field value after filling.")
def test_page_register_field_firstname_test_value(page_register):
    field_text = page_register.get_firstname_field_value()
    assert field_text.get_attribute("value") == loc.FIRST_NAME_TEST


@allure.epic("Test Register page.")
@allure.feature("Register account window.")
@allure.title("Check 'Last name' field value after filling.")
def test_page_register_field_lastname_test_value(page_register):
    field_text = page_register.get_lastname_field_value()
    assert field_text.get_attribute("value") == loc.LAST_NAME_TEST


@allure.epic("Test Register page.")
@allure.feature("Register account window.")
@allure.title("'Privacy Policy' check box is not selected.")
def test_page_register_privacy_policy_check_box_visible(page_register):
    box = page_register.get_privacy_policy_check_box()
    assert not box.is_selected()
