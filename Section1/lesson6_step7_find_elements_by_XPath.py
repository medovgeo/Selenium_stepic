from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
value1 = "input"
value2 = "last_name"
value3 = "city"
value4 = "country"

with webdriver.Chrome() as browser:
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//lesson6_step7_find_elements_by_XPath.pybutton[@type='submit']")
    button.click()
    time.sleep(10)