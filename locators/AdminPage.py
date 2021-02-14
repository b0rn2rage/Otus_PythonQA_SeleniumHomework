from selenium.webdriver.common.by import By


class AdminPage:
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASS = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn")
    FORGOTTEN_PASSWORD = (By.XPATH, "//a[text()='Forgotten Password']")
    GO_TO_HOMEPAGE = (By.CSS_SELECTOR, "[title='OpenCart']")
