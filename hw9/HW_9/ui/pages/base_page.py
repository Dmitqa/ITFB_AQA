from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from loggers import logger_file
import keyboard


class BasePage:

    def __init__(self, driver: WebDriver, logger=logger_file):
        self.driver = driver
        self.logger = logger

    def element(self, locator, time=10):
        self.logger.info(f"Wait and identify page element: {locator}.")
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def elements(self, locator, time=10):
        self.logger.info(f"Wait and identify some page elements: {locator}.")
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements

    def clicking(self, element: WebElement, time=10):
        self.logger.info("Clicking page element.")
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element))
        return element.click()

    def filling(self, fields: list, field_values: list):
        self.logger.info(f"Fill values'{field_values}' in fields.")
        for field, value in zip(fields, field_values):
            field.clear()
            field.send_keys(value)

    def filling_datetime(self, fields: list, field_values: list):
        self.logger.info(f"Fill values'{field_values}' in fields.")
        for field, value in zip(fields, field_values):
            field.clear()
            field.send_keys(value)
            field.send_keys(Keys.RETURN)

    def uploading(self, load_element: WebElement, file_name):
        self.logger.info(f"Uploading file {file_name}.")
        self.clicking(load_element)
        try:
            self.wait_invisible(load_element, 3)
        except Exception:
            keyboard.write(file_name)
            keyboard.press('enter')

    def accept_alert(self):
        self.logger.info(f"Accepting alert.")
        sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()

    def wait_visible(self, locator, time=10):
        self.logger.info(f"Wait visibility page element: {locator}.")
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator, time=10):
        self.logger.info(f"Wait visibility some page elements: {locator}.")
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def wait_clickable(self, locator, time=10):
        self.logger.info(f"Wait clickability page element: {locator}.")
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
