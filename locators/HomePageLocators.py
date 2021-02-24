from selenium.webdriver.common.by import By


class HomePageLocators:
    CURRENCY = (By.CSS_SELECTOR, ".fa.fa-caret-down")
    MY_ACCOUNT = (By.CSS_SELECTOR, ".fa.fa-user")
    WISH_LIST = (By.CSS_SELECTOR, "#wishlist-total")
    SHOPPING_CART = (By.XPATH, "//span[text()='Shopping Cart']")
    CHECKOUT = (By.CSS_SELECTOR, ".fa.fa-share")
