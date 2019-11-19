from pages.product_page import AddInBasket
from pages.base_page import BasePage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    pages = AddInBasket(browser, link)
    pages.open()
    pages.add_in_basket()
    pages.AssertIsNotElementPresent()

def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    pages = AddInBasket(browser, link)
    pages.open()
    pages.AssertIsNotElementPresent()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    pages = AddInBasket(browser, link)
    pages.open()
    pages.add_in_basket()
    pages.IsDisappeared()

