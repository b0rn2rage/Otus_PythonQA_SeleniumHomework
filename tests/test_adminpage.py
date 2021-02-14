from locators.AdminPage import AdminPage


def test_adminpage(browser):
    browser.get("https://demo.opencart.com/admin/")
    browser.find_element(*AdminPage.INPUT_USERNAME)
    browser.find_element(*AdminPage.INPUT_PASS)
    browser.find_element(*AdminPage.LOGIN_BUTTON)
    browser.find_element(*AdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*AdminPage.GO_TO_HOMEPAGE)
