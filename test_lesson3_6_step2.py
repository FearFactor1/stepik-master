
import pytest
from selenium import webdriver
import time
import math




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_paramet_tests(browser, links):
    #link = links
    browser.get(links)
    input = browser.find_element_by_xpath("//textarea")
    answer = math.log(int(time.time()))
    input.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    text = browser.find_element_by_class_name("smart-hints__hint").text
    assert "Correct!" in text



