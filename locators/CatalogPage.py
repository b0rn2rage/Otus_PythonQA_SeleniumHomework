from selenium.webdriver.common.by import By


class CatalogPage:
    MENU_DESKTOPS = (By.XPATH, "//a[@class='dropdown-toggle' and  text()='Desktops']")
    MENU_LAPTOPS_AND_NOTEBOOKS = (By.XPATH, "//a[@class='dropdown-toggle' and  text()='Laptops & Notebooks']")
    MENU_COMPONENTS = (By.XPATH, "//a[@class='dropdown-toggle' and  text()='Components']")
    MENU_TABLETS = (By.XPATH, "//a[text()='Tablets']")
    MENU_SOFTWARE = (By.XPATH, "//a[text()='Software']")
