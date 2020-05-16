from selenium import webdriver
import time
import math

value1 = "input"
value2 = "last_name"
value3 = "city"
value4 = "country"
link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element_by_link_text(text)
    button.click()

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_class_name("btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
