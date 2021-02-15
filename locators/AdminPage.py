from selenium.webdriver.common.by import By


class AdminPage:
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASS = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn")
    FORGOTTEN_PASSWORD = (By.XPATH, "//a[text()='Forgotten Password']")
    GO_TO_HOMEPAGE = (By.CSS_SELECTOR, "[title='OpenCart']")
    CONTAINER = (By.CSS_SELECTOR, "#container")
    VIEW_LATEST_ORDERS = (By.CSS_SELECTOR, ".fa.fa-eye")
    PRINT_SHIPPING_LIST = (By.CSS_SELECTOR, "[data-original-title='Print Shipping List']>.fa.fa-truck")
    SALES = (By.CSS_SELECTOR, ".fa.fa-shopping-cart.fw")
    SECTIONS_IN_SALES = (By.CSS_SELECTOR, "#collapse26>li>a")
    ADD_NEW_ORDER = (By.CSS_SELECTOR, ".fa.fa-plus")
    CUSTOMER_FIELD = (By.CSS_SELECTOR, "#input-customer")

