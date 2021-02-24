from pages.CatalogPage import CatalogPage


def test_catalogpage(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page()
    catalog_page.check_elements_on_catalog_page()
