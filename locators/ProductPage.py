from selenium.webdriver.common.by import By


class ProductPage:
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, ".btn.btn-default>.fa.fa-heart")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-default>.fa.fa-exchange")
    ADD_TO_CART = (By.CSS_SELECTOR, "#button-cart.btn")
    SEARCH = (By.CSS_SELECTOR, "[name='search']")
    CHECK_PRODUCTS_IN_SHOPING_CART = (By.CSS_SELECTOR, "#cart-total")
