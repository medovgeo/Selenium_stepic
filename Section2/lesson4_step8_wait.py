from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )

    button = browser.find_element_by_css_selector("#book")
    button.click()

    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    y = calc(x)

    # Заполняем обязательные поля
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("#solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
