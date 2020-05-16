from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.execute_script("document.title='Script executing'; alert('Robots at work');")
    time.sleep(10)