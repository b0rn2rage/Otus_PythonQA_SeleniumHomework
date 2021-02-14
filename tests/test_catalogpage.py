from locators.CatalogPage import CatalogPage


def test_catalogpage(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=20")
    browser.find_element(*CatalogPage.MENU_DESKTOPS)
    browser.find_element(*CatalogPage.MENU_LAPTOPS_AND_NOTEBOOKS)
    browser.find_element(*CatalogPage.MENU_COMPONENTS)
    browser.find_element(*CatalogPage.MENU_TABLETS)
    browser.find_element(*CatalogPage.MENU_SOFTWARE)
