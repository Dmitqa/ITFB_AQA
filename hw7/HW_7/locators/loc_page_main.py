from selenium.webdriver.common.by import By


class LocPageMain:
    CURRENCY_TYPE = (By.TAG_NAME, "strong")
    CURRENCY_DROP_DOWN = (By.XPATH, '//form[@id="form-currency"]/div')
    CURRENCY_EURO = (By.XPATH, '//a[@href="EUR"]')
    CURRENCY_POUND_STERLING = (By.XPATH, '//a[@href="GBP"]')
    CURRENCY_US_DOLLAR = (By.XPATH, '//a[@href="USD"]')

    CARD_BUTTON = (By.XPATH, '//div[@id="header-cart"]/div/button')
    EMPTY_CARD_MESSAGE = (By.XPATH, '//div[@id="header-cart"]//li')
    NAVBAR_PANEL = (By.XPATH, '//nav[@id="menu"]')
    TEXT_HEADER_3 = (By.TAG_NAME, 'h3')
    NAVBAR_TITLES = (By.XPATH, '//div[@id="narbar-menu"]/ul')
    SEARCH_FIELD = (By.XPATH, '//div[@id="search"]/input')
