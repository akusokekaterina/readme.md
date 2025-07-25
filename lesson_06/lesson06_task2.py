from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.maximize_window()

# Переход на указанный сайт
driver.get("http://uitestingplayground.com/textinput")

# Ввод текста в поле
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

# Нажатие на кнопку
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

# Ожидание обновления текста на кнопке
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )

# Вывод текста обновленной кнопки
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(button.text)

# Закрытие браузера
driver.quit()
