from selenium import webdriver
import pytest
import logging
import configparser
from pathlib import Path

logging.basicConfig(level=logging.INFO, filename="../selenium.log")
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox", "ie"], help="Choose browser")
    parser.addoption("--baseurl", default="https://demo.opencart.com/")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    test_name = request.node.name
    driver = None
    logger.info(f"Run browser {browser}")
    logger.info(f"Run test {test_name}")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = True
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
    logger.info(f"Browser {browser} close")
    driver.quit()


@pytest.fixture()
def open_opencart_homepage(request):
    baseurl = request.config.getoption("--baseurl")
    return baseurl


@pytest.fixture(scope='session')
def config():
    cfg = configparser.ConfigParser()
    cfg.read(Path(__file__).parent / 'config.ini')
    logger.info(f"Read config from {Path(__file__).parent / 'config.ini'}")
    return cfg
