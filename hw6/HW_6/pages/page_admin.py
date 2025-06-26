from selenium.webdriver import ActionChains
from hw6.pages.base_page import BasePage
from hw6.locators.loc_page_admin import LocPageAdmin as loc


class PageAdmin(BasePage):

    def login_admin(self, username, password):
        username_field = self.find(loc.USERNAME_PATH)
        password_field = self.find(loc.PASSWORD_PATH)
        login_btn = self.find(loc.LOGIN_PATH)

        (ActionChains(self.driver)
         .click(username_field).send_keys(username).click(password_field)
         .send_keys(password).click(login_btn).perform())

    def go_to_catalog_products(self):
        self.find(loc.CATALOG).click()
        self.find(loc.PRODUCTS).click()

    def add_new_product(self):
        self.find(loc.ADD_PRODUCT_BUTTON).click()
        self.find(loc.ALERT_CROSS).click()

        general_tab = self.find(loc.GENERAL_TAB)
        product_name_field = self.find(loc.PRODUCT_NAME_FIELD)
        meta_tag_field = self.find(loc.META_TAG_FIELD)
        (ActionChains(self.driver)
         .click(product_name_field).send_keys(loc.PRODUCT_NAME_TEXT)
         .click(meta_tag_field).send_keys(loc.META_TAG_TEXT).perform())

        self.find(loc.DATA_TAB).click()
        data_model_field = self.find(loc.DATA_MODEL_FIELD)
        (ActionChains(self.driver)
         .click(data_model_field).send_keys(loc.DATA_MODEL_TEXT).perform())

        self.find(loc.SEO_TAB).click()
        seo_keyword_field = self.find(loc.SEO_KEYWORD_FIELD)
        (ActionChains(self.driver)
         .click(seo_keyword_field).send_keys(loc.SEO_KEYWORD_TEXT).perform())
        general_tab.click()

        self.find(loc.SAVE_BUTTON).click()
        self.find(loc.PRODUCTS).click()

    def check_new_product_name_in_filter(self):
        filter_prod_name_field = self.find(loc.FILTER_PROD_NAME_FIELD)
        (ActionChains(self.driver).click(filter_prod_name_field)
         .send_keys(loc.FILTER_PROD_NAME_TEXT).perform())

        self.find(loc.FILTER_SEARCH_BUTTON).click()
        result = self.find(loc.PRODUCTS_LIST_PRODUCT_NAME)
        return result

    def delete_existing_product(self):
        self.find(loc.PRODUCTS_LIST_CHECK_BOX).click()
        self.find(loc.PRODUCTS_DELETE_PRODUCT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def check_deleted_product(self):
        self.find(loc.FILTER_SEARCH_BUTTON).click()
        result = self.find(loc.FILTER_NO_RESULTS)
        return result
