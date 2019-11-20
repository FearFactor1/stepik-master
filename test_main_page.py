from pages.base_page import BasePage
from pages.product_page import AddInBasket
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_look_basket()
    pages = AddInBasket(browser, link)
    pages.AssertIsNotElementPresent()
    page1 = BasketPage(browser, link)
    page1.AssertTextBasketEmpty()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasePage(browser, link)
    page.open()
    page1 = BasketPage(browser, link)
    page1.AllProducts()
    page.go_to_look_basket()
    pages = AddInBasket(browser, link)
    pages.AssertIsNotElementPresent()
    page1.AssertTextBasketEmpty()







