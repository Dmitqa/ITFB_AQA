from hw7.locators.loc_page_admin import LocPageAdmin as loc
import allure


@allure.epic("Test Admin page.")
@allure.feature("Add new product in 'Catalog/Products'.")
@allure.title("New product add in Products.")
def test_page_admin_add_new_product(driver, admin):
    admin.login_admin(loc.LOGIN_ADM_USERNAME, loc.LOGIN_ADM_PASSWORD)
    admin.go_to_catalog_products()
    admin.add_new_product()
    search_result = admin.check_new_product_name_in_filter()
    assert loc.PRODUCT_NAME_TEXT in search_result.text


@allure.epic("Test Admin page.")
@allure.feature("Delete existing product from 'Catalog/Products'.")
@allure.title("Deleted product not in Products.")
def test_page_admin_delete_existing_product(driver, admin):
    admin.login_admin(loc.LOGIN_ADM_USERNAME, loc.LOGIN_ADM_PASSWORD)
    admin.go_to_catalog_products()
    admin.check_new_product_name_in_filter()
    admin.delete_existing_product()
    search_result = admin.check_deleted_product()
    assert search_result.text == 'No results!'
