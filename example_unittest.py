import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLesson6(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    first_name_locator = "input[placeholder='Input your name']"
    email_locator = "input[placeholder='Input your email']"
    button_locator = "button.btn"
    welcome_text_elt_locator = "h1"

    def test_registration1(self):
        TestLesson6.browser.get(TestLesson6.link1)
        TestLesson6.browser.implicitly_wait(5)
        first_name = TestLesson6.browser.find_element(
            By.CSS_SELECTOR, TestLesson6.first_name_locator
        )
        first_name.send_keys("Ivan")
        email = TestLesson6.browser.find_element(
            By.CSS_SELECTOR, TestLesson6.email_locator
        )
        email.send_keys("Smolensk@mail.ru")
        button = TestLesson6.browser.find_element(
            By.CSS_SELECTOR, TestLesson6.button_locator
        )
        button.click()
        welcome_text_elt = TestLesson6.browser.find_element(
            By.TAG_NAME, TestLesson6.welcome_text_elt_locator
        )
        welcome_text = welcome_text_elt.text
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Попытка регистрации оказалось неудачной",
        )

    def test_registration2(self):
        TestLesson6.browser.get(TestLesson6.link2)
        TestLesson6.browser.implicitly_wait(5)
        first_name = TestLesson6.browser.find_element(
            By.CSS_SELECTOR, TestLesson6.first_name_locator
        )
        first_name.send_keys("Ivan")
        email = TestLesson6.browser.find_element(
            By.CSS_SELECTOR, TestLesson6.email_locator
        )
        email.send_keys("Smolensk@mail.ru")
        button = TestLesson6.browser.find_element(
            By.CSS_SELECTOR, TestLesson6.button_locator
        )
        button.click()
        welcome_text_elt = TestLesson6.browser.find_element(
            By.TAG_NAME, TestLesson6.welcome_text_elt_locator
        )
        welcome_text = welcome_text_elt.text
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Попытка регистрации оказалось неудачной",
        )


if __name__ == "__main__":
    unittest.main()
