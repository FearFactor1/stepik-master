from selenium import webdriver
import time
import math



link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    alert = browser.switch_to.alert
    alert.accept()
    browser.get(link)


    button = browser.find_element_by_css_selector(".trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)

    button2 = browser.find_element_by_xpath("//*/button[contains(text(), 'Submit')]")
    button2.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()