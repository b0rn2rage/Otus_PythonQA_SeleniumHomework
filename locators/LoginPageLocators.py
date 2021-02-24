from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASS = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.btn")
    FORGOTTEN_PASSWORD = (By.XPATH, "//a[@class='list-group-item' and  text()='Forgotten Password']")
    TRANSACTIONS = (By.XPATH, "//a[@class='list-group-item' and  text()='Transactions']")
