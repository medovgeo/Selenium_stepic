from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os



# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

link = "http://suninjuly.github.io/file_input.html"
file = "test.txt"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, file)

with webdriver.Chrome() as browser:
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Test")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Test")
    email = browser.find_element_by_name("email")
    email.send_keys("Test")
    file = browser.find_element_by_name("file")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(2)

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])

