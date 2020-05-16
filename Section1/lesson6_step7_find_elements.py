from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/huge_form.html"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

with webdriver.Chrome() as browser:
    browser.get(link)

    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
