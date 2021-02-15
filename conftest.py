from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox", "ie"], help="Choose browser")
    parser.addoption("--baseurl", default="https://demo.opencart.com/")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")

    driver = None
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif browser == "ie":
        options = webdriver.IeOptions()
        options.headless = True
        driver = webdriver.Ie(options=options)
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture()
def open_opencart_homepage(request):
    baseurl = request.config.getoption("--baseurl")
    return baseurl
