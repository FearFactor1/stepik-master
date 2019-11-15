from .base_page import BasePage
from .locators import ProductPageLocators



class AddInBasket(BasePage):
    def add_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def AssertFinishText(self):
        name = self.browser.find_element(*ProductPageLocators.FINISH_TEXT).text
        assert "The shellcoder's handbook был добавлен в вашу корзину." in name
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert "9,99 £" in price_basket and price_product