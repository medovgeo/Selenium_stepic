from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    time.sleep(5)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    y = calc(x)

    # Заполняем обязательные поля
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
