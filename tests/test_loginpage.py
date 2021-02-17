from locators.LoginPage import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_loginpage(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/login")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_EMAIL))
    wait.until(EC.visibility_of_element_located(LoginPage.INPUT_PASS))
    wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON))
    wait.until(EC.visibility_of_element_located(LoginPage.FORGOTTEN_PASSWORD))
    wait.until(EC.visibility_of_element_located(LoginPage.TRANSACTIONS))
