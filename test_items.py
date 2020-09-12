import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_check_add_to_basket(browser):
     browser.get(link)
     basket_btn = browser.find_element_by_css_selector("button.btn-add-to-basket")
     assert basket_btn, "Кнопка не найдена"
