from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasketPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def AssertTextBasketEmpty(self):
        text_basket = self.browser.find_element(*BasePageLocators.TEXT_IN_BASKET).text
        assert "Ваша корзина пуста" in text_basket

    def AllProducts(self):
        products = self.browser.find_element(*BasePageLocators.PRODUCTS_LINK)
        products.click()
