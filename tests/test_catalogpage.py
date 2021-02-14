from locators.CatalogPage import CatalogPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalogpage(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU_DESKTOPS))
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU_LAPTOPS_AND_NOTEBOOKS))
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU_COMPONENTS))
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU_TABLETS))
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU_SOFTWARE))
