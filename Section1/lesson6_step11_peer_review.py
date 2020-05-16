from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
value1 = "input"
value2 = "last_name"
value3 = "city"
value4 = "country"

with webdriver.Chrome() as browser:
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element_by_css_selector("input.first[placeholder~='name']")
    first_name.send_keys("Test")
    last_name = browser.find_element_by_css_selector("input.second[placeholder~='name']")
    last_name.send_keys("Test")
    email = browser.find_element_by_css_selector("input.third[placeholder~='email']")
    email.send_keys("Test")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(2)
