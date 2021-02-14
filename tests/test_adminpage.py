from locators.AdminPage import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_adminpage(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_PASS))
    wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    wait.until(EC.visibility_of_element_located(AdminPage.FORGOTTEN_PASSWORD))
    wait.until(EC.visibility_of_element_located(AdminPage.GO_TO_HOMEPAGE))

