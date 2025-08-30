from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self):
        self.driver.get(self.url)
        return self

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, button_text):
        xpath = f"//span[text()='{button_text}']"
        self.driver.find_element(By.XPATH, xpath).click()
        return self

    def calculate(self, expression):
        for char in expression:
            self.click_button(char)
        return self

    def get_result(self, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    def wait_for_result(self, expected_result, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), str(expected_result)
            )
        )
        return self
