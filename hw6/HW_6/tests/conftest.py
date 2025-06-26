import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.firefox.service import Service as FoxService
from selenium.webdriver.edge.service import Service as EdgeService
from hw6.pages.page_laptop_hp_lp_3065 import PageLaptopHpLp3065
from hw6.pages.page_login import PageLogin
from hw6.pages.page_register import PageRegister
from hw6.pages.page_admin import PageAdmin


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--url", default="http://localhost:80", action="store")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")


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

    driver.maximize_window()
    driver.get(url)
    driver.url = url

    yield driver
    driver.close()


@pytest.fixture(scope="module")
def click_laptop(driver):
    driver.get("http://localhost/en-gb/catalog/laptop-notebook")
    return driver


@pytest.fixture()
def laptop_card(driver):
    driver.get("http://localhost/en-gb/product/laptop-notebook/hp-lp3065")
    return PageLaptopHpLp3065(driver)


@pytest.fixture(scope="module")
def page_login(driver):
    driver.get("http://localhost/en-gb?route=account/login")
    return PageLogin(driver)


@pytest.fixture()
def page_register(driver):
    driver.get("http://localhost/en-gb?route=account/register")
    return PageRegister(driver)


@pytest.fixture()
def admin(driver):
    driver.get("http://localhost/administration")
    return PageAdmin(driver)
