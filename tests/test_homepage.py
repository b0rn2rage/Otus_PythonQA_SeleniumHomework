from locators.HomePage import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_homepage(browser, open_opencart_homepage):
    browser.get(open_opencart_homepage)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(HomePage.CURRENCY))
    wait.until(EC.visibility_of_element_located(HomePage.MY_ACCOUNT))
    wait.until(EC.visibility_of_element_located(HomePage.WISH_LIST))
    wait.until(EC.presence_of_element_located(HomePage.SHOPPING_CART))
    wait.until(EC.visibility_of_element_located(HomePage.CHECKOUT))
