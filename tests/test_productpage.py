from locators.ProductPage import ProductPage


def test_productpage(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
    browser.find_element(*ProductPage.ADD_TO_WISHLIST)
    browser.find_element(*ProductPage.COMPARE_PRODUCT)
    browser.find_element(*ProductPage.ADD_TO_CART)
    browser.find_element(*ProductPage.SEARCH)
    browser.find_element(*ProductPage.CHECK_PRODUCTS_IN_SHOPING_CART)