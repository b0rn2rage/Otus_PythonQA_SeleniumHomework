from pages.ProductPage import ProductPage


def test_productpage(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page()
    product_page.check_elements_on_product_page()
