import pytest
from hw7.pages.page_main import PageMain
import allure


@allure.epic("Test main page.")
@allure.feature("Selection currency.")
@allure.title("Selected € Currency.")
def test_page_main_set_euro_currency(driver):
    currency = PageMain(driver).set_euro_currency()
    assert currency.text == "€ Currency"


@allure.epic("Test main page.")
@allure.feature("Selection currency.")
@allure.title("Selected £ Currency.")
def test_page_main_set_pound_sterling_currency(driver):
    currency = PageMain(driver).set_pound_currency()
    assert currency.text == "£ Currency"


@allure.epic("Test main page.")
@allure.feature("Selection currency.")
@allure.title("Selected $ Currency.")
def test_page_main_set_us_dollar_currency(driver):
    currency = PageMain(driver).set_us_dollar_currency()
    assert currency.text == "$ Currency"


@allure.epic("Test main page.")
@allure.feature("'Cart shopping' button.")
@allure.title("'Cart shopping' button is displayed.")
def test_page_main_cart_btn_visible(driver):
    cart_btn = PageMain(driver).get_cart_button()
    assert cart_btn.is_displayed()


@allure.epic("Test main page.")
@allure.feature("'Cart shopping' button.")
@allure.title("'Cart shopping' button(empty) message if click.")
def test_page_main_click_empty_cart_btn(driver):
    message = PageMain(driver).get_empty_card_message()
    assert message == "Your shopping cart is empty!"


@allure.epic("Test main page.")
@allure.feature("'Navbar' panel.")
@allure.title("'Navbar' panel is displayed.")
def test_page_main_navbar_panel_visible(driver):
    navbar_panel = PageMain(driver).get_navbar_panel()
    assert navbar_panel.is_displayed()


@allure.epic("Test main page.")
@allure.feature("'Navbar' panel.")
@allure.title("All 'Navbar' elements are existed and displayed.")
@pytest.mark.parametrize("index, title", [
    (0, "Desktops"),
    (1, "Laptops & Notebooks"),
    (2, "Components"),
    (3, "Tablets"),
    (4, "Software"),
    (5, "Phones & PDAs"),
    (6, "Cameras"),
    (7, "MP3 Players")])
def test_page_main_navbar_titles(driver, index, title):
    title_list = PageMain(driver).list_titles()
    assert title_list[index] == title


@allure.epic("Test main page.")
@allure.feature("Headers.")
@allure.title("Check header#3 text.")
def test_page_main_header_3_text(driver):
    header = PageMain(driver).get_header_3()
    assert header.text == "Featured"


@allure.epic("Test main page.")
@allure.feature("Search field.")
@allure.title("Check search field placeholder text.")
def test_page_main_search_field_placeholder(driver):
    field = PageMain(driver).get_search_field()
    assert field.get_attribute("placeholder") == 'Search'
