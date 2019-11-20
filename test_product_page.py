from pages.product_page import AddInBasket
from pages.base_page import BasePage
from pages.login_page import LoginPage
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize('offers', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, offers):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offers}"
    pages = AddInBasket(browser, link)
    pages.open()
    pages.add_in_basket()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    pages.AssertFinishText()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/ru/"
        page = BasePage(browser, link)
        page.open()
        page.enter_or_authorized()
        pages = LoginPage(browser, link)
        pages.register_new_user()
        page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = AddInBasket(browser, link)
        pages.open()
        pages.add_in_basket()
        base_page = BasePage(browser, link)
        base_page.solve_quiz_and_get_code()
        pages.AssertFinishText()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = AddInBasket(browser, link)
        pages.open()
        pages.AssertIsNotElementPresent()