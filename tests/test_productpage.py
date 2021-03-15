import allure

from pages.ProductPage import ProductPage


@allure.title("Проверка наличия элементов на странице товаров")
def test_productpage(remote):
    product_page = ProductPage(remote)
    product_page.open_product_page()
    product_page.check_elements_on_product_page()
