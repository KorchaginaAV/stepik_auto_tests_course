import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    magic_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    magic_button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.submit()

finally:
    time.sleep(5)
    browser.quit()
