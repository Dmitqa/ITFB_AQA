import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.firefox.service import Service as FoxService
from selenium.webdriver.edge.service import Service as EdgeService
from hw7.pages.page_laptop_hp_lp_3065 import PageLaptopHpLp3065
from hw7.pages.page_login import PageLogin
from hw7.pages.page_register import PageRegister
from hw7.pages.page_admin import PageAdmin
from hw7.loggers import logger_file


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--url", default="http://localhost:80", action="store")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "Chrome":
        driver = webdriver.Chrome(service=ChromService())
    elif browser == "Firefox":
        driver = webdriver.Firefox(service=FoxService())
    else:
        driver = webdriver.Edge(service=EdgeService())

    logger_file.info(f"Browser '{browser}' started.")
    driver.maximize_window()
    driver.get(url)
    driver.url = url
    logger_file.info("Go to Main page.")

    yield driver
    driver.close()
    logger_file.info(f"Browser '{browser}' closed.")


@pytest.fixture(scope="module")
def click_laptop(driver):
    logger_file.info("Go to Laptops page.")
    driver.get("http://localhost/en-gb/catalog/laptop-notebook")
    return driver


@pytest.fixture()
def laptop_card(driver):
    logger_file.info("Go to Laptop HP LP 3065 page.")
    driver.get("http://localhost/en-gb/product/laptop-notebook/hp-lp3065")
    return PageLaptopHpLp3065(driver)


@pytest.fixture(scope="module")
def page_login(driver):
    logger_file.info("Go to Login page.")
    driver.get("http://localhost/en-gb?route=account/login")
    return PageLogin(driver)


@pytest.fixture()
def page_register(driver):
    logger_file.info("Go to Register page.")
    driver.get("http://localhost/en-gb?route=account/register")
    return PageRegister(driver)


@pytest.fixture()
def admin(driver):
    logger_file.info("Go to Admin page.")
    driver.get("http://localhost/administration")
    return PageAdmin(driver)
