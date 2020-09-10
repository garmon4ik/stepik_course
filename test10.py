from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #иницилизируем браузер и ссылку
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #считываем значение Х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    #Вводим значение выражение в тексотовое поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    #кликаем чекбокс
    input2 = browser.find_element_by_css_selector("#robotCheckbox")
    input2.click()


    #кликаем радиокнопку
    input3 = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("window.scrollBy(0, 100);")
    input3.click()
    time.sleep(2)

    #отправляем заполненную форму

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()
