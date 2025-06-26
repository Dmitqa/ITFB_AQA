from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from hw7.loggers import logger_file


class BasePage:

    def __init__(self, driver: WebDriver, logger=logger_file):
        self.driver = driver
        self.logger = logger

    def find(self, locator, time=5):
        self.logger.info(f"Wait and identify page element: {locator}.")
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def find_all(self, locator, time=5):
        self.logger.info(f"Wait and identify some page elements: {locator}.")
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements

    def clicking(self, element):
        self.logger.info("Clicking page element.")
        return element.click()

    def filling(self, fields: list, field_values: list):
        self.logger.info(f"Fill values'{field_values}' in fields.")
        for field, value in zip(fields, field_values):
            field.send_keys(value)

    def wait_visible(self, locator, time=5):
        self.logger.info(f"Wait visibility page element: {locator}.")
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator, time=5):
        self.logger.info(f"Wait visibility some page elements: {locator}.")
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
