import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from loggers import logger_file
from ui.pages.register_account_from_shopping_cart import RegisterAccountFromShoppingCart
from ui.pages.order_from_compare import OrderFromCompare
from ui.pages.return_product import ReturnProduct


@pytest.fixture(scope="module")
def driver(request):
    url = "http://192.168.0.103"
    driver = webdriver.Chrome(service=ChromService())
    logger_file.info(f"Browser Chrome started.")
    driver.maximize_window()
    driver.get(url)
    driver.url = url
    logger_file.info("Go to Main page.")

    yield driver
    driver.close()
    logger_file.info(f"Browser Chrome closed.")


@pytest.fixture()
def register(driver):
    logger_file.info("Call 'Register Account from shopping cart' driver.")
    return RegisterAccountFromShoppingCart(driver)

@pytest.fixture()
def compare(driver):
    logger_file.info("Call 'Order from compare' driver.")
    return OrderFromCompare(driver)

@pytest.fixture()
def return_order(driver):
    logger_file.info("Call 'Return product' driver.")
    return ReturnProduct(driver)
