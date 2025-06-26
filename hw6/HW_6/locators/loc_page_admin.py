from selenium.webdriver.common.by import By
from random import sample


class LocPageAdmin:
    USERNAME_PATH = (By.XPATH, '//input[@id="input-username"]')
    PASSWORD_PATH = (By.XPATH, '//input[@id="input-password"]')
    LOGIN_PATH = (By.XPATH, '//button[@type="submit"]')

    LOGIN_ADM_USERNAME = 'user'
    LOGIN_ADM_PASSWORD = 'bitnami'

    CATALOG = (By.XPATH, '//li[@id="menu-catalog"]/a')
    PRODUCTS = (By.XPATH, '//ul[@id="collapse-1"]/li[2]/a')

    GENERAL_TAB = (By.XPATH, '//a[@href="#tab-general"]')
    ADD_PRODUCT_BUTTON = (By.XPATH, '//div[@id="content"]/div[1]/div/div/a')
    DELETE_PRODUCT_BUTTON = (By.XPATH, '//button[@aria-label="Delete"]')

    PRODUCT_NAME_FIELD = (By.XPATH, '//input[@id="input-name-1"]')
    PRODUCT_NAME_TEXT = 'Universal keyboard YKB 1002 CS USB spill-resistant'
    META_TAG_FIELD = (By.XPATH, '//input[@id="input-meta-title-1"]')
    DATA_TAB = (By.XPATH, '//a[@href="#tab-data"]')
    DATA_MODEL_FIELD = (By.XPATH, '//input[@name="model"]')
    META_TAG_TEXT = 'Keyboard YKB 1002'
    DATA_MODEL_TEXT = 'YKB 1002'

    SEO_TAB = (By.XPATH, '//a[@href="#tab-seo"]')
    SEO_KEYWORD_FIELD = (By.XPATH, '//input[@placeholder="Keyword"]')
    SEO_KEYWORD_TEXT = 'http//' + ''.join(sample('population', 10))

    SAVE_BUTTON = (By.XPATH, '//div[@id="content"]/div[1]/div/div/button')

    ALERT = (By.XPATH, '//div[@role="alert"]')
    ALERT_CROSS = (By.XPATH, '//a[@title="Close"]')

    ALERT_SUCCESS = (By.XPATH, '//div[@id="alert"]')
    FILTER_PROD_NAME_FIELD = (By.XPATH, '//input[@name="filter_name"]')
    FILTER_PROD_NAME_TEXT = 'Universal keyboard YKB 1002'
    FILTER_SEARCH_BUTTON = (By.XPATH, '//button[@id="button-filter"]')
    FILTER_NO_RESULTS = (By.XPATH, '//tbody/tr/td[@class="text-center"]')

    PRODUCTS_LIST_PRODUCT_NAME = (By.XPATH, '//tbody/tr/td[@class="text-start"]')
    PRODUCTS_LIST_CHECK_BOX = (By.XPATH, '//tbody/tr/td[@class="text-center"]/input')
    PRODUCTS_DELETE_PRODUCT_BUTTON = (By.XPATH, '//div[@class="float-end"]/button[@class="btn btn-danger"]')
