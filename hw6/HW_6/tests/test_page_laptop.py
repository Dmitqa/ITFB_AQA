from hw6.pages.page_laptop import PageLaptop


def test_page_laptop_compare_btn_visible(driver, click_laptop):
    compare_btn = PageLaptop(driver).get_compare_button()
    assert compare_btn.is_displayed()


def test_page_laptop_compare_btn_text(driver, click_laptop):
    compare_btn = PageLaptop(driver).get_compare_button()
    assert compare_btn.text == "Product Compare (0)"


def test_page_laptop_list_btn_visible(driver, click_laptop):
    list_btn = PageLaptop(driver).get_list_button()
    assert list_btn.is_displayed()


def test_page_laptop_grid_btn_visible(driver, click_laptop):
    grid_btn = PageLaptop(driver).get_grid_button()
    assert grid_btn.is_displayed()


def test_page_laptop_sort_by_field_visible(driver, click_laptop):
    sort_by_field = PageLaptop(driver).get_sort_by_field()
    assert sort_by_field.is_displayed()


def test_page_laptop_sort_by_field_text(driver, click_laptop):
    sort_by_field = PageLaptop(driver).get_sort_by_field()
    assert sort_by_field.text == "Default"
