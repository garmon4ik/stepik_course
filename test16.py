from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.execute_script("window.scrollBy(0, 100);")


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    element = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element_by_css_selector("button.btn").click()
    #thats code

    #считываем значение Х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    #Вводим значение выражение в тексотовое поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Копируем результат. Спасибо за данный фрагмент кода Vitaliy Ya! =)
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

    # Нажимаем на кноку "Ok"
    alert.accept()

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием

    browser.get("https://stepik.org/course/575/promo?auth=login")
    time.sleep(2)


    s_username = browser.find_element_by_id("id_login_email")
    s_username.send_keys("gar.bounty@gmail.com")

    s_password = browser.find_element_by_id("id_login_password")
    s_password.send_keys("Wdb2#AVQz@Bc#_2")

    # Ищем кнопку для авторизации
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(5)


    browser.get("https://stepik.org/lesson/181384/step/8")
    time.sleep(4)


    # Находим поле для ввода ответа
    textarea = browser.find_element_by_css_selector(".textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)

    # Напишем текст ответа в найденное поле
    textarea.send_keys(addToClipBoard)

    # Отправляем ответ
    browser.find_element_by_css_selector(".submit-submission").click()
finally:
    time.sleep(5)
    browser.quit()
