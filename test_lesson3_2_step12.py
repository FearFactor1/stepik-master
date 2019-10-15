import unittest
import time
from selenium import webdriver



link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestUn(unittest.TestCase):
    def test_un1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

        input1 = browser.find_element_by_css_selector("input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input.form-control.third")
        input3.send_keys("fdgd@ya.ru")
        input4 = browser.find_element_by_css_selector(".second_block > div:nth-child(1) > input:nth-child(2)")
        input4.send_keys("+79875734t")
        input5 = browser.find_element_by_css_selector(".second_block > div:nth-child(2) > input:nth-child(2)")
        input5.send_keys("st. yyyhaha d 23")
        button = browser.find_element_by_css_selector(".btn")
        button.click()
        welcome_text = browser.find_element_by_css_selector(".container > h1:nth-child(1)").text
        #self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!")
        assert "Congratulations! You have successfully registered!" == welcome_text

    if __name__ == "__main__":
        unittest.main()



    def test_un2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        input1 = browser.find_element_by_css_selector(".first_block > div:nth-child(1) > input:nth-child(2)")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".third")
        input3.send_keys("fdgd@ya.ru")
        input4 = browser.find_element_by_css_selector(".second_block > div:nth-child(1) > input:nth-child(2)")
        input4.send_keys("+79875734t")
        input5 = browser.find_element_by_css_selector(".second_block > div:nth-child(2) > input:nth-child(2)")
        input5.send_keys("st. yyyhaha d 23")
        button = browser.find_element_by_css_selector(".btn")
        button.click()
        welcome_text = browser.find_element_by_css_selector(".container > h1:nth-child(1)").text
        #self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!")
        assert "Congratulations! You have successfully registered!" == welcome_text


    if __name__ == "__main__":
        unittest.main()







