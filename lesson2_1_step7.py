from selenium import webdriver
import time
import math



link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)

    checkbox = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    radiobutton.click()

    button = browser.find_element_by_xpath("//*/button[contains(text(), 'Submit')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()