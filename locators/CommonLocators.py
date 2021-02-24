from selenium.webdriver.common.by import By


class CommonLocators:
    WAIT_CONTAINER_LOAD = (By.CSS_SELECTOR, "#container")
    GO_TO_HOMEPAGE = (By.CSS_SELECTOR, "[title='OpenCart']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".fa.fa-sign-out")
