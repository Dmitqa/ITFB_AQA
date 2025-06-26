from selenium.webdriver.common.by import By


class LocPageLogin:
    NEW_CUSTOMER_WINDOW = (By.XPATH, "//div[@id='content']/div/div[1]/div")
    NEW_CUSTOMER_HEADER = (By.TAG_NAME, "h2")
    NEW_CUSTOMER_CONTINUE_BUTTON = (By.XPATH, "//a[contains(text(), 'Continue')]")
    RETURN_CUSTOMER_EMAIL = (By.XPATH, "//input[@id='input-email']")
    RETURN_CUSTOMER_EMAIL_TEXT = "test@test.com"
