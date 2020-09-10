import os
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_css_selector("input:nth-child(2)")
    input1.send_keys("Askar")
    input2 = browser.find_element_by_css_selector("input:nth-child(4)")
    input2.send_keys("Chalbayev")
    input3 = browser.find_element_by_css_selector("input:nth-child(6)")
    input3.send_keys("Askar@mail.km")

    element = browser.find_element_by_css_selector("input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
