from locators.ProductPage import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_productpage(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(ProductPage.ADD_TO_WISHLIST))
    wait.until(EC.visibility_of_element_located(ProductPage.COMPARE_PRODUCT))
    wait.until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART))
    wait.until(EC.visibility_of_element_located(ProductPage.SEARCH))
    wait.until(EC.visibility_of_element_located(ProductPage.CHECK_PRODUCTS_IN_SHOPING_CART))
