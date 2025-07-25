from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout():
    # Открываем сайт в Firefox
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    try:
        # Авторизация
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

        # Добавление товаров в корзину
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        for item_name in items_to_add:
            item_xpath = (
                f"//div[text()='{item_name}']/ancestor::div["
                "@class='inventory_item']//button"
            )
            driver.find_element(By.XPATH, item_xpath).click()

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Нажатие Checkout
        driver.find_element(By.ID, "checkout").click()

        # Заполнение формы
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Получение итоговой суммы
        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_amount = total_text.split("$")[1]

        # Проверка суммы
        assert total_amount == "58.29", (
            f"Ожидаемая сумма: $58.29, Фактическая сумма: ${total_amount}"
        )

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_saucedemo_checkout()
