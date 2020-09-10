import os
import time
import math
from selenium import webdriver
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element_by_css_selector("button.trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #finding value for function
    x = browser.find_element_by_css_selector("#input_value").text

    #inputing answer of function in textarea
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))

    #clicking button to send form
    browser.find_element_by_css_selector("button.btn").click()

    # Копируем результат. Спасибо за данный фрагмент кода Vitaliy Ya! =)
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

    # Нажимаем на кноку "Ok"
    alert.accept()

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием

    browser.get("https://stepik.org/course/575/promo?auth=login")
    time.sleep(5)


    s_username = browser.find_element_by_id("id_login_email")
    s_username.send_keys("gar.bounty@gmail.com")

    s_password = browser.find_element_by_id("id_login_password")
    s_password.send_keys("Wdb2#AVQz@Bc#_2")

    # Ищем кнопку для авторизации
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(4)

    browser.get("https://stepik.org/lesson/184253/step/6")
    time.sleep(5)

    # Находим поле для ввода ответа
    textarea = browser.find_element_by_css_selector(".textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    time.sleep(1)
    # Напишем текст ответа в найденное поле
    textarea.send_keys(addToClipBoard)

    # Отправляем ответ
    browser.find_element_by_css_selector(".submit-submission").click()

    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
