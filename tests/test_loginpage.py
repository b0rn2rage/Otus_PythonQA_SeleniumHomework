from locators.LoginPage import LoginPage


def test_loginpage(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/login")
    browser.find_element(*LoginPage.INPUT_EMAIL)
    browser.find_element(*LoginPage.INPUT_PASS)
    browser.find_element(*LoginPage.LOGIN_BUTTON)
    browser.find_element(*LoginPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginPage.TRANSACTIONS)
