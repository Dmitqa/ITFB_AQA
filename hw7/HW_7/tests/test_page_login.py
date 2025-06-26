import allure

from hw7.locators.loc_page_login import LocPageLogin as loc


@allure.epic("Test Login page.")
@allure.feature("'New Customer' window.")
@allure.title("'New Customer' window is displayed.")
def test_page_login_modal_window_new_customer_visible(page_login):
    window = page_login.get_new_customer_window()
    assert window.is_displayed()


@allure.epic("Test Login page.")
@allure.feature("'New Customer' window.")
@allure.title("'New Customer' window header text.")
def test_page_login_modal_window_new_customer_header(page_login):
    header = page_login.get_new_customer_window_header()
    assert header.text == "New Customer"


@allure.epic("Test Login page.")
@allure.feature("'New Customer' window.")
@allure.title("'New Customer' 'Continue' button is displayed.")
def test_page_login_new_customer_continue_button_visible(page_login):
    continue_button = page_login.get_new_customer_continue_button()
    assert continue_button.is_displayed()


@allure.epic("Test Login page.")
@allure.feature("'Returning Customer' window.")
@allure.title("'E-Mail Address' field is displayed.")
def test_page_login_returning_customer_email_field_visible(page_login):
    email_field = page_login.get_returning_customer_email_field()
    assert email_field.is_displayed()


@allure.epic("Test Login page.")
@allure.feature("'Returning Customer' window.")
@allure.title("'Entered in 'E-Mail Address' field text.")
def test_page_login_returning_customer_email_text_in_field(page_login):
    email_field = page_login.get_text_from_returning_customer_email_field()
    assert email_field.get_attribute("value") == loc.RETURN_CUSTOMER_EMAIL_TEXT
