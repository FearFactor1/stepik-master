from pages.product_page import AddInBasket
from pages.base_page import BasePage
import pytest
import time


@pytest.mark.xfail
@pytest.mark.parametrize('offers', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, offers):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offers}"
    pages = AddInBasket(browser, link)
    pages.open()
    pages.add_in_basket()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    time.sleep(10)
    pages.AssertFinishText()
