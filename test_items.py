import time


def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0
