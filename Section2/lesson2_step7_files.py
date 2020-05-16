# from selenium import webdriver
# import time
# import math
# from selenium.webdriver.support.ui import Select
#
# link = "http://suninjuly.github.io/execute_script.html"
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# with webdriver.Chrome() as browser:
#     browser.get(link)
#
#     x = browser.find_element_by_css_selector("#input_value").text
#     y = calc(x)
#
#     answer = browser.find_element_by_css_selector("#answer")
#     answer.send_keys(y)
#
#     robotCheckbox = browser.find_element_by_css_selector("#robotCheckbox")
#     robotCheckbox.click()
#
#     robotsRule = browser.find_element_by_css_selector("#robotsRule")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
#     robotsRule.click()
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
#
#     alert = browser.switch_to.alert
#     alert_text = alert.text
#     # validate the alert text
#     alert.accept()
#
#     print(alert_text.split()[-1])

import os

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))