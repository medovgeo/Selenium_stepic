from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    x = browser.find_element_by_css_selector("#treasure")
    y = calc(x.get_attribute("valuex"))

    # Заполняем обязательные поля
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    robotCheckbox = browser.find_element_by_css_selector("#robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element_by_css_selector("#robotsRule")
    robotsRule.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
