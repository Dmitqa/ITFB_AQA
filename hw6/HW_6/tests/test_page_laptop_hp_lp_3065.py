import pytest


def test_page_hp_lp_3065_title_text_title(laptop_card):
    title = laptop_card.get_title()
    assert title.text == "HP LP3065"


def test_page_hp_lp_3065_price_visible(laptop_card):
    price = laptop_card.get_price()
    assert price.is_displayed()
    assert price.text == "$122.00"


@pytest.mark.parametrize("index, title", [
    (0, "Add to Wish List"),
    (1, "Compare this Product")])
def test_page_hp_lp_3065_card_menu_titles(laptop_card, index, title):
    titles = laptop_card.get_card_move_menu()
    assert titles[index].get_property("title") == title


def test_page_hp_lp_3065_add_to_card_btn_visible(laptop_card):
    add_to_card_btn = laptop_card.add_to_card_button()
    assert add_to_card_btn.is_displayed()


def test_page_hp_lp_3065_add_to_card_btn_clickable(laptop_card):
    add_to_card_btn = laptop_card.add_to_card_button()
    assert add_to_card_btn.is_enabled()
