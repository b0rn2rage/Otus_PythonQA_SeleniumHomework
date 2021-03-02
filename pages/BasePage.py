from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class BasePage:
    url = "https://demo.opencart.com"

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def _input_text(self, element, text):
        self.logger.info(f"Clear form {element}")
        element.clear()
        self.logger.info(f"Click on form {element}")
        element.click()
        self.logger.info(f"Input text '{text}' in form {element}")
        element.send_keys(text)

    def _wait_element_to_be_clickable(self, locator, wait_time=3):
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            self.logger.info(f"Wait {element} to be clickable")
            element = wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error(f"Element {element} not found")
            raise AssertionError(f'{element} не найден/не кликабелен')
        return element

    def _find_elements(self, locator):
        self.logger.info(f"Find elements {locator}")
        return self.browser.find_elements(*locator)

    def _find_element(self, locator):
        self.logger.info(f"Find element {locator}")
        return self.browser.find_element(*locator)

    def _wait_element_to_be_presence(self, locator, wait_time=3):
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            self.logger.info(f"Wait {element} to be presence")
            element = wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Element {element} not presence in DOM")
            raise AssertionError(f'{element} не отображается в DOM дереве')
        return element
