from pages.product_page import AddInBasket
from pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    pages = AddInBasket(browser, link)
    pages.open()
    pages.add_in_basket()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    prompt = browser.switch_to.alert
    prompt.send_keys(str(base_page))
    prompt.accept()
    pages.AssertFinishText()
