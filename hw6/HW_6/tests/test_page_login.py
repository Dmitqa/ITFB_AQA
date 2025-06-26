from hw6.locators.loc_page_login import LocPageLogin as loc


def test_page_login_modal_window_new_customer_visible(page_login):
    window = page_login.get_new_customer_window()
    assert window.is_displayed()


def test_page_login_modal_window_new_customer_header(page_login):
    window = page_login.get_new_customer_window_header()
    assert window.text == "New Customer"


def test_page_login_new_customer_continue_button_visible(page_login):
    continue_button = page_login.get_new_customer_continue_button()
    assert continue_button.is_displayed()


def test_page_login_returning_customer_email_field_visible(page_login):
    email_field = page_login.get_returning_customer_email_field()
    assert email_field.is_displayed()


def test_page_login_returning_customer_email_text_in_field(page_login):
    email_field = page_login.get_text_from_returning_customer_email_field()
    assert email_field.get_attribute("value") == loc.RETURN_CUSTOMER_EMAIL_TEXT
