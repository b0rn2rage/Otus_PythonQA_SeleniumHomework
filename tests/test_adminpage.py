from locators.AdminPage import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_adminpage(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_PASS))
    wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    wait.until(EC.visibility_of_element_located(AdminPage.FORGOTTEN_PASSWORD))
    wait.until(EC.visibility_of_element_located(AdminPage.GO_TO_HOMEPAGE))


def test_print_shipping_list(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    login_button = wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    login_button.click()
    wait.until(EC.visibility_of_element_located(AdminPage.CONTAINER))  # Жду загрузку страницы
    latest_orders = browser.find_elements(*AdminPage.VIEW_LATEST_ORDERS)
    latest_orders[0].click()
    wait.until(EC.visibility_of_element_located(AdminPage.CONTAINER))
    print_shipping_button = wait.until(EC.visibility_of_element_located(AdminPage.PRINT_SHIPPING_LIST))
    print_shipping_button.click()
    try:
        wait.until(EC.visibility_of_element_located(AdminPage.CONTAINER))
    except TimeoutException:
        raise AssertionError()


def test_open_add_new_order_form(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    login_button = wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    login_button.click()
    wait.until(EC.visibility_of_element_located(AdminPage.CONTAINER))
    browser.find_element(*AdminPage.SALES).click()
    wait.until(EC.visibility_of_element_located(AdminPage.SECTIONS_IN_SALES))
    sections_in_sales = browser.find_elements(*AdminPage.SECTIONS_IN_SALES)
    sections_in_sales[0].click()
    add_new_order = wait.until(EC.visibility_of_element_located(AdminPage.ADD_NEW_ORDER))
    add_new_order.click()
    wait.until(EC.visibility_of_element_located(AdminPage.CUSTOMER_FIELD))

