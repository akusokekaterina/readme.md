from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from pages.LoginPage import LoginPage


def test_saucedemo_checkout():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        for item_name in items_to_add:
            xpath = (
                f"//div[text()='{item_name}']/"
                "ancestor::div[@class='inventory_item']//button"
            )
            driver.find_element(By.XPATH, xpath).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_amount = total_text.split("$")[1]

        expected_amount = "58.29"
        assert total_amount == expected_amount, (
            f"Ожидаемая сумма: ${expected_amount}, "
            f"Фактическая сумма: ${total_amount}"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_saucedemo_checkout()
