from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_amount(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        return total_text.split("$")[1]
