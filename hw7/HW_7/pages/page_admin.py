import allure
from hw7.pages.base_page import BasePage
from hw7.locators.loc_page_admin import LocPageAdmin as loc


class PageAdmin(BasePage):

    @allure.title("Login Administration")
    def login_admin(self, username, password):
        with allure.step("Filling Login window fields."):
            username_field = self.find(loc.USERNAME_PATH)
            password_field = self.find(loc.PASSWORD_PATH)
            login_fields = [username_field, password_field]
            login_passwords = [username, password]
            self.filling(login_fields, login_passwords)
        with allure.step("Click 'Continue' button."):
            self.clicking(self.find(loc.LOGIN_PATH))

    @allure.title("Go to: 'Catalog/Products'")
    def go_to_catalog_products(self):
        self.clicking(self.find(loc.CATALOG))
        self.clicking(self.find(loc.PRODUCTS))

    @allure.title("Add new product in 'Products'.")
    def add_new_product(self):
        with allure.step("Go to 'Add product' page."):
            self.clicking(self.find(loc.ADD_PRODUCT_BUTTON))
        with allure.step("Get alert banner."):
            alert = self.find(loc.ALERT_CROSS)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'screenshot',
                attachment_type=allure.attachment_type.PNG)
            self.clicking(alert)
        with allure.step("Filling 'General' tab."):
            general_tab = self.find(loc.GENERAL_TAB)
            product_name_field = self.find(loc.PRODUCT_NAME_FIELD)
            meta_tag_field = self.find(loc.META_TAG_FIELD)
            fields = [product_name_field, meta_tag_field]
            values = [loc.PRODUCT_NAME_TEXT, loc.META_TAG_TEXT]
            self.filling(fields, values)
        with allure.step("Go to 'Data' tab and fillings fields."):
            self.clicking(self.find(loc.DATA_TAB))
            data_model_field = self.find(loc.DATA_MODEL_FIELD)
            self.filling([data_model_field], [loc.DATA_MODEL_TEXT])
        with allure.step("Go to 'SEO' tab and fillings fields."):
            self.clicking(self.find(loc.SEO_TAB))
            seo_keyword_field = self.find(loc.SEO_KEYWORD_FIELD)
            self.filling([seo_keyword_field], [loc.SEO_KEYWORD_TEXT])
        with allure.step("Go back to 'General' tab."):
            self.clicking(general_tab)
        with allure.step("Click 'Save' button."):
            self.clicking(self.find(loc.SAVE_BUTTON))
        with allure.step("Go back to 'Catalog/Products'."):
            self.clicking(self.find(loc.PRODUCTS))

    @allure.title("Find product in Products filter")
    def check_new_product_name_in_filter(self):
        with allure.step("Fill in search field product name and click 'Filter'."):
            filter_prod_name_field = self.find(loc.FILTER_PROD_NAME_FIELD)
            self.filling([filter_prod_name_field], [loc.FILTER_PROD_NAME_TEXT])
            self.clicking(self.find(loc.FILTER_SEARCH_BUTTON))
        with allure.step("Get search result"):
            result = self.find(loc.PRODUCTS_LIST_PRODUCT_NAME)
        return result

    @allure.title("Delete existing product.")
    def delete_existing_product(self):
        with allure.step("Enable checkbox at the left side of the product image."):
            self.clicking(self.find(loc.PRODUCTS_LIST_CHECK_BOX))
        with allure.step("Click 'Delete' button."):
            self.clicking(self.find(loc.PRODUCTS_DELETE_PRODUCT_BUTTON))
        with allure.step("Get alert banner and accept."):
            alert = self.driver.switch_to.alert
            alert.accept()

    @allure.title("Find deleted product in Products filter.")
    def check_deleted_product(self):
        with allure.step("Fill in search field deleted product name and click 'Filter'."):
            filter_prod_name_field = self.find(loc.FILTER_PROD_NAME_FIELD)
            self.filling([filter_prod_name_field], [loc.FILTER_PROD_NAME_TEXT])
            self.clicking(self.find(loc.FILTER_SEARCH_BUTTON))
        with allure.step("Get deleted product search result."):
            result = self.find(loc.FILTER_NO_RESULTS)
        return result
