from .base_page import BasePage
from .locators import ProductPageLocators




class AddInBasket(BasePage):
    def add_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def AssertFinishText(self):
        name = self.browser.find_element(*ProductPageLocators.FINISH_TEXT).text
        name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_TEXT).text
        assert name == name2
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_basket == price_product

    def AssertIsNotElementPresent(self):
        assert self.is_not_element_present(*ProductPageLocators.FINISH_TEXT)

    def IsDisappeared(self):
        assert self.is_disappeared(*ProductPageLocators.FINISH_TEXT)