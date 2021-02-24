from pages.BasePage import BasePage
from locators.ProductPageLocators import ProductPageLocators


class ProductPage(BasePage):
    path = "/index.php?route=product/product&path=57&product_id=49"

    def open_product_page(self):
        self.browser.get(self.url + self.path)

    def check_elements_on_product_page(self):
        self._find_element(ProductPageLocators.CHECK_PRODUCTS_IN_SHOPING_CART)
        self._find_element(ProductPageLocators.SEARCH)
        self._find_element(ProductPageLocators.ADD_TO_CART)
        self._find_element(ProductPageLocators.COMPARE_PRODUCT)
        self._find_element(ProductPageLocators.ADD_TO_WISHLIST)
