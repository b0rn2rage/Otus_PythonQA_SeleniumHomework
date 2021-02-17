from locators.AdminPage import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def test_adminpage(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_USERNAME))
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_PASS))
    wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    wait.until(EC.visibility_of_element_located(AdminPage.FORGOTTEN_PASSWORD))
    wait.until(EC.visibility_of_element_located(AdminPage.GO_TO_HOMEPAGE))


def test_open_print_shipping_list(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    login_button = wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    login_button.click()
    wait.until(EC.visibility_of_element_located(AdminPage.LOAD_ADMIN_PAGE))  # Дождаться загрузки страницы
    latest_orders = browser.find_elements(*AdminPage.VIEW_LATEST_ORDERS)
    latest_orders[0].click()  # Перейти в последний заказ
    print_shipping_button = wait.until(EC.visibility_of_element_located(AdminPage.PRINT_SHIPPING_LIST))
    window_before = browser.window_handles[0]  # Сохранить текущее окно
    print_shipping_button.click()  # Перейти в список доставки по заказу
    window_after = browser.window_handles[1]  # Сохранить новое окно с открывшейся накладной
    browser.switch_to.window(window_after)  # Свичнуться на окно с накладной
    try:
        wait.until(EC.visibility_of_element_located(AdminPage.CONTAINER))  # Дождаться загрузки страницы
        wait.until(EC.visibility_of_element_located(AdminPage.DISPATCH_NOTE))  # Проверить что накладная загрузилась
    except TimeoutException:
        raise AssertionError("Накладная не загрузилась")


def test_open_add_new_order_form(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    login_button = wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    login_button.click()
    wait.until(EC.visibility_of_element_located(AdminPage.LOAD_ADMIN_PAGE))  # Дождаться загрузки страницы
    browser.find_element(*AdminPage.SALES).click()
    wait.until(EC.visibility_of_element_located(AdminPage.SECTIONS_IN_SALES))  # Подождать открытие разделов
    sections_in_sales = browser.find_elements(*AdminPage.SECTIONS_IN_SALES)
    sections_in_sales[0].click()  # Перейти в раздел Orders
    add_new_order = wait.until(EC.visibility_of_element_located(AdminPage.ADD_NEW_ORDER))
    add_new_order.click()  # Добавить новый заказ
    try:
        wait.until(EC.visibility_of_element_located(AdminPage.CUSTOMER_FIELD))  # Поле customer есть на странице
    except TimeoutException:
        raise AssertionError("Форма по добавлению нового заказа не загрузилась либо в ней отсутствует поле customer")


def test_login_logout(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    login_button = wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    login_button.click()
    try:
        # Дождаться загрузки страницы после авторизации
        wait.until(EC.visibility_of_element_located(AdminPage.LOAD_ADMIN_PAGE))
        logout_button = browser.find_element(*AdminPage.LOGOUT_BUTTON)
    except(TimeoutException, NoSuchElementException):
        raise AssertionError("Авторизация в админку не удалась")
    logout_button.click()  # Сделать logout из админки
    # После logout'а на странице есть кнопка логина
    try:
        wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    except TimeoutException:
        raise AssertionError("Сделать Logout из админки не получилось")


def test_open_product_page(browser):
    browser.get("https://demo.opencart.com/admin/")
    wait = WebDriverWait(browser, 5)
    login_button = wait.until(EC.visibility_of_element_located(AdminPage.LOGIN_BUTTON))
    login_button.click()
    wait.until(EC.visibility_of_element_located(AdminPage.LOAD_ADMIN_PAGE))  # Дождаться загрузки страницы
    browser.find_element(*AdminPage.MENU_CATALOG).click()  # Раскрыть меню с каталогом
    wait.until(EC.element_to_be_clickable(AdminPage.SECTIONS_IN_CATALOG))  # Дождаться раскрытия меню
    sections_in_catalog = browser.find_elements(*AdminPage.SECTIONS_IN_CATALOG)
    sections_in_catalog[1].click()  # Перейти в раздел Products
    wait.until(EC.visibility_of_element_located(AdminPage.LOAD_ADMIN_PAGE))  # Дождаться загрузки страницы
    try:
        browser.find_element(*AdminPage.TABLE_WITH_PRODUCT_LIST)
    except NoSuchElementException:
        raise AssertionError("Каталог с продуктами не загрузился")
