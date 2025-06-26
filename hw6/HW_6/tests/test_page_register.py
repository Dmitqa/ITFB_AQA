from hw6.locators.loc_page_register import LocPageRegister as loc


def test_page_register_new_account_positive(page_register):
    alert = page_register.create_new_account()
    assert alert.text == "Warning: E-Mail Address is already registered!"


def test_page_register_window_visible(page_register):
    window = page_register.get_page_register_window()
    assert window.is_displayed()


def test_page_register_window_header(page_register):
    title = page_register.get_page_register_window_header()
    assert title.text == "Register Account"


def test_page_register_field_firstname_test_value(page_register):
    field_text = page_register.get_firstname_field_value()
    assert field_text.get_attribute("value") == loc.FIRST_NAME_TEST


def test_page_register_field_lastname_test_value(page_register):
    field_text = page_register.get_lastname_field_value()
    assert field_text.get_attribute("value") == loc.LAST_NAME_TEST


def test_page_register_privacy_policy_check_box_visible(page_register):
    box = page_register.get_privacy_policy_check_box()
    assert not box.is_selected()
