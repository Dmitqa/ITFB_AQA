from selenium.webdriver.common.by import By


class LocPageLaptop:
    COMPARE_BUTTON = (By.XPATH, '//a[@id="compare-total"]')
    LIST_BUTTON = (By.XPATH, "//button[@id='button-list']")
    GRID_BUTTON = (By.XPATH, "//button[@id='button-grid']")
    SORT_BY_FIELD = (By.XPATH, '//select[@id="input-sort"]/option[1]')
