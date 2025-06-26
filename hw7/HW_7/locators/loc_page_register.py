from selenium.webdriver.common.by import By


class LocPageRegister:
    REG_ACCOUNT_WINDOW = (By.XPATH, '//div[@id="content"]')
    REG_ACCOUNT_WINDOW_HEADER = (By.TAG_NAME, "h1")
    FIRST_NAME_FIELD = (By.XPATH, '//input[@id="input-firstname"]')
    FIRST_NAME_TEST = "Ner'Zhul"
    LAST_NAME_FIELD = (By.XPATH, '//input[@id="input-lastname"]')
    LAST_NAME_TEST = "Ivanovich"
    EMAIL_FIELD = (By.XPATH, '//input[@id="input-email"]')
    EMAIL_TEST = "test@test.com"
    PASSWORD_FIELD = (By.XPATH, '//input[@id="input-password"]')
    PASSWORD_TEST = "123456"
    CONTINUE_BUTTON = (By.XPATH, '//form[@id="form-register"]/div/button')
    PRIVATE_POLICY_CHECK_BOX = (By.XPATH, "//input[@type='checkbox' and @name='agree']")
    ALREADY_REG_ALERT = (By.XPATH, '//div[@id="alert"]')
