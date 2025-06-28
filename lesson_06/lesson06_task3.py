from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()  # Максимизируем окно браузера

# Переход на указанный сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидаем, пока все изображения загрузятся (проверка по тегу img)
WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)

# Находим третью картинку (индекс 2, так как индексация начинается с 0)
third_image = driver.find_elements(By.TAG_NAME, "img")[2]

# Получаем значение атрибута src
src_value = third_image.get_attribute("src")

# Выводим значение в консоль
print(src_value)

# Закрываем браузер
driver.quit()