from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def find_all(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements

    def wait_visible(self, locator, time=2):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator, time=2):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
