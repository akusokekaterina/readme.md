from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()  # Максимизируем окно браузера
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

WebDriverWait(driver, 15).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
)

# Находим третью картинку (индекс 2, так как индексация начинается с 0)
third_image = driver.find_elements(By.TAG_NAME, "img")[2]

# Получаем значение атрибута src
src_value = third_image.get_attribute("src")

print(src_value)
# Закрываем браузер
driver.quit()
