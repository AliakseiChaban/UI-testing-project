import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.create_new_customer import CreateCustomerAccount


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)

    return chrome_driver


@pytest.fixture()
def create_new_customer_page(driver):
    return CreateCustomerAccount(driver)
