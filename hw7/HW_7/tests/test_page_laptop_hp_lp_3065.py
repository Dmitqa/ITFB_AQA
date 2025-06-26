import pytest
import allure


@allure.epic("Test Laptop product page.")
@allure.feature("Product info.")
@allure.title("Check product title.")
def test_page_hp_lp_3065_title_text_title(laptop_card):
    title = laptop_card.get_title()
    assert title.text == "HP LP3065"


@allure.epic("Test Laptop product page.")
@allure.feature("Product info.")
@allure.title("Check product price.")
def test_page_hp_lp_3065_price_visible(laptop_card):
    price = laptop_card.get_price()
    assert price.is_displayed()
    assert price.text == "$122.00"


@allure.epic("Test Laptop product page.")
@allure.feature("Product move menu.")
@allure.title("Check cart move menu titles.")
@pytest.mark.parametrize("index, title", [
    (0, "Add to Wish List"),
    (1, "Compare this Product")])
def test_page_hp_lp_3065_card_menu_titles(laptop_card, index, title):
    titles = laptop_card.get_card_move_menu()
    assert titles[index].get_property("title") == title


@allure.epic("Test Laptop product page.")
@allure.feature("'Add to Cart' button.")
@allure.title("'Add to Cart' button is displayed.")
def test_page_hp_lp_3065_add_to_card_btn_visible(laptop_card):
    add_to_card_btn = laptop_card.add_to_card_button()
    assert add_to_card_btn.is_displayed()


@allure.epic("Test Laptop product page.")
@allure.feature("'Add to Cart' button.")
@allure.title("'Add to Cart' button is enabled.")
def test_page_hp_lp_3065_add_to_card_btn_clickable(laptop_card):
    add_to_card_btn = laptop_card.add_to_card_button()
    assert add_to_card_btn.is_enabled()
