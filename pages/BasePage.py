from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    url = "https://demo.opencart.com"

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def _input_text(element, text):
        element.clear()
        element.click()
        element.send_keys(text)

    def _wait_element_to_be_clickable(self, locator, wait_time=3):
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f'{element} не найден/не кликабелен')
        return element

    def _find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def _find_element(self, locator):
        return self.browser.find_element(*locator)

    def _wait_element_to_be_presence(self, locator, wait_time=3):
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            element = wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'{element} не отображается в DOM дереве')
        return element
